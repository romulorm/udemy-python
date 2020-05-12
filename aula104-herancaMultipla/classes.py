from log import logMixing

class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False


    def ligar(self):
        if self._ligado:
            info = f'{self._nome} já está ligado.'
            print(info)
            self.log_error(info)
            return
        self._ligado = True
        print(f'{self._nome} foi ligado.')


    def desligar(self):
        if not self._ligado:
            info = f'{self._nome} já se encontra desligado.'
            print(info)
            self.log_error(info)
            return
        self._ligado = False
        info = f'{self._nome} foi desligado.'
        print(info)
        self.log_info(info)


class Smartphone(Eletronico, logMixing):
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False


    def conectar(self):
        if not self._ligado:
            info = f'{self._nome} está desligado, não pode se conectar.'
            print(info)
            self.log_error(info)
            return

        if self._conectado:
            info = f'{self._nome} já está conectado.'
            print(info)
            self.log_error(info)

        self._conectado = True
        info = f'{self._nome} conectou-se à Internet.'
        print(info)
        self.log_info(info)


    def desconectar(self):
        if not self._ligado:
            info = f'{self._nome} está desligado, não pode se conectar.'
            print(info)
            self.log_error(info)
            return

        if not self._conectado:
            info = f'{self._nome} já está desconectado.'
            print(info)
            self.log_error(info)
            return

        self._conectado = False
        info = f'{self._nome} desconectou-se da Internet.'
        print(info)
        self.log_info(info)