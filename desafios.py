# QUESTÃO 1
print("Código verifica se uma palavra começa com 'B' e termina com 'A'")

inicio = "b"
fim = "a"

nome = input("Digite um nome: ")

if nome[0] == inicio and nome[-1] == fim:
    print("A palavra ", nome, "termina com 'A' e começa com 'B', a palavra é valida. Parabéns!")
else:
    print("A palavra ", nome, "não atende aos requisitos, tente novamente!")

# ---------------------------------------------------------------
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

# ---------------------------------------------------------------
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

    elif hora >= 12 and hora <= 17:
        print(f"São {hora}hs, Boa Tarde!")

    elif hora >= 18 and hora <= 24:
        print(f"São {hora}hs, Boa Noite!")

    else:
        print("Não existe mais que 24hs no dia!")

else:
    print(f"'{hora}' Não é um horário válido, tente novamente!")

# ---------------------------------------------------------------
# QUESTÃO 4
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

# ---------------------------------------------------------------
# QUESTÃO 5
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

# ---------------------------------------------------------------
# QUESTÃO 6
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

# ---------------------------------------------------------------
# QUESTÃO 7
'''
Função enumerate em uma lista.
'''
lista = ['Diógenes', 'Emmanuel', 'Dantas', 'Soares']

for indice, nome in enumerate(lista):
    print(indice, nome)

# ---------------------------------------------------------------
# QUESTÃO 8
'''
Função desempacotamento em uma lista.
'''
lista = ['Diógenes', 'Emmanuel', 'Dantas', 'Soares']

n1, n2, *_ = lista  # O "*_" na variável indica que vou imprimir apenas os dois primeiros índices na lista

print(n1, n2)

# ---------------------------------------------------------------
# QUESTÃO 9
'''
Operador ternário (usuario_logado)
'''
usuario_logado = True
msg = 'Você está logado!' if (usuario_logado) else 'Você precisa logar no Sistema!'
print(msg)
# ---------------------------------------------------------------
'''
Operador ternário (maior_de_idade)
'''
idade = input('Qual a sua idade? ')
if not idade.isnumeric():  # Condição verifica se está digitando apenas números inteiros!
    print('Digite apenas números inteiros!')
else:
    idade = int(idade)
    maior_de_idade = (idade >= 18)
    msg = 'É de maior, pode acessar!' if (maior_de_idade) else 'Você não é maior de idade!'
    print(msg)

# ---------------------------------------------------------------
# QUESTÃO 10
'''
crie as estruturas for retornando de 0 até 8 e while retornando de 10 até 2
'''
diminuindo = [10, 9, 8, 7, 6, 5, 4, 3, 2]

for contador, numeros in enumerate(diminuindo):
    print(contador, numeros)

# for x, y in enumerate(range(10, 1, -1)):
#     print(x, y)

# ---------------------------------------------------------------
# QUESTÃO 11
'''
Programa pra validar seu CPF.
'''
while True:
    cpf = input('Digite um CPF: ')
    novo_cpf = cpf[:-2]  # Elimina os 2 últimos números do CFP
    reverso = 10  # Contador reverso
    total = 0
    if cpf.isdigit():  # Valida para ser digitado apenas números
        cpf = int(cpf)

        for index in range(19):
            if index > 8:  # Primeiro índice vai de 0 até 9
                index -= 9  # Referente aos 9 primeiros números do CPF

            total += int(novo_cpf[index]) * reverso  # Valor total da multiplicação
            reverso -= 1  # Decrementa o contador reverso

            if reverso < 2:
                reverso = 11
                digito = 11 - (total % 11)

                if digito > 9:  # Se o digito for maior que 9 ele zera
                    digito = 0
                total = 0
                novo_cpf += str(digito)  # Concatena o digito gerado no novo CPF

        if cpf == novo_cpf:
            print(f'O CPF {cpf} é válido!')
        else:
            print(f'O CPF {cpf} é válido!')

    else:
        print('Por favor digite APENAS NÚMEROS INTEIROS!')  # Retorno da validação se não for apenas números

# ---------------------------------------------------------------
# QUESTÃO 12
'''
# Programa para gerar CPFs Válidos.
'''
from random import randint

numero = str(randint(100000000, 999999999))  # Gera um CPF aleatório e válido entre esses 2 números

novo_cpf = numero  # Elimina os 2 últimos números do CFP
reverso = 10  # Contador reverso
total = 0

for index in range(19):
    if index > 8:  # Primeiro índice vai de 0 até 9
        index -= 9  # Referente aos 9 primeiros números do CPF

    total += int(novo_cpf[index]) * reverso  # Valor total da multiplicação
    reverso -= 1  # Decrementa o contador reverso

    if reverso < 2:
        reverso = 11
        digito = 11 - (total % 11)

        if digito > 9:  # Se o digito for maior que 9 ele zera
            digito = 0
        total = 0
        novo_cpf += str(digito)  # Concatena o digito gerado no novo CPF

print(f'Esse é seu novo CPF: {novo_cpf}')

# ---------------------------------------------------------------
# QUESTÃO 13
'''
Definindo Funções em Python(def)
'''
# 1 - Crie uma função que exibe uma saudação com os parametros: saudacao e nome.
def welcome():
    saudacao = input('Digite uma saudação: ')
    nome = input('Digite seu nome: ')
    print(saudacao, nome)
welcome()

# 2 - Crie uma função que recebe 3 números e exibe a soma entre eles.
def calculadora():
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite um número: '))
    n3 = int(input('Digite um número: '))
    soma = n1+n2+n3
    print(f'A soma de {n1} + {n2} + {n3} é: {soma}')
calculadora()

# 3 - Crie uma função que recebe 2 números. O primeiro é um valor e o segundo um percentual(ex: 10%).
# Retorne(return) o valor do primeiro número somado com o percentual
def percentual():
    valor = int(input('Digite um valor: '))
    porcento = int(input('Deseja adicionar quantos %: '))
    soma = valor + (valor * porcento / 100)
    print(f'O valor {valor} + {porcento}% é igual a: {soma}')
    return soma
percentual()

# 4 - Fizz Buzz - Se o parâmetro da função for divisível por 2, retorne Fizz, se for divisível por 5, retorne Buzz.
# Se o parâmetro da função for divisível por 5 e 3, retorne FizzBuzz, caso contrário retorne o número enviado.
def comparador_fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    if n % 3 == 0:
        return 'Fizz'
    if n % 5 == 0:
        return 'Buzz'
    else:
        return f'{n} Não atende nenhum resultado, Tente outro número!'
print(comparador_fizzbuzz(int(input('Digite um número: '))))

# ---------------------------------------------------------------
# QUESTÃO 14
'''
Game de Perguntas e Respostas
'''
print()
print('Esse é um programa de perguntas e respostas.')
print('Você deve escolher apenas uma alternativa por pergunta.')

perguntas = {
    'Pergunta "1"': {
        'pergunta': 'Quanto é 2+2 ?',
        'respostas': {
            'a': '1',
            'b': '4',
            'c': '5',
        },
        'resposta_certa': 'b',
    },
    'Pergunta "2"': {
        'pergunta': 'Quanto é 3*2 ?',
        'respostas': {
            'a': '4',
            'b': '10',
            'c': '6',
        },
        'resposta_certa': 'c',
    },
}
print()

respostas_certas = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Respostas: ')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')
    
    resposta_usuario = input('Sua resposta é? ')

    if resposta_usuario == pv['resposta_certa']:
        print('Parabéns, você acertou!!! :)')
        respostas_certas += 1
    else:
        print('Que pena, você errou!!! ;(')

    print()

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100

print(f'Você acertou {respostas_certas} respostas ')
print(f'Sua porcentagem de acerto foi {porcentagem_acerto}% ')

# ---------------------------------------------------------------
# QUESTÃO 15
"""
-> É uma lista de listas de números inteiros
-> As listas internas tem o tamanho de 10 elementos
-> As listas internas contém números entre 1 a 10 e eles podem ser duplicados
Exercício
-> Crie uma função que encontra o primeiro duplicado considerando o segundo
    número como a duplicação. Retorne a duplicação considerada.
        Requisitos:
            A ordem do número duplicado é considerada a partir da segunda
            ocorrência do número, ou seja, o número duplicado em si.
            Exemplo:
                [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
                [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
            Se não encontrar duplicados na lista, retorne -1
"""
lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]


def encontra_primeiro_duplicado(param_lista_de_inteiros):
    numeros_checados = set()
    primeiro_duplicado = -1

    for numero in param_lista_de_inteiros:
        if numero in numeros_checados:
            primeiro_duplicado = numero
            break

        numeros_checados.add(numero)
    
    return primeiro_duplicado

for lista_de_inteiros in lista_de_listas_de_inteiros:
    print(lista_de_inteiros, encontra_primeiro_duplicado(lista_de_inteiros))

# ---------------------------------------------------------------
# QUESTÃO 16
"""
LIST COMPREHENSIONS
"""
string = '012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'
n =10
lista = [string[i:i + n] for i in range(0, len(string), n)]
retorno_final = '.'.join(lista)

print()
print(lista)
print()
print(retorno_final)


# ---------------------------------------------------------------
# QUESTÃO 17
"""
"""


# ---------------------------------------------------------------
# QUESTÃO 18
"""
"""


# ---------------------------------------------------------------
# QUESTÃO 19
"""
"""


# ---------------------------------------------------------------
# QUESTÃO 20
"""
"""
