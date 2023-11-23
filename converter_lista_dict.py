def converter_lista_dict(lista_de_dicionarios):
    chaves = list(lista_de_dicionarios[0].keys())
    dicionario = {chave: [] for chave in chaves}
    for dicionario_atual in lista_de_dicionarios:
        for chave in chaves:
            dicionario[chave].append(dicionario_atual[chave])
            
    return dicionario