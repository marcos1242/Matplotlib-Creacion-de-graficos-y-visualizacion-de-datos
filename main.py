# Archivo principal que ejecuta el flujo del programa

from data_loader import load_facultades, load_shapefile, create_geodataframe
from plotter import assign_colors, plot_map

def main():
    # Cargar los datos
    df_publicas = load_facultades()
    mapa_CABA = load_shapefile()
    
    # Crear el GeoDataFrame
    gdf_publicas = create_geodataframe(df_publicas)
    
    # Asignar colores
    gdf_publicas, color_mapping = assign_colors(gdf_publicas)
    
    # Graficar el mapa
    plot_map(mapa_CABA, gdf_publicas, color_mapping)

if _name_ == "_main_":
    main()
