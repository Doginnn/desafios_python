print('Digite os valores para serem somados:')
print('Para finalizar é só digitar zero: 0')
total = 0
while 1:
    try:
        n = float(input())
        total = total + n
    except:
        break
print('TOTAL: %s'%total)