from odoo import models, fields, api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    state = fields.Selection([
        ('draft', 'Draft'),
        ('manager_approval', 'Manager Approval'),
        ('finance_approval', 'Finance Approval'),
        ('approved', 'Approved'),
        ('sent', 'RFQ Sent'),
        ('to approve', 'To Approve'),
        ('purchase', 'Purchase Order'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled')
    ], string='state', readonly=True, index=True, copy=False, default='draft', tracking=True)
    urgency_level = fields.Selection(
        [('low', 'Low'), ('medium', 'Medium'), ('high', 'High')],
        string='Urgency Level',
        default='low'
    )

    purchase_purpose = fields.Char(string='Purchase Purpose')

    vendor_bill_ids = fields.One2many(
        comodel_name='account.move',
        string='Vendor Bills',
        compute='_compute_vendor_bill_ids',
    )
    vendor_bill_count = fields.Integer(
        string='Vendor Bill Count',
        compute='_compute_vendor_bill_ids'
    )

    total_product_qty = fields.Float(
        string="Total Product Quantity",
        compute='_compute_total_product_qty',
    )

    note_based_on_qty = fields.Char(
        string="Size Note"
    )

    @api.depends('order_line.product_qty')
    def _compute_total_product_qty(self):
        for order in self:
            order.total_product_qty = sum(line.product_qty for line in order.order_line)

    @api.onchange('total_product_qty')
    def _onchange_total_product_qty(self):
        for order in self:
            if order.total_product_qty > 100:
                order.note_based_on_qty = "Large Order"
            elif 50 <= order.total_product_qty <= 100:
                order.note_based_on_qty = "Medium Order"
            else:
                order.note_based_on_qty = "Small Order"

    @api.depends('order_line.invoice_lines.move_id', 'order_line.invoice_lines.move_id.move_type')
    def _compute_vendor_bill_ids(self):
        for order in self:
            print('orders:', order.order_line.invoice_lines.move_id)
            moves = order.order_line.mapped('invoice_lines.move_id').filtered(
                lambda m: m.move_type == 'in_invoice'
            )
            order.vendor_bill_ids = moves
            print(moves)
            order.vendor_bill_count = len(moves)

    def action_view_vendor_bills(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Vendor Bills',
            'res_model': 'account.move',
            'view_mode': 'list,form',
            'domain': [('id', 'in', self.vendor_bill_ids.ids)],
            'context': {'create': False}
        }

    # def action_view_vendor_bills(self):
    #     return {
    #         'type': 'ir.actions.act_window',
    #         'name': 'Vendor Bills',
    #         'view_mode': 'list,form',
    #         'res_model': 'account.move',
    #         'domain': [('purchase_id', '=', self.id), ('move_type', '=', 'in_invoice')],
    #         'context': {'default_purchase_id': self.id},
    #     }

    def action_urgency_level(self):
        for urgent in self:
            print('urgencies:', urgent.urgency_level)
            urgent.urgency_level = 'high'

    def _prepare_invoice(self):
        invoice_val = super()._prepare_invoice()
        invoice_val['purchase_purpose'] = self.purchase_purpose
        invoice_val['purchase_id'] = self.id
        return invoice_val

    def _get_invoice_qty(self):
        return self.product_qty

    def action_rfq_send(self):
        print('inside action_rfq_send', self.state)
        for rec in self:
            rec.state = 'sent'

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

    def action_manager_approve(self):
        for rec in self:
            rec.state = 'manager_approval'

    def action_finance_approve(self):
        for rec in self:
            rec.state = 'finance_approval'

    def action_approved(self):
        for rec in self:
            rec.state = 'approved'

    # def action_post(self):
    #     res = super().action_post()
    #     print('inside action_post method')
    #     return res
