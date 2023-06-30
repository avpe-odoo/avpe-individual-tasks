from odoo import api, models

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"
    
    @api.depends('product_id', 'product_uom', 'product_uom_qty')
    def _compute_price_unit(self):
        return

    def recompute_amount(self):
        super(SaleOrderLine, self)._compute_price_unit()