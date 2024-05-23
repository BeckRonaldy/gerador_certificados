# Gerador de Certificados

### Funcionamento:
Para gerar um certificado, são carregados os dados dos alunos fornecidos através de um arquivo .CSV, junto aos dados também é carregado um modelo de certificado em .PNG, a partir disso gera um certificado unindo as informações dos alunos contidas no .CSV com o modelo de certificado, gerando um certificado .PNG
#
### Exemplo:
_Imagem modelo para o certificado_

<img src="modelo/modelo_certificado.png" alt="Exemplo de certificado gerado" style="width:400px;">

_Dados contidos no arquivo .CSV_

|        nome        |        email        |
|--------------------|---------------------|
|   Nome do Aluno A  |  aluno_a@gmail.com  |
|   Nome do Aluno B  |  aluno_b@gmail.com  | 
|   Nome do Aluno C  |  aluno_c@gmail.com  |
|   Nome do Aluno D  |  aluno_d@gmail.com  |
#
### Resultado:
Os dados do arquivo .CSV são posicionados e escritos sobre o modelo inserido, gerando o certificado:

<img src="modelo/certificado_gerado.png" alt="Exemplo de certificado gerado" style="width:400px;">

O gerador repete o processo para todas as linhas da coluna "nome" informado no .CSV, os certificados gerados são armazenados no diretório "saida/" do projeto.

#
_Esta é uma versão demonstrativa utilizada apenas para estudo de caso_
