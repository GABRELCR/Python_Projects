# Programa de cálculo de desconto para vendas da empresa X

# A) Mensagem de boas-vindas com nome e sobrenome
print("Olá, Usuário! Bem-vindo a loja do Gabriel Corrêa Rebustini!")

# B) Entrada do valor unitário e quantidade do produto
preco_un = float(input("Digite o valor unitário do produto: "))
qnt = int(input("Digite a quantidade desejada: "))

# Cálculo do valor total sem desconto
valor_tt = preco_un * qnt

# C) Implementação do desconto conforme as condições
# E) Implementação das estruturas if, elif e else

if (valor_tt < 2500):
    desconto = 0

elif ((valor_tt >= 2500) and (valor_tt < 6000)):
    desconto = 4

elif ((valor_tt >= 6000) and (valor_tt < 10000)):
    desconto = 7

else:  # valor_total_sem_desconto >= 10000
    desconto = 11

# Cálculo do valor do desconto
valor_des = valor_tt * (desconto / 100)

# D) Cálculo do valor total com desconto
valor_tt_des = valor_tt - valor_des

# Apresentação dos resultados
print("\n--- Resumo do Pedido ---")
print(f"Valor total SEM desconto: R$ {valor_tt:.2f}")
print(f"Desconto aplicado: {desconto}% (R$ {valor_des:.2f})")
print(f"Valor total COM desconto: R$ {valor_tt_des:.2f}")

# F) Inserção de comentários relevantes no código
