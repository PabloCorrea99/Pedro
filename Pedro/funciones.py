import numpy as np
import matplotlib.pyplot as plt
import os

#Diccionario de Datos de los integrantes del equipo.
integrantes = {"201810013013":"Santiago Rave Trujillo", "201810020013":"Pedro Correa", "201810066013":"Valentina Carvajal", "201810024013":"Juan Jose Garcia"}


#Funcion que abre un archivo de texto, lo lee y a apartir de el crea y retorna un arreglo numpy con los valores utiles.
def lectura(archivo):
    read=open(archivo,'r')
    a=[]
    lineas=read.readlines()
    for i in lineas:
        a.append(i[0:5])
    read.close()
    b=[float(i) for i in a]
    b=np.array(b)

    return b

#Funcion que retorna la deflexion y de la punta de un mastil.
def calcular(arreglo):
    f=arreglo[0]    #Fuerza (lbf/ft)
    l=arreglo[1]    #Altura (ft)
    e=arreglo[2]    #Modulo de elasticidad (lbf/ft)
    i=arreglo[3]    #Momento de inercia (ft)
    y=(f*(l**4))/(8*e*i)  #y=(FL^4)/(8EI)

    return y

#Funcion que crea y llena una matriz.En la primera columna van valores de altura y en la segunda sus correspondiente deflexion y.
def relacion(arreglo,n):
    matrix=[[0 for i in range(2)] for j in range(n)]
    for i in range(n):
        matrix[i][0]= arreglo[1]
        matrix[i][1]= calcular(arreglo)
        arreglo[1]+=1
    matrix=np.array(matrix)

    return matrix

#Funcion que toma la matriz de la funcion relacion y genera una grafica.
def graficar(matrix):
    x=np.array(matrix[:,1])
    y=np.array(matrix[:,0])
    plt.grid()
    plt.plot(x,y,'-o')
    plt.xlabel('Deflexion y (ft)')
    plt.ylabel('Altura (ft)')
    plt.title('Deflexión y de la punta de un mástil')
    plt.show()
    
#Funcion que toma la matriz de la funcion relacion y escribe los resultados en un archivo .txt
def escribir(matrix):
    file = open("salida.txt", "w")
    for i in range(len(matrix)):
        y=str(matrix[i])
        x=y.replace("["," ")
        x=x.replace("]"," ")
        file.write( x + os.linesep)
    file.close()

