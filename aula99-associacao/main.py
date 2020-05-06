'''
Associação: Um objeto usa outro objeto
Agregação: Um objeto tem outros objetos como parte de si
Composição: Um objeto é dono de outros objetos
Herança: Um objeto é outro objeto

'''

from classes import Escritor, Caneta, MaquinaDeEscrever

escritor = Escritor('Eça de Queiroz')
caneta = Caneta('BIC')
maquina = MaquinaDeEscrever('Olivetti')

escritor.ferramenta = caneta
escritor.ferramenta.escrever()

