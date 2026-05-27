chances = 5
palavra_secreta = 'batata'

while chances > 0:
    palavra = input(f"Qual a palavra secreta? Você tem {chances} chances: ")
    chances -= 1
    
    if palavra == 'batata':
        print("Você acertou a palavra, toma aqui uma batata 🥔")
        
        break