from odoo import models, fields, api
from odoo.exceptions import ValidationError

class custom_manage(models.Model):
    _name = 'customers'
    _description = 'custom manager'
    # ..............proparty...........
    # _inherit = 'lawyers.order'
    # .........delegate................
    # _inherits = {
    #     'lawyers.order':'lawyer_id',
    
    name = fields.Char(string='Name')
    age = fields.Integer(string='Age')

    def my_create(self):
        record = {
            'name':'ahmed',
            'age':55,
        }

        record1 = {
            'name':'salh',
            'age':66,
        }

        self.env['customers'].create([record,record1])


    # @api.model
    # def create(self,record):
    #     print('>>>>>>>>>>>>>>>',record)
    #     record['age']=30
    #     return super(ChannelUsersRelation,self).create(record)



    # active = fields.Boolean(string='Active', default=True)
    # acount_customer = fields.Integer(string='acount_customer')

    # def active_customer(self):
    #     domain = [('age','>=','25')]
    #     filter_cus = self.env['customers'].search(domain)
    #     for rec in filter_cus:
    #         rec.active = False

    #  دالة لاستبدال اي اسم عميل عمره فوق 30 سنه باسم جمعان
    # def print_record(self):
    #     domain = [('age','>=','30')]
    #     fillter_record = self.env['customers'].search(domain)
    #     for rec in fillter_record:
    #         rec.name = 'jumaan'

    # def active_customer(self):
    #     domain = [('age','>=',30)]
    #     filter_cus = self.env['customers'].search_count(domain)
    #     self.acount_customer = filter_cus






    

    # date = fields.Date(string='Date')
    # lawyer_id = fields.Many2one('lawyers.order',string='lawyers')
    # create_user = fields.Many2one('res.users',string='users')
    # res_text = fields.Text(string='Text By')
    # lawyer_id = fields.Many2one('lawyers.order')

    # def check_point(self):
    #     for rec in self:
    #             rec.res_text = self.env['lawyers.order'].search([('age','>',30)])



#     @api.constrains('age')
#     def check_age(self):
#         if self.age < 21:
#             raise ValidationError('The age is not required')

# _sql_constraints[
#     (
#         "check_name",
#         "unique(name)",
#         "The name is exist"),
# ]
