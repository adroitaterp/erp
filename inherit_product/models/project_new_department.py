# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProjectNewDepartment(models.Model):
    _name = 'project.new.department'
    name = fields.Char(string="Department")
    department_id = fields.Many2many('project.type', string='Project Type', store=True)