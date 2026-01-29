l-- ======================================================
-- CONSULTAS DE ANÁLISIS ESTRATÉGICO - NYC REAL ESTATE
-- Autor: [Tu Nombre]
-- Objetivo: Validar datos y extraer KPIs de negocio
-- ======================================================

-- 1. TOP 5 BARRIOS CON MAYOR VOLUMEN DE VENTAS Y FACTURACIÓN
-- Útil para identificar dónde está la mayor liquidez del mercado.
SELECT 
    BOROUGH, 
    COUNT(*) AS Total_Ventas, 
    SUM(SALE_PRICE) AS Facturacion_Total,
    AVG(SALE_PRICE) AS Precio_Promedio
FROM cleaned_sales
GROUP BY BOROUGH
ORDER BY Facturacion_Total DESC
LIMIT 5;

-- 2. ANÁLISIS DE PRECIO POR PIE CUADRADO POR CATEGORÍA DE EDIFICIO
-- Permite entender qué tipo de construcciones son más valiosas.
SELECT 
    BUILDING_CLASS_CATEGORY, 
    AVG(price_per_sqft) AS Precio_Promedio_SqFt,
    COUNT(*) AS Cantidad_Propiedades
FROM cleaned_sales
GROUP BY BUILDING_CLASS_CATEGORY
HAVING Cantidad_Propiedades > 100
ORDER BY Precio_Promedio_SqFt DESC;

-- 3. IDENTIFICACIÓN DE "GANGAS" (OPORTUNIDADES DE INVERSIÓN)
-- Consultando la tabla generada por el modelo de Machine Learning.
-- Filtramos propiedades donde el modelo predice un valor un 30% superior al real.
SELECT 
    REAL_PRICE, 
    PREDICTED_PRICE, 
    GAP_PERCENTAGE,
    (PREDICTED_PRICE - REAL_PRICE) AS Ganancia_Potencial
FROM ml_predictions_results
WHERE GAP_PERCENTAGE > 30
ORDER BY GAP_PERCENTAGE DESC
LIMIT 20;

-- 4. ESTADO DEL INVENTARIO POR AÑO DE CONSTRUCCIÓN
-- Para entender si el mercado prefiere lo antiguo o lo moderno.
SELECT 
    CASE 
        WHEN YEAR_BUILT < 1900 THEN 'Pre-Siglo XX'
        WHEN YEAR_BUILT BETWEEN 1900 AND 1950 THEN '1900-1950'
        WHEN YEAR_BUILT BETWEEN 1951 AND 2000 THEN '1951-2000'
        ELSE 'Moderno (Post-2000)'
    END AS Epoca_Construccion,
    AVG(SALE_PRICE) AS Precio_Promedio
FROM cleaned_sales
WHERE YEAR_BUILT > 0
GROUP BY Epoca_Construccion;