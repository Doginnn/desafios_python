print ('Balanço de despesas domésticas')
print()
gasto1 = float(input('Quanto você gastou Diógenes? '))
gasto2 = float(input('Quanto você gastou Gracinha? '))
total = gasto1 + gasto2
print ('Total de gastos foi = R$ %.2f' % total)
media = total/2
print ('Gastos por pessoa foi = R$ %.2f' % media)
if gasto1 < media:
    diferença = media - gasto1
    print('Diógenes deve pagar R$ %.2f de diferença a você Gracinha!'%diferença)
elif gasto2 < media:
    diferença = media - gasto2
    print('Gracinha deve pagar R$ %.2f de diferença a você Diógenes!'%diferença)
else:
    print('Vocês gastaram o mesmo valor, não precisa dar diferença a ninguém :) !!!')