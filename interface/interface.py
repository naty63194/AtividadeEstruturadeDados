from util.tratamentoDeDados import *

# Função que chama o menu e retorna a escolha do usuário
def menu():
    print(f'{" Listas Duplamente Encadeadas e Ordenadas ":=^60}')
    print("1. Mostrar lista (Crescente)")
    print("2. Mostrar lista (Decrescente)")
    print("3. Inserir um valor")
    print("4. Excluir um valor (Início)")
    print("5. Excluir um valor (Final)")
    print("6. Excluir um valor (Específico)")
    print("7. Excluir um Tudo")
    print("8. Buscar um valor (Crescente)")
    print("9. Buscar um valor (Decrescente)")
    print("10. Sair")
    opcao = recebe_inteiro(1, 9, "Escolha uma opção: ")
    return opcao
