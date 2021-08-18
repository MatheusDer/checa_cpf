
VALORES = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]  # constante


def valida(cnpj):  # valida o cnpj
    try:
        int(cnpj)
    except ValueError:
        print('Inválido')
        return False

    cnpj_original = str(cnpj)
    sequencia = cnpj_original[0] * len(cnpj_original)  # sequencias tmb checam verdadeiro
    if cnpj_original == sequencia:
        print('Inválido')
        return False

    if len(cnpj_original) != 14:
        print('CNPJ contém apenas 14 digitos.')
        return False

    n_cnpj = valores(cnpj_original)

    if cnpj_original == n_cnpj:
        print('Válido')
        return True

    print('Inválido')
    return False


def valores(cnpj):  # faz a multiplicacao das listas

    n_cnpj = list(cnpj[:-2:])
    val = VALORES
    soma = 0

    for i, j in enumerate(val[1::]):  # soma dos pares das listas
        soma += j * int(n_cnpj[i])

    n_cnpj = numeros(n_cnpj, soma)  # adiciona o penultimo numero
    soma = 0

    for i, j in enumerate(val):
        soma += j * int(n_cnpj[i])

    n_cnpj = numeros(n_cnpj, soma)
    n_cnpj = ''.join(n_cnpj)

    return n_cnpj


def numeros(cnpj, soma):  # checa os valores da soma para adicionar o ultimo e penultimo número

    valor = 11 - (soma % 11)
    if valor > 9:
        cnpj.append('0')
    else:
        cnpj.append(str(valor))

    return cnpj


if __name__ == '__main__':
    # Valores Teste
    # 04252011000110 40688134000161 71506168000111 12544992000105

    while True:
        print()

        cnpj_input = input('Digite o CNPJ: ')
        print(30 * '=')

        valida(cnpj_input)

        print(30*'=')
        print('Deseja checar mais um CNPJ? s/n')

        while True:
            ponto_quebra = input('->')
            if not ponto_quebra.upper() == 'S' and not ponto_quebra.upper() == 'N':
                continue
            else:
                break

        if ponto_quebra.upper() == 'S':
            continue
        else:
            break
