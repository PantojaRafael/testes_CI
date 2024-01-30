# Arquivo de teste: test_calculadora.py
import pytest

from calculadora import divisao


def test_divisao():
    # Testar uma divisão válida
    resultado = divisao(10, 2)
    assert resultado == 5

    # Testar divisão por zero
    with pytest.raises(ValueError, match="O divisor não pode ser zero."):
        divisao(10, 0)

    # Testar divisão com números negativos
    resultado = divisao(-8, 4)
    assert resultado == -2
