# Como Usar o Sistema:

#### Autores: Leonor Franco Marques (a107248) e Leonor Pereira Mendes (a107284)
#### Data: 2025/01/05

Este sistema tem como objetivo criar, atualizar e manipular registos de publicações científicas, permitindo a inserção, edição, remoção e consulta de dados de uma maneira eficaz. É constituído por uma Interface de Linha de Comando e uma Interface Gráfica. Apresentamos aqui as instruções para a sua utilização:

## Requisitos
* Python 3.8
* Matplotlib
* FreeSimpleGUI ou PySimpleGUI
* Arquivo JSON (para carregamento dos registos iniciais)

## Opções Disponíveis
1. **Carregar Ata Médica**: Carrega os dados de um ficheiro JSON para manipulação. 
2. **Guardar Ata Médica**: Guarda os dados manipulados num ficheiro JSON.
3. **Inserir Registo**: Insere um novo registo à base de dados. São solicitadas ao utilizador informações como: abstract, palavras-chave, autores, DOI, link do PDF, data de publicação, título do registo e URL.
4. **Apagar Registo por Título**: Apaga um registo existente com base num título fornecido pelo utilizador.
5. **Consultar Registo**: Filtra os registos com base no título, autor, afiliação, data de publicação ou palavras-chave. Os resultados podem ser ordenados por data de publicação ou por ordem alfabética de título. Estes são guardados num ficheiro, cujo nome é imposto pela aplicação.
6. **Listar Autores**: Gera listas de autores ordenadas por ordem alfabética ou por frequência das suas publicações. Permite também aceder ao URL de um registo específico de algum autor.
7. **Atualização dos Dados de uma Publicação**: Atualiza campos específicos de um registo, com base no seu título ou DOI (caso o registo não tenha título).
8. **Análise de Publicações**: Analisa os registos por frequência de palavras-chave ou por ordem alfabética. Pode também aceder aos registos com uma determinada palavra-chave.
9. **Estatísticas**: Permite a visualização de gráficos de distribuição de autores, publicações e palavras-chave.
10. **Sair**: Encerra o sistema.

## Interface Gráfica

Para realizar cada opção deve escrever o seu número correspondente na caixa de entrada. Deve confirmar cada operação, clicando no botão "Enviar" ou "Ok".

### Navegação Inicial:
1. **Carregar Ata Médica**: Digite o número 1. Insira o nome do ficheiro JSON que quer carregar.
2. **Guardar Ata Médica**: Digite o número 2. Insira o nome do ficheiro JSON que quer guardar.
3. **Inserir Registo**: Digite o número 3. Siga as etapas do formulário para adicionar um novo registo.
4. **Apagar Registo por Título**: Digite o número 4. Insira o título do registo a ser removido.

### Consultas:

Digite o número 5. Clicando nos botões, pode selecionar o critério de consulta. Deve preencher os requisitos que o sistema peça, para assim obter a consulta mediante esses requisitos. Pode visualizar o resultado diretamente no ecrã ou no ficheiro que foi guardado com este (cujo nome é fornecido pelo sistema).

### Listagem de Autores e Acesso aos Artigos:

Digite o número 6. Clicando nos botões, pode selecionar o critério de listagem. Deve preencher os requisitos que o sistema peça, para assim obter a listagem mediante esses requisitos. Pode visualizar o resultado da listagem diretamente no ecrã. Pode também aceder aos artigos de algum autor em específico, através do seu URL.

### Atualização dos Dados de uma Publicação:

Digite o número 7. Insira o título do registo que quer atualizar ou o seu DOI (caso o registo não tenha título). Após isso, deverá preencher os campos que quer atualizar, com as novas informações.

### Análise de Publicações:

Digite o número 8. Clicando nos botões, pode selecionar o critério de análise de publicações e visualizar o resultado diretamente no ecrã ou no ficheiro que foi guardado com este (cujo nome foi fornecido pelo sistema). Para além disso, pode também aceder às publicações que tenham uma palavra-chave específica. O resultado é mostrado diretamente no ecrã.

### Estatística de Publicações:

Digite o número 9. Clicando nos botões, pode escolher um dos critérios estabelecidos e visualizar o correspondente gráfico. Se necessário, deve preencher os requisitos que o sistema peça, para assim obter o gráfico correspondente.

### Sair:

Clique no botão "Sair".

## Interface de Linha de Comando (CLI)

Para realizar cada opção deve escrever o seu número correspondente na caixa de entrada.

### Navegação Inicial:
1. **Carregar Ata Médica**: Digite o número 1 e insira o nome do ficheiro JSON que quer carregar.
2. **Guardar Ata Médica**: Digite o número 2 e insira o nome do ficheiro JSON que quer guardar.
3. **Inserir Registo**: Digite o número 3 e siga as etapas do formulário para adicionar um novo registo.
4. **Apagar Registo por Título**: Digite o número 4 e insira o título do registo a ser removido.

### Consultas:

Digite um dos seguintes números: 5, 6, 7, 8 ou 9. Cada um deles corresponde a um critério de consulta diferente. Pode visualizar os resultados de cada consulta nos ficheiros em que foram guardados (cujo nome é fornecido pelo sistema).

### Listagem de Autores e Acesso aos Artigos:

Digite o número 10 ou 11. Cada um deles corresponde a um critério de listagem diferente. Pode visualizar os resultados de cada listagem nos ficheiros em que foram guardados (cujo nome é fornecido pelo sistema). 
Posteriormente, se pretender aceder aos artigos de algum autor em específico, digite o número 1. Senão, digite o número 2.
Se selecionou o número 1: digite o nome do autor que quer consultar. A listagem de títulos desse autor é exibida no ecrã. Introduza um dos títulos presentes nessa listagem e, assim, terá acesso ao URL correspondente, que lhe dá acesso ao artigo.

### Atualização dos Dados de uma Publicação:

Digite o número 12. Insira o título do registo que quer atualizar ou o seu DOI (caso o registo não tenha título). Após isso, deverá preencher os campos que quer atualizar, com as novas informações.

### Análise de Publicações:

Digite o número 13 ou 14. Cada um deles corresponde a um critério de análise de publicações diferente. Pode visualizar os resultados de cada análise nos ficheiros em que foram guardados (cujo nome é fornecido pelo sistema). 
Posteriormente, se pretender aceder aos artigos que tenham uma palavra-chave específica, digite o número 1. Senão, digite o número 2.
Se selecionou o número 1: digite a palavra-passe que quer analisar. Os resultados dessa pesquisa são guardados num ficheiro (cujo nome é fornecido pelo sistema).

### Estatística de Publicações:

Digite um dos seguintes números: 15, 16, 17, 18, 19 ou 20. Cada um deles corresponde a um critério diferente, a partir do qual é gerado um gráfico correspondente.
Caso seja necessário um requisito extra para gerar o gráfico, deve introduzi-lo.

### Sair:

Digite o número 0 para encerrar o sistema.

## Observações
* Antes de realizar qualquer operação tem de realizar a opção 1 ("Carregar Ata Médica"), pois as operações só podem ser realizadas após o carregamento de uma ata médica.
* Certifique-se que guarda os dados antes de encerrar o sistema, para evitar a perda de qualquer informação.
* Certifique-se que os ficheiros que permitem o funcionamento da aplicação e os ficheiros que pretende carregar estão na mesma pasta, sendo nesta pasta que a aplicação vai trabalhar. Todos os ficheiros gerados pela aplicação vão ser guardados nessa mesma pasta.