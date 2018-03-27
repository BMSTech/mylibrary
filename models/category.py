# -*- coding: utf-8 -*-

from odoo import fields, models


class Category(models.Model):
    _name = 'mylib.category'
    _description = 'My library categories'

    name = fields.Char("Tên danh mục")
    parent_category = fields.Many2one('mylib.category', 'Danh mục cha')
    description = fields.Text("Mô tả")

    _sql_constraints = [
        ('unique_name', 'unique(name)', u'Tên danh mục đã tồn tại, hãy thử lại!'),
    ]