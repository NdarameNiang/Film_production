{
    'name': 'Film Production',
    'version': '1.0',
    'category': 'Entertainment',
    'summary': 'Module for managing film productions',
    'description': 'Module for managing films, locations, production companies, shootings, and directors.',
    'depends': ['base'],
    'data': [
        'views/realisateur_views.xml',
        'views/lieu_views.xml',
        'views/tournage_views.xml',
        'views/menus_views.xml',
        'views/maison_production_views.xml',
        'views/film_views.xml',
    ],
    'installable': True,
    'application': True,
}
