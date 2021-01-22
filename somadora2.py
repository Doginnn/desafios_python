print('Digite os valores para serem somados:')
print('Para finalizar é só digitar zero: 0')
total = 0
while 1:
    n = float(input())
    if n == 0:
        break
    total = total + n
print('TOTAL: %s'%total)