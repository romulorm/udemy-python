from cp import ContaPoupanca
from cc import ContaCorrente


cp = ContaPoupanca(1111, 2222, 0)
cp.depositar(100)
cp.sacar(150)

cc = ContaCorrente(2222, 5334, 0)
cc.depositar(100)
cc.sacar(250)
