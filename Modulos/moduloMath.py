#módulos de cálculos matemáticos
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        raise ValueError("Divisão por zero não é permitida.")

def potencia(a, b):
    return a ** b

def resto(a, b):
    if b != 0:
        return a % b
    else:
        raise ValueError("Divisão por zero não é permitida.")