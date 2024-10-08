# Relatório do TP4

## Data: 02.10.2024
## Autor: Leonor Pereira Mendes

## Resumo:

O TP4 consiste na realização de uma aplicação.
Nesta aplicação é mostrado ao utilizador o menu com as opções que o utilizador pode selecionar.
Se a opção não for sair, a aplicação executa a operação pretendida, apresenta o resultado e a seguir apresenta de novo o menu.
Se a opção for sair, a aplicação termina colocando uma mensagem no monitor.


Durante o ciclo em que a condição é verdadeira pus a imprimir o menu no inicio e após da escolha do utilizador, enquanto a escolha deste for diferente de 0. Se o utilizador não escolher uma das opções disponíveis, a sua resposta entra na estrutura while e é feita a pergunta até que o utilizador escolha uma das opções do menu dadas. Utilizei o if e o elif para o computador executar as funções relacionadas com a opção escolhida pelo utilizador.

Criei uma lista vazia res caso a primeira opção do utilizador não seja a 1 nem a 2. A aplicação continua a funcionar mas vai sempre apresentar o valor 0.


### Raciocínio:

* Para a opção 1 utilizei a variável res para criar uma lista vazia e pergunto ao utilizador quantos números deseja que a sua lista tenha. A partir daí dentro da função criarlista, dentro da estrutura while com a função random gera números aleatórios de 1 a 100 até que o comprimento da lista seja o desejado pelo utilizador e acrescento esses números à variável res com a função append.

* Para a opção 2 utilizei a variável res para criar uma lista vazia e pergunto ao utilizador quantos números deseja que a sua lista tenha. A partir daí dentro da função lerlista, dentro da estrutura for transformo o "num" num intervalo de números, o que me permite acrescentar o número de números pedido pelo utilizador. É também perguntado ao utilizador os números que deseja por na lista e com função append é acrescentado os números à lista res.

* Para a opção 3 utilizei a função soma que recebe a lista criada ou guardada até ao momento. Utilizei a estrutura for para que a cada número da lista res, ela acrescente ao total (resultado da soma) o total mais o numero da lista.

* Para a opção 4 utilizei a função media que recebe a lista criada ou guardada até ao momento. Utilizei a estrutura if. Caso o comprimento da lista res seja "0" pus a média a dar 0. Senão entra no else e faz a função utilizada anteriormente (a soma) a dividir pelo comprimento da lista. 

* Para a opção 5 utilizei a função maior_elemento que recebe a lista criada ou guardada até ao momento. Inicialmente defini a variável maior igual a 0. Utilizei a estrutura for para que a cada número da lista res, ela compare o número com o número guardado no maior. Caso o número seja maior do que o número guardado na variável maior, o número que estava antes nesta variável vai ser substituído por esse novo número.

+ Para a opção 6 utilizei a função menor_elemento que recebe a lista criada ou guardada até ao momento. Inicialmente defini a variável menor igual ao primeiro número da lista. Utilizei a estrutura for para que a cada número da lista res a partir da posição 1, inclusive, ela compare o número com o número guardado no menor. Caso o número seja menor do que o número guardado na variável menor, o número que estava antes nesta variável vai ser substituído por esse novo número. Apena utilizei no for os números a partir da posição 1 da lista res para o computador não fazer duas vezes a mesma comparação.

* Para a opção 7 utilizei a função ordem_crescente que recebe a lista criada ou guardada até ao momento. Inicialmente defini a cond2 como True. Utilizei a estrutura for para que a cada número da lista do comprimento da lista res menos 1, ela compare o número da lista res naquela posição com o número seguinte da lista res. Caso se verifique que algum número da lista res seja maior do que o número seguinte da mesma lista, a condição torna-se falsa e podemos concluir que a função não é crescente. Utilizei o intervalo do comprimento da lista res menos 1 para que não ocorra nenhum erro e para o computador não fazer a mesma comparação duas vezes.

* Para a opção 8 utilizei a função ordem_decrescente que recebe a lista criada ou guardada até ao momento. Inicialmente defini a cond1 como True. Utilizei a estrutura for para que a cada número da lista do comprimento da lista res menos 1, ela compare o número da lista res naquela posição com o número seguinte da lista res. Caso se verifique que algum número da lista res seja menor do que o número seguinte da mesma lista, a condição torna-se falsa e podemos concluir que a função não é decrescente. Utilizei o intervalo do comprimento da lista res menos 1 para que não ocorra nenhum erro e para o computador não fazer a mesma comparação duas vezes.

* Para a opção 9 utilizei a função procura que recebe a lista criada ou guardada até ao momento. Perguntei ao utilizador que elemento deseja procurar na lista. Utilizei a estrutura if e caso o elemento esteja na lista res, através da função index obtenho a posição na lista desse elemento. Senão é devolvido ao utilizador a posição -1 o que significa que o elemento não está na lista res.

* Para opção 0 pus a condição a ser falsa para ela sair do ciclo e encerrar a aplicação!


