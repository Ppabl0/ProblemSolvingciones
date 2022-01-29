# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 2022

@author: Ppablo
"""
# Comprobar que un numero es primo
#   ¿como? divide el numero entre todos los numeros positivos anteriores a el excepto el 1
#   y verifica si el residuo es 0. guarda cada comparacion (booleanos) en una lista.
#   con numpy.any busca si en esa lista hay algun True, si hay al menos 1 True entonses no es primo
#   y la expresion evalua a True pero como True en este caso significa que no es primo se cambia el valor
#   con "not" para indicar que no es primo y viceversa

import numpy

numero_aleatorio = 20
not numpy.any([numero_aleatorio % i == 0 for i in range(2, numero_aleatorio)])
