# Dia 1: Estruturas Condicionais
# Crie um programa que leia a idade de uma pessoa e informe se ela pode votar ou não.

# Necessário para votar no Brasil
# Idade minima: 16 e 17 e maiores de 70 anos- Voto Facultativo
# Idade minima: 18 aos 70 anos - Voto Obrigatório
# Nacionalidade: Ser Brasileiro ou naturalizado
# Titulo de Eleitor: Numero de identificação
# Documento de Identificação: Utilizar CPF ou RG 
# Capacidade Civil: direitos políticos suspensos (condenação eleitoral)
# Esse programa Verifica se a pessoa está apta a votar, não realiza consultas externas
from datetime import datetime

ANO_ATUAL = datetime.now().year

class ArmezenaInfo:
    def armazena_true(self, texto, lista_true):
        lista_true.append(texto)

    def armazena_false(self, texto, lista_false):
        lista_false.append(texto)

    def listagem_true(self, lista_true):
        for texto in lista_true:
            print(texto, sep=' | ')

    def listagem_false(self, lista_false):
        for texto in lista_false:
            print(texto, sep=' | ')
       
class NecessarioParaVotar(ArmezenaInfo):
    def idade_minima(self, ano_nascimento) -> bool:
        idade = ANO_ATUAL - ano_nascimento
        if idade == 16 or idade == 17 or idade >= 70:
            self.armazena_true(f'Idade: {idade} - Voto Facultativo')
            return True
        
        elif 18 <= idade < 70:
            self.armazena_true(f'Idade: {idade} - Voto Obrigatório')
            return True
        
        self.armazena_false(f'Idade: {idade} - Não está apto para votar')
        return False
        
    def verifica_nacionalidade(self, cpf) -> bool:
        validacao = input('Confirme seu CPF: ')
        if validacao == cpf:
            return True
        
        return False
    
    def verifica_titulo(self):
        inscricao_titulo = input('Insira sua inscriação de titulo: ')
        if 0 < len(inscricao_titulo) <= 6:
            self.armazena_true(f'Titulo:{inscricao_titulo} - Titulo Validado')
            return True
        
        self.armazena_false(f'Titulo:{inscricao_titulo} - Titulo Invalido')
        return False
     
    def capacidade_civil(self):
        verifica_capacidade_civil = input('Possui condenação eleitoral, [s]im ou [n]ão: ').lower().startswith('n')
        if verifica_capacidade_civil:
            self.armazena_true(f'Capacidade Civil: {verifica_capacidade_civil} - Titulo Validado')
            return True
        
        return False
    
class Pessoa(ArmezenaInfo):
    def __init__(self, nome, cpf, ano_nascimento) -> None:
        self._nome = nome
        self._cpf = cpf
        self._ano_nascimento = ano_nascimento     
        self.necessario_para_votar = NecessarioParaVotar()

    def pode_votar(self) -> bool:
        if self.necessario_para_votar.idade_minima(self._ano_nascimento) and self.necessario_para_votar.verifica_nacionalidade(self._cpf) and self.necessario_para_votar.verifica_titulo() and self.necessario_para_votar.capacidade_civil():
            self.listagem_true()
        
        self.listagem_false()
        

    # def __del__(self):
    #     print('Dados sendo destruídos após validação!')
def cadastro_pessoa(lista):
    nome = input('Digite seu nome: ')
    cpf = input('Digite seu CPF: ')
    ano_nascimento = int(input('Digite seu ano de nascimento: '))
    usuario = Pessoa(nome=nome, cpf=cpf, ano_nascimento=ano_nascimento)
    
def main():
    lista_true = []
    lista_false = []


main()