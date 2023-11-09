# -*- coding: utf-8 -*-
# from odoo import http


# class HrEmployee(http.Controller):
#     @http.route('/hr_employee/hr_employee', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_employee/hr_employee/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_employee.listing', {
#             'root': '/hr_employee/hr_employee',
#             'objects': http.request.env['hr_employee.hr_employee'].search([]),
#         })

#     @http.route('/hr_employee/hr_employee/objects/<model("hr_employee.hr_employee"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_employee.object', {
#             'object': obj
#         })
