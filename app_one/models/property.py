from odoo import models, fields, api

from encodings.punycode import digits
from server.odoo.api import readonly
from server.odoo.exceptions import ValidationError, UserError


class Proparty(models.Model):
    _name = 'property'
    _description = 'Property'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(required=True, default='New')
    property_line_id = fields.One2many('property.line', 'property_id')
    description = fields.Text(tracking=1)
    postcode = fields.Char(required=True, size=8)
    date_available = fields.Date(tracking=1)
    expected_price = fields.Float()
    selling_price = fields.Float()
    diff = fields.Float(compute='_compute_diff', store=1)
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
                                          default='north')
    owner_id = fields.Many2one('owner')
    owner_phone = fields.Char(related='owner_id.phone', readonly=0)
    owner_address = fields.Char(related='owner_id.address', readonly=0)
    tag_id = fields.Many2many('tag')
    status = fields.Selection([
        ('draft', 'Draft'),
        ('pending', 'Pending'),
        ('sold', 'Sold'),
    ], default='draft', tracking=1)

    _sql_constraints = [
        ('unique_name', ('unique("name")'), 'Name already exists!'),
    ]

    @api.depends('selling_price', 'expected_price')
    def _compute_diff(self):
        for rec in self:
            rec.diff = rec.expected_price - rec.selling_price

    @api.onchange('expected_price')
    def _onchange_expected_price(self):
        for rec in self:
            if rec.expected_price < rec.selling_price:
                return {
                    'warning': {'title': 'warning',
                                'message': 'negative value; expected price must be greater than selling price!',
                                'type': 'notification'}
                }

    def action_draft(self):
        for rec in self:
            rec.status = 'draft'

    def action_pending(self):
        print('action_pending')
        for rec in self:
            rec.status = 'pending'

    def action_sold(self):
        for rec in self:
            rec.status = 'sold'

    @api.constrains('bedrooms')
    def check_bedrooms_greater_zero(self):
        for rec in self:
            if rec.bedrooms == 0:
                raise ValidationError('Please add valid number of bedrooms!')

    # @api.model_create_multi
    # def create(self, vals):
    #     res = super(Proparty, self).create(vals)
    #     print('Inside create method')
    #     return res
    #
    # @api.model
    # def _search(self, domain, offset=0, limit=None, order=None, access_rights_uid=None):
    #     res = super(Proparty, self)._search(domain, offset=0, limit=None, order=None, access_rights_uid=None)
    #     print('Inside Search method')
    #     return res
    #
    # def write(self, vals):
    #     res = super(Proparty, self).write(vals)
    #     print('Inside write method')
    #     return res
    #
    # def unlink(self):
    #     res = super(Proparty, self).unlink()
    #     print('Inside unlink method')
    #     return res

    @api.model_create_multi
    def create(self, vals):
        print('Inside create method')
        res = super().create(vals)
        return res

    @api.model
    def _search(self, domain, offset=0, limit=None, order=None, access_rights_uid=None):
        print('Inside search method')
        return super()._search(domain, offset=offset, limit=limit, order=order)

    def write(self, vals):
        print('Inside write method')
        return super().write(vals)

    def unlink(self):
        print('Inside unlink method')
        return super().unlink()


class PropertyLine(models.Model):
    _name = 'property.line'

    property_id = fields.Many2one('property')
    area = fields.Float()
    description = fields.Char()
