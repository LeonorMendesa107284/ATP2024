import json
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import random
import os

def verificar_arquivo_existente(ficheiro):
    existir = os.path.join("./", ficheiro)
    return os.path.isfile(existir)

def carregarAta(fnome):
    f = open("./" + fnome, encoding='utf-8')
    atamed = json.load(f)
    f.close()
    return atamed

def guardarATA(fnome, lista):
    fout = open('./' + fnome, "w")
    json.dump(lista, fout)
    fout.close()
    return

def inserir(lista,reg):
    lista.append(reg)
    return 

def apagar(lista,titulo):
    res=-1
    encontrado=False
    i=0
    while not encontrado and i<len(lista):
        if 'title' in lista[i]:
            if lista[i]["title"]==titulo:
                encontrado=True
                res=i
            else:
                i=i+1
        else:
            i=i+1
    if encontrado==True:
        del lista[res]
        a=True
    else:
        a=False
    return a

def ordena_data(registo):
    return registo['publish_date']

def remover_acentos(texto):
    acentos = {
        'á': 'a', 'à': 'a', 'ã': 'a', 'â': 'a', 'ä': 'a',
        'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e',
        'í': 'i', 'ì': 'i', 'î': 'i', 'ï': 'i',
        'ó': 'o', 'ò': 'o', 'õ': 'o', 'ô': 'o', 'ö': 'o',
        'ú': 'u', 'ù': 'u', 'û': 'u', 'ü': 'u',
        'ç': 'c',
        'Á': 'A', 'À': 'A', 'Ã': 'A', 'Â': 'A', 'Ä': 'A',
        'É': 'E', 'È': 'E', 'Ê': 'E', 'Ë': 'E',
        'Í': 'I', 'Ì': 'I', 'Î': 'I', 'Ï': 'I',
        'Ó': 'O', 'Ò': 'O', 'Õ': 'O', 'Ô': 'O', 'Ö': 'O',
        'Ú': 'U', 'Ù': 'U', 'Û': 'U', 'Ü': 'U',
        'Ç': 'C',
        'Ş': 'S'
    }
    return ''.join(acentos.get(c, c) for c in texto)

def consultarTitulo_data(lista,titulo, ficheiro):
    tit=[]
    reg_data=[]
    reg_sem_data=[]
    final=[]
    i=0
    while i<len(lista):
        if 'title' in lista[i]:
            if lista[i]["title"]==titulo:
                tit.append(lista[i])
        i=i+1
    if tit!=[]:
        for reg in tit:
            if 'publish_date' in reg:
                reg_data.append(reg)
            else:
                reg_sem_data.append(reg)
        res=sorted(reg_data, key=ordena_data)
        final=res+reg_sem_data
        f = open("./"+ficheiro,"w", encoding="utf-8")
        f.write("-_-_-_-_-_ Lista de Títulos Ordenados Pelas Datas _-_-_-_-_-\n")
        f.write("\n")
        i=1
        for reg in final:
            f.write(f" - - - - - - - - - - - - Registo nº{i} - - - - - - - - - - - -\n")
            if "abstract" in reg:
                f.write(f"Abstract: {reg["abstract"]}\n")
            if "keywords" in reg:
                f.write(f"Keywords: {reg["keywords"]}\n")
            if "authors" in reg:
                f.write(f"Authors:\n")
                for autor in reg["authors"]:
                    if "name" in autor:
                        f.write(f"    Name: {autor["name"]}\n")
                    if "affiliation" in autor:
                        f.write(f"    Affiliation: {autor["affiliation"]}\n")
                    if "orcid" in autor:
                        f.write(f"    Orcid: {autor["orcid"]}\n")
            if "doi" in reg:
                f.write(f"Doi: {reg["doi"]}\n")
            if "pdf" in reg:
                f.write(f"Pdf: {reg["pdf"]}\n")
            if "publish_date" in reg:
                f.write(f"Publish-date: {reg["publish_date"]}\n")
            if "title" in reg:
                f.write(f"Title: {reg["title"]}\n")
            if "url" in reg:
                f.write(f"Url: {reg["url"]}\n")
            f.write("\n")
            f.write("\n")
            i=i+1
        f.close() 
        resposta=True
    else:
        resposta=False
    return resposta

def consultaAutor_data(lista, autor, ficheiro):
    i=0
    pubs=[]
    reg_data=[]
    reg_sem_data=[]
    final=[]
    while i<len(lista):
        if 'authors' in lista[i]:
            for nome in lista[i]["authors"]:
                if nome["name"]==autor:
                    pubs.append(lista[i])
        i=i+1
    if pubs!=[]:
        for reg in pubs:
            if 'publish_date' in reg:
                reg_data.append(reg)
            else:
                reg_sem_data.append(reg)
        res=sorted(reg_data, key=ordena_data)
        final=res+reg_sem_data
        f = open("./" +ficheiro,"w", encoding="utf-8")
        f.write("-_-_-_-_-_ Lista de Autores Ordenados Pelas Datas _-_-_-_-_-\n")
        i=1
        for reg in final:
            f.write(f"- - - - - - - - - - - - Registo nº{i} - - - - - - - - - - - -\n")
            if "abstract" in reg:
                f.write(f"Abstract: {reg["abstract"]}\n")
            if "keywords" in reg:
                f.write(f"Keywords: {reg["keywords"]}\n")
            if "authors" in reg:
                f.write(f"Authors:\n")
                for autor in reg["authors"]:
                    if "name" in autor:
                        f.write(f"    Name: {autor["name"]}\n")
                    if "affiliation" in autor:
                        f.write(f"    Affiliation: {autor["affiliation"]}\n")
                    if "orcid" in autor:
                        f.write(f"    Orcid: {autor["orcid"]}\n")
            if "doi" in reg:
                f.write(f"Doi: {reg["doi"]}\n")
            if "pdf" in reg:
                f.write(f"Pdf: {reg["pdf"]}\n")
            if "publish_date" in reg:
                f.write(f"Publish-date: {reg["publish_date"]}\n")
            if "title" in reg:
                f.write(f"Title: {reg["title"]}\n")
            if "url" in reg:
                f.write(f"Url: {reg["url"]}\n")
            f.write("\n")
            f.write("\n")
            i=i+1
        f.close() 
        resposta=True
    else:
        resposta=False
    return resposta

def consultaAutor_tit(lista, autor, ficheiro):
    i=0
    pubs=[]
    reg_tit=[]
    reg_sem_tit=[]
    final=[]
    while i<len(lista):
        if 'authors' in lista[i]:
            for nome in lista[i]["authors"]:
                if nome["name"]==autor:
                    pubs.append(lista[i])
        i=i+1
    if pubs!=[]:
        for reg in pubs:
            if 'title' in reg:
                reg_tit.append(reg)
            else:
                reg_sem_tit.append(reg)
        res=sorted(reg_tit, key= lambda x: remover_acentos(x["title"].lower()))
        final=res+reg_sem_tit
        f = open("./" +ficheiro,"w", encoding="utf-8")
        f.write("-_-_-_-_-_ Lista de Autores Ordenados Pelo Título _-_-_-_-_-\n")
        i=1
        for reg in final:
            f.write(f"- - - - - - - - - - - - Registo nº{i} - - - - - - - - - - - -\n")
            if "abstract" in reg:
                f.write(f"Abstract: {reg["abstract"]}\n")
            if "keywords" in reg:
                f.write(f"Keywords: {reg["keywords"]}\n")
            if "authors" in reg:
                f.write(f"Authors:\n")
                for autor in reg["authors"]:
                    if "name" in autor:
                        f.write(f"    Name: {autor["name"]}\n")
                    if "affiliation" in autor:
                        f.write(f"    Affiliation: {autor["affiliation"]}\n")
                    if "orcid" in autor:
                        f.write(f"    Orcid: {autor["orcid"]}\n")
            if "doi" in reg:
                f.write(f"Doi: {reg["doi"]}\n")
            if "pdf" in reg:
                f.write(f"Pdf: {reg["pdf"]}\n")
            if "publish_date" in reg:
                f.write(f"Publish-date: {reg["publish_date"]}\n")
            if "title" in reg:
                f.write(f"Title: {reg["title"]}\n")
            if "url" in reg:
                f.write(f"Url: {reg["url"]}\n")
            f.write("\n")
            f.write("\n")
            i=i+1
        f.close() 
        resposta=True
    else:
        resposta=False
    return resposta

def consultarData(lista, data,ficheiro):
    i=0
    pubs=[]
    reg_tit=[]
    reg_sem_tit=[]
    final=[]
    while i<len(lista):
        if 'publish_date' in lista[i]:
            if lista[i]["publish_date"]==data:
                pubs.append(lista[i])
        i=i+1
    if pubs!=[]:
        for reg in pubs:
            if 'title' in reg:
                reg_tit.append(reg)
            else:
                reg_sem_tit.append(reg)
        res=sorted(reg_tit, key= lambda x: remover_acentos(x["title"].lower()))
        final=res+reg_sem_tit
        f = open("./" +ficheiro,"w", encoding="utf-8")
        f.write(f"-_-_-_-_-_ Lista de Registos do Dia -{data}- Ordenados Pelos Titulos  _-_-_-_-_-\n")
        i=1
        for reg in final:
            f.write(f"- - - - - - - - - - - - Registo nº{i} - - - - - - - - - - - -\n")
            if "abstract" in reg:
                f.write(f"Abstract: {reg["abstract"]}\n")
            if "keywords" in reg:
                f.write(f"Keywords: {reg["keywords"]}\n")
            if "authors" in reg:
                f.write(f"Authors:\n")
                for autor in reg["authors"]:
                    if "name" in autor:
                        f.write(f"    Name: {autor["name"]}\n")
                    if "affiliation" in autor:
                        f.write(f"    Affiliation: {autor["affiliation"]}\n")
                    if "orcid" in autor:
                        f.write(f"    Orcid: {autor["orcid"]}\n")
            if "doi" in reg:
                f.write(f"Doi: {reg["doi"]}\n")
            if "pdf" in reg:
                f.write(f"Pdf: {reg["pdf"]}\n")
            if "publish_date" in reg:
                f.write(f"Publish-date: {reg["publish_date"]}\n")
            if "title" in reg:
                f.write(f"Title: {reg["title"]}\n")
            if "url" in reg:
                f.write(f"Url: {reg["url"]}\n")
            f.write("\n")
            f.write("\n")
            i=i+1
        f.close() 
        resposta=True
    else:
        resposta=False
    return resposta

def consultaAfiliacao_Data(lista, afiliacao, ficheiro):
    i = 0
    pubs=[]
    reg_data=[]
    reg_sem_data=[]
    final=[]
    while i<len(lista):
        if 'authors' in lista[i]:
            for autor in lista[i]["authors"]:
                if "affiliation" in autor:
                    if afiliacao==autor['affiliation'] and lista[i] not in pubs:
                        pubs.append(lista[i])
        i=i+1
    if pubs!=[]:
        for reg in pubs:
            if 'publish_date' in reg:
                reg_data.append(reg)
            else:
                reg_sem_data.append(reg)
        res=sorted(reg_data, key=ordena_data)
        final=res+reg_sem_data
        f = open("./" +ficheiro,"w", encoding="utf-8")
        f.write("-_-_-_-_-_ Lista de Registos Ordenados Pelas Datas _-_-_-_-_-\n")
        i=1
        for reg in final:
            f.write(f"- - - - - - - - - - - - Registo nº{i} - - - - - - - - - - - -\n")
            if "abstract" in reg:
                f.write(f"Abstract: {reg["abstract"]}\n")
            if "keywords" in reg:
                f.write(f"Keywords: {reg["keywords"]}\n")
            if "authors" in reg:
                f.write(f"Authors:\n")
                for autor in reg["authors"]:
                    if "name" in autor:
                        f.write(f"    Name: {autor["name"]}\n")
                    if "affiliation" in autor:
                        f.write(f"    Affiliation: {autor["affiliation"]}\n")
                    if "orcid" in autor:
                        f.write(f"    Orcid: {autor["orcid"]}\n")
            if "doi" in reg:
                f.write(f"Doi: {reg["doi"]}\n")
            if "pdf" in reg:
                f.write(f"Pdf: {reg["pdf"]}\n")
            if "publish_date" in reg:
                f.write(f"Publish-date: {reg["publish_date"]}\n")
            if "title" in reg:
                f.write(f"Title: {reg["title"]}\n")
            if "url" in reg:
                f.write(f"Url: {reg["url"]}\n")
            f.write("\n")
            f.write("\n")
            i=i+1
        f.close() 
        resposta=True
    else:
        resposta=False
    return resposta

def consultaAfiliacao_Tit(lista, afiliacao, ficheiro):
    i = 0
    pubs=[]
    reg_tit=[]
    reg_sem_tit=[]
    final=[]
    while i<len(lista):
        if 'authors' in lista[i]:
            for autor in lista[i]["authors"]:
                if "affiliation" in autor:
                    if afiliacao==autor['affiliation'] and lista[i] not in pubs:
                        pubs.append(lista[i])
        i=i+1
    if pubs!=[]:
        for reg in pubs:
            if 'title' in reg:
                reg_tit.append(reg)
            else:
                reg_sem_tit.append(reg)
        res=sorted(reg_tit, key= lambda x: remover_acentos(x["title"].lower()))
        final=res+reg_sem_tit
        f = open("./" +ficheiro,"w", encoding="utf-8")
        f.write(f"-_-_-_-_-_ Lista de Registos Ordenados Pelo Título  _-_-_-_-_-\n")
        i=1
        for reg in final:
            f.write(f"- - - - - - - - - - - - Registo nº{i} - - - - - - - - - - - -\n")
            if "abstract" in reg:
                f.write(f"Abstract: {reg["abstract"]}\n")
            if "keywords" in reg:
                f.write(f"Keywords: {reg["keywords"]}\n")
            if "authors" in reg:
                f.write(f"Authors:\n")
                for autor in reg["authors"]:
                    if "name" in autor:
                        f.write(f"    Name: {autor["name"]}\n")
                    if "affiliation" in autor:
                        f.write(f"    Affiliation: {autor["affiliation"]}\n")
                    if "orcid" in autor:
                        f.write(f"    Orcid: {autor["orcid"]}\n")
            if "doi" in reg:
                f.write(f"Doi: {reg["doi"]}\n")
            if "pdf" in reg:
                f.write(f"Pdf: {reg["pdf"]}\n")
            if "publish_date" in reg:
                f.write(f"Publish-date: {reg["publish_date"]}\n")
            if "title" in reg:
                f.write(f"Title: {reg["title"]}\n")
            if "url" in reg:
                f.write(f"Url: {reg["url"]}\n")
            f.write("\n")
            f.write("\n")
            i=i+1
        f.close()
        resposta=True
    else:
        resposta=False
    return resposta

def consultarPalavra_Chave_Data(lista, palavra_chave, ficheiro):
    i=0
    pubs=[]
    reg_data=[]
    reg_sem_data=[]
    final=[]
    while i<len(lista):
        if "keywords" in lista[i]:
            palavras=lista[i]["keywords"].split(", ")
            for p in palavras:
                if palavra_chave==p:
                    pubs.append(lista[i])
        i=i+1
    if pubs!=[]:
        for reg in pubs:
            if 'publish_date' in reg:
                reg_data.append(reg)
            else:
                reg_sem_data.append(reg)
        res=sorted(reg_data, key=ordena_data)
        final=res+reg_sem_data
        f = open("./" +ficheiro,"w", encoding="utf-8")
        f.write(f"-_-_-_-_-_ Lista de Registos com a Palavra-Chave -{palavra_chave}- Ordenados Pelas Datas _-_-_-_-_-\n")
        i=1
        for reg in final:
            f.write(f"- - - - - - - - - - - - Registo nº{i} - - - - - - - - - - - -\n")
            if "abstract" in reg:
                f.write(f"Abstract: {reg["abstract"]}\n")
            if "keywords" in reg:
                f.write(f"Keywords: {reg["keywords"]}\n")
            if "authors" in reg:
                f.write(f"Authors:\n")
                for autor in reg["authors"]:
                    if "name" in autor:
                        f.write(f"    Name: {autor["name"]}\n")
                    if "affiliation" in autor:
                        f.write(f"    Affiliation: {autor["affiliation"]}\n")
                    if "orcid" in autor:
                        f.write(f"    Orcid: {autor["orcid"]}\n")
            if "doi" in reg:
                f.write(f"Doi: {reg["doi"]}\n")
            if "pdf" in reg:
                f.write(f"Pdf: {reg["pdf"]}\n")
            if "publish_date" in reg:
                f.write(f"Publish-date: {reg["publish_date"]}\n")
            if "title" in reg:
                f.write(f"Title: {reg["title"]}\n")
            if "url" in reg:
                f.write(f"Url: {reg["url"]}\n")
            f.write("\n")
            f.write("\n")
            i=i+1
        f.close()
        resposta=True
    else:
        resposta=False
    return resposta

def consultarPalavra_Chave_Tit(lista, palavra_chave, ficheiro):
    i = 0
    pubs=[]
    reg_tit=[]
    reg_sem_tit=[]
    final=[]
    while i<len(lista):
        if "keywords" in lista[i]:
            palavras=lista[i]["keywords"].split(", ")
            for p in palavras:
                if palavra_chave==p:
                    pubs.append(lista[i])
        i=i+1
    if pubs!=[]:
        for reg in pubs:
            if 'title' in reg:
                reg_tit.append(reg)
            else:
                reg_sem_tit.append(reg)
        res=sorted(reg_tit, key= lambda x: remover_acentos(x["title"].lower()))
        final=res+reg_sem_tit
        f = open("./" +ficheiro,"w", encoding="utf-8")
        f.write(f"-_-_-_-_-_ Lista de Registos com a Palavra-Chave -{palavra_chave}- Ordenados Pelos Titulos _-_-_-_-_-\n")
        i=1
        for reg in final:
            f.write(f"- - - - - - - - - - - - Registo nº{i} - - - - - - - - - - - -\n")
            if "abstract" in reg:
                f.write(f"Abstract: {reg["abstract"]}\n")
            if "keywords" in reg:
                f.write(f"Keywords: {reg["keywords"]}\n")
            if "authors" in reg:
                f.write(f"Authors:\n")
                for autor in reg["authors"]:
                    if "name" in autor:
                        f.write(f"    Name: {autor["name"]}\n")
                    if "affiliation" in autor:
                        f.write(f"    Affiliation: {autor["affiliation"]}\n")
                    if "orcid" in autor:
                        f.write(f"    Orcid: {autor["orcid"]}\n")
            if "doi" in reg:
                f.write(f"Doi: {reg["doi"]}\n")
            if "pdf" in reg:
                f.write(f"Pdf: {reg["pdf"]}\n")
            if "publish_date" in reg:
                f.write(f"Publish-date: {reg["publish_date"]}\n")
            if "title" in reg:
                f.write(f"Title: {reg["title"]}\n")
            if "url" in reg:
                f.write(f"Url: {reg["url"]}\n")
            f.write("\n")
            f.write("\n")
            i=i+1
        f.close() 
        resposta=True
    else:
        resposta=False
    return resposta
    
def OrdenaAutores(lista_autores):
    return lista_autores[1]

def listar_freq(lista, ficheiro):
    freq_autores={}
    for dic in lista:
        if "authors" in dic:
            for autor in dic['authors']:
                if autor['name'] in freq_autores:
                    freq_autores[autor['name']]=freq_autores[autor['name']]+1
                elif autor['name'] not in freq_autores:
                    freq_autores[autor['name']]=1
    dist=sorted(freq_autores.items(), key=OrdenaAutores, reverse=True) 
    f = open("./" +ficheiro,"w", encoding="utf-8")
    f.write(f"-_-_-_-_-_ Lista de Autores pela Frequência _-_-_-_-_-\n")
    for autor in dist:
        f.write (f"{autor [0]} - {autor[1]} artigos \n")
    return ""

def listarAutor_Alf(lista,ficheiro):
    res = []
    for d in lista:
        for autor in d['authors']:
            if autor['name'] not in res:
                res.append(autor['name'])
    res = sorted(res, key=lambda x: remover_acentos(x.lower()))
    f = open("./" +ficheiro,"w", encoding="utf-8")
    f.write(f"-_-_-_-_-_ Lista de Autores por Ordem Alfabética _-_-_-_-_-\n")
    for autor in res:
        f.write (f"{autor} \n")
    return ""

def listarAutor_Alf_Inter(lista):
    res = []
    for d in lista:
        for autor in d['authors']:
            if autor['name'] not in res:
                res.append(autor['name'])
    res = sorted(res, key=lambda x: remover_acentos(x.lower()))
    return res

def listar_freq_Inter(lista):
    freq_autores={}
    for dic in lista:
        if "authors" in dic:
            for autor in dic['authors']:
                if autor['name'] in freq_autores:
                    freq_autores[autor['name']]=freq_autores[autor['name']]+1
                elif autor['name'] not in freq_autores:
                    freq_autores[autor['name']]=1
    dist=sorted(freq_autores.items(), key=OrdenaAutores, reverse=True) 
    return [f"{autor} - {freq} artigos" for autor, freq in dist]

def acederRes(lista, nome):
    post=[]
    for dic in lista:
        for autor in dic["authors"]:
            if autor["name"]==nome:
                if 'title' in dic:
                    post.append(dic["title"])
                else:
                    post.append(dic["abstract"])
                    print(f"Um artigo deste autor não tem título, pelo que apresentamos o abstract. O doi deste artigo é: {dic['doi']}")
    if post==[]:
        print("Não existe esse autor na lista!")
    else:
        print("\n")
        print(f" --------------Lista de títulos do autor {nome}------------------ ")
        for pub in post:
            print(pub)
    return ""

def acederRes_Inter(lista, nome):
    post=[]
    for dic in lista:
        for autor in dic["authors"]:
            if autor["name"]==nome:
                if 'title' in dic:
                    post.append(dic["title"])
                else:
                    post.append(dic["abstract"])
                    print(f"Um artigo deste autor não tem título, pelo que apresentamos o abstract. O doi deste artigo é: {dic['doi']}")
    if post==[]:
        print("Não existe esse autor na lista!")
    return post

def acederURL_Inter(lista, titulo):
    res=[]
    for dic in lista:
        if "title" in dic and dic['title']==titulo:
            if 'url' in dic:
                res.append(dic['url'])
            else:
                print("Este dicionário não tem URL!")
    return res

def acederURL(lista, titulo):
    res=""
    for dic in lista:
        if "title" in dic and dic['title']==titulo:
            res =dic['title']
            if 'url' in dic:
                print(dic['url'])
            else:
                print("Este dicionário não tem URL!")
    if res=="":
        print("Esse título não existe!")
    return ""

def distribGrafico(d):
    valores=list(d.values())
    labels=list(d.keys())
    cores_nomeadas=list(x for x in mcolors.CSS4_COLORS.keys() if x not in ("white", "whitesmoke", "snow", "liteyellow", "liteblue", "litegreen"))
    random.shuffle(cores_nomeadas)
    cores_personalizadas=cores_nomeadas[:len(labels)]
    plt.figure(figsize=(9,9))
    plt.bar(labels, valores, color=cores_personalizadas)
    plt.title('Distribuição dos Top 20 Autores')
    plt.xticks(rotation=30, ha='right', fontsize=7)
    plt.show()

def distribTop20_Autor(lista):
    top_autores={}
    for dic in lista:
        if "authors" in dic:
            for autor in dic['authors']:
                if autor['name'] in top_autores:
                    top_autores[autor['name']]=top_autores[autor['name']]+1
                elif autor['name'] not in top_autores:
                    top_autores[autor['name']]=1
    
    dist=sorted(top_autores.items(), key=OrdenaAutores, reverse=True)[:21]  
    return distribGrafico(dict(dist))

def atual_reg(lista, titulo, doi , data, resumo,palavra_chaves, autores):
    cond=False
    for reg in lista:
        if "title" in reg:
            if reg["title"]==titulo:
                cond=True
                if data != "":
                    reg["publish_date"]=data
                if resumo!="":
                    reg["abstract"]=resumo
                if palavra_chaves!="":
                    reg['keywords']=palavra_chaves
                if autores!=[] :
                    for autor in autores:
                        reg["authors"].append(autor)
                
        else:
            if "doi" in reg:
                if reg["doi"]==doi:
                    cond=True
                    if data != "":
                        reg["publish_date"]=data
                    if resumo!="":
                        reg["abstract"]=resumo
                    if palavra_chaves!="":
                        reg["keywords"]=palavra_chaves
                    if autores!=[] :
                        for autor in autores:
                            reg["authors"].append(autor)
    return cond

def analise_palavra_chave_freq(lista, ficheiro):
    palavras={}
    for dic in lista:
        if "keywords" in dic:
            palavra_chave=dic["keywords"].split(", ")
            for p in palavra_chave:
                if p in palavras:
                    palavras[p]=palavras[p]+1
                elif p not in palavras:
                    palavras[p]=1
    dist=sorted(palavras.items(), key=OrdenaAutores, reverse=True) 
    f = open("./" +ficheiro,"w", encoding="utf-8")
    f.write("- - - - - Lista de Palavras Chave Por Frequência - - - - -\n")
    f.write(f"| Palavra-Chave :: Frequência |\n")
    for palavra in dist:
        f.write(f" {palavra[0]} :: {palavra[1]} \n")
    f.close() 
    return

def analise_palavra_chave_alf(lista, ficheiro):
    palavras = []
    for dic in lista:
        if "keywords" in dic:
            palavra_chave = dic["keywords"].split(", ")
            for palavra in palavra_chave:
                if palavra not in palavras:
                    palavras.append(palavra)
    palavras_list=sorted(palavras, key= lambda x: remover_acentos(x.lower())) 
    f = open("./" +ficheiro,"w", encoding="utf-8")
    f.write("- - - - - Lista de Palavras Chave Por Ordem Alfabética - - - - -\n")
    for palavra in palavras_list:
        f.write(f"{palavra}\n")
    f.close() 
    return 

def aceder_pubs_pal(lista, pal, ficheiro):
    publicacoes=[]
    for dic in lista:
        if "keywords" in dic:
            palavra_chave = dic["keywords"].split(", ")
            for palavra in palavra_chave:
                if palavra==pal:
                    publicacoes.append(dic)
    if publicacoes!=[]:
        f = open("./" +ficheiro,"w", encoding="utf-8")
        f.write(f"-_-_-_-_-_ Lista de Registos Com a Palavra-Chave: {pal} _-_-_-_-_-\n")
        i=1
        for reg in publicacoes:
            f.write(f"- - - - - - - - - - - - Registo nº{i} - - - - - - - - - - - -\n")
            if "abstract" in reg:
                f.write(f"Abstract: {reg["abstract"]}\n")
            if "keywords" in reg:
                f.write(f"Keywords: {reg["keywords"]}\n")
            if "authors" in reg:
                f.write(f"Authors:\n")
                for autor in reg["authors"]:
                    if "name" in autor:
                        f.write(f"    Name: {autor["name"]}\n")
                    if "affiliation" in autor:
                        f.write(f"    Affiliation: {autor["affiliation"]}\n")
                    if "orcid" in autor:
                        f.write(f"    Orcid: {autor["orcid"]}\n")
            if "doi" in reg:
                f.write(f"Doi: {reg["doi"]}\n")
            if "pdf" in reg:
                f.write(f"Pdf: {reg["pdf"]}\n")
            if "publish_date" in reg:
                f.write(f"Publish-date: {reg["publish_date"]}\n")
            if "title" in reg:
                f.write(f"Title: {reg["title"]}\n")
            if "url" in reg:
                f.write(f"Url: {reg["url"]}\n")
            f.write("\n")
            f.write("\n")
            i=i+1
        f.close()
        resposta=True
    else:
        resposta=False
    return resposta

def Ordena_Ano_Mes(dic):
    return dic[0]

def distribGrafico_Ano(d):
    valores=list(d.values())
    labels=list(d.keys())
    cores_nomeadas=list(x for x in mcolors.CSS4_COLORS.keys() if x not in ("white", "whitesmoke", "snow", "ligthyellow", "ligthblue", "ligthgreen"))
    random.shuffle(cores_nomeadas)
    cores_personalizadas=cores_nomeadas[:len(labels)]
    plt.figure(figsize=(9,9))
    plt.bar(labels, valores, color=cores_personalizadas)
    plt.title('Distribuição de Publicações por Ano')
    plt.xticks(rotation=30, ha='right', fontsize=7)
    plt.show()

def distribPub_Ano(lista):
    pub_ano={}
    for dic in lista:
        if "publish_date" in dic:
            if dic["publish_date"][:4] in pub_ano:
                pub_ano[dic["publish_date"][:4]]=pub_ano[dic["publish_date"][:4]]+1
            elif dic["publish_date"][:4] not in pub_ano:
                pub_ano[dic["publish_date"][:4]]=1 
    dist=sorted(pub_ano.items(), key=Ordena_Ano_Mes)  
    return distribGrafico_Ano(dict(dist))

def distribGrafico_Mes(d):
    valores=list(d.values())
    labels=list(d.keys())
    if valores!=[] and labels!=[]:
        cond=True
        cores_nomeadas=list(x for x in mcolors.CSS4_COLORS.keys() if x not in ("white", "whitesmoke", "snow", "ligthyellow", "ligthblue", "ligthgreen"))
        random.shuffle(cores_nomeadas)
        cores_personalizadas=cores_nomeadas[:len(labels)]
        plt.figure(figsize=(9,9))
        plt.bar(labels, valores, color=cores_personalizadas)
        plt.title('Distribuição de Publicações por Mês de um Determinado Ano')
        plt.xticks(rotation=30, ha='right', fontsize=7)
        plt.show()
    else:
        cond=False
    return cond
    
def distribPub_Mes(lista,ano):
    pub_mes={}
    for dic in lista:
        if "publish_date" in dic:
            if dic["publish_date"][:4] ==ano:
                if dic["publish_date"][5:7] in pub_mes:
                    pub_mes[dic["publish_date"][5:7]]=pub_mes[dic["publish_date"][5:7]]+1
                else:
                    pub_mes[dic["publish_date"][5:7]]=1 
    dist=sorted(pub_mes.items(), key=Ordena_Ano_Mes)  
    return distribGrafico_Mes(dict(dist))

def distribGrafico_Autor(d):
    valores=list(d.values())
    labels=list(d.keys())
    if valores!=[] and labels!=[]:
        cond=True
        cores_nomeadas=list(x for x in mcolors.CSS4_COLORS.keys() if x not in ("white", "whitesmoke", "snow", "ligthyellow", "ligthblue", "ligthgreen"))
        random.shuffle(cores_nomeadas)
        cores_personalizadas=cores_nomeadas[:len(labels)]
        plt.figure(figsize=(9,9))
        plt.bar(labels, valores, color=cores_personalizadas)
        plt.title('Distribuição de Publicações de um autor por Anos')
        plt.xticks(rotation=30, ha='right', fontsize=7)
        plt.show()
    else:
        cond=False
    return cond

def distribPub_Autor(lista,autor):
    pub_autor_ano={}
    for dic in lista:
        if "authors" in dic:
            for nome in dic["authors"]:
                if nome["name"]== autor:
                    if "publish_date" in dic:
                        if dic["publish_date"][:4] in pub_autor_ano:
                            pub_autor_ano[dic["publish_date"][:4]]=pub_autor_ano[dic["publish_date"][:4]]+1
                        else:
                            pub_autor_ano[dic["publish_date"][:4]]=1 
    dist=sorted(pub_autor_ano.items(), key=Ordena_Ano_Mes)  
    return distribGrafico_Autor(dict(dist))

def distribGrafico_Palavras_Freq(d):
    valores=list(d.values())
    labels=list(d.keys())
    cores_nomeadas=list(x for x in mcolors.CSS4_COLORS.keys() if x not in ("white", "whitesmoke", "snow", "ligthyellow", "ligthblue", "ligthgreen"))
    random.shuffle(cores_nomeadas)
    cores_personalizadas=cores_nomeadas[:len(labels)]
    plt.figure(figsize=(9,9))
    plt.bar(labels, valores, color=cores_personalizadas)
    plt.title('Distribuição de das Top 20 Palavras-chave')
    plt.xticks(rotation=20, ha='right', fontsize=7)
    plt.show()

def distribPalavras_Freq(lista):
    pub_palavras={}
    for dic in lista:
        if "keywords" in dic:
            palavra_chave = dic["keywords"].split(", ")
            for palavra in palavra_chave:
                if palavra in pub_palavras:
                    pub_palavras[palavra]=pub_palavras[palavra]+1
                else:
                    pub_palavras[palavra]=1 
    dist=sorted(pub_palavras.items(), key=OrdenaAutores, reverse=True)[:21]  
    return distribGrafico_Palavras_Freq(dict(dist))

def distribGrafico_Palavras_Freq_Ano(d, ano):
    valores=list(d.values())
    labels=list(d.keys())
    if valores!=[] and labels!=[]:
        cond=True
        cores_nomeadas=list(x for x in mcolors.CSS4_COLORS.keys() if x not in ("white", "whitesmoke", "snow", "ligthyellow", "ligthblue", "ligthgreen"))
        random.shuffle(cores_nomeadas)
        cores_personalizadas=cores_nomeadas[:len(labels)]
        plt.figure(figsize=(9,9))
        plt.bar(labels, valores, color=cores_personalizadas)
        plt.title(f'Distribuição de das Top 20 Palavras-chave no Ano {ano} ')
        plt.xticks(rotation=16, ha='right', fontsize=7)
        plt.show()
    else:
        cond=False
    return cond

def distribPalavras_Freq_Ano(lista, ano):
    pub_palavras_ano={}
    for dic in lista:
        if "publish_date" in dic:
            if dic["publish_date"][:4]==ano:
                if "keywords" in dic:
                    palavra_chave = dic["keywords"].split(", ")
                    for palavra in palavra_chave:
                        if palavra in pub_palavras_ano:
                            pub_palavras_ano[palavra]=pub_palavras_ano[palavra]+1
                        else:
                            pub_palavras_ano[palavra]=1 
    dist=sorted(pub_palavras_ano.items(), key=OrdenaAutores, reverse=True)[:21]  
    return distribGrafico_Palavras_Freq_Ano(dict(dist), ano)