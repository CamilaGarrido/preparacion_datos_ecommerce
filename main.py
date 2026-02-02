# Importación de funciones específicas desde diferentes archivos (módulos)
from src.leccion_1_numpy import generar_datos  # Trae la función para crear datos aleatorios
from src.leccion_2_pandas import numpy_a_pandas  # Trae la función para convertir arreglos a tablas
from src.leccion_3_obtencion import unificar_datos  # Trae la función que junta archivos y web
from src.leccion_4_limpieza import limpiar_datos  # Trae la función que quita nulos y errores
from src.leccion_5_wrangling import wrangling  # Trae la función que normaliza y crea categorías
from src.leccion_6_agrupamiento import agrupamiento  # Trae la función que hace promedios y pivots

# --- EJECUCIÓN DEL PIPELINE (FLUJO DE DATOS) ---

# Lección 1: generar datos con NumPy
generar_datos()  # Crea los archivos base con números aleatorios para empezar

# Lección 2: convertir NumPy a Pandas
numpy_a_pandas()  # Transforma esos números en un formato de tabla legible

# Lección 3: unificar CSV + Excel + Web
df_total, df_web = unificar_datos()  # Combina todas las fuentes de datos en un solo lugar

# Lección 4: limpieza de datos
df_limpio = limpiar_datos(df_total)  # Recibe el DataFrame total y le quita la "basura"

# Lección 5: wrangling
df_wrangling = wrangling(df_limpio)  # Toma los datos limpios y crea la columna "categoria_cliente"

# Lección 6: agrupamiento y métricas
agrupamiento(df_wrangling)  # Toma los datos procesados y genera los reportes finales (promedios)