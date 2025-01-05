### Exemplo de Execução

O exemplo que se segue demonstra como usar a aplicação para explorar a sua lista de registos, utilizando a interface de linha de comando. Na aplicação é apresentado um menu em que cada número está associado a uma funcionalidade. Segue-se o menu e um exemplo de como usar a aplicação:

Introduza a opção:
    1 - Carregar Ata Médica
    2 - Guardar Ata Médica
    3 - Inserir Registo
    4 - Apagar Registo por Título
    5 - Consultar Registo
    6 - Listar Autores
    7 - Atualização dos Dados de uma Publicação
    8 - Análise de Publicações
    9 - Estatísticas

**Opção 1** : Carregar um ficheiro JSON
* Ação: digitar o número 1
* Entrada: Insira o nome do ficheiro que pretende carregar, por exemplo, ata_medica_papers.json.
* Saída esperada: O seu ficheiro foi carregado com sucesso!

**Opção 2**: Guardar Ata Médica
* Ação: digitar o número 2
* Entrada: Insira o nome do ficheiro onde pretende guardar a sua base de dados, por exemplo, minha_ata_medica.json.
* Saída esperada: A sua base de dados foi guardada com sucesso!

**Opção 3**: Inserir Registo
* Ação: digitar o número 3
* Entrada: Preencher os campos dos novo registo
    * Abstract: Resumo da publicação
    * Palavras-chave: Hospital
    * Número de autores: 2
    * Nome do 1º autor: Augusto Fernandes
    * Afiliação do 1º autor: Universidade do Porto
    * ORCID: https://orcid.org/...
    * Nome do 2º autor: Débora Peixoto
    * Afiliação do 2º autor: Universidade do Minho
    * ORCID: (deixar vazio caso não houver/souber, e faça o mesmo para os restantes campos)
    * DOI: https://doi.org/...
    * Link do PDF: https://www.actamedicaexemplo.com/...
    * Data: 2025-01-05
    * Título: Condições hospitalares
    * URL: http://www.exemplo.com/...
* Saída esperada: Registo inserido com sucesso!

**Opção 4**: Apagar Registo por Título
* Ação: digitar o número 4
* Entrada: Insira o título do registo que pretende apagar, por exemplo, Condições hospitalares
* Saída esperada: O seu ficheiro foi apagado com sucesso!

**Opção 5**: Consultar Registo
* Ação: digitar o número 5.
* Entrada: Selecionar um dos botões e preencher o campo pedido. Exemplo:
    * Carregar no botão: Consultar por Palavra-chave
    * Carregar no botão: Por Data
    * Introduza a Palavra-Chave: Hospitalização
    * Saída esperada: O resultado foi salvo no ficheiro: consultarPalavra_Chave_Data.txt
    * Deseja abrir/consultar esse ficheiro?: Carregar no botão Sim
    * Saída esperada: Conteúdo do ficheiro: consultarPalavra_Chave_Data.txt ...

**Opção 6**: Listar Autores
* Ação: digitar o número 6
* Entrada: Selecionar um dos botões. Exemplo:
    * Carregar no botão: Por Frequência
    * Deseja aceder aos artigos de algum autor? Carregar no botão Sim
    * Introduza o autor que pretende consultar: Ricardo Fonseca
    * Clicar no botão Consultar
    * Selecione um título para consultar mais informações: Doenças Cardiovasculares
    * Clicar no botão Aceder ao URL
    * Saida esperada: URL: http://www.exemplo.com/...

**Opção 7**: Atualização dos Dados de uma Publicação
* Ação: digitar o número 7
* Entrada: Preencher os campos do registo a atualizar
    * Título: Colheitas de Sangue
    * DOI: (Deixar em branco se preencheu o título. Caso o registo que está a atualizar não tenha título deve preencher o DOI. Estes dois campos não podem ficar simultaneamente vazios!)
    * Abstract: Resumo da publicação
    * Palavras-chave: Seringas
    * Data: 2023-11-25
    * Número de autores: 1
    * Nome do 1º autor: Augusto Fernandes
    * Afiliação do 1º autor: (deixar vazio caso não houver/souber, e faça o mesmo para os restantes campos)
* Saída esperada: O registo foi atualizado com sucesso!

**Opção 8**: Análise de Publicações
* Ação: digitar o número 8
* Entrada: Selecionar um dos botões. Exemplo:
    * Carregar no botão: Ordenada Alfabeticamente
    * Saida esperada: O resultado foi salvo no ficheiro: palavras_chave_ord_alf.txt
    * Deseja abrir/consultar esse ficheiro? Carregar no botão Sim
    * Selecione uma Palavra-Chave para consultar mais informações: Seringas
    * Clicar no botão Publicações com esta Palavra-Chave
    * Conteúdo do ficheiro: pubs_pal_selecionada.txt ...

**Opção 9**: Estatísticas
* Ação: digitar o número 9
* Entrada: Selecionar um dos botões. Exemplo:
    * Carregar no botão: Por Mês de um Determinado Ano
    * Introduza o Ano que Pretende Analisar: 2021
    * Clicar no Ok
* Saida esperada: gráfico da distribuição 
