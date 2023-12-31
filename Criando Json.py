import json
def criar_json():
  '''
  Cadastro de clientes: ID_Cliente, idade, sexo, escolaridade, estado, valor_compra
  Aqui é criado o banco de dados para o Json Server
  '''
  dicionario = {  "ID_Cliente":[1,2,3,4,5,6,7],
                  "idade":[18,19,20,21,22,23,25],
                  "sexo":["M","F","M","F","M","F","M"],
                  "escolaridade":["Ensino fundamental","Ensino médio","Ensino Superior",
                                  "Ensino médio","Ensino médio", "Ensino Superior", "Ensino Superior"],
                  "estado":["SP","MG","RN","SP","RJ","SP","SP"],
                  'valor_compra':[100.0,200.0,300.0,400.0,500.0,600.0,600.0]
              }
  with open('Teste.json', 'w') as arq:
    arq.write(json.dumps(dicionario))

criar_json()  
