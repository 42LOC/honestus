
from odoo import api, fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    honestus_code = fields.Char(string="Honestus Code")

    honestus_price = fields.Float(string="Honestus Price")
