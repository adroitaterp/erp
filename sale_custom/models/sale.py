# -*- coding: utf-8 -*-

from odoo.exceptions import Warning
from datetime import datetime
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_is_zero, float_compare


class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    state = fields.Selection([
        ('to_review', 'Waiting For Review'),
        ('approve', 'Waiting For Approval'),
        ('draft', 'Quotation'),
        ('sent', 'Quotation Sent'),
        ('sale', 'Sales Order'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled'),
        ('rejected', 'Rejected'),
    ], string='Status', readonly=True, copy=False, index=True, tracking=3, default='to_review')

    scope_of_work = fields.Text(string='Customer Note')
    employee_id = fields.Many2one('hr.employee', string='Employee')
    auth_sign_id = fields.Many2one('hr.employee', string='Authorised Signatory')
    term_of_contract = fields.Text(string='Term of Contract')
    license_no = fields.Char(string='License No')

    def button_review(self):
        self.write({
            'state': 'approve'
        })

    def button_approve(self):
        self.write({
            'state': 'draft'
        })

    def button_review_reject(self):
        self.write({
            'state': 'rejected'
        })

    def button_approve_reject(self):
        self.write({
            'state': 'rejected'
        })



