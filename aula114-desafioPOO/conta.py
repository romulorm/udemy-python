from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @property
    def agencia(self):
        return self.agencia

    @property
    def conta(self):
        return self.conta

    @property
    def saldo(self):
        return self.saldo

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Saldo precisa ser numérico")

        self.saldo = valor

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Depósito precisa ser numérico")

        self.saldo += valor
        self.detalhes()

    def detalhes(self):
        print(f'Agência: {self.agencia} - Conta: {self.conta}')
        print(f'Saldo: {self.saldo}')

    @abstractmethod
    def sacar(self, valor):
        pass


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    @property
    def limite(self):
        return self.limite

    def sacar(self, valor): # Polimorfismo - método igual ao da classe cp, mas com comportamento diferente.
        if not isinstance(valor, (int, float)):
            raise ValueError("Valor precisa ser numérico")

        if self.saldo + self.limite < valor:
            print('Saldo insuficiente')
            return

        self.saldo -= valor
        self.detalhes()


class ContaPoupanca(Conta):
    def sacar(self, valor): # Polimorfismo - método igual ao da classe cc, mas com comportamento diferente.
        if not isinstance(valor, (int, float)):
            raise ValueError("Valor precisa ser numérico")

        if self.saldo < valor:
            print('Saldo insuficiente')
            return

        self.saldo -= valor
        self.detalhes()
