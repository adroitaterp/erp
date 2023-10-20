# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProjectProjectInherit(models.Model):
    _name = 'project.department'
    name = fields.Char(string="Department")
    project_by_id = fields.Many2many('project.type', string='Project Type', store=True)
    




