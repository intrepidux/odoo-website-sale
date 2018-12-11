# -*- encoding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2018 Vertel (<http://www.vertel.se>).
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


{
    'name': 'Sale Statistics',
    'version': '1.0',
    'category': 'Sale',
    'description': """
Web based application show realtime sale statistics
===================================================
""",
    'author': 'Vertel AB',
    'website': 'http://www.vertel.se',
    'category': '',
    'depends': ['website_sale', 'sale_margin', 'pos_margin'],
    'init_xml': [],
    'data': [
        'views/templates.xml',
    ],
    'demo_xml' : [],
    'installable': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
