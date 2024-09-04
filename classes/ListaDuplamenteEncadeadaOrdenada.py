from classes.No import No

class ListaDuplamenteEncadeadaOrdenada:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self.tamanho = 0

    # Verifica se a lista está vazia
    def __lista_vazia(self):
        return self.primeiro is None

    # Insere um valor já na posição correta
    def insere_ordenado(self, valor):
        novo = No(valor)
        atual = self.primeiro
        anterior = None
        self.tamanho += 1

        # Caso a lista ainda esteja vazia
        # O valor inserido se torna o primeiro e ultimo elemento da lista
        if self.__lista_vazia():
            self.primeiro = novo
            self.ultimo = novo
        else:
            # Enquanto um valor maior que o inserido não for encontrado
            # continua percorrendo a lista
            while atual is not None and atual.valor < valor:
                anterior = atual
                atual = atual.proximo

            # Se encontrar o maior logo no primeiro elemento
            # simplesmente "empurra" o primeiro e modifica os ponteiros
            if atual == self.primeiro:
                novo.proximo = self.primeiro
                self.primeiro.anterior = novo
                self.primeiro = novo

            # Se chegar ao final da lista, se torna o novo ultimo elemento e
            # modifica os ponteiros do ultimo
            elif atual is None:
                self.ultimo.proximo = novo
                novo.anterior = self.ultimo
                self.ultimo = novo

            # Caso seja encontrado no meio da lista, faz as modificações necessárias
            # nos elementos vizinhos
            else:
                novo.proximo = atual
                novo.anterior = anterior
                anterior.proximo = novo
                atual.anterior = novo

    # Função para excluir o primeiro elemento da lista
    def excluir_inicio(self):
        if self.__lista_vazia(): # Se já estiver vazia não faz nada
            return None

        temp = self.primeiro  # Armazena em uma variável temporária a informação do primeiro elemento

        if self.primeiro == self.ultimo:
            self.primeiro = None
            self.ultimo = None
        else:
            self.primeiro = self.primeiro.proximo  # O primeiro agora passa a ser o seu posterior
            self.primeiro.anterior = None  # O ponteiro "anterior" do elemento que agora está em primeiro é zerado (null)

        self.tamanho -= 1  # Atualiza o atributo tamanho na lista

        return temp # retorna o novo inicio da lista já modificado

    # Função para excluir o último elemento da lista
    def excluir_final(self):
        if self.__lista_vazia(): # Se já estiver vazia não faz nada
            return None

        temp = self.ultimo  # Armazena em uma variável temporária a informação do último elemento

        if self.ultimo == self.primeiro:
            self.ultimo = None
            self.primeiro = None
        else:
            self.ultimo = self.ultimo.anterior  # O último agora passa a ser o seu anterior
            self.ultimo.proximo = None  # O ponteiro "posterior" do elemento que agora está em último é zerado (null)

        self.tamanho -= 1

        return temp # retorna o novo final da lista já modificado

    # Função para excluir um valor em específico na lista
    def excluir_valor(self, valor):
        # Percorre a lista em busca de um elemento igual ao que será excluído
        atual = self.primeiro
        while atual is not None and atual.valor != valor:
            atual = atual.proximo

        # se chegar ao final da lista sem encontrar não altera nada
        if atual is None:
            print("Valor não encontrado.")
            return None

        # Se for o primeiro elemento simplesmete sobreescreve o primeiro pelo seu posterior
        if atual == self.primeiro:
            self.primeiro = atual.proximo
        # Modifica o ponteiro de "proximo" do seu anterior para apontar para seu posterior
        else:
            atual.anterior.proximo = atual.proximo

        # Se for o último elemento sobreescreve pelo penúltimo
        if atual == self.ultimo:
            self.ultimo = atual.anterior

        # Modifica o ponteiro de "anterior" para apontar para o seu anterior
        else:
            atual.proximo.anterior = atual.anterior

        print(f"Número {valor} excluido com sucesso.")
        return atual # Retorna as mudanças

    # Exibe a lista de forma crescente
    def mostrar_frente(self):
        atual = self.primeiro
        while atual is not None:
            atual.mostra_no()
            atual = atual.proximo

    # Exibe a lista de forma decrescente
    def mostrar_tras(self):
        atual = self.ultimo
        while atual is not None:
            atual.mostra_no()
            atual = atual.anterior

    # Exclui a lista inteira
    def limpar_lista(self):
        # Enquanto a lista não estiver vazia exclui o primeiro da lista
        while not self.__lista_vazia():
            self.excluir_inicio()

    # Faz a busca de um número começando no início da lista
    def buscar_frente(self, valor):
        atual = self.primeiro
        posicao = 0 # Guarda o "index" do elemento

        # Percorre a lista até encontrar um valor igual ou maior que o esperado
        while atual is not None and atual.valor <= valor:
            if atual.valor == valor:
                return f"O Número {valor} foi encontrado na posição {posicao}. N° de comparações: {posicao + 1}"
            atual = atual.proximo
            posicao += 1

        return f"O número {valor} não foi encontrado."

    # Faz a busca de um número começando no final da lista
    def buscar_tras(self, valor):
        atual = self.ultimo
        posicao = self.tamanho - 1 # Guarda o "index" do elemento

        # Percorre a lista até encontrar um valor igual ou menor que o esperado
        while atual is not None and atual.valor >= valor:
            if atual.valor == valor:
                return f"O Número {valor} foi encontrado na posição {posicao}. N° de comparações: {(self.tamanho - posicao)}"
            atual = atual.anterior
            posicao -= 1

        return f"O número {valor} não foi encontrado."
