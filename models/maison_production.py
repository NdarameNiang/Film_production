from odoo import models, fields, api

class MaisonProduction(models.Model):
    _name = 'cinema.maison.production'
    _description = 'Maison de Production'
    _rec_name = 'nom'
    _sql_constraints = [
        ('nom_unique', 'UNIQUE(nom)', 'Le nom de la maison de production doit être unique!')
    ]

    # Champs de base
    nom = fields.Char(
        string='Nom',
        required=True,
    )

    capital = fields.Float(
        string='Capital (fcfa)',
        required=True,
        digits=(16, 2),
        help="Capital de la maison de production"
    )

    # Relations
    film_ids = fields.One2many(
        'cinema.film',
        'maison_production_id',
        string='Films produits'
    )

    # Champs calculés
    nombre_films = fields.Integer(
        string='Nombre de films',
        compute='_compute_nombre_films',
        store=True
    )

    total_revenus = fields.Float(
        string='Total des revenus (€)',
        compute='_compute_total_revenus',
        store=True,
        digits=(16, 2)
    )

    # Méthodes calculées
    @api.depends('film_ids')
    def _compute_nombre_films(self):
        for record in self:
            record.nombre_films = len(record.film_ids)

    @api.depends('film_ids.prix_vendu')
    def _compute_total_revenus(self):
        for record in self:
            record.total_revenus = sum(film.prix_vendu for film in record.film_ids if film.prix_vendu)

    
    # Méthodes d'action
    def action_view_films(self):
        self.ensure_one()
        return {
            'name': 'Films',
            'view_mode': 'tree,form',
            'res_model': 'cinema.film',
            'type': 'ir.actions.act_window',
            'domain': [('maison_production_id', '=', self.id)],
        }