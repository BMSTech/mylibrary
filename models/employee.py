# -*- coding: utf-8 -*-

from odoo import fields, models, api, exceptions


class Contact(models.Model):
    _name = 'mylib.contact'

    name = fields.Char("Tên")
    phone = fields.Char("Số điện thoại")
    address = fields.Char("Địa chỉ")

    @api.constrains("phone")
    def _phone_validate(self):
        for employee in self:
            if len(employee.phone) < 10:
                raise exceptions.ValidationError(u"Số điện thoại chưa hợp lệ!")


class Employee(models.Model):
    _name = 'mylib.employee'
    _description = 'My library employee'
    _inherit = 'mylib.author'
    _inherits = {'mylib.contact': 'contact'}

    name = fields.Char(related='contact.name', inherited=True)
    gender = fields.Selection([('1', 'Nam'), ('2', 'Nữ')], 'Giới tính')
    description = fields.Char("Ghi chú")
    contact = fields.Many2one('mylib.contact', ondelete='cascade')


