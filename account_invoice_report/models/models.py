# -*- coding: utf-8 -*-

from odoo import models, fields, api , Command


class AccountMoveInherit(models.Model):
     _inherit = "account.move"
     reference = fields.Char(string="Reference")

    


