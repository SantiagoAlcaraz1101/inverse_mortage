
class Property:
    def __init__(self, stratum: int, commercial_value: float, antiqueness: int, legality: bool):
        self.stratum: int = stratum
        self.commercial_value: float = commercial_value
        self.antiqueness: int = antiqueness
        self.legality: bool = legality

    def is_property_valid(self):
        return self.antiqueness <= 25
    
    def required_stratum(self) -> bool:
        return self.stratum >= 4
    
    def is_value_enough(self) -> bool:
        return self.commercial_value >= 600e5 and self.commercial_value <= 800e5
    
    def cal_value_property(self, V0: float, mu: float, sigma: float, T: int, dt: float):
        import numpy as np
        import matplotlib.pyplot as plt

        # Parámetros
        # V0 = 100  valor inicial
        # mu = 0.05  tasa de retorno
        # sigma = 0.2  volatilidad
        # T = 1  tiempo total en años
        # dt = 0.01   tamaño del paso de tiempo
        self.V0: float = V0
        self.mu: float = mu
        self.sigma: float = sigma
        self.T: int = T
        self.dt: float = dt
        
        n_steps = int(self.T / self.dt)  # número de pasos
        t = np.linspace(0, self.T, n_steps)  # vector de tiempos

        # Generación de un proceso de Wiener (ruido blanco)
        W = np.random.normal(0, np.sqrt(self.dt), size=n_steps)  # Incrementos de Wiener
        W = np.cumsum(W)  # Sumando los incrementos para obtener el proceso de Wiener

        # Cálculo de Vt según la fórmula
        V = self.V0 * np.exp((self.mu - 0.5 * self.sigma**2) * t + self.sigma * W)
        return V

        # Graficando el resultado
        # plt.plot(t, V)
        # plt.title("Simulación de Geometric Brownian Motion")
        # plt.xlabel("Tiempo (t)")
        # plt.ylabel("Valor (V_t)")
        # plt.show()


class Person:
    def __init__(self, name: str, age: int, is_women: bool, discapacity_condition: bool, Property: Property):
        self.name: str = name
        self.age: int = age
        self.is_women: bool = is_women
        self.discapacity_condition: bool = discapacity_condition

    def is_old_enough(self) -> bool:
        return self.age >=65

    def hope_of_life(self) -> int:
        if self.is_women:
            life_expentancy: int = 78
            if life_expentancy < self.age:
                return 0 

            return life_expentancy - self.age
        else:
            life_expentancy: int = 71
            if life_expentancy < self.age:
                return 0 
            return life_expentancy - self.age
        
