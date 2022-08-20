# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class Academy(http.Controller):

    @http.route('/academy/academy', auth='public')
    def index(self, **kw):
        return "Hello, World"

    @http.route('/academy/academy/objects', auth='public', website=True)
    def list(self, **kw):
        return request.render('academy.listing', {
            'root': '/academy/academy',
            'objects': request.env['academy.academy'].search([]),
        })

    @http.route('/academy/<int:id>/', auth='public', website=True)
    def academybyid(self, id):
        print ('idssssssssssssssss', id)
        return request.render('academy.template_id', {'id': id
        })


    @http.route('/academy/<model("academy.academy"):obj>', auth='public', website=True)
    def academy_list(self, obj):
        print ('BOjectttttttttttt', obj)
        return request.render('academy.object', {
            'objects': obj,
        })

    @http.route('/academy/academy/create', auth='public', website=True)
    def academy_created(self, **kw):
        AcademyObj = request.env['academy.academy']
        vals = {
            'name': 'Odoo Training-123',
            'city': 'Coimbatore'
        }
        AcademyObj.sudo().create(vals)
        return request.render('academy.academy_created', {})

