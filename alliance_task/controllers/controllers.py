# -*- coding: utf-8 -*-
# from odoo import http


# class AllianceTask(http.Controller):
#     @http.route('/alliance_task/alliance_task', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/alliance_task/alliance_task/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('alliance_task.listing', {
#             'root': '/alliance_task/alliance_task',
#             'objects': http.request.env['alliance_task.alliance_task'].search([]),
#         })

#     @http.route('/alliance_task/alliance_task/objects/<model("alliance_task.alliance_task"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('alliance_task.object', {
#             'object': obj
#         })
