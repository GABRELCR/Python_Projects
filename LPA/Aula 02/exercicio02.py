km= float(input('Insira o valor dos quilometros(km) percorridos: '))
dias= int(input('Insira a quantidade de dias que alugou o carro: '))

preco= float(dias*60+km*0.15)

print(f'quilometros(km) percorridos: {km} km. Em {dias} dia(s). O total a pagar será de R${preco:.2f}')