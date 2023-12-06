# -*- coding: utf-8 -*-

from odoo import models, fields, api , Command


class HrEmployeeInherit(models.Model):
     _inherit = "hr.employee"
     expire_visa = fields.Date(string="E-visa Expiry")
     insurance_new_no = fields.Char(string="Insurance No")
     new_status = fields.Char(string="Status")
     validate_date_from = fields.Date('Validity Date From')
     validate_date_to = fields.Date('Validity Date To')
     present_address = fields.Char(string="Present Address")
     personal_whatsup_no = fields.Char(string="Personal Whatsapp No")
     emergency_contact_person_name = fields.Char(string="Emergency Contact Person Name")
     emergency_address = fields.Char(string="Emergency Address")
     relationship = fields.Char(string="Relationship")


