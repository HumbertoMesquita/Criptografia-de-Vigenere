import string
import os

# Lista de caracteres suportados (letras, números, espaços)
caracteres_validos = string.printable  # 100 caracteres (~do espaço até o ~)
#0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ \t\n\r\x0b\x0c


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def gerar_chave(mensagem, chave):
    
    #Gera uma chave repetida com mesmo comprimento da mensagem.
    
    chave = list(chave)
    if len(chave) == len(mensagem):
        return "".join(chave)
    else:
        for i in range(len(mensagem) - len(chave)):
            chave.append(chave[i % len(chave)])
    return "".join(chave)

def criptografar(mensagem, chave):
    
    #Criptografa a mensagem usando a cifra de Vigenère.
    
    chave = gerar_chave(mensagem, chave)
    resultado = ""

    for m, k in zip(mensagem, chave):
        if m in caracteres_validos and k in caracteres_validos:
            i_m = caracteres_validos.index(m)
            i_k = caracteres_validos.index(k)
            i_c = (i_m + i_k) % len(caracteres_validos)
            resultado += caracteres_validos[i_c]
        else:
            resultado += m  # Se não for válido, mantém o caractere original

    return resultado

def decriptografar(mensagem_cifrada, chave):
    
    #Decriptografa a mensagem usando a cifra de Vigenère.
    
    chave = gerar_chave(mensagem_cifrada, chave)
    resultado = ""

    for c, k in zip(mensagem_cifrada, chave):
        if c in caracteres_validos and k in caracteres_validos:
            i_c = caracteres_validos.index(c)
            i_k = caracteres_validos.index(k)
            i_m = (i_c - i_k) % len(caracteres_validos)
            resultado += caracteres_validos[i_m]
        else:
            resultado += c

    return resultado

def menu():
    while True:
        limpar_tela()
        print("=" * 40)
        print("    Cifra de Vigenère")
        print("=" * 40)
        print("1. Criptografar mensagem")
        print("2. Decriptografar mensagem")
        print("3. Sair")
        print("=" * 40)
        opcao = input("Escolha uma opção (1-3): ")

        if opcao == '1':
            mensagem = input("\nDigite a mensagem que deseja criptografar:\n> ")
            chave = input("Digite a chave:\n> ")
            resultado = criptografar(mensagem, chave)
            print("\n Mensagem criptografada:\n", resultado)

        elif opcao == '2':
            mensagem = input("\nDigite a mensagem criptografada:\n> ")
            chave = input("Digite a chave usada na criptografia:\n> ")
            resultado = decriptografar(mensagem, chave)
            print("\n Mensagem decriptografada:\n", resultado)

        elif opcao == '3':
            print("\nEncerrando o programa. Até logo!")
            break

        else:
            print("\n Opção inválida. Tente novamente.")

        input("\nPressione Enter para continuar...")

# Início do programa
if __name__ == "__main__":
    menu()
