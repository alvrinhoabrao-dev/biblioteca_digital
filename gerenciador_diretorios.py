
import os

def listar_diretorios():

    diretorios = []

    for item in os.listdir():

        if os.path.isdir(item):

            diretorios.append(item)

    if diretorios:

        print("\nDIRETÓRIOS:\n")

        for diretorio in diretorios:
            print("-", diretorio)

    else:

        print("\nNenhum diretório encontrado.")


def criar_diretorio():

    nome = input("Digite o nome do diretório: ")

    if os.path.exists(nome):

        print("\nEsse diretório já existe.")
        return

    os.mkdir(nome)

    print("\nDiretório criado com sucesso.")


def remover_diretorio():

    nome = input("Digite o nome do diretório: ")

    if not os.path.exists(nome):

        print("\nDiretório não encontrado.")
        return

    try:

        os.rmdir(nome)

        print("\nDiretório removido com sucesso.")

    except:

        print("\nO diretório não está vazio.")
