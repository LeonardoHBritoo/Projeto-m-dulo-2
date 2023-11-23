import json
from functools import reduce
def ler_json():
    try:
         with open('Teste.json', 'r') as arquivo:
            dados_json = json.load(arquivo)
            return dados_json
    except FileNotFoundError:
        print('Arquivo de inicial não encontrado')

def adicionar_cliente(clientes):
    try:
        clientes['ID_Cliente'].append(clientes['ID_Cliente'][-1]+1) # Incremento automático do id
        clientes['idade'].append(int(input('Digite a idade: ')))
        clientes['sexo'].append(input('Digite o sexo: '))
        clientes['escolaridade'].append( input('Digite a escolaridade: '))   
        clientes['estado'].append(input('Digite o estado: '))
        clientes['valor_compra'].append(float(input('Digite o valor_compra: ')))
        with open('Teste.json', 'w') as arquivo:
            arquivo.write(json.dumps(clientes))
        return clientes
    except TypeError:
        print('Uma das entradas foi de tipo errado, dados não registrados')

def listar_clientes(clientes):
    try:
        for iteracao in range(len(clientes['ID_Cliente'])):
            for chave in clientes:
                print(f'{chave} : {clientes[chave][iteracao]}',end='  ')
            print()
    except TypeError:
        print('Base de dados não encontrada')

def buscar_cliente(clientes):
   try:
    id_buscado = int(input('Digite o ID do cliente '))
    indice = clientes['ID_Cliente'].index(id_buscado)# Repete, então talvez criar função
    for chave in clientes:
        print(clientes[chave][indice], end='  ')
   except ValueError:
       print('Cliente não encontrado')
       

def atualizar_cliente(clientes):
    try:
        listar_clientes(clientes)
        id = int(input('Digite o ID do cliente que deseja atualizar '))
        indice = clientes['ID_Cliente'].index(id) # Repete, então talvez criar função
        dicionario_chaves = {i:j for i,j in zip(range(len(clientes.keys())),clientes.keys())}
        dicionario_chaves.pop(0)
        chave = dicionario_chaves[int(input(f'O que deseja alterar?\n{dicionario_chaves}\n'))]
        alteracao = input(f'Digite o novo valor de {chave} ')
        if type(clientes[chave][-1]) == int:
            alteracao = int(alteracao)
        if type(clientes[chave][-1]) == float:
            alteracao = float(alteracao)
        clientes[chave][indice] = alteracao
        with open('Teste.json','w') as arquivo:
            arquivo.write(json.dumps(clientes))
        return clientes
    except ValueError:    
        print('Cliente não cadastrado')
def deletar_cliente(clientes):
    try:
        listar_clientes(clientes)
        id = int(input('Digite o ID do cliente que deseja deletar '))
        indice = clientes['ID_Cliente'].index(id)
        for i in clientes:
            clientes[i].pop(indice)
        listar_clientes(clientes)
        return clientes
    except ValueError:
        print('Cliente não está presente na base')


def ticket_max_min(clientes, maximo = True):
    if maximo:
        valor_maximo = reduce(lambda x,y: x if x > y else y , clientes['valor_compra'],clientes['valor_compra'][0])
        return [(i,j) for i,j in zip(clientes['ID_Cliente'],clientes['valor_compra']) if j == valor_maximo]
    else:
        valor_minimo = reduce(lambda x,y: x if x < y else y , clientes['valor_compra'],clientes['valor_compra'][0])
        return [(i,j) for i,j in zip(clientes['ID_Cliente'],clientes['valor_compra']) if j == valor_minimo]
def dados_estatisticos(clientes:dict, agregador:str='sexo' ,agregado:str='idade'):

    lista_agregador = list(set(clientes[agregador]))
    lista_de_clientes = []
    dicionario_agregado = {}
    lista_agregada =[]
    for indice in range(len(clientes['ID_Cliente'])):
        lista_intermediaria = []
        for chave in clientes:
            lista_intermediaria.append(clientes[chave][indice])
        lista_de_clientes.append(lista_intermediaria)
    for item in lista_agregador:
        lista_agregada = list(map(lambda x :x [list(clientes.keys()).index(agregado)],(filter(lambda x:item in x,lista_de_clientes))))
        dicionario_agregado[item] = lista_agregada
    media =  calcula_media(dicionario_agregado)
    moda =  calcula_moda(dicionario_agregado)
    mediana = calcula_mediana(dicionario_agregado)  
    
    with open('Dados_Estatisticos.csv', 'w') as arq:
        arq.write(f'media; moda; mediana\n{media}; {moda}; {mediana}')
def calcula_media(dicionario_agregado):
    return {chave : sum(dicionario_agregado[chave])/len(dicionario_agregado[chave]) for chave in dicionario_agregado}

def calcula_moda(dicionario_agregado):
    for i in dicionario_agregado:
        dicionario_moda = {}
        for j in dicionario_agregado[i]:
            if j not in dicionario_moda:
                dicionario_moda[j]= 1 
            else:
                dicionario_moda[j] += 1
        dicionario_agregado[i] = list(max(list(dicionario_moda.items())))[0]
        return dicionario_agregado
        
    
def calcula_mediana(dicionario_agregado):
    for chave in dicionario_agregado:
        if not isinstance(dicionario_agregado[chave],list):
            dicionario_agregado[chave] = list([dicionario_agregado[chave]])
    return  {chave:(sorted(dicionario_agregado[chave])[len(dicionario_agregado[chave]) // 2] +                             \
                    sorted(dicionario_agregado[chave])[(len(dicionario_agregado[chave]) - 1) // 2])/                       \
                    2 for chave in dicionario_agregado if len(dicionario_agregado[chave]) > 0 }


clientes = ler_json()

# clientes = adicionar_cliente(clientes)
# print(clientes)
# listar_clientes(clientes)
# buscar_cliente(clientes)
# atualizar_cliente(clientes)
# deletar_cliente(clientes)
# print(ticket_max_min(clientes, maximo=False))
# dados_estatisticos(clientes, agregador='estado' ,agregado='valor_compra')