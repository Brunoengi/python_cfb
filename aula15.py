#Lista
l_carros = ['HRB', 'Golf', 'Argo']

for x in l_carros:
  print(x)

#Tupla Não suporta adição ou modificação de itens diretamente na tupla
t_carros = ('HRB', 'Golf', 'Argo')

#É possível converter a variável de tupla para lista
t_carros = list(t_carros) #Agora é uma list
t_carros = tuple(t_carros) #Agora é uma tupla
