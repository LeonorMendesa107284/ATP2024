import Projeto

import FreeSimpleGUI as sg

def menu():
    print("""
1 - Carregar Ata Médica
2 - Guardar Ata Médica
3 - Inserir Registo
4 - Apagar Registo por Título
5 - Consultar Registo por Título
6 - Consultar Registo por Autor
7 - Consultar Registo por Data
8 - Consultar Registo por Afiliação
9 - Consultar Registo por Palavras-Chave
10 - Listar Autores por Frequência e Aceder a Artigos
11 - Listar Autores por Ordem Alfabética e Aceder a Artigos
12 - Atualização dos Dados de uma Publicação
13 - Análise de Publicações por Frequência de Palavras-Chave
14 - Análise de Publicações por Ordem Alfabética de Palavras-Chave
15 - Estatística de Publicações por Ano
16 - Estatística de Publicações por Mês de um Determinado Ano
17 - Estatística dos Top 20 Autores
18 - Estatística de Publicações de um Autor por Anos
19 - Estatística das Top 20 Palavras-chave  
20 - Estatística de Palavras-chave mais Frequente por Ano     
0 - Sair da Aplicação
""")

ata_medica=[]
cond = True
while cond:
    menu()
    opcao = input("Introduza a opção desejada:")
    if opcao == "1":
        fnome = input("Introduza o nome do seu ficheiro (só são permitidos ficheiros em JSON):")
        if Projeto.verificar_arquivo_existente(fnome):
            if ".json" in fnome:
                ata_medica = Projeto.carregarAta(fnome)
                print("O seu ficheiro foi carregado com sucesso!")
            else:
                print("O seu ficheiro não foi carregado! Só são suportados ficheiros em .json")
        else:
            print(f"O arquivo '{fnome}' não foi encontrado na pasta onde se encontra.")        
    elif opcao == "2":
        if len(ata_medica) == 0:
            print("Desculpe, mas não existe nenhum ficheiro carregado. Utilize a opção 1 primeiramente!")
        else:
            fnome = input("Introduza o nome do ficheiro onde quer guardar a base de dados (só são permitidos ficheiros em JSON):")
            if ".json" in fnome:
                Projeto.guardarATA(fnome, ata_medica)
                print(f"A base de dados foi guardada no ficheiro : {fnome}")
            else:
                print("A sua base de dados não foi guardada! Só são suportados ficheiros em .json")
    elif opcao == "3":
        if len(ata_medica) == 0:
            print("Desculpe, mas não existe nenhum ficheiro carregado. Utilize a opção 1 primeiramente!")
        else:
            reg = {} 
            abstract = input("Introduza o abstract:")
            if abstract:
                reg["abstract"] = abstract
            keywords = input("Introduza palavra(s) chave(s):")
            if keywords:
                reg["keywords"] = keywords
            numero = input("Quantos autores tem este registo?")
            authors = []
            if numero!="" and numero!=None:
                for i in range(1, int(numero) + 1):
                    name = input(f"Introduza o {i}º nome:")
                    affiliation = input(f"Introduza a {i}ª afiliação:")
                    orcid = input(f"Introduza o {i}º orcid:")
                    autor = {}
                    if name:
                        autor["name"] = name
                    if affiliation:
                        autor["affiliation"] = affiliation
                    if orcid:
                        autor["orcid"] = orcid
                    if autor:  
                        authors.append(autor)
                if authors:
                    reg["authors"] = authors
            doi = input("Introduza o DOI:")
            if doi:
                reg["doi"] = doi
            pdf = input("Introduza o link do pdf:")
            if pdf:
                reg["pdf"] = pdf
            publish_date = input("Introduza a data (ano-mês-dia):")
            if publish_date:
                reg["publish_date"] = publish_date
            title = input("Introduza o título do registo:")
            if title:
                reg["title"] = title
            url = input("Introduza o url:")
            if url:
                reg["url"] = url
            if reg:
                Projeto.inserir(ata_medica, reg)
                print("Registo adicionado com sucesso!")
            else:
                print("Nenhum dado foi inserido, o registo está vazio.")
    elif opcao == "4":
        if len(ata_medica) == 0:
            print("Desculpe, mas não existe nenhum ficheiro carregado. Utilize a opção 1 primeiramente!")
        else:
            titulo = input("Introduza o título do registo que quer apagar:")
            res=Projeto.apagar(ata_medica,titulo)
            if res==True:
                print("O registo foi apagado com sucesso!")
            else:
                print("Não foi possivel encontrar esse título na lista de registos!")
    elif opcao == "5":
        if len(ata_medica) == 0:
           print("Desculpe, mas não existe nenhum ficheiro carregado. Utilize a opção 1 primeiramente!") 
        else:
            titulo = input("Introduza o título do registo que quer consultar:")
            res=Projeto.consultarTitulo_data(ata_medica, titulo, "consultarTitulo_data.txt")
            if res==True:
                print("Os registos foram guardados com sucesso! O nome do ficheiro é: consultarTitulo_data.txt ")
            else:
                print("Não é possivel encontrar nenhum registo com esse título!")
    elif opcao == "6":
        if len(ata_medica) == 0:
            print("Desculpe, mas não existe nenhum ficheiro carregado. Utilize a opção 1 primeiramente!")
        else:
            autor = input("Introduza o nome do autor do registo que quer consultar:")
            escolha = input("Deseja ordenar os registos por data ou por título? Responda com 1 (data) ou 2 (título):")
            while escolha != "1" and escolha != "2":
                print("A sua resposta é inválida!")
                escolha = input("Deseja ordenar os registos por data ou por título? Responda com 1 (data) ou 2 (título):")
            if escolha == "1": 
                res= Projeto.consultaAutor_data(ata_medica, autor, "consultaAutor_data.txt")
                if res==True:
                    print("Os resgistos foram guardados com sucesso! O nome do ficheiro é: consultaAutor_data.txt ")
                else:
                    print("Não é possivel encontrar nenhum registo com esse Autor!")
            else:
                res=Projeto.consultaAutor_tit(ata_medica, autor, "consultarAutor_tit.txt")
                if res==True:
                    print("Os resgistos foram guardados com sucesso! O nome do ficheiro é: consultarAutor_tit.txt")
                else:
                    print("Não é possivel encontrar nenhum registo com esse Autor!")
    elif opcao == "7":
        if len(ata_medica) == 0:
            print("Desculpe, mas não existe nenhum ficheiro carregado. Utilize a opção 1 primeiramente!")
        else:
            data = input("Introduza a data da registo que quer consultar:")
            res=Projeto.consultarData(ata_medica, data, "consultarData.txt")
            if res==True:
                print("Os resgistos foram guardados com sucesso! O nome do ficheiro é: consultarData.txt")
            else:
                print("Não é possivel encontrar nenhum registo com essa Data!")
    elif opcao == "8":
        if len(ata_medica) == 0:
            print("Desculpe, mas não existe nenhum ficheiro carregado. Utilize a opção 1 primeiramente!")
        else:
            afiliacao = input("Introduza a afiliação do registo que quer consultar:")
            escolha = input("Deseja ordenar os registos por data ou por título? Responda com 1 (data) ou 2 (título):")
            while escolha != "1" and escolha != "2":
                print("A sua resposta é inválida!")
                escolha = input("Deseja ordenar os registos por data ou por título? Responda com 1 (data) ou 2 (título):")
            if escolha == "1": 
                res= Projeto.consultaAfiliacao_Data(ata_medica, afiliacao, "consultaAfiliacao_Data.txt")
                if res==True:
                    print("Os resgistos foram guardados com sucesso! O nome do ficheiro é: consultaAfiliacao_Data.txt")
                else:
                    print("Não é possivel encontrar nenhum registo com essa Afiliação!")
            else:
                res= Projeto.consultaAfiliacao_Tit(ata_medica, afiliacao, "consultaAfiliacao_Tit.txt")
                if res==True:
                    print("Os resgistos foram guardados com sucesso! O nome do ficheiro é: consultaAfiliacao_Tit.txt")
                else:
                    print("Não é possivel encontrar nenhum registo com essa Afiliação!")
    elif opcao == "9":
        if len(ata_medica) == 0:
            print("Desculpe, mas não existe nenhum ficheiro carregado. Utilize a opção 1 primeiramente!")
        else:
            palavra_chave = input("Introduza a palavra-chave do registo que quer consultar:")
            escolha = input("Deseja ordenar os registos por data ou por título? Responda com 1 (data) ou 2 (título):")
            while escolha != "1" and escolha != "2":
                print("A sua resposta é inválida!")
                escolha = input("Deseja ordenar os registos por data ou por título? Responda com 1 (data) ou 2 (título):")
            if escolha == "1": 
                res=Projeto.consultarPalavra_Chave_Data(ata_medica, palavra_chave, "consultarPalavra_Chave_Data.txt")
                if res==True:
                    print("Os resgistos foram guardados com sucesso! O nome do ficheiro é: consultarPalavra_Chave_Data.txt")
                else:
                    print("Não é possivel encontrar nenhum registo com essa Palavra-Chave!")
            else:
                res=Projeto.consultarPalavra_Chave_Tit(ata_medica, palavra_chave, "consultarPalavra_Chave_Tit.txt")
                if res==True:
                    print("Os resgistos foram guardados com sucesso! O nome do ficheiro é: consultarPalavra_Chave_Tit.txt")
                else:
                    print("Não é possivel encontrar nenhum registo com essa Palavra-Chave!")
    elif opcao=="10":
        if len(ata_medica) == 0:
            print("Desculpe, mas não existe nenhum ficheiro carregado. Utilize a opção 1 primeiramente!")
        else:
            Projeto.listar_freq(ata_medica, "autores_freq.txt")
            print("A sua listagem foi guardada com sucesso no ficheiro: autores_freq.txt")
            escolha= input("Deseja aceder a algum registo de algum autor? (responda com 1 (sim) ou 2 (não)):")
            while escolha!="1" and escolha!="2":
                print("A sua resposta é inválida!")
                escolha= input("Deseja aceder a algum registo de algum autor? (responda com 1 (sim) ou 2 (não)):")
            if escolha=="1":
                nome=input("Introduza o nome do autor que pretende consultar:")
                print(Projeto.acederRes(ata_medica,nome))
                titulo= input("Introduza o título do registo que pretende aceder:")
                print(Projeto.acederURL(ata_medica, titulo))
    elif opcao=="11":
        if len(ata_medica) == 0:
            print("Desculpe, mas não existe nenhum ficheiro carregado. Utilize a opção 1 primeiramente!")
        else:
            Projeto.listarAutor_Alf(ata_medica, "autores_alf.txt")
            print("A sua listagem foi guardada com sucesso no ficheiro: autores_alf.txt")
            escolha= input("Deseja aceder a algum registo de algum autor? (responda com 1 (sim) ou 2 (não)):")
            while escolha!="1" and escolha!="2":
                print("A sua resposta é inválida!")
                escolha= input("Deseja aceder a algum registo de algum autor? (responda com 1 (sim) ou 2 (não)):")
            if escolha=="1":
                nome=input("Introduza o nome do autor que pretende consultar:")
                print(Projeto.acederRes(ata_medica,nome))
                titulo= input("Introduza o título do registo que pretende aceder:")
                print(Projeto.acederURL(ata_medica, titulo))
    elif opcao == "12":
       if len(ata_medica) == 0:
           print("Desculpe, mas não existe nenhum ficheiro carregado. Utilize a opção 1 primeiramente!")
       else:
           titulo = input("Introduza o título do registo que quer atualizar:")
           doi=""
           if titulo=="":
                doi = input("Caso não tenha título introduza o doi:")
           if titulo!="" or doi!="":
                data = input("Introduza a nova data:")
                resumo = input("Introduza o novo abstract:")
                palavra_chaves = input("Introduza as novas keywords:")
                numero = input("Quantos autores tem este registo?")
                authors=[]
                if numero!="" and numero!=None:
                    i=1
                    while i <= int(numero):
                            name = input(f"Introduza o {i}º nome:")
                            affiliation = input(f"Introduza a {i}ª afiliação:")
                            orcid = input(f"Introduza o {i}º orcid:")
                            i = i + 1
                            if name != "":
                                if affiliation != "":
                                    authors.append({"name": name, "affiliation": affiliation})
                                else:
                                    authors.append({"name": name})
                res=Projeto.atual_reg(ata_medica, titulo, doi , data, resumo, palavra_chaves, authors)
                if res==True:
                    print("O seu registo foi atualizado com sucesso!")
                else:
                    print("Não foi possivel encontrar nenhum registo com esse título/doi.")
           else:
               print("Tem de preencher o campo do título! Só caso não tenha título preencha o campo do doi.")          
    elif opcao=="13":
        if len(ata_medica) == 0:
           print("Desculpe, mas não existe nenhum ficheiro carregado. Utilize a opção 1 primeiramente!")
        else:
            Projeto.analise_palavra_chave_freq(ata_medica, "palavras_chave_freq.txt")
            print(f"A sua listagem foi guardada no ficheiro : palavras_chave_freq.txt")
            escolha= input("Deseja aceder às publicações de alguma Palavra-Chave? (responda com 1 (sim) ou 2 (não)):")
            while escolha!="1" and escolha!="2":
                print("A sua resposta é inválida!")
                escolha= input("Deseja aceder às publicações de alguma Palavra-Chave? (responda com 1 (sim) ou 2 (não)):")
            if escolha=="1":
                palavra=input("Introduza a Palavra-Chave para consultar mais informações:")
                res=Projeto.aceder_pubs_pal(ata_medica, palavra, "pubs_pal_selecionada.txt")
                if res==True:
                    print(f"Os registos com a palavra-chave -{palavra}- foram guardados num ficheiro cujo nome é: pubs_pal_selecionada.txt")
                else:
                    print("Não é possivel encontrar nenhum registo com essa palavra-chave!")
    elif opcao=="14":
        if len(ata_medica) == 0:
           print("Desculpe, mas não existe nenhum ficheiro carregado. Utilize a opção 1 primeiramente!")
        else:
            Projeto.analise_palavra_chave_alf(ata_medica, "palavras_chave_ord_alf.txt")
            print(f"A sua listagem foi guardada no ficheiro : palavras_chave_ord_alf.txt")
            escolha= input("Deseja aceder às publicações de alguma Palavra-Chave? (responda com 1 (sim) ou 2 (não)):")
            while escolha!="1" and escolha!="2":
                print("A sua resposta é inválida!")
                escolha= input("Deseja aceder às publicações de alguma Palavra-Chave? (responda com 1 (sim) ou 2 (não)):")
            if escolha=="1":
                palavra=input("Introduza a Palavra-Chave para consultar mais informações:")
                res=Projeto.aceder_pubs_pal(ata_medica, palavra, "pubs_pal_selecionada.txt")
                if res==True:
                    print(f"Os registos com a palavra-chave -{palavra}- foram guardados num ficheiro cujo nome é: pubs_pal_selecionada.txt")
                else:
                    print("Não é possivel encontrar nenhum registo com essa palavra-chave!")
    elif opcao=="15":
        if len(ata_medica) == 0:
            print("Desculpe, mas não existe nenhum ficheiro carregado. Utilize a opção 1 primeiramente!")
        else:
            Projeto.distribPub_Ano(ata_medica)
    elif opcao=="16":
        if len(ata_medica) == 0:
            print("Desculpe, mas não existe nenhum ficheiro carregado. Utilize a opção 1 primeiramente!")
        else:
            ano= input("Introduza o ano que pretende analisar:")
            res=Projeto.distribPub_Mes(ata_medica, ano)
            if res==False:
                print("Não existe nenhum registo de publicações nesse ano!")
    elif opcao=="17":
        if len(ata_medica) == 0:
            print("Desculpe, mas não existe nenhum ficheiro carregado. Utilize a opção 1 primeiramente!")
        else:
            Projeto.distribTop20_Autor(ata_medica)
    elif opcao=="18":
        if len(ata_medica) == 0:
            print("Desculpe, mas não existe nenhum ficheiro carregado. Utilize a opção 1 primeiramente!")
        else:
            autor= input("Introduza o autor que pretende analisar:")
            res=Projeto.distribPub_Autor(ata_medica, autor)
            if res==False:
                print("Não existe nenhum registo de publicações desse autor!")
    elif opcao=="19":
        if len(ata_medica) == 0:
            print("Desculpe, mas não existe nenhum ficheiro carregado. Utilize a opção 1 primeiramente!")
        else:
            Projeto.distribPalavras_Freq(ata_medica)
    elif opcao=="20":
        if len(ata_medica) == 0:
            print("Desculpe, mas não existe nenhum ficheiro carregado. Utilize a opção 1 primeiramente!")
        else:
            ano=input("Introduza o ano que pretende consultar as top 20 palavras_chave: ")
            res=Projeto.distribPalavras_Freq_Ano(ata_medica, ano)
            if res==False:
                print("Não existe nenhum registo de palavras-chave nesse ano!")
    elif opcao == '0':
        cond = False
        print("A aplicação vai encerrar. Volte sempre!!")
    else:
        print("A opção que introduziu é inválida. Por favor, escolha uma opção entre 0 e 20")
    
