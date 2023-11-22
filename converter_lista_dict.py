def converter_lista_dict(lista_de_dicionarios):
    chaves = list(lista_de_dicionarios[0].keys())
    dicionario = {chave: [] for chave in chaves}
    for dicionario_atual in lista_de_dicionarios:
        for chave in chaves:
            dicionario[chave].append(dicionario_atual[chave])
    
    return dicionario

lista_de_dicionarios = [
    {'ID_Cliente': 1, 'idade': 18, 'sexo': 'M', 'escolaridade': 'Ensino fundamental', 'estado': 'SP', 'valor_compra': 100.0},
    {'ID_Cliente': 2, 'idade': 19, 'sexo': 'F', 'escolaridade': 'Ensino médio', 'estado': 'MG', 'valor_compra': 200.0},
    {'ID_Cliente': 3, 'idade': 20, 'sexo': 'M', 'escolaridade': 'Ensino Superior', 'estado': 'RN', 'valor_compra': 300.0},
    {'ID_Cliente': 4, 'idade': 21, 'sexo': 'F', 'escolaridade': 'Ensino médio', 'estado': 'SP', 'valor_compra': 400.0},
    {'ID_Cliente': 5, 'idade': 22, 'sexo': 'M', 'escolaridade': 'Ensino médio', 'estado': 'RJ', 'valor_compra': 500.0},
    {'ID_Cliente': 6, 'idade': 23, 'sexo': 'F', 'escolaridade': 'Ensino Superior', 'estado': 'SP', 'valor_compra': 600.0},
    {'ID_Cliente': 7, 'idade': 25, 'sexo': 'M', 'escolaridade': 'Ensino Superior', 'estado': 'SP', 'valor_compra': 600.0}
]

dicionario = converter_lista_dict(lista_de_dicionarios)
print(dicionario)