# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
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
 
from openerp import models, fields, api, tools, _
from openerp.osv import fields as fields_old
# import openerp.addons.decimal_precision as dp


class MrpTetzPdo(models.Model):
    _name = 'mrp_tetz_pdo'
    _description = 'mrp_tetz_pdo'
    _rec_name = 'number'
    number = fields.Char(required=True)
    master_pdo_id = fields.Many2one('res.users', required=True, default=lambda self: self.env.user)
    start_data = fields.Date(required=True, default=fields.Date.today)
    dobav_ids = fields.One2many('mrp_product','sqt_id')
    work_centr = fields.Selection( selection=[(u'centr2', u'Zag work'), (u'centr1', u'Mex work')], required=True)
    text = fields.Text()
    position = fields.Char(required=True, default="Инженер ПДО")	
	
	
    _defaults = {

        'number': lambda self, cr, uid, context: self.pool['ir.sequence'].get(cr, uid, 'mrp_tetz_pdo', context=context) or '/',

    }
 

    state = fields.Selection([
        ('draft', "Draft"),
        ('confirmed', "Confirmed"),		
        ('done', "Done"),
    ])

    @api.multi
    def action_draft(self):
        self.state = 'draft'

    @api.multi
    def action_confirm(self):
        self.state = 'confirmed'		

    @api.multi
    def action_done(self):
        self.state = 'done'




class MrpProduct(models.Model):
    _name = 'mrp_product'
    _description = 'mrp_product'
    tab_number = fields.Char('Tabnumber')
    master_id = fields.Many2one('res.users', string='Master')	
    production_id = fields.Many2one('product.template', string='Production',)
    work = fields.Char() 
    col1 = fields.Char()
    col2 = fields.Char()
    otk = fields.Char('OTK')
    sqt_id = fields.Many2one('mrp_tetz_pdo', string='SQT', ondelete='cascade')
    opera = fields.Char()
    
class AddmasterUsers(models.Model):
    _name = "res.users"
    _inherit = "res.users"

# Add new field
    master = fields.Boolean("Mastera", default=False)
    ingener = fields.Boolean("Ingener", default=False)
	
	


