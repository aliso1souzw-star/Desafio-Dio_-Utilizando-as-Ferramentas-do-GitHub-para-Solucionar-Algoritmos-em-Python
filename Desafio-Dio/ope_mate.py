# Vamos solicitar como entrada dois numeros e depois vamos realizar uma operação simples entre os dois.

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
operacao = input("Digite a operação desejada (+, -, *, /): ")

if operacao == "+":
    resultado = num1 + num2
    print(f"O resultado de {num1} + {num2} é: {resultado}")
elif operacao == "-":
    resultado = num1 - num2
    print(f"O resultado de {num1} - {num2} é: {resultado}")
elif operacao == "*":
    resultado = num1 * num2
    print(f"O resultado de {num1} * {num2} é: {resultado}")
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
        print(f"O resultado de {num1} / {num2} é: {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida.")
else:
    print("Operação inválida. Por favor, escolha entre +, -, * ou /.")