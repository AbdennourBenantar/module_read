

from odoo import models, fields, api
import pandas as pd
from . import pgcnct


class module_read_SQL(models.Model):
    _name = 'siquel.siquel'
    _description = 'Accéder à la BDD (petite porte)'

    name = fields.Char(string="Nom de la table")
    content=fields.Char(compute="read_sql",)
    
    def read_sql(self):
        conn=pgcnct.connecct()
        names=pgcnct.get_col_names(self.name,conn)
        import logging
        _logger = logging.getLogger(__name__)
        _logger.debug("ee"+str(names))
        self.env.cr.execute('SELECT * FROM '+self.name)
        df=self.env.cr.fetchall()
        df=pd.DataFrame(df,columns=names)
        _logger.debug(df)
        df=df.iloc[:,5:]
        df.to_csv("odoo\\addons\\module_read\\foo.csv",index=False)
        self.content=df



class cols(models.Model):
    _name = 'orm.cols'
    _description = 'orm.cols'
    colonne= fields.Many2one('orm.orm', readonly=True)
    name = fields.Selection(string='colonnes',  selection = 'recupererColBDD' )
    
    def recupererColBDD(self):
        list = []
        headers = self.env['execution.predicting__house_prices'].fields_get().keys()
        for key in headers:
            list.append((str(key),str(key)))   
        return list

class orm(models.Model):
    _name = 'orm.orm'
    _description = 'orm.orm'
    name = fields.Char(string='Name of the table')
    status = fields.Char(string='status', compute='recupererBDD' , default='Dataframe non récupéré')


    @api.depends('status')
    def recupererBDD(self):
        list = []
        headers = self.env[self.name].fields_get().keys()
        for key in headers:
            list.append((str(key),str(key))) 
        df = pd.DataFrame()      
        for r in self:
                recset = self.env[self.name].search([])
        for col in list[:-7] :        
                l = []
                l =recset.mapped(col[0])
                df[col[0]] = pd.Series(l)      
        self.status = 'Dataframe récupéré'
        df.to_csv('C:/Users/benantaa/Documents/odoo 14 entreprise/server/odoo/addons/module_read/data.csv',index=False)

  
        


        

