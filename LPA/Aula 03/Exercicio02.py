print('Calculadora')
print('+ Adição')
print('- Subtração')
print('* Multiplicação')
print('/ Divisão')
print('Pressione qualquer outra tecla para sair')

op = input('Qual operação você quer utilizar? ')

if (op == '+' or op == '-' or op == '*' or op == '/'):
    x = int(input('Digite primeiro valor: '))
    y = int(input('Digite segundo valor: '))

    if (op == '+'):
        res = x + y
        print(f'Resultado: {x} + {y} = {res}')
    elif (op == '-'):
        print(f'Resultado: {x} - {y} = {x - y}')
    elif (op == '*'):
        print(f'Resultado: {x} * {y} = {x * y}')
    elif (op == '/'):
        print(f'Resultado: {x} / {y} = {x / y}')

else:
    print('Encerrando o programa...')