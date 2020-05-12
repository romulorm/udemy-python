from conta import Conta

from conta import Conta

class ContaCorrente(Conta):

    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self._limite = limite

    @property
    def limite(self):
        return self._limite

    def sacar(self, valor): # Polimorfismo - método igual ao da classe cp, mas com comportamento diferente.
        if not isinstance(valor, (int, float)):
            raise ValueError("Valor precisa ser numérico")

        if self._saldo + self._limite < valor:
            print('Saldo insuficiente')
            return

        self._saldo -= valor
        self.detalhes()