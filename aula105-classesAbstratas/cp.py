from conta import Conta

class ContaPoupanca(Conta):

    def sacar(self, valor): # Polimorfismo - método igual ao da classe cc, mas com comportamento diferente.
        if not isinstance(valor, (int, float)):
            raise ValueError("Valor precisa ser numérico")

        if self._saldo < valor:
            print('Saldo insuficiente')
            return

        self._saldo -= valor
        self.detalhes()

