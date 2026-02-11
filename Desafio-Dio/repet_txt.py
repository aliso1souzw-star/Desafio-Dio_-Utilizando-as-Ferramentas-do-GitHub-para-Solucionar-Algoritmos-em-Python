# Agora vamos solicitar uma string e um numero inteiro como entrada, Depois teremos que retornar a string repetida o numero de vezes do informado.

texto = input("Digite uma string: ")
numero = int(input("Digite um numero inteiro: "))

texto_repetido = " ".join([texto] * numero)
print("A string repetida é: " + texto_repetido)