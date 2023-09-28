class Carro:
    velMax = 0
    ligado = False
    cor = ""

    def __init__(self, vm, li, c):
        self.velMax = vm
        self.ligado = li
        self.cor = c
    
    def mostrar(self):
        print(self.velMax)
        print(self.ligado)
        print(self.cor)

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False
        
c1 = Carro(200, False, 'Preto')

c1.mostrar()