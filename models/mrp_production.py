# -*- coding: utf-8 -*- 

from odoo import models,fields,api,_
from odoo.exceptions import ValidationError


class MrpProduction(models.Model):
    _inherit = "mrp.production"

    def _pack_move_line(self, move_line, packaging):
        package = self.env['stock.quant.package'].create(
            {'name':_('Unknown Pack'),'package_type_id': packaging.package_type_id and packaging.package_type_id.id})
        move_line.write({'result_package_id': package.id})
        # Dynamic sequence settings
        dynamic_prefix_fields = package._build_dynamic_prefix_fields()
        package.name = self.env['ir.sequence'].with_context(dynamic_prefix_fields=dynamic_prefix_fields).next_by_code(
                package._name)
        return package

