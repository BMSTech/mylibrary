# -*- coding: utf-8 -*-

from odoo import fields, models


class Partner(models.Model):
    _inherit = 'res.partner'

    is_blacklist = fields.Boolean('Thuộc danh sách đen')
    fax = fields.Char(default="00000000", required=True)