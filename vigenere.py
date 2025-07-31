import os

# Função para limpar a tela do terminal após uma interação completa

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função que gera uma chave do mesmo tamanho da mensagem
# A chave original é repetida até igualar o tamanho da mensagem

def gerar_chave(mensagem, chave):
    chave = list(chave)
    if len(chave) == len(mensagem):
        return "".join(chave)
    else:
        for i in range(len(mensagem) - len(chave)):
            chave.append(chave[i % len(chave)])
    return "".join(chave)

# Função de criptografia usando a cifra de Vigenère

def criptografar(mensagem, chave):
    mensagem = mensagem.upper()                # Converte a mensagem para letras maiúsculas
    chave = gerar_chave(mensagem, chave.upper())  # Gera uma chave com mesmo tamanho
 
    # Para cada letra da mensagem e da chave:

    for m, k in zip(mensagem, chave):
        if m.isalpha():  # Criptografa apenas letras
            # Soma os códigos das letras e aplica módulo 26
            c = chr(((ord(m) + ord(k)) % 26) + ord('A'))
            criptografada.append(c)

        else:
            # Mantém espaços, números e pontuação
            criptografada.append(m)

    return "".join(criptografada)

# Função de decriptografia da cifra de Vigenère
def decriptografar(cifrada, chave):
    cifrada = cifrada.upper()
    chave = gerar_chave(cifrada, chave.upper())
    original = []

    # Para cada letra da mensagem cifrada e da chave:
    for c, k in zip(cifrada, chave):
        if c.isalpha():  # Decriptografa apenas letras
            # Subtrai os códigos das letras e aplica módulo 26
            o = chr(((ord(c) - ord(k) + 26) % 26) + ord('A'))
            original.append(o)
        else:
            # Mantém espaços, números e pontuação
            original.append(c)

    return "".join(original)

# Função com menu interativo
def menu():
    while True:
        limpar_tela()  # Limpa a tela a cada nova execução do menu
        print("=" * 40)
        print("       Cifra de Vigenère")
        print("=" * 40)
        print("1. Criptografar mensagem")
        print("2. Decriptografar mensagem")
        print("3. Sair")
        print("=" * 40)
        opcao = input("Escolha uma opção (1-3): ")

        if opcao == '1':
            # Entrada da mensagem e chave para criptografar
            mensagem = input("\n Digite a mensagem a ser criptografada: ")
            chave = input("Digite a chave: ")
            resultado = criptografar(mensagem, chave)
            print("\n Mensagem criptografada:\n", resultado)

        elif opcao == '2':
            # Entrada da mensagem cifrada e chave para decriptografar
            mensagem = input("\n Digite a mensagem criptografada: ")
            chave = input("Digite a chave usada na criptografia: ")
            resultado = decriptografar(mensagem, chave)
            print("\n Mensagem original:\n", resultado)

        elif opcao == '3':
            # Encerra o programa
            print("\n Encerrando o programa !")
            break

        else:
            # Mensagem de erro para opção inválida
            print("\n Opção inválida. Tente novamente.")

        # Pausa antes de voltar ao menu
        input("\n Pressione Enter para continuar...")

# Ponto de entrada do programa
if __name__ == "__main__":
    menu()
