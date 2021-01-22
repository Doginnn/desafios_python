print('Digite os valores para serem somados:')
print('Para finalizar é só digitar 0 ou teclar ENTER duas vezes')
total = 0
while 1:
    try:
        linha = input()
        n = float(linha)
        total = total + n
    except:
        if len(linha) == 0:
            break
        elif ',' in linha:
            print('Use o . (ponto) como separador decimal!')
        else:
            print('Por favor digite apenas números!')
print('O total da soma é: %s'%total)