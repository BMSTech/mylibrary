# -*- coding: utf-8 -*-

from odoo import fields, models


class Author(models.Model):
    _name = 'mylib.author'
    _description = 'My library authors'

    name = fields.Char("Tên tác giả")
    image = fields.Binary("Ảnh tác giả")
    nation = fields.Many2one('res.country', 'Quốc gia')
    description = fields.Text("Tiểu sử")