from odoo import fields, models, api


class PurchaseCategory(models.Model):
    _name = 'purchase.category'
    _description = 'Purchase Category'

    name = fields.Char()
    description = fields.Char()
    categories = fields.Selection([('category1','Category1'),('category2','Category2')],default='category1')
