import pandas as pd  # Importa la librería para manejar tablas de datos

def agrupamiento(df):  # Define la función que procesará los grupos y formatos

    # Normalizar nombres de columnas
    df.columns = df.columns.str.strip().str.lower()  # Limpia espacios y pasa títulos a minúsculas para evitar errores

    # Detectar columna de monto
    if "monto_total" in df.columns:  # Revisa si existe la columna "monto_total"
        columna_monto = "monto_total"  # Si existe, la guarda como nuestra variable de trabajo
    elif "total_compras" in df.columns:  # Si no, busca la alternativa "total_compras"
        columna_monto = "total_compras"  # La asigna para usarla en los cálculos
    else:  # Si no encuentra ninguna de las dos
        raise ValueError(  # Detiene el programa y avisa qué columnas sí encontró
            f"No se encontró columna de monto. Columnas disponibles: {df.columns.tolist()}"
        )

    # 1 Agrupamiento
    resumen = (
        df.groupby("categoria_cliente")[columna_monto]  # Agrupa los datos por tipo de cliente (Alto/Bajo)
        .mean()  # Calcula el promedio del monto para cada grupo
        .reset_index()  # Convierte el resultado de nuevo en una tabla limpia (DataFrame)
        .rename(columns={columna_monto: "promedio_monto"})  # Cambia el nombre de la columna para que sea descriptivo
    )

    # 2 Pivot (Tabla Dinámica)
    pivot = df.pivot_table(
        values=columna_monto,  # El dato que queremos analizar (el dinero)
        index="categoria_cliente",  # Lo que queremos ver en las filas (categorías)
        aggfunc="mean"  # La operación matemática, en este caso el promedio
    )

    # 3 Melt (Despivotar)
    melt = pivot.reset_index().melt(
        id_vars="categoria_cliente",  # La columna que se queda fija
        value_name="promedio_monto"  # El nombre que recibirá la columna de los valores calculados
    )

    # 4 Exportar dataset final
    df.to_csv("data/final/dataset_final.csv", index=False)  # Guarda los datos completos en formato CSV
    df.to_excel("data/final/dataset_final.xlsx", index=False)  # Guarda los mismos datos en un archivo de Excel

    # Exportar resumen (opcional, suma puntos)
    resumen.to_csv("data/final/resumen_categoria_cliente.csv", index=False)  # Guarda solo la tablita de promedios

    return df  # Entrega el DataFrame original por si se necesita seguir trabajando