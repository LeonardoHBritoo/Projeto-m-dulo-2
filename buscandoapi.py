import requests
def Buscar_dados_API():
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
