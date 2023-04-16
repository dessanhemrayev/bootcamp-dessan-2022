from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    line_number = fields.Integer(compute="_compute_line_number", store=True)

    tag_ids = fields.Many2many("sale.order.line.tag")

    # @profile
    @api.depends("order_id.order_line", "sequence")
    def _compute_line_number(self):
        order_ids = self.mapped("order_id")
        for order in order_ids:
            count = 1
            for line in order.order_line.sorted(lambda l: l.sequence):
                line.line_number = count
                count += 1


class SaleOrderLineTag(models.Model):
    _name = "sale.order.line.tag"
    _description = "Sale order line tags"

    name = fields.Char(required=True)
    color = fields.Integer()
