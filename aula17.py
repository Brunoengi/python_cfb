carro = {
  "Fabricante": "Honda",
  "Modelo": "HRV",
  "Ano": "2016",
  "Cor": "Prata"
}

#Adicionando chave, valor
carro["Estado"] = "Conservado"
carro["Cambio"] = "Automático"

#Removendo chave, valor
del carro["Estado"]
carro.pop("Cambio")

#Equivalente
print(carro['Fabricante'])
print(carro.get("Fabricante"))

for x in carro:
  print(x) #Percorrendo as chaves
  print(carro[x]) #Percorrendo os valores

#carro.items() retorna um array em que cada posição tem um array em que a primeira posição é a chave e o segundo é o valor
for chave, valor in carro.items():
  print(chave, valor)

if "Modelo" in carro:
  print("Modelo é uma chave")

  #Pode-se acessar o lenght de um dicionário que será o número de conjuntos (chave, valor)
  print(len(carro))

  """Sobre o del e pop() é a seguinte:

pop( ) = deleta provisoriamente o item, mas, se quiser pode chamá-lo de volta no comando print( )
del = deleta permanentemente o item e não é possível chamá-lo de volta no comando print( )

as vezes podemos usar a função pop( ) para mostrar qual foi o item deletado de uma lista / Dictionary"""