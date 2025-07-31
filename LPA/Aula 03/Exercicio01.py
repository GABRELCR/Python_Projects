A = float(input('Digite o 1º lado do triângulo: '))
B = float(input('Digite o 2º lado do triângulo: '))
C = float(input('Digite o 3º lado do triângulo: '))

if ((A > 0 and B > 0 and C > 0) and (A + B > C and A + C > B and B + C > A)):
    #Se chegou até aqui, é porque o triângulo é válido
    if (A!= B and A != C and B != C):
        print('Triângulo escaleno')
    elif (A == B and B == C):
        print('Triângulo equilátero')
    else:
        print('Triângulo isósceles')
else:
    print('Um dos valores indicados não servem para formar um triângulo')