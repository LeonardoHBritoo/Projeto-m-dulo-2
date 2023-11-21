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
    # Falta fazer lógica da lista de tuplas para valores iguais
    if maximo:
        return reduce(lambda x,y: x if x > y else y , clientes['valor_compra'],clientes['valor_compra'][0])
    else:
        return reduce(lambda x,y: x if x < y else y , clientes['valor_compra'],clientes['valor_compra'][0])

def dados_estatisticos(clientes:dict, agregador:str ,valor):
    # Aqui precisa ter:
    # Média, moda e mediana
    # map, filter e reduce
    # Usar List comprehension
    # Salvar como CSV
    pass


clientes = ler_json()

# clientes = adicionar_cliente(clientes)
# print(clientes)
# listar_clientes(clientes)
# buscar_cliente(clientes)
# atualizar_cliente(clientes)
# deletar_cliente(clientes)
# print(ticket_max_min(clientes))
