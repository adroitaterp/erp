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




class SaleOrderInheritNew(models.Model):
    _inherit = 'sale.order'
    def butto_expire_and_renew(self):
        
        self.write({
            'state': 'contract_expired_and_renewed'
        })
