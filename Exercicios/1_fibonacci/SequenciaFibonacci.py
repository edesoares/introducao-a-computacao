'''
MAC110 - Introdução à Computação
Primeiro Semestre de 2021

Exercício 1
A sequência de Fibonacci é uma sequência de inteiros onde cada elemento é igual
a soma dos dois anteriores. Os dois primeiros são iguais a 1:
1, 1, 2, 3, 5, 8, 13, 21, 34,...
Faça um programa que dado N > 0, imprima todos os números da sequência menores ou iguais a N.
'''

# Início do programa
print("### Fibonacci ###\n")
n = int(input("Entre com o valor de N: "))

# Método pra calcular a sequência
def fibonacci(n):
    print("Sequência de Fibonacci até ",n,)
    a, b = 1, 1
    while a <= n:
        print(a)    
        a, b = b, a + b

# Controle (n > 0)
if (n < 1):
    while (n < 1):
        print("!!! N deve ser maior que 0 !!!\n")
        n = int(input("Tente novamente: "))
    fibonacci(n)
else :
    fibonacci(n)