# -*- coding: utf-8 -*-
# from odoo import http


# class CalenderEventAlliance(http.Controller):
#     @http.route('/calender_event_alliance/calender_event_alliance', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/calender_event_alliance/calender_event_alliance/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('calender_event_alliance.listing', {
#             'root': '/calender_event_alliance/calender_event_alliance',
#             'objects': http.request.env['calender_event_alliance.calender_event_alliance'].search([]),
#         })

#     @http.route('/calender_event_alliance/calender_event_alliance/objects/<model("calender_event_alliance.calender_event_alliance"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('calender_event_alliance.object', {
#             'object': obj
#         })
