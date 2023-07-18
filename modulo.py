import os
import json

def ExibirMenu():
    print('''
<>---------------------------------------<>
                SysAcademy
<>---------------------------------------<>
    Digite a opção desejada:
    1. Cadastrar Aluno
    2. Exibir lista de alunos
    3. Buscar aluno por ID
    4. Filtrar alunos por IMC
    5. Sair
<>---------------------------------------<>
    Opção: ''',end ='')

def limpar_tela():
    '''limpar_tela: limpa as linhas do terminal
    '''
    input("Digite 'ENTER' para continuar...")
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def cadastrar_alunos():
    '''cadastrar_alunos: Retorna um dicionário com as informações de cadastro
    '''
    cont = carregar_alunos()
    cont = len(cont)

    aluno = {'nome':'', 'id':'', 'telefone':'', 'peso':0.0, 'altura':0.0, 'mensalidade':0.0, 'sexo':''}
    for chave in aluno:
        if chave == 'nome':
            aluno[chave] = str(input(f"{chave}: "))
        
        elif chave == 'id':
            aluno[chave] = cont+1

        elif chave == 'telefone':
            aluno[chave] = int(input(f"{chave}: "))

        elif chave == 'peso':
            aluno[chave] = float(input(f"{chave}: "))

        elif chave == 'altura':
            aluno[chave] = float(input(f"{chave}: "))

        elif chave == 'mensalidade':
            aluno[chave] = float(input(f"{chave}: "))

        elif chave == 'sexo':
            aluno[chave] = str(input(f"{chave}: "))

    return aluno

def carregar_alunos():
    '''carregar_alunos: carrega os dicionarios de alunos dentro do arquivo json
    '''
    alunos = []
    try:
        ler = open("Alunos.json","r")
        alunos = json.load(ler)
        ler.close()
    except:
        print("Ainda não existem alunos cadastrados!!")
    return alunos

def salvar_alunos(alunos):
    '''salvar_alunos: salva os dicionarios de alunos dentro do arquivo json
    '''
    esc = open('Alunos.json','w')
    json.dump(alunos,esc)
    esc.close()

def imprimir(alunos):
    '''imprimir: imprimi os dicionarios de alunos na tela
    '''
    print(alunos)

def buscar_id(alunos):
    '''buscar_id: busca no arquivo json os dicionarios com o id correspondente e mostra na tela
    '''
    print('Digite um ID do aluno desejado: ')
    ident = int(input())

    cont = len(alunos)
    
    if ident > cont or ident <= 0:
        return print('ID inválido!')
    else:
        for i in range(cont+1):
            if i == ident:
                return print(alunos[i-1])

def filtrar(alunos):
    '''filtrar: filtra os dicionarios que possuem imc maior que 30 e mostra na tela
    '''
    lista = {}
    for i in range(len(alunos)):
        peso = alunos[i].get('peso')
        altura = alunos[i].get('altura')
        imc = peso/(altura*altura)
        if imc > 30:
            lista[i] = alunos[i]
    return print(lista)

def perguntar_e_salvar(alunos):
    '''perguntar_e_salvar: pergunta ao usuario se deseja sair do programa e salva o parametro alunos dentro do arquivo json
    '''
    print("Deseja salvar e sair? (S) para sim (N) para não")
    resp = str(input())
    if resp == 'S' or resp == 's':
        salvar_alunos(alunos)
        return 5
    else:
        return 0