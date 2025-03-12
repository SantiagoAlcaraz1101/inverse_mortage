import numpy as np
import matplotlib.pyplot as plt



def property_value(left_years: int, initial_value: float):
    if left_years == 0:
        return initial_value * deprecation_value
    # Parameters
    deprecation_value:float = 0.75
    return_rate:float = 0.034
    volatibility:float = 0.05
    time_span:float = 0.01  
    n_steps = int(left_years / time_span)  
    time_vector = np.linspace(0, left_years, n_steps) 

    noise_vector = np.random.normal(0, np.sqrt(time_span), size=n_steps)  
    noise_vector = np.cumsum(noise_vector) 

    # Cálculo de Vt según la fórmula
    value_vector = initial_value*deprecation_value * np.exp((return_rate - 0.5 * volatibility**2) * time_vector + volatibility * noise_vector)

    return value_vector[-1]/left_years/12
