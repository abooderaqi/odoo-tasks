{
    'name': 'App One',
    'author': 'Abood Eraqi',
    'category': '',
    'version': '18.0',
    'depends': ['base', 'sale_management', 'account', 'mail', 'purchase'],
    'sequence': 1,
    'data': ['security/security.xml', 'security/ir.model.access.csv', 'views/base_menu.xml', 'views/property_view.xml',
             'views/owner_view.xml',
             'views/tag_view.xml', 'views/sales_order_view.xml', 'views/custom_purchase_view.xml', 'views/account_move_view.xml',],
    'assets': {
        'web.assets_backend': ['app_one/static/src/css/property.css']
    },
    'application': True,
}
