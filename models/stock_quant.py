# -*- coding: utf-8 -*- 

from odoo import models,fields,api,_
from odoo.exceptions import ValidationError


class QuantPackage(models.Model):
    _inherit = "stock.quant.package"

    lot_id = fields.Many2one('stock.production.lot',compute='_compute_lot_id')


    def _compute_lot_id(self):
        for each in self:
            finished_move_line = each._get_current_linked_move_line()
            if not finished_move_line:
                each.lot_id = False
                continue
            try:
                each.lot_id = finished_move_line.move_id.production_id.lot_producing_id.id
            except Exception as exc:
                each.lot_id = False

    def _build_dynamic_prefix_fields(self):
        self.ensure_one()
        vals = {}
        for field_name, _ in self._fields.items():
            vals.update({field_name: getattr(self, field_name)})
        return vals







