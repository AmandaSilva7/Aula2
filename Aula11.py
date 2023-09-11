'''#criar classe
class Computador:
    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video

    def Exibirinformacoes(self):    
        print(self.marca, self.memoria_ram, self.placa_de_video)

def Desligar(self):
    print('estou desligando')        

#criar objeto

computador1 = Computador('Asus', '16gb', 'Samsung')
computador1.Exibirinformacoes()
computador1.Desligar()


'''

#Desafio

# classe chamada automoveis com os parametros = marca, ano
# objetos, locadora1, locadora2 e imprima valores marca, ano




class Automoveis:
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano

    
    def Exibirinformacoes(self):    
        print(self.marca, self.ano)

    def Desligar(self):
        print('estou desligando')    
    

locadora1 = Automoveis('Fusca', '1990')    
locadora1.Exibirinformacoes()
locadora1.Desligar()


locadora2 = Automoveis('Gol', '2010')        
print(locadora2.marca, locadora2.ano)



