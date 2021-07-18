# MAC110 - Introdução à Computação
# Primeiro Semestre de 2021
# BMAC–IMEUSP
# Aluno: Edgar Soares Marinho
# nºUSP: 9337691

from math import cos, sin, pi
from time import process_time_ns

# Essas variáveis globais vão armazenando os valores de 'x' e 'n' toda vez que
# a função 'consistencia()' é chamada. Esses valores vão pra 'x' e 'n' quando o
# usuário não entrar com um numero. No ínicio do programa elas valem 0.
a, b = 0.0, 0

# Função principal
def main():

    # Faz a primeira chamada da 'consistencia()'
    consistencia()

    # depois entra nesse loop pra repetir o cálculo
    while True:
        try:
            resp = input("\nDeseja realizar um novo cálculo? (s/n): ")
        except:
            pass
        else:
            if resp == "n" or resp == "N":
                print("\n!!! PROGRAMA ENCERRADO PELO USUÁRIO !!!\n")
                break
            elif resp == "s" or resp == "S":

                # Se o usuário quiser repetir chama a 'consistencia()' de novo
                consistencia()
                continue
            else:
                print("\n!!! ENTRADA INVALIDA !!!")
                continue

# Essa função recebe 'x' e 'n' e faz a consistência
# se estiver td certo, ela chama a função 'calcular()'
def consistencia():
    global a, b

    # Entrada e consistência de 'x'
    while True:
        try:
            x = input("\nEntre com o valor de x: ")

            # Ele recebe 'x' como string pra verificar que a entrada foi vazia
            if x == "":

                # Se for vazia 'x' fica sendo o valor de 'a'. Mesma coisa pra 'n'.
                x = a
                break
            x = float(x)
            break
        except:
            print("\n!!! VALOR INVALIDO PARA x !!!")
            continue

    # Entrada e consistência de 'n'
    while True:
        try:
            n = input("\nEntre com o valor de n: ")
            if n == "":
                n = b
                break
            n = int(n)

            # Verifica se 'n' é um valor válido (n > 0 e n < 101)
            if n < 1 or n > 100:
                print("\n!!! n DEVE SER MAIOR QUE 0 E MENOR QUE 101 !!!")
                continue
            break
        except:
            print("\n!!! VALOR INVALIDO PARA n !!!")
            continue
    
    # Armazena os valores nas variáveis globais
    a, b = x, n

    print("\nValores calculados para: ")
    print(f"x = {x}")
    print(f"n = {n}")

    # Chama o cálculo passando 'x' e 'n'
    calcular(x, n)

def calcular(x, n):
    # Reduz o valor de 'x' pra evitar overflow
    x %= (2 * pi)

    # SENO
    print("\nSENO\n")

    # Calculo usando a função 'math.sin'
    # 't' e 'dt' calculam o tempo de execução
    t = process_time_ns()
    s1 = sin(x)
    dt1 = process_time_ns() - t

    # Mesma coisa usando séries de Taylor
    t = process_time_ns()
    s2 = seno(x, n)
    dt2 = process_time_ns() - t

    imprime("math.sin", s1, dt1, s2, dt2)

    # COSSENO
    print("\nCOSSENO\n")

    # Usando a função 'math.cos'
    t = process_time_ns()
    c1 = cos(x)
    dt1 = process_time_ns() - t

    # Usando séries de Taylor
    t = process_time_ns()
    c2 = cosseno(x, n)
    dt2 = process_time_ns() - t

    imprime("math.cos", c1, dt1, c2, dt2)

# Calcula o seno usando séries de Taylor
def seno(x, n):
    sen, pot, s, fat = 0.0, x, 1, 1.0
    for i in range(1, n + 1):
        sen += s * (pot/fat)
        fat *= (2 * i + 1) * (2 * i)
        pot *= x * x
        s *= -1
    return sen

# Calcula o cosseno usando séries de Taylor
def cosseno(x, n):
    cos, pot, s, fat = 0.0, 1, 1, 1.0
    for i in range(1, n + 1):
        cos += s * (pot/fat)
        fat *= (i * 2) * ((i * 2) - 1)
        pot *= x * x
        s *= -1
    return cos

# Essa função imprime resultados
def imprime(string, resultado1, tempo1, resultado2, tempo2):

    print(f"Usando a função {string}")
    print(f"Valor Calculado: {resultado1}")
    print(f"Tempo: {tempo1} ns")
    print()
    print(f"Usando a soma de termos")
    print(f"Valor Calculado: {resultado2}")
    print(f"Tempo: {tempo2} ns")

# Inicia o programa
main()