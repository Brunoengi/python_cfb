num_int = 10
num_float = 5.2
num_complexo = 1j

x = num_int

#Conversão para string
print("Valor:" + str(x) + " Tipo: " + str(type(x)))

#Conversao de inteiro para float
num2_float = float(num_int)

#Conversão de inteiro para float
num2_int = int(num_float) ## Saída: 5

#Trabalhando com números aleatórios
import random

#Número inteiro aleatório entre 0 e 59
num_random = random.randrange(0, 59)