preco = float(input('Insira o valor do produto: '))
percentual = float(input('Insira o percentual de desconto (0-100%): '))

desconto = float(preco * (percentual/100))
final = float(preco - desconto)

print(f'O valor do produto é {preco:.1f}. Com o desconto de {percentual:.1f}%.')
print(f'Valor cálculado do desconto {desconto:.1f}. Valor final do produto é {final:.2f}.')
