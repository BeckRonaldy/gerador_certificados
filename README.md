# Gerador de Certificados

### Funcionamento:
Este gerador de certificados carrega os dados como nome e e-mail dos alunos, fornecidos através de um arquivo .CSV, ele também carrega um modelo base do certificado em .PNG e a partir disso, gera um certificado com as informações dos alunos contidas no .CSV
#
### Exemplo:
Neste exemplo foi utilizada essa imagem como um modelo base para o certificado:

<img src="modelo/modelo_certificado.png" alt="Exemplo de certificado gerado" style="width:400px;">

Os dados contidos no arquivo .CSV são os seguintes:

|        nome        |        email        |
|--------------------|---------------------|
|   Nome do Aluno A  |  aluno_a@gmail.com  |
|   Nome do Aluno B  |  aluno_b@gmail.com  | 
|   Nome do Aluno C  |  aluno_c@gmail.com  |
|   Nome do Aluno D  |  aluno_d@gmail.com  |
#
### Resultado:
O gerado carrega os dados so aluno e os escreve sobre o modelo de certificado:

<img src="modelo/certificado_gerado.png" alt="Exemplo de certificado gerado" style="width:400px;">

O gerador repete o processo para todos os alunos informador no .CSV e armazena os certificados gerados no diretório "saida/" do projeto.

#
_Esta é uma versão demonstrativa utilizada apenas para estudo de caso_
