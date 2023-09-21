##Strings e operações com Strings

texto = ' Um texto aleatorio '

print(texto[5]) #Imprime o sexto elemento do array, indíce 5
print(texto[0 : 5]) #Imprime do índice 0 ao índice 5
print("Tamanho: " + str(len(texto)))

arr = [1, 2, 3, 4, 5]
print(str(len(arr))) #Conta o número de elementos
print(str(texto.strip())) #Retira o espaço no início e fim 
print(str(texto.lower())) #Transforma em minúsculo

curso = 'Curso de Python'

cursoJS = curso.replace('Python', 'JS') #Substitui um termo por outro
arr = curso.split('') #Cria um array em que a posição é delimitada pelo caracter dado como parâmetro
print(cursoJS)



