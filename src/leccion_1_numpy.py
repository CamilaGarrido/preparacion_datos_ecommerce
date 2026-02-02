import numpy as np  # Importa la librería NumPy para operaciones numéricas

def generar_datos():
    ids = np.arange(1, 101)                     # Genera IDs del 1 al 100
    edades = np.random.randint(18, 65, size=100)  # Edades aleatorias entre 18 y 65 años
    compras = np.random.randint(5000, 200000, size=100)  # Montos de compra aleatorios

    datos = np.column_stack((ids, edades, compras))  # Combina los arrays en una matriz
    np.save("data/processed/datos_numpy.npy", datos)  # Guarda los datos en formato .npy

    print("Media compras:", np.mean(compras))    # Calcula la media de los montos
    print("Total compras:", np.sum(compras))     # Calcula el total de compras
    print("Cantidad registros:", compras.size)   # Cantidad total de registros

if __name__ == "__main__":
    generar_datos()  # Ejecuta la función solo si el archivo se corre directamente.