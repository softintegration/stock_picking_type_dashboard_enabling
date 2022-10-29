# -*- coding: utf-8 -*- 

from odoo import models,fields,api,_
from odoo.exceptions import UserError


class StockPickingType(models.Model):
    _inherit = "stock.picking.type"

    display_in_dashboard = fields.Boolean(string='Display in main dashboard',default=False)


