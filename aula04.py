a = 1 #int
b = 1.5 #float
c = 'txt'
d = True #bool
g = complex(5, 2) #Número complexo
g = complex(0, 1j) #Número complexo
h = [1, 2, 3, 4, 5, 'text', True] #Lista ou Array
i = ("Carro", "Aviao,", True) #Os elementos dõ tupla não podem ser modificados nem inseridos
j = range(0, 100, 2) #Cria uma lista de 0 a 100 com valor múltiplo de 2
#Existe uma função nativa para a verificção de tipo, type()
k = {
    "canal": "CFB",
    "curso": "Curso de Python",
    "nome": "Bruno"
}
l = {5, 7, 4, 5, 7, 8} #Tipo set (Não repete valores)
m = frozenset({5,7,4,5,8,7}) #Tipo set congelado, sem poder ser modificado
print(type(a), type(b), type(c), type(d), str(a), g.real, g.imag, j[2], k["canal"])