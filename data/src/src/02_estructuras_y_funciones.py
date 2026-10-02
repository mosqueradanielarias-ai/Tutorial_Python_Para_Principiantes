# ESTRUCTURAS Y FUNCIONES
# Concepto: las estructuras agrupan datos; las funciones reutilizan código.

# Lista: colección ordenada y modificable
precios = [3500, 800, 500, 45000]
precios.append(1200)                 # Agrega un elemento al final
print("Primer precio:", precios[0])  # El índice empieza en 0
print("Cantidad de datos:", len(precios))

# Diccionario: pares clave -> valor
producto = {"nombre": "Cuaderno", "precio": 3500}
print(producto["nombre"])            # Se accede por la clave

# Bucle for: repite una acción para cada elemento
for p in precios:
    print("Precio:", p)

# Funciones: se definen una vez y se usan muchas veces
def aplicar_iva(precio, iva=0.19):
    """Devuelve el precio con IVA incluido."""
    return precio * (1 + iva)

print(aplicar_iva(10000))            # 11900.0

# Comprensión de listas: crea una lista nueva en una sola línea
con_iva = [aplicar_iva(p) for p in precios]
print(con_iva)

# Estadísticas simples sin librerías
print("Suma:", sum(precios))
print("Mínimo:", min(precios))
print("Máximo:", max(precios))
print("Promedio:", sum(precios) / len(precios))