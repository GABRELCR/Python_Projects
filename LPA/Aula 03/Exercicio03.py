kwh = float (input('Digite a quantidade em KW/h consumida: '))
tipo = input('Digite o tipo da instalação? (R, C ou I): ')
preco = float(0)

if (tipo == 'R' or tipo == 'C' or tipo == 'I'):

    if(tipo == 'R'):
        if (kwh >= 500):
            preco = 0.65
        else:
            preco = 0.4

    elif (tipo == 'C'):
        if (kwh >= 1000):
            preco = 0.6
        else:
            preco = 0.55

    elif (tipo == 'I'):
        if (kwh >= 5000):
            preco = 0.6
        else:
            preco = 0.55

    print(f'Total a pagar: {kwh * preco:.2f}')
else:
    print('Tipo de instalação invalido. Encerrando...')