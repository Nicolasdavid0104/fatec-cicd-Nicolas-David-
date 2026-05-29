import sys
import os
import pytest

# Força o Python a encontrar o main.py na pasta de cima
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import saudacao, calcular_media

class TestSaudacao:
    def test_saudacao_nome_valido(self):
        resultado = saudacao("Nicolas")
        assert "Nicolas" in resultado

    def test_saudacao_tipo_invalido(self):
        with pytest.raises(TypeError):
            saudacao(123)

class TestCalcularMedia:
    def test_media_simples(self):
        assert calcular_media([10, 8, 6]) == 8.0

    def test_lista_vazia(self):
        with pytest.raises(ValueError):
            calcular_media([])
