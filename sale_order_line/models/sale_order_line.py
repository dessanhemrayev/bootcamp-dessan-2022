from odoo import api,fields,models
from odoo.tools.profiler import profile


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    line_number = fields.Integer(compute = "_compute_line_number")

    @profile
    @api.depends('order_id.order_line','sequence')
    def _compute_line_number(self):
        order_ids = self.mapped('order_id')
        for order in order_ids:
            count = 1
            for line in order.order_line.sorted(lambda l:l.sequence):
                line.line_number = count
                count += 1
