Proyecto de Preparación de Datos E-commerce 
Este proyecto implementa un Pipeline de Datos automatizado para una empresa de e-commerce utilizando Python. El sistema integra información de múltiples fuentes, realiza una limpieza estadística profunda y transforma datos crudos en activos estratégicos para la toma de decisiones.

Estructura del Proyecto
El flujo está organizado de manera modular para garantizar escalabilidad y orden:

Plaintext
preparacion_datos_ecommerce/
├── data/
│   ├── raw/            # Datos originales (Inmutables)
│   ├── processed/      # Resultados de etapas intermedias
│   └── final/          # Datasets finales para negocio (CSV/Excel)
├── src/                # Módulos de procesamiento por etapas
│   ├── leccion_1_numpy.py
│   ├── leccion_2_pandas.py
│   ├── leccion_3_obtencion.py
│   ├── leccion_4_limpieza.py
│   ├── leccion_5_wrangling.py
│   └── leccion_6_agrupamiento.py
├── main.py             # Orquestador principal del flujo
├── informe_preparacion_datos.docx # Informe detallado del proyecto
├── requirements.txt    # Dependencias del proyecto
└── README.md           # Documentación

Tecnologías Utilizadas
NumPy: Generación de datos sintéticos y cálculos de alto rendimiento mediante memoria contigua y funciones vectorizadas.

Pandas: Motor principal para la manipulación de DataFrames, permitiendo manejar datos heterogéneos y múltiples formatos (CSV, Excel, HTML).

Flujo de Procesamiento
Generación y Carga: Creación de datos sintéticos y carga de archivos desde fuentes locales y externas.

Limpieza Estadística: Imputación de nulos mediante la mediana y eliminación de outliers utilizando el método del Rango Intercuartílico (IQR) para asegurar datos precisos.

Wrangling: Normalización de encabezados, eliminación de duplicados y segmentación de clientes mediante funciones lambda.

Estructuración Final: Generación de reportes ejecutivos y transformación de formatos (Melt) para facilitar la visualización.

Instalación y Ejecución
Clonar el repositorio:

Bash
git clone https://github.com/CamilaGarrido/preparacion_datos_ecommerce.git
cd preparacion_datos_ecommerce
Instalar dependencias:

Bash
pip install -r requirements.txt
Ejecutar el Pipeline completo:

Bash
python main.py

Entregables Finales
Informe Detallado: informe_preparacion_datos.docx contiene la justificación técnica y conclusiones del proceso.
Datasets Finales: Ubicados en data/final/, incluyen el dataset limpio y un reporte resumido por categoría de cliente.

Desarrollado por: Camila Garrido Módulo: Obtención y Preparación de Datos
