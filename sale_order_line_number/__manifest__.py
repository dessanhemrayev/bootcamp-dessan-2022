{
    "name": "Sale order line",
    "version": "14.0.1.0.0",
    "license": "AGPL-3",
    "category": "",
    "summary": """Добавить нумерацию строк Заказа Продаж (Sales Order).
                  Нумерация должна дополнять существующий""",
    "author": "DessanHemrayev",
    "website": "https://dessanhemrayev.github.io",
    "depends": ["sale"],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/sale_order_line_views.xml",
        "views/sale_order_line_tree.xml",
    ],
    "demo": ["data/demo_data.xml"],
    "installable": True,
    "auto_install": False,
    "application": False,
}
