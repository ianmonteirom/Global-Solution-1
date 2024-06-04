import numpy as np
import matplotlib.pyplot as plt

tam_inicial = 10
cresc_mes = 0.03
num_meses = 55
capacidade_disco = 50

# Calcula o tamanho da base de dados para cada mês, e a quantidade de meses até chegar a 50tb de uso
tamanhos = [tam_inicial * (1 + cresc_mes) ** i for i in range(num_meses)]

tamanho_base_dados = tam_inicial
qnt_meses = 0
while tamanho_base_dados <= capacidade_disco:
    qnt_meses += 1
    tamanho_base_dados = tam_inicial * (1 + cresc_mes) ** qnt_meses

# Respostas para a questão 2 da GS
print('--' * 50)
print('Differenciated Problem Solving - Global Solution Maio/Junho 2024 - Questão 2'.center(50 * 2))
print('--' * 50)

print("""Uma base de dados de escaneamento 3d de oceanos está sendo
construída. Ela atualmente contém 10 tb em dados, e estima-se que
haverá um crescimento de 3% ao mês nessa quantidade de dados.
""")
print(f'2a) Quantidade de dados consumida pela aplicação em 1 ano de acordo com o gráfico: aproximadamente 13.84 TB\n'
      f'2b) De acordo com o gráfico, aplicação ainda poderá rodar no disco rígido atual do servidor por {qnt_meses} '
      f'meses, até chegar a 50 tb.')

meses = np.arange(1, num_meses + 1)
plt.plot(meses, tamanhos, marker='o', linestyle='-')
plt.title('Crescimento Mensal da Base de Dados de Escaneamento 3D dos Oceanos')
plt.xlabel('Mês')
plt.ylabel('Tamanho da Base de Dados (TB)')
plt.grid(True)
plt.xticks(meses)
plt.show()
