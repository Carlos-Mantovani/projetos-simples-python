import random
import PySimpleGUI as sg

class ChutaNumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.venceu = False

    def Iniciar(self):
        layout = [
            [sg.Text('Seu Chute',size=(39,0))],
            [sg.Input(size=(18,0),key='ValorChute')],
            [sg.Button('Chutar')],
            [sg.Output(size=(39,10))]
        ]
        self.janela = sg.Window('Chute o número!',layout=layout)
        self.GerarNumeroAleatorio()
        try:
            while True:
                self.evento, self.valores = self.janela.Read()
                if self.evento == 'Chutar':
                    self.chute = int(self.valores['ValorChute'])
                    while self.venceu == False:
                        if self.chute > self.valor_aleatorio:
                            print('O número secreto é menor')
                            break
                        elif self.chute < self.valor_aleatorio:
                            print('O número secreto é maior')
                            break
                        if self.chute == self.valor_aleatorio:
                            self.venceu = True
                            print('Você venceu!')
                            break
        except:
            self.janela.close()
            self.Iniciar()

    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo, self.valor_maximo)

chute_o_numero = ChutaNumero()
chute_o_numero.Iniciar()
