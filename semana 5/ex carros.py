class Carro:
    def __init__(self):
        self.ligado = False
        self.cor = None
        self.modelo = None
        self.velocidade = 0
    
    def ligar(self):
        self.ligado = True
        print('Carro ligado.')

    def desligar(self):
        self.ligado = False
        print('Carro desligado.')

    def aumentarVelocidade(self):
        if self.ligado == True:
            self.velocidade += 10
            print(f'O carro está andando a {self.velocidade}km/h.')
        else:
            print('O carro está desligado. Ligue o carro primeiro.')
    
    def diminuirVelocidade(self):
        if self.ligado == True:
            if self.velocidade != 0:
                self.velocidade -= 0
                print(f'O carro está andando a {self.velocidade}km/h.')
            else:
                print('A velocidade já é 0km/h. O carro está parado.')
        else:
            print('O carro está desligado. Ligue o carro primeiro.')


novo = Carro()
novo.cor = 'azul'
novo.modelo = 'top 2025'
novo.ligar()
novo.aumentarVelocidade()
novo.aumentarVelocidade()