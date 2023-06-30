{
    "name": "Link_Source_Unit_Price_Variation",
    "summary": "Client sells hardware with a lot of price variance. Handle this variation in the price calculation.",
    "description": "Once a sale order line is created on an SO, price does not recompute when the quantity of the item is changed.",
    "license": "OPL-1",
    "category": "Custom Development.",
    "depends": [
        "sale",

    ],
    "data": ["views/inherit_sale_order.xml"
    ],
    "demo": [],
    "application": True,
}