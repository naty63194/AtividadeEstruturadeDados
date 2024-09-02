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
def recebe_inteiro(numero_inicial, numero_final, txt=""):
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

# Função que chama o menu
def menu():
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
print(f'{" Listas Duplamente Encadeadas e Ordenadas ":=^60}')
while True:
    escolha = menu()
    if escolha == 1:
        print("escolheu 1")
        lista.mostrar_frente()
    elif escolha == 2:
        print("escolheu 2")
        lista.mostrar_tras()
    elif escolha == 3:
        print("escolheu 3")
        lista.insere_ordenado(1)
    elif escolha == 4:
        print("escolheu 4")
        lista.excluir_inicio()
    elif escolha == 5:
        print("escolheu 5")
        lista.excluir_final()
    elif escolha == 6:
        print("escolheu 6")
        lista.limpar_lista()
    elif escolha == 7:
        print("escolheu 7")
        lista.buscar_frente(1)
    elif escolha == 8:
        print("escolheu 8")
        lista.buscar_tras(1)
    else:
        break


# Exemplo de uso:
# lista = ListaDuplamenteEncadeadaOrdenada()
# lista.insere_ordenado(10)
# lista.insere_ordenado(20)
# lista.insere_ordenado(30)
# lista.insere_ordenado(40)
# lista.insere_ordenado(40)
# lista.insere_ordenado(80)
# lista.insere_ordenado(5)
# lista.insere_ordenado(35)
# lista.insere_ordenado(55)

# lista.mostrar_frente()
#
# print("")
#
# print(lista.buscar_frente(30))
# print(lista.buscar_tras(30))

