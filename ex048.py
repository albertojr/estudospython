soma = 0
cont = 0
print('Todos os números ímpares que são múltiplos de 3 e estão entre 1 e 500:')
for num in range(1, 5001, 2):
    if (num % 3) == 0:
        soma += num
        cont += 1

print(soma)
print(cont)
