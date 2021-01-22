print('Digite os valores para serem somados:')
print('Para finalizar é só digitar zero: 0')
n = float(input())
total = n
while n:
    n = float(input())
    total = total + n
print('TOTAL: %s'%total)