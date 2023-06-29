from odoo import api, fields, models, Command
from odoo.exceptions import ValidationError

class StockPickingInherit(models.Model):
    _inherit = "stock.picking"

    def button_validate(self):

        for picking in self:
            state = self.env["purchase.order"].search([("name", "=", picking.origin)]).state
            if state== "purchase":
                stock_move_record=self.env["stock.move"].search([("picking_id", "=", picking.id)])
                if stock_move_record.product_uom_qty < stock_move_record.quantity_done:
                    raise ValidationError("You can't receive more than the ordered quantity. Please, enter another quantity")
        res = super(StockPickingInherit, self).button_validate()
        return res
