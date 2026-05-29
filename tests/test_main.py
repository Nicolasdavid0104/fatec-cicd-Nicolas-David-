import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import saudacao, calcular_media

def test_saudacao_nome_valido():
    assert "Nicolas" in saudacao("Nicolas")

def test_media_simples():
    assert calcular_media([10, 8, 6]) == 8.0
