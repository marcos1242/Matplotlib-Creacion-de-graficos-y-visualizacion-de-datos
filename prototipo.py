import pandas as pd
import matplotlib.pyplot as plt #Importamos las librerias que vamos a utilizar

class TemperaturaAire(): #Definimos la clase TemperaturaAire
    def __init__(self, file_path): 
        self.file_path = file_path
        self.df = None
        self.promedios_mensuales = None

    def cargar_datos(self):
        #Lee el archivo CSV
        self.df = pd.read_csv(self.file_path)
        #Convertimos la columna 'fecha' a datetime
        self.df['fecha'] = pd.to_datetime(self.df['fecha'])
        #Extraemos el año y el mes
        self.df['año'] = self.df['fecha'].dt.year
        self.df['mes'] = self.df['fecha'].dt.month

    def calcular_promedios_mensuales(self):
        #Agrupamos por año y mes y calculamos el promedio de TempAire
        self.promedios_mensuales = self.df.groupby(['año', 'mes'])['TempAire'].mean().reset_index()

    def mostrar_promedios(self):
        #Muestra de los promedios mensuales calculados
        print(self.promedios_mensuales)

    def graficar_promedios_mensuales(self):
        #Crea el gráfico de barras
        plt.figure(figsize=(10, 5))
        plt.bar(self.promedios_mensuales['mes'], self.promedios_mensuales['TempAire'])
        plt.xlabel('Mes')
        plt.ylabel('Temperatura Promedio del Aire (°C)')
        plt.title('Promedio Mensual de la Temperatura del Aire en 2023')
        plt.xticks(self.promedios_mensuales['mes'])  # Asegurar que cada mes tiene una etiqueta
        plt.grid(axis='y')  #Muestra solo la cuadrícula horizontal
        plt.show()


