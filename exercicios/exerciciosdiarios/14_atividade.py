# Dia 14: Tratamento de Exceções
# Desenvolva um calculadora que peça dois números ao usuário, e faça a divisão tratando a exceção de divisão por zero.
def divisao_por_zero(self):
    ...

def verificacao_string(metodo):
    def interno(self, *args, **kwargs):
        resultado = metodo(self, *args, **kwargs)

        for arg in args:
            if isinstance(arg, (str, bool)):
                raise ValueError('Erro. Deve ser colocado um número.')
        
        return resultado
    
    return interno

class Calculadora:
    @verificacao_string
    def __init__(self, numero1: int | float, numero2: int | float) -> None:
        self.numero1 = numero1
        self.numero2 = numero2
    
    def soma(self):
        return f'Soma: {self.numero1 + self.numero2}'
    
    def subtracao(self):
        ...

    def multiplicacao(self):
        ...
    
    def divisao(self):
        ...

def calculadora(digitos):
    ...

def main():
    ...

if __name__ == '__main__':
    main()
    teste = Calculadora('1', 2)
