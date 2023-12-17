# -*- coding: utf-8 -*-

from odoo import models, fields, api , Command


class HrEmployeeInherit(models.Model):
     _inherit = "hr.employee"
     date_of_joining = fields.Date('Date of Joining',track_visibility='always')
     end_date_of_probationary = fields.Date('End Date of Probationary',track_visibility='always')
     date_of_regularization = fields.Date('Date of Regularization', track_visibility='always')
     end_date = fields.Date('End Date',track_visibility='always')
     visa_company_name = fields.Selection([
        ('alliance_prime', 'Alliance Prime'),('adroit_bM', 'Adroit BM'),
     ('adroit_artisan','Adroit Artisan'),('vyora','Vyora')
     ],default='', string='Visa Company Name',track_visibility='always')
     visa_title = fields.Char(string="Visa Title",track_visibility='always')
     Online_Offer_letter = fields.Char(string="Online Offer Letter No",track_visibility='always')
     visa_no = fields.Char(string="E-visa No",track_visibility='always')   
     visa_change_status_no = fields.Char(string="Visa Change Status No",track_visibility='always')
     labour_contract_no = fields.Char(string="Labour Contract No",track_visibility='always')
     labour_card_no = fields.Char(string="Labour Card No",track_visibility='always')
     labour_card_expiry = fields.Date('Labour Card Expiry',track_visibility='always')
     passport = fields.Selection([
        ('company', 'Company'),('him_her_self', 'Him/Her self'),],
        default='', string='Passport With', track_visibility='always')
     passport_number = fields.Char(string="Passport Number",track_visibility='always')
     passport_expiration_date = fields.Date('Passport Expiration',track_visibility='always')
     employment_visa_no = fields.Char(string="Employment Visa No",track_visibility='always')
     employment_visa_start_date = fields.Date('Employment Visa Start Date',track_visibility='always')
     employment_visa_end_date = fields.Date('Employment Visa End Date',track_visibility='always')
     emirates_id_no = fields.Char(string="Emirates ID No",track_visibility='always')
     emirates_id_expiration = fields.Date('Emirates ID Expiration',track_visibility='always')
     expire_visa = fields.Date('E-visa Expiry',track_visibility='always')
     insurance_new_no = fields.Char(string="Insurance No",track_visibility='always')
     visa_title = fields.Char(string="Visa Title",track_visibility='always')
     labour_card_no = fields.Char(string="Labour Card No",track_visibility='always')
     labour_card_expiry = fields.Date('Labour Card Expiry',track_visibility='always')
     # work_permit_no = fields.Char(string="Work Permit No")   
     health_insurance_number = fields.Integer('Health Insurance Number',track_visibility='always')
     health_insurance_expiry = fields.Date('Health Insurance Expiry',track_visibility='always')
     religion = fields.Char(string="Religion",track_visibility='always')
     personal_email_address = fields.Char("Personal Email Address",track_visibility='always')
     personal_contact_no = fields.Char(string='Personal Contact No',track_visibility='always')
     personal_whatsapp_no = fields.Char("Personal Whatsapp No",track_visibility='always')
     attachment_ids = fields.Many2many(comodel_name='ir.attachment', string='Attachments', tracking=True,track_visibility='always')
     cv_attachment_ids = fields.Many2many(comodel_name='ir.attachment',relation='employee_cv_attachment_rel', string='Attachments',   tracking=True,track_visibility='always')
     passport_attachment_ids = fields.Many2many(comodel_name='ir.attachment',relation='passport_attachment_rel', string='Attachments', tracking=True,track_visibility='always')
     insurance_attachment_ids = fields.Many2many(comodel_name='ir.attachment',relation='insurance_attachment_rel', string='Attachments', tracking=True,track_visibility='always')
     emirates_attachment_ids = fields.Many2many(comodel_name='ir.attachment',relation='emirates_attachment_rel', string='Attachments', tracking=True,track_visibility='always')
     residence_attachment_ids = fields.Many2many(comodel_name='ir.attachment',relation='residence_attachment_rel', string='Attachments', tracking=True,track_visibility='always')
     original_p_attachment_ids = fields.Many2many(comodel_name='ir.attachment',relation='original_p_attachment_rel', string='Attachments', tracking=True,track_visibility='always')
     e_visa_attachment_ids = fields.Many2many(comodel_name='ir.attachment',relation='e_visa_attachment_rel', string='Attachments', tracking=True,track_visibility='always')
     insurance_attachment_ids = fields.Many2many(comodel_name='ir.attachment',relation='insurance_attachment_rel', string='Attachments', tracking=True,track_visibility='always')
     labour_attachment_ids = fields.Many2many(comodel_name='ir.attachment',relation='labour_attachment_rel', string='Attachments', tracking=True,track_visibility='always')
     medical_attachment_ids = fields.Many2many(comodel_name='ir.attachment',relation='medical_attachment_rel', string='Attachments', tracking=True,track_visibility='always')
     visa_c_attachment_ids = fields.Many2many(comodel_name='ir.attachment',relation='visa_c_attachment_rel', string='Attachments', tracking=True,track_visibility='always')
     
     s_labour_attachment_ids = fields.Many2many(comodel_name='ir.attachment',relation='s_labour_attachment_rel', string='Attachments', tracking=True,track_visibility='always')
     s_online_attachment_ids = fields.Many2many(comodel_name='ir.attachment',relation='s_online_attachment_rel', string='Attachments', tracking=True,track_visibility='always')
     s_offer_attachment_ids = fields.Many2many(comodel_name='ir.attachment',relation='s_offer_attachment_rel', string='Attachments', tracking=True,track_visibility='always')
     passport_u_attachment_ids = fields.Many2many(comodel_name='ir.attachment',relation='passport_u_attachment_rel', string='Attachments', tracking=True,track_visibility='always')
     employee_e_attachment_ids = fields.Many2many(comodel_name='ir.attachment',relation='employee_e_attachment_rel', string='Attachments', tracking=True,track_visibility='always')
     ndis_conf_attachment_ids = fields.Many2many(comodel_name='ir.attachment',relation='ndis_conf_attachment_rel', string='Attachments', tracking=True,track_visibility='always')
    
     staf_f_attachment_ids = fields.Many2many(comodel_name='ir.attachment',relation='staf_f_attachment_rel', string='Attachments', tracking=True,track_visibility='always')
     t_c_attachment_ids = fields.Many2many(comodel_name='ir.attachment',relation='t_c_attachment_rel', string='Attachments', tracking=True,track_visibility='always')
     visit_v_attachment_ids = fields.Many2many(comodel_name='ir.attachment',relation='visit_v_attachment_rel', string='Attachments', tracking=True,track_visibility='always')
     h_country_attachment_ids = fields.Many2many(comodel_name='ir.attachment',relation='h_country_attachment_rel', string='Attachments', tracking=True,track_visibility='always')
     attested_e_attachment_ids = fields.Many2many(comodel_name='ir.attachment',relation='attested_e_attachment_rel', string='Attachments', tracking=True,track_visibility='always')
     previous_e_attachment_ids = fields.Many2many(comodel_name='ir.attachment',relation='previous_e_attachment_rel', string='Attachments', tracking=True,track_visibility='always')
     other_attachment_ids = fields.Many2many(comodel_name='ir.attachment',relation='other_attachment_rel', string='Attachments', tracking=True,track_visibility='always')

     category_ids = fields.Many2many(
        'hr.employee.category', 'employee_category_rel',
        'emp_id', 'category_id', groups="hr.group_hr_manager",
        string='Tags',track_visibility='always')


class HrEmployeeBaseInherit(models.AbstractModel):
    _inherit = "hr.employee.base"
    

    job_title = fields.Char("Job Title", compute="_compute_job_title", store=True, readonly=False,track_visibility='always')
    work_phone = fields.Char('Work Phone', compute="_compute_phones", store=True, readonly=False,track_visibility='always')
    mobile_phone = fields.Char('Work Mobile',track_visibility='always')
    work_email = fields.Char('Work Email',track_visibility='always')
    job_id = fields.Many2one('hr.job', 'Job Position', domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]")
    address_id = fields.Many2one('res.partner', 'Work Address', compute="_compute_address_id", store=True, readonly=False,
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]")
    company_id = fields.Many2one('res.company', 'Company')
    department_id = fields.Many2one('hr.department', 'Department', domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]",track_visibility='always')


    @api.depends('job_id')
    def _compute_job_title(self):
        for employee in self.filtered('job_id'):
            employee.job_title = employee.job_id.name


    @api.depends('address_id')
    def _compute_phones(self):
        for employee in self:
            if employee.address_id and employee.address_id.phone:
                employee.work_phone = employee.address_id.phone
            else:
                employee.work_phone = False

    @api.depends('company_id')
    def _compute_address_id(self):
        for employee in self:
            address = employee.company_id.partner_id.address_get(['default'])
            employee.address_id = address['default'] if address else False
    

