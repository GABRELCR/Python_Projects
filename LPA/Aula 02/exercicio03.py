frase = input('Digite uma frase: ') #usuario insere a frase
tam = len(frase) #descobrir o tamanho da string

metade = frase[:int(tam/2)] #pegar a metade da frase do inicio ao meio

print(metade[-2:]) #Acessa a variavel do fim para o inicio