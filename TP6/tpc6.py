
def existeAluno (turma,id):
    cond=False
    for a in turma:
        if a[1]==id:
            cond=True
    return cond

def existeAlunoNome (turma,nome, id):
    cond=False
    for a in turma:
        if a[0]==nome and a[1]==id:
            cond=True
    return cond


def criaTurma(turma):
    todos=int(input("Quantos alunos tem a turma?"))
    i=1
    while i<=todos:
        id_novo=int(input(f"Introduza o id do {i}º aluno:"))
        if not existeAluno (turma,id_novo):
            nome_novo=input(f"Introduza o nome do {i}º aluno (ID:{id_novo}):")
            notaTPC=int(input("Introduza a nota do TPC:"))
            notaProj=int(input("Introduza a nota do Projeto:"))
            notaTeste=int(input("Introduza a nota do Teste:"))
            aluno=(nome_novo, id_novo, [notaTPC, notaProj, notaTeste]) 
            turma.append(aluno)
            i=i+1
        
    return turma


def inserirAluno( turma, aluno):
    if not existeAluno (turma,aluno[1]) :
        turma.append(aluno)
    elif existeAlunoNome(turma,aluno[0],aluno[1]):
        print("Esse aluno já está na turma!")
    elif existeAluno(turma,aluno[1]):
        print("O id que introduziu está associado ao nome de outro aluno!") 
   
    return turma

def listarTurma( turma ):
    print("-------------------------------------Lista de Turma---------------------------------------")
    for a in turma:
        print(f"Nome:{a[0]} | ID:{a[1]} | Notas: TPC- {a[2][0]}; Projeto- {a[2][1]}; Teste- {a[2][2]}")
    print("-------------------------------------------------------------------------------------------")
    return 

def listarID(turma, id):
    for a in turma:
        if a[1]==id:
            print(f"Nome:{a[0]} | ID:{a[1]} | Notas: TPC- {a[2][0]}; Projeto- {a[2][1]}; Teste- {a[2][2]}")
    return

def guardarTurma(turma, fnome):
    file = open(fnome,"w") 
    for a in turma:
        file.write(str(a[0]) + " # " + str(a[1]) + " # " + str(a[2][0]) + " | " + str(a[2][1]) + " | " + str(a[2][2]))
        file.write("\n")
    file.close()


def recuperarTurma(fnome):
    turma= []
    file = open(fnome,"r")
    for line in file: 
        elem=line.split("#")
        nome, id, notas = elem[0], elem[1], elem[2]
        nota=notas.split(" | ")
        notaTPC, notaProj, notaTeste=nota[0],nota[1], nota[2]
        aluno=(nome, int(id), [int(notaTPC), int(notaProj), int(notaTeste)])
        turma.append(aluno)
    file.close()
    return turma


def menu():
    print(""" 
    --------------------------Menu--------------------------
    (1) Criar uma turma
    (2) Inserir um aluno na turma
    (3) Listar a turma
    (4) Consultar um aluno por id
    (8) Guardar a turma em ficheiro
    (9) Carregar uma turma dum ficheiro
    (0) Sair
    """)

opcao="1"
turma=[]
cond=True
while opcao != '0' and cond:
    menu()
    opcao = input("Introduza uma opção: ")
    if opcao=="1":
        print(criaTurma(turma))
    elif opcao=="2":
        if turma!=[]:
            id_a=int(input("Introduza o ID do aluno:"))
            nome_a=input("Introduza o nome do aluno:")
            notaTPC_a=int(input("Introduza a nota do TPC:"))
            notaProj_a=int(input("Introduza a nota do Projeto:"))
            notaTeste_a=int(input("Introduza a nota do Teste:"))
            aluno_a=(nome_a, id_a, [notaTPC_a, notaProj_a, notaTeste_a]) 
            turma_a=inserirAluno(turma, aluno_a)
            print(turma_a)
        else:
            print("A lista turma está vazia. Crie primeiro uma Lista!")
    elif opcao=="3":
        listarTurma( turma )
    elif opcao=="4":
        id_a=int(input("Introduza o ID do aluno:"))
        cond1=True
        i=0
        while cond1==True and i<len(turma):
            i=i+1
            for al in turma:
                if id_a==al[1]:
                    listarID(turma, id_a)
                    cond1=False
        if cond1==True:
            print("Esse aluno não pertence a esta turma.")
    elif opcao=="8":
        guardarTurma(turma, "turma.txt")
        print("A sua lista turma foi guardada no ficheiro turma.")
    elif opcao=="9":
        turma_a=recuperarTurma("turma.txt")
        print(turma_a)
    else:
        if opcao!="0":
            print("Resposta inválida")
        elif opcao==0:
            cond=False  
if opcao=="0":
    print("A aplicasão vai encerrar!")