class NPC: #Base, Pai, Super
    def __init(self, nome, time, forca, municao):
        self.nome = nome
        self.time = time
        self.forca = forca
        self.municao = municao
        self.vivo = True
        self.energia = 100
    
    def info(self):
        print("Nome: " + str(self.nome))
        print("Time: " + str(self.nome))
        print("Força: " + str(self.nome))
        print("Munição: " + str(self.nome))

    