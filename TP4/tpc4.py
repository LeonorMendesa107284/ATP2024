
def menu():
    print("-----------------Menu-----------------")
    print("opção 1 - Criar Lista") 
    print("opção 2 - Ler Lista")
    print("opção 3 - Soma")     
    print("opção 4 - Média")
    print("opção 5 - Maior")
    print("opção 6 - Menor")
    print("opção 7 - estaOrdenada por ordem crescente")
    print("opção 8 - estaOrdenada por ordem decrescente")
    print("opção 9 - Procura um elemento")
    print("opção 0 - Sair")


import random


def criarlista(n):
    i=0
    res=[]
    while i<n:
        num= random.randint(1,100)
        res.append(num)
        i=i+1
    return res


def lerlista(num):
    res=[]
    for i in range(num):
        n=int(input("Introduza um número que deseja na lista:"))
        res.append(n)
    return res 


def soma(res):
    total=0
    for c in res:
        total =total+c
    return total


def media(res):
    if len(res)==0:
        total1=0
    else:
        total1=soma(res)/len(res)
    return total1 


def maior_elemento(res):
    maior=0
    for c in res:
        if c>maior:
            maior=c
    return maior


def menor_elemento(res):
    menor=res[0]
    for c in res[1:]:
        if c<menor:
            menor=c
    return menor


def ordem_crescente(res):
    cond2=True
    for c in range(len(res)-1):
        if res[c]> res[c+1]:
            cond2=False
    return cond2



def ordem_decrescente(res):
    cond1=True
    for c in range(len(res)-1):
        if res[c]< res[c+1]:
            cond1=False
    return cond1
   

def procura(res):
    if elem in res:
        total2=res.index(elem)
        return total2
    else:
        total2=-1
        return total2
    


cond=True
res=[]
while cond:
    menu()
    opcao=int(input("Introduza a opção pretendida:"))
    while opcao!=0 and opcao!=1 and opcao!=2 and opcao!=3 and opcao!=4 and opcao!=5 and opcao!=6 and opcao!=7 and opcao!=8 and opcao!=9: 
        print("Resposta inválida!")
        opcao=int(input("Introduza a opção pretendida:"))
        
    if opcao==1:
        n=int(input("Introduza o número de números que quer ter na lista:"))
        res=criarlista(n)
        print(res)
    elif opcao==2:
        num= int(input("Introduza o número de números que quer ter na lista:"))
        res=lerlista(num)
        print(res)
    elif opcao==3:
        total=soma(res)
        print(f"A soma de todos os números da lista é: {total}!")
    elif opcao==4:
        total1=media(res)
        print(f"A média dos números da lista é: {total1}!")
    elif opcao==5:
        maior=maior_elemento(res)
        print(f"O maior número de todos os elementos da lista é: {maior}!")
    elif opcao==6:
        menor=menor_elemento(res)
        print(f"O menor número de todos os elementos da lista é: {menor}!")
    elif opcao==7:
        if ordem_crescente(res)== True:
            print("Sim, a lista está ordenada de forma crescente!")
        else:
            print("Não, a lista não está ordenada de forma crescente!")
    elif opcao==8:
        if ordem_decrescente(res)==True:
            print("Sim, a lista está ordenada de forma decrescente!")
        else:
            print("Não, a lista não está ordenada de forma decrescente")
    elif opcao==9:
        elem=int(input("Introduza o elemento que deseja procurar na lista:"))
        total2=procura(res)
        if total2!= -1:
            print(f"O elemento que procura da lista está na posição: {total2}!")
        else:
            print (total2)
            print("O elemento que procura não está na lista!")
    elif opcao==0:
        print("A aplicação vai encerrar. A ultima lista utilizada foi:")
        print(res)
        cond=False 


