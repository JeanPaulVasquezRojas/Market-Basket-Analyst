# 1 ) se importa las librerias
import numpy as np 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as dt
from mlxtend.preprocessing import TransactionEncoder # !pip install mlxtend # TRANSACTION ENCODER
from mlxtend.frequent_patterns import apriori, association_rules # APRIORI FUNCTION 
import itertools # ITERTOOLS 
import warnings # CONFIGURATION
from tabulate import tabulate
from pandasgui import show # Ventana emergente de los datos
from colorama import Fore, Style # Importa el módulo colorama para cambiar el color del texto

## MATRIZ BINARIA ORIGINAL
# 2 ) se establece las variables de las rutas de los archivos y el nombre de la hoja ventas BasePrueba.csv  
archivo_excel = 'C:/Users/Jean Paul/OneDrive - pucp.edu.pe/CICLOS DE UNIVERSIDAD CATOLICA/. TESIS/Data Procesada.xlsx'
# 3 se lee y carga la tabla desde el archivo Excel
df = pd.read_excel(archivo_excel)
df_copy =df
# 4 la columna products que  contiene elementos se separados por comas se convierte en Listas cada ITEM  en una serie de  una columna con LISTAS
data = df['products'].str.split(',')
# 5 Ss declara esta instancia porque se utilizará para ajustar y transformar los datos.
te = TransactionEncoder()
# 6 se crea la matriz binaria que representa la presencia o ausencia de cada producto para cada fila del DataFrame original df
te_data = te.fit(data).transform(data)
# 7 se crea un DataFrame con los datos transformados "MATRIZ BINARIA"
df = pd.DataFrame(te_data, columns=te.columns_).astype(int)

## TABLA DE SOPORTE 
# 1 se calcula el soporte por producto
medidas_1 =  df.sum() / df.shape[0]
# 2 se añade nombre a los encabezados
medidas =  pd.DataFrame({'Productos': medidas_1.index, 'Support': medidas_1.values}).sort_values("Support", ascending = False)
# 3 se redondea el valor del soporte
medidas['Support'] = medidas['Support'].round(4)
medida_0 = medidas
# 4 se filtra un soporte mayor que 0.01 medidas = medidas[medidas.Support >= 0.01]
medidas = medidas.head(10)
# 5 se realiza el formato tabla
medidas_tabla  = tabulate(medidas, headers='keys', tablefmt='pretty', showindex=False)
# 6 se imprime el formato tabla


## REDUCCION
# lista_valores = medidas['Productos'].tolist()
lista_valores= list(itertools.combinations(medidas['Productos'], 2)) # medidas.index indices = ['BREAD', 'COFFEE', 'BISCUIT', 'TEA', 'CORNFLAKES', 'SUGER', 'MAGGI','MILK', 'BOURNVITA', 'COCK', 'JAM']
lista_valores = [list(i) for i in lista_valores]

# Función para verificar si una fila contiene al menos uno de los valores de la lista
def contains_at_least_one_value(row, values):
    products_in_row = row.split(',')
    for value in values:
        if any(item in products_in_row for item in value):
            return True
    return False

# Aplicar la función y crear una columna de verificación
df_copy['Contiene_Valor'] = df_copy['products'].apply(contains_at_least_one_value, values=lista_valores)
df_copy = df_copy[df_copy['Contiene_Valor'] == True]
df_copy = df_copy.drop(columns=['Contiene_Valor'])
df_copy = df_copy.reset_index(drop=True)

# Filtro de columna
a = medida_0['Productos'].head(100).tolist()

## Matriz Binaria Reducida
data_reducida  = df_copy ['products'].str.split(',')
te = TransactionEncoder() # te almacena implícitamente las columnas, y puedes acceder a ellas directamente sin necesidad de definir te.columns_
te_data_reducida = te.fit(data_reducida).transform(data_reducida)
matriz_binaria = pd.DataFrame(te_data_reducida,columns=te.columns_).astype(int)
matriz_binaria = matriz_binaria[a].head(30)

# Apriori
freq_items = apriori(matriz_binaria, min_support = 0.0022, use_colnames = True)
print(freq_items.sort_values("support", ascending = False))

# Association Rules & Info
df_ar = association_rules(freq_items, metric = "confidence", min_threshold = 0.0001)
print (df_ar.head(10))






