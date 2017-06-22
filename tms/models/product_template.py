# -*- coding: utf-8 -*-
# Copyright 2012, Israel Cruz Argil, Argil Consulting
# Copyright 2016, Jarsa Sistemas, S.A. de C.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import _, api, exceptions, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    tms_product_category = fields.Selection([
        ('freight', 'Freight (Waybill)'),
        ('move', 'Moves (Waybill)'),
        ('insurance', 'Insurance'),
        ('tolls', 'Highway Tolls'),
        ('other', 'Other'),
        ('real_expense', 'Real Expense'),
        ('made_up_expense', 'Made up Expense'),
        ('salary', 'Salary'),
        ('salary_retention', 'Salary Retention'),
        ('salary_discount', 'Salary Discount'),
        ('fuel', 'Fuel'),
        ('other_income', 'Other Income'),
        ('refund', 'Refund'),
        ('negative_balance', 'Negative Balance'),
        ('fuel_cash', 'Fuel in Cash'),
        ('tollstations', 'Tollstations (Expenses)')],
        string='TMS Product Category')
    apply_for_salary = fields.Boolean()

    @api.constrains('tms_product_category')
    def unique_product_per_category(self):
        for rec in self:
            categorys = [
                ['freight', 'Freight (Waybill)'],
                ['move', 'Moves (Waybill)'],
                ['salary', 'Salary'],
                ['negative_balance', 'Negative Balance'],
                ['indirect_expense', 'Indirect Expense']
            ]
            for category in categorys:
                product = rec.search([
                    ('tms_product_category', '=', category[0])])
                if len(product) > 1:
                    raise exceptions.ValidationError(
                        _('Only there must be a product with category "' +
                            category[1] + '"'))
