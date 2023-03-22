from calculadora import Calculadora

calc = Calculadora()
res = ''

print("Digite off para sair a qualquer momento")
while res != 'off':
    res = calc.resultado()
