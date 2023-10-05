import os

carros = []

class Carro:
    nome = ''
    potencia = 0
    velocidadeMaxima = 0
    ligado = False

    def __init__(self, nome, potencia):
        self.nome = nome
        self.potencia = potencia
        self.velocidadeMaxima = int(potencia) * 2
        self.ligado = False

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def info(self):
        print('Nome:...' + self.nome)
        print('Potência:...' + str(self.potencia))
        print('Velocidade Máxima:...' + str(self.velocidadeMaxima))
        print('Ligado:...' + str( 'sim' if self.ligado else 'não'))

def menu():
    os.system('cls') or None
    print('1 - Novo Carro')
    print('2 - Informações do carro') 
    print('3 - Excluir o carro')
    print('4 - Ligar o carro')
    print('5 - Desligar o carro')
    print('6 - Listar o carro')
    print('7 - Sair')
    print('8 - Quantidade de carros' + str(len(carros)))
    opcao = input('Digite uma opção: ')
    return opcao

def novoCarro():
    os.system('cls') or None
    nome = input('Nome do Carro....')
    potencia = input('Potência do Carro....')
    carro = Carro(nome, potencia)
    carros.append(carro)
    print('Novo carro criado')
    os.system('pause')

def informacoes():
    os.system('cls') or None
    numeroCarro = int(input('Informe o número do carro que deseja ter as informações:....'))
    try:
        carros[numeroCarro].info()
    except:
        print('O carro não existe na lista')
    os.system('pause')

def excluirCarro():
    os.system('cls') or None
    numeroCarroExcluir = int(input('Informe o número do carro que deseja excluir:....'))
    try:
        del carros[numeroCarroExcluir]
        print('Carro Excluído')
    except:
        print('O carro não existe na lista')
    os.system('pause')

def ligarCarro():
    os.system('cls') or None
    numeroCarroLigar = int(input('Informe o número do carro que deseja ligar:....'))
    try:
        carros[numeroCarroLigar].ligar()
        print('Carro Ligado')
    except:
        print('O carro não existe na lista')
    os.system('pause')

def desligarCarro():
    os.system('cls') or None
    numeroCarroDesligar = int(input('Informe o número do carro que deseja desligar:....'))
    try:
        carros[numeroCarroDesligar].ligar()
        print('Carro Desligado')
    except:
        print('O carro não existe na lista')
    os.system('pause')

def listarCarros():
    os.system('cls') or None
    p = 0
    for c in carros:
        print(str(p) + ' - ' + c.nome)
        p += 1
    os.system('pause')