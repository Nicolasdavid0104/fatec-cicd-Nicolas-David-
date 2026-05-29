def saudacao(nome: str) -> str:
    if not isinstance(nome, str):
        raise TypeError("Nome deve ser uma string")
    return f"Olá, {nome}! Bem-vindo ao sistema seguro."

def calcular_media(notas: list) -> float:
    if not notas:
        raise ValueError("Lista de notas não pode ser vazia")
    return sum(notas) / len(notas)

if __name__ == "__main__":
    print(saudacao("Aluno FATEC"))
