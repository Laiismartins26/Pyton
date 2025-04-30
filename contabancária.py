class ContaBancaria: 
    def __init__(self, titular, saldo_inicial=0, limite=0):
        self._titular = titular
        self._saldo = saldo_inicial
        self._limite = limite
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            return True
        return False
    
    def sacar(self, valor):
        if valor > 0 and (self._saldo + self._limite) >= valor:
            self._saldo -= valor
            return True
        return False
    
    def get_saldo(self):
        return self._saldo
    
    def set_limite(self, novo_limite):
        if novo_limite >= 0:
            self._limite = novo_limite
            return True
        return False
    
    def __str__(self):
        return (f"titular: {self._titular}\n"
                f"saldo: R${self._saldo:.2f}\n"
                f"limite: R${self._limite:.2f}")