# -*- coding: utf-8 -*-

from odoo import models, fields, api , Command


class HrEmployeeInherit(models.Model):
     _inherit = "hr.employee"
     date_of_joining = fields.Date('Date of Joining')
     passport = fields.Selection([
        ('company', 'Company'),('him_her_self', 'Him/Her self'),],
        default='', string='Passport With', track_visibility='always')
     passport_number = fields.Char(string="Passport Number")
     passport_expiration_date = fields.Date('Passport Expiration')
     Online_Offer_letter = fields.Char(string="Online Offer Letter No")
     visa_change_status_no = fields.Char(string="Visa Change Status No")
     visa_title = fields.Char(string="Visa Title")
     labour_card_no = fields.Char(string="Labour Card No")
     labour_card_expiry = fields.Date('Labour Card Expiry')
     labour_contract_no = fields.Char(string="Labour Contract No")
     work_permit_no = fields.Char(string="Work Permit No")
     employment_visa_no = fields.Char(string="Employment Visa No")
     employment_visa_start_date = fields.Date('Employment Visa Start Date')
     employment_visa_end_date = fields.Date('Employment Visa End Date')
     emirates_id_no = fields.Char(string="Emirates ID No")
     emirates_id_expiration = fields.Date('Emirates ID Expiration')
     health_insurance_number = fields.Integer('Health Insurance Number')
     health_insurance_expiry = fields.Date('Health Insurance Expiry')

     def _name_search(self, name='passport', args=None, operator='ilike', limit=100, name_get_uid=None):
        args = args or []
        domain= []
        if name:
            args += [('passport', operator, name)]
        return self._search(args, limit=limit)



     religion = fields.Char(string="Religion")
     personal_email_address = fields.Char("Personal Email Address")
     personal_contact_no = fields.Char(string='Personal Contact No')
     personal_whatsapp_no = fields.Char("Personal Whatsapp No")

     attachment_ids = fields.Many2many(comodel_name='ir.attachment', string='Attachments', tracking=True)

     
     

    

