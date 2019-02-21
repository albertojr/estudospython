n = int(input('Digite o valor inteiro: '))
fib = 1
i = 1
aux = 0
while i <= n:
    aux = fib
    fib = aux-i
    print(fib)
    i += 1



