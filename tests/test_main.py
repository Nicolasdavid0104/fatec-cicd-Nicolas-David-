import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import autenticar_usuario

def test_autenticacao_falsa():
    # Nós sabemos que o usuário 'comum' deve retornar False
    resultado = autenticar_usuario("comum")
    
    # Mas vamos forçar o teste a esperar True. 
    # Isso vai fazer o Pytest estourar um X Vermelho na pipeline!
    assert resultado is True
