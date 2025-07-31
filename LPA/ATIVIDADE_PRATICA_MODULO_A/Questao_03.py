# A) Mensagem de boas-vindas com o nome e opções de serviço
print("Olá, Usuário! Bem-vindo a copiadora do Gabriel Corrêa Rebustini.")

# Opções de serviços para o usuário
print("\n--- Opções de Serviço ---")
print("DIG - Digitalização: R$ 1.10 por página")
print("ICO - Impressão Colorida: R$ 1.00 por página")
print("IPB - Impressão Preto e Branco: R$ 0.40 por página")
print("FOT - Fotocópia: R$ 0.20 por página")
print("-------------------------\n")

# Define os preços dos serviços
preco_dig = 1.10
preco_ico = 1.00
preco_ipb = 0.40
preco_fot = 0.20

# Define os preços dos serviços extras
preco_es = 15.00
preco_ecd = 40.00
preco_se = 0.00

# B) Função para escolher o serviço
def escolha_servico():

    # Pergunta ao usuário o serviço desejado e retorna o preço por página do serviço.
    # Repete a pergunta se a opção for inválida.

    while True:
        servico = input("Digite o serviço desejado: ").lower()

        if servico == 'dig':
            return preco_dig
        elif servico == 'ico':
            return preco_ico
        elif servico == 'ipb':
            return preco_ipb
        elif servico == 'fot':
            return preco_fot
        else:
            print("Opção de serviço inválida. Tente novamente.")

# C) Função para obter o número de páginas com desconto
def num_pagina():

    # Pergunta ao usuário o número de páginas e retorna o número de páginas com desconto aplicado.
    # Repete a pergunta se o valor for não numérico ou acima do limite.

# F) Implementação do try e except
    while True:
        try:
            num = int(input("Digite o número de páginas: "))

            if num >= 20000:
                print("Quantidade de páginas não aceita. O limite é 19999.")
            else:
                if num >= 2000:
                    return num * (1 - 0.25) # 25% de desconto
                elif num >= 200:
                    return num * (1 - 0.20) # 20% de desconto
                elif num >= 20:
                    return num * (1 - 0.15) # 15% de desconto
                else:
                    return num # Sem desconto
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")

# D) Função para escolher o serviço extra
def servico_extra():

    # Pergunta ao usuário se deseja algum serviço extra e retorna o valor do serviço extra.
    # Repete a pergunta se a opção for inválida.

    while True:

        # Opções de serviços extras para o usuário

        print("\n--- Serviços Extras ---")
        print("0 - Não desejo serviço extra")
        print("1 - Encadernação Simples: R$ 15.00")
        print("2 - Encadernação Capa Dura: R$ 40.00")
        print("-------------------------\n")

        extra = input("Deseja algum serviço extra? ")

        if extra == '0':
            return preco_se
        elif extra == '1':
            return preco_es
        elif extra == '2':
            return preco_ecd
        else:
            print("Opção de serviço extra inválida. Tente novamente.")

# E) Cálculo do total a pagar (código principal - main)
if __name__ == "__main__":
    # Exemplo de interação com o usuário
    preco = escolha_servico()
    num_pag_desconto = num_pagina()
    valor_extra = servico_extra()

    # Calcula o valor total da conta
    total = (preco * num_pag_desconto) + valor_extra

    # Apresenta o valor total
    print(f"\n--- Resumo da Cobrança ---")
    print(f"Preço por página do serviço: R$ {preco:.2f}")
    print(f"Número de páginas (com desconto): {int(num_pag_desconto)}")
    print(f"Valor do serviço extra: R$ {valor_extra:.2f}")
    print(f"Valor total a pagar: R$ {total:.2f}")

# G) Inserção de comentários relevantes