import numpy as np
import matplotlib.pyplot as plt



def property_value(T: int, initial_value: float):
# Parámetros

    mu = 0.034  # tasa de retorno
    sigma = 0.1  # volatilidad
    dt = 0.01  # tamaño del paso de tiempo
    n_steps = int(T / dt)  # número de pasos
    t = np.linspace(0, T, n_steps)  # vector de tiempos

    # Generación de un proceso de Wiener (ruido blanco)
    W = np.random.normal(0, np.sqrt(dt), size=n_steps)  # Incrementos de Wiener
    W = np.cumsum(W)  # Sumando los incrementos para obtener el proceso de Wiener

    # Cálculo de Vt según la fórmula
    V = initial_value * np.exp((mu - 0.5 * sigma**2) * t + sigma * W)

    return(V[-1]/T/12)

# Graficando el resultado
#plt.plot(t, V)
#plt.title("Simulación de Geometric Brownian Motion")
#plt.xlabel("Tiempo (t)")
#plt.ylabel("Valor (V_t)")
#plt.show()
