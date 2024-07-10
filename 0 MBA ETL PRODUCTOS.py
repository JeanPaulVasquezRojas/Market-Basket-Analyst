##  Analysis of purchases of a client
""""
Una canasta de compra es el conjunto de productos que un cliente compra durante una sola
transacción.

* Veremos la relacion entre la diferentes compras para recomendacion y prediccion
* Preferencia de los clientes
* Uso : operativos / publicitarios / estratégicos / logísticos
* Predecir futuras preferencias
* Patrones de compras --> Establecer preferencias / se puedan tomar decisiones con respecto a las compras de los clientes y
  establecer relaciones entre los productos -- se podría determinar cuáles productos en las vitrinas
  podrían ir acompañados con sus complementos
* Productos con siempre STOCK
* Reducir siempre el tiempo en que la personas pasa en a infraestructura
"""

### La problemática : Analizar el comportamiento de compra de los clientes de una cadena de Biomarkets


"""" Reglas de Asociacion """
# ----------------------------
# Librerias y su funcionalidad
# nombre_tabla = 'VENTAS'
# It provides support for large, multi-dimensional ARRAYS and matrices, along with a collection of mathematical functions to operate on these arrays
import numpy as np
# It is a powerful library for data manipulation and analysis. It provides data structures like DataFrames, which allow you to efficiently handle and analyze tabular data.
import pandas as pd
# t is a data visualization library built on top of Matplotlib. Seaborn provides a high-level interface for creating informative and attractive statistical graphics.
import seaborn as sns
# It is a plotting library that provides a MATLAB-like interface for creating various types of plots, including line plots, bar charts, histograms, scatter plots, etc.
import matplotlib.pyplot as plt
# It is a module that supplies classes for working with dates and times. This library is useful for manipulating and formatting dates and times in Python.
import datetime as dt
# It is a module that supplies classes for working with dates and times. This library is useful for manipulating and formatting dates and times in Python.
import openpyxl as xl
# pip install openpyxl

# ----------------------------
# Base de Datos 

# 1 Se importamos la libreria oandas  
import pandas as pd
# 2 se establece las variables de las rutas de los archivos y el nombre de la hoja ventas
archivo_excel = 'C:/Users/Jean Paul/OneDrive - pucp.edu.pe/CICLOS DE UNIVERSIDAD CATOLICA/. TESIS/Ventas.xlsx'
nombre_hoja = 'VENTAS'              
# 3 se lee y carga la tabla desde el archivo Excel
df = pd.read_excel(archivo_excel, sheet_name=nombre_hoja, header=None, engine='openpyxl')
# 4 se elimina las 5 primeras filas
# df = df.drop(index=df.index[:5]) Estto se hacia cuando se descargaba ahora se consulta y aparece el la primera fila
# 5 se reindexa los indices
df = df.reset_index(drop=True)
# 6 se asigna la primera fila como nombres de columna
df.columns = df.iloc[0]
# 7 se elimina la primera fila (opcional)
df = df.drop(index=df.index[0])
# 8 se fitra las filas con solo Ventas
df = df[df['Tipo Movimiento'] == 'Venta']
# 9 se conserva solo las columnas 'Numero de Serie','Producto / Servicio'
df = df[['Numero de Serie','Producto / Servicio']]
# 10 se ordena las columnas 
df = df.sort_values(by=['Numero de Serie','Producto / Servicio'])
# 11 se renombrar los nombres de los encabezados
df = df.rename(columns={'Numero de Serie':'Comprabante','Producto / Servicio':'Productos'}) 
# 12 se agrupa todos lo productos a un comprobante
df = df.groupby('Comprabante')['Productos'].apply(','.join).reset_index()
# 13 se conserva  los productos
df = df[['Productos']]
# 14 se renombrar los nombres de los encabezados
df = df.rename(columns={'Productos': 'products'})
# 15 Se almacena la informacion en "Data Procesada."
df.to_excel('C:/Users/Jean Paul/OneDrive - pucp.edu.pe/CICLOS DE UNIVERSIDAD CATOLICA/. TESIS/Data Procesada.xlsx', index=False)


























## AUXILIARES
# Imprimimos columnas
# print(df.columns)
# Imprime el contenido de la tabla
# print(df)
# df.to_excel('C:/Users/Jean Paul/OneDrive - pucp.edu.pe/CICLOS DE UNIVERSIDAD CATOLICA/. TESIS/Ventas2.xlsx', index=False)
# df.size ## Número de elementos del DataFrame
# Observamos los nombres de la hojas
# workbook = xl.load_workbook(archivo_excel)
# print(workbook.sheetnames)  