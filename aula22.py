#lambda args:expr
# São funções simples, já tem o return incorporado 
soma = lambda a, b: a + b

print(soma(1, 2))

#Pode-se executar a função sem associar a nada
(lambda a,b: a + b)(3, 4)

#Pode-se utilizar funções como argumentos
r = lambda x,y: x + y(x)

res = r(2, lambda x: x * x)

print(res)