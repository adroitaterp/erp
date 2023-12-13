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
     emergency_contact = fields.Char("Emergency Contact Person Name", groups="hr.group_hr_user", tracking=True)
     emergency_phone = fields.Char("Emergency Contact No", groups="hr.group_hr_user", tracking=True)
     device_name = fields.Char(string="Device Name")
     product = fields.Char(string="Product ID")
     windows = fields.Char(string="Windows")
     accessories = fields.Char(string="Accessories")
     ms_office_id = fields.Char(string="MS Office Id")
     ms_office_password = fields.Char(string="MS Office Password")
     laptop_password = fields.Char(string="Laptop Password")
     company_serial_no = fields.Char(string="Company Serial No")
     laptop_password = fields.Char(string="Laptop Password")
     laptop_history = fields.Char(string="Laptop History")
     outlook_email_account = fields.Char(string="Outlook Email Account")
     country_id = fields.Many2one(
        'res.country', 'Nationality', groups="hr.group_hr_user", tracking=True)
     religion = fields.Char(string="Religion")
     languange_new = fields.Char(string="Language")
     phone_model = fields.Char(string="Phone Model")
     serial_number = fields.Char(string="Serial Number")
     phone_password = fields.Char(string="Phone Password")
     company_serial_no = fields.Char(string="Company Serial No")
     phone_history = fields.Char(string="Phone History")
     sim_history = fields.Char(string="Sim History")
     iphone_cloud = fields.Char(string="Iphone Cloud")
     iphone_cloud_password = fields.Char(string="Iphone Cloud Password")
     recovery_email = fields.Char(string="Recovery Email")
     personal_email = fields.Char(string="Personal Contact No", groups="hr.group_hr_user")
     personal_whatsup_no = fields.Char(string="Personal Whatsapp No.", groups="hr.group_hr_user")







     


