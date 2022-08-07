from odoo import models, fields, api
from pkg_resources import require


class training_odoo(models.Model):
    _name = 'training.course'
    _description = 'Training Kursus'

    name = fields.Char(string='Judul', required=True)
    description = fields.Text(string='Keterangan')
