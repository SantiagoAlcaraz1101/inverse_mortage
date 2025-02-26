import numpy as np
import matplotlib.pyplot as plt

# Parámetros
V0 = 100  # valor inicial
mu = 0.05  # tasa de retorno
sigma = 0.2  # volatilidad
T = 1  # tiempo total en años
dt = 0.01  # tamaño del paso de tiempo
n_steps = int(T / dt)  # número de pasos
t = np.linspace(0, T, n_steps)  # vector de tiempos

# Generación de un proceso de Wiener (ruido blanco)
W = np.random.normal(0, np.sqrt(dt), size=n_steps)  # Incrementos de Wiener
W = np.cumsum(W)  # Sumando los incrementos para obtener el proceso de Wiener

# Cálculo de Vt según la fórmula
V = V0 * np.exp((mu - 0.5 * sigma**2) * t + sigma * W)

# Graficando el resultado
plt.plot(t, V)
plt.title("Simulación de Geometric Brownian Motion")
plt.xlabel("Tiempo (t)")
plt.ylabel("Valor (V_t)")
plt.show()
