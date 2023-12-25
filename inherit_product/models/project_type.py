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
    created_date=fields.Date('Create Date', default=date.today(), store=True, force_save=True,)
    product_ids=fields.One2many('products.projects','project_id',string="products")
    until_completion = fields.Boolean('Until Completion')
    one_time_job_annual = fields.Selection([('one_time_job', 'One Time Job'), ('annual_services', 'Annual Services')])
    project_start_date=fields.Date('Project Start Date', store=True, force_save=True)
    project_end_date=fields.Date('Project End Date', store=True, force_save=True)
    sale_order = fields.Many2one('sale.order', string="Sale Order no",track_visibility='always') 
    stage_name=fields.Char('Stage Name',related="stage_id.name")

    # @api.model
    # def fields_view_get(self,view_id=None, view_type='form', toolbar=False, submenu=False):
    #     sale_orders = self.env['sale.order'].search([('partner_id','=',self.partner_id.id)])
    #     res = super(ProjectProject,self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu)
    #     fields=res.get('fields')
    #     if sale_orders:
    #         if fields.get('sale_order'):
    #             res['fields']['sale_order']['domain'] = [('id','in',sale_orders.ids),('state','in',['sale','cancel','contract_expired','contract_expired_and_renewed'])]
    #     # else:
    #     #     res['fields']['sale_order']['domain'] = [('id','in',[])]
    #     return res



  
   

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


