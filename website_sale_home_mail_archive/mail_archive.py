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
import math

import logging
_logger = logging.getLogger(__name__)


class website(models.Model):
    _inherit="website"

class mass_mailing(models.Model):
    _inherit='mail.mass_mailing'
    
    category_ids = fields.Many2many(comodel_name='mail.mass_mailing.category', string='Category', relation='mail_mass_mailing_category2_rel')


# ~ class mass_mailing_category(models.Model):
    # ~ _name='mail.mass_mailing.category'
    
    # ~ name=fields.Char(string='Category')
    
    

