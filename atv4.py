soma = 0

while True:
    num = float(input("Digite um número: "))
    
    if num < 0:
        break
    
    soma += num

print("Soma total:", soma)
