import time

# Sistema fictício com usuário e senha (somente para simulação)
USUARIO_CORRETO = "admin"
SENHA_CORRETA = "1234"

# Wordlist totalmente fictícia para simulação
wordlist = [
    "0000", "1111", "2222", "3333",
    "1234", "4321", "9999"
]

def tentativa_login(usuario, senha):
    """Simula uma verificação de login sem acesso real a nenhum sistema."""
    time.sleep(0.3)  # simula o tempo de resposta
    return usuario == USUARIO_CORRETO and senha == SENHA_CORRETA

def brute_force(usuario):
    print("=== SIMULAÇÃO DE BRUTE FORCE ===\n")

    for tentativa in wordlist:
        print(f"Tentando senha: {tentativa}...")
        if tentativa_login(usuario, tentativa):
            print("\n[SENHA ENCONTRADA]")
            print(f"Usuário: {usuario}")
            print(f"Senha: {tentativa}")
            return

    print("\nNenhuma senha da wordlist funcionou.")

if __name__ == "__main__":
    brute_force("admin")
