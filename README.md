NYC Real Estate: Inteligencia de Datos y Modelado Predictivo de Inversiones
![alt text](https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)

![alt text](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

![alt text](https://img.shields.io/badge/SQL-CC0000?style=for-the-badge&logo=sqlite&logoColor=white)

![alt text](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)

🎯 Objetivo del Proyecto
Este proyecto desarrolla un flujo de trabajo End-to-End (Punta a Punta) para analizar el mercado inmobiliario de Nueva York. El objetivo principal es transformar datos históricos crudos en una herramienta de toma de decisiones que identifique propiedades subvaloradas mediante el uso de Machine Learning y Business Intelligence.
🏢 Escenario de Negocio
En un mercado tan volátil como el de NYC, la tasación manual es lenta y propensa a errores. Este sistema permite a un fondo de inversión o corredor inmobiliario:
Identificar tendencias de precios por barrio.
Predecir el valor de mercado "lógico" de una propiedad basándose en sus características físicas.
Detectar Gaps de Inversión (propiedades cuyo precio real es significativamente menor al predicho por la IA).
🛠️ Stack Tecnológico
Procesamiento de Datos: Python (Pandas, NumPy).
Visualización Analítica: Matplotlib, Seaborn.
Machine Learning: Scikit-Learn (Random Forest Regressor).
Persistencia de Datos: SQL (SQLite).
Inteligencia de Negocios: Power BI (Modelado de datos en estrella y DAX).
📈 Pipeline del Proyecto
1. ETL y Limpieza (Python)
Procesamiento de un dataset de +84,000 registros.
Tratamiento de datos inconsistentes (precios en $0, formatos de fecha erróneos, valores nulos).
Ingeniería de Características: Creación de KPIs como Price per SqFt y limpieza de outliers mediante criterios estadísticos y de negocio.
2. Análisis Exploratorio (EDA)
Identificación de estacionalidad (picos de ventas en junio).
Correlación de variables: Se determinó que el Gross Square Feet explica gran parte de la variabilidad del precio.
Visualización de distribuciones de precios mediante escalas logarítmicas para manejar la alta volatilidad de Manhattan.
3. Machine Learning
Implementación de un modelo de Random Forest Regressor.
Resultados:
Precisión (R2): 0.74 (El modelo explica el 74% del precio).
MAE: ~$903k (Contextualizado para el mercado de propiedades de alto valor de NYC).
Generación de una tabla de predicciones comparativa (Real vs. Predicho).
4. Arquitectura de Datos (SQL)
Migración de datos procesados de Python a SQLite.
Diseño de un Esquema en Estrella con tablas de Hechos (Fact_Sales) y Dimensiones (Dim_Location, Dim_Date, Dim_PropertyType) para optimizar el rendimiento de las consultas.
5. Dashboard Estratégico (Power BI)
Desarrollo de métricas avanzadas en DAX.
Implementación de un "Semáforo de Inversión" mediante formato condicional para resaltar oportunidades de arbitraje inmobiliario donde el Gap de valor es superior al 20%.
📂 Estructura del Repositorio
/data: Contiene el dataset original y el procesado (o instrucciones para descargarlos).
/notebooks: Jupyter Notebook con todo el proceso de limpieza y modelado.
/sql: Consultas estratégicas para validación de negocio.
/reports: Archivo .pbix de Power BI y capturas de pantalla del dashboard.
requirements.txt: Librerías necesarias para replicar el entorno.
📊 Visualización de Resultados
<img width="1922" height="1079" alt="image" src="https://github.com/user-attachments/assets/6322677a-28b6-481c-8fbf-0a200e4a5907" />
<img width="1923" height="1073" alt="image" src="https://github.com/user-attachments/assets/a230b925-ab5d-4969-bdd5-a67fa04331b0" />
Vista General de Ventas: Tendencias y mapas.
Predictor de Inversiones: El gráfico de dispersión con el análisis de Gaps.
👤 Autor: JAIME JESUS ALVARADO PEREZ
Licenciado en Informática.
Estudiante de último año de Administración de Empresas.
Especialista en Ciencia de Datos y Business Intelligence.
Cómo Replicar el Proyecto
Clona el repositorio: git clone https://github.com/tu-usuario/NYC-Real-Estate-Predictor.git
Instala dependencias: pip install -r requirements.txt
Ejecuta el notebook en /notebooks para generar la base de datos SQL.
Abre el archivo en /reports con Power BI Desktop.
¿Cómo guardarlo?
Crea un archivo nuevo en tu carpeta raíz llamado README.md.
Pega este contenido.
Personaliza tu nombre y el enlace de GitHub al final.
Súbelo junto con tus archivos.
