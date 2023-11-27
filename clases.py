#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import scipy.io as sio

def operacion (x):
    return x*0.8 +1.1

def desviacion(tabla,columna):
    return tabla[columna].std(axis=1).values
    
class ControlAire:

    def __init__(self,data = np.zeros((2,2))):
            self._data = data
            self._tabla = pd.DataFrame(data)
            self.__dimension =  self._data.ndim
            self.__forma =  self._data.shape
            self.__tamano =  self._data.size
            self.__canales = self.__forma[0]
            self.__puntos = self.__forma[1]
            self.__columnas = self._tabla.columns
            
    def operacion2(self, columna): 
        h = self._tabla.copy()
        h[columna]=h[columna].apply(operacion)#apply se usa para aplicar una función a lo largo de filas o columnas
        return h[columna].values
            
    def extraerCol(self,x):
        col = self._tabla.loc[:,x].values
        #print(col)
        return col
    
    def dividirData(self,columnas):
        h = self._tabla.copy()
        n = len(h)
        t = n//2
        print(t)
        part1 = h.iloc[:t,:]
        part2 = h.iloc[t:,:]
        #es1 =part1.[columnas].std(axis=1)
        #res2 =part2[columnas].std(axis=1)       
        return part1, part2

    
    
    def vercolumnas(self):
        return self.__columnas
    
    def __str__(self):
            return f"""Las características de la matriz de la señal matriz son: 
forma: {self.__forma}
dimension: {self.__dimension}
tamaño: {self.__tamano}"""

    def asignarDatos(self,data):
        self._data = data 
        self.__dimension =  self._data.ndim
        self.__forma =  self._data.shape
        self.__tamano =  self._data.size
        self.__canales = data.forma[0]
        self.__puntos = data.forma[1]
        
    def verForma(self):
        return self.__forma
    def verDim(self):
        return self.__dimension
    def verTam(self):
        return self.__tamano
    def verCanales(self):
        return self.__canales
    def verPuntos(self):
        return self.__puntos
        
    def devolver_Canal(self,canal):
        l = self._data.loc[canal].values
        l = l[2:36]
        #return self._data[canal]
        return l
        
    
    def devolver_Segmento(self,pmin,pmax, col):
        if pmin >= pmax:
            return None
        return self._tabla[pmin:pmax,col]
    
    def devolver_segCanales(self, pmin, pmax):
        if pmin >= pmax:
            return None
        return self._data[pmin:pmax,:]        
    
    
class senal_ECG:
    def __init__(self,data = np.zeros((2,2))):
        self._data = data
        self.__dimension =  self._data.ndim
        self.__forma =  self._data.shape
        self.__tamano =  self._data.size
        self.__canales = self.__forma[0]
        self.__puntos = self.__forma[1]
    
    def mult(self,c1, c2, c3,c4 ):
        aux1 = np.multiply(c1, c2)
        aux2 = np.multiply(c3, c4)
        aux3 = np.multiply(aux1, aux2)
        return aux3
    
    def operacion(self,c1, c2, c3,c4):
        aux1 = np.multiply(c1, c2)
        aux2 = np.multiply(c3, c4)
        aux3 = np.multiply(aux1, aux2)
        #print(aux3)
        #print(np.divide(aux3,3))
        return np.divide(aux3,3)
    
    def extraerCanal(self,canal):
        c = self._data[canal,:100]
        return c
    
    def __str__(self):
        return f"""Las características de la matriz de la señal matriz son: 
forma: {self.__forma}
dimension: {self.__dimension}
tamaño: {self.__tamano}
"""

    def devolver_Segmento(self,imin,imax, maxc,minc):
        if imin >= imax:
            return None
        if minc >= maxc:
            return None
        return self._data[imin:imax,minc:maxc]
    
    def verForma(self):
        return self.__forma
    def verDim(self):
        return self.__dimension
    def verTam(self):
        return self.__tamano
    def verCanales(self):
        return self.__canales
    def verPuntos(self):
        return self.__puntos

class Sistema:

    def __init__(self):
        self._aire= []
        self.senal_ECG =[]
            
    def ingresarCaire(self, aire):
        self._aire.append(aire)
        
    def ingresarSenal(self, senal):
        self.senal_ECG.append(senal)
        
    def versenal(self):
        return self.senal_ECG
    
    def verAire(self):
        return self._aire
        
            
            
class Graficadora:
    
    def __init__(self):
        self.__fig, self.__ax = plt.subplots(2, 2, sharey = True)
        
    def graficar(self,x,y,z):
        self.__ax[0,0].plot(x)
        self.__ax[0,1].plot(y)
        self.__ax[1,0].boxplot(z)
        
        self.__ax[0,0].set_xlabel('Segundos')
        self.__ax[0,0].set_ylabel('multipllicacion')
        self.__ax[0,0].set_title('Grafica 1')
        
        self.__ax[0,1].set_xlabel('Segundos')
        self.__ax[0,1].set_ylabel('multipllicacion + divison')
        self.__ax[0,1].set_title('Grafica 2')
        
        self.__ax[1,0].set_xlabel('Segundos')
        self.__ax[1,0].set_ylabel('4 canales')
        self.__ax[1,0].set_title('Grafica 3')
        plt.subplots_adjust(hspace = 0.8, wspace = 0.8)
        
        
        
        
        
        plt.show()
        
        
    #def graficarcan(self,c1)
        
        


# In[ ]:





# # 

# 
