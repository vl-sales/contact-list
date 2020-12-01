class Interface:
    def __init__(self, fornecedores):
        self.fornecedor = fornecedores

    def insere_fornecedor(self):
        nome = input('Informe o nome do fornecedor: ')
        telefone = input('Informe o telefone do fornecedor: ')
        email = input('Informe o e-mail do fornecedor: ')

        self.fornecedor.append([nome, telefone, email])

    def remove_fornecedor(self):
        informacao = input('Digite alguma informação do fornecedor (nome/telefone/email): ')
        verifica = False

        for linha in self.fornecedor:
            for valor in linha:
                if informacao == valor:
                    self.fornecedor.remove(linha)
                    verifica = True
                    print('Fornecedor removido!')
        if verifica == False:
            print('Fornecedor não encontrado')

    def busca_fornecedor(self):
        informacao = input('Digite alguma informação do fornecedor (nome/telefone/email): ')
        verifica = False

        for linha in self.fornecedor:
            if informacao in linha:
                print(linha)
                verifica = True
        if verifica == False:
            print('Fornecedor não encontrado')

    def visualiza_fornecedores(self):
        for linha in self.fornecedor:
            print(linha)

    def transforma_em_csv(self):
        arquivo = open('fornecedores.csv', 'w')

        escritor = csv.writer(arquivo, delimiter=';', lineterminator='\n')
        escritor.writerows(self.fornecedor)

        arquivo.close()
        print('Arquivo transformado com sucesso')

    def run(self):
        print('1- Inserir novo fornecedor\n\
        2- Remover fornecedor\n\
        3- Busca fornecedor\n\
        4- Transformar em arquivo .csv\n\
        5- Visualizar arquivo completo\n\
        0- Sair')

        escolha = input('O que fazer: ')

        while escolha != '1' and escolha != '2' \
                and escolha != '3' and escolha != '4' \
                and escolha != '5' and escolha != '0':
            print('Opção inválida')
            escolha = input('O que fazer: ')

        while escolha != '0':
            if escolha == '1':
                self.insere_fornecedor()
                escolha = input('O que fazer: ')
            elif escolha == '2':
                self.remove_fornecedor()
                escolha = input('O que fazer: ')
            elif escolha == '3':
                self.busca_fornecedor()
                escolha = input('O que fazer: ')
            elif escolha == '4':
                self.transforma_em_csv()
                escolha = input('O que fazer: ')
            elif escolha == '5':
                self.visualiza_fornecedores()
                escolha = input('O que fazer: ')

        print('===FINALIZADO===')