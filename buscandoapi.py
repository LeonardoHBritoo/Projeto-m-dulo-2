import requests
import json
def Buscar_dados_API():
    '''
    Busca os dados em uma API json server
    '''
    dicionario = { 
                "ID_Cliente":[],
                "idade":[],
                "sexo":[],
                "escolaridade":[],
                "estado":[],
                "valor_compra":[]
             }
    for i in dicionario:
        dicionario[i] = requests.get(f'http://localhost:3000/{i}').json()
    
    with open('Teste.json','w') as arquivo:
            arquivo.write(json.dumps(dicionario)) 
