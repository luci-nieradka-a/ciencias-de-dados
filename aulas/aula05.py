import pandas as pd
import matplotlib.pyplot as plt

# Cria um DataFrame a ártir de um arquivo CSV
df = pd.read_csv('./dados/dados.csv')

# Exibe as primeiras linhas do DataFrame
print(df.head()) 

# Gráficos de boxplot
plt.boxplot(df['nota'])
plt.title('Boxplot das notas')
plt.ylabel('Notas')
plt.show()
plt.savefig('aula05-boxplot')