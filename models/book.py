# -*- coding: utf-8 -*-

from odoo import fields, models, api, exceptions


class Book(models.Model):
    _name = 'mylib.book'
    _description = 'My library books'

    name = fields.Char("Tên sách")
    code = fields.Char("Mã sách")
    year = fields.Integer("Năm xuất bản")
    category = fields.Many2many('mylib.category', string="Danh mục sách")
    author = fields.Many2many('mylib.author', string="Tác giả")
    description = fields.Text("Mô tả sách")
    image = fields.Binary("Ảnh bìa")
    amount = fields.Integer("Số lượng")
    state = fields.Selection(
        [('con', 'Còn sách'), ('saphet', 'Sắp hết'), ('het', 'Hết sách')], "Trạng thái")

    _sql_constraints = [
        ('unique_code', 'unique(code)', u'Mã sách đã tồn tại, hãy thử lại!'),
        ('unique_name', 'unique(name)', u'Tên sách đã tồn tại, hãy thử lại!'),
    ]

    @api.constrains("code")
    def _code_validate(self):
        for book in self:
            if len(book.code) < 4:
                raise exceptions.ValidationError(u"Mã sách quá ngắn!")

    @api.constrains("amount")
    def _amount_validate(self):
        for book in self:
            if book.amount < 0:
                raise exceptions.ValidationError(u"Số lượng không thể ít hơn được nữa!")

    @api.onchange("amount")
    def _amount_onchange(self):
        if self.amount == 0:
            self.state = 'het'
        elif 0 < self.amount < 20:
            self.state = 'saphet'
        else:
            self.state = 'con'
