# -*- coding: utf-8 -*-

from odoo import fields, models, api


class Author(models.Model):
    _name = 'mylib.author'
    _description = 'My library authors'

    name = fields.Char("Tên")
    image = fields.Binary("Ảnh")
    nation = fields.Many2one('res.country', 'Quốc gia')
    description = fields.Text("Tiểu sử")

    @api.model
    def create(self, vals):
        if vals.get('name'):
            vals['name'] = vals.get('name').title()
            self.env['mylib.contact'].create({'name': vals['name']})
        return super(Author, self).create(vals)
