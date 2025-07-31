from odoo import fields, models, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    purchase_purpose = fields.Char(string='Purchase Purpose')