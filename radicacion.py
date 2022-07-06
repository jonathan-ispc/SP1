# Función radicación: retorna la raíz del primero respecto del segundos parámetros Args: base indice 
    
base=int(input("Ingrese la base: "))
indice=int(input("Ingrese el índice: "))

def radicacion (a, b): 
    return pow(base, 1/indice)

print("La radicación es:", radicacion(base, indice))