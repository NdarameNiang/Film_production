# from odoo import models, fields
#
# class Film(models.Model):
#     _name = 'film.production'
#     _description = 'Film'
#
#     name = fields.Char(string='Nom', required=True)
#     release_date = fields.Date(string='Date de sortie')
#     duration = fields.Float(string='Durée (minutes)')
#     director_id = fields.Many2one('film.director', string='Réalisateur')
#     location_id = fields.Many2one('film.location', string='Lieu tourné')
#     production_company_id = fields.Many2one('film.production.company', string='Société de production')
#     film_type = fields.Selection([
#         ('action', 'Action'),
#         ('drama', 'Drame'),
#         ('comedy', 'Comédie'),
#         ('horror', 'Horreur'),
#     ], string='Type de film')
#     size = fields.Float(string='Taille (Go)')
#     price = fields.Float(string='Prix vendu (€)')
#
# class Location(models.Model):
#     _name = 'film.location'
#     _description = 'Lieu'
#
#     name = fields.Char(string='Nom', required=True)
#     film_ids = fields.One2many('film.production', 'location_id', string='Films tournés')
#     number_of_films = fields.Integer(string='Nombre de films tournés', compute='_compute_number_of_films')
#
#     def _compute_number_of_films(self):
#         for record in self:
#             record.number_of_films = len(record.film_ids)
#
# class ProductionCompany(models.Model):
#     _name = 'film.production.company'
#     _description = 'Société de production'
#
#     name = fields.Char(string='Nom', required=True)
#     film_ids = fields.One2many('film.production', 'production_company_id', string='Films')
#     number_of_films = fields.Integer(string='Nombre de films', compute='_compute_number_of_films')
#     capital = fields.Float(string='Capital (€)')
#
#     def _compute_number_of_films(self):
#         for record in self:
#             record.number_of_films = len(record.film_ids)
#
# class Shooting(models.Model):
#     _name = 'film.shooting'
#     _description = 'Tournage'
#
#     shooting_number = fields.Char(string='Numéro de tournage', required=True)
#     start_date = fields.Date(string='Date début')
#     end_date = fields.Date(string='Date de fin')
#     duration = fields.Float(string='Durée (jours)')
#     film_id = fields.Many2one('film.production', string='Film')
#
# class Director(models.Model):
#     _name = 'film.director'
#     _description = 'Réalisateur'
#
#     name = fields.Char(string='Nom', required=True)
#     film_ids = fields.One2many('film.production', 'director_id', string='Films réalisés')
#     number_of_films = fields.Integer(string='Nombre de films', compute='_compute_number_of_films')
#     gender = fields.Selection([
#         ('male', 'Masculin'),
#         ('female', 'Féminin'),
#     ], string='Sexe')
#     marital_status = fields.Char(string='Situation matrimoniale')
#     birth_date = fields.Date(string='Date de naissance')
#     age = fields.Integer(string='Âge')
#
#     def _compute_number_of_films(self):
#         for record in self:
#             record.number_of_films = len(record.film_ids)
