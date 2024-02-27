# -*- coding: utf-8 -*-
# from odoo import http


# class CustomNew(http.Controller):
#     @http.route('/custom_new/custom_new', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_new/custom_new/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_new.listing', {
#             'root': '/custom_new/custom_new',
#             'objects': http.request.env['custom_new.custom_new'].search([]),
#         })

#     @http.route('/custom_new/custom_new/objects/<model("custom_new.custom_new"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_new.object', {
#             'object': obj
#         })
