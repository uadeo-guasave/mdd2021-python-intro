# Obtener valores de entrada
num1 = input("Teclea un número:")  # 10
num2 = input("Teclea otro número:")  # 20

# print(type(num1), type(num2))
nums = num1 + num2
print("cadena concatenada: ", nums)  # 1020

# convertir las cadenas
num1 = int(num1)
num2 = int(num2)
nums = num1 + num2
print("número sumado: ", nums)  # 30

# convertir decimales a enteros
decimal = 8.34
entero = int(decimal)  # pérdida de valor
print(entero)

cadena = str(decimal)
print(cadena)
