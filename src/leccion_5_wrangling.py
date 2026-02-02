import pandas as pd  # Importa la librería pandas para manipulación de datos

def wrangling(df):  # Define la función que recibe un DataFrame como entrada

    # Normalizar nombres de columnas
    df.columns = df.columns.str.strip().str.lower()  # Elimina espacios en blanco y pasa los títulos a minúsculas

    # Determinar columna de monto según disponibilidad
    if "monto_total" in df.columns:  # Verifica si existe la columna exacta "monto_total"
        columna_monto = "monto_total"  # Si existe, la asigna como nuestra variable de referencia
    elif "total_compras" in df.columns:  # Si no, busca si existe la alternativa "total_compras"
        columna_monto = "total_compras"  # Si existe esta última, la asigna para el cálculo
    else:  # Si no encuentra ninguna de las dos opciones anteriores
        raise ValueError(  # Lanza un error personalizado explicando qué salió mal
            f"No se encontró una columna de monto. Columnas disponibles: {df.columns.tolist()}"
        )

    # Eliminar duplicados
    df = df.drop_duplicates()  # Borra todas las filas que tengan valores idénticos en todas sus celdas

    # Crear categoría de cliente según monto
    df["categoria_cliente"] = df[columna_monto].apply(  # Crea una nueva columna basada en la lógica siguiente:
        lambda x: "Alto" if x > 100000 else "Bajo"  # Si el valor supera los 100,000 es "Alto", de lo contrario es "Bajo"
    )

    # Guardar resultado del wrangling
    df.to_csv("data/processed/datos_wrangling.csv", index=False)  # Exporta el resultado a un CSV sin guardar el índice

    return df  # Devuelve el DataFrame ya limpio y procesado