# Importando bibliotecas necessárias
import json
from functools import reduce
import time
import os
from buscandoapi import Buscar_dados_API
def ler_json() -> None:
    '''
    Busca os dados do arquivo Json adquirido através da API
    
    '''
    try:
         with open('Teste.json', 'r') as arquivo:
            dados_json = json.load(arquivo)
            return dados_json
    except FileNotFoundError:
        print('Arquivo de inicial não encontrado')

def adicionar_cliente(clientes:dict) -> dict:
    '''
    Adiciona informações a Base, salvando em arquivo Json
    '''
    try:
        clientes['ID_Cliente'].append(clientes['ID_Cliente'][-1]+1) # Incremento automático do id
        clientes['idade'].append(int(input('Digite a idade: ')))
        clientes['sexo'].append(input('Digite o sexo: '))
        clientes['escolaridade'].append( input('Digite a escolaridade: '))   
        clientes['estado'].append(input('Digite o estado: '))
        clientes['valor_compra'].append(float(input('Digite o valor_compra: ')))
        with open('Teste.json', 'w') as arquivo:
            arquivo.write(json.dumps(clientes))
        print('Operação concluída')
        return clientes
    except TypeError:
        print('Uma das entradas foi de tipo errado, dados não registrados')

def listar_clientes(clientes:dict) -> None:
    '''
    Lista os clientes da Base 
    '''
    try:
        for iteracao in range(len(clientes['ID_Cliente'])): # Acha o tamanho da lista de clientes com base no ID
            for chave in clientes:
                print(f'{chave} : {clientes[chave][iteracao]}',end='  ')
            print()
    except TypeError:
        print('Base de dados não encontrada')

def buscar_cliente(clientes:dict) -> dict:
   '''
   Busca clientes com base no ID 
   '''
   try:
    id_buscado = int(input('Digite o ID do cliente '))
    indice = clientes['ID_Cliente'].index(id_buscado)
    for chave in clientes:
        print(clientes[chave][indice], end='  ')
    print()
   except ValueError:
       print('Cliente não encontrado')
       
def atualizar_cliente(clientes:dict) -> dict:
    '''
    Atualiza um cliente da base de dados e salva em arquivo Json com informações mais recentes
    '''
    try:
        listar_clientes(clientes)
        id = int(input('Digite o ID do cliente que deseja atualizar '))
        indice = clientes['ID_Cliente'].index(id) 
        dicionario_chaves = {i:j for i,j in zip(range(len(clientes.keys())),clientes.keys())}
        dicionario_chaves.pop(0)
        chave = dicionario_chaves[int(input(f'O que deseja alterar?\n{dicionario_chaves}\n'))]
        alteracao = input(f'Digite o novo valor de {chave} ')
        if type(clientes[chave][-1]) == int: # Verifica tipo do elemento anterior para coerção do input
            alteracao = int(alteracao)
        if type(clientes[chave][-1]) == float:# Verifica tipo do elemento anterior para coerção do input
            alteracao = float(alteracao)
        clientes[chave][indice] = alteracao
        with open('Teste.json','w') as arquivo:
            arquivo.write(json.dumps(clientes))
        print('Operação concluída')
        return clientes
    except ValueError:    
        print('Cliente não cadastrado')

def deletar_cliente(clientes:dict) -> dict:
    '''
    Deleta um cliente a partir do ID e salva informações mais recentes na base
    '''
    try:
        listar_clientes(clientes)
        id = int(input('Digite o ID do cliente que deseja deletar '))
        indice = clientes['ID_Cliente'].index(id)
        for i in clientes:
            clientes[i].pop(indice)
        print('Operação concluída')
        with open('Teste.json', 'w') as arquivo:
            arquivo.write(json.dumps(clientes))
        return clientes
    except ValueError:
        print('Cliente não está presente na base')


def ticket_max_min(clientes:dict, maximo:bool = True) -> list:
    '''
    A função recebe a base de clientes e um booleano que indica qual operação deve ser realizada:

    1)Buscar os maiores tickets
    2)Buscar os menores tickets

    retorna os uma tupla de (ID_Cliente,valor_compra)
    '''
    if maximo:
        valor_maximo = reduce(lambda x,y: x if x > y else y , clientes['valor_compra'],clientes['valor_compra'][0])
        return [(i,j) for i,j in zip(clientes['ID_Cliente'],clientes['valor_compra']) if j == valor_maximo]
    else:
        valor_minimo = reduce(lambda x,y: x if x < y else y , clientes['valor_compra'],clientes['valor_compra'][0])
        return [(i,j) for i,j in zip(clientes['ID_Cliente'],clientes['valor_compra']) if j == valor_minimo]
    
def dados_estatisticos(clientes:dict, agregador:str='sexo' ,agregado:str='idade') -> None:
    '''
    Recebe um a base, um valor agregador e um agregado e salva as estatísticas de média,moda e mediana em
    um arquivo CSV que pode ser interpretado como uma tabela das estatísticas para o valor agregado pelo 
    valor agregador.
    exemplo: tabela de média,moda e mediana da idade (agregado) em relação ao sexo(agregador)
    '''
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
    string = f'{agregador}, media de {agregado}, moda de {agregado}, mediana de {agregado}\n'
    for item in lista_agregador:
        string+=f'{item}, {media[item]}, {moda[item][0]}, {mediana[item]}\n'
    print(string)
    with open('Dados_Estatisticos.csv', 'w') as arq:
        arq.write(string)
    print('Arquivo csv com os dados estatísticos foi gerado')

def calcula_media(dicionario_agregado:dict) -> dict:
    '''
    Calcula a para cada chave do dicionário
    '''
    return {chave : sum(dicionario_agregado[chave])/len(dicionario_agregado[chave]) for chave in dicionario_agregado}

def calcula_moda(dicionario_agregado:dict) -> dict:
    '''
    Calcula a moda para cada chave do dicionário
    '''
    for i in dicionario_agregado:
        dicionario_moda = {}
        for j in dicionario_agregado[i]:
            if j not in dicionario_moda:
                dicionario_moda[j]= 1 
            else:
                dicionario_moda[j] += 1
        dicionario_agregado[i] = list(max(list(dicionario_moda.items())))[0]
    return dicionario_agregado
        
def calcula_mediana(dicionario_agregado:dict) -> dict:
    '''
    Calcula a mediana para cada chave do dicionário
    '''
    for chave in dicionario_agregado:
        if not isinstance(dicionario_agregado[chave],list):
            dicionario_agregado[chave] = list([dicionario_agregado[chave]])
    return  {chave:(sorted(dicionario_agregado[chave])[len(dicionario_agregado[chave]) // 2] +                             \
                    sorted(dicionario_agregado[chave])[(len(dicionario_agregado[chave]) - 1) // 2])/                       \
                    2 for chave in dicionario_agregado if len(dicionario_agregado[chave]) > 0 }

def main()-> None:
    '''
    Função principal que inicializa todas as outras
    '''
    Buscar_dados_API()
    clientes = ler_json()
    entrada = 'inicio'
    while entrada:
        if entrada != 'inicio':
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
        entrada = input(""" Escolha uma das operações:
                            1) Adicionar cliente
                            2) Listar clientes
                            3) Buscar cliente
                            4) Atualizar cliente
                            5) Deletar cliente
                            6) Ticket mínimo ou máximo entre os clientes
                            7) Dados estatísticos 
                            0) Sair
                        * Digite o número correspondente:
        """)
        
        if  entrada=='1' :
            clientes = adicionar_cliente(clientes)
        elif entrada=='2':
            listar_clientes(clientes)
        elif entrada=='3':
            buscar_cliente(clientes)
        elif entrada=='4':
            clientes = atualizar_cliente(clientes)
        elif entrada=='5':
            clientes = deletar_cliente(clientes)
        elif entrada=='6':
            resposta = input("""
                  Escolha o ticket que deseja obter:
                    1) Máximo
                    2) Mínimo

                  """)
            if resposta == '1':
                print(ticket_max_min(clientes, maximo=True))
            elif resposta =='2':
                print(ticket_max_min(clientes, maximo=False))
            else:
                print('Entrada inválida')
        elif entrada=='7':
           agregador = input('Digite o valor agregador ')
           agregado = input('Digite o valor agregado ')
           dados_estatisticos(clientes, agregador ,agregado)
        elif entrada=='0':
            print('Programa encerrado')
            entrada = ''
        else:
            print('Valor digitado é inválido')
            continue
        
main()
