# **Relatório sobre o “Sistema de Consulta e Análise de Publicações Científicas”**

#### Data: 2025.01.05
#### Autores: Leonor Franco Marques (a107248), Leonor Pereira Mendes (a107284)


Este relatório tem como objetivo dar a conhecer e relacionar os códigos desenvolvidos nos ficheiros “Projeto_App_Interface.py”, “Projeto_App.py” e “Projeto.py”. Estes ficheiros em Python são os constituintes do nosso projeto “Sistema de Consulta e Análise de Publicações Científicas”, desenvolvido para a unidade curricular “Algoritmos e Técnicas de Programação” no ano 2024/2025.

Este projeto permite criar, analisar e atualizar diversas publicações científicas, que estão expostas num dataset de publicações (como o dataset “ata_medica_papers.json” que nos foi fornecido). O sistema permite, então, realizar pesquisas sobre os artigos presentes num dataset, utilizando todos os filtros de pesquisa considerados relevantes. Para além disso, foram também gerados gráficos com diversas estatísticas sobre os artigos referidos.

Distribuímos este projeto em três ficheiros Python, estabelecendo assim uma separação entre a Interface de Linha de Comando (presente no ficheiro “Projeto_App.py”), a Interface Gráfica (ficheiro “Projeto_App_Interface.py”) e o ficheiro controlador do projeto (ficheiro “Projeto.py”).
Primeiramente, o ficheiro “Projeto.py” contém todas as funções necessárias para o correto funcionamento das tarefas exigidas pela aplicação. 
Por sua vez, no ficheiro “Projeto_App.py” encontram-se todas as instruções que controlam a troca de informações entre a interface e as funções do ficheiro “Projeto.py”. Neste ficheiro está implementado um menu, no qual cada funcionalidade está associada a um número. O utilizador, ao selecionar um número, a aplicação realiza a funcionalidade associada a este. 
Finalmente, o ficheiro “Projeto_App_Interface.py” permite a apresentação da interface gráfica ao utilizador. Utilizamos diversos elementos visuais como botões, labels e caixas de entrada. Todos estes estão organizados através de estruturas de layout que determinam o seu posicionamento e alinhamento no ecrã. São também definidos eventos que permitem a interação do utilizador com a aplicação.


### **1. Funções de Entrada e Saída de Dados**
**verificar_arquivo_existente(ficheiro)** - Verifica se determinado ficheiro existe na pasta onde o utilizador está a trabalhar.
* os.path.join: Junta a pasta e o nome do arquivo, criando o caminho completo do arquivo.
* os.path.isfile: Retorna True se o caminho especificado for um arquivo existente, e False caso contrário.

**carregarAta(fnome)** - Lê um arquivo JSON contendo registos médicos e retorna uma lista de dicionários representando esses registos. O seu funcionamento é o seguinte:
* Abre o arquivo especificado no modo de leitura (r).
* Utiliza o módulo json para carregar os dados e convertê-los numa estrutura Python. A estrutura utilizada foi uma lista de dicionários e denominamo-la de ata_med/ata_medica.
* De seguida fecha o ficheiro e retorna os dados (lista de dicionários).

O ficheiro “Projeto_App.py” verifica se o arquivo tem a extensão .json e exibe mensagens de erro caso o carregamento falhe. No ficheiro “Projeto_App_Interface.py” cria-se o layout para carregar atas médicas, em que apresenta um campo de entrada para o nome do ficheiro a carregar em JSON. Além disso, inclui botões para confirmar ou sair. Ambos os ficheiros verificam se o nome do ficheiro fornecido pelo utilizador existe na pasta onde está a trabalhar.

**guardarATA(fnome, lista)** - Guarda uma lista de atas médicas num ficheiro do tipo JSON. O seu funcionamento é o seguinte:
* Abre o ficheiro no modo de escrita (w).
* Utiliza a função json.dump para despejar a lista de dicionários no ficheiro, cujo nome foi fornecido.
* Fecha o ficheiro após guardar.

No ficheiro “Projeto_App.py” guarda-se a lista ata_med utilizada até ao momento num ficheiro, cujo o nome foi fornecido pelo utilizador. No ficheiro “Projeto_App_Interface.py” cria-se uma layout para guardar a lista ata_med, que apresenta um campo de entrada para o nome do ficheiro em JSON, onde o utilizador pretende guardar os registos. Além disso, inclui botões para confirmar ou sair.

**inserir(lista, reg)** - Insere um novo registo na lista de atas médicas. O seu funcionamento é o seguinte:
* Adiciona o dicionário reg à lista utilizando o .append().

O ficheiro “Projeto_App.py” permite ao utilizador adicionar um registo à lista de registos preenchendo campos como título, autores, data, palavras-chave, etc. A aplicação recebe os dados via input(). A cada campo que pode ser preenchido pelo utilizador verifica se está vazio ou não. Caso não seja uma string vazia, insere esse campo no dicionário reg. No final, valida se o registo contém pelo menos um campo preenchido antes de adicioná-lo. No ficheiro “Projeto_App_Interface.py” cria-se uma layout que permite ao utilizador adicionar um registo à lista de registos preenchendo campos como abstract, palavras-chave, título, data, palavras-chave, etc. Cria-se também outro layout em que pergunta os autores, as afiliações e o orcid. A cada campo que pode ser preenchido pelo utilizador verifica se está vazio ou não. Caso não seja uma string vazia, insere esse campo no dicionário registo. No final, valida se o registo contém pelo menos um campo preenchido antes de adicioná-lo.

**apagar(lista, titulo)** - Remove um registo da lista com base no título fornecido. O seu funcionamento é o seguinte:
* Percorre a lista para encontrar o índice do registo cujo título corresponde ao fornecido pelo utilizador.
* De seguida remove o registo utilizando o comando (del lista[índice]) caso o título que foi especificado seja encontrado.
* Retorna True se o registo foi removido, ou False caso não tenha sido encontrado.

No ficheiro “Projeto_App.py” permite ao utilizador introduzir o título do registo que pretende remover, via input (). Caso a condição devolvida pela função seja True, imprime uma mensagem a dizer que o registo foi apagado com sucesso. Caso contrário, informa o utilizador de que não foi possível encontrar esse título na lista de registos. No ficheiro “Projeto_App_Interface.py” cria uma layout em que permite ao utilizador fornecer o título do registo que pretende apagar. Caso a condição devolvida pela função seja True, imprime uma mensagem a dizer que o registo foi apagado com sucesso. Caso contrário, informa o utilizador de que não foi possível encontrar esse título na lista de registos.


### **2. Funções de Consulta**
Todas estas funções de consulta guardam o resultado da consulta efetuada num ficheiro, cujo nome é imposto pela aplicação.

**consultarTitulo_data(lista, titulo, ficheiro)** - Filtra registos com base no título fornecido e ordena por data. O seu funcionamento é o seguinte:
* Procura todos os registos que possuem o título fornecido pelo utilizador.
* Divide os registos em dois grupos: com e sem data.
* Posteriormente utiliza a lista dos registos com data e ordena-a utilizando a função sorted. De seguida, cria uma lista final em que guarda a lista dos registos com data ordenada e a lista dos registos sem data.
* Por último salva os resultados da consulta num ficheiro de texto (.txt).

**consultaAutor_data(lista, autor, ficheiro)** e **consultaAutor_tit(lista, autor, ficheiro)** - Filtra registros por autor e ordena por data ou por ordem alfabética de títulos, respetivamente. O funcionamento destas funções é o seguinte:
* Verifica se o autor, cujo nome foi fornecido pelo utilizador, está presente na lista de autores do registo.
* Divide os registos em dois grupos: com e sem data e com título e sem título respetivamente.
* Posteriormente, utiliza a lista dos registos com data (na função consultaAutor_data) e a lista dos registos com título (na função consultaAutor_tit) e ordena-as utilizando a função sorted. De seguida, cria uma lista final em que guarda a lista dos registos com data ordenada e a lista dos registos sem data, ou cria uma lista final em que guarda a lista com os títulos ordenados e a lista dos registos sem título.
* Por último salva os resultados da consulta num ficheiro de texto (.txt).

**consultarData(lista, data,ficheiro)** - Filtra registos com base na data fornecida e ordena por título. O seu funcionamento é o seguinte:
* Procura todos os registos que possuem a data fornecida pelo utilizador.
* Divide os registos em dois grupos: com e sem título.
* Posteriormente, utiliza a lista dos registos com título e ordena-a utilizando a função sorted. De seguida, cria uma lista final em que guarda a lista dos registos com título ordenada e a lista dos registos sem título.
* Por último, guarda os resultados da consulta num ficheiro de texto (.txt).

**consultaAfiliacao_Data(lista, afiliacao, ficheiro)** e **consultaAfiliacao_Tit(lista, afiliacao, ficheiro)** - Filtra registos por afiliação e ordena por data ou por ordem alfabética de títulos, respetivamente. O funcionamento destas funções é da seguinte forma:
* Verifica se a afiliação fornecida pelo utilizador está presente na lista de registos.
* Divide os registos em dois grupos: com e sem data, e com título e sem título respetivamente.
* Posteriormente, utiliza a lista dos registos com data (na função consultaAfiliacao_Data) e a lista dos registos com título (na função consultaAfiliacao_Tit) e ordena-as utilizando a função sorted. De seguida, cria uma lista final em que guarda a lista dos registos com data ordenada e a lista dos registos sem data, ou cria uma lista final em que guarda a lista com os títulos ordenados e a lista dos registos sem título.
* Por último, guarda os resultados da consulta num ficheiro de texto (.txt).

**consultarPalavra_Chave_Data(lista, palavra_chave, ficheiro)** e **consultarPalavra_Chave_Tit(lista, palavra_chave, ficheiro)** - Filtra registros por palavra-chave e ordena por data ou por ordem alfabética de títulos, respetivamente. O funcionamento destas funções é da seguinte forma:
* Verifica se a palavra-chave fornecida pelo utilizador está presente na lista de registos.
* Divide os registos em dois grupos: com e sem data, e com título e sem título respetivamente.
* Posteriormente utiliza a lista dos registos com data (na função consultarPalavra_Chave_Data) e a lista dos registos com título (na função consultarPalavra_Chave_Tit) e ordena-as utilizando a função sorted. De seguida, cria uma lista final em que guarda a lista dos registos com data ordenada e a lista dos registos sem data, ou cria uma lista final em que guarda a lista com os títulos ordenados e a lista dos registos sem título.
* Por último, guarda os resultados da consulta num ficheiro de texto (.txt).

O ficheiro “Projeto_App.py” permite ao utilizador introduzir o requisito para efetuar a consulta, via input (). Caso a condição devolvida pela função seja True, imprime uma mensagem a dizer que os registos foram guardados com sucesso e menciona o nome do ficheiro onde foi guardado. Caso contrário, informa o utilizador de que não foi possível encontrar esse requisito na lista de registos. No ficheiro “Projeto_App_Interface.py” cria-se uma layout em que permite ao utilizador fornecer o requisito para efetuar a consulta. Caso a condição devolvida pela função seja True, imprime uma mensagem a dizer que os registos foram guardados com sucesso e menciona o nome do ficheiro onde foi guardado. Caso contrário, informa o utilizador de que não foi possível encontrar esse requisito na lista de registos. 


### **3. Funções de Listagem de Autores e Acesso aos Artigos**
Todas estas funções de listagem guardam o resultado da consulta efetuada num ficheiro, cujo nome é imposto pela aplicação.
	
**listar_freq(lista, ficheiro)** e **listar_freq_Inter(lista)** - Gera uma lista dos autores ordenados pela frequência das suas publicações. Estas funcionam da seguinte forma: 
* Cria um dicionário para contar quantas vezes cada autor aparece na lista de registos.
* Ordena os autores pela frequência de publicações, através da função sorted, e aplica-se reverse = True, para obtermos o resultado por ordem decrescente (aparecem primeiramente os autores com mais artigos). 
* Por último, guarda o resultado num ficheiro de texto (.txt), que poderá ser consultado pelo utilizador posteriormente.

O ficheiro “Projeto_App.py” executa a função explicada acima e, posteriormente, pergunta ao utilizador se quer aceder a um registo específico de algum autor. Se a resposta for “sim”, é questionado ao utilizador o nome do autor que quer consultar, através da função acederRes(lista, nome). É questionado também o título do registo a que quer aceder, mostrando ao utilizador o URL associado a este artigo, através da função acederURL(lista, titulo). Isto permite aceder ao artigo. No ficheiro “Projeto_App_Interface.py” pergunta-se ao utilizador se quer listar os autores por ordem alfabética ou por frequência, através de listar(). Se o utilizador clicar no botão “Ordenada pela Frequência”, executam-se estas funções. Posteriormente, a função Aceder_artigos() permite ao utilizador inserir o nome de um autor e, em seguida, selecionar um artigo para visualizar o URL. Para aceder ao registo é usada também a função acederRes(lista, nome); para aceder ao URL usa-se a função acederURL_Inter(lista, titulo). 

**listarAutor_Alf(lista,ficheiro)** e **listarAutor_Alf_Inter(lista)** - Lista os autores por ordem alfabética. Estas funcionam da seguinte forma:
* Cria uma lista de nomes únicos de autores a partir dos registos.
* Remove caracteres acentuados para obtermos uma melhor ordenação, através da função remover_acentos(texto).
* Ordena os nomes por ordem alfabética e guarda o resultado num ficheiro de texto (.txt).

O ficheiro “Projeto_App.py” funciona aqui de modo semelhante às funções listar_freq(lista, ficheiro) e listar_freq_Inter(lista). No ficheiro “Projeto_App_Interface.py” se o utilizador clicar no botão “Ordenada Alfabeticamente”, executam-se estas funções. Após isso, se o utilizador pretender, poderá executar as funções acederRes(lista, nome) e acederURL_Inter(lista, titulo) - de modo semelhante ao explicado acima.


### **4. Atualização dos Dados de uma Publicação**
**atual_reg(lista, titulo, doi , data, resumo,palavra_chaves, autores)** – Atualiza um registo da lista carregada com base no título fornecido. Caso o registo a atualizar não tenha título, o utilizador deve fornecer o doi. O seu funcionamento é o seguinte:
* Percorre a lista para encontrar o registo cujo título corresponde ao fornecido pelo utilizador. Caso não seja preenchido o campo do título faz o mesmo em relação ao doi.
* De seguida, atualiza o registo apenas substituindo os campos que foram preenchidos pelo utilizador, verificando se esses campos estão vazios ou não.

No ficheiro “Projeto_App.py” permite ao utilizador introduzir os campos do registo que pretende atualizar, via input (). Também verifica se os campos título e doi estão vazios. Caso ambos estejam vazios, imprime uma mensagem ao utilizador alertando que tem de preencher o campo do título! Só caso não tenha título, preenche o campo do doi. No ficheiro “Projeto_App_Interface.py” cria-se um layout que permite ao utilizador introduzir os campos do registo que pretende atualizar. Executa o mesmo procedimento que o mencionado acima.


### **5. Análise de Publicações**
**analise_palavra_chave_freq(lista, ficheiro)** e **analise_palavra_chave_alf(lista, ficheiro)** – Analisa a lista de registos pela frequência de palavras-chave ou pela ordem alfabética, respetivamente. O funcionamento destas funções é da seguinte forma:
* Analisa os registos pela palavra-chave e cria uma lista envolvendo todas as palavras-chave da lista de registos. Posteriormente, faz uma distribuição pela frequência ou ordena as palavras-chave por ordem alfabética, respetivamente.
**aceder_pubs_pal(lista, pal, ficheiro)** – Permite ao utilizador aceder aos registos com uma determinada palavra-chave.

No ficheiro “Projeto_App.py”, caso o utilizador queira aceder aos registos com uma determinada palavra-chave, pede ao utilizador para introduzir a palavra-chave, via input (). O mesmo acontece no ficheiro “Projeto_App_interface.py” e, caso o utilizador queira aceder ao ficheiro com os registos com a palavra-chave fornecida pelo utilizador, pode visualizá-lo na interface.


### **6. Estatística de Publicações**
**distribTop20_Autor(lista)**, **distribPub_Ano(lista)**, **distribPub_Mes(lista,ano)**, **distribPub_Autor(lista,autor)**, **distribPalavras_Freq(lista)**, **distribPalavras_Freq_Ano(lista, ano)** – Faz as distribuições perante os requisitos fornecidos ou por um determinado critério. O funcionamento destas funções é da seguinte forma:
* Inicialização de um dicionário para se realizar a distribuição.
* Iteração sobre a lista de publicações para fazer a distribuição com base na frequência de determinado parâmetro.
* Posteriormente ordena a distribuição pela frequência, de modo a ficar do mais comum para o menos.
* De seguida, chama uma função para desenhar o gráfico daquela distribuição. Caso o dicionário da distribuição não esteja vazio, faz o gráfico e devolve uma condição True, senão não o faz e devolve uma condição False.

No ficheiro “Projeto_App.py” caso seja necessário o utilizador fornecer algum requisito, é pedido o mesmo por via input (). O mesmo acontece no ficheiro “Projeto_App_Interface.py” através da criação de um layout. Em ambos, se a condição devolvida for False, informa o utilizador de que não existe nenhum registo com o parâmetro que o utilizador introduziu.

