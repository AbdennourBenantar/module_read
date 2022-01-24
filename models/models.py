# -*- coding: utf-8 -*-

from odoo import models, fields, api
import pandas as pd


class module_read_SQL(models.Model):
    _name = 'siquel.siquel'
    _description = 'Accéder à la BDD (petite porte)'

    name = fields.Char(string="Nom de la table")
    content=fields.Char(compute="read_sql",)
    
    def read_sql(self):
        import logging
        _logger = logging.getLogger(__name__)
        _logger.debug("innnnnn")
        self.env.cr.execute('SELECT * FROM '+self.name)
        df=self.env.cr.fetchall()
        df=pd.DataFrame(df)
        _logger.debug(df)
        df=df.iloc[:,5:]
        df.to_csv("odoo\\addons\\module_read\\foo.csv")
        self.content=df



class module_read_ORM(models.Model):
    _name = 'orm.orm'
    _description = 'Accéder à la BDD (ORM)'

    name = fields.Char()
    value = fields.Integer()