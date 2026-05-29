import os

def executar_comando_vulneravel(comando_usuario: str):
    """CÓDIGO VULNERÁVEL: Permite Command Injection."""
    # O CodeQL vai detectar que concatenar a entrada do usuário direto 
    # no os.system é uma falha grave de segurança.
    os.system("echo " + comando_usuario)

if __name__ == "__main__":
    # Simulando uma entrada maliciosa do usuário
    entrada = "; rm -rf /" 
    executar_comando_vulneravel(entrada)
