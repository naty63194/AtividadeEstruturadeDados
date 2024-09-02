import sys

# Função para receber os dados do tipo correto já que python tem tipagem dinâmica
# Também determina um limite mínimo e máximo aceito
# Caso não sejam definidos ele já deixa um limite bem generoso
def recebe_inteiro(numero_inicial=sys.maxsize * -1, numero_final=sys.maxsize, txt=""):
    while True:
        try:
            inteiro = int(input(txt))
        except ValueError:
            print("Valor do tipo incorreto inserido! Tente novamente.")
        else:
            if inteiro < numero_inicial or inteiro > numero_final:
                print("Esse valor não é válido! Tente novamente.")
            else:
                break
    return inteiro