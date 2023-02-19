# -*- coding: utf-8 -*-
# from odoo import http


# class JobEstimate(http.Controller):
#     @http.route('/job_estimate/job_estimate', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/job_estimate/job_estimate/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('job_estimate.listing', {
#             'root': '/job_estimate/job_estimate',
#             'objects': http.request.env['job_estimate.job_estimate'].search([]),
#         })

#     @http.route('/job_estimate/job_estimate/objects/<model("job_estimate.job_estimate"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('job_estimate.object', {
#             'object': obj
#         })
