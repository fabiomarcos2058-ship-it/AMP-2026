import datetime

# Obtém a data atual
hoje = datetime.datetime.now()

# Cria a data da prova (Ano, Mês, Dia)
data_prova = datetime.datetime(2026, 7, 14)

# Calcula a diferença (Data futura - Data atual para dar valor positivo)
diferenca = data_prova - hoje

# Exibe o resultado na tela
print(f"Faltam {diferenca.days} dias para a sua prova!")