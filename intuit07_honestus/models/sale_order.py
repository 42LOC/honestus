
from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    honestus_code = fields.Char(string="Honestus code", related="product_id.honestus_code")
    honestus_name = fields.Char(string="Honestus Name", compute="_compute_honestus_name", store=True)

    honestus_price = fields.Float(string="Honestus Price", related="product_id.honestus_price")

    @api.depends("honestus_code")
    def _compute_honestus_name(self):
        for rec in self:
            rec.honestus_name = f"[{rec.honestus_code or rec.product_id.default_code}] {rec.product_id.name}"
