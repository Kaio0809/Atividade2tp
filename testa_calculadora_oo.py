from calculadora_oo import Calculadora

calc = Calculadora()

def teste():
    print(calc.somar(10,19))
    print(calc.subtrair(15,12))
    print(calc.multiplicar(20,25))
    print(calc.dividir(10,2))
    print(calc.dividir(10,0))

teste()