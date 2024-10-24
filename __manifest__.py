{
    'name': 'Module Tournage de Film',
    'version': '1.0',
    'category': 'Cinema',
    'description': 'Gestion des tournages de film',
    'author': '[Issa Ndiaye, Mame Diarra BA, Seynabou Gaye, Ndeye Arame Niang]',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/tournage_views.xml',
    ],
    'installable': True,
    'application': True,
}
