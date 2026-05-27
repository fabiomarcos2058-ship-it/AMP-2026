conta_total = 0.0

while True: # loop infinito
    print("\nCardápio")
    print("1. Açaí 300ml - R$ 12,00")
    print("2. Mousse - R$ 6,50")
    print("3. Salada de frutas - R$ 10,00")
    print("4. Fechar a conta")
    
    opcao = int(input("Digite o número da opção desejada: "))
    
    if opcao == 1:
        conta_total += 12.00
        print("-> Açaí de 300ml adicionado!")
    elif opcao == 2:
        conta_total += 6.50
        print("-> Mousse adicionado!")
    elif opcao == 3:
        conta_total += 10.00
        print("-> Salada de frutas adicionada!")
    elif opcao == 4:
        print(f"\nFechando a conta... O valor total a pagar é R$ {conta_total:.2f}")
        break # Sai do loop infinito
    else:
        print("-> Opção inválida. Digite um número do cardápio.")
        # Explicação: Simulando um caixa de cantina, este código cria um menu usando 
# 'while True' (um loop que rodaria para sempre). Ele soma os preços das opções 
# escolhidas numa variável acumuladora até o usuário selecionar a opção 4, 
# que aciona o 'break' para finalmente quebrar o loop infinito e exibir a conta.
