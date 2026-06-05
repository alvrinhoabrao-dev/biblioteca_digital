
import os

PASTA_DOCUMENTOS = "documentos"

if not os.path.exists(PASTA_DOCUMENTOS):
    os.makedirs(PASTA_DOCUMENTOS)


def listar_documentos():

    arquivos = os.listdir(PASTA_DOCUMENTOS)

    if arquivos:

        print("\nDOCUMENTOS DISPONÍVEIS:\n")

        for arquivo in arquivos:
            print("-", arquivo)

    else:

        print("\nNenhum documento encontrado.")


def adicionar_documento():

    nome = input("Digite o nome do documento: ")

    caminho = os.path.join(PASTA_DOCUMENTOS, nome)

    if os.path.exists(caminho):

        print("\nJá existe um documento com esse nome.")
        return

    print("\nTipos disponíveis:")
    print("1 - Livro")
    print("2 - Artigo")
    print("3 - Revista")
    print("4 - eBook")

    opcao = input("\nEscolha o tipo: ")

    tipos = {
        "1": "Livro",
        "2": "Artigo",
        "3": "Revista",
        "4": "eBook"
    }

    if opcao not in tipos:

        print("\nTipo inválido.")
        return

    tipo = tipos[opcao]

    ano = input("Digite o ano de publicação: ")

    conteudo = input("Digite o conteúdo do documento: ")

    with open(caminho, "w") as arquivo:

        arquivo.write(f"TIPO: {tipo}\n")
        arquivo.write(f"ANO: {ano}\n\n")
        arquivo.write(conteudo)

    print("\nDocumento criado com sucesso.")


def ler_documento():

    nome = input("Digite o nome do documento: ")

    caminho = os.path.join(PASTA_DOCUMENTOS, nome)

    if not os.path.exists(caminho):

        print("\nDocumento não encontrado.")
        return

    with open(caminho, "r") as arquivo:

        print("\nCONTEÚDO:\n")
        print(arquivo.read())


def renomear_documento():

    nome_antigo = input("Nome atual do documento: ")
    novo_nome = input("Novo nome do documento: ")

    caminho_antigo = os.path.join(PASTA_DOCUMENTOS, nome_antigo)
    caminho_novo = os.path.join(PASTA_DOCUMENTOS, novo_nome)

    if not os.path.exists(caminho_antigo):

        print("\nDocumento não encontrado.")
        return

    os.rename(caminho_antigo, caminho_novo)

    print("\nDocumento renomeado com sucesso.")


def remover_documento():

    nome = input("Digite o nome do documento: ")

    caminho = os.path.join(PASTA_DOCUMENTOS, nome)

    if not os.path.exists(caminho):

        print("\nDocumento não encontrado.")
        return

    os.remove(caminho)

    print("\nDocumento removido com sucesso.")


def buscar_documento():

    termo = input("Digite o termo de busca: ").lower()

    arquivos = os.listdir(PASTA_DOCUMENTOS)

    encontrados = []

    for arquivo in arquivos:

        if termo in arquivo.lower():

            encontrados.append(arquivo)

    if encontrados:

        print("\nDOCUMENTOS ENCONTRADOS:\n")

        for arquivo in encontrados:
            print("-", arquivo)

    else:

        print("\nNenhum documento encontrado.")


def listar_documentos_organizados():

    arquivos = os.listdir(PASTA_DOCUMENTOS)

    organizacao = {}

    for nome_arquivo in arquivos:

        caminho = os.path.join(PASTA_DOCUMENTOS, nome_arquivo)

        if not os.path.isfile(caminho):
            continue

        try:

            with open(caminho, "r") as arquivo:

                tipo_linha = arquivo.readline().strip()
                ano_linha = arquivo.readline().strip()

            if not tipo_linha.startswith("TIPO:"):
                continue

            if not ano_linha.startswith("ANO:"):
                continue

            tipo = tipo_linha.replace("TIPO:", "").strip()
            ano = ano_linha.replace("ANO:", "").strip()

            if tipo not in organizacao:
                organizacao[tipo] = {}

            if ano not in organizacao[tipo]:
                organizacao[tipo][ano] = []

            organizacao[tipo][ano].append(nome_arquivo)

        except:

            continue

    if not organizacao:

        print("\nNenhum documento organizado encontrado.")
        return

    print("\nDOCUMENTOS ORGANIZADOS\n")

    for tipo in organizacao:

        print(f"\n{tipo.upper()}")

        for ano in organizacao[tipo]:

            print(f"  {ano}")

            for documento in organizacao[tipo][ano]:

                print(f"    - {documento}")
