def inicio():
    print('******************')
    print('***Calculadora****')
    print('******************')

def adicao(a, b):
    return a + b
def subtracao(a, b):
    return a - b
def multiplicacao(a, b):
    return a * b
def divisao(a, b):
    return a / b
def resto(a, b):
    return a % b

def calcula():
    a = int(input('Digite o primeiro número: '))
    b = int(input('Digite o segundo número: '))

    print('(1) Adição, (2) Subtração, (3) Multiplicação, (4) Divisão')
    operacao = int(input('Qual operação deseja realizar? '))

    if operacao == 1:
        print(f'A soma é {adicao(a, b)}')
    elif operacao == 2:
        print(f'A diferença é {subtracao(a, b)}')
    elif operacao == 3:
        print(f'O produto é {multiplicacao(a, b)}')
    elif operacao == 4:
        print(f'O quociente é {divisao(a, b)} e o resto é {resto(a, b)}')
    else:
        print('Operacao inválida')

    reiniciar = input('Deseja calcular novamente? ')

    if reiniciar == 'sim':
        calcula()
    else: 
        pass

inicio()
calcula()