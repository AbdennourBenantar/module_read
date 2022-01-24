# -*- coding: utf-8 -*-


from re import T, VERBOSE
from pandas.core.frame import DataFrame
import pandas as pd
import numpy as np

from odoo import models, fields, api




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
    colonnes= fields.One2many('orm.cols','colonne',"Champs de la table" )
    date_min = fields.Datetime(string= 'récupérer à partir de')
    status = fields.Char(string='status', compute='recupererBDD' , default='Dataframe non récupéré')

    

    @api.onchange('colonne')
    def recupererBDD(self):
        df = pd.DataFrame()      
        for r in self:
                recset = self.env['execution.predicting__house_prices'].search([('create_date', '>=', r.date_min)])
        for col in self.colonnes :        
                l = []
                l =recset.mapped(col.name)
                df[col.name] = pd.Series(l)      
        self.status = 'Dataframe récupéré'
        df.to_csv('/Users/mac/Downloads/odoo/addons/orm/data.csv',index=False)

  
        


        

