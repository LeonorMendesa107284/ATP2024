# Relatório do TP5

## Data: 08.10.2024
## Autor: Leonor Pereira Mendes

## Resumo:

O TP5 consiste na realização de uma aplicação para gerir salas de cinema.
Nesta aplicação é mostrado ao utilizador o menu com as opções que o utilizador pode selecionar.
Se a opção não for sair, a aplicação executa a operação pretendida, apresenta o resultado e a seguir apresenta de novo o menu.
Se a opção for sair, a aplicação termina colocando uma mensagem no monitor.


Durante o ciclo em que a condição é verdadeira pus a imprimir o menu no inicio e após da escolha do utilizador, enquanto a escolha deste for diferente de 0. Se o utilizador não escolher uma das opções disponíveis, a sua resposta entra na estrutura else. Utilizei o if e o elif para o computador executar as funções relacionadas com a opção escolhida pelo utilizador.

Ao longo do programa é pedido ao utilizador para introduzir o nome do filme. Utilizei um ciclo while com um for dentro para que seja efetuada a comparação no máximo o número de vezes, que é equivalente ao comprimento da lista cinema caso o utilizador tenha introduzido mal o nome do filme. Caso isto aconteça é dito ao utilizador que esse filme não existe. Caso o utilizador coloque um filme que exista no cinema o ciclo só vai executar até encontrar o nome do filme na lista cinema.

Criei uma lista vazia cinema para que a aplicação continua a funcionar.

### Raciocínio:

Executei as 6 funcionalidades pedidas no enunciado e acrescentei a remover sala caso o utilizador queira remover alguma sala.
Acrescentei também a função listar apenas uma Sala.

Sendo assim as opções de escolha permitidas ao utilizador foram:
    (1) Listar Cinema
    (2) Consultar Sala (Ver se um lugar está disponível)
    (3) Consultar Sala (Registar a venda de um lugar da sala)
    (4) Listar (Filme e nº de lugares disponíveis para cada sala)
    (5) Inserir Sala
    (6) Consultar Sala (listar uma sala)
    (7) Remover Sala
    (0) Sair

Para todas as funções a não ser a inserir sala usei estruturas for para que percorre-se toda a lista de cinemas.

Em especial na função que corresponde à opção 5 do menu, inserirSala, dei a possibilidade do utilizador por o mesmo filme em exibição em varias salas, no entanto tem que por um número para distinguir as salas e para que posteriormente as outras funções funcionem corretamente.

No elif da opção 2, 3, 6 e 7 usei a estrutura while com uma condição (cond1=True) e com i menor que o comprimento da lista cinema, sendo que i toma o valor zero. Dentro desta estrutura usei um for para verificar se o utilizador colocou de forma correta o nome do filme. Caso tenha colocado um nome do filme que exista na lista cinema, a condição passa a falsa e sai da estrutura while. Se após percorrer a estrutura while a condição continuar verdadeira, ou seja percorreu o ciclo ao equivalente do comprimento da lista cinema e não entrou na estrutura if, então a condição continua verdadeira e é dito ao utilizador que o nome do filme que inseriu não existe no cinema.
