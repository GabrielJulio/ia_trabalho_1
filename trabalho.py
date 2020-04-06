# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 16:14:20 2020

@author: Wescley
"""

import numpy as np
from lib import distancia

data = np.loadtxt('iris_log.dat', encoding='ASCII')

class1 = data[0:50]
class2 = data[50:100]
class3 = data[100:150]

class1_center = class1.mean(axis=0)[0:4]
class2_center = class2.mean(axis=0)[0:4]
class3_center = class3.mean(axis=0)[0:4]

distancia.euclidiana(class1_center, class2_center, class3_center, data)

distancia.manhattan(class1_center, class2_center, class3_center, data)

distancia.chebyshev(class1_center, class2_center, class3_center, data)
