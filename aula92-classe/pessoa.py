from datetime import datetime
from random import randint

class Pessoa:
  ano_atual = datetime.now().year
  def __init__(self, nome, idade, comendo=False, falando=False):
    self.nome = nome
    self.idade = idade
    self.comendo = comendo
    self.falando = falando


  def comer(self, alimento):
    if self.comendo == True:
      print(f'{self.nome} já está comendo.')
      return
    if self.falando == True:
      print(f'{self.nome} está falando, não pode comer.')
      return

    print(f'{self.nome} está comendo {alimento}.')
    self.comendo = True


  def parar_comer(self):
    if self.comendo == False:
      print(f'{self.nome} não está comendo.')
      return

    print(f'{self.nome} parou de comer.')
    self.comendo = False


  def falar(self, assunto):
    if self.falando == True:
      print(f'{self.nome} já está falando.')
      return
    if self.comendo == True:
      print(f'{self.nome} está comendo, não pode falar.')
      return

    print(f'{self.nome} está falando sobre {assunto}.')
    self.falando = True

  def parar_falar(self):
    if self.falando == False:
      print(f'{self.nome} não está falando.')
      return

    print(f'{self.nome} parou de falar.')
    self.falando = False


  def get_nascimento(self):
    return self.ano_atual - self.idade


  # classmethod - aula 94
  @classmethod
  def cria_pessoa_por_ano(cls, nome, ano_nasc):
    idade = cls.ano_atual - ano_nasc
    return cls(nome, idade)


  # staticmethod - aula 95
  @staticmethod
  def gera_id():
    aleat = randint(10000, 19999)
    return aleat