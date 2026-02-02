import pandas as pd

def unificar_datos():
    """
    Obtiene datos desde múltiples fuentes:
    - Archivos locales en formato CSV y Excel
    - Tabla extraída desde una página web
    Unifica los datos locales y almacena los resultados
    en archivos procesados.
    """

    df_csv = pd.read_csv("data/raw/clientes_ecommerce.csv")      # Lectura de datos desde CSV
    df_excel = pd.read_excel("data/raw/clientes_ecommerce.xlsx") # Lectura de datos desde Excel

    url = "https://www.w3schools.com/html/html_tables.asp"        # URL de la fuente web
    tablas_web = pd.read_html(url)                                # Lectura de tablas HTML
    df_web = tablas_web[0]                                        # Selección de la primera tabla

    df_web = df_web.rename(columns={                              # Normaliza nombres de columnas
        "Company": "empresa",
        "Contact": "contacto",
        "Country": "pais"
    })

    df_total = pd.concat([df_csv, df_excel], ignore_index=True)   # Unifica las fuentes locales

    df_total.to_csv("data/processed/datos_consolidados.csv", index=False)  # Guarda datos locales
    df_web.to_csv("data/processed/datos_web.csv", index=False)             # Guarda datos web

    print("Datos locales unificados:", len(df_total))             # Total de registros locales
    print("Datos obtenidos desde la web:", len(df_web))            # Total de registros web

    return df_total, df_web                                       # Retorna ambos DataFrames

if __name__ == "__main__":
    unificar_datos()                                              # Permite ejecución independiente