import datetime

# Cadastro da primeira pessoa
nome1 = input("Digite o nome da primeira pessoa: ")
data_str1 = input(f"Digite a data de nascimento de {nome1} (dd/mm/aaaa): ")
data1 = datetime.datetime.strptime(data_str1, "%d/%m/%Y")

# Cadastro da segunda pessoa
nome2 = input("Digite o nome da segunda pessoa: ")
data_str2 = input(f"Digite a data de nascimento de {nome2} (dd/mm/aaaa): ")
data2 = datetime.datetime.strptime(data_str2, "%d/%m/%Y")

# Quem nasceu antes (menor data) é mais velho
if data1 < data2:
    print(f"\nA pessoa mais velha é: {nome1}")
elif data2 < data1:
    print(f"\nA pessoa mais velha é: {nome2}")
else:
    print(f"\n{nome1} e {nome2} têm exatamente a mesma idade!")