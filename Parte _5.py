from datasets import load_dataset
import numpy as np
import pandas as pd
import requests
import csv

#parte 1
data = load_dataset("mstz/heart_failure")["train"]
promedio_edades = np.mean(np.array(data['age']))


#parte 2
df = pd.DataFrame(data)

#parte 5

def limpieza_de_datos (df):
    
    #Verificar que no existan valores faltantes

    print ("Falta algun valor?" ,df.isnull().sum())

    #Verificar que no existan filas repetidas

    print("Hay filas duplicadas en el df?", df.duplicated().any())

    #Verificar si existen valores atípicos y eliminarlos

    print("Dataframe original:")
    print(df)
    valores_atipicos_eliminados = pd.DataFrame()

    for columna in df.select_dtypes(include=['int64', 'float64']).columns:
        Q1 = df[columna].quantile(0.25)
        Q3 = df[columna].quantile(0.75)
        IQR = Q3 - Q1
    
        valores_atipicos = (df[columna] < (Q1 - 1.5 * IQR)) | (df[columna] > (Q3 + 1.5 * IQR))
       
        valores_atipicos_eliminados = pd.concat([valores_atipicos_eliminados, df[valores_atipicos]])
        
        df = df[~valores_atipicos]

    print("\nValores atípicos eliminados:")
    print(valores_atipicos_eliminados)

    #Crear una columna que categorice por edades
    df['Categorías_Edad'] = pd.cut(df['age'], bins=[0, 12, 19, 39, 59, float('inf')],
                             labels=['Niño', 'Adolescente', 'Joven Adulto', 'Adulto', 'Adulto Mayor'])
    
    #Guardar el resultado como csv
    df.to_csv('DataFrame_Limpio.csv', index=False)
    
    print (f"Dataframe con una columna nueva de cataegoria de edades\n {df}")

limpieza_de_datos(df)




