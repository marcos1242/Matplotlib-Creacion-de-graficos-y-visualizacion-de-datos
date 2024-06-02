import numpy as np
import matplotlib.pyplot as plt

# Crear datos de ejemplo
x = np.linspace(0, 10, 100)  
y = np.sin(x)  # Función seno

# Crear el gráfico
plt.figure(figsize=(10, 6))  
plt.plot(x, y, label='Seno de x')

# Agregar etiquetas y título
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Gráfico de la función seno')

# Mostrar leyenda
plt.legend()

# Mostrar el gráfico
plt.grid(True)  # Agregar una cuadrícula
plt.show()

