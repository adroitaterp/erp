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
