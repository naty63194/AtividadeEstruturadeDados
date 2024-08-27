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

  def __lista_vazia(self):
      return self.primeiro == None

  def insere_ordenado(self, valor):
      novo = No(valor)
      atual = self.primeiro

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
      if self.primeiro.proximo is None:
          self.primeiro = None
          self.ultimo = None
      else:
          self.primeiro = self.primeiro.proximo
          self.primeiro.anterior = None

      return temp

  def excluir_final(self):
      if self.__lista_vazia():
          return None

      temp = self.ultimo
      if self.primeiro.proximo is None:
          self.primeiro = None
          self.ultimo = None
      else:
          self.ultimo = self.ultimo.anterior
          self.ultimo.proximo = None

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

# Exemplo de uso:
lista = ListaDuplamenteEncadeadaOrdenada()
lista.insere_ordenado(10)
lista.insere_ordenado(20)
lista.insere_ordenado(30)
