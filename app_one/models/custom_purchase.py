from odoo import models, fields


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

    purchase_purpose = fields.Char(string='Purchase Purpose')

    def _prepare_invoice(self):
        invoice_vals = super()._prepare_invoice()
        invoice_vals['purchase_purpose'] = self.purchase_purpose
        return invoice_vals

    def _get_invoice_qty(self):
        # OVERRIDE: Always return ordered quantity instead of received
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
