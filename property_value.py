import numpy as np
import matplotlib.pyplot as plt



def property_value(left_years: int, initial_value: float):
    if left_years == 0:
        return initial_value * 0.75
    # Parameters
    return_rate = 0.034
    volatibility = 0.05
    time_span = 0.01  
    n_steps = int(left_years / time_span)  
    time_vector = np.linspace(0, left_years, n_steps) 

    W = np.random.normal(0, np.sqrt(time_span), size=n_steps)  
    W = np.cumsum(W) 

    # Cálculo de Vt según la fórmula
    V = initial_value * np.exp((return_rate - 0.5 * volatibility**2) * time_vector + volatibility * W)

    return V[-1]/left_years/12
