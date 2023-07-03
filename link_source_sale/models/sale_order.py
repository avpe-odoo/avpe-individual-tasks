from odoo import api, models

class SaleOrder(models.Model):
    _inherit = "sale.order"

    def recompute_amount(self):
        for line in self:
            sale_order_lines=self.env["sale.order.line"].search([("order_id", "=", line.id)])
            for line in sale_order_lines:
                if line.qty_invoiced > 0:
                    continue
                if not line.product_uom or not line.product_id or not line.order_id.pricelist_id:
                    line.price_unit = 0.0
                else:
                    price = line.with_company(line.company_id)._get_display_price()
                    line.price_unit = line.product_id._get_tax_included_unit_price(
                        line.company_id,
                        line.order_id.currency_id,
                        line.order_id.date_order,
                        'sale',
                        fiscal_position=line.order_id.fiscal_position_id,
                        product_price_unit=price,
                        product_currency=line.currency_id
                    )
