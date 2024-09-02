import sys

class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        self.anterior = None

    def mostra_no(self):
        print(self.valor)


class ListaDuplamenteEncadeadaOrdenada:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self.tamanho = 0

    def __lista_vazia(self):
        return self.primeiro is None

    def insere_ordenado(self, valor):
        novo = No(valor)
        atual = self.primeiro
        anterior = None
        self.tamanho += 1

        if self.__lista_vazia():
            self.primeiro = novo
            self.ultimo = novo
        else:
            while atual is not None and atual.valor < valor:
                anterior = atual
                atual = atual.proximo

            if atual == self.primeiro:
                novo.proximo = self.primeiro
                self.primeiro.anterior = novo
                self.primeiro = novo
            elif atual is None:
                self.ultimo.proximo = novo
                novo.anterior = self.ultimo
                self.ultimo = novo
            else:
                novo.proximo = atual
                novo.anterior = anterior
                anterior.proximo = novo
                atual.anterior = novo

    def excluir_inicio(self):
        if self.__lista_vazia():
            return None

        temp = self.primeiro
        self.primeiro = self.primeiro.proximo
        self.primeiro.anterior = None
        self.tamanho -= 1

        return temp

    def excluir_final(self):
        if self.__lista_vazia():
            return None

        temp = self.ultimo
        self.ultimo = self.ultimo.anterior
        self.ultimo.proximo = None
        self.tamanho -= 1

        return temp

    def excluir_posicao(self, valor):
        atual = self.primeiro
        while atual is not None and atual.valor != valor:
            atual = atual.proximo
        if atual is None:
            return None

        if atual == self.primeiro:
            self.primeiro = atual.proximo
        else:
            atual.anterior.proximo = atual.proximo

        if atual == self.ultimo:
            self.ultimo = atual.anterior
        else:
            atual.proximo.anterior = atual.anterior

        return atual

    def mostrar_frente(self):
        atual = self.primeiro
        while atual is not None:
            atual.mostra_no()
            atual = atual.proximo

    def mostrar_tras(self):
        atual = self.ultimo
        while atual is not None:
            atual.mostra_no()
            atual = atual.anterior

    def limpar_lista(self):
        while not self.__lista_vazia():
            self.excluir_inicio()
        print("Lista limpa com sucesso.")

    # Faz a busca de um número começando no início da lista
    def buscar_frente(self, valor):
        atual = self.primeiro
        posicao = 0

        while atual is not None and atual.valor <= valor:
            if atual.valor == valor:
                return f"O Número {valor} foi encontrado na posição {posicao}."
            atual = atual.proximo
            posicao += 1

        return f"O número {valor} não foi encontrado."

    # Faz a busca de um número começando no final da lista
    def buscar_tras(self, valor):
        atual = self.ultimo
        posicao = self.tamanho - 1

        while atual is not None and atual.valor >= valor:
            if atual.valor == valor:
                return f"O Número {valor} foi encontrado na posição {posicao}."
            atual = atual.anterior
            posicao -= 1

        return f"O número {valor} não foi encontrado."


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

# Função que chama o menu e retorna a escolha do usuário
def menu():
    print(f'{" Listas Duplamente Encadeadas e Ordenadas ":=^60}')
    print("1. Mostrar lista (Crescente)")
    print("2. Mostrar lista (Decrescente)")
    print("3. Inserir um valor")
    print("4. Excluir um valor (Início)")
    print("5. Excluir um valor (Final)")
    print("6. Excluir um valor (Tudo)")
    print("7. Buscar um valor (Crescente)")
    print("8. Buscar um valor (Decrescente)")
    print("9. Sair")
    opcao = recebe_inteiro(1, 9, "Escolha uma opção: ")
    return opcao


# Começa aqui "main()"
lista = ListaDuplamenteEncadeadaOrdenada()
while True:
    escolha = menu()
    if escolha == 1:
        print("Lista Crescente: ")
        lista.mostrar_frente()
    elif escolha == 2:
        print("Lista Decrescente: ")
        lista.mostrar_tras()
    elif escolha == 3:
        numeroInt = recebe_inteiro(txt="Digite um número inteiro: ")
        lista.insere_ordenado(numeroInt)
        print(f"Número {numeroInt} inserido com sucesso.")
    elif escolha == 4:
        lista.excluir_inicio()
        print("Primeiro item da lista excluido com sucesso.")
    elif escolha == 5:
        lista.excluir_final()
        print("Último item da lista excluido com sucesso.")
    elif escolha == 6:
        lista.limpar_lista()
        print("Lista limpa com sucesso.")
    elif escolha == 7:
        print(lista.buscar_frente(recebe_inteiro(txt="Digite um número inteiro: ")))
    elif escolha == 8:
        print(lista.buscar_tras(recebe_inteiro(txt="Digite um número inteiro: ")))
    else:
        break
    print("")
    