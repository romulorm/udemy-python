from classes import Escritor, Caneta, MaquinaDeEscrever

escritor = Escritor('Eça de Queiroz')
caneta = Caneta('BIC')
maquina = MaquinaDeEscrever('Olivetti')

escritor.ferramenta = caneta
escritor.ferramenta.escrever()

