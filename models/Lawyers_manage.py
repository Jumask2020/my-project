from odoo import models, fields, api
from datetime import date, datetime, timedelta


class CovenentRecord(models.Model):
    _name = 'lawyers.order'
    _description = 'Lawyers management'

    name = fields.Char(string='Name')
    age = fields.Integer(string='Age',compute='cal_age')
    date = fields.Date(string='Date')
    note = fields.Text(string='Text')

    @api.depends('date')
    def cal_age(self):
        for rec in self:
            years = date.today()
            if rec.date:
                rec.age = years.year - rec.date.year
            else:
                rec.age = 1

    # def check_point(self):
    #     print('-------------------',self.inv.users)

    # _sql_constraints[
    #     ('Chack_name','UNIQUE(name)','The name is exist',)
    # ]

    
    # _sql_constraints = [
    #     ("Chack_name",
    #      "UNIQUE(name)",
    #      "The name is exist"),
    # ]

    # _sql_constraints = [
    #     ("Chack_age",
    #      "CHECK(age > 21)",
    #      "The age is not required"),
    # ]
    # customer_id = fields.Many2one('customers',string='Customer_id')
    # customer_ids = fields.Many2many('customers',string='Customer_id')
    # customer_ids1 = fields.One2many('customers','lawyer_id',string='Customer_id')
    # lawyer_id = fields.Many2one('res.users',string='Lawyer')
    # price = fields.Monetary(currency_field='currency_id' ,string='price')
    # currency_id = fields.Many2one('res.currency',string='Currency',related='company_id.currency_id')
    # company_id = fields.Many2one('res.company',string='Company',related='lawyer_id.company_id')
    # reference = fields.Reference(selection=[('res.users','Customers'),('res.company','Company')],string='Reference')
    # float1 = fields.Float(string='float',help='The float',digital='digital4')
    # age = fields.Integer(string='Age', compute='_compute_age')
    # new_field = fields.Char(string='New Field')
    # field1 = fields.Selection([('male','male'),('female','female')],string='selection')
    # field2 = fields.Text(string='TEXT')
    # field3 = fields.Image(string='image')
    # field4 = fields.Binary(string='binary')
    # field5 = fields.Html(string='HTMl')
    # date = fields.Date(string='date', default= date.today())
    # datetime = fields.Datetime(string='date time', default= datetime.now())
    # field8 = fields.Boolean(string='boolean')

    # @api.depends('date')
    # def _compute_age(self):
    #     for rec in self:
    #         currentyear = date.today()
    #         if rec.date:
    #             rec.age = currentyear.year - rec.date.year
    #         else:
    #             rec.age = 1