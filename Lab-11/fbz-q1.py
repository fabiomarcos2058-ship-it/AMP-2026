while True:
    resposta = input("Você quer saber como manter uma pessoa ingênua ocupada por horas? S/N\n> ")
    
    # Validação de resposta válida positiva
    if resposta in ['s', 'S', 'sim', 'SIM']:
        continue
        
    # Validação de resposta válida negativa
    elif resposta in ['n', 'N', 'não', 'NÃO', 'nao', 'NAO']:
        print("Obrigada. Tenha um bom dia!")
        break
        
    # Resposta inválida
    else:
        print(f'"{resposta}" não é uma resposta válida de sim/não.')