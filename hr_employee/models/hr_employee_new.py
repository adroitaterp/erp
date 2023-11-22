# -*- coding: utf-8 -*-

from odoo import models, fields, api , Command


class HrEmployeeInherit(models.Model):
     _inherit = "hr.employee"
     expire_visa = fields.Date(string="E-visa Expiry")
     insurance_new_no = fields.Char(string="Insurance No")