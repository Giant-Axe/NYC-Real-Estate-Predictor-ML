# IMPORTACION DE LAS LIBRERIAS A USAR
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
# importamos sqlite para exportar el data frame ya tratado
import sqlite3
# importamos skitlearn para trabajar con machine learning
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score


# ---------- 1. Cargar datos desde nuestra base de datos SQL
conn = sqlite3.connect('NYC_Real_Estate_Production.db')
df = pd.read_sql("SELECT * FROM cleaned_sales", conn)

# ---------- 2. Selección de variables (Features y Target)
# Elegimos variables clave para el precio
features = ['BOROUGH', 'BUILDING_CLASS_CATEGORY',
            'GROSS_SQUARE_FEET', 'YEAR_BUILT']
X = df[features]
y = df['SALE_PRICE']

# --------- 3. Preprocesamiento: Convertir texto a números (Dummy Variables)
# Esto es necesario porque el algoritmo solo entiende de matemáticas
X = pd.get_dummies(
    X, columns=['BOROUGH', 'BUILDING_CLASS_CATEGORY'], drop_first=True)

# ---------- 4. Dividir los datos: 80% para entrenar, 20% para probar (Test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# ---------- 5. Entrenar el modelo
print("⏳ Entrenando el modelo (esto puede tardar unos segundos)...")
model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
model.fit(X_train, y_train)

# ---------- 6. Realizar predicciones sobre el set de prueba
predictions = model.predict(X_test)

# ---------- 7. Evaluación (Visión de Administrador)
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print(f"\n📊 RESULTADOS DEL MODELO:")
print(f"Error Medio Absoluto (MAE): ${mae:,.2f}")
print(f"Precisión (R² Score): {r2:.2f}")

# --------- 8. GUARDAR PREDICCIONES EN SQL PARA POWER BI
# Vamos a crear una tabla final que compare Real vs Predicho
results = X_test.copy()
results['REAL_PRICE'] = y_test
results['PREDICTED_PRICE'] = predictions
results['GAP_PERCENTAGE'] = (
    (results['PREDICTED_PRICE'] - results['REAL_PRICE']) / results['REAL_PRICE']) * 100

results.to_sql('ml_predictions_results', conn,
               if_exists='replace', index=False)
conn.close()

print("\n✅ Predicciones guardadas en la tabla 'ml_predictions_results' de tu base de datos.")
