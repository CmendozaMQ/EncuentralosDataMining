# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 15:31:44 2018

@author: Rexxar
"""
import pandas as pd
import numpy as np
import math

b=[
"desaparecido",
"desaparecida",
"desaparecidos",
"desaparecidas",
"extraviados",
"buscamos",
"desaparecio",
"Buscamos"]

def isNaN(num):
    return num != num

dataset = pd.read_csv('../EncuentralosDataMining/155727921303318_facebook_statuses.csv')
csvRows = dataset.iloc[:, :-9].values
for datacsv in csvRows:
    if(isNaN(datacsv[1]) is False):
        datacsv_info=list(datacsv[1].split())
        print(list(set(datacsv_info).intersection(set(b))))