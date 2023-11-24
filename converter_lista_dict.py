
def converter_lista_dict(lista_de_dicionarios:list):
    ''' Função para converter a estrutura dos dados, caso necessário
        De: lista de dicionários - Para: dicionário de listas
    '''
    chaves = list(lista_de_dicionarios[0].keys())
    dicionario = {chave: [] for chave in chaves}
    for dicionario_atual in lista_de_dicionarios:
        for chave in chaves:
            dicionario[chave].append(dicionario_atual[chave])
    return dicionario
