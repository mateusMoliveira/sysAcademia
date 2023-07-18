from modulo import *
import os

alunos = []
alunos = carregar_alunos()
opc = 0

while (opc != 5):

    ExibirMenu()
    opc = int(input())

    if opc == 1:
        alunos.append(cadastrar_alunos())
        limpar_tela()
        salvar_alunos(alunos)
    
    elif opc == 2:
        imprimir(alunos)

        limpar_tela()

    elif opc == 3:
        buscar_id(alunos)
        
        limpar_tela()

    elif opc == 4:
        filtrar(alunos)
        limpar_tela()

    elif opc == 5:
        opc = perguntar_e_salvar(alunos)
        limpar_tela()

    else:
        print("Opção Inválida!")
        limpar_tela()
