#Coleção List

carros = ['HRV', 'Golf', 'Argo', 'Focus']

print(1)
print(-1)

carros.append('Fit') #Adiciona no próximo índice
carros.append('Polo') 

len(carros) #Descobre o tamanho da lista

carros.remove('Golf') #Percorre a lista e quando encontrar remove e reordena
# carros.remove('Gold') #Dará erro pois não temos esse elemento

carros.pop() #Remove o último
del carros[2] #Remove e reordena

print(carros)

carros2 = list(carros) #Recebimento da lista
carros3 = ['Fusca', "147"]

carros4 = carros3 + carros2
print(carros4)