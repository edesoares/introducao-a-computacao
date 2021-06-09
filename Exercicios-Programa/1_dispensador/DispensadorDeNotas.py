# MAC110 - Introdução à Computação
# Primeiro Semestre de 2021
# BMAC–IMEUSP
# Aluno: Edgar Soares Marinho
# nºUSP: 9337691

# Entrada de dados, contagem do total de cédulas e tratamento de excessão
# Retorna o total de cada cédula durante a execução do programa
totCem, totCinq, totVinte, totDez = 0,0,0,0
cem, cinq, vinte, dez = 0,0,0,0

def inicio():
    global totCem, totCinq, totVinte, totDez
    global cem, cinq, vinte, dez
    print("#### INICIANDO SAQUE ####")
    print("\nCédulas disponíveis: R$10, R$20, R$50 e R$ 100")
    while True:
        try:
            valor = int(input("\nDigite o valor para o saque: "))
        except:
            print("\n!!! Valor não é um numero !!!\n")
        else:
            if (valor < 0):
                print("\n!!! Valor inválido !!!\n")
            elif (valor == 0):
                break
            elif (valor % 10 == 0):
                opcao(valor)
                totCem += cem
                totCinq += cinq
                totVinte += vinte
                totDez += dez
            else: print("\n!!! Não temos cédulas para este valor !!!\n")

# Função que conta as cédulas. Recebe o valor e a cédula a partir da qual ele deve
# começar a contagem. Retorna as quantidades de cada cédula, durante a atual contagem,
# pra função opcao()
def contaCed(cedAtual, valor):
    global cem, cinq, vinte, dez
    resto = valor
    numcedulas = 0
    while True:
        if cedAtual <= resto:
            resto -= cedAtual
            numcedulas += 1
        else:
            if numcedulas > 0:
                print(f"{numcedulas} cédula(s) de R${cedAtual},00")
                if cedAtual == 100:
                    cem = numcedulas
                elif cedAtual == 50:
                    cinq = numcedulas
                elif cedAtual == 20:
                    vinte = numcedulas
                elif cedAtual == 10:
                    dez = numcedulas                
            if resto == 0:
                break
            if cedAtual == 100:
                cedAtual = 50
            elif cedAtual == 50:
                cedAtual = 20
            elif cedAtual == 20:
                cedAtual = 10
            numcedulas = 0

## Função que verifica se o cliente quer ou não proceder com a operação de saque
# Recebe o valor da função inicio(), inicia pela cédula de cem, chama o contador,
# verifica se o cliente quer prosseguir (só aceita s ou n). Se sim, retorna as
# quantidades de cada cédula neste saque pra função inicio(). Se não, ele zera
# as qtdes e inicie outra contagem começando pela cédula de R$ 50 (o count determina
# qual o valor da cédula inicial).
def opcao(valor):
    global cem, cinq, vinte, dez
    check = 'n'
    count = 0
    if (valor <= 10):
        count = 3
    elif (valor <= 20):
        count = 2
    elif (valor <= 50):
        count = 1
    while (check != 's'):
        cem, cinq, vinte, dez = 0,0,0,0
        print("\nQuantidade de cédulas a serem sacadas:")
        if count == 0:
            cedAtual = 100
            contaCed(cedAtual, valor)
            count += 1   
        elif count == 1:
            cedAtual = 50
            contaCed(cedAtual, valor)
            count += 1
        elif count == 2:
            cedAtual = 20
            contaCed(cedAtual, valor)
            count += 1
        elif count == 3:
            cedAtual = 10
            contaCed(cedAtual, valor)
            count = 0
        while True:
            try:
                check = input("\nDeseja sacar desta forma (s/n)? ")
            except:
                print("\n!!! Entrada inválida !!!")
            else:
                if (check == 's' or check == 'n'):
                    break
                else:
                    print("\n !!! Entrada inválida. Favor digite s ou n !!!")

## Chamada da função inicio() que retorna as quantidades totais de cédulas durante
# toda a execução do programa
inicio()

## Imprime os totais
print("\n# # # # Fim da operação # # # #\n")
print("Total de notas sacadas:")
print(f"{totCem} nota(s) de R$100")
print(f"{totCinq} nota(s) de R$50")
print(f"{totVinte} nota(s) de R$20")
print(f"{totDez} nota(s) de R$10")
print(f"\nValor total: R${((totCem*100)+(totCinq*50)+(totVinte*20)+(totDez*10))},00")