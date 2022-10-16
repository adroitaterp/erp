# -*- coding: utf-8 -*-

from odoo.exceptions import Warning
from datetime import datetime
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_is_zero, float_compare


class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    state = fields.Selection([
        ('to_proposal_review', 'Waiting For Proposal Review'),
        ('to_proposal_approve', 'Waiting For Proposal Approval'),
        ('draft', 'Proposal'),
        ('sent', 'Proposal Sent'),
        ('to_contract_review', 'Waiting For Contract Review'),
        ('to_contract_approve', 'Waiting For Contract Approval'),
        ('sale', 'Contract'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled'),
        ('rejected', 'Rejected'),
    ], string='Status', readonly=True, copy=False, index=True, tracking=3, default='to_proposal_review')

    scope_of_work = fields.Text(string='Customer Note')
    employee_id = fields.Many2one('hr.employee', string='Employee')
    auth_sign_id = fields.Many2one('hr.employee', string='Authorised Signatory')
    term_of_contract = fields.Text(string='Term of Contract')
    license_no = fields.Char(string='License No')

    def button_proposal_review(self):
        self.write({
            'state': 'to_proposal_approve'
        })

    def button_proposal_approve(self):
        self.write({
            'state': 'draft'
        })

    def button_proposal_review_reject(self):
        self.write({
            'state': 'rejected'
        })

    def button_proposal_approve_reject(self):
        self.write({
            'state': 'rejected'
        })



