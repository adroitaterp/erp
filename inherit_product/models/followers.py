from odoo import api,models,fields
from odoo.exceptions import ValidationError
from datetime import datetime


class EmploymentHistory(models.Model):
    _name = "followers.group.project"
    _rec_name = 'follower_group_name'

    follower_group_name = fields.Char(string='Group Name')
    following_user_ids = fields.Many2many(
        'res.partner', 'res_users_rel', 'follower_id', 'user_id', string='Followers Users',
        help="Users who will get email when lead is created")
    active_follower_group = fields.Boolean(string='Active')

