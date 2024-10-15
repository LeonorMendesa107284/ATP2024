
def listar( cinema ):
    print("-----------Lista de Filmes-------------")
    for s in cinema:
        print(f"Filme:{s[2]}")
    print("----------------------------------------")
    return 

#  Sala = [nlugares, Vendidos, filme]
def disponivel( cinema, filme_s, lugar ):
    cond=True
    for s in cinema:
        nlugares, Vendidos, filme= s
        if filme_s==filme and lugar<=nlugares:
            if lugar in Vendidos:
                cond=False
    return cond

def vendeBilhete( cinema, filme_s, lugar ):
    if disponivel( cinema, filme_s, lugar ):
        for s in cinema:
            _, Vendidos, filme= s
            if filme_s==filme:
                Vendidos.append(lugar)
                Vendidos.sort()
    else:
        print("Esse lugar já está ocupado. Escolha outro lugar!")
    return cinema

def listardisponibilidades( cinema ):
    for s in cinema:
        nlugares, Vendidos, filme= s
        if nlugares-len(Vendidos)!=0:
            print(f"Nome do parque: {filme} | Nº de lugares disponível: {nlugares-len(Vendidos)}.")
    return 



def existesala (cinema,sala_nova):
    cond=False
    for s in cinema:
        if s[2]==sala_nova[2]:
            cond=True
    return cond

def inserirSala( cinema, sala_nova ):
    if not existesala (cinema,sala_nova):
        cinema.append(sala_nova)
    else:
        print("Já existe uma sala com esse filme em exibição!")
        print("Se quiser por o mesmo filme em exibição, no nome do filme coloque para além do nome, um caracter/número para distinguir o filme das diferentes salas.")
        filmenovo=input("Introduza o nome do filme (Se se enganou em alguma operação digite '0' para voltar ao menu principal):")
        if filmenovo=="0":
            sala_nova=[nlugares,Vendidos,filme_s]
        else:     
            sala_nova=[nlugares,Vendidos,filmenovo]
            if not existesala (cinema,sala_nova):
                cinema.append(sala_nova)
    return cinema


def listarS(cinema, filme_s):
    for s in cinema:
        nlugares, Vendidos, filme= s
        if filme_s==filme:
            print(f"Nome:{filme_s} | Nº de lugares:{nlugares} | Nº de lugares ocupados:{len(Vendidos)}") 
    return

def removeSala(cinema, filme_s):
    for s in cinema:
        if filme_s==s[2] :
            cinema.remove(s)
            print(f"A sala do filme {s[2]} foi removida.")
    return cinema

def menu():
    print(""" 
    --------------------------Menu--------------------------
    (1) Listar Cinema
    (2) Consultar Sala (Ver se um lugar está disponível)
    (3) Consultar Sala (Registar a venda de um lugar da sala)
    (4) Listar (Filme e nº de lugares disponíveis para cada sala)
    (5) Inserir Sala
    (6) Consultar Sala (listar uma sala)
    (7) Remover Sala
    (0) Sair
    """)

opcao="1"
cinema=[]
cond=True
while opcao != '0' and cond:
    menu()
    opcao = input("Introduza uma opção: ")
    if opcao=="1":
        listar(cinema)
    elif opcao=="2":
        filme_s=input("Introduza o nome do filme:")
        cond1=True
        i=0
        while cond1==True and i<len(cinema):
            i=i+1
            for c in cinema :
                if filme_s==c[2]:
                    lugar=int(input("Introduza o lugar da sala:"))
                    print(disponivel(cinema, filme_s, lugar))
                    cond1=False
        if cond1==True:
            print("Esse filme não existe neste cinema.")
    elif opcao=="3":
        filme_s=input("Introduza o nome do filme:")
        cond1=True
        i=0
        while cond1==True and i<len(cinema):
            i=i+1
            for c in cinema :
                if filme_s==c[2]:
                    lugar=int(input("Introduza o lugar da sala onde a pessoa se vai sentar:"))
                    print(vendeBilhete(cinema, filme_s, lugar)) 
                    cond1=False
        if cond1==True:
            print("Esse filme não existe neste cinema.")
    elif opcao=="4":
        listardisponibilidades( cinema )
    elif opcao=="5":
        salan=input("Introduza o nome da sala:")
        nlugares=int(input(f"Introduza o número de lugares da {salan}:"))
        nVendidos=int(input(f"Introduza o número de lugares vendidos da {salan}:"))
        while nVendidos>nlugares:
            print(f"O número de lugares vendidos não pode ser superior ao número de lugares da sala ({nlugares})!")
            nlugares=int(input(f"Introduza o número de lugares da {salan}:"))
            nVendidos=int(input(f"Introduza o número de lugares vendidos da {salan}:"))
        i=1
        Vendidos=[]
        while nVendidos>=i and nVendidos<=nlugares:
            lugar=int(input(f"Introduza o {i}º lugar ocupado:"))
            Vendidos.append(lugar)
            i=i+1
        Vendidos.sort()
        filme_s=input("Introduza o nome do filme:")
        sala_nova=[nlugares,Vendidos,filme_s]
        cinema=inserirSala(cinema,sala_nova)
        print(cinema)
    elif opcao=="6":
        cond1=True
        i=0
        filme_s=input("Introduza o nome do filme:")
        while cond1==True and i<len(cinema):
            for c in cinema:
                if filme_s==c[2]:
                    listarS(cinema, filme_s)
                    cond1=False
            i=i+1
        if cond1==True:
            print("Esse filme não existe neste cinema.")
    elif opcao=="7":
        filme_s=(input("Introduza o nome do filme:"))
        cond1=True
        i=0
        while cond1==True and i<len(cinema):
            for c in cinema:
                if filme_s==c[2]:
                    print(removeSala(cinema,filme_s))
                    cond1=False
            i=i+1
        if cond1==True:
            print("Esse filme não existe neste cinema.")
        
    else:
        if opcao!="0":
            print("Resposta inválida")
        elif opcao==0:
            cond=False  
if opcao=="0":
    print("A aplicasão vai encerrar!")