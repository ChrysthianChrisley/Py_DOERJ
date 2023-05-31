import base64

def encode():
    
    ano = '2023'
    mes = '05'
    dia = '31'

    data = ano+mes+dia

    data64 = base64.b64encode(data.encode('utf-8')).decode('utf-8')

    return data64
