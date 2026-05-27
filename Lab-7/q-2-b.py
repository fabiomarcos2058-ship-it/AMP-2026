soma = 0
contador = 0 

while contador < 10: 
    num = int(input("Digite um número para somar: "))
    soma += num
    contador += 1 
print(f"A soma dos 10 números é: {soma}")
#Explicação: O objetivo aqui é rodar um loop exatamente 10 vezes usando um contador. A cada volta, o código pede um número inteiro ao usuário 
#e vai somando (acumulando) esse valor na variável 'soma', exibindo o total no final.
