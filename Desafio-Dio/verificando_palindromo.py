# Verificador de Palíndromos

def verificar_palindromo(palavra):
    """Verifica se uma palavra é um palíndromo"""
    # Remove espaços e converte para minúsculas para comparação mais robusta
    palavra_limpa = palavra.strip().lower().replace(" ", "")
    
    # Compara a palavra com sua reversa
    if palavra_limpa == palavra_limpa[::-1]:
        return True
    else:
        return False

# Entrada do usuário
entrada = input("Digite uma palavra para verificar se é um palíndromo: ")

# Verifica se é palíndromo
eh_palindromo = verificar_palindromo(entrada)

# Saída do resultado
if eh_palindromo:
    print(f"✓ '{entrada}' é um PALÍNDROMO!")
else:
    print(f"✗ '{entrada}' NÃO é um palíndromo.")