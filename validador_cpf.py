while 1:
    cpf1, cpfn, sum1, sum2 = [], [], [], []
    cpf = input('Digite apenas os números do seu cpf: ')
    if cpf.isnumeric():
        for i, j in enumerate(cpf):
            j = int(j)
            cpf1.append(j)
            if i < 9:
                cpfn.append(j)
                sum1.append(j*(10-i))

        if 11 - (sum(sum1) % 11) > 9:
            cpfn.append(0)
        else:
            cpfn.append(11 - (sum(sum1) % 11))

        for i, j in enumerate(cpfn):
            if i < 10:
                sum2.append(j * (11 - i))

        if 11 - (sum(sum2) % 11) > 9:
            cpfn.append(0)
        else:
            cpfn.append(11 - (sum(sum2) % 11))
        break
    else:
        print('Digite apenas números')

if cpf1 == cpfn:
    print('Cpf válido')
else:
    print('Cpf inválido')
