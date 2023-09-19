curso = 'Curso de Python'

#Ambos são case sensitive
res = "Python" in curso #Verifica se tem Python na string contida na variável curso, retorna True ou False
res2 = 'JS' not in curso #Retorna true se não achar e False se achar 

print(res)

#String format
dia = 15
mes = 'setembro'

data = "{dia} de {mes}".format(dia = dia, mes = mes)

print(data)