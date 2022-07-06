# Función módulo: retorna el módulo de 2 parámetros:

a=int(input("Ingrese el dividendo: "))
b=int(input("Ingrese el divisor: "))

def modulo(a, b): 
    return a % b 

print("El residuo es ", modulo(a, b))