# Funcoes decoradoras - @syntax_sugar
# Decorar = Adicionar / Remover / Restringir / Alterar
# Decoram outras funcoes 
# Principio da responsabilidade unica - Se um objeto faz mais que o necessário, você deve dividir suas tarefas 

def criar_funcao(func):
    def interna(*args, **kwargs): # inner function / aninhada
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        return resultado
    return interna

@criar_funcao # passa de forma autmática a funcao desejada para a funcao
def inverte_string(string):
    return string[::-1]

def e_string(param):
    if not isinstance(param, str):
        raise TypeError('Deve ser inserido uma string.')
    
#inverte_string_verifica_parametro = criar_funcao(inverte_string) # sem utilizar o syntax sugar
#inverte = inverte_string_verifica_parametro(123)
inverte = inverte_string(123)
print(inverte)

# def fabrica_de_decoradores(a=None, b=None, c=None):
#     def fabrica_de_funcoes(func):
#         print('Decoradora 1')

#         def aninhada(*args, **kwargs):
#             print('Parâmetros do decorador, ', a, b, c)
#             print('Aninhada')
#             res = func(*args, **kwargs)
#             return res
#         return aninhada
#     return fabrica_de_funcoes


# @fabrica_de_decoradores(1, 2, 3)
# def soma(x, y):
#     return x + y


# decoradora = fabrica_de_decoradores()
# multiplica = decoradora(lambda x, y: x * y)

# dez_mais_cinco = soma(10, 5)
# dez_vezes_cinco = multiplica(10, 5)
# print(dez_mais_cinco)
# print(dez_vezes_cinco)
