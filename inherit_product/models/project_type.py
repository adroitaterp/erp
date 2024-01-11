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
    project_type_id = fields.Many2one('project.type', string="Project Type", track_visibility='always')
    department_project_id = fields.Many2one('project.new.department', string="Department", track_visibility='always') 
    created_date=fields.Date('Create Date', default=date.today(), store=True, force_save=True,track_visibility='always')
    product_ids=fields.One2many('products.projects','project_id',string="products")
    until_completion = fields.Boolean('Until Completion',track_visibility='always')
    one_time_job_annual = fields.Selection([('one_time_job', 'One Time Job'), ('annual_services', 'Annual Services')], string="One Time Job/Annual",track_visibility='always')
    project_start_date=fields.Date('Project Start Date', store=True, force_save=True,track_visibility='always')
    project_end_date=fields.Date('Project End Date', store=True, force_save=True,track_visibility='always')
    sale_order = fields.Many2one('sale.order', string="Sale Order no",track_visibility='always') 
    stage_name=fields.Char('Stage Name',related="stage_id.name")
    tag_ids = fields.Many2many('project.tags', relation='project_project_project_tags_rel', string='Tags')
    date_start = fields.Date(string='Start Date',track_visibility='always')
    allow_subtasks = fields.Boolean('Sub-tasks', default=lambda self: self.env.user.has_group('project.group_subtask_project'),track_visibility='always')
    allow_recurring_tasks = fields.Boolean('Recurring Tasks', default=lambda self: self.env.user.has_group('project.group_project_recurring_tasks'),track_visibility='always')
    allow_timesheets = fields.Boolean(
        "Timesheets", compute='_compute_allow_timesheets', store=True, readonly=False,
        default=True, help="Enable timesheeting on the project.",track_visibility='always')

   
    def write(self, values):
        result = super(ProjectProject, self).write(values)
        if values.get('tag_ids'):
            all=""
            for rec in self.tag_ids:    
                all +=" "+rec.name
            self.message_post(body=all,subject="Tags")
        
        return result


    @api.constrains("stage_id")
    def check_stage_id_permission(self):
        # for the default value on create
        if self.env.context.get("disable_stage_check", False):
            return True
    
        if (self.env.ref("inherit_product.group_project_admin").id not in self.env.user.groups_id.ids):
            raise ValidationError(_("You are not authorized to change stage"))

    # on create just call the super with the context to disable the stage change, to allow it as "default" value
    
    @api.model
    def create(self, values):
        return super(ProjectProject, self.with_context(disable_stage_check=True)).create(values)

  



  
   

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
    task_start_date=fields.Date('Task Start Date', store=True, force_save=True)
    task_end_date=fields.Date('Task End Date', store=True, force_save=True)


    


