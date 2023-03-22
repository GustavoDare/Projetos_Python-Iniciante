class Operacoes():

    def __init__(self, numero1, numero2):
        self.n1 = numero1
        self.n2 = numero2

    
    def soma(self):
        soma = self.n1 + self.n2
        return soma
    

    def subtracao(self):
        sub = self.n1 - self.n2
        return sub
    

    def divisao(self):
        try:
            div = self.n1 / self.n2
        except ZeroDivisionError:
            return "Não é possível dividir por zero."
        else:
            return div
        
    
    def multiplicacao(self):
        mult = self.n1 * self.n2
        return mult
