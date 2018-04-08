# -*- coding: utf-8 -*-

from odoo import fields, models


class TestDomain(models.Model):
    _name = 'test.domain'
    _description = 'domain test'
    _rec_name = 'book'

    book = fields.Many2one("mylib.book", 'Sách của tôi',
                           domain="[('year', '<', 2000), '!' ,('state', '=', 'con')]"
                           )
