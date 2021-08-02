# MAC110 - Introdução à Computação
# Primeiro Semestre de 2021
# BMAC–IMEUSP
# Aluno: Edgar Soares Marinho
# nºUSP: 9337691

from random import randrange

# Coloquei esse trecho de código pq o python não tava
# encontrando o arquivo de dentro do conda environment.
# Achei prudende deixar assim pra garantir que, desde
# que o arquivo esteja na mesma pasta do script, ele
# o encontre independente do ambiente de desenvolvimento.
import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# Função principal
def main():
    print("\n"+(8*"# ")+"PALPITES DA MEGA-SENA"+ (8*" #")+"\n")

    # Chama a função 'lerArquivo()' e recebe a matriz com dados
    jogosMega = lerArquivo()

    print("\n\tEscolha de apostas")
    while True:
        
        # Chama 'escolheAposta()' recebe um vetor com os numeros da aposta
        aposta = escolheAposta()

        # Chama 'validaAposta()' passando a matriz com os jogos anteriores e
        # a aposta. Recebe um valor booleano em 'valida'
        valida = validaAposta(jogosMega, aposta)

        # Se a aposta não for válida, gera uma nova    
        if valida == False:
            print("\nGerar nova aposta:")
            continue
        else:
        # Se for válida, chama a função 'repetir()' passando a variável 'valida' essa
        # função vai aproveitar a variável pra ver se o usuário quer gerar nova aposta
            valida = repetir(valida)
            if valida == False:
                print("\nGerar nova aposta")
                continue
            else:
                break
    # Fim do programa        
    print("\n"+(8*"# ")+"Programa encerrado"+ (8*" #")+"\n")

# Função que lê o arquivo txt
def lerArquivo():

    #Inicializa a matriz que vai receber os dados
    jogosMega = []

    # Tratamento de excessão caso haja erro pra abrir o arquivo
    while True:
        try: 
            # Recebe o nome do arquivo 
            nome = input("Entre com o nome do arquivo: ") 

            #nome = "megasena2021.txt" # Pra agilizar os testes

            # Lê o arquivo e armazena o conteúdo na variável "arq"
            arq = open(nome, "r")

            i = 0
            for linha in arq:                
                try:
                    lin = linha[:len(linha) - 1] # Tira o \n do final
                    item = lin.split('\t') # Separa os elementos da string
                    jogosMega.append([]) # Adiciona uma nova linha a matriz

                    # Transforma os strings numéricos em números inteiros
                    for j in range(8):
                        if j == 1:
                            jogosMega[i].append(item[1])
                        else:
                            jogosMega[i].append(int(item[j]))
                    i = i + 1
                except:
                    # Se houver erro na leitura do arquivo
                    raise ValueError("\n!!! Erro de leitura. A formatação do arquivo é inválida !!!\n")

            # Chama a consistência da matriz retornando um booleano e uma mensagem de erro, se houver
            verifica, msg = consistMatriz(jogosMega)

            # Se a consistencia retornar falso, exibe essa mensagem de erro com a string que retornou
            if not verifica:
                raise ValueError("\n!!! Erro de consistência. "+msg+" !!!\n")

        # Em caso de erro na leitura do arquivo            
        except ValueError as e:
            print(e)
            continue 
        # Em caso de erro pra abrir o arquivo   
        except:
            print("\n!!! Erro na abertura do arquivo !!!\n")
            continue
  
        # Fecha arquivo e retorna a matriz
        arq.close()
        return jogosMega

# Função que faz a consistência dos dados da matriz. Retorna um booleano
# e uma mensagem de erro
def consistMatriz(mat):
    verifica = True
    msg = ""
    for n in mat:
        if n[0] <= 0:
            verifica = False
            msg = "O arquivo contém índice de sorteio menor que 0"
        if len(n[1]) != 10:
            verifica = False
            msg = "O arquivo contém data em formato inválido"
        for k in range (2, len(n)):
            if n[k] <= 0 or n[k] > 60:
                verifica = False
                msg = "O arquivo contém numero de sorteio menor que 0 ou maior que 60"
    return verifica, msg

# Interage com o usuário pra saber qtos numeros vai ter a aposta
def escolheAposta():
    while True:
        try:
            # Recebe o valor
            numAposta = int(input("Quantidade de números da aposta: "))
            if numAposta < 6 or numAposta > 12:
                # Consistência
                print("\n!!! Digite um numero entre 6 e 12 !!!\n")
                continue
        # Tratamento de excessão
        except:
            print("\n!!! ERRO - Valor inválido !!!\n")
            continue
        else:
            print(f"\nAposta escolhida {numAposta} numeros:\n")
            #Deixei isso aqui pra testar uma aposta que já aconteceu
            #aposta = [53, 17, 38, 4, 47, 37, 42, 15]

            # Chama 'geraAposta()' recebe o vetor com os numeros da aposta
            aposta = geraAposta(numAposta)
            # Imprime na tela
            for n in aposta:
                print(n, end ="\t")
            # Retorna a aposta gerada
            return aposta

# Gera uma aposta com base na qtde de numeros que o usuário escolheu
def geraAposta(n):
    aposta = []
    k = 0
    while k < n:
        num = randrange(1, 61)
        if num not in aposta:
            aposta.append(num)
            k+=1
    # Retorna a aposta
    return aposta

# Verifica se a aposta gerada contém numeros já sorteados
def validaAposta(jogosMega, aposta):
    for n in jogosMega:
        vet = []
        for k in range(2,len(n)):
            # Coloca somente os numeros de cada sorteio num vetor temporário
            vet.append(n[k])
        # Compara o sorteio com a aposta gerada. Se coincidir, imprime quando
        # foram sorteados esses numeros e retorna 'False'
        if set(aposta).issuperset(vet):
            print(f"\n\nNumeros já sorteados no sorteio {n[0]} de {n[1]}")
            return False
    # Se não, imprime "Aposta válida" e retorna True
    print("\n\nAposta Válida!\n")
    return True

# Aproveita a variável 'valida' pra ver se o usuário quer gerar nova aposta
def repetir(valida):
    while True:
        try:
            r = input("\nDeseja gerar nova aposta? (s/n) ")
            if r.upper() == 'S':
                valida = False
            elif r.upper() == 'N':
                valida = True
            else:
                raise 
            return valida                    
        except:
            print("\n!!! Erro! Responda 's' ou 'n' !!!\n")
            continue
# Inicia o programa
main()