# Relatório do TP8

## Data: 30.10.2024
## Autor: Leonor Pereira Mendes

## Resumo:

O TP8 consiste na realização de três trabalhos de casa.

O primeiro consiste na especificação de listas em compreensão.
O segundo consiste na definição de algumas funções.
O terceiro consiste na definição de funções para gerir uma rede social.


### Raciocínio:

No exercício 1:
* a) Ver se o numero já estava na lista e se não estiver colocar o número devolvendo uma lista formada pelos elementos que não são comuns às duas listas.
* b) Separar o texto inicial por espaços e ver quais palavras têm mais de 3 letras e retorna uma lista formada pelas palavras do texto compostas por mais de 3 letras.
* c) Devolve uma lista formada por pares do tipo (índice, valor) com os valores da lista dada.

No exercício 2:
* a) Consiste em especificar uma função que dada uma string e uma substring não vazia, calcula  o número de vezes em que a substring aparece na string, sem que haja sobreposição de substrings. Para isso percorro a string com o comprimento da substring até chegar ao final da string.
* b) Especificar uma função que recebe uma lista de números inteiros positivos e devolve o menor produto que for possível calcular multiplicando os 3 menores inteiros da lista. Para isso ordeno a lista por ordem e multiplico o 3 primeiro números.
* c) Especificar uma função que dado um número inteiro positivo, repetidamente adiciona os seus dígitos até obter apenas um dígito que é retornado como resultado. Para isso faço uma divisão inteira do número e somo com o resto da divisão inteira. Caso dê maior que 10 repito o processo até a soma ser menor que 10.
* d) Especifique uma função que recebe duas strings, 'string1' e 'string2', e devolve o índice da primeira ocorrência de 'string2' em 'string1', caso não ocorra nenhuma vez a função deverá retornar '-1'.Para isso separo o string por espaços e percorro a string com o comprimento da substring.

No exercício 3:
* a) Indica quantos posts estão registados na rede social. Para isso percorro a lista de posts e por cada post somo ao total o total + 1.
* b) Devolve a lista de posts de um determinado autor. Para isso percorro a lista de posts e vejo quais posts foram publicados por determinado autor com parando o nome do autor do post com o nome introduzido pelo utilizador
* c) Devolve a lista de autores ordenada alfabeticamente. Para isso crio uma lista de autores e no final ordeno a lista.
* d) Acrescenta um novo post à lista de posts, sendo que cada post é um dicionário.
* e) Remove o post da lista de post através do id introduzido pelo utilizador. Se id introduzido por igual ao id de um dos posts da lista de posts esse post é removido.
* f) Devolve uma lista com a distribuição de número de posts por autor.
* g) Devolve uma lista de posts comentados por determinado autor. Para isso percorro a lista de post e em cada post vejo se no dicionário comentários o nome do autor introduzido pelo utilizador está lá. Se estiver acrescento esse post à lista criada. 