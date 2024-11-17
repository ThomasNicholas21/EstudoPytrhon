# Dia 15: Estruturas Aninhadas
# Faça um programa que simule uma agenda telefônica, 
# onde o usuário pode cadastrar contatos (nome e número) e buscar um contato pelo nome.
from dataclasses import dataclass

@dataclass
class Contato:
    _nome: str
    _numero: str 

    @property
    def get_nome(self) -> str:
        return self._nome

    @property
    def get_numero(self) -> str:
        return self._numero

@dataclass
class Agenda_telefonica:
    lista_contatos: list[Contato]

    def insert_contato(self, contato: Contato):
        self.lista_contatos.append(contato)

    def find_contato(self, contato: Contato) -> bool:
        if contato in self.lista_contatos:
            return True
        return False
    
    def get_informacoes(self, contato: Contato) -> str | None:
        if self.find_contato(contato):
            return f'Nome:{contato.get_nome}, número:{contato.get_numero}'
        return 

def cadastro_contato(lista_contatos) -> None:
    ...

def buscar_contato():
    ...

def menu_processos(agenda):
    opcoes = input('Comandos Agenda: Cadastro de Contato [CC],' 
                   'Buscar Contato [BC] e Sair [S]\n-->')

    match opcoes:
        case 'cc':
            cadastro_contato(agenda)
            return False
        case 'bc':
            ...
            return False
        case 's':
            ...
            return True   
        case _:
            print('Comando invalido')
            return False

def main():
    lita_contatos = []
    agenda = Agenda_telefonica(lista_contatos)
    
    while True:
        menu = menu_processos(agenda)
        if menu:
            print('Fechando agenda.')
            break
        
if __name__ == '__main__':
    #main()
    contato_teste1 = Contato('Fulano', '62982520334')
    lista_contatos = []
    agenda = Agenda_telefonica(lista_contatos)
    agenda.insert_contato(contato_teste1)
    print(lista_contatos)
    # print(contato_teste1, agenda)
    # if agenda.find_contato(contato_teste1):
    #     print('Presente')
    # contato = agenda.get_informacoes(contato_teste1)
    # print(contato)