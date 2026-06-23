# Mude este valor para testar os outros casos: "10", "3.5", "-2.5", "palavra", "False"
entrada = input("Digite um valor: ") 

# --- Testes de Conversão ---

# Saída int()
# OBS: str com ponto decimal ou texto puro vai dar erro (ValueFlaw) se tentar direto para int.
# Descomente a linha abaixo apenas quando a entrada for "10"
# print(int(entrada)) 

# Saída float()
# OBS: "palavra" e "False" vão falhar aqui.
# Descomente a linha abaixo apenas quando a entrada for "10", "3.5" ou "-2.5"
# print(float(entrada))

# Saída bool()
# Qualquer string que não esteja vazia retorna True em Python!
print(bool(entrada))