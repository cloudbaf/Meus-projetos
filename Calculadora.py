print('Bem-vindo ao Calculadora: ')
def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

def raizquadrada(a):
    return a ** 0.5

def calculadora():
    o = input('Operação(+ = Mais, - = Menos, * = Vezes, / = Dividir.): ')
    num = float(input('Digite um número: '))
    num2 = float(input('Digite um outro número: '))

    if o == "+":
        r = adicao(num, num2)
        print('resultado: ', r)
    elif o == "-":
        r = subtracao(num, num2)
        print('Resultado: ', r)
    elif o== "*":
        r = multiplicacao(num, num2)
        print('Resultado: ', r)
    elif o == "/":
        r = divisao(num, num2)
        print('Resultado: ', r)
    else:
        print('Operação Inválida!')
calculadora()
