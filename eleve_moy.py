# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 17:07:22 2019

@author: LENOVO
"""
#Importer pandas pour la manipulation des donnees
import pandas as pd
import os
cwd=os.getcwd()

#importation des bibliotheques pour la creation et l'ecriture d'un fichier Excel
Eléve = pd.read_excel('eleve.xlsx')

#creer un fichier excel contenant la liste des eleves qui ont la moyenne

eleves_moyenne = Eléve[Eléve.Moyenne >= 10]
eleves_moyenne.to_excel(cwd+'/Eléve_Admis.xls', index=False)