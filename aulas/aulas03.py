import matplotlib.pyplot as plt

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho']
vendas = [200, 300, 305, 340, 360, 400]

#Gráficos de Linhas
plt.plot(meses, vendas, color='gold')
plt.title('Vendas no Primeiro Semestre')

plt.xlabel('Meses')
plt.ylabel('Vendas')

plt.show()
plt.savefig('aula03')