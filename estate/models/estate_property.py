# -*- coding: utf-8 -*-

from odoo import models, fields, api


class estateProperty(models.Model):
    _name = 'estate.property'
    _description = 'estate property model'
    _order = 'expected_price'

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(required=True, default=2)
    living_area = fields.Integer()
    garden_orientation = fields.Selection(
        string='Garden Orientation',
        selection = [('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')]
    )
