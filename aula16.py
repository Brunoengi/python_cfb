##List

carros = ['HRV', 'Golf', 'Focus', 'Argo']

for x in carros:
  print(x)

#Matrizes

matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

for l,c,k in matriz: #Por ser uma matriz com 3 elementos por linha, precisa de 3 variáveis para acessar todos os elementos
  print(str(l)+ '+' + str(c) + '+' + str(k))

print(matriz[1][2])