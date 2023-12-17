# -*- coding: utf-8 -*-

from odoo import models, fields, api , Command


class HrContractInherit(models.Model):
     _inherit = "hr.contract"
     basic_salary = fields.Char(string="Basic Salary")
    
     under_contract_state = fields.Selection([
        ('done', 'Under Contract'),
        ('blocked', 'Not Under Contract')
    ], string='Contractual Status', compute='_compute_under_contract_state')
     contract_id = fields.Many2one('hr.contract', readonly=True)
     contract_ids = fields.One2many('hr.contract', string='Contracts', compute='_compute_contract_ids', readonly=True,      compute_sudo=True)
     date_hired = fields.Date('Hire Date', readonly=True)
     def hr_contract_view_form_new_action(self):
        self.ensure_one()
        action = self.env['ir.actions.actions']._for_xml_id('hr_contract.action_hr_contract')
        action.update({
            'context': {'default_employee_id': self.employee_id.id},
            'view_mode': 'form',
            'view_id': self.env.ref('hr_contract.hr_contract_view_form').id,
            'views': [(self.env.ref('hr_contract.hr_contract_view_form').id, 'form')],
        })
        return action


    
     