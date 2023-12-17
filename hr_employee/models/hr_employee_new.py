# -*- coding: utf-8 -*-

from odoo import models, fields, api , Command


class HrEmployeeInherit(models.Model):
     _inherit = "hr.employee"
     expire_visa = fields.Date(string="E-visa Expiry",track_visibility='always')
     insurance_new_no = fields.Char(string="Insurance No",track_visibility='always')
     new_status = fields.Char(string="Status",track_visibility='always')
     validate_date_from = fields.Date('Validity Date From',track_visibility='always')
     validate_date_to = fields.Date('Validity Date To',track_visibility='always')
     present_address = fields.Char(string="Home Country Address)",track_visibility='always')
     personal_whatsup_no = fields.Char(string="Personal Whatsapp No",track_visibility='always')
     emergency_contact_person_name = fields.Char(string="Emergency Contact Person Name",track_visibility='always')
     emergency_address = fields.Char(string="Emergency Address",track_visibility='always')
     relationship = fields.Char(string="Relationship",track_visibility='always')
     emergency_contact = fields.Char("Emergency Contact Person Name", groups="hr.group_hr_user", tracking=True,track_visibility='always')
     emergency_phone = fields.Char("Emergency Contact No", groups="hr.group_hr_user", tracking=True,track_visibility='always')
     device_name = fields.Char(string="Device Name",track_visibility='always')
     product = fields.Char(string="Product ID",track_visibility='always')
     windows = fields.Char(string="Windows",track_visibility='always')
     accessories = fields.Char(string="Accessories",track_visibility='always')
     ms_office_id = fields.Char(string="MS Office Id",track_visibility='always')
     ms_office_password = fields.Char(string="MS Office Password",track_visibility='always')
     laptop_password = fields.Char(string="Laptop Password",track_visibility='always')
     company_serial_no = fields.Char(string="Company Serial No",track_visibility='always')
     laptop_history = fields.Char(string="Laptop History",track_visibility='always')
     outlook_email_account = fields.Char(string="Outlook Email Account",track_visibility='always')
     country_id = fields.Many2one(
        'res.country', 'Nationality', groups="hr.group_hr_user", tracking=True,track_visibility='always')
     religion = fields.Char(string="Religion",track_visibility='always')
     languange_new = fields.Char(string="Language",track_visibility='always')
     phone_model = fields.Char(string="Phone Model",track_visibility='always')
     serial_number = fields.Char(string="Serial Number",track_visibility='always')
     phone_password = fields.Char(string="Phone Password",track_visibility='always')
     company_serial_no = fields.Char(string="Company Serial No",track_visibility='always')
     phone_history = fields.Char(string="Phone History",track_visibility='always')
     sim_history = fields.Char(string="Sim History",track_visibility='always')
     iphone_cloud = fields.Char(string="Iphone Cloud",track_visibility='always')
     iphone_cloud_password = fields.Char(string="Iphone Cloud Password",track_visibility='always')
     recovery_email = fields.Char(string="Recovery Email",track_visibility='always')
     personal_email = fields.Char(string="Personal Contact No", groups="hr.group_hr_user",track_visibility='always')
     personal_whatsup_no = fields.Char(string="Personal Whatsapp No.", groups="hr.group_hr_user",track_visibility='always')
     uae_address = fields.Char("UAE Address",track_visibility='always')
     bank_name = fields.Char("Bank Name",track_visibility='always')
     bank_account = fields.Char("Bank Account Number",track_visibility='always')
     bank_account_ibn = fields.Char("IBN Number",track_visibility='always')
     marital = fields.Selection([
        ('single', 'Single'),
        ('married', 'Married'),
        ('cohabitant', 'Legal Cohabitant'),
        ('widower', 'Widower'),
        ('divorced', 'Divorced')
    ], string='Marital Status', groups="hr.group_hr_user", default='single', track_visibility='always')
     gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], groups="hr.group_hr_user", track_visibility='always')
     country_of_birth = fields.Many2one('res.country', string="Country of Birth", groups="hr.group_hr_user",  
                                      track_visibility='always')
     name = fields.Char(string="Employee Name", related='resource_id.name', store=True, readonly=False, track_visibility='always')
     category_ids = fields.Many2many(
            'hr.employee.category', 'employee_category_rel',
            'emp_id', 'category_id', groups="hr.group_hr_user",
            string='Tags', track_visibility='always')

   







    






     


