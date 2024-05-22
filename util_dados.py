import csv

def carregar_dados_destinatarios(caminho_arquivo):
    dados_destinatarios = []
    with open(caminho_arquivo, 'r') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            dados_destinatarios.append(linha)
    return dados_destinatarios
