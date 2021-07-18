# MAC110 - Introdução à Computação
# Primeiro Semestre de 2021
# BMAC–IMEUSP
# Aluno: Edgar Soares Marinho
# nºUSP: 9337691

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