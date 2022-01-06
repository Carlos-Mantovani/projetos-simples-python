import random
import PySimpleGUI as sg

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        # layout
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('sim'), sg.Button('nao')]
        ]

    def Iniciar(self):
        # janela
        self.janela = sg.Window('Simulador de Dado', self.layout)
        # ler os valores da tela
        self.eventos, self.valores = self.janela.Read()
        # fazer alguma coisa com os valores
        try:
            if self.eventos == 'sim' or self.eventos == 's':
                self.RolaDado()
            elif self.eventos == 'nao' or self.eventos == 'n':
                print('Finalizando o programa')
            else:
                print('Digite "sim" ou "nao"')
        except:
            print('Ocorreu um erro ao receber sua resposta')

    def RolaDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))

simulador_de_dado = SimuladorDeDado()
simulador_de_dado.Iniciar()