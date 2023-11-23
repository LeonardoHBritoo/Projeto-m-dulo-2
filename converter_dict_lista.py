def converter_dict_lista(dicionario):
    chaves = list(dicionario.keys())
    num_elementos = len(dicionario[chaves[0]])
    lista_de_dicionarios = []
    for i in range(num_elementos):
        novo_dicionario = {}
        for chave in chaves:
            novo_dicionario[chave] = dicionario[chave][i]
        lista_de_dicionarios.append(novo_dicionario)
    
    return lista_de_dicionarios