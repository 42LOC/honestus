
from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    def create(self, vals):
        res = super(ResPartner, self).create(vals)
        mobile = self.env.context.get("mobile_phone") if self.env.context.get("mobile_phone") else False
        res.mobile = mobile
        return res
