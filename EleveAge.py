# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 18:00:45 2019

@author: LENOVO
"""
import pandas as pd
from os import getcwd

Eléve= pd.read_excel('eleve.xlsx')

#extraire la liste des personne ayant un age >20
Eléve_age = Eléve[Eléve.Age > 20 ]
Eléve_age.to_excel(getcwd()+'/Age_Sup_20.xls', index= False)
