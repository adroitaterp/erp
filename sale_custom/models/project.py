# -*- coding: utf-8 -*-

from odoo.exceptions import Warning
from datetime import datetime
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_is_zero, float_compare
import logging
from datetime import datetime




class SaleOrderInherit(models.Model):
    _inherit = 'project.project'
    name = fields.Char(string='Name', required=False, translate=True)

    @api.onchange('partner_id')
    def sale_order_domain(self):
        sale_orders = self.env['sale.order'].search([('partner_id','=',self.partner_id.id)])

        if sale_orders:
            return {'domain': {'sale_order': [('id', 'in', sale_orders.ids),('state','in',['sale','cancel','contract_expired','contract_expired_and_renewed'])]}}
        else:
            return {'domain': {'sale_order': [('id', 'in', [])]}}


    
        
