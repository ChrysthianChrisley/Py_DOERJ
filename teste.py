import base64


data = '20230531'

data64 = base64.b64encode(data.encode('utf-8')).decode('utf-8')

print(data64)