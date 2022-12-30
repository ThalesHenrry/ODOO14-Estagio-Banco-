{
    'name': 'Banco',
    'version': '14.0.0.0',
    'sumary': 'Modulo para pagamentos',
    'sequence': 1,
    'description': "Modulos para pagamentos"
                   "Odoo v14",
    'website': 'https://www.google.com/',
    'category': 'banco',
    'author': 'Thales Gregorio',
    'depends': ['base', 'account'],
    'data': [
        'views/banco_views.xml',
        'security/ir.model.access.csv'
    ],
    'application': True,
    'installable': True
}