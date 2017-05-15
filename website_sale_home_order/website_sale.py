# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution, third party addon
#    Copyright (C) 2017- Vertel AB (<http://vertel.se>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp import models, fields, api, _
from openerp.exceptions import except_orm, Warning, RedirectWarning
from openerp import http
from openerp.http import request
import werkzeug
from openerp.addons.website_sale_home.website_sale import website_sale_home

import logging
_logger = logging.getLogger(__name__)



class website(models.Model):
    _inherit="website"


    @api.model
    def sale_home_order_search_domain(self,user,search=None):
        domain = [('partner_id','child_of',user.partner_id.parent_id.id if user.partner_id.parent_id else user.partner_id.id)]
        if search:
            search = search.strip()
            # invoices and picking
            invoice_ids = self.env['sale.order'].sudo().search(domain).mapped('invoice_ids').filtered(lambda i: search in i.name or search in i.number or search in i.date_invoice).mapped('id')
            picking_ids = self.env['sale.order'].sudo().search(domain).mapped('picking_ids').filtered(lambda p: search in p.name).mapped('group_id').mapped('id')
            #~ _logger.warn('invoice_ids: %s picking_ids: %s' % (invoice_ids,picking_ids))
            for s in ['|',('invoice_ids','in',invoice_ids),'|',('procurement_group_id','in',picking_ids),'|',('name','ilike', search),'|',('date_order','ilike', search),'|',('client_order_ref','ilike',search),('user_id','ilike',search)]:
                domain.append(s)
        _logger.debug('search_domain: %s' % (domain))
        return domain

    
    @api.model
    def sale_home_order_get(self,user,search):
        #~ _logger.warn('domain: %s result: ' % (search,self.env['sale.order'].sudo().search(self.sale_home_order_search_domain(user,search))))
        return self.env['sale.order'].sudo().search(self.sale_home_order_search_domain(user,search))
        
    @api.model
    def sale_home_order_get_invoice(self,order):
        invoice = order.invoice_ids.mapped('id') if order else []
        #~ raise Warning(invoice,len(invoice))
        if len(invoice)>0:
            document = self.env['ir.attachment'].search([('res_id','=',invoice[0]),('res_model','=','account.invoice')]).mapped('id') 
            if len(document)>0:
                return ("/attachment/%s/%s.pdf" % (document[0],order.invoice_ids[0].origin),order.invoice_ids[0].state)
        return None
            

class website_sale_home(website_sale_home):

    @http.route(['/home/<model("res.users"):user>/order_search',], type='http', auth="user", website=True)
    def home_page_order_search(self, user=None,order_search=None, **post):
        return request.render('website_sale_home.home_page', {
            'home_user': user if user else request.env['res.users'].browse(request.uid),
            'order_search_domain': request.website.sale_home_order_search_domain(user,order_search),
            'order_search': order_search,
        })

    @http.route(['/home/<model("res.users"):home_user>/order/<model("sale.order"):order>',], type='http', auth="user", website=True)
    def home_page_order(self, home_user=None, order=None, **post):
        self.validate_user(home_user)
        return request.render('website_sale_home_order.page_order', {
            'home_user': home_user if home_user else request.env['res.users'].browse(request.uid),
            'order': request.env['sale.order'].sudo().browse(order.id),
        })


    @http.route(['/home/<model("res.users"):home_user>/order/<model("sale.order"):order>/copy',], type='http', auth="user", website=True)
    def home_page_order_copy(self, home_user=None,order=None, **post):
        sale_order = request.website.sale_get_order()
        if not sale_order:
            sale_order = request.website.sale_get_order(force_create=True)
        sale_order.order_line |= order.order_line
        #~ for line in order.order_line:
            #~ sale_order.order_line = [(0,0,{'product_id': line.product_id.id, 'product_uom_qty': line.product_uom_qty})]
        return werkzeug.utils.redirect("/shop/cart")
