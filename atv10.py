numero_secreto = 7

while True:
    palpite = int(input("Adivinhe o número: "))
    
    if palpite == numero_secreto:
        print("Você acertou!")
        break
    elif palpite > numero_secreto:
        print("Muito alto!")
    else:
        print("Muito baixo!")