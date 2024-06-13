from  prototipo import TemperaturaAire

archivo_csv = 'https://catalogodatos.gub.uy/dataset/ecd6cb6f-67c4-4f2f-8dd7-9155fa10b2f9/resource/1813b9e8-9e32-482f-ac8f-500439f8cab9/download/inumet_temperatura-del-aire-2023.csv'
temperatura_aire = TemperaturaAire(archivo_csv)
temperatura_aire.cargar_datos()
temperatura_aire.calcular_promedios_mensuales()
temperatura_aire.mostrar_promedios()
temperatura_aire.graficar_promedios_mensuales()