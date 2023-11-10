def sumar(a, b):
    """
    Suma dos números proporcionados.

    Args:
    a (int/float): Primer número.
    b (int/float): Segundo número.

    Returns:
    int/float: La suma de a y b.
    """
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Ambos argumentos deben ser números enteros o flotantes")
    return a + b

# Prueba de la función
try:
    resultado = sumar(3, 4)
    print(f"El resultado de la suma es: {resultado}")
except ValueError as e:
    print(e)
