# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Yannick Buron and Valeureux  Copyright Valeureux.org
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Wezer Exchange',
    'version': '1.0',
    'category': 'Wezer module',
    'author': 'Yannick Buron and Valeureux for Valeureux',
    'license': 'AGPL-3',
    'description': """
Wezer Exchange
==============

Use your Odoo to manage communities.
------------------------------------
    * Install official module useful for communities
    * Manage community access from user simplified form
    * Add a custom form to install module for managing community
""",
    'website': 'https://github.com/valeureux/wezer-exchange',
    'depends': [
        'base',
        'base_community',
        'calendar',
        'document',
        'gamification',
        'im_chat',
        'im_livechat',
        'mail_holacracy',
        'membership',
        'membership_users',
        'community_send_notification',
        'portal',
        'website',
        'website_mail_group',
    ],
    'data': [
        'data/community_data.xml',
        'community_view.xml',
        'security/community_security.xml',
        'res_config_view.xml'
    ],
    'demo': ['data/community_demo.xml'],
    'installable': True,
    'application': True,
}
