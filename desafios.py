# QUESTÃO 1
print("Código verifica se uma palavra começa com 'B' e termina com 'A'")

inicio = "b"
fim = "a"

nome = input("Digite um nome: ")

if nome[0] == inicio and nome[-1] == fim:
    print("A palavra ",nome, "termina com 'A' e começa com 'B', a palavra é valida. Parabéns!")
else:
    print("A palavra ",nome, "não atende aos requisitos, tente novamente!")

#---------------------------------------------------------------
# QUESTÃO 2
'''
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
'''

num1 = (input("Digite um número inteiro: "))

if num1.isdigit():
    num1 = int(num1)

    if (num1 % 2) == 0:
        print(f"O número {num1} é inteiro e é Par!")

    else:
        print(f"O número {num1} é inteiro e é Ímpar!")

else:
    print(f"{num1} não é um número inteiro, Digite apenas números inteiros!")

#---------------------------------------------------------------
# QUESTÃO 3
'''
Faça um programa que tenha um input da hora e que baseando-se no input exiba
a saudação apropriada. Ex: Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-24
'''

hora = input("Digite um horário: ")

if hora.isdigit():
    hora = int(hora)

    if hora <= 11:
        print(f"São {hora}hs, Bom Dia!")

    elif hora >= 12 and hora <=17:
        print(f"São {hora}hs, Boa Tarde!")

    elif hora >= 18 and hora <= 24:
        print(f"São {hora}hs, Boa Noite!")

    else:
        print("Não existe mais que 24hs no dia!")

else:
    print(f"'{hora}' Não é um horário válido, tente novamente!")

#---------------------------------------------------------------
#QUESTÃO 4
'''
Faça um programa que peça o primeiro nome de usuário. Se o nome tiver 4 letras
ou menos escreva "Nome curto", entre 5 e 6 escreva "Nome normal" e maior que
6 escreva "Nome muito grande".
'''

nome = input("Digite um nome: ")
tamanho = len(nome)

if tamanho <= 4:
    print(f"O nome '{nome}' é muito curto!")

elif tamanho >= 5 and tamanho <= 6:
    print(f"O nome '{nome}' é um nome normal!")

else:
    print(f"O nome '{nome}' é um nome muito grande!")

#---------------------------------------------------------------
#QUESTÃO 5
'''
Calculadora de operações básicas.
'''

while True:
    print()
    num_1 = input('Digite um número: ')
    num_2 = input('Digite um número: ')
    operador = input('Digite um operador: ')
    sair = input('Deseja sair? [y]Yes ou [n]No: ')

    if sair == 'y':
        print('Obrigado por usar a calculadora!')
        break

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Por favor digite apenas números!')
        continue
    
    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador == '+':
        print(num_1 + num_2)

    elif operador == '-':
        print(num_1 - num_2)
    
    elif operador == '/':
        print(num_1 / num_2)

    elif operador == '*':
        print(num_1 * num_2)

print('Até breve!')

#---------------------------------------------------------------
#QUESTÃO 6
'''
Iterando strings com While.
O programa pega uma frase pré definida e coloca dentro de outra string vazia
com o comando input dado pelo usuário com a letra que ficará maiúscula.
'''

frase = 'o rato roeu a roupa do rei de roma'
tamanho = len(frase)
count = 0
nova_frase = ''

print(frase)
print()
letra_maiuscula = input('Digite a letra nessa frase que ficará "MAIÚSCULA": ')

while count < tamanho:
    letra = frase[count]

    if letra == letra_maiuscula:
        nova_frase += letra_maiuscula.upper()
    
    else:
        nova_frase += letra
    count += 1

print(nova_frase)

#---------------------------------------------------------------
#QUESTÃO 7