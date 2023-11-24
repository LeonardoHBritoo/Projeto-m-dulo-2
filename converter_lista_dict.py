
def converter_lista_dict(lista_de_dicionarios:list):
    ''' Função para converter a estrutura dos dados, caso necessário
        De: lista de dicionários - Para: dicionário de listas
    '''
    chaves = list(lista_de_dicionarios[0].keys()) # Pegando a lista de chaves
    dicionario = {chave: [] for chave in chaves} # Inicializando dicionário
    for dicionario_atual in lista_de_dicionarios:
        for chave in chaves:
            dicionario[chave].append(dicionario_atual[chave]) # Adicionando elementos
    return dicionario
