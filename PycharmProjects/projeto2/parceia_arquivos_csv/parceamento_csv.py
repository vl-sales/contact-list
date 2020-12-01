def eh_nome(arquivo):
    nomes = []
    for linha in arquivo:
        for elemento in linha:
            if elemento.isalpha() == True:
                nomes.append(elemento)
    return nomes

def eh_email(arquivo):
    emails = []
    for linha in arquivo:
        for elemento in linha:
            if '@' in elemento:
                emails.append(elemento)
    return emails

def eh_telefone(arquivo):
    telefones = []
    for linha in arquivo:
        for elemento in linha:
            if elemento.isnumeric() == True:
                telefones.append(elemento)
    return telefones

def parceia_csv(arquivo):
    telefones = eh_telefone(arquivo)
    nomes = eh_nome(arquivo)
    emails = eh_email(arquivo)

    dados_estruturados = []

    for i in range(len(telefones)):
        dados_estruturados.append([nomes[i], telefones[i], emails[i]])

    return dados_estruturados