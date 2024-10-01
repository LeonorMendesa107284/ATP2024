
# Relatório do TP2

## Data: 25.09.2024
## Autor: Leonor Pereira Mendes

## Resumo:

O TP3 consiste na realização de um jogo chamado "21 fósforos".
Este jogo tem duas modalidades:
* Modalidade número 1- O jogador joga em primeiro lugar e o computador começa a jogar em segundo lugar;
* Modalidade número 2- o computador começa em primeiro e o jogador joga em segundo lugar.
Depois de ser feita a escolha da modalidade o jogo é iniciado.


Achei este trabalho de casa desafiante. Entre as duas modalidades a que me causou mais dificuldade foi a modalidade 2.



### Raciocínio:

O meu raciocínio foi em primeiro lugar perguntar a modalidade que o utilizador desejava jogar. 

Caso o utilizador não escolha nenhuma das hipóteses propostas, a resposta do utilizador entra na estrutura while até que o utilizador responda com um 1 ou com um 2, para escolher uma das duas modalidades.

Se o utilizador escolher a 1: o utilizador é o primeiro a jogar e portanto tem de escolher um número de 1, 2, 3 ou 4. Caso o utilizador não escolha um números dos referidos anteriormente, a resposta do utilizador entra na estrutura while até que o utilizador responda com um dos números dito a cima. Posteriormente à variável inicio é retirada o número de fósforos que o utilizador pediu. 
Para que o computador ganhe sempre fiz com que o utilizador calhasse sempre no número de fósforos 16, 11, 6 e 1. Sendo um 6 um número muito falacioso neste jogo, se este número calha ao utilizador é declarada a derrota para o utilizador, uma vez que qualquer que seja o número de fósforos que o utilizador retire aos 6 fósforos em jogo, o computador vai tirar a diferença para que sobre 1 fósforo para o utilizador.
Sendo assim a diferença entre 6 e 1 é 5 então pus a jogada do computador a ser sempre a diferença entre 5 e a jogada do utilizador, fazendo assim com que o utilizador caia sempre nas posições 16, 11, 6 e 1.
Caso o utilizador, durante o jogo, não escolha um números dos referidos anteriormente, a resposta do utilizador entra na estrutura while até que o utilizador responda com 1, 2, 3 ou 4.
À variável inicio é sempre retirada a jogada do utilizador e a jogada do computador até o número de fósforos ser igual a 5.


Se o utilizador escolher a 2: o computador é o primeiro a jogar e portanto tem de escolher um número de 1, 2, 3 ou 4. Utilizei a função aleatória para o computador escolher um número dos referidos anteriormente. Posteriormente à variável inicio é retirada o número de fósforos que o computador pediu. A seguir o utilizador tem de tirar 1, 2, 3 ou 4 dos fósforos que sobram.
À variável inicio é sempre retirada a jogada do utilizador e a jogada do computador.
Caso o utilizador não se engane nos cálculos, ou seja, por o computador nas posições 16, 11, 6 e 1, o computador perde.
Se o utilizador se engana nos cálculos, ou seja, não põe o computador nas posições 16, 11, 6 e 1, pus o computador a por o utilizador nas posições indicadas acima. Para isso utilizei a estrutura while e retirei sempre um fósforo á variável inicio até que o inicio fosse igual a 16, 11, 6 ou 1.
A partir daí a jogada do computador vai ser sempre a diferença entre 5 e a jogada do utilizador, fazendo assim com que o utilizador caia sempre nas posições 16, 11, 6 ou 1. Sendo assim, jogo está garantido para o computador.
Caso o utilizador, durante o jogo, não escolha um números dos referidos anteriormente, a resposta do utilizador entra na estrutura while até que o utilizador responda com 1, 2, 3 ou 4.