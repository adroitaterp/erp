from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from datetime import datetime,date
import re
import ast
import logging
_logger = logging.getLogger(__name__)


class ProjectType(models.Model):
    _name = 'project.type'
  
    
    name = fields.Char(string="Type Name")
class ProjectProject(models.Model):
    _inherit = 'project.project'
    _order = 'create_date desc'


    follower = fields.Many2many('res.partner', string="Follower", compute='_compute_follower', readonly=False, store=True)
    all_follower= fields.Many2many(comodel_name='res.partner',relation ='project_id_rel',column1='partner_id',column2 ='project_id' , string="All Follower",store=True)
    remove_follower= fields.Char("Remove Followers")
    new_follower= fields.Char("New Followers")
    end_date_display = fields.Char(string="Contract End Date", compute="_compute_display")

    def _compute_display(self):
        
        for record in self:
            if not record.date:
                record.end_date_display = 'until completion'
            else:
                formatted_date = record.date.strftime("%d/%m/%Y")
                record.end_date_display = formatted_date

            
            


    

    @api.depends('message_follower_ids')
    def _compute_follower(self):
        for project in self:
            follower_ids = project.message_follower_ids.mapped('partner_id')
            project.follower = [(6, 0, follower_ids.ids)]

    @api.onchange('follower')
    def add_followers(self):
        for rec in self:
            rec.message_subscribe(partner_ids=rec.follower.ids)

            set_a = set(rec.all_follower.ids)

            self.all_follower = [(6, 0, rec.follower.ids)]
          
            set_b = set(rec.all_follower.ids)
            result = list(set_a - set_b)

            set_c=set(rec.message_follower_ids.mapped('partner_id').ids)
            
            new=list(set_b-set_c)

           
            rec.new_follower=new

            ee=rec.remove_follower
           
            if ee:
                result=str(result)+ee
            a=rec.remove_follower=result
            if a:
                numbers = re.findall(r'\d+', a)
                numbers = [int(num) for num in numbers]
                rec.remove_follower=numbers
            
    
            
            


    activity_type_id = fields.Many2one('mail.activity.type', string="Activity Type", store=True)
    activity_type_group = fields.Char(string="Activity Type Group", compute='_compute_activity_type_group', store=True)

    @api.depends('activity_type_id')
    def _compute_activity_type_group(self):
        for project in self:
            project.activity_type_group = project.activity_type_id.name


   
   
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

    follower_group_id = fields.Char(string='Related Field')

    def write(self, values):
        
        result = super(ProjectProject, self).write(values)
        res=self.remove_follower
        res=ast.literal_eval(res)
        self.message_unsubscribe(res)
        if values.get('tag_ids'):
            all=""
            for rec in self.tag_ids:    
                all +=" "+rec.name
            self.message_post(body=all,subject="Tags")
        if values.get('follower'):
            all=""
            for rec in self.follower:    
                all +=" "+rec.name
            self.message_post(body=all,subject="Followers")
        template=self.env.ref('inherit_product.project_mail_pp')
        if values.get('user_id'):
            email_values={'email_to': self.user_id.partner_id.email}
            template.send_mail(self.id,email_values=email_values,force_send=True)

        if values.get('new_follower'):
            
            pp=ast.literal_eval(self.new_follower)
            
            all=self.env['res.partner'].search([('id','in',pp)])
            
            email_to_list=all.mapped('email')
            email_to_list = ', '.join(email_to_list)
          
            email_values={'email_to': email_to_list}
            template=self.env.ref('inherit_product.project_mail_pp')
            template.send_mail(self.id,email_values=email_values,force_send=True)

        # _logger.warning("This test relies on demo data. '%s'",self.follower._origin.ids)
        # _logger.warning("This test relies on demo data. '%s'",values.get('follower'))

        
        return result

    @api.onchange('stage_id')
    def task_stage(self):
        if self._origin.stage_id.name == 'Done' and self.stage_id.name != 'Done':
            if self.env.ref("inherit_product.group_project_admin").id not in self.env.user.groups_id.ids:
                raise ValidationError(_("You are not authorized to change stage"))



    @api.constrains("stage_id")
    def check_stage_id_permission(self):
        
        # Your validation logic goes here
        if self.stage_id and self.stage_id.name == "In Progress" and not self.project_start_date:
            raise ValidationError("Please fill in the Project Start Date before moving to In Progress.")

       
        # Your validation logic goes here
        if self.stage_id and self.stage_id.name == "Done" and not self.project_end_date:
            raise ValidationError("Please fill in the Project End Date before moving to Done.")

        # Additional validation logic if needed

        return True

        
    
    # @api.model
    # def create(self, values):
    #     return super(ProjectProject, self.with_context(disable_stage_check=True)).create(values)

  



  
   

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

    project_type_id = fields.Many2one('project.type', string="Project Type" , related='project_id.project_type_id',track_visibility='onchange')
    leave_warning = fields.Char(string="")
    task_start_date=fields.Date('Task Start Date', store=True, force_save=True,track_visibility='onchange')
    task_end_date=fields.Date('Task End Date', store=True, force_save=True,track_visibility='onchange')
    project_id = fields.Many2one('project.project', string='Project',
        compute='_compute_project_id', recursive=True, store=True, readonly=False,
        index=True, tracking=True, check_company=True, change_default=True,track_visibility='onchange')
    parent_id = fields.Many2one('project.task', string='Parent Task', index=True,track_visibility='onchange')
    recurring_task = fields.Boolean(string="Recurrent",track_visibility='onchange')
    


    def write(self, values):
        result = super(ProjectTask, self).write(values)
        if values.get('user_ids'):
            all=""
            for rec in self.user_ids:    
                all +=" "+rec.name
            self.message_post(body=all,subject="Assignees")

        if values.get('tag_ids'):
            all=""
            for rec in self.tag_ids:    
                all +=" "+rec.name
            self.message_post(body=all,subject="Tags")
        
        return result



    @api.constrains("stage_id")
    def check_stage_id_permission(self):
        
        # Your validation logic goes here
        if self.stage_id and self.stage_id.name == "In Progress (For Client or FTA Action)" and not self.task_start_date:
            raise ValidationError("Please fill in the Task Start Date before moving to In Progress.")

        if self.stage_id and self.stage_id.name == "In Progress (For Alliance Action)" and not self.task_start_date:
            raise ValidationError("Please fill in the Task Start Date before moving to In Progress.")

        # Your validation logic goes here
        if self.stage_id and self.stage_id.name == "Done" and not self.task_end_date:
            raise ValidationError("Please fill in the Task End Date before moving to Done.")

        # Additional validation logic if needed

        return True


    


