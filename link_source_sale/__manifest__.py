{
    "name": "Link_Source_Unit_Price_Variation",
    "website": "https://www.odoo.com",
    "author": "Odoo Inc.",
    "summary": "Client sells hardware with a lot of price variance. Handle this variation in the price calculation.",
    "description": "Once a sale order line is created on an SO, price does not recompute when the quantity of the item is changed.",
    "license": "OPL-1",
    "category": "Custom Development.",
    "depends": [
        "sale",

    ],
    "data": ["views/sale_order.xml"
    ],
    "application": False,
}