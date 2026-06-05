
from gerenciador_arquivos import (
    listar_documentos,
    listar_documentos_organizados,
    buscar_documento,
    adicionar_documento,
    ler_documento,
    renomear_documento,
    remover_documento
)

from gerenciador_diretorios import (
    listar_diretorios,
    criar_diretorio,
    remover_diretorio
)

while True:

    print("\n===== BIBLIOTECA DIGITAL =====\n")

    print("1 - Listar documentos")
    print("2 - Listar documentos organizados")
    print("3 - Buscar documento")
    print("4 - Adicionar documento")
    print("5 - Ler documento")
    print("6 - Renomear documento")
    print("7 - Remover documento")
    print("8 - Listar diretórios")
    print("9 - Criar diretório")
    print("10 - Remover diretório")
    print("0 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        listar_documentos()

    elif opcao == "2":
        listar_documentos_organizados()

    elif opcao == "3":
        buscar_documento()

    elif opcao == "4":
        adicionar_documento()

    elif opcao == "5":
        ler_documento()

    elif opcao == "6":
        renomear_documento()

    elif opcao == "7":
        remover_documento()

    elif opcao == "8":
        listar_diretorios()

    elif opcao == "9":
        criar_diretorio()

    elif opcao == "10":
        remover_diretorio()

    elif opcao == "0":

        print("\nEncerrando sistema...")
        break

    else:

        print("\nOpção inválida.")
