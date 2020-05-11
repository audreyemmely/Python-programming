#Chute o numero
#O algoritmo gera um valor aleatorio e o usuario tem que tentar adivinhar o numero, ate acertar
from random import randrange
import PySimpleGUI as sg

class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = randrange(101)
        self.tentar_novamente = True

    def Iniciar(self):
        layout = [
            [sg.Text('Seu chute: ', size=(20,0))],
            [sg.Input(size(18,0),key='ValorChute')],
            [sg.Button('Chutar!')],
            [sg.Output(size=(30,10))]
        ]

    self.janela = sg.Window('Chute o numero!', layout = layout)
    self.GerarNumeroAleatorio()
    try:
        while True:
            self.evento, self.valores = self.janela.Read()
            if self,evento == 'Chutar!':
                self.valor_do_chute = self.valores['ValorChute']
                while self.tentar_novamente == True:
                    if int(self.valor_do_chute) > self.valor_aleatorio:
                        print('Chute um valor mais baixo!')
                        break
                    elif int(self.valor_do_chute) < self.valor_aleatorio:
                        print('Chute um valor mais alto!')
                        break
                    if int(self.valor_do_chute) == self.valor_aleatorio:
                        self.tentar_novamente = False 
                        print('Parabens, voce acertou!') 
                        break
    except: 
        print('Digite um numero.')
        self.Iniciar()

    def PedirValorAleatorio(self):
        self.valor_do_chute = input('Chute um numero: ')

    def GerarNumeroAleatorio(self):
        return self.valor_aleatorio

chute = ChuteONumero()
chute.Iniciar()