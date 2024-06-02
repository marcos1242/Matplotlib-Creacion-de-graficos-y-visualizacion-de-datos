import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('https://catalogodatos.gub.uy/dataset/1c1d75d0-b3c9-4ea4-a519-8c6b1468e589/resource/922f23e1-296c-490a-a3df-61e03e122d17/download/emisivo.csv')



# Mostrar las primeras filas del DataFrame
print(df.head())

# Supongamos que queremos hacer un gráfico de barras de la cantidad de películas por año
# Para esto, necesitamos contar la cantidad de películas por año
conteo_por_año = df['Alojamiento'].value_counts().sort_index()

# Crear el gráfico de barras
plt.figure(figsize=(10, 6))
conteo_por_año.plot(kind='bar')
plt.title('Cantidad de Películas por Año')
plt.xlabel('Año')
plt.ylabel('Cantidad de Películas')
plt.show()
