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

    def inserir_contato(self, contato: Contato) -> None:
        self.lista_contatos.append(contato)

    def achar_contato(self, contato: Contato) -> bool:
        if contato in self.lista_contatos:
            return True
        return False
    
    def pegar_informacoes(self, contato: Contato) -> str | None:
        if self.achar_contato(contato):
            return f'Nome:{contato.get_nome}, Número:{contato.get_numero}'
        return 

def cadastro_contato(agenda: Agenda_telefonica) -> None:
    nome = input('Nome: ').capitalize().strip()
    telefone = input('Número: ').strip()
    contato = Contato(nome, telefone)
    agenda.inserir_contato(contato)

def buscar_contato(agenda: Agenda_telefonica):
    nome = input('Digite o nome: ').capitalize().strip()
    buscar = [
        agenda.pegar_informacoes(contato) 
        for contato in agenda.lista_contatos 
        if contato.get_nome == nome
    ]
    if buscar:
        print(*buscar, sep='\n')
        print()
    else:
        print('Contato Inexistente.', '\n')

def listar_contatos(agenda: Agenda_telefonica):
    contatos = [contato for contato in agenda.lista_contatos]
    if contatos:
        print(*contatos, sep='\n')
        print()
    else:
        print('Sem Contatos cadastrados.', '\n')

def menu_processos(agenda: Agenda_telefonica) -> bool:
    opcoes = input('Comandos Agenda: Cadastro de Contato [CC],' 
                   'Buscar Contato [BC], Listar Contatos [LC] '
                   'e Sair [S]\n-->').lower().strip()

    match opcoes:
        case 'cc':
            cadastro_contato(agenda)
            return False
        case 'bc':
            buscar_contato(agenda)
            return False
        case 'lc':
            listar_contatos(agenda)
            return False
        case 's':
            print('Encerrando agenda.')
            return True   
        case _:
            print('Comando invalido')
            return False

def main():
    lista_contatos = []
    agenda = Agenda_telefonica(lista_contatos)
    
    while True:
        menu = menu_processos(agenda)
        if menu:
            print('Fechando agenda.')
            break
        
if __name__ == '__main__':
    main()
    # contato_teste1 = Contato('Fulano', '62982520334')
    # lista_contatos = []
    # agenda = Agenda_telefonica(lista_contatos)
    # agenda.insert_contato(contato_teste1)
    # print(lista_contatos)
    # print(contato_teste1, agenda)
    # if agenda.find_contato(contato_teste1):
    #     print('Presente')
    # contato = agenda.get_informacoes(contato_teste1)
    # print(contato)