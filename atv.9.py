positivos = 0
negativos = 0

while True:
    num = float(input("Digite um número (0 para parar): "))
    
    if num == 0:
        break
    
    if num > 0:
        positivos += 1
    else:
        negativos += 1

print("Positivos:", positivos)
print("Negativos:", negativos)
