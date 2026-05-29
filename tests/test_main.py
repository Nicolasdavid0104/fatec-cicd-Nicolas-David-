import sys
import os
import pytest

# Força o Python a encontrar o main.py na raiz
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Puxa a função vulnerável que você colocou no main.py
from main import executar_comando_vulneravel

def test_comando_vulneravel_execucao():
    # Esse teste vai rodar a função, mas nós queremos que ele FALHE de propósito
    # para gerar a sua pipeline vermelha do relatório.
    resultado = executar_comando_vulneravel("teste")
    
    # Força um erro: como a função usa os.system(), ela não retorna texto, retorna None.
    # Ao comparar com "sucesso", o teste quebra com X vermelho de forma limpa!
    assert resultado == "sucesso"
