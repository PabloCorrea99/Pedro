import matplotlib.pyplot as plt
import numpy as np
import funciones 

#Funcion que corre todas las funciones del archivo funciones.py 
def todo(archivo,n):
    funciones.graficar(funciones.relacion(funciones.lectura(archivo),n))
    funciones.escribir(funciones.relacion(funciones.lectura(archivo),n))

todo("ejemplo.txt",4)