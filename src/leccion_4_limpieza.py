import pandas as pd

def limpiar_datos(df):
    """
    Limpia los datos del DataFrame:
    - Completa valores faltantes
    - Elimina datos fuera de lo normal
    - Guarda el resultado limpio
    """

    df = df.copy()  # Copiamos el DataFrame para no cambiar el original

    if "edad" in df.columns:
        df["edad"] = df["edad"].fillna(df["edad"].median())  
        # Si hay edades vacías, se reemplazan por la edad promedio

    if "monto_compra" in df.columns:
        Q1 = df["monto_compra"].quantile(0.25)  # Valor bajo típico
        Q3 = df["monto_compra"].quantile(0.75)  # Valor alto típico
        IQR = Q3 - Q1                            # Rango normal de los datos

        df = df[
            (df["monto_compra"] >= Q1 - 1.5 * IQR) &
            (df["monto_compra"] <= Q3 + 1.5 * IQR)
        ]  
        # Se eliminan compras demasiado pequeñas o grandes

    df.to_csv("data/processed/datos_limpios.csv", index=False)       # Guardamos el archivo limpio

    return df