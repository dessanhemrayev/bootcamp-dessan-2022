from odoo import api,fields,model


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    line_number = fields.Integer()