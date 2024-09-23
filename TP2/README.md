
# Relatório do TP2

## Data: 18.09.2024
## Autor: Leonor Pereira Mendes

## Resumo:

O TP2 consiste na realização de um jogo chamado "Adivinha o número"
Este jogo tem duas modalidades:
* Modalidade número 1- O computador pensa num número (entre 0 e 100) e o utilizador tenta adivinhar;
* Modalidade número 2- O utilizador pensa num número (entre 0 e 100) e o computador tenta adivinhar.
Depois de ser feita a escolha da modalidade, quem pensou no número terá de dizer se a resposta está certa utilizando a palavra Acertou, ou se o número é Maior ou Menor.


O que me causou mais dificuldade neste trabalho de casa foi descobrir qual era a função que tinha de usar para que o computador escolhesse um número aleatório. Também achei complexo a realização da modalidade 2.



### Raciocínio:

O meu raciocínio foi em primeiro lugar perguntar a modalidade que o utilizador desejava jogar. 

Caso o utilizador não escolha nenhuma das hipóteses propostas, a resposta do utilizador entra na estrutura while até que o utilizador responda com um 1 ou com um 2, para escolher uma das duas modalidades.

Se o utilizador escolher a 1: pus o computador a escolher um número aleatório utilizando a função random. Utilizei a variável tentativas para contar o número de tentativas. Posteriormente usei a condição if caso o utilizador acerte à primeira e pus a dizer acertou e utilizou apenas uma tentativa. Caso contrário, a resposta do utilizador entra na estrutura while até o utilizador acertar no número. 


Se o utilizador escolher a 2: utilizei a variável maior e menor. Utilizei também a variável num para o palpite inicial do computador e num1 para os restantes palpites. 
Inicialmente igualei o menor ao menor número do intervalo(0) e o maior ao maior número do intervalo(100). Posteriormente, fiz a média entre o menor e o maior para que o computador apresentasse o valor do meio do intervalo. 
Caso o computador acerte à primeira o número do utilizador, a resposta entra na condição if é dito acertou e que o computador utilizou apenas uma tentativa. Caso contrário, entra na estrutura while e apenas sai dela quando o computador acertar a resposta do utilizador. 
Se o palpite do computador for maior que o numero pensado pelo utilizador, ele entra na condição if. Posteriormente, igualei o palpite ao menor e somei mais uma unidade para restringir cada vez mais o intervalo e para excluir do intervalo o número dito anteriormente. 
Se o palpite do computador for menor que o numero pensado pelo utilizador, ele entra na condição elif. Posteriormente, igualei o palpite ao maior e subtraí uma unidade para restringir cada vez mais o intervalo e para excluir do intervalo o número dito anteriormente.
Caso o utilizador não responda coma palavra "Acertou", com "Maior" ou com "Menor", a resposta do utilizador entra na condição else. Aqui é dito ao utilizador que a reposta é invalida e é pedido para dizer novamente se o palpite do computador está certo, ou se é maior ou menor.


No final, tanto na modalidade 1 como na 2 é apresentado o número de tentativas utilizado até acertar no número.