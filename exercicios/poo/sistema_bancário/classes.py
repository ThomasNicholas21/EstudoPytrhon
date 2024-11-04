import abc

class Pessoa:
    def __init__(self, nome: str, idade: int, cpf: str, cep: str) -> None:
        self._nome = nome
        self._idade = idade
        self._cpf = cpf
        self._cep = cep

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def idade(self):
        return self._idade
    
    @property
    def cpf(self) -> str:
        return self._cpf
    
    @property
    def cep(self) -> str:
        return self._cep

class Cliente(Pessoa): # Agrega classe Conta
    def __init__(self, conta, nome: str, idade: int, cpf: str, cep: str) -> None:
        super().__init__(nome, idade, cpf, cep)
        self.conta = conta

class Conta(abc.ABC):
    def __init__(self, numero: int, saldo: float = 0, agencia='001') -> None:
        self.agencia = agencia
        self._numero = numero
        self._saldo = saldo

    @abc.abstractmethod
    def sacar(self, valor) -> float: ...  

    def depositar(self, valor: float) -> None:
        print(f'Depositando R${valor:.2f}')
        self.saldo += valor

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}:{self.agencia!r} | {self._numero!r} | {self._saldo!r}'

class ContaCorrente(Conta):
    def __init__(self, limite_maximo, numero: int, saldo: float = 0) -> None:
        super().__init__(numero, saldo)
        self.limite_maximo = limite_maximo

    def sacar(self, valor) -> float:
        if valor > self.limite_maximo:
            print('Limite máximo excedido.')
            return 
        
        self._saldo -= valor
        print('Saque realizado.')
        return self._saldo

class ContaPoupanca(Conta):
    def sacar(self, valor) -> float | None:
        if valor > self._saldo:
            print('Valor supera seu Saldo.')
            return
        
        self._saldo -= valor
        print('Saque efetuado')
        return self._saldo


class Banco: # agrega clientes e contas
    def __init__(self, agencia: '001', contas: list, clientes: list) -> None:
        self.agencia = agencia
        self.contas = contas
        self.clientes = clientes

    def verificar_agencia(self, conta) -> bool:
        if self.agencia in conta.__dict__:
            return True
        return False

    def verificar_conta(self, cliente):
        ...

if __name__ == '__main__':
    cliente1 = Pessoa('Thomas', 22, '123456789', '123456')
    print(cliente1.nome)
    print(cliente1.idade)
    print(cliente1.cpf)
    print(cliente1.cep)
    #conta = Conta(1, 120.50)
    cc = ContaCorrente(1000, 12, 1000)
    cc.sacar(500)
    print(cc._saldo) # verificando se saldo está sendo realizado, porém o atributo so deve ser visualizado caso ele seja público
    cp = ContaPoupanca(1, 555)
    cliente2 = Cliente(cp, 'Nicholas', 21, '987456321', '123987456')
    print(cliente2.conta)
    print(cliente2.nome)
    print(cliente2.idade)
    print(cliente2.cpf)
    print(cliente2.cep)
    cp.sacar(155)
    print(cp._saldo)