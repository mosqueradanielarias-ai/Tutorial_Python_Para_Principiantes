# IMPORTAR DATOS
# Concepto: pandas organiza los datos en un DataFrame (una tabla con filas y columnas).

from pathlib import Path
import pandas as pd

# Ruta del archivo, construida desde la ubicación de este script
ruta = Path(__file__).resolve().parent.parent / "data" / "ventas_sucias.csv"

df = pd.read_csv(ruta)       # Lee el CSV y lo convierte en tabla

print(df.head())             # Muestra las primeras 5 filas
print(df.shape)              # (filas, columnas)
print(df.columns.tolist())   # Nombres de las columnas
print(df.dtypes)             # Tipo de dato de cada columna
print(df.isna().sum())       # Cuenta los valores vacíos por columna
print(df.describe())         # Resumen estadístico de las columnas numéricas