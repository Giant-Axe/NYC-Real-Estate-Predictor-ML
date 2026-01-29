# importamos skitlearn para trabajar con machine learning
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# hacemos una verificacion ceros logicos
print("Registros con 0 en Gross Square Feet:",
      (df['GROSS SQUARE FEET'] == 0).sum())

# Crear la columna de precio por pie cuadrado
# Usamos un filtro para evitar división por cero si aún quedaran algunos
df = df[df['GROSS SQUARE FEET'] > 0]
df['price_per_sqft'] = df['SALE PRICE'] / df['GROSS SQUARE FEET']

print("KPI 'Price per SqFt' fue creado exitosamente.")


# ----------Verificamos cual es el barrio (BOROUGH) mas caro en Nueva York
# Agrupar por Barrio y calcular estadísticas clave
stats_by_borough = df.groupby('BOROUGH').agg({
    'SALE PRICE': ['mean', 'median', 'count'],
    'price_per_sqft': 'mean'
}).reset_index()

# Renombrar columnas para que sean legibles
stats_by_borough.columns = ['Borough', 'Precio_Promedio',
                            'Precio_Mediana', 'Num_Ventas', 'Precio_m2_Promedio']

# Ordenar por el más caro
print(stats_by_borough.sort_values(by='Precio_Mediana', ascending=False))

# ----------Hacemos una visualización rapida en diagrama de cajas
plt.figure(figsize=(12, 6))
sns.boxplot(x='BOROUGH', y='SALE PRICE', data=df)
plt.yscale('log')  # Usamos escala logarítmica porque los precios varían mucho
plt.title('Distribución de Precios por Barrio (Escala Logarítmica)')
plt.show()

# ----------Histograma de Distribucion de Frecuencia
plt.figure(figsize=(10, 6))
sns.histplot(df['SALE PRICE'], bins=50, kde=True, color='blue', log_scale=True)
# plt.xscale('log')
plt.title('Distribución de Precios de Venta (Escala Logarítmica)')
plt.xlabel('Precio de Venta (Log 10)')
plt.ylabel('Frecuencia (Cantidad de ventas)')
plt.show()

# ----------MAPA DE CALOR de CORRELACIONES
plt.figure(figsize=(12, 8))
# Seleccionamos solo columnas numéricas para la correlación
numeric_df = df.select_dtypes(include=[np.number])
correlation = numeric_df.corr()

sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Mapa de Calor de Correlaciones')
plt.show()

# ----------GRÄFICO DE DISPERSION
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='GROSS SQUARE FEET',
                y='SALE PRICE', hue='BOROUGH', alpha=0.5)
plt.xscale('log')
plt.yscale('log')
plt.title('Relación: Tamaño de Construcción vs Precio')
plt.show()


# ----------SERIES DE TIEMPO (TENDENCIA DE VENTAS)
# Agrupar por mes
df['month_year'] = df['SALE DATE'].dt.to_period('M')
sales_trend = df.groupby('month_year').size()

plt.figure(figsize=(12, 5))
sales_trend.plot(kind='line', marker='o', color='green')
plt.title('Tendencia Mensual de Cantidad de Ventas')
plt.xticks(rotation=45)
plt.ylabel('Número de ventas')
plt.show()
