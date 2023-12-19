from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from datetime import datetime,date
import logging
_logger = logging.getLogger(__name__)


class ProjectType(models.Model):
    _name = 'project.type'

    name = fields.Char(string="Type Name")
class ProjectProject(models.Model):
    _inherit = 'project.project'
    _order='created_date desc'
    project_type_id = fields.Many2one('project.type', string="Project Type")
    department_project_id = fields.Many2one('project.new.department', string="Department") 
    created_date=fields.Date('Create Date', default=date.today(), store=True, force_save=True, readonly=True)
    product_ids=fields.One2many('products.projects','project_id',string="products")
    until_completion = fields.Boolean('Until Completion')
    one_time_job_annual = fields.Selection([('one_time_job', 'One Time Job'), ('annual_services', 'Annual Services')])
    project_start_date=fields.Date('Project Start Date', store=True, force_save=True)
    project_end_date=fields.Date('Project End Date', store=True, force_save=True)
    sale_order = fields.Many2one('sale.order', string="Sale Order no") 




   

class productsproject(models.Model):
    _name='products.projects'

    project_id=fields.Many2one('project.project')
    product_id = fields.Many2one('product.product', string="Product",)
    name=fields.Html(string='Description')

    
    # @api.onchange('department_project_id')
    # def branch_filter(self):
    #     aa=self.department_project_id.department_id
    #     all=[]
    #     for j in aa:
    #         all.append(j.id)
    #     if all:
           
    #         return {'domain': {'project_type_id': [('id', 'in', all)]}}
    #     else:
         
    #         return {'domain': {'project_type_id': [('id', 'in', [])]}}

       
            



class ProjectTask(models.Model):
    _inherit = 'project.task'

    project_type_id = fields.Many2one('project.type', string="Project Type" , related='project_id.project_type_id')
    leave_warning = fields.Char(string="")


