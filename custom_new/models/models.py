# -*- coding: utf-8 -*-

from odoo import models, fields, api



class HrPayrollRep(models.Model):
    _inherit = 'hr.payslip'
    
    house_allowance = fields.Float('House Allowance')
    
    
    transportation_allowance = fields.Float('Transportation Allowance')
    other_allowance = fields.Float('Other Allowance') 


class HrPayslipPivot(models.Model):
    _inherit = "hr.payroll.report"

    house_allowance = fields.Float('House Allowance')
    transportation_allowance = fields.Float('Transportation Allowance')
    other_allowance = fields.Float('Other Allowance') 
    
