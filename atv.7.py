soma = 0
quantidade = 0

while True:
    nota = float(input("Digite uma nota (-1 para parar): "))
    
    if nota == -1:
        break
    
    soma += nota
    quantidade += 1

if quantidade > 0:
    media = soma / quantidade
    print("Média:", media)
else:
    print("Nenhuma nota válida.")
