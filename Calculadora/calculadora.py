from operacoes import Operacoes

class Calculadora():

    def resultado(self):
        resultado = self.operacao()
        if resultado == 'off':
            return 'off'
        else:
            print(f"O resultado é: {resultado}")

    def operacao(self):
        n1 =self.primeiro_numero()
        if n1 == 'off':
            return 'off'
        operador = self.operador()
        if operador == 'off':
            return 'off'
        n2 = self.segundo_numero()
        if n2 == 'off':
            return 'off'
        
        op = Operacoes(n1, n2)
        if operador == '+':
            resultado = op.soma()
        if operador == '-':
            resultado = op.subtracao()
        if operador == '/':
            resultado = op.divisao()
        if operador == '*':
            resultado = op.multiplicacao()
        
        return resultado

    
    def primeiro_numero(self):
        while True:
            numero1 = input("Digite o primeiro número: ")
            if numero1 == 'off':
                return numero1
            else:
                try:
                    numero1 = float(numero1)
                except:
                    print("É necessário digitar um número")
                else:
                    return numero1
    
    def operador(self):
        while True:
            operador = input("Digite um operador (+ - / *): ")
            if operador == 'off':
                return operador
            else:
                if operador in "+-/*" and operador != '':
                    return operador
                else:
                    print("Operador inválido.")
    

    def segundo_numero(self):
        while True:
            numero2 = input("Digite o segundo número: ")
            if numero2 == 'off':
                return numero2
            else:
                try:
                    numero2 = float(numero2)
                except:
                    print("É necessário digitar um número")
                else:
                    return numero2