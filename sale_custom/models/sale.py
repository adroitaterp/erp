# -*- coding: utf-8 -*-

from odoo.exceptions import Warning
from datetime import datetime
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_is_zero, float_compare


class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

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
        # ('rejected_by_customer', 'Rejected By Customer'),
    ], string='Status', readonly=True, copy=False, index=True, tracking=3, default='to_proposal_approve')

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
            'state': 'sale'
        })

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


class SaleLines(models.Model):
    _inherit = 'sale.order.line'

    term = fields.Selection([('one_time', 'One Time'), ('monthly', 'Monthly'), ('quarterly', 'Quarterly'),
                             ('yearly', 'Yearly'), ('per_item', 'Per Item'), ('free_of_charge', 'Free of Charge')])

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
