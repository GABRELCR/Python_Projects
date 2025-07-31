# A) Mensagem de boas-vindas com nome e sobrenome
print("Olá, Usuário! Bem-vindo à loja de Açaí e Cupuaçu do Gabriel Corrêa Rebustini!\n")

# Cardápio
print('-'*13 + 'Nosso Cardápio' + '-'*13)
print('Tamanho | Cupuaçu (CP) | Açaí (AC)')
print("-" * 40)
print('| P | R$ 09.00 | R$ 11.00 |')
print('| M | R$ 14.00 | R$ 16.00 |')
print('| G | R$ 18.00 | R$ 20.00 |')
print("-" * 40 + "\n")

# Inicializa o acumulador de pedidos
valor_tt= 0

# Loop principal para permitir múltiplos pedidos
while True:
    # B) Entrada do sabor (CP/AC)
    # G) Implementação das estruturas while e break
    while True:
        sabor = input("Digite o sabor desejado (CP para Cupuaçu / AC para Açaí): ").upper()
        if sabor == 'CP' or sabor == 'AC':
            break
        else:
            print("Sabor inválido. Tente novamente.")
            continue # Volta ao início do loop de sabor

    # C) Entrada do tamanho (P/M/G)
    while True:
        tamanho = input("Digite o tamanho desejado (P/M/G): ").upper()
        if tamanho == 'P' or tamanho == 'M' or tamanho == 'G':
            break
        else:
            print("Tamanho inválido. Tente novamente.")
            continue # Volta ao início do loop de tamanho

    preco = 0

    # D) Implementação de if, elif e else aninhados para definir o preço
    if sabor == 'CP':
        if tamanho == 'P':
            preco = 9
        elif tamanho == 'M':
            preco = 14
        elif tamanho == 'G':
            preco = 18
    elif sabor == 'AC':
        if tamanho == 'P':
            preco = 11
        elif tamanho == 'M':
            preco = 16
        elif tamanho == 'G':
            preco = 20

    # E) Acumula o valor do pedido atual
    valor_tt += preco
    print(f"Você pediu {sabor} tamanho {tamanho} no valor de R$ {preco:.2f}.")

    # F) Pergunta se deseja pedir mais alguma coisa
    while True:
        mais = input("Deseja pedir mais alguma coisa? (Sim/Não): ").upper()
        if mais == 'SIM':
            break # Sai do loop de confirmação e volta ao início para um novo pedido
        elif mais == 'NÃO':
            break # Sai do loop de confirmação e vai para o encerramento
        else:
            print("Resposta inválida. Digite Sim ou Não.")
            continue # Volta ao início do loop de confirmação

    if mais == 'NÃO':
        break # Encerra o loop principal de pedidos

# F) Print do acumulador ao final
print(f"\nValor total do seu pedido: R$ {valor_tt:.2f}")
print("Obrigado pela sua compra!")

# H) Inserção de comentários relevantes