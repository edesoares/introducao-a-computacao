# MAC110 - Introdução à Computação
# Primeiro Semestre de 2021
# BMAC–IMEUSP
# Aluno: Edgar Soares Marinho
# nºUSP: 9337691

from random import seed, randrange

# Função principal
def main():
    while True:

        # Essa variável 'resp' precisa ser inicializada antes do while onde ela é verificada
        resp = ""
        print("\n" + 4*"#"+ " HISTOGRAMA " + 4*"#" + "\n")

        # Chama a entrada de dados recebendo 'a', 'b' e 'n'
        a, b, n = entrada()

        am = geraAmostra(a, b, n)
        imprimeAmostra(am)

        # Esse trecho permite o usuário escolher o numero de intervalos 'i' exibido pelo gráfico
        # se o valor for igual a zero a impressão é encerrada e se for menor que 0, retorna erro.
        while True:
            try:
                i = int(input("\nEntre com o numero de intervalos (ou 0 para encerrar): "))
                if i == 0:
                    break
                if i < 0:
                    print("\n!!! ERRO - Numero inválido de intervalos !!!\n")
                    continue
            except:
                print("\n!!! ERRO - Valor inválido !!!\n")
                continue
            else:

                # Não havendo erros nem encerrando, ele chama a função que faz o histograma
                # passando 'a', 'b', 'i' e 'am'
                histograma(a, b, i, am)
        
        # Se a impressão do gráfico for encerrada, ele pergunta se o usuário deseja entrar com
        # novos dados ou encerrar o programa
        while resp != "N" and resp != "S":

            resp = input("\nDeseja executar novamente? (s/n): ")
            if resp.upper() == "S" or resp.upper() == "N":
                break
            else:
                print("\n!!! ERRO - Entrada inválida !!!\n")
                continue
        if resp.upper() == "S":
            continue
        else:
            break

# Função que faz a entrada e a consistência dos dados. Retorna 'a', 'b' e 'n'
def entrada():
    while True:
        try:
            a = float(input("Limite inferior: "))
            b = float(input("Limite superior: "))

            # Verifica se o limite superior é maior que o limite inferior
            if a > b: 
                print("\n!!! ATENÇÃO - O limite superior deve ser maior que o limite inferior !!!\n")
                continue

            n = int(input("Quantidade de elementos da amostra: "))

            # Verifica se o intervalo é válido
            if (b - a)/n < 0.001:
                print("\n!!! ATENÇÃO - O intervalo entre os limites deve ser maior do que 0.001 !!!\n")
                continue
            else:
                break
        except:
            print("\n!!! ERRO - Valor inválido !!!\n")
            continue
    return a, b, n

# Gera n números aleatórios no intervalo [a, b] usando meu nUSP como semente.
# Retorna um array 'amostra' com esses numeros
def geraAmostra(a, b, n):

    # Use o seu NUSP como semente
    NUSP = 9337691
    seed(NUSP)
    amostra = n * [0]
    for k in range(n):
        amostra[k] = a + float(randrange(1000000)) * (b - a)/1000000.0
    return amostra

# Imprime a amostragem a partir do vetor 'amostra'
def imprimeAmostra(am):

    # imprime 5 elementos por linha
    am.sort()
    print("\nAmostra:")
    for k in range(len(am)):
        if k % 5 == 4:
            print("%10.5f" % am[k])
        else:
            print("%10.5f" % am[k], end=' ')
    print("")

# Calcula o histograma a partir do numero de intervalos 'i' e da amostragem 'am'   
def histograma(a, b, i, am): 
    x, cont, freqDe, freqA  = 0, 0, 0.0, a
    dif = abs(b - a)
    frequencia = dif/i

    # Imprime o cabeçalho da tabela
    imprimeHistograma("\nIntervalo", "Frequência", "Gráfico")
    while freqA < b:
        freqDe = freqA
        freqA = round((freqA + frequencia),5)
        if freqA > b:
            break
        freqTxt = "De " + "{:.3f}".format(freqDe) + " a " + "{:.3f}".format(freqA)
        while x < len(am):
            if am[x] > freqDe and am[x] <= freqA:
                cont+= 1
            x += 1
        graf = cont*"\u2593 "

        # Imprime as linhas da tabela
        imprimeHistograma(freqTxt, cont, graf)
        cont = 0
        x = 0
        freqTxt = ""

# Função que imprime os dados do histograma
def imprimeHistograma(a, b , c):
    print ("{:<30} {:<15} {:<10}".format(a, b, c))

# Início do programa
main()    