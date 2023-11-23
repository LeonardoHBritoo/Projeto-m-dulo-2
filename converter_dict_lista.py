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
dicionario = {  'ID_Cliente':[1,2,3,4,5,6,7],
                'idade':[18,19,20,21,22,23,25],
                'sexo':['M','F','M','F','M','F','M'],
                'escolaridade':['Ensino fundamental','Ensino médio','Ensino Superior',
                                'Ensino médio','Ensino médio', 'Ensino Superior', 'Ensino Superior'],
                'estado':['SP','MG','RN','SP','RJ','SP','SP'],
                'valor_compra':[100.0,200.0,300.0,400.0,500.0,600.0,600.0]
             }
print(converter_dict_lista(dicionario))