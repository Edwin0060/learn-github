# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import requests


class MyWebsite(http.Controller):

    @http.route('/employee/details', auth='public', website=True)
    def employee_information(self, **kw):
        return request.render('mywebsite.employee_information', {})

    @http.route('/employee/info', type="http", methods=["POST"], auth='none', csrf=False, website=True)
    def employee_info(self, **kw):
        emp_name = kw.get('name')
        print('****************************************emp Name ********************************', emp_name)
        vals = {
            'name': emp_name,
        }
        request.env['res.partner'].sudo().create(vals)
        return

