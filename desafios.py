# QUESTÃO 1
# print("Código verifica se uma palavra começa com 'B' e termina com 'A'")

# inicio = "b"
# fim = "a"

# nome = input("Digite um nome: ")

# if nome[0] == inicio and nome[-1] == fim:
#     print("A palavra ",nome, "termina com 'A' e começa com 'B', a palavra é valida. Parabéns!")
# else:
#     print("A palavra ",nome, "não atende aos requisitos, tente novamente!")


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