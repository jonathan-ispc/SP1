from resta import resta
from producto import producto

def funcion_p1_resta(param1, param2, param3):
    """Función que resta los dos primeros parámetros "p1" y "p2" y los
       multipica por el parámetro "p3" usando las funciones externas "resta" y "producto".
    Args:
        p1 (int | float)
        p2 (int | float)
        p3 (int | float)
    Returns:
        int | float: Resultado final de las operaciones con redondeo de 2 decimales.
    """
    
    op_resta = resta(param1, param2)
    result = producto(op_resta, param3)
    return result
