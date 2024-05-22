from util_dados import carregar_dados_destinatarios
from gerador_certificado import gerar_certificado

def main():
    dados_destinatarios = carregar_dados_destinatarios('dados/destinatarios.csv')
    for destinatario in dados_destinatarios:
        gerar_certificado(destinatario)

if __name__ == "__main__":
    main()
