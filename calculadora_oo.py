class Calculadora:
    def __init__(self):
        pass

    def somar(self,operando_a,operando_b):
        return operando_a + operando_b
    
    def subtrair(self,operando_a, operando_b):
        return operando_a - operando_b
    
    def multiplicar(self,operando_a, operando_b):
        return operando_a*operando_b
    
    def dividir(self,operando_a,operando_b):
        return operando_a/operando_b if operando_b != 0 else "Erro de Divisão por Zero"
    