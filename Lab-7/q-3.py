chances = 5
palavra_secreta = 'batata'

while chances > 0:
    palavra = input(f"Qual a palavra secreta? Você tem {chances} chances: ")
    chances -= 1
    
    if palavra == 'batata':
        print("Você acertou a palavra, toma aqui uma batata 🥔")
        
        break
# Explicação: Este código testa o comando 'break'. Ele te dá 5 chances num 
# loop 'while' para acertar a palavra secreta ('batata'). Se você acertar o 
# chute antes das chances zerarem, o 'break' quebra o loop imediatamente e 
# encerra a execução com sucesso, sem precisar rodar o resto das tentativas.
