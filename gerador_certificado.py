from PIL import Image, ImageDraw, ImageFont
import os

def gerar_certificado(destinatario):
    # Carregar modelo de certificado
    caminho_modelo = 'modelo/modelo_certificado.png'
    certificado = Image.open(caminho_modelo)

    # Adicionar nome do destinatário ao certificado
    draw = ImageDraw.Draw(certificado)
    fonte = ImageFont.truetype("arial.ttf", 30)
    draw.text((200, 200), f"Certificado de Conclusão\n{destinatario['nome']}", (0, 0, 0), font=fonte)

    # Salvar o certificado gerado
    diretorio_saida = 'saida'
    if not os.path.exists(diretorio_saida):
        os.makedirs(diretorio_saida)
    certificado.save(os.path.join(diretorio_saida, f"Certificado_{destinatario['nome']}.png"))
