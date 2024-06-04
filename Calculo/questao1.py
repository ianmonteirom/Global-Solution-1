import numpy as np
import matplotlib.pyplot as plt

# Dados do número de indivíduos por ano e dos anos
num_indivs = np.array([1190, 1155, 1030, 1015])
anos = np.array([0, 1, 2, 3])

# Ajuste da curva aos dados
coeficientes = np.polyfit(anos, num_indivs, 2)
a, b, c = coeficientes

# Calculo dos valores da curva ajustada
curva_ajustada = a * anos**2 + b * anos + c

# Estimativa da população de mamíferos aquáticos em 5 anos
t = 5
num_indivs_5anos = a * t**2 + b * t + c

# Encontrando o tempo onde a população é mínima
tempo_minimo = -b / (2 * a)

# Respostas para a questão 1 da GS
print('--' * 50)
print('Differenciated Problem Solving - Global Solution Maio/Junho 2024 - Questão 1'.center(50 * 2))
print('--' * 50)

print('Questão 1')
print(f'1a) Função obtida ajustando a curva: {a:.0f}t² + {b:.0f}t + {c:.0f}\n'
      f'1b) Tamanho da população em 5 anos: {num_indivs_5anos:.0f}\n'
      f'1c) Não há um momento em que a população chega a 0 indivíduos, pois o delta desta função é negativo para quando'
      f' N(t) = 0.\n'
      f'1d) O menor tamanho da população será daqui a {tempo_minimo:.0f} anos\n'
      f'1e) Não é possível estimar o maior tamanho da população, pois o gráfico desta função é uma parábola positiva, e '
      f'teoricamente ela cresce infinitamente, sendo impossível estimar o maior valor, entretanto é possível estimar o '
      f'menor valor, pois a parábola positiva tem um mínimo, sendo este 8 anos, após este valor, a parábola começa a '
      f'crescer.')

# Plota o gráfico com os dados e a curva ajustada
plt.scatter(anos, num_indivs, label='Dados Originais')
plt.plot(anos, curva_ajustada, color='red', label=f'Curva Ajustada')
plt.xlabel('Ano')
plt.ylabel('Número de Indivíduos')
plt.title('Ajuste de curva para recuperação de mamíferos aquáticos')
plt.legend()
plt.grid(True)
plt.show()
