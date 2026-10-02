# LIMPIAR DATOS
# Concepto: datos limpios = resultados confiables.

from pathlib import Path
import pandas as pd

base = Path(__file__).resolve().parent.parent
df = pd.read_csv(base / "data" / "ventas_sucias.csv")

# 1. Eliminar filas duplicadas
df = df.drop_duplicates()

# 2. Corregir texto: quitar espacios y unificar mayúsculas
df["categoria"] = df["categoria"].str.strip().str.title()

# 3. Tratar valores vacíos
df["cantidad"] = df["cantidad"].fillna(0)                      # vacío -> 0
df["precio"] = df["precio"].fillna(df["precio"].median())      # vacío -> mediana

# 4. Convertir tipos de dato
df["fecha"] = pd.to_datetime(df["fecha"])                      # texto -> fecha
df["cantidad"] = df["cantidad"].astype(int)                    # decimal -> entero

# 5. Crear una columna nueva con un cálculo
df["total"] = df["precio"] * df["cantidad"]

print(df)

# 6. Guardar el resultado limpio
salida = base / "outputs"
salida.mkdir(exist_ok=True)                                    # Crea la carpeta si no existe
df.to_csv(salida / "ventas_limpias.csv", index=False)
print("Archivo limpio guardado en outputs/")