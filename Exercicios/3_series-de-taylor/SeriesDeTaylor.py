# MAC110 - Introdução à Computação
# Primeiro Semestre de 2021
# BMAC–IMEUSP
# Aluno: Edgar Soares Marinho
# nºUSP: 9337691

import math

# Essas variáveis globais vão armazenando os valores de 'x' e 'n' toda vez que
# a função 'consistencia()' é chamada. Esses valores vão pra 'x' e 'n' quando o
# usuário não entrar com um numero. No ínicio do programa elas valem 0.
a, b = 0.0, 0.0

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

# Faz a entrada e a consistência dos valores inseridos
def consistencia():
    global a, b

    # Entrada e consistência de 'x'
    while True:
        try:
            x = input("\nEntre com o valor de x: ")

            # Ele recebe 'x' como string pra verificar se a entrada foi vazia
            if x == '':

                # Se 'x' for vazio atribui o valor de 'a', o mesmo pra 'eps'
                x = a
                break
            x = float(x)

            # Verifica se 'x' é um valor válido (x > -11 e x < 11)
            if x > -11 and x < 11: 
                break
            else:
                print("\n !!! x DEVE ESTAR ENTRE -10 E 10 !!!")
                continue
        except:
            print("\n!!! VALOR INVALIDO PARA x !!!")
            continue

    # Entrada e consistência de 'eps'
    while True:
        try:
            eps = input("\nEntre com o valor de eps: ")
            if eps == '':
                eps = b
                break
            eps = float(eps)

            # Verifica se 'eps' é um valor válido (eps > 0 e eps < 1)
            if eps > 0 and eps < 1:
                break
            else:
                print("\n!!! eps DEVE ESTAR ENTRE 0 e 1 !!!")
                continue
        except:
            print("\n!!! VALOR INVALIDO PARA eps !!!")

    # Armazena os valores nas variáveis globais
    a, b = x, eps

    print("\nValores calculados para: ")
    print(f"x = {x}")
    print(f"eps = {eps}")

    # Chama o cálculo passando 'x' e 'eps'
    calcular(x, eps)


def calcular(x, eps):

    # Calculo usando 'math.exp'
    res1 = math.exp(x)

    # Calculo usando soma de séries
    res2 = expSoma(x, eps)

    # Calcula a diferença
    dif = abs(res1 - res2)

    # Imprime resultados
    print("\nExponencial:")
    print(f"Valor calculado usando a função math.exp: {res1}")
    print(f"Valor calculado usando a soma de termos: {res2}")
    print(f"Diferença: {dif}")

# Função que faz a soma de séries
def expSoma(x, eps):
    soma, termo, pot, cont, fat = 1.0, eps, x, 1, 1.0
    while (abs(termo) >= eps):
        termo = pot/fat
        fat *= cont + 1
        soma += termo
        pot *= x
        cont += 1
    return soma

# Início do programa
main()