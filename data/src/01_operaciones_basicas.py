# OPERACIONES BÁSICAS
# Concepto: una variable guarda un valor; un operador hace un cálculo con él.

a = 20          # Guarda el número 20 en la variable "a"
b = 6           # Guarda el número 6 en la variable "b"

print("Suma:", a + b)                    # + suma
print("Resta:", a - b)                   # - resta
print("Multiplicación:", a * b)          # * multiplica
print("División:", a / b)                # / divide (resultado decimal)
print("División entera:", a // b)        # // divide y descarta los decimales
print("Residuo:", a % b)                 # % entrega lo que sobra de la división
print("Potencia:", a ** 2)               # ** eleva a una potencia

# Redondear y valor absoluto
print("Redondeo:", round(a / b, 2))      # round(número, decimales)
print("Absoluto:", abs(b - a))           # abs() quita el signo negativo

# Tipos de datos básicos
nombre = "Ana"          # str  -> texto
edad = 25               # int  -> entero
altura = 1.62           # float -> decimal
es_estudiante = True    # bool -> verdadero o falso

print(type(nombre), type(edad), type(altura), type(es_estudiante))

# Comparaciones (devuelven True o False)
print(a > b)    # ¿a es mayor que b?
print(a == b)   # ¿a es igual a b?

# Condicional: ejecuta código solo si se cumple una condición
if a > b:
    print("a es mayor que b")
else:
    print("a no es mayor que b")