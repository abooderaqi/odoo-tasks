from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = 'account.move'

    property_id = fields.Many2one("property", 'Property')

    def action_post(self):
        res = super().action_post()
        print('inside action_post method')
        return res
