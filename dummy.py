# Importando bibliotecas necesarias
import math

# Función para calcular el cuadrado de un número
def calcular_cuadrado(numero):
    """Devuelve el cuadrado del número dado.
    texto
    texto
    texto"""
    return numero ** 2

# Función para calcular el área de un círculo
def calcular_area_circulo(radio):
    '''Devuelve el área de un círculo dado su radio.
    lalala
    lalala
    '''
    return math.pi * (radio ** 2)

# Función principal para demostrar la funcionalidad
def main():
    """Función principal para ejecutar el script."""
    # Ejemplo de uso de calcular_cuadrado
    num = 5
    print(f"El cuadrado de {num} es {calcular_cuadrado(num)}")

    # Ejemplo de uso de calcular_area_circulo
    radio = 3
    print(f"El área de un círculo con radio {radio} es {calcular_area_circulo(radio)}")

# Asegurando que el script se ejecute solo cuando se llama directamente
if __name__ == "__main__":
    main()
