maior = None

while True:
    num = float(input("Digite um número (0 para parar): "))
    
    if num == 0:
        break
    
    if maior is None or num > maior:
        maior = num

print("Maior número:", maior)
