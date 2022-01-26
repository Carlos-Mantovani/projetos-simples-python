import random

class ChutaNumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentativas = 3
        self.venceu = False

    def Iniciar(self):
        self.tentativas = 3
        self.GerarNumeroAleatorio()
        self.PedirValorChute()
        while self.tentativas > 1:
            if self.chute > self.valor_aleatorio:
                print('O número secreto é menor')
                self.tentativas -= 1
                self.PedirValorChute()
            elif self.chute < self.valor_aleatorio:
                print('O número secreto é maior')
                self.tentativas -= 1
                self.PedirValorChute()
            else:
                print('Você venceu!')
                self.venceu = True
                self.ReiniciarJogo()
        self.ReiniciarJogo()

    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo, self.valor_maximo)

    def PedirValorChute(self):
        self.chute = int(input('Chute um número: '))

    def ReiniciarJogo(self):
        resposta = input('Deseja jogar novamente? (sim) (nao): ')
        if resposta == 'sim':
            self.Iniciar()
        else:
            pass

chute_o_numero = ChutaNumero()

chute_o_numero.Iniciar()
