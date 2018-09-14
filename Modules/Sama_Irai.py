# --------------------------------------------------------------------------------------------------
# Title: Space Weather codes
# Author: Edson Alonso Falla Luza
# Description: Source codes 
# Collaboratores: Alexandre Andrei
# --------------------------------------------------------------------------------------------------

#-------------------- Importing Python Internal Libraries ----------------#

import numpy as np
import time
from math import atan
from math import cos
from math import sqrt
from math import sin
from math import acos
import matplotlib.pyplot as plt
from IPython.display import Image as img

#DEFININDO CONSTANTES

pi = np.pi
RT = 6731 #KM

#DEFININDO A FUNCAO QUE CALCULA DISTANCIAS SAMA-IRAI

def caldist(latA,longA,latB,longB):
    ax = longA*pi/180
    ay = latA*pi/180
    bx = longB*pi/180
    by = latB*pi/180
    d = RT *acos(sin(ay)*sin(by) + cos(ay)*cos(by)*cos(ax-bx))
    return d

#DEFININDO A FUNCAO QUE CALCULA O ANGULOS SAMA - IRAI

def calang(latA,longA,latB,longB):
    x = abs(longB-longA)
    y = abs(latB-latA)
    ang = (180/pi)*atan(y/x)
    return ang