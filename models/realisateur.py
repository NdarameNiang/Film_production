from odoo import models, fields, api
from datetime import date

class Realisateur(models.Model):
    _name = 'cinema.realisateur'
    _description = 'Réalisateur de film'
    _rec_name = 'nom'

    nom = fields.Char(string='Nom', required=True)
    sexe = fields.Selection([
        ('homme', 'Homme'),
        ('femme', 'Femme')
    ], string='Sexe', required=True)
    
    situation_matrimoniale = fields.Selection([
        ('celibataire', 'Célibataire'),
        ('marie', 'Marié(e)')
    ], string='Situation Matrimoniale')
    
    date_naissance = fields.Date(string='Date de Naissance', required=True)
    age = fields.Integer(string='Âge', compute='_compute_age', store=True)
    
    # Relation One2many avec les films
    film_ids = fields.One2many('cinema.film', 'realisateur_id', string='Films Réalisés')
    nombre_films = fields.Integer(string='Nombre de Films', compute='_compute_nombre_films', store=True)

    @api.depends('date_naissance')
    def _compute_age(self):
        for record in self:
            if record.date_naissance:
                today = date.today()
                record.age = today.year - record.date_naissance.year - (
                    (today.month, today.day) < (record.date_naissance.month, record.date_naissance.day)
                )
            else:
                record.age = 0

    @api.depends('film_ids')
    def _compute_nombre_films(self):
        for record in self:
            record.nombre_films = len(record.film_ids)