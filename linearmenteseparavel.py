import matplotlib.pyplot as plt
import numpy as np

# Dados de exemplo
x = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])
y = np.array([0, 1, 1, 0])  # XOR

# Plotar os dados
for i, label in enumerate(np.unique(y)):
    plt.scatter(x[y == label, 0], x[y == label, 1], label=f'Classe {label}')
plt.legend()
plt.title('Visualização dos Dados')
plt.show()



