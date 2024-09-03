from classes.ListaDuplamenteEncadeadaOrdenada import ListaDuplamenteEncadeadaOrdenada
from interface.interface import menu
from util.tratamentoDeDados import *

# "main()"
lista = ListaDuplamenteEncadeadaOrdenada()
while True:
    match menu():
        case (1):
            print("Lista Crescente: ")
            lista.mostrar_frente()
        case (2):
            print("Lista Decrescente: ")
            lista.mostrar_tras()
        case (3):
            numeroInt = recebe_inteiro(txt="Digite um número inteiro: ")
            lista.insere_ordenado(numeroInt)
            print(f"Número {numeroInt} inserido com sucesso.")
        case (4):
            lista.excluir_inicio()
            print("Primeiro item da lista excluido com sucesso.")
        case (5):
            lista.excluir_final()
            print("Último item da lista excluido com sucesso.")
        case (6):
            numeroInt = recebe_inteiro(txt="Digite um número inteiro: ")
            lista.excluir_valor(numeroInt)
        case (7):
            lista.limpar_lista()
            print("Lista limpa com sucesso.")
        case (8):
            print(lista.buscar_frente(recebe_inteiro(txt="Digite um número inteiro: ")))
        case (9):
            print(lista.buscar_tras(recebe_inteiro(txt="Digite um número inteiro: ")))
        case _:
            break
    print("")