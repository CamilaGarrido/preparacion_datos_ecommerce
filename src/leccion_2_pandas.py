import numpy as np
import pandas as pd

def numpy_a_pandas():
    """
    Convierte datos almacenados en formato NumPy (.npy) a un DataFrame de Pandas.
    Muestra estadísticas descriptivas básicas y exporta los datos a formato CSV.
    """

    datos = np.load("data/processed/datos_numpy.npy")  # Carga el archivo NumPy
    df = pd.DataFrame(
        datos,
        columns=["id_cliente", "edad", "monto_compra"]  # Define las columnas del DataFrame
    )

    print(df.head())        # Muestra las primeras filas
    print(df.describe())    # Muestra estadísticas básicas

    df.to_csv("data/processed/datos_pandas.csv", index=False)  # Guarda el DataFrame en CSV
    return df              # Retorna el DataFrame para otros módulos

if __name__ == "__main__":
    numpy_a_pandas()        # Permite ejecutar el archivo de forma independiente