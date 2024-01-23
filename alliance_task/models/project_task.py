# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProjectTaskInherit(models.Model):
    _inherit = 'project.task'
    name = fields.Char(string="Name")
