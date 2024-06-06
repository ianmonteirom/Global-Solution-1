import numpy as np
import matplotlib.pyplot as plt

# Preço inicial do ingresso e quantidade inicial de vendas
preco_ingresso = 50
vendas_ingressos = 800

# Lista para armazenar os preços dos ingressos e as vendas correspondentes
precos = []
vendas = []
receitas = []

# Adicionando o preço inicial e as vendas iniciais às listas
precos.append(preco_ingresso)
vendas.append(vendas_ingressos)
receitas.append(preco_ingresso * vendas_ingressos)

# Calculando as vendas e os preços para cada aumento de R$5 no preço do ingresso, chegando até R$150
for i in range(1, 21):
    preco_ingresso += 5
    vendas_ingressos -= 20
    precos.append(preco_ingresso)
    vendas.append(vendas_ingressos)
    receitas.append(preco_ingresso * vendas_ingressos)

# Convertendo as listas para arrays NumPy
precos = np.array(precos)
vendas = np.array(vendas)
receitas = np.array(receitas)


# Respostas para a questão 3 da GS
print('--' * 50)
print('Differenciated Problem Solving - Global Solution Maio/Junho 2024 - Questão 3'.center(50 * 2))
print('--' * 50)

print("""Uma conferência sobre desenvolvimento sustentável está em curso, e deseja-se estudar
a relação entre preço do ingresso e receita.
Estimamos que, ao vender cada ingresso por 50 reais, conseguiremos vender 800
ingressos. Mas, para cada aumento de 5 reais no preço, estimamos uma redução de 20
vendas.
""")
print(f'3a) De acordo com o gráfico, para cada R$5 de aumento no preço do ingresso, é estimada a redução de 20 vendas '
      f'do ingresso\n'
      f'3b) De acordo com o gráfico, ao preço de R$115, o número de vendas está estimada em 540\n'
      f'3c) Visto que o valor da receita é dada pelo Preço do Ingresso x Quantidade de Vendas e de acordo com o gráfico'
      f' R$70 de preço x 720 vendas = R$50.400 de receita, se diminuir o preço do ingresso para R$69.45 e '
      f'manter a quantidade de vendas em 720, o valor de vendas será aproximadamente R$50.000.\n'
      f'3d) A receita máxima possível de acordo com o segundo gráfico é de R$62.500 com o valor do ingresso de R$125'
      f', pois é o ponto máximo da parábola do gráfico da Receita (R$) vs Preço do Ingresso (R$), após esse ponto o '
      f'valor da receita começa a descer. ')


# Plotando o gráfico de Preço do Ingresso x Quantidade de Vendas
plt.plot(precos, vendas, marker='o')
plt.title('Preço do Ingresso vs Quantidade de Vendas')
plt.xlabel('Preço do Ingresso (R$)')
plt.ylabel('Quantidade de Vendas')
plt.grid(True)
plt.show()

# Plotando o gráfico de Receita x Preço
plt.plot(precos, receitas, marker='o')
plt.title('Valor da Receita vs Preço do Ingresso')
plt.xlabel('Preço do Ingresso (R$)')
plt.ylabel('Receita (R$)')
plt.grid(True)
plt.show()
