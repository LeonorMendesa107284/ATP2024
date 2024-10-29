
def existeDia ( TabMeteo, dia):
    cond=False
    for d in TabMeteo:
        if d[0]==dia[0]:
            cond=True
    return cond


def inserirDia( TabMeteo, dia ):
    if not existeDia (TabMeteo, dia ):
        TabMeteo.append(dia)
    else:
        print("Esse dia já existe nesta lista!")
    return TabMeteo

def listarLista( TabMeteo ):
    print("-------------------------------------Lista de Dias---------------------------------------")
    for d in TabMeteo:
        print(f"Data:{d[0]} | Temperatura Mínima:{d[1]} | Temperatura Máxima:{d[2]} | Precipitação :{d[3]}")
    print("-------------------------------------------------------------------------------------------")
    return 


def medias(TabMeteo):
    res = []
    for data, min, max, prec in TabMeteo:
        tempmédia=(min+max)/2
        res.append((data, tempmédia))
    return res


def guardaTabMeteo(t, fnome):
    file=open(fnome, "w")
    for dia_n in t:
        data, min, max,prec=dia_n
        ano, mes,dia=data
        registo=f"{ano} - {mes} - {dia} & {min} & {max} & {prec}\n"
        file.write(registo)
    file.close()
    return



def carregaTabMeteo(fnome):
    res = []
    file=open(fnome, "r")
    for linha in file:
        linha=linha.strip()
        campos=linha.split("&")
        data, min, max,prec=campos
        ano, mes, dia=data.split("-")
        dia=((int(ano),int(mes),int(dia)), float(min), float(max), float(prec))
        res.append(dia)
    file.close()
    return res



def minMin(TabMeteo):
    minima=TabMeteo[0][1]
    for d in TabMeteo[1:]:
        if d[1]<minima:
            minima=d[1]
    return minima



def amplTerm(TabMeteo):
    res = []
    amplitude=0
    for d in TabMeteo:
        amplitude=d[2]-d[1]
        meteo=(d[0], amplitude)
        res.append(meteo)
    return res



def maxChuva(TabMeteo):
    max_prec=TabMeteo[0][3]
    for d in TabMeteo[1:]:
        if d[3]>max_prec:
            max_prec=d[3]
    return (d[0], max_prec)
   



def diasChuvosos(TabMeteo, p):
    res=[]
    for d in TabMeteo:
        if d[3]>p:
            meteo=(d[0], d[3])
            res.append(meteo)
    return res



def maxPeriodoCalor(TabMeteo, p):
    num_consec=0
    consec_global=0
    for data, min, max, prec in TabMeteo:
        if prec<p:
            num_consec = num_consec +1
        else:
            if num_consec> consec_global:
                consec_global= num_consec
            num_consec=0
    if num_consec> consec_global:
        consec_global= num_consec
    return consec_global


import matplotlib.pyplot as plt
def grafTabMeteo(t):
    datas=[f"{data[0]}-{data[1]}-{data[2]}"  for data, *_ in t  ]
    temp_min=[min for _, min, *_ in t]
    tem_max=[max for _,_, max,_ in t]
    plt.plot(datas, temp_min, label="Temp Mínima")
    plt.plot(datas, tem_max, label="Temp Máxima")
    
    plt.xlabel("Data")
    plt.ylabel("Temperatura ºC")
    plt.title("Temperatura Mínima e Máxima")
    plt.legend()
    plt.show()
    return

def grafTabMeteoPrec(t):
    datas=[f"{data[0]}-{data[1]}-{data[2]}" for data,*_ in t]
    precs=[prec for _,_,_,prec in t]

    plt.bar(datas,precs)
    plt.xlabel('Data')
    plt.ylabel('Precipitação')
    plt.title('Pluviosidade')
    plt.show()
    return 

def menu():
    print(""" 
    --------------------------Menu--------------------------
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
    """)


TabMeteo = []
cond = True
while cond:
    menu()
    opcao = int(input("Introduza a opção pretendida:"))
    if opcao == 1:
        ano = int(input("Introduza o ano:"))
        mes = int(input("Introduza o mes:"))
        dia = int(input("Introduza o dia:"))
        data = (ano,mes,dia)
        temp_min = float(input(f"Introduza a temperatura mínima que foi registada no dia ({data}):"))
        temp_max = float(input(f"Introduza a temperatura máxima que foi registada no dia ({data}):"))
        prec = float(input(f"Intoduza a precipitação registada no dia ({data}):"))
        dia = (data,temp_min,temp_max,prec)
        TabMeteo1=inserirDia( TabMeteo, dia )
        print(TabMeteo1)
    elif opcao == 2:
        listarLista( TabMeteo )
    elif opcao == 3:
        if len(TabMeteo) == 0:
            print("A lista está vazia! Para realizar esta operação crie primeiro uma lista através da opção 'Inserir Dia na Lista' .")
        else:
            print(medias(TabMeteo))
    elif opcao == 4:
        if len(TabMeteo) == 0:
            print("A lista está vazia! Para realizar esta operação crie primeiro uma lista através da opção 'Inserir Dia na Lista' .")
        else:
            guardaTabMeteo(TabMeteo, "TabelaMeteo.txt")    
            print("A lista que criou foi guardada no ficheiro com o nome: TabelaMeteo.txt.")  
    elif opcao == 5:
        if len(TabMeteo) == 0:
            print("A lista está vazia! Para realizar esta operação crie primeiro uma lista através da opção 'Inserir Dia na Lista'.")
        else:
            print(carregaTabMeteo("TabelaMeteo.txt"))
    elif opcao == 6:
        if len(TabMeteo) == 0:
            print("A lista está vazia! Para realizar esta operação crie primeiro uma lista através da opção 'Inserir Dia na Lista' .")
        else:
            print(minMin(TabMeteo))
    elif opcao == 7:
        if len(TabMeteo) == 0:
            print("A lista está vazia! Para realizar esta operação crie primeiro uma lista através da opção 'Inserir Dia na Lista' .")
        else:
            print(amplTerm(TabMeteo))
    elif opcao == 8:
        if len(TabMeteo) == 0:
            print("A lista está vazia! Para realizar esta operação crie primeiro uma lista através da opção 'Inserir Dia na Lista' .")
        else:
            print(maxChuva(TabMeteo))
    elif opcao == 9:
        if len(TabMeteo) == 0:
            print("A lista está vazia! Para realizar esta operação crie primeiro uma lista através da opção 'Inserir Dia na Lista' .")
        else:
            p = float(input("Introduza um valor de precipitação:"))
            print(f"Dias em que a precipitação foi superior a {p}:")
            print(diasChuvosos(TabMeteo, p))
    elif opcao == 10:
        if len(TabMeteo) == 0:
            print("A lista está vazia! Para realizar esta operação crie primeiro uma lista através da opção 'Inserir Dia na Lista' .")
        else:
            p = float(input("Introduza um valor de precipitação:"))
            print(f"Dias consecutivos em que a precipitação foi inferior a {p}:")
            print(maxPeriodoCalor(TabMeteo, p))
    elif opcao == 11:
        if len(TabMeteo) == 0:
            print("A lista está vazia! Para realizar esta operação crie primeiro uma lista através da opção 'Inserir Dia na Lista' .")
        else:
            grafTabMeteo(TabMeteo)
    elif opcao==12:
        if len(TabMeteo) == 0:
            print("\nNão há dados na tabela. Crie uma tabela usando a opção 1.")
        else:
            grafTabMeteoPrec(TabMeteo)
    else:
        if opcao!=0:
            print("Resposta inválida")
        elif opcao==0:
            cond=False  
if opcao=="0":
    print("A aplicasão vai encerrar!")