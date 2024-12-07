import numpy as np

# Funções de pertinência (triangular e trapezoidal)
def triangular(x, a, b, c):
    """Função de pertinência triangular."""
    return np.maximum(0, np.minimum((x - a) / (b - a), (c - x) / (c - b)))

def trapezoidal(x, a, b, c, d):
    """Função de pertinência trapezoidal."""
    return np.maximum(0, np.minimum(np.minimum((x - a) / (b - a), 1), (d - x) / (d - c)))

# Entradas fornecidas
v_input = 160  # Velocidade em km/h
m_input = 3.5  # Massa em toneladas

# Definições das variáveis fuzzy
x_velocidade = np.linspace(0, 200, 1000)  # Velocidade de 0 a 200 km/h
x_massa = np.linspace(0, 10, 1000)        # Massa de 0 a 10 toneladas
x_pressao = np.linspace(0, 100, 1000)     # Pressão de 0 a 100 unidades

# Funções de pertinência para Velocidade
vel_MB = trapezoidal(x_velocidade, 0, 0, 20, 50)
vel_BA = triangular(x_velocidade, 20, 50, 80)
vel_ME = triangular(x_velocidade, 50, 80, 120)
vel_AL = triangular(x_velocidade, 100, 140, 160)
vel_MA = trapezoidal(x_velocidade, 140, 160, 200, 200)

# Funções de pertinência para Massa
mass_MP = trapezoidal(x_massa, 0, 0, 1, 2)
mass_PE = triangular(x_massa, 1, 2, 3)
mass_ME = triangular(x_massa, 2, 4, 6)
mass_GR = triangular(x_massa, 4, 6, 8)
mass_MG = trapezoidal(x_massa, 6, 8, 10, 10)

# Funções de pertinência para Pressão
press_MI = trapezoidal(x_pressao, 0, 0, 20, 40)
press_ME = triangular(x_pressao, 20, 50, 80)
press_EL = trapezoidal(x_pressao, 60, 80, 100, 100)

# Calcular graus de pertinência para as entradas
mu_v_MB = np.interp(v_input, x_velocidade, vel_MB)
mu_v_BA = np.interp(v_input, x_velocidade, vel_BA)
mu_v_ME = np.interp(v_input, x_velocidade, vel_ME)
mu_v_AL = np.interp(v_input, x_velocidade, vel_AL)
mu_v_MA = np.interp(v_input, x_velocidade, vel_MA)

mu_m_MP = np.interp(m_input, x_massa, mass_MP)
mu_m_PE = np.interp(m_input, x_massa, mass_PE)
mu_m_ME = np.interp(m_input, x_massa, mass_ME)
mu_m_GR = np.interp(m_input, x_massa, mass_GR)
mu_m_MG = np.interp(m_input, x_massa, mass_MG)

# Coletar os graus de pertinência
mu_v = [mu_v_MB, mu_v_BA, mu_v_ME, mu_v_AL, mu_v_MA]
mu_m = [mu_m_MP, mu_m_PE, mu_m_ME, mu_m_GR, mu_m_MG]

mu_v, mu_m  # Retornar os graus de pertinência calculados para as entradas
