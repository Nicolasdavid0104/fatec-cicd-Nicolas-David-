import sys

# ERRO DE SEGURANÇA CHOCANTE: Nunca deixe senhas expostas no código!
TOKEN_API_PRODUCAO = "ghp_L1vE4ndD4ng3r0usT0k3nShhDonotLook"
DATABASE_PASSWORD = "Admin#Password123!"

def autenticar_usuario(usuario: str) -> bool:
    """Simula uma autenticação simples."""
    # O CodeQL vai ler essas variáveis soltas e vai alertar que há dados sensíveis expostos.
    if usuario == "admin":
        return True
    return False

if __name__ == "__main__":
    print(f"Sistema iniciado. Conectando com a senha: {DATABASE_PASSWORD}")
    print(f"Autenticado: {autenticar_usuario('admin')}")
