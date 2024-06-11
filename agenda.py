class AgendaTelefonica:
    def __init__(self):
        self.contatos = {}

    def adicionar_contato(self, nome, telefone):
        if nome in self.contatos:
            print("Contato já existe.")
        else:
            self.contatos[nome] = telefone
            print("Contato adicionado com sucesso.")

    def remover_contato(self, nome):
        mensagem = "Contato removido com sucesso." if nome in self.contatos else "Contato não encontrado."
        self.contatos.pop(nome, None)
        print(mensagem)

    def pesquisar_contato(self, nome):
        mensagem = f"Nome: {nome}, Telefone: {self.contatos.get(nome, 'Contato não encontrado.')}"
        print(mensagem)

    def listar_contatos(self):
        mensagem = "\n".join([f"Nome: {nome}, Telefone: {telefone}" for nome, telefone in self.contatos.items()])
        print(mensagem if mensagem else "A agenda está vazia.")

def menu():
    print("\nOperações disponíveis:")
    print("1. Adicionar Contato")
    print("2. Remover Contato")
    print("3. Pesquisar Contato")
    print("4. Listar Contatos")
    print("5. Sair")

def main():
    agenda = AgendaTelefonica()
    while True:
        menu()
        escolha = input("Escolha uma opção (1/2/3/4/5): ")

        if escolha == '5':
            print("Obrigado por usar a agenda telefônica. Adeus!")
            break
        elif escolha == '1':
            nome, telefone = input("Digite o nome e o telefone do contato separados por espaço: ").split()
            agenda.adicionar_contato(nome, telefone)
        elif escolha == '2':
            nome = input("Digite o nome do contato que deseja remover: ")
            agenda.remover_contato(nome)
        elif escolha == '3':
            nome = input("Digite o nome do contato que deseja pesquisar: ")
            agenda.pesquisar_contato(nome)
        elif escolha == '4':
            agenda.listar_contatos()
        else:
            print("Opção inválida. Escolha uma opção válida (1/2/3/4/5).")

if __name__ == "__main__":
    main()
