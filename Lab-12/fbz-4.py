# Solicitando os dados ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Calculando a diferença absoluta
diferenca = abs(num1 - num2)

# Arredondando o resultado
resultado_final = round(diferenca, 2)

# Exibindo o resultado formatado
print(f"A diferença absoluta entre os números é: {resultado_final}")