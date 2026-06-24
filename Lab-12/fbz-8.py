import datetime

# Obter a data atual
hoje = datetime.datetime.now()
ano_atual = hoje.year

# Cadastro da primeira pessoa
nome1 = input("Digite o nome da primeira pessoa: ")
data_str1 = input(f"Digite a data de nascimento de {nome1} (dd/mm/aaaa): ")
data_nasc1 = datetime.datetime.strptime(data_str1, "%d/%m/%Y")

# Cadastro da segunda pessoa
nome2 = input("Digite o nome da segunda pessoa: ")
data_str2 = input(f"Digite a data de nascimento de {nome2} (dd/mm/aaaa): ")
data_nasc2 = datetime.datetime.strptime(data_str2, "%d/%m/%Y")

# Definir o próximo aniversário de cada um para o ano atual
niver1 = datetime.datetime(ano_atual, data_nasc1.month, data_nasc1.day)
niver2 = datetime.datetime(ano_atual, data_nasc2.month, data_nasc2.day)

# Se o aniversário já passou este ano, ajustamos para o ano que vem
if niver1 < hoje:
    niver1 = datetime.datetime(ano_atual + 1, data_nasc1.month, data_nasc1.day)
if niver2 < hoje:
    niver2 = datetime.datetime(ano_atual + 1, data_nasc2.month, data_nasc2.day)

# Calcular a diferença em dias
dif1 = (niver1 - hoje).days
dif2 = (niver2 - hoje).days

# Comparação de proximidade
if dif1 < dif2:
    print(f"\nO aniversário de {nome1} está mais próximo! Faltam {dif1} dias.")
elif dif2 < dif1:
    print(f"\nO aniversário de {nome2} está mais próximo! Faltam {dif2} dias.")
else:
    print(f"\nAmbos estão à mesma distância! Faltam {dif1} dias.")