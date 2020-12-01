import csv
from parte_2.fornecedor import Fornecedor
from parte_2.agenda import Agenda

class SistemaCadastros:
    max_cadastro = 0  # Conta o números de fornecedores na agenda
    identificador = 1  # Número de identificação (não regride após algum contato ser removido)

    # Método estático para auxiliar o método cadastra_fornecedor a adicionar fornecedores a grupos
    @staticmethod
    def adiciona_ao_grupo(nome_grupo, fornecedor, agenda):

        if not nome_grupo in agenda.keys():
            agenda[nome_grupo] = {fornecedor.identificador: [fornecedor.nome,
                                                             fornecedor.telefone,
                                                             fornecedor.email]}

            SistemaCadastros.max_cadastro += 1
            SistemaCadastros.identificador += 1
        else:
            agenda[nome_grupo][fornecedor.identificador] = [fornecedor.nome,
                                                            fornecedor.telefone,
                                                            fornecedor.email]

            SistemaCadastros.max_cadastro += 1
            SistemaCadastros.identificador += 1

    @staticmethod
    def valida_ddd(ddd):
        while len(ddd) != 2 or ddd.isnumeric() != True:
            print('DDD inválido')
            ddd = input('Informe o DDD: ')
        return ddd

    @staticmethod
    def valida_telefone(numero):
        while (len(numero) == 8 or len(numero) == 9) and (numero.isnumeric() != True):
            print('Número inválido')
            numero = input(f'Informe o telefone do fornecedor: ')
        return numero

    @staticmethod
    def valida_email(email):
        while not ('.' in email and '@' in email):
            print('E-mail inválido, tente novamente')
            email = input(f'Informe o e-mail novamente: ')
        return email

    @staticmethod
    def altera_telefone_email(agenda, id_fornecedor, index, nova_info_cadastro):
        '''
        Método estático usado para encontrar os telefones e emails dentro das listas que ficam agrupados
        emails e telefones
        :param agenda: agenda com todos os fornecedores cadastrados (self.agenda.fornecedores_SI)
        :param id_fornecedor: Id do fornecedor a ser alterado
        :param index: 1 - telefone, 2- email
        :param nova_info_cadastro: Informação que substituirá  antiga
        :return:
        '''
        if id_fornecedor not in agenda:
            for id_cadastrado, informacoes in agenda.items():
                if type(informacoes) == dict and id_fornecedor in informacoes:
                    total_infos_armaz = len(informacoes[id_fornecedor][index]) + 1
                    if len(informacoes[id_fornecedor][index]) > 1:
                        informacao_substituida = int(input('Qual contato substituir? '
                                                           f'{list(range(1, total_infos_armaz))}'))
                        informacao_substituida -= 1  # Ajusta ao index da lista de telefones
                        informacoes[id_fornecedor][index][informacao_substituida] = nova_info_cadastro
                    else:
                        informacoes[id_fornecedor][index][0] = nova_info_cadastro
        else:
            if type(agenda[id_fornecedor][index]) == list:
                informacao_substituida = int(input('Qual das informações a seguir deseja alterar? '
                                                   f'{list(range(1, len(agenda[id_fornecedor][index]) + 1))}'))
                informacao_substituida -= 1
                agenda[id_fornecedor][index][informacao_substituida] = nova_info_cadastro
            else:
                agenda[id_fornecedor][index] = nova_info_cadastro

    @staticmethod
    def valida_id(id_fornecedor):
        while id_fornecedor.isnumeric() != True:
            print('ID inválido')
            id_fornecedor = input('Informe o ID novamente: ')

        return int(id_fornecedor)

    @staticmethod
    def eh_dicionario(agenda, id_fornecedor):
        '''
        Encontra o fornecedor dentro de grupos e remove-os do mesmo

        :param agenda: agenda completa com todos os fornecedores e grupos
        :param id_fornecedor: ID do fornecedor que será movido
        :return: Todos os dados do fornecedor
        '''
        for chave, valor in agenda.items():
            if type(valor) == dict and id_fornecedor in valor:
                break
        return agenda[chave].pop(id_fornecedor)

    def __init__(self, dados_estruturados):
        self.lista_fornecedores = dados_estruturados
        self.agenda = Agenda()

    def popula_agenda(self):
        '''
        Adiciona os fornecedores já existentes no csv, dentro da nova agenda
        '''
        for i in range(1, len(self.lista_fornecedores) + 1):
            self.agenda.fornecedores_SI[i] = self.lista_fornecedores[i - 1]
            SistemaCadastros.max_cadastro += 1
            SistemaCadastros.identificador += 1

    def visualizar_agenda(self):  # Visualiza a agenda completa
        for chave, valor in self.agenda.fornecedores_SI.items():
            print(chave, valor)


    def cadastra_fornecedor(self):
        '''
        Método que adiciona um novo fornecedor à agenda, passando por algumas validações para evitar
        cadastros errados.
        '''
        if SistemaCadastros.max_cadastro < 75:

            identificador = SistemaCadastros.identificador
            nome = input('Informe o nome do novo fornecedor: ')

            n_contatos = input('quantos numeros de telefone o fornecedor possui: ')
            while n_contatos.isnumeric() != True:
                print('Opção inválida')
                n_contatos = input('quantos numeros de telefone o fornecedor possui: ')

            n_contatos = int(n_contatos)
            telefones = []

            for i in range(1, n_contatos + 1):
                ddd = input('Informe o DDD: ')
                ddd = SistemaCadastros.valida_ddd(ddd)

                numero = input(f'Informe o telefone {i} do fornecedor: ')
                numero = SistemaCadastros.valida_telefone(numero)

                telefone = ddd + numero

                telefones.append(telefone)

            n_emails = input('Informe a quantidade de e-mails que o fornecedor possui: ')
            while n_emails.isnumeric() != True:
                print('Quantidade Inválida')
                n_emails = input('Informe a quantidade de e-mails que o fornecedor possui: ')

            n_emails = int(n_emails)
            emails = []

            for i in range(1, n_emails + 1):
                email = input(f'Informe o e-mail {i} do fornecedor: ')
                email = SistemaCadastros.valida_email(email)

                emails.append(email)

            novo_fornecedor = Fornecedor(identificador, nome, telefones, emails)
            self.agenda.novos_fornecedores.append(novo_fornecedor)

            print('1- Sim\n2- Não')
            opcao_usuario = input('Deseja adicionar o fornecedor a um grupo: ')

            while opcao_usuario != '1' and opcao_usuario != '2':
                print('Opção inválida')
                opcao_usuario = input('Deseja adicionar o fornecedor a um grupo: ')

            if opcao_usuario == '1':
                nome_grupo = input('Informe o nome do grupo: ')
                SistemaCadastros.adiciona_ao_grupo(nome_grupo,
                                                   novo_fornecedor,
                                                   self.agenda.fornecedores_SI)
            else:
                self.agenda.fornecedores_SI[novo_fornecedor.identificador] = [novo_fornecedor.nome,
                                                                              novo_fornecedor.telefone,
                                                                              novo_fornecedor.email]
        else:
            print('Agenda cheia')

    def altera_cadastro(self):
        print('1- Alterar nome'
              '\n2- Alterar telefone'
              '\n3- Alterar email')

        escolha = input('Qual informação deseja alterar: ')

        while escolha != '1' and escolha != '2' and escolha != '3':
            print('Opção inválida')
            escolha = input('Qual informação deseja alterar: ')

        id_fornecedor = input('Informe o ID do fornecedor que deseja alterar: ')
        id_fornecedor = SistemaCadastros.valida_id(id_fornecedor)

        if escolha == '1':
            try:
                novo_nome = input('Informe o novo nome do fornecedor: ')
                for chave, valor in self.agenda.fornecedores_SI.items():
                    if id_fornecedor == chave:
                        valor[0] = novo_nome
                        if id_fornecedor >= 26:
                            self.agenda.novos_fornecedores[id_fornecedor - 26].nome = novo_nome
                    elif type(valor) == dict and id_fornecedor in valor:
                        valor[id_fornecedor][0] = novo_nome
                        self.agenda.novos_fornecedores[id_fornecedor - 26].nome = novo_nome
                print('Realizado com sucesso')
            except:
                print('Usuário não encontrado')
        elif escolha == '2':
            try:
                ddd = input('Informe o novo DDD: ')
                ddd = SistemaCadastros.valida_ddd(ddd)

                numero = input('Informe o novo número: ')
                numero = SistemaCadastros.valida_telefone(numero)

                telefone = ddd + numero

                SistemaCadastros.altera_telefone_email(self.agenda.fornecedores_SI, id_fornecedor,
                                                       1, telefone)
                if id_fornecedor >= 26:
                    self.agenda.novos_fornecedores[id_fornecedor - 26].telefone = telefone
                print('Alteração bem sucedida')
            except:
                print('Usuário não encontrado')
        elif escolha == '3':
            try:
                email = input('Informe o novo e-mail: ')
                email = SistemaCadastros.valida_email(email, )

                SistemaCadastros.altera_telefone_email(self.agenda.fornecedores_SI,
                                                       id_fornecedor,
                                                       2,
                                                       email)
                if id_fornecedor >= 26:
                    self.agenda.novos_fornecedores[id_fornecedor - 26].email = email
                print('Realizado com sucesso')
            except:
                print('Usuário não encontrado')

    def altera_grupo(self):
        '''
        Altera o grupo do usuário ou cria um novo caso o nome do grupo que o usuário passar não exista
        '''
        id_fornecedor = input('Informe o ID do usuário que deseja adicionar em um grupo: ')
        id_fornecedor = SistemaCadastros.valida_id(id_fornecedor)
        nome_grupo = input('Informe o nome do grupo: ')

        try:
            if not id_fornecedor in self.agenda.fornecedores_SI.keys():
                infos = SistemaCadastros.eh_dicionario(self.agenda.fornecedores_SI, id_fornecedor)

                if not nome_grupo in self.agenda.fornecedores_SI.keys():
                    self.agenda.fornecedores_SI[nome_grupo] = {id_fornecedor: infos}
                else:
                    self.agenda.fornecedores_SI[nome_grupo][id_fornecedor] = infos

                print('Usuário Movido')

            else:
                infos = self.agenda.fornecedores_SI.pop(id_fornecedor)

                if not nome_grupo in self.agenda.fornecedores_SI.keys():
                    self.agenda.fornecedores_SI[nome_grupo] = {id_fornecedor: infos}
                else:
                    self.agenda.fornecedores_SI[nome_grupo][id_fornecedor] = infos

                print('Usuário Movido')
        except:
            print('Fornecedor não encontrado')

    def remove_fornecedor(self):
        id_fornecedor = input('Entre com o ID do fornecedor que deseja remover: ')

        id_fornecedor = SistemaCadastros.valida_id(id_fornecedor)

        try:
            if id_fornecedor in self.agenda.fornecedores_SI.keys():
                self.agenda.fornecedores_SI.pop(id_fornecedor)
                print('Fornecedor removido!')
                SistemaCadastros.max_cadastro -= 1

            else:
                SistemaCadastros.eh_dicionario(self.agenda.fornecedores_SI, id_fornecedor)
                print('Fornecedor removido')
                SistemaCadastros.max_cadastro -= 1
        except:
            print('Fornecedor não encontrado')

    def remove_grupo(self):
        print('Esta opção removerá o grupo e tudo que houver dentro dele')
        print('Digite 0 para cancelar')
        nome_grupo = input('Entre com o nome do grupo que deseja remover: ')

        try:
            self.agenda.fornecedores_SI.pop(nome_grupo)
            print('Grupo removido')
        except:
            if nome_grupo == '0':
                print('Cancelado')
            else:
                print('Grupo não encontrado')

    def buscar_contato(self):
        id_fornecedor = input('Informe o ID do fornecedor que deseja buscar: ')

        id_fornecedor = SistemaCadastros.valida_id(id_fornecedor)

        try:
            if not id_fornecedor in self.agenda.fornecedores_SI.keys():
                for chave, valor in self.agenda.fornecedores_SI.items():
                    if type(valor) == dict and id_fornecedor in valor:
                        break
                print(self.agenda.fornecedores_SI[chave][id_fornecedor])
            else:
                print(self.agenda.fornecedores_SI[id_fornecedor])
        except:
            print('Usuário não encontrado')

    def busca_grupo(self):
        nome_grupo = input('Informe o nome do grupo que deseja buscar: ')
        try:
            print(self.agenda.fornecedores_SI[nome_grupo])
        except:
            print('Grupo não encontrado')

    def transforma_csv(self):
        '''
        :return: Retorna um arquivo csv com os elementos da agenda
        '''
        # Gera uma lista de listas para ser transformado em csv

        dados_organizados = []

        for valor in self.agenda.fornecedores_SI.values():
            dados = []

            if type(valor) == list:
                for informacao in valor:
                    # Caso haja mais de um telefone ou email o algoritmo adiciona cada um deles para a
                    #lista dados
                    if type(informacao) == list:
                        for dado in informacao:
                            dados.append(dado)
                    # se não, ele apenas coloca o dado na nova lista
                    else:
                        dados.append(informacao)
                dados_organizados.append(dados)
            # Realiza o mesmo processo do if, porém, para os grupos criados pelo usuário
            else:
                for fornecedor in valor.values():
                    dados = []
                    for informacao in fornecedor:
                        if type(informacao) == list:
                            for dado in informacao:
                                dados.append(dado)
                        else:
                            dados.append(informacao)
                    dados_organizados.append(dados)

        # Transforma em csv
        arquivo = open('fornecedores.csv', 'w')

        escritor = csv.writer(arquivo, delimiter=';', lineterminator='\n')

        escritor.writerows(dados_organizados)
        arquivo.close()

        print('Realizado com êxito')

    def run(self):
        self.popula_agenda()

        print('1- Visualizar agenda completa'
        '\n2- Cadastrar fornecedor'
        '\n3- Alterar cadastro'
        '\n4- Alterar usuario de grupo ou adicionar a um novo grupo'
        '\n5- Remover fornecedor'
        '\n6- Remover grupo'
        '\n7- Buscar fornecedor'
        '\n8- Busca Grupo'
        '\n9- Exportar agenda em .csv'
        '\n0 - Sair')

        escolha = input('Escolha a opção de navegação: ')

        while escolha != '0' and escolha != '1'\
        and escolha != '2' and escolha != '3'\
        and escolha != '4' and escolha != '5'\
        and escolha != '6' and escolha != '7'\
        and escolha != '8' and escolha != '9':
            print('Opção inválida')
            escolha = input('Escolha a opção de navegação: ')

        while escolha != '0':
            if escolha == '1':
                self.visualizar_agenda()
            elif escolha == '2':
                self.cadastra_fornecedor()
            elif escolha == '3':
                self.altera_cadastro()
            elif escolha == '4':
                self.altera_grupo()
            elif escolha == '5':
                self.remove_fornecedor()
            elif escolha == '6':
                self.remove_grupo()
            elif escolha == '7':
                self.buscar_contato()
            elif escolha == '8':
                self.busca_grupo()
            elif escolha == '9':
                self.transforma_csv()
            elif escolha == '0':
                break
            print('===FIM DA OPERAÇÃO===\n')
            print('1- Visualizar agenda completa'
                  '\n2- Cadastrar fornecedor'
                  '\n3- Alterar cadastro'
                  '\n4- Alterar usuario de grupo ou adicionar a um grupo inexistente'
                  '\n5- Remover fornecedor'
                  '\n6- Remover grupo'
                  '\n7- Buscar fornecedor'
                  '\n8- Busca Grupo'
                  '\n9- Exportar agenda em .csv'
                  '\n0 - Sair')
            escolha = input('Escolha a opção de navegação: ')
        print('===FINALIZADO===')
