from odoo import models ,fields ,api

class inhert(models.Model):
    _inherit = 'sale.order'

    new_field = fields.Char(string='New Field')
