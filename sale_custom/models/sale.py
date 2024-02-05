# -*- coding: utf-8 -*-

from odoo.exceptions import Warning
from datetime import datetime
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_is_zero, float_compare
import logging
from datetime import datetime

import logging
_logger = logging.getLogger(__name__)




class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'
    ref = fields.Char(sring="", copy=False, default=" ", readonly="True")
    prefix_pr = fields.Char('PR Prefix', store=True)
    one_time_job_annual = fields.Selection([('one_time_job', 'One time job contract'), ('annual_contract', 'Annual Contract')], string="One Time Job/Annual",track_visibility='always')

    state = fields.Selection([
        # ('to_proposal_review', 'Waiting For Proposal Review'),
        ('to_proposal_approve', 'Waiting For Management Proposal Approval'),
        ('waiting_for_customer_approval', 'Waiting For Customer Proposal Approval'),
        ('customer_rejected', 'Proposal Rejected By Customer'),
        ('draft', 'Proposal'),
        ('sent', 'Proposal Sent'),
        # ('to_contract_review', 'Waiting For Contract Review'),
        ('to_contract_approve', 'Waiting For Management Contract Approval'),
        ('waiting_customer_contract_approval', 'Waiting For Customer Contract Approval'),
        ('sale', 'Contract'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled'),
        ('rejected', 'Rejected'),
        ('customer_contract_rejected', 'Customer Contract Rejected'),
        ('contract_expired', 'Contract Expired'), ('one_time_job_done', 'One Time Job Done'),
        # ('contract_expiredand Renewed', 'Contract Expired')
         ('contract_expired_and_renewed', 'Contract Expired And Renewed'),
    ], string='Status', readonly=True, copy=False, index=True, tracking=3, default='to_proposal_approve')

    sale_ids = fields.One2many('sale.order.line', 'sale_order_line_id', )
    term = fields.Char(string="Term")
    services = fields.Char(string="Services")

    percentage = fields.Char(string="Fee for each service")

    
   
    



    @api.onchange('order_line')
    def _onchange_order_line_term(self):
        term_list = []
        service_list = []
        percentage_list = []
    
        for line in self.order_line:
            if line.term:
                term_list.append(line.term)
    
            if line.product_id.name:
                product_name_parts = line.product_id.name.split('(')
                if len(product_name_parts) == 2:
                    service_list.append(product_name_parts[0])
                    percentage_list.append(product_name_parts[1].strip())  # Remove leading/trailing whitespaces
    
        self.term = ', '.join(term_list)
        self.services = ', '.join(service_list)
        self.percentage = ', '.join(percentage_list)


    until_completion = fields.Boolean('Until Completion')
    scope_of_work = fields.Text(string='Customer Note')
    employee_id = fields.Many2one('hr.employee', string='Employee')
    auth_sign_id = fields.Many2one('hr.employee', string='Authorised Signatory')
    term_of_contract = fields.Text(string='Term of Contract')
    license_no = fields.Char(string='License No')
    start_date = fields.Date('Start Date')
    end_date = fields.Date('End Date')
    payment_terms_note = fields.Text(string='Payment Terms Note')
    termination_days = fields.Integer('Termination Days')
    payment_details = fields.Text('Payment Details')
    contact_id = fields.Many2one('res.partner', string='Contact')
    estimation_id = fields.Many2one('job.estimate')

    sale_description_lines = fields.One2many('sale.description', 'order_id')

    contact_ids = fields.Many2many('res.partner', string='Contacts', compute='compute_contact_ids')





    days=fields.Char("Days")
    days_int=fields.Integer("Dayssss")

    # @api.onchange('start_date','end_date')
    # def calculatedays(self):
    #     if self.start_date and self.end_date:
    #         days=(self.end_date-self.start_date).days
    #         self.days_int = days
    #         self.days=str(days)+" days"

    contract_expired = fields.Boolean(string='Contract Expired', compute='_compute_contract_expired',store=True)
    
    def _compute_function_name(self):
        all=self.env['sale.order'].search([])
        for rec in all:
            if rec.start_date and rec.end_date:
                days = (rec.end_date - datetime.now().date()).days
                rec.days_int = days
                rec.days = f"{days} days"
            if rec.end_date and rec.end_date < datetime.now().date():
                rec.contract_expired = True
                rec.days = "Contract Expired"
            else:
                rec.contract_expired = False
            

    @api.onchange('end_date')
    def calculatedays(self):
        if self.start_date and self.end_date:
            days = (self.end_date - datetime.now().date()).days
            self.days_int = days
            self.days = f"{days} days"

    @api.depends('end_date')
    def _compute_contract_expired(self):
        for record in self:
            if record.end_date and record.end_date < datetime.now().date():
                record.contract_expired = True
                record.days = "Contract Expired"
            else:
                record.contract_expired = False
    

    @api.depends('contact_id')
    def compute_contact_ids(self):
        # contacts = self.env['res.partner'].search([('is_eng', '=', True)])
        for rec in self:
            contacts = rec.partner_id.child_ids.ids
        self.contact_ids = contacts

    @api.model
    def create(self, vals):
        res = super(SaleOrderInherit, self).create(vals)
        lines = []
        for r in res.order_line:
            
            vals = {
                'order_id': res.id,
                'product_id': r.product_id.id,
                'name': r.product_id.description,
            }
            lines.append(vals)
        result = self.env['sale.description'].create(lines)
       
        a = 2
        if res.prefix_pr:
            res.ref = (res.prefix_pr, res.id)
        else:
            res.ref = 'IR-00%s' % (res.id)
   
        return res

    def write(self, vals):
        res = super(SaleOrderInherit, self).write(vals)
        for rec in self:
            result = self.env['sale.order'].browse(self.env.context.get('active_ids'))
            print(result)
            lines = []
            sale_description = []
            for i in rec.sale_description_lines:
                sale_description.append(i.product_id.id)
            for r in rec.order_line:
                print(r)
                if r.product_id.id not in sale_description:
                    values = {
                        'order_id': self.id,
                        'product_id': r.product_id.id,
                        'name': r.product_id.description,
                    }
                    lines.append(values)
            print(lines)
            result = self.env['sale.description'].create(lines)
        return res

    # @api.onchange('order_line')
    # def compute_sale_desc(self):
    #     for rec in self.order_line:
    #         rec.order_id.sale_description_lines.product_id = rec.product_id.id

    # def button_proposal_review(self):
    #     self.write({
    #         'state': 'to_proposal_approve'
    #     })

    def button_proposal_approve(self):
        self.write({
            'state': 'waiting_for_customer_approval'
        })

    def button_customer_approve(self):
        self.write({
            'state': 'draft'
        })

    def button_customer_rejected(self):
        self.write({
            'state': 'customer_rejected'
        })

    # def button_proposal_review_reject(self):
    #     self.write({
    #         'state': 'rejected'
    #     })

    def button_proposal_approve_reject(self):
        self.write({
            'state': 'rejected'
        })

    def action_confirm(self):
        self.write({
            'state': 'to_contract_approve'
        })

    def button_contract_approve(self):
        self.write({
            'state': 'waiting_customer_contract_approval'
        })

    def button_customer_contract_approve(self):
        self.write({
            'state': 'sale',
        })
        for rec,s_work in zip(self.order_line,self.sale_description_lines):   
            name=rec.product_template_id.name
            description=rec.name
            product_objs = []
            # for obj in objs:
            product_data = {
                'product_id': s_work.product_id.id,
                'name': s_work.name,
            }
            product_objs.append((0, 0, product_data))   
            self.env['project.project'].create({        
                'name':name,
                'sale_order': self.id,
                'description':description,
                'partner_id': self.partner_id.id,
                'created_date':self.date_order,
                'date_start': self.start_date,
                'date': self.end_date,
                'until_completion': self.until_completion,
                'product_ids':product_objs
                
            })
         
        return

    

    


    def button_customer_contract_reject(self):
        self.write({
            'state': 'customer_contract_rejected'
        })

    # def button_customer_approve(self):
    #     rec = super(SaleOrderInherit, self).action_confirm()
    #     self.write({'state': 'sale'})

    # def button_customer_reject(self):
    #     self.write({'state': 'rejected_by_customer'})

    def button_contract_approve_reject(self):
        self.write({
            'state': 'rejected'
        })

    def button_contract_expired(self):
        self.write({
            'state': 'contract_expired'
        })

    def button_one_time_job_done(self):
        self.write({
            'state': 'one_time_job_done'
        })

    project = fields.Integer(string="Project",compute='_count_project')
    # project_count = fields.Char(string="Project")

    @api.depends('state')
    def _count_project(self):
        # if self.state == 'sale':
        count=self.env['project.project'].search_count([('sale_order','=',self.id)])
        self.project=count


   
   
    def get_project(self):
        self.ensure_one()
        
        action= {
            'type': 'ir.actions.act_window',
            'name': 'project.project',
            'view_mode': 'tree,form',
            'res_model': 'project.project',
            'domain': [('sale_order', '=', self.name)],
        }
        if self.state in ['cancel','contract_expired','contract_expired_and_renewed']:
            action['context']={'edit':False}
            all=self.env['project.project'].search([('sale_order','=',self.name)])
            stage=self.env['project.project.stage'].search([('name','=','Cancelled')])
            for a in all:
                a.stage_id=stage.id
        return action

    







    


class SaleLines(models.Model):
    _inherit = 'sale.order.line'
    
    product_id = fields.Many2one(
        comodel_name='product.product',
        string="Service",
        change_default=True, ondelete='restrict', check_company=True, index='btree_not_null',
        domain="[('sale_ok', '=', True), '|', ('company_id', '=', False), ('company_id', '=', company_id)]")

    term = fields.Selection([('one_time', 'One Time'), ('monthly', 'Monthly'), ('quarterly', 'Quarterly'),
                             ('yearly', 'Per Year'), ('per_item', 'Per Item'), ('free_of_charge', 'Free of Charge')])
    sale_order_line_id = fields.Many2one('sale.order', string="Measurment")
    

    # def write(self, values):
    #     if 'product_id' in values:
    #         record = self.env['sale.description'].search([('product_id', '=', self.product_id.id),('order_id', '=', self.order_id.id)])
    #         print("ggggggggggggggggggggggggg" , record)
    #         for r in record:
    #             r.update({
    #                 'product_id': values['product_id']
    #             })
    #
    #     res = super(SaleLines, self).write(values)
    #     return res


class SaleNameLines(models.Model):
    _name = 'sale.description'
    _description = 'Sale Description'
    _rec_name = 'product_id'

    order_id = fields.Many2one('sale.order')
    product_id = fields.Many2one('product.product', string='Product')
    name = fields.Html('Description')
    # name = fields.Text('Description')
    #name = fields.Text('Description' , related='product_id.description')
