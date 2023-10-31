{
    'name': 'open academy',
    'version': '1.0.0',
    'sequence': -100,
    'author': 'Jumaan askool',
    'website': ['www.askool','.com'],
    'category': 'Lawyers',
    'summary': 'Lawyers managment system',
    'description': 'Lawyers management system',
    'depends': ['base','sale'],
    'data': [
        'views/Lawers_views.xml',
        'views/custom_views.xml',
        'views/inherit_views.xml',
        'security/ir.model.access.csv',

    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3'
}
