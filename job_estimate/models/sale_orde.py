# -*- coding: utf-8 -*-
from odoo import models, fields, api

class InheritSaleOrder(models.Model):
    _inherit = 'sale.order'

    estimation_id = fields.Many2one(comodel_name='job.estimation')