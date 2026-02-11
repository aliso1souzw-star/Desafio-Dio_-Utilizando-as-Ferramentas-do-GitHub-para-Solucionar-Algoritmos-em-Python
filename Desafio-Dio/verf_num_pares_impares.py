# Como entrada, receba um número inteiro e verifique se ele é par ou ímpar

numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print(f"{numero} é PAR")
else:
    print(f"{numero} é ÍMPAR")