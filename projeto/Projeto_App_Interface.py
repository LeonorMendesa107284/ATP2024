import Projeto
import FreeSimpleGUI as sg
    
sg.theme("NeutralBlue")
a=0
layout = [
    [sg.Column([[sg.Text("-OPÇÕES DE MENU-", font=("Calibri", 17))]], justification="center")],
    [sg.Text("Introduza a opção:"), sg.InputText()],
    [sg.Text("1 - Carregar Ata Médica")],
    [sg.Text("2 - Guardar Ata Médica")],
    [sg.Text("3 - Inserir Registo")],
    [sg.Text("4 - Apagar Registo por Título")],
    [sg.Text("5 - Consultar Registo")],
    [sg.Text("6 - Listar Autores")],
    [sg.Text("7 - Atualização dos Dados de uma Publicação")],
    [sg.Text("8 - Análise de Publicações")],
    [sg.Text("9 - Estatísticas")],
    [sg.Button("Enviar"), sg.Button("Sair")]
]


def criar_layout_1():
    return [
        [sg.Text("Introduza o nome do ficheiro:"), sg.InputText(key='-FICHEIRO-')],
        [sg.Button("Ok"), sg.Button("Sair")]
    ]

def criar_layout_2():
    return [
        [sg.Text("Introduza o nome do ficheiro onde pretende guardar a base de dados:"), sg.InputText(key='-FICHEIRO-')],
        [sg.Button("Ok"), sg.Button("Sair")]
    ]

def criar_layout_3():
    return [
        [sg.Text("Introduza o abstract:"), sg.Input(key='-ABSTRACT-')],
        [sg.Text("Introduza palavra(s) chave(s):"), sg.Input(key='-KEYWORD-')],
        [sg.Text("Introduza o DOI:"), sg.Input(key='-DOI-')],
        [sg.Text("Introduza o link do pdf:"), sg.Input(key='-PDF-')],
        [sg.Text("Introduza a data (ano-mês-dia):"), sg.Input(key='-DATE-')],
        [sg.Text("Introduza o título do registo:"), sg.Input(key='-TITLE-')],
        [sg.Text("Introduza o url:"), sg.Input(key='-URL-')],
        [sg.Button("Ok"), sg.Button("Sair")]
    ]

def criar_layout_3_autores():
    return [
        [sg.Text("Quantos autores tem este registo?"), sg.Input(key='-AUTHORS-')],
        [sg.Button("Ok"), sg.Button("Sair")]
    ]

def criar_layout_4():
    return [
        [sg.Text("Introduza o título do registo que pretende apagar:"), sg.InputText(key='-DELETE-TITLE-')],
        [sg.Button("Ok"), sg.Button("Sair")]
    ]

def criar_layout_5():
    return [
        [sg.Text("Consultar Registo", font=("Calibri", 17), justification="center")],
        [sg.Text("Escolha o critério de consulta:")],
        [sg.Button("Consultar por Título", key="-CONSTIT-", size=(25, 1))],
        [sg.Button("Consultar por Autor", key="-CONSAUT-", size=(25, 1))],
        [sg.Button("Consultar por Data", key="-CONSDATE-", size=(25, 1))],
        [sg.Button("Consultar por Afilição", key="-CONSAF-", size=(25, 1))],
        [sg.Button("Consultar por Palavra-chave", key="-CONSPAL-", size=(25, 1))],
        [sg.Button("Fechar")]
    ]

def consultar_Título(ata_med):
    layout_consulta = [
        [sg.Text("Consultar Registo por Título", font=("Calibri", 17), justification="center")],
        [sg.Text("Introduza o Título:"), sg.Input(key='-TIT-')],
        [sg.Button("Ok"), sg.Button("Sair")]
    ]

    window_consulta = sg.Window("Consultar Registo por Título", layout_consulta, font=('Calibri', 15))
    stop_consulta = False

    while not stop_consulta:
        event_consulta, values_consulta = window_consulta.read()
        if event_consulta in ["Sair", sg.WIN_CLOSED]:
            stop_consulta = True
        else:
            valor = values_consulta["-TIT-"]
            if not valor:
                sg.popup_error(f"O campo do título não pode estar vazio!")
            else:
                try:
                    res = Projeto.consultarTitulo_data(ata_med, valor, "consultarTitulo_data.txt")
                    if res:
                        sg.popup(f"O resultado foi salvo no ficheiro: consultarTitulo_data.txt", font=('Calibri', 15))
                        ficheiro=[
                            [sg.Text("Deseja abrir/consultar esse ficheiro?")],  
                            [sg.Button("Sim"), sg.Button("Não")]
                        ]
                        window_ficheiro = sg.Window("Consultar Registo por Título", ficheiro, font=('Calibri', 15))
                        stop_f = False

                        while not stop_f:
                            event_f, _= window_ficheiro.read()
                            if event_f in ["Não", sg.WIN_CLOSED]:
                                stop_f = True
                            else:
                                window_ficheiro.close()
                                with open("./consultarTitulo_data.txt", 'r', encoding="utf-8") as f:
                                    conteudo = f.read()
                                sg.popup_scrolled(f"Conteúdo do ficheiro: consultarTitulo_data.txt\n\n{conteudo}", title="Resultado da Consulta", size=(90, 30))
                        window_ficheiro.close()
                    else:
                        sg.popup(f"Não foram encontrados registos com esse título.", title="Erro", font=('Calibri', 15))
                except Exception as e:
                    sg.popup_error(f"Erro ao consultar Título: {str(e)}")
                stop_consulta = True
    window_consulta.close()

def consulta():
    return [
        [sg.Text("Consultar de Forma Ordenada", font=("Calibri", 17), justification="center")],
        [sg.Button("Por Ordem Alfabética", size=(27, 1))],
        [sg.Button("Por Data", size=(27, 1))],
        [sg.Button("Ok"), sg.Button("Sair")]
    ]

def consultar_Af_Alf(ata_med):
    layout_consulta = [
        [sg.Text("Consultar Registo por Afiliação Ordenada Alfabeticamente", font=("Calibri", 17), justification="center")],
        [sg.Text("Introduza a Afiliação:"), sg.Input(key='-AFI-')],
        [sg.Button("Ok"), sg.Button("Sair")]
    ]

    window_consulta = sg.Window("Consultar Registo por Afiliação Ordenada Alfabeticamente", layout_consulta, font=('Calibri', 15))
    stop_consulta = False

    while not stop_consulta:
        event_consulta, values_consulta = window_consulta.read()
        if event_consulta in ["Sair", sg.WIN_CLOSED]:
            stop_consulta = True
        else:
            valor = values_consulta["-AFI-"]
            if not valor:
                sg.popup_error(f"O campo da Afiliação não pode estar vazio!")
            else:
                try:
                    res = Projeto.consultaAfiliacao_Tit(ata_med, valor, "consultaAfiliacao_Tit.txt")
                    if res:
                        sg.popup(f"O resultado foi salvo no ficheiro: consultaAfiliacao_Tit.txt", font=('Calibri', 15))
                        ficheiro=[
                            [sg.Text("Deseja abrir/consultar esse ficheiro?")],  
                            [sg.Button("Sim"), sg.Button("Não")]
                        ]
                        window_ficheiro = sg.Window("Consultar Registo por Afiliação", ficheiro, font=('Calibri', 15))
                        stop_f = False

                        while not stop_f:
                            event_f, _ = window_ficheiro.read()
                            if event_f in ["Não", sg.WIN_CLOSED]:
                                stop_f = True
                            else:
                                window_ficheiro.close()
                                with open("./consultaAfiliacao_Tit.txt", 'r', encoding="utf-8") as f:
                                    conteudo = f.read()
                                sg.popup_scrolled(f"Conteúdo do ficheiro: consultaAfiliacao_Tit.txt\n\n{conteudo}", title="Resultado da Consulta", size=(90, 30))
                        window_ficheiro.close()
                    else:
                        sg.popup(f"Não foram encontrados registos com essa Afiliação.", title="Erro", font=('Calibri', 15))
                except Exception as e:
                    sg.popup_error(f"Erro ao consultar Afiliação: {str(e)}")
                stop_consulta = True
    window_consulta.close()

def consultar_Af_Data(ata_med):
    layout_consulta = [
        [sg.Text("Consultar Registo por Afiliação Ordenada Cronológicamente", font=("Calibri", 17), justification="center")],
        [sg.Text("Introduza a Afiliação:"), sg.Input(key='-AFI-')],
        [sg.Button("Ok"), sg.Button("Sair")]
    ]

    window_consulta = sg.Window("Consultar Registo por Afiliação Ordenada Cronológicamente", layout_consulta, font=('Calibri', 15))
    stop_consulta = False

    while not stop_consulta:
        event_consulta, values_consulta = window_consulta.read()
        if event_consulta in ["Sair", sg.WIN_CLOSED]:
            stop_consulta = True
        else:
            valor = values_consulta["-AFI-"]
            if not valor:
                sg.popup_error(f"O campo da Afiliação não pode estar vazio!")
            else:
                try:
                    res = Projeto.consultaAfiliacao_Data(ata_med, valor, "consultaAfiliacao_Data.txt")
                    if res:
                        sg.popup(f"O resultado foi salvo no ficheiro: consultaAfiliacao_Data.txt", font=('Calibri', 15))
                        ficheiro=[
                            [sg.Text("Deseja abrir/consultar esse ficheiro?")],  
                            [sg.Button("Sim"), sg.Button("Não")]
                        ]
                        window_ficheiro = sg.Window("Consultar Registo por Afiliação", ficheiro, font=('Calibri', 15))
                        stop_f = False

                        while not stop_f:
                            event_f, _ = window_ficheiro.read()
                            if event_f in ["Não", sg.WIN_CLOSED]:
                                stop_f = True
                            else:
                                window_ficheiro.close()
                                with open("./consultaAfiliacao_Data.txt", 'r', encoding="utf-8") as f:
                                    conteudo = f.read()
                                sg.popup_scrolled(f"Conteúdo do ficheiro: consultaAfiliacao_Data.txt\n\n{conteudo}", title="Resultado da Consulta", size=(90, 30))
                        window_ficheiro.close()
                    else:
                        sg.popup(f"Não foram encontrados registos com essa Afiliação.", title="Erro", font=('Calibri', 15))
                except Exception as e:
                    sg.popup_error(f"Erro ao consultar Afiliação: {str(e)}")
                stop_consulta = True
    window_consulta.close()

def consultar_Autor_Alf(ata_med):
    layout_consulta = [
        [sg.Text("Consultar Registo por Autor Ordenada Alfabeticamente", font=("Calibri", 17), justification="center")],
        [sg.Text("Introduza o Autor:"), sg.Input(key='-AUTOR-')],
        [sg.Button("Ok"), sg.Button("Sair")]
    ]

    window_consulta = sg.Window("Consultar Registo por Autor Ordenada Alfabeticamente", layout_consulta, font=('Calibri', 15))
    stop_consulta = False

    while not stop_consulta:
        event_consulta, values_consulta = window_consulta.read()
        if event_consulta in ["Sair", sg.WIN_CLOSED]:
            stop_consulta = True
        else:
            valor = values_consulta["-AUTOR-"]
            if not valor:
                sg.popup_error(f"O campo da Autor não pode estar vazio!")
            else:
                try:
                    res = Projeto.consultaAutor_tit(ata_med, valor, "consultaAutor_tit.txt")
                    if res:
                        sg.popup(f"O resultado foi salvo no ficheiro: consultaAutor_tit.txt", font=('Calibri', 15))
                        ficheiro=[
                            [sg.Text("Deseja abrir/consultar esse ficheiro?")],  
                            [sg.Button("Sim"), sg.Button("Não")]
                        ]
                        window_ficheiro = sg.Window("Consultar Registo por Autor", ficheiro, font=('Calibri', 15))
                        stop_f = False

                        while not stop_f:
                            event_f, _ = window_ficheiro.read()
                            if event_f in ["Não", sg.WIN_CLOSED]:
                                stop_f = True
                            else:
                                window_ficheiro.close()
                                with open("./consultaAutor_tit.txt", 'r', encoding="utf-8") as f:
                                    conteudo = f.read()
                                sg.popup_scrolled(f"Conteúdo do ficheiro: consultaAutor_tit.txt\n\n{conteudo}", title="Resultado da Consulta", size=(90, 30))
                        window_ficheiro.close()
                    else:
                        sg.popup(f"Não foram encontrados registos com esse Autor.", title="Erro", font=('Calibri', 15))
                except Exception as e:
                    sg.popup_error(f"Erro ao consultar Autor: {str(e)}")
                stop_consulta = True
    window_consulta.close()

def consultar_Autor_Data(ata_med):
    layout_consulta = [
        [sg.Text("Consultar Registo por Autor Ordenada Cronológicamente", font=("Calibri", 17), justification="center")],
        [sg.Text("Introduza o Autor:"), sg.Input(key='-AUTOR-')],
        [sg.Button("Ok"), sg.Button("Sair")]
    ]
    window_consulta = sg.Window("Consultar Registo por Autor Ordenada Cronológicamente", layout_consulta, font=('Calibri', 15))
    stop_consulta = False
    while not stop_consulta:
        event_consulta, values_consulta = window_consulta.read()
        if event_consulta in ["Sair", sg.WIN_CLOSED]:
            stop_consulta = True
        else:
            valor = values_consulta["-AUTOR-"]
            if not valor:
                sg.popup_error(f"O campo da Autor não pode estar vazio!")
            else:
                try:
                    res = Projeto.consultaAutor_data(ata_med, valor, "consultaAutor_data.txt")
                    if res:
                        sg.popup(f"O resultado foi salvo no ficheiro: consultaAutor_data.txt", font=('Calibri', 15))
                        ficheiro=[
                            [sg.Text("Deseja abrir/consultar esse ficheiro?")],  
                            [sg.Button("Sim"), sg.Button("Não")]
                        ]
                        window_ficheiro = sg.Window("Consultar Registo por Autor", ficheiro, font=('Calibri', 15))
                        stop_f = False
                        while not stop_f:
                            event_f, _ = window_ficheiro.read()
                            if event_f in ["Não", sg.WIN_CLOSED]:
                                stop_f = True
                            else:
                                window_ficheiro.close()
                                with open("./consultaAutor_data.txt", 'r', encoding="utf-8") as f:
                                    conteudo = f.read()
                                sg.popup_scrolled(f"Conteúdo do ficheiro: consultaAutor_data.txt\n\n{conteudo}", title="Resultado da Consulta", size=(90, 30))
                        window_ficheiro.close()
                    else:
                        sg.popup(f"Não foram encontrados registos com esse Autor.", title="Erro", font=('Calibri', 15))
                except Exception as e:
                    sg.popup_error(f"Erro ao consultar Autor: {str(e)}")
                stop_consulta = True
    window_consulta.close()

def consultar_Data(ata_med):
    layout_consulta_data = [
        [sg.Text("Consultar Registo por Data", font=("Calibri", 17), justification="center")],
        [sg.Text("Introduza a Data (AAAA-MM-DD):"), sg.Input(key='-DATA-')],
        [sg.Button("Ok"), sg.Button("Sair")]
    ]

    window_consulta_data = sg.Window("Consultar Registo por Data", layout_consulta_data, font=('Calibri', 15))
    stop_consulta_d = False

    while not stop_consulta_d:
        event_consulta_d, values_consulta_d = window_consulta_data.read()
        if event_consulta_d in ["Sair", sg.WIN_CLOSED]:
            stop_consulta_d = True
        else:
            valor = values_consulta_d["-DATA-"]
            if not valor:
                sg.popup_error(f"O campo da data não pode estar vazio!")
            else:
                try:
                    res = Projeto.consultarData(ata_med, valor, "consultarData.txt")
                    if res:
                        sg.popup(f"O resultado foi salvo no ficheiro: consultarData.txt", font=('Calibri', 15))
                        ficheiro=[
                            [sg.Text("Deseja abrir/consultar esse ficheiro?")],  
                            [sg.Button("Sim"), sg.Button("Não")]
                        ]
                        window_ficheiro = sg.Window("Consultar Registo por Data", ficheiro, font=('Calibri', 15))
                        stop_f = False
                        while not stop_f:
                            event_f, _ = window_ficheiro.read()
                            if event_f in ["Não", sg.WIN_CLOSED]:
                                stop_f = True
                            else:
                                window_ficheiro.close()
                                with open("./consultarData.txt", 'r', encoding= "utf-8") as f:
                                    conteudo = f.read()
                                sg.popup_scrolled(f"Conteúdo do ficheiro: consultarData.txt\n\n{conteudo}", title="Resultado da Consulta", size=(90, 30))
                        window_ficheiro.close()
                    else:
                        sg.popup(f"Não foram encontrados registos com essa data.", title="Erro", font=('Calibri', 15))
                except Exception as e:
                    sg.popup_error(f"Erro ao consultar Data: {str(e)}")
                stop_consulta_d = True
    window_consulta_data.close()


def consultar_Pal_data(ata_med):
    layout_consulta_pal_d = [
        [sg.Text("Consultar Registo por Palavra-Chave", font=("Calibri", 17), justification="center")],
        [sg.Text("Introduza a Palavra-Chave:"), sg.Input(key='-PAL-')],
        [sg.Button("Ok"), sg.Button("Sair")]
    ]

    window_consulta_pal_d = sg.Window("Consultar Registo por Palavra-Chave", layout_consulta_pal_d, font=('Calibri', 15))
    stop_consulta_pd = False

    while not stop_consulta_pd:
        event_consulta_pd, values_consulta_pd = window_consulta_pal_d.read()
        if event_consulta_pd in ["Sair", sg.WIN_CLOSED]:
            stop_consulta_pd = True
        else:
            valor = values_consulta_pd["-PAL-"]
            if not valor:
                sg.popup_error(f"O campo da palavra-chave não pode estar vazio!")
            else:
                try:
                    res = Projeto.consultarPalavra_Chave_Data(ata_med, valor, "consultarPalavra_Chave_Data.txt")
                    if res:
                        sg.popup(f"O resultado foi salvo no ficheiro: consultarPalavra_Chave_Data.txt", font=('Calibri', 15))
                        ficheiro=[
                            [sg.Text("Deseja abrir/consultar esse ficheiro?")],  
                            [sg.Button("Sim"), sg.Button("Não")]
                        ]
                        window_ficheiro = sg.Window("Consultar Registo por Palavras-Chave Ordenadas Cronologicamente", ficheiro, font=('Calibri', 15))
                        stop_f = False

                        while not stop_f:
                            event_f, _ = window_ficheiro.read()
                            if event_f in ["Não", sg.WIN_CLOSED]:
                                stop_f = True
                            else:
                                window_ficheiro.close()
                                with open("./consultarPalavra_Chave_Data.txt", 'r', encoding= "utf-8") as f:
                                    conteudo = f.read()
                                sg.popup_scrolled(f"Conteúdo do ficheiro: consultarPalavra_Chave_Data.txt\n\n{conteudo}", title="Resultado da Consulta", size=(90, 30))
                        window_ficheiro.close()
                    else:
                        sg.popup(f"Não foram encontrados registos com essa palavra-chave.", title="Erro", font=('Calibri', 15))
                except Exception as e:
                    sg.popup_error(f"Erro ao consultar Palavra-Chave: {str(e)}")
                stop_consulta_pd = True
    window_consulta_pal_d.close()

def consultar_Pal_Alf(ata_med):
    layout_consulta_pal_alf = [
        [sg.Text("Consultar Registo por Palavra-Chave", font=("Calibri", 17), justification="center")],
        [sg.Text("Introduza a Palavra-Chave:"), sg.Input(key='-PAL2-')],
        [sg.Button("Ok"), sg.Button("Sair")]
    ]

    window_consulta_pal_alf = sg.Window("Consultar Registo por Palavra-Chave", layout_consulta_pal_alf, font=('Calibri', 15))
    stop_consulta_pa = False

    while not stop_consulta_pa:
        event_consulta_pa, values_consulta_pa = window_consulta_pal_alf.read()
        if event_consulta_pa in ["Sair", sg.WIN_CLOSED]:
            stop_consulta_pa = True
        else:
            valor = values_consulta_pa["-PAL2-"]
            if not valor:
                sg.popup_error(f"O campo da palavra-chave não pode estar vazio!")
            else:
                try:
                    res = Projeto.consultarPalavra_Chave_Tit(ata_med, valor, "consultarPalavra_Chave_Tit.txt")
                    if res:
                        sg.popup(f"O resultado foi salvo no ficheiro: consultarPalavra_Chave_Tit.txt", font=('Calibri', 15))
                        ficheiro=[
                            [sg.Text("Deseja abrir/consultar esse ficheiro?")],  
                            [sg.Button("Sim"), sg.Button("Não")]
                        ]
                        window_ficheiro = sg.Window("Consultar Registo por Palavras-Chave Ordenadas Alfabeticamente", ficheiro, font=('Calibri', 15))
                        stop_f = False

                        while not stop_f:
                            event_f, _ = window_ficheiro.read()
                            if event_f in ["Não", sg.WIN_CLOSED]:
                                stop_f = True
                            else:
                                window_ficheiro.close()
                                with open("./consultarPalavra_Chave_Tit.txt", 'r', encoding= "utf-8") as f:
                                    conteudo = f.read()
                                sg.popup_scrolled(f"Conteúdo do ficheiro: consultarPalavra_Chave_Tit.txt\n\n{conteudo}", title="Resultado da Consulta", size=(90, 30))
                        window_ficheiro.close()
                    else:
                        sg.popup(f"Não foram encontrados registos com essa palavra-chave.", title="Erro", font=('Calibri', 15))
                except Exception as e:
                    sg.popup_error(f"Erro ao consultar Palavra-Chave: {str(e)}")
                stop_consulta_pa = True
    window_consulta_pal_alf.close()

def listar():
    return [
        [sg.Text("Listar Autores", font=("Calibri", 17), justification="center")],
        [sg.Button("Por Ordem Alfabética", size=(27, 1))],
        [sg.Button("Por Frequência", size=(27, 1))],
        [sg.Button("Ok"), sg.Button("Sair")]
    ]

def Aceder_artigos():
    layout_autor=[
        [sg.Text("Introduza o autor que pretende consultar:", font=("Calibri", 17), justification="center"), sg.InputText(key='-AUTOR-')],
        [sg.Button("Consultar"), sg.Button("Sair")]
    ]
    window_autor = sg.Window("Autor a Consultar", layout_autor, font=('Calibri', 15))
    stop_a = False
    while not stop_a:
        event_a, values_a = window_autor.read()
        if event_a in ["Sair", sg.WIN_CLOSED]:
            stop_a = True
        else:
            autor = values_a["-AUTOR-"]
            if not autor:
                sg.popup_error(f"O campo do Autor não pode estar vazio!")
            else:
                res = Projeto.acederRes_Inter(ata_med, autor)
                if not res:
                    sg.popup_error("Nenhum artigo encontrado para este autor.")
                else:
                    window_autor.close()
                    layout_titulos = [
                        [sg.Text("Selecione um título para consultar mais informações:", font=("Calibri", 17))],
                        [sg.Listbox(values=res, size=(80, 10), horizontal_scroll=True, key='-TITULO-', enable_events=True)],
                        [sg.Button("Aceder ao URL"), sg.Button("Voltar")]
                    ]
                    window_titulos = sg.Window("Artigos do Autor", layout_titulos, font=('Calibri', 15))
                    stop_t=False
                    while not stop_t:
                        event_t, values_t = window_titulos.read()
                        if event_t in ["Voltar", sg.WIN_CLOSED]:
                            stop_t=True
                        elif event_t == "Aceder ao URL":
                            titulo_selecionado = values_t['-TITULO-']
                            url = Projeto.acederURL_Inter(ata_med, titulo_selecionado[0])
                            if url:
                                layout_url = [
                                    [sg.Text("URL do artigo:", font=("Calibri", 17))],
                                    [sg.Text(url[0], font=("Calibri", 15), text_color="blue", enable_events=True, key='-URL-')],
                                    [sg.Button("Fechar")]
                                ]
                                window_url = sg.Window("URL", layout_url, font=('Calibri', 15))
                                stop_u = False
                                while not stop_u:
                                    event_u, values_u = window_url.read()
                                    if event_u in ["Fechar", sg.WIN_CLOSED]:
                                        stop_u = True
                                    elif event_u == '-URL-':
                                        import webbrowser
                                        webbrowser.open(url[0])
                                window_url.close()
                            else:
                                sg.popup_error("Nenhum URL disponível para o artigo selecionado.")
                    window_titulos.close()
    window_autor.close()

def criar_layout_7():
    layout_requesito=[
        [sg.Text("Introduza o título do registo que pretende atualizar:"), sg.Input(key='-TITLE-')],
        [sg.Text("Caso não tenha título, introduza o DOI:"), sg.Input(key='-DOI-')],
        [sg.Button("Ok"), sg.Button("Sair")]
    ]
    window_requesitos = sg.Window("Registo a Atualizar", layout_requesito, font=('Calibri', 15))
    stop_req = False
    while not stop_req:
        event_req, values_req = window_requesitos.read()
        if event_req in ["Sair", sg.WIN_CLOSED]:
            stop_req = True
        else:
            titulo= values_req["-TITLE-"]
            doi=values_req["-DOI-"]
            window_requesitos.close()
            if (titulo!="" and titulo!=None) or (doi!="" and doi !=None):
                alteracoes= [
                        [sg.Text("Introduza o abstract:"), sg.Input(key='-ABSTRACT-')],
                        [sg.Text("Introduza palavra(s) chave(s):"), sg.Input(key='-KEYWORD-')],
                        [sg.Text("Introduza a data (ano-mês-dia):"), sg.Input(key='-DATE-')],
                        [sg.Button("Ok"), sg.Button("Sair")]
                    ]
                window_alteracoes = sg.Window("Atualizações", alteracoes, font=('Calibri', 15)) 
                stop_alter = False
                while not stop_alter:
                    event_alter, values_alter = window_alteracoes.read()
                    if event_alter in ["Sair", sg.WIN_CLOSED]:
                        stop_alter = True
                    else:
                        abstract=values_alter["-ABSTRACT-"]
                        keyword=values_alter["-KEYWORD-"]
                        date=values_alter["-DATE-"]
                        stop_alter=True
                    window_alteracoes.close()
                nome_autor=[]
                afiliacao=[]
                layout_3_autores= criar_layout_3_autores()
                window_layout_3_autores = sg.Window("Quantidade de Autores", layout_3_autores, font=('Calibri', 15))
                stop_3a = False
                while not stop_3a:
                    event_3a, values_3a = window_layout_3_autores.read()
                    if event_3a in ["Sair", sg.WIN_CLOSED]:
                        stop_3a = True
                    else:
                        try:
                            numero=int(values_3a["-AUTHORS-"])
                            window_layout_3_autores.close()
                            i = 1
                            while i<=numero:
                                layout_3_info = [
                                            [sg.Text(f"Introduza o {i}º nome:"), sg.Input(key = '-NOME-')],
                                            [sg.Text(f"Introduza a {i}ª afiliação:"), sg.Input(key = '-AFFILIATION-')],
                                            [sg.Button("Ok"), sg.Button("Sair")]
                                ]
                                window_layout_3_info = sg.Window("Informações sobre Autores", layout_3_info, font=('Calibri', 15))
                                i=i+1
                                stop_3i = False
                                while not stop_3i:
                                    event_3i, values_3i = window_layout_3_info.read()
                                    if event_3i in ["Sair", sg.WIN_CLOSED]:
                                        stop_3i = True
                                    else:
                                        nome_autor.append(values_3i["-NOME-"])          
                                        afiliacao.append(values_3i["-AFFILIATION-"])
                                        stop_3i = True
                                window_layout_3_info.close()
                        except Exception as e:
                            sg.popup_error(f"Erro: {str(e)}")
                window_layout_3_autores.close()
                dic_autor=[]
                a1=0
                for n in nome_autor:
                    a=afiliacao[a1]
                    if a!="":
                        dic_autor.append({"name": n, "affiliation": a})
                    else:
                        dic_autor.append({"name": n})
                    a1=a1+1
                if titulo!="" and titulo!=None:
                    res=Projeto.atual_reg(ata_med, titulo, "" , date, abstract,keyword, dic_autor)
                elif doi!="" and doi !=None:
                    res=Projeto.atual_reg(ata_med, "", doi, date, abstract,keyword, dic_autor)
                if res==True:
                    sg.popup("O seu registo foi atualizado com sucesso!", title="Sucesso", font=('Calibri', 15))
                else:
                    sg.popup("Não foi possivel encontrar nenhum registo com esse título/doi.", title="Atenção", font=('Calibri', 15))
            else:
                sg.popup("Tem de preencher o campo do título! Só caso não tenha título preencha o campo do doi.")
    window_requesitos.close()       

def criar_layout_8():
    return [
        [sg.Text("Análise de Publicações por Palavras-chave:", font=("Calibri", 17), justification="center")],
        [sg.Button("Ordenada Alfabeticamente", key="-AALF-", size=(27, 1))],
        [sg.Button("Ordenada pela Frequência", key="-AFREQ-", size=(27, 1))],
        [sg.Button("Fechar")]
    ]

def criar_layout_9():
    return [
        [sg.Text("Distribuições de Publicações", font=("Calibri", 17), justification="center")],
        [sg.Button("Por Ano", key="-DISTANO-", size=(30, 2))],
        [sg.Button("Por Mês de um Determinado Ano", key="-DISTMES-", size=(30, 2))],
        [sg.Button("Top 20 Autores", key="-DISTAUT20-", size=(30, 2))],
        [sg.Button("De um Determinado Autor por Anos", key="-DISTAUTANO-", size=(30, 2))],
        [sg.Button("Top 20 Palavras-chave", key="-DISTPAL20-", size=(30, 2))],
        [sg.Button("Frequência de Palavras-chave de um Determinado Ano", key="-DISTPALANO-", size=(30, 2))],
        [sg.Button("Fechar")]
    ]

window = sg.Window("Opções de menu", layout, font=('Calibri', 15)) 
stop = False
while not stop:
    event, values = window.read()
    if event in ["Sair", sg.WIN_CLOSED]:
        sg.popup("A aplicação vai encerrar. Volte sempre!", title="Encerrar", font=('Calibri', 15))
        stop = True
    else:
        opcao=values[0]
        if opcao == "1":
            layout_1 = criar_layout_1()
            window_layout_1 = sg.Window("Carregar Ata Médica", layout_1, font=('Calibri', 15)) 
            stop1 = False
            while not stop1:
                event_1, values_1 = window_layout_1.read() 
                if event_1 in ["Sair", sg.WIN_CLOSED]: 
                    stop1 = True
                else:
                    fnome=values_1["-FICHEIRO-"]
                    if Projeto.verificar_arquivo_existente(fnome):
                        if ".json" in fnome:
                            ata_med = Projeto.carregarAta(fnome)
                            sg.popup("O seu ficheiro foi carregado com sucesso!", title="Sucesso", font=('Calibri', 15))
                            a=1
                        else:
                            sg.popup("O seu ficheiro não foi carregado! Só são suportados ficheiros em .json", title="Erro", font=('Calibri', 15))
                    else:
                        sg.popup(f"O arquivo '{fnome}' não foi encontrado na pasta onde se encontra." , title="Atenção", font=('Calibri', 15))
            window_layout_1.close()
        elif opcao == "2":
            if a==0:
                sg.popup("Ainda não usou a função carregar ficheiro. Para que qualquer opção funcione tem que utilizar primeiro a opção 1.")
            else:
                layout_2 = criar_layout_2()
                window_layout_2 = sg.Window("Guardar Base de Dados", layout_2, font=('Calibri', 15)) 
                stop2 = False
                while not stop2:
                    event_2, values_2 = window_layout_2.read()
                    if event_2 in ["Sair", sg.WIN_CLOSED]:
                        stop2 = True
                    else:
                        fnome=values_2["-FICHEIRO-"]
                        if ".json" in fnome:
                            Projeto.guardarATA(fnome,ata_med)
                            sg.popup("A sua base de dados foi guardada com sucesso!", title="Sucesso", font=('Calibri', 15))
                        else:
                            sg.popup("A sua base de dados não foi guardada! Só são suportados ficheiros em .json" , title="Erro", font=('Calibri', 15))
                window_layout_2.close()
        elif opcao == "3":                  
            if a == 0:
                sg.popup("Ainda não usou a função carregar ficheiro. Para que qualquer opção funcione tem que utilizar primeiro a opção 1.",title="Atenção")
            else:
                layout_3 = criar_layout_3()
                window_layout_3 = sg.Window("Opções de menu", layout_3, font=('Calibri', 15)) 
                stop3 = False
                while not stop3:
                    event_3, values_3 = window_layout_3.read()
                    if event_3 in ["Sair", sg.WIN_CLOSED]:
                        stop3 = True
                    else:
                        registo={}
                        abstract=values_3["-ABSTRACT-"]
                        if abstract:
                            registo["abstract"] = abstract
                        keyword=values_3["-KEYWORD-"]
                        if keyword:
                            registo["keywords"] = keyword
                        nome_autor=[]
                        afiliacao=[]
                        orcid=[]
                        layout_3_autores= criar_layout_3_autores()
                        window_layout_3_autores = sg.Window("Quantidade de Autores", layout_3_autores, font=('Calibri', 15))
                        stop_3a = False
                        while not stop_3a:
                            event_3a, values_3a = window_layout_3_autores.read()
                            if event_3a in ["Sair", sg.WIN_CLOSED]:
                                stop_3a = True
                            else:
                                try:
                                    numero=int(values_3a["-AUTHORS-"])
                                    window_layout_3_autores.close()
                                    i = 1
                                    while i<=numero:
                                        layout_3_info = [
                                                    [sg.Text(f"Introduza o {i}º nome:"), sg.Input(key = '-NOME-')],
                                                    [sg.Text(f"Introduza a {i}ª afiliação:"), sg.Input(key = '-AFFILIATION-')],
                                                    [sg.Text(f"Introduza o {i}º orcid:"), sg.Input(key = '-ORCID-')],
                                                    [sg.Button("Ok"), sg.Button("Sair")]
                                        ]
                                        window_layout_3_info = sg.Window("Informações sobre Autores", layout_3_info, font=('Calibri', 15))
                                        i=i+1
                                        stop_3i = False
                                        while not stop_3i:
                                            event_3i, values_3i = window_layout_3_info.read()
                                            if event_3i in ["Sair", sg.WIN_CLOSED]:
                                                stop_3i = True
                                            else:
                                                nome_autor.append(values_3i["-NOME-"])          
                                                afiliacao.append(values_3i["-AFFILIATION-"])
                                                orcid.append(values_3i["-ORCID-"])
                                                stop_3i = True
                                        window_layout_3_info.close()
                                except Exception as e:
                                    sg.popup_error(f"Erro: {str(e)}")  
                        window_layout_3_autores.close()
                        dic_autor=[]
                        a1=0
                        o1=0
                        for n in nome_autor:
                            if n!="":
                                a=afiliacao[a1]
                                if a!="":
                                    o=orcid[o1]
                                    if o!="":
                                        dic_autor.append({"name": n, "affiliation": a, "orcid": o})
                                    else:
                                        dic_autor.append({"name": n, "affiliation": a})
                                else:
                                    o=orcid[o1]
                                    if o!="":
                                        dic_autor.append({"name": n, "orcid": o})
                                    else:
                                        dic_autor.append({"name": n})
                                a1=a1+1
                                o1=o1+1
                        if dic_autor:
                            registo["authors"] = dic_autor
                        doi=values_3["-DOI-"]
                        if doi:
                            registo["doi"] = doi
                        pdf=values_3["-PDF-"]
                        if pdf:
                            registo["pdf"] = pdf
                        date=values_3["-DATE-"]
                        if date:
                            registo["publish_date"] = date
                        titulo=values_3["-TITLE-"]
                        if titulo:
                            registo["title"] = titulo
                        url=values_3["-URL-"]
                        if url:
                            registo["url"] = url
                        stop3=True
                        window_layout_3.close()
                        if registo:
                            Projeto.inserir(ata_med,registo)
                            sg.popup("Registo inserido com sucesso!", title="Sucesso", font=('Calibri', 15))
                        else:
                            sg.popup("Nenhum dado foi inserido, o registo está vazio.", title="Erro", font=('Calibri', 15) )
                window_layout_3.close()
        elif opcao == "4":
            if a==0:
                sg.popup("Ainda não usou a função carregar ficheiro. Para que qualquer opção funcione tem que utilizar primeiro a opção 1.", title="Atenção")
            else:
                layout_4 = criar_layout_4()
                window_layout_4 = sg.Window("Apagar Registo", layout_4, font=('Calibri', 15)) 
                stop4 = False
                while not stop4:
                    event_4, values_4 = window_layout_4.read()
                    if event_4 in ["Sair", sg.WIN_CLOSED]:
                        stop4 = True
                    else:
                        tit=values_4["-DELETE-TITLE-"]
                        resposta=Projeto.apagar(ata_med,tit)
                        if resposta==True:
                            sg.popup("O seu ficheiro foi apagado com sucesso!",title="Sucesso",font=('Calibri', 15))
                        else:
                            sg.popup("Não foi possivel encontrar um registo com esse título!", title="Atenção", font=('Calibri', 15))
                window_layout_4.close()
        elif opcao == "5":
            if a == 0:
                sg.popup("Ainda não usou a função carregar ficheiro. Para que qualquer opção funcione, tem que utilizar primeiro a opção 1.",title="Atenção")
            else:
                layout_5 = criar_layout_5()
                window_layout_5 = sg.Window("Opções de Consulta", layout_5, font=('Calibri', 15))
                stop5 = False
                while not stop5:
                    event_5, _ = window_layout_5.read()
                    if event_5 in ["Fechar", sg.WIN_CLOSED]:
                        stop5 = True
                    elif event_5 == "-CONSTIT-":
                        consultar_Título(ata_med)
                    elif event_5 == "-CONSAUT-":
                        layout_cons= consulta()
                        window_cons = sg.Window("Consultar Registo por Título", layout_cons, font=('Calibri', 15))
                        stop_c = False
                        while not stop_c:
                            event_c, _ = window_cons.read()
                            if event_c in ["Sair", sg.WIN_CLOSED]:
                                stop_c = True
                            else:
                                if event_c=="Por Ordem Alfabética":
                                    window_cons.close()
                                    consultar_Autor_Alf(ata_med)
                                else:
                                    window_cons.close()
                                    consultar_Autor_Data(ata_med)
                        window_cons.close()
                    elif event_5 == "-CONSDATE-":
                        consultar_Data(ata_med)
                    elif event_5 == "-CONSAF-":
                        layout_cons= consulta()
                        window_cons = sg.Window("Consultar Registo por Título", layout_cons, font=('Calibri', 15))
                        stop_c = False
                        while not stop_c:
                            event_c, _ = window_cons.read()
                            if event_c in ["Sair", sg.WIN_CLOSED]:
                                stop_c = True
                            else:
                                if event_c=="Por Ordem Alfabética":
                                    window_cons.close()
                                    consultar_Af_Alf(ata_med)
                                else:
                                    window_cons.close()
                                    consultar_Af_Data(ata_med)
                        window_cons.close()
                    elif event_5 == "-CONSPAL-":
                        layout_cons= consulta()
                        window_cons = sg.Window("Consultar Registo por Palavra-Chave", layout_cons, font=('Calibri', 15))
                        stop_c = False
                        while not stop_c:
                            event_c, _ = window_cons.read()
                            if event_c in ["Sair", sg.WIN_CLOSED]:
                                stop_c = True
                            else:
                                if event_c=="Por Ordem Alfabética":
                                    window_cons.close()
                                    consultar_Pal_Alf(ata_med)
                                else:
                                    window_cons.close()
                                    consultar_Pal_data(ata_med) 
                        window_cons.close()
                window_layout_5.close()
        elif opcao == "6":
            if a == 0:
                sg.popup("Ainda não usou a função carregar ficheiro. Para que qualquer opção funcione, tem que utilizar primeiro a opção 1.",title="Atenção")
            else:
                layout_6 = listar()
                window_layout_6 = sg.Window("Opções de Listagem", layout_6, font=('Calibri', 15))
                stop6 = False
                while not stop6:
                    event_6, _ = window_layout_6.read()
                    if event_6 in ["Sair", sg.WIN_CLOSED]:
                        stop6 = True
                    elif event_6=="Por Ordem Alfabética":
                        listagem = Projeto.listarAutor_Alf_Inter(ata_med)
                        if listagem:
                            sg.popup_scrolled("\n".join(listagem), title="Lista de Autores", font=("Calibri", 12), size=(90, 20))
                            resposta = [
                            [sg.Text("Deseja aceder aos artigos de algum autor?")],
                            [sg.Button("Sim"), sg.Button("Não")]
                            ]
                            window_resposta = sg.Window("Aceder a Artigos", resposta, font=('Calibri', 15))
                            stop_r = False
                            while not stop_r:
                                event_r, _ = window_resposta.read()
                                if event_r in ["Não", sg.WIN_CLOSED]:
                                    stop_r = True
                                elif event_r == "Sim":
                                    window_resposta.close()
                                    Aceder_artigos()
                            window_resposta.close()
                        else:
                            sg.popup_error("Nenhum autor encontrado.")
                    elif event_6 == "Por Frequência":
                        listagem = Projeto.listar_freq_Inter(ata_med)
                        if listagem:
                            sg.popup_scrolled("\n".join(listagem), title="Lista de Autores", font=("Calibri", 12), size=(90, 20))
                            resposta = [
                                [sg.Text("Deseja aceder aos artigos de algum autor?")],
                                [sg.Button("Sim"), sg.Button("Não")]
                            ]
                            window_resposta = sg.Window("Aceder a Artigos", resposta, font=('Calibri', 15))
                            stop_r = False
                            while not stop_r:
                                event_r, _ = window_resposta.read()
                                if event_r in ["Não", sg.WIN_CLOSED]:
                                    stop_r = True
                                elif event_r == "Sim":
                                    window_resposta.close()
                                    Aceder_artigos()
                            window_resposta.close()
                        else:
                            sg.popup_error("Nenhum autor encontrado.")
                window_layout_6.close()
        elif opcao=="7":
            if a == 0:
                sg.popup("Ainda não usou a função carregar ficheiro. Para que qualquer opção funcione, tem que utilizar primeiro a opção 1.",title="Atenção")
            else:
                criar_layout_7()
        elif opcao=="8":
            if a == 0:
                sg.popup("Ainda não usou a função carregar ficheiro. Para que qualquer opção funcione, tem que utilizar primeiro a opção 1.",title="Atenção")
            else:
                layout_8=criar_layout_8()
                window_layout_8 = sg.Window("Opções de Análise", layout_8, font=('Calibri', 15))
                stop8 = False
                while not stop8:
                    event_8, _ = window_layout_8.read()
                    if event_8 in ["Fechar", sg.WIN_CLOSED]:
                        stop8 = True
                    elif event_8=="-AALF-":
                        try:
                            Projeto.analise_palavra_chave_alf(ata_med, "palavras_chave_ord_alf.txt")
                            sg.popup(f"O resultado foi salvo no ficheiro: palavras_chave_ord_alf.txt", font=('Calibri', 15))
                            ficheiro=[
                                [sg.Text("Deseja abrir/consultar esse ficheiro?")],  
                                [sg.Button("Sim"), sg.Button("Não")]
                            ]
                            window_ficheiro = sg.Window("Análise Registo de Palavras-Chave", ficheiro, font=('Calibri', 15))
                            stop_f = False
                            while not stop_f:
                                event_f, _ = window_ficheiro.read()
                                if event_f in ["Não", sg.WIN_CLOSED]:
                                    stop_f = True
                                else:
                                    window_ficheiro.close()
                                    with open("./palavras_chave_ord_alf.txt", 'r', encoding= "utf-8") as f:
                                        conteudo = f.read().splitlines()
                                    layout_pal = [
                                        [sg.Text("Selecione uma Palavra-Chave para consultar mais informações:", font=("Calibri", 17))],
                                        [sg.Listbox(values=conteudo, size=(80, 10), horizontal_scroll=True, key='-PAL-', enable_events=True)],
                                        [sg.Button("Publicações com esta Palavra-Chave"), sg.Button("Voltar")]
                                    ]
                                    window_pal = sg.Window("Listagem das Palavras-Chave", layout_pal, font=('Calibri', 15))
                                    stop_p=False
                                    while not stop_p:
                                        event_p, values_p = window_pal.read()
                                        if event_p in ["Voltar", sg.WIN_CLOSED]:
                                            stop_p=True
                                        elif event_p == "Publicações com esta Palavra-Chave":
                                            palavra=str(values_p['-PAL-']).split("\n")
                                            pal_selecionado = str(palavra[0][2:-2])
                                            nome_fich=f"pubs_pal_selecionada.txt"
                                            resposta=Projeto.aceder_pubs_pal(ata_med, pal_selecionado, nome_fich)
                                            if resposta:
                                                with open(f"./{nome_fich}", 'r', encoding= "utf-8") as f:
                                                    registos = f.read()
                                                sg.popup_scrolled(f"Conteúdo do ficheiro:{nome_fich}\n\n{registos}", title=f"Resultado da Análise por: {pal_selecionado}", size=(100,20) )
                                            else:
                                                sg.popup(f"Não foram encontrados registos com essa Palavra-Chave.", title="Erro", font=('Calibri', 15))
                                    window_pal.close()
                            window_ficheiro.close() 
                        except Exception as e:
                            sg.popup_error(f"Erro ao consultar Palavra-Chave: {str(e)}")
                        
                    elif event_8== "-AFREQ-":
                        try:
                            Projeto.analise_palavra_chave_freq(ata_med, "palavras_chave_freq.txt")
                            sg.popup(f"O resultado foi salvo no ficheiro: palavras_chave_freq.txt", font=('Calibri', 15))
                            ficheiro=[
                                [sg.Text("Deseja abrir/consultar esse ficheiro?")],  
                                [sg.Button("Sim"), sg.Button("Não")]
                            ]
                            window_ficheiro = sg.Window("Análise Registo de Palavras-Chave", ficheiro, font=('Calibri', 15))
                            stop_f = False
                            while not stop_f:
                                event_f, _ = window_ficheiro.read()
                                if event_f in ["Não", sg.WIN_CLOSED]:
                                    stop_f = True
                                else:
                                    window_ficheiro.close()
                                    with open("./palavras_chave_freq.txt", 'r', encoding= "utf-8") as f:
                                        conteudo = f.read().splitlines()
                                    layout_pal = [
                                        [sg.Text("Selecione uma Palavra-Chave para consultar mais informações:", font=("Calibri", 17))],
                                        [sg.Listbox(values=conteudo, size=(80, 10), horizontal_scroll=True, key='-PAL-', enable_events=True)],
                                        [sg.Button("Publicações com esta Palavra-Chave"), sg.Button("Voltar")]
                                    ]
                                    window_pal = sg.Window("Listagem das Palavras-Chave", layout_pal, font=('Calibri', 15))
                                    stop_p=False
                                    while not stop_p:
                                        event_p, values_p = window_pal.read()
                                        if event_p in ["Voltar", sg.WIN_CLOSED]:
                                            stop_p=True
                                        elif event_p == "Publicações com esta Palavra-Chave":
                                            palavra=str(values_p['-PAL-']).split(" :: ")
                                            pal_selecionado = str(palavra[0][3:])
                                            nome_fich=f"pubs_pal_selecionada.txt"
                                            resposta=Projeto.aceder_pubs_pal(ata_med, pal_selecionado, nome_fich)
                                            if resposta:
                                                with open(f"./{nome_fich}", 'r', encoding= "utf-8") as f:
                                                    registos = f.read()
                                                sg.popup_scrolled(f"Conteúdo do ficheiro:{nome_fich}\n\n{registos}", title=f"Resultado da Análise por: {pal_selecionado}", size=(100,20) )
                                            else:
                                                sg.popup(f"Não foram encontrados registos com essa Palavra-Chave.", title="Erro", font=('Calibri', 15))
                                    window_pal.close()
                            window_ficheiro.close() 
                        except Exception as e:
                            sg.popup_error(f"Erro ao consultar Palavra-Chave: {str(e)}")
                window_layout_8.close()
        elif opcao=="9":
            if a == 0:
                sg.popup("Ainda não usou a função carregar ficheiro. Para que qualquer opção funcione, tem que utilizar primeiro a opção 1.",title="Atenção")
            else:
                layout_9=criar_layout_9()
                window_layout_9 = sg.Window("Opções de Distribuição", layout_9, font=('Calibri', 15))
                stop9 = False
                while not stop9:
                    event_9, _ = window_layout_9.read()
                    if event_9 in ["Fechar", sg.WIN_CLOSED]:
                        stop9 = True
                    elif event_9=="-DISTANO-":
                        Projeto.distribPub_Ano(ata_med)
                    elif event_9=="-DISTMES-":
                        ano=[
                            [sg.Text("Introduza o Ano que Pretende Analisar:"), sg.Input(key='-ANO-')],
                            [sg.Button("Ok"), sg.Button("Fechar")]
                        ]
                        window_ano = sg.Window("Ano", ano , font=('Calibri', 15))
                        stop_ano = False
                        while not stop_ano:
                            event_ano, values_ano = window_ano.read()
                            if event_ano in ["Fechar", sg.WIN_CLOSED]:
                                stop_ano = True
                            else:
                                data=values_ano["-ANO-"]
                                res= Projeto.distribPub_Mes(ata_med,data)
                                if res==False:
                                    sg.popup("Não foi possivel encontrar nenhum registo com esse Ano!", title="Atenção", font=('Calibri', 15))
                        window_ano.close()
                    elif event_9=="-DISTAUT20-":
                        Projeto.distribTop20_Autor(ata_med)
                    elif event_9=="-DISTAUTANO-":
                        autor=[
                            [sg.Text("Introduza o Nome do Autor que Pretende Analisar:"), sg.Input(key='-NOME-')],
                            [sg.Button("Ok"), sg.Button("Fechar")]
                        ]
                        window_autor = sg.Window("Autor", autor , font=('Calibri', 15))
                        stop_autor = False
                        while not stop_autor:
                            event_autor, values_autor = window_autor.read()
                            if event_autor in ["Fechar", sg.WIN_CLOSED]:
                                stop_autor = True
                            else:
                                nome=values_autor["-NOME-"]
                                res=Projeto.distribPub_Autor(ata_med,nome)
                                if res==False:
                                    sg.popup("Não foi possivel encontrar nenhum registo com esse autor!", title="Atenção", font=('Calibri', 15))
                        window_autor.close()
                    elif event_9 == '-DISTPAL20-':
                        Projeto.distribPalavras_Freq(ata_med)
                    elif event_9 == '-DISTPALANO-':
                        ano=[
                            [sg.Text("Introduza o Ano que Pretende Analisar:"), sg.Input(key='-DATA-')],
                            [sg.Button("Ok"), sg.Button("Fechar")]
                        ]
                        window_ano = sg.Window("Ano", ano , font=('Calibri', 15))
                        stop_ano = False
                        while not stop_ano:
                            event_ano, values_ano = window_ano.read()
                            if event_ano in ["Fechar", sg.WIN_CLOSED]:
                                stop_ano = True
                            else:
                                ano=values_ano["-DATA-"]
                                res=Projeto.distribPalavras_Freq_Ano(ata_med, ano)
                                if res==False:
                                    sg.popup("Não foi possivel encontrar nenhum registo com esse Ano!", title="Atenção", font=('Calibri', 15))
                        window_ano.close()
                window_layout_9.close()
        else:
            sg.popup("Essa opção não é valida! Digite um número de 1 a 9." , title="Erro", font=('Calibri', 15))