# -*- coding: utf-8 -*-

from odoo.exceptions import Warning
from datetime import datetime
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_is_zero, float_compare


class ResPartnerInh(models.Model):
    _inherit = 'res.partner'

    license_no = fields.Char(string='License No')

    def action_view_sale_order(self):
        pass