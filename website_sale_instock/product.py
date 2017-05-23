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
from datetime import timedelta,date
import logging
_logger = logging.getLogger(__name__)
import timeit
route_warehouse0_mto
class product_template(models.Model):
    _inherit = 'product.template'
    @api.one
    def _is_mto_route(self):
        if self.env.ref('stock.route_warehouse0_mto').id in self.route_ids.mapped('id'):
            self.is_mto_route = True
        self.is_mto_route = False
    is_mto_route = fields.Boolean(compute="_is_mto_route")


class product_product(models.Model):
    _inherit = 'product.product'

    @api.one
    def _is_mto_route(self):
        if self.env.ref('stock.route_warehouse0_mto').id in self.route_ids.mapped('id'):
            self.is_mto_route = True
        self.is_mto_route = False
    is_mto_route = fields.Boolean(compute="_is_mto_route")
