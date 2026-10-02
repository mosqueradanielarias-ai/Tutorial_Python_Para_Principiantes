# GRÁFICOS
# Concepto: un gráfico resume una tabla para que se entienda de un vistazo.

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

base = Path(__file__).resolve().parent.parent
df = pd.read_csv(base / "outputs" / "ventas_limpias.csv", parse_dates=["fecha"])
# Requiere haber ejecutado antes 04_limpiar_datos.py

# Gráfico de barras: total vendido por categoría
por_categoria = df.groupby("categoria")["total"].sum()   # Agrupa y suma

por_categoria.plot(kind="bar", color="steelblue")
plt.title("Ventas totales por categoría")
plt.xlabel("Categoría")
plt.ylabel("Total (COP)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(base / "outputs" / "barras.png")             # Guarda la imagen
plt.show()                                               # Muestra el gráfico

# Gráfico de líneas: evolución del total por fecha
por_fecha = df.groupby("fecha")["total"].sum()

por_fecha.plot(kind="line", marker="o", color="darkorange")
plt.title("Ventas por fecha")
plt.xlabel("Fecha")
plt.ylabel("Total (COP)")
plt.tight_layout()
plt.savefig(base / "outputs" / "lineas.png")
plt.show()