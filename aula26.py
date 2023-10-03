x = 10

try:
  print(x)
except:
  print('Erro desconhecido')
else:
  print('Tudo certo')
finally:
  print('Fim do tratamento')

#Gerando exceção
num = -10

if(num < 1):
  raise Exception('Valor não permitido')

#Gerando exceção

onlyNumbers = "Bruno"

if not type(onlyNumbers)is int:
  raise Exception("Somento números permitidos")
