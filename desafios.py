# QUESTÃO 1
print("Código verifica se uma palavra começa com 'B' e termina com 'A'")

inicio = "b"
fim = "a"

nome = input("Digite um nome: ")

if nome[0] == inicio and nome[-1] == fim:
    print("A palavra ",nome, "termina com 'A' e começa com 'B', a palavra é valida. Parabéns!")
else:
    print("A palavra ",nome, "não atende aos requisitos, tente novamente!")