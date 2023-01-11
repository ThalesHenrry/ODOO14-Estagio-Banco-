{
    'name': 'Cheque',
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
        'security/ir.model.access.csv',
        'views/cheque_views.xml',
        'views/cheque_views.xml',
        'Data/bank_cheque.xml'
    ],
    'application': True,
    'installable': True
}