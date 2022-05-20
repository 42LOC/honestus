
from odoo import api, fields, models


class ResUsers(models.Model):
    _inherit = "res.users"

    mobile_phone = fields.Char(string="Mobile")

    def create(self, vals):
        mobile = vals.get("mobile_phone") if vals else False
        self.env.context = dict(self.env.context)
        self.env.context.update({
            'mobile_phone': mobile,
        })
        return super(ResUsers, self).create(vals)
