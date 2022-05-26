
from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    honestus_code = fields.Char(string="Honestus code", related="product_id.honestus_code")
    honestus_product_default_code = fields.Char(string="Product Code", related="product_id.default_code", store=True)
    honestus_name = fields.Char(string="Honestus Name", compute="_compute_honestus_name", store=True)

    honestus_price = fields.Float(string="Honestus Price", related="product_id.honestus_price", store=True)
    honestus_margin = fields.Float(string="Margin", compute="_compute_margin", store=True)

    @api.depends("honestus_code", "product_id")
    def _compute_honestus_name(self):
        for rec in self:
            rec.honestus_name = f"[{rec.honestus_code or rec.product_id.default_code}] {rec.product_id.name}"


    @api.depends("honestus_price", "price_unit", "product_id", "product_id.standard_price")
    def _compute_margin(self):
        for rec in self:
            price = rec.honestus_price if rec.honestus_price else rec.price_unit
            rec.honestus_margin = (price - rec.product_id.standard_price) / price
