# IMPORTACION DE LAS LIBRERIAS A USAR
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# ===============LIMPIEZA DE LOS DATOS====================
# 1. Carga del data set
df = pd.read_csv(
    r"C:\Users\jes-z\OneDrive\Escritorio\Proyectos\Proyecto NYC Property Sales\data\raw\nyc-rolling-sales.csv", sep=',')
# --------------1. Eliminamos la columna Innecesaria Unnamed 0, EASY-MENT
df.drop(columns=['Unnamed: 0', 'EASE-MENT'], inplace=True, errors='ignore')
df.info()

# -------------2. Convertir columnas numéricas que vinieron como 'object'
# Usamos errors='coerce' para que lo que no sea número se convierta en NaN (nulo)
numeric_cols = ['SALE PRICE', 'LAND SQUARE FEET', 'GROSS SQUARE FEET']
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# -------------3. Convertir la fecha
df['SALE DATE'] = pd.to_datetime(df['SALE DATE'], errors='coerce')

# -------------4. Mapeo de Borough (Visión de Negocio)
# Según la documentación: 1=Manhattan, 2=Bronx, 3=Brooklyn, 4=Queens, 5=Staten Island
borough_map = {1: 'Manhattan', 2: 'Bronx',
               3: 'Brooklyn', 4: 'Queens', 5: 'Staten Island'}
df['BOROUGH'] = df['BOROUGH'].map(borough_map)

# -------------5. Revisamos cuántos nulos resultaron tras la conversión
print("Nulos por columna después de la conversión:")
print(df[numeric_cols].isnull().sum())

# ================LIMPIEZA DE OUTLIERS Y VALORES NULOS============
# -------------1. Eliminamos filas donde SALE PRICE es nulo (NaN)
df = df.dropna(subset=['SALE PRICE'])

# -------------2. Filtramos solo ventas que representen transacciones reales de mercado
# Elegimos un umbral de $10,000 para eliminar regalos, transferencias y errores
df = df[df['SALE PRICE'] > 10000]

# -------------3. Veamos cuántos datos nos quedan
print(f"Registros después de filtrar precios: {len(df)}")

# -------------Revisamos cuántos nulos resultaron tras eliminar los nulos de SALE PRICE
print("Nulos por columna después de la conversión:")
print(df[numeric_cols].isnull().sum())

# -------------4. Revisamos los metros cuadrados (SQUARE FEET)
# Tenemos muchos nulos ahí. Si queremos calcular 'Precio por metro cuadrado' en el futuro, también deberíamos considerar qué hacer con esos nulos.

# Vamos a rellenar nulos de metros cuadrados con la mediana de su barrio
df['LAND SQUARE FEET'] = df.groupby(
    'BOROUGH')['LAND SQUARE FEET'].transform(lambda x: x.fillna(x.median()))
df['GROSS SQUARE FEET'] = df.groupby(
    'BOROUGH')['GROSS SQUARE FEET'].transform(lambda x: x.fillna(x.median()))

# Verificamos si aún quedan nulos
print(df[['LAND SQUARE FEET', 'GROSS SQUARE FEET', 'SALE PRICE']].isnull().sum())
