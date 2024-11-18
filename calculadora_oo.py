class Calculadora:
    def __init__(self):
        self.__acumulador = 0.0

    def somar(self,operando_a,operando_b = None):
        self.__acumulador += operando_a if operando_b is None else operando_a + operando_b
        return self.__acumulador
    
    def subtrair(self,operando_a, operando_b = None):
        self.__acumulador = operando_a - self.__acumulador if operando_b is None else operando_a - operando_b
        return self.__acumulador
    
    def multiplicar(self,operando_a, operando_b = None):
        self.__acumulador = operando_a*self.__acumulador if operando_b is None else operando_a*operando_b
        return self.__acumulador
    
    def dividir(self,operando_a,operando_b = None):
        try:
            if operando_b is None:
                self.__acumulador = operando_a / self.__acumulador
            else:
                self.__acumulador = operando_a / operando_b
            return self.__acumulador
        
        except ZeroDivisionError:
            return "Erro de divisão por Zero!"
