#Funções com argumentos

def somarComParametros(num1, num2):
  print('Soma de 2 números = ' + str(num1 + num2))

somarComParametros(10, 20)

#Funções com argumentos arbitrados

def textos(*txt):
  for t in txt:
    print(t)

textos('texto1', 'texto2', 'texto3', 'texto4', 'texto5')

#Funções com argumentos arbitrados devem estar no final

def numeros(n1, *outrosNumeros):
  print(n1,"Esse é o primeiro")
  for outros in outrosNumeros:
    print(outros)

numeros(1, 2, 3, 4, 5)

#Funções com valores padrão

def carros(modelo = "Gol"):
  print("modelo: ", modelo)

carros("HB20")
carros()