# -*- coding: utf-8 -*-
# from odoo import http


# class MailTemplateWork(http.Controller):
#     @http.route('/mail_template_work/mail_template_work', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mail_template_work/mail_template_work/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('mail_template_work.listing', {
#             'root': '/mail_template_work/mail_template_work',
#             'objects': http.request.env['mail_template_work.mail_template_work'].search([]),
#         })

#     @http.route('/mail_template_work/mail_template_work/objects/<model("mail_template_work.mail_template_work"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mail_template_work.object', {
#             'object': obj
#         })
