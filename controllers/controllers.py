# -*- coding: utf-8 -*-
# from odoo import http


# class ModuleRead(http.Controller):
#     @http.route('/module_read/module_read/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module_read/module_read/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module_read.listing', {
#             'root': '/module_read/module_read',
#             'objects': http.request.env['module_read.module_read'].search([]),
#         })

#     @http.route('/module_read/module_read/objects/<model("module_read.module_read"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module_read.object', {
#             'object': obj
#         })