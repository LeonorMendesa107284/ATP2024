
# Relatório do TP6

## Data: 16.10.2024
## Autor: Leonor Pereira Mendes

## Resumo:

O TP6 consiste na realização de uma aplicação para gestão de alunos.
Nesta aplicação é mostrado ao utilizador o menu com as opções que o utilizador pode selecionar.
Se a opção não for sair, a aplicação executa a operação pretendida, apresenta o resultado e a seguir apresenta de novo o menu.
Se a opção for sair, a aplicação termina colocando uma mensagem no monitor.


Durante o ciclo em que a condição é verdadeira pus a imprimir o menu no inicio e após da escolha do utilizador, enquanto a escolha deste for diferente de 0. Se o utilizador não escolher uma das opções disponíveis, a sua resposta entra na estrutura else. Utilizei o if e o elif para o computador executar as funções relacionadas com a opção escolhida pelo utilizador.


Criei uma lista vazia turma para que a aplicação continua a funcionar.

### Raciocínio:

Executei as 6 funcionalidades pedidas no enunciado.

Sendo assim as opções de escolha permitidas ao utilizador foram:
    (1) Criar uma turma
    (2) Inserir um aluno na turma
    (3) Listar a turma
    (4) Consultar um aluno por id
    (8) Guardar a turma em ficheiro
    (9) Carregar uma turma dum ficheiro
    (0) Sair

Para todas as funções a não ser a criar sala e inserir sala usei estruturas for para que percorre-se toda a lista de cinemas.

Na função criarTurma pergunto ao utilizador quantos elementos tem a turma, sendo que designei a variável pelo nome todos. Utilizei um while com um contador(i) para sejam introduzidos em ciclo o nome o id e as notas do aluno até que complete uma turma com o número de alunos pedido pelo utilizador. Caso ponha um id igual ao já introduzido é dito ao utilizador que o aluno já está na turma.

Na função inserirAluno vejo através de outra função se o aluno existe. Caso não exista acrescento o aluno à lista de alunos (turma). Caso exista e o id e o nome desse aluno já esteja na turma digo ao utilizador que o aluno já se encontra na turma. Caso o id do aluno não coincida com o nome do aluno já inserido na turma digo ao utilizador que o id que introduziu já está associado a outro aluno.
No elif da opção 2 peço ao utilizador para introduzir o id, o nome e a lista de notas (TPC, Projeto, Teste) e crio o tuplo do aluno para posteriormente poder inserir na lista turma.

No elif da opção 4 usei a estrutura while com uma condição (cond1=True) e com i menor que o comprimento da lista turma, sendo que i toma o valor zero. Dentro desta estrutura usei um for para verificar se o utilizador colocou de forma correta o id do aluno. Caso tenha colocado um id que exista na lista turma, a condição passa a falsa e sai da estrutura while. Se após percorrer a estrutura while a condição continuar verdadeira, ou seja percorreu o ciclo ao equivalente do comprimento da lista turma e não entrou na estrutura if, então a condição continua verdadeira e é dito ao utilizador que o aluno não pertence à turma.

Na função guardarTurma abro o ficheiro com o open e utilizo o for para percorrer a lista turma e para a cada aluno escrever no ficheiro o nome, o id e as notas da seguinte forma: 
* nome  #  id  #  notaTPC | notaProj  | notaTeste

Na função recuperarTurma criei uma lista vazia para a variável turma utilizei o for para percorrer todas as linhas do ficheiro e a cada linha seperei cada frase com o split("#") e o split("|") e posteriormente criei o tuplo para o aluno, sendo este aluno adicionado posteriormente à lista Turma. No final fecho o ficheiro.