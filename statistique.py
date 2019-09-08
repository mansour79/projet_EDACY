# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 18:13:56 2019

@author: LENOVO
"""
import pandas as pd
from xlwt import Workbook

Eléve= pd.read_excel('eleve.xlsx')
#Extraire la moyenne de la classe

moyClasse = Eléve['Moyenne'].mean()

#Extraire le pourcentage de fille
nombreFille = len(Eléve[Eléve['Sexe'] =='masculin'])
nombreEtudiant = len(Eléve)

pourcentageFille = (nombreFille * 100.0)/nombreEtudiant

#Extraire le pourcentage de boy

pourcentageGarcon = 100.0 - pourcentageFille

#Extraire la region qui a enregistre la plus forte moyenne
meilleureMoy = Eléve['Moyenne'].max()
getObject = Eléve[Eléve['Moyenne'] == meilleureMoy].reset_index()
Region =getObject['Region'][0]

#Mettre ces informations sur un fichier excel

wb2 = Workbook()

#ajouter une feuille dans notre document excel
sheet3 = wb2.add_sheet('Sheet 3') 
sheet3.write(0,0,"Moyenne de l\'ecole")
sheet3.write(0,1,"Pourcentage de fille")
sheet3.write(0,2,"Pourcentage d'homme")
sheet3.write(0,3,"RegionMoyenneSup")

sheet3.write(1,0,moyClasse)
sheet3.write(1,1,pourcentageFille)
sheet3.write(1,2,pourcentageGarcon)
sheet3.write(1,3,Region)

wb2.save('statistiques.xls')