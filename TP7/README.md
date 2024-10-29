# Relatório do TP7

## Data: 23.10.2024
## Autor: Leonor Pereira Mendes

## Resumo:

O TP7 consiste na realização de uma aplicação relacionada com meteorologia.
Nesta aplicação é mostrado ao utilizador o menu com as opções que o utilizador pode selecionar.
Se a opção não for sair, a aplicação executa a operação pretendida, apresenta o resultado e a seguir apresenta de novo o menu.
Se a opção for sair, a aplicação termina colocando uma mensagem no monitor.


Durante o ciclo em que a condição é verdadeira pus a imprimir o menu no inicio e após da escolha do utilizador, enquanto a escolha deste for diferente de 0. Se o utilizador não escolher uma das opções disponíveis, a sua resposta entra na estrutura else. Utilizei o if e o elif para o computador executar as funções relacionadas com a opção escolhida pelo utilizador.


Criei uma lista vazia TabMeteo para que a aplicação funcionar.

### Raciocínio:

Executei as 12 funcionalidades.

Sendo assim as opções de escolha permitidas ao utilizador foram:
    (1) Inserir Dia na Lista 
    (2) Listar Lista
    (3) Calcular temperaturas médias
    (4) Guardar o ficheiro
    (5) Carregar ficheiro
    (6) Consultar a Temperatura Mínima verificada 
    (7) Amplitude Térmica
    (8) Dia com Precipitação Máxima e o dia em que verificou a precipitação Máxima
    (9) Dias com Precipitação Superior a p
    (10) Dias com Precipitação Inferior a p
    (11) Gráfico Temperatura Máxima e Mínima
    (12) Gráfico pluviosidade 
    (0) Sair

Caso o utilizador selecione a opção 1, pus a criar a lista TabMeteo com todos os dados solicitados ao utilizador.

Caso o utilizador selecione a opção 2 esta lista a lista TabMeteo.

Caso o utilizador selecione a opção 3 esta calcula a temperatura média de cada dia, ou seja, soma a temperatura máxima com a mínima, e divide por dois. Esta função devolve a data e a temperatura média.

Caso o utilizador selecione a opção 4 esta guarda a lista TabMeteo num ficheiro cujo o nome é "TabelaMeteo.txt". Cada linha do ficheiro corresponde a uma data. Em cada linha, os elementos da data são separados por "-" e os restantes elementos são separados por "&".

Caso o utilizador selecione a opção 5 esta carrega as informações contidas no ficheiro e é apresentada ao utilizador na forma de uma lista.

Caso o utilizador selecione a opção 6 esta devolve ao utilizador a temperatura mínima verificada no conjunto de todos os dias.

Caso o utilizador selecione a opção 7 esta calcula a amplitude térmica e devolve ao utilizador a amplitude térmica juntamente com a data onde esta se verificou.

Caso o utilizador selecione a opção 8 esta retorna ao utilizador qual foi o dia com maior precipitação juntamente com o valor indicado acima.

Caso o utilizador selecione a opção 9 esta mostra ao utilizador os dias em que a precipitação foi superior ao valor p introduzido pelo utilizador.

Caso o utilizador selecione a opção 10 esta retorna o maior número de dias consecutivos em que a precipitação desses dias foi inferior ao valor p introduzido pelo utilizador.

Caso o utilizador selecione a opção 11 esta desenha os gráficos da temperatura mínima e máxima.

Caso o utilizador selecione a opção 12 esta devolve um gráfico de barras que mostra a precipitação de cada dia.