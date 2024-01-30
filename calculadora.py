# Módulo a ser testado: calculadora.py

def divisao(dividendo, divisor):
    if divisor == 0:
        raise ValueError("O divisor não pode ser zero.")
    return dividendo / divisor
