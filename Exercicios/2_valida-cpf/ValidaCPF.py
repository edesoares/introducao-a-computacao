# MAC110 - Introdução à Computação
# Primeiro Semestre de 2021
# BMAC–IMEUSP
# Aluno: Edgar Soares Marinho
# nºUSP: 9337691

def main ():
    while True:
        try:
            # Recebe o número do CPF do usuário como String.
            cpf = input('Digite o número do CPF: ')

            # Encerra o programa se for digitado '0'.
            if cpf == '0':
                break
            else:
                # Chama a função que verifica os dígitos. Ela recebe como argumentos, respectivamente,
                # o controlador indicando o dígito que vai ser verificado e o CPF inserido.  
                d10 = verificador(10, cpf)
                d11 = verificador(11, cpf)

            # Retorno da validação pro usuário.
            if d10 and d11:
                print('### CPF VALIDO ###')
            else:
                print('### CPF INVALIDO ###')
        except:
            print('### ENTRADA INVALIDA ###')

# Função que faz a verificação dos dígitos. Eu abstraí a lógica da verificação
# passando o dígito como argumento no parâmetro 'controlador'. Assim eu não
# preciso de duas funções iguais pra verificar cada dígito.
def verificador (controlador, cpf):

    # Verifica que a quantidade de dígitos é válida. Se não for, joga a excessão pra
    # ser tratada na função main.
    if len(cpf) != 11:
        raise

    # Variáveis de controle pra ajudar com as operações de verificação.
    contador = 0
    soma = 0

    # Identifica o digito na String inserida de acordo com o controlador.
    for i in cpf:
        contador += 1
        if contador == controlador:
            digito = int(i)
            break

    # Calcula o valor esperado pro digito conforme a fórmula de verificação.
    for j in cpf:
        aux = int(j)
        soma += aux * contador
        if contador == 2:
            break
        contador -=1
    aux = soma % 11
    if aux < 2:
        digEsperado = 0
    else:
        digEsperado = 11 - aux

    # Verifica se o digito separado é igual o digito esperado conforme o cálculo que foi feito.
    if digito == digEsperado:
        return True
    else:
        return False

# Início do programa
main()