# -*- coding: utf-8 -*-

from odoo import fields, models


class BookLoan(models.Model):
    _name = 'mylib.book.loan'
    _description = 'Book loan'

    name = fields.Char("Mã phiếu mượn")
    user = fields.Many2one("res.partner", "Người mượn")
    date = fields.Datetime("Ngày mượn")
    date_return = fields.Datetime("Ngày hẹn trả")
    is_archive = fields.Boolean("Đã lưu trữ", groups="mylibrary.mylib_manager")
    loan_detail = fields.One2many(
        comodel_name="mylib.book.loan.detail", inverse_name="book_loan", string="Danh sánh mượn")


class BookLoanDetail(models.Model):
    _name = 'mylib.book.loan.detail'
    _description = 'Book loan detail'

    book_loan = fields.Many2one("mylib.book.loan", "Phiếu mượn")
    book = fields.Many2one("mylib.book", "Sách")
    amount = fields.Integer("Số lượng", default=1)
