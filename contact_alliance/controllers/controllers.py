# -*- coding: utf-8 -*-
# from odoo import http


# class ContactAlliance(http.Controller):
#     @http.route('/contact_alliance/contact_alliance', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/contact_alliance/contact_alliance/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('contact_alliance.listing', {
#             'root': '/contact_alliance/contact_alliance',
#             'objects': http.request.env['contact_alliance.contact_alliance'].search([]),
#         })

#     @http.route('/contact_alliance/contact_alliance/objects/<model("contact_alliance.contact_alliance"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('contact_alliance.object', {
#             'object': obj
#         })
