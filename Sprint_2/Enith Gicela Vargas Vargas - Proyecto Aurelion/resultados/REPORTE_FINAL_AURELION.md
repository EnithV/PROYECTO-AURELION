# REPORTE FINAL - PROYECTO AURELION
**Proyecto desarrollado como parte del curso AI Fundamentals - Guayerd - IBM Skills Build**

**Fecha:** 27/11/2025 | **Hora:** 21:10:11
**Autor:** Enith Gicela Vargas Vargas
**Curso:** AI Fundamentals - Guayerd - IBM Skills Build

---

## RESUMEN EJECUTIVO

Este proyecto implementa un sistema completo de normalización de datos y machine learning para la base de datos de la Tienda Aurelion. Se desarrollaron algoritmos de regresión, clasificación y clustering para optimizar las operaciones comerciales.

### OBJETIVOS ALCANZADOS

✅ **Análisis Exploratorio de Datos (EDA)**
- Esquema de base de datos analizado
- Primary Keys y Foreign Keys identificadas
- 4 tablas procesadas: clientes, productos, ventas, detalle_ventas

✅ **Normalización de Datos**
- Tratamiento de outliers con Winsorization
- Normalización numérica (MinMax, Standard, Robust)
- Encoding categórico (OneHot, Label)
- Dataset final: 343 registros × 27 columnas

✅ **Machine Learning**
- Regresión: Predicción de importes (99.62% precisión)
- Clasificación: Segmentación de clientes (88.41% precisión)
- Clustering: Agrupación de productos/ventas

## RESULTADOS PRINCIPALES

### MODELOS DE REGRESIÓN (Predicción de Importes)

| Modelo | R² Entrenamiento | R² Prueba | CV R² |
|--------|------------------|-----------|-------|
| Linear Regression | 0.8947 | 0.8499 | 0.8834 |
| **Random Forest** | **0.9997** | **0.9962** | **0.9981** |
| SVR | 0.9950 | 0.9918 | 0.9944 |

### MODELOS DE CLASIFICACIÓN (Segmentación de Clientes)

| Modelo | Accuracy Entrenamiento | Accuracy Prueba | CV Accuracy |
|--------|------------------------|-----------------|-------------|
| Logistic Regression | 0.8869 | 0.8841 | 0.8863 |
| Random Forest | 0.9526 | 0.8261 | 0.8046 |
| **SVC** | **0.8869** | **0.8841** | **0.8863** |

### MODELOS DE CLUSTERING

- **K-Means**: 3 clusters (Silhouette Score: 0.3863)
- **DBSCAN**: 5 clusters detectados automáticamente

## ARCHIVOS GENERADOS

### Scripts Principales
- `00_analisis_esquema_simple.py` - Análisis de esquema de BD
- `01_analisis_exploratorio_simple.py` - EDA completo
- `02_normalizacion_datos.py` - Normalización por tabla
- `03_merge_tablas.py` - Merge final
- `04_resumen_final.py` - Resumen de resultados
- `05_visualizaciones_avanzadas.py` - Visualizaciones
- `06_modelos_ml.py` - Modelos de ML
- `07_reporte_final.py` - Reporte final

### Datasets Normalizados
- `clientes_normalizada.csv`
- `productos_normalizada.csv`
- `ventas_normalizada.csv`
- `detalle_ventas_normalizada.csv`
- `dataset_final_completo.csv` (343 registros)

### Visualizaciones (17 gráficos)
- Comparación antes/después normalización
- Matrices de correlación
- Análisis de distribuciones (con tipos de distribución)
- Análisis de outliers (boxplots)
- Pairplots y scatter plots para relaciones entre variables
- Análisis estadístico detallado de medios de pago
- Comparación de modelos ML
- Análisis de clustering
- Importancia de variables

## CONCLUSIONES Y RECOMENDACIONES

### Conclusiones Principales

1. **Excelente calidad de datos**: El dataset final no presenta valores nulos
2. **Modelos de alta precisión**: Random Forest alcanza 99.62% de precisión
3. **Clustering efectivo**: Se identificaron 3-5 grupos naturales en los datos
4. **Normalización exitosa**: Todas las variables fueron procesadas correctamente

### Recomendaciones para Producción

1. **Implementar Random Forest** para predicción de importes
2. **Usar SVC o Logistic Regression** para segmentación de clientes
3. **Aplicar K-Means** para agrupación de productos
4. **Monitorear rendimiento** con métricas de negocio
5. **Retrenar modelos** periódicamente con nuevos datos

### Próximos Pasos Sugeridos

1. **Despliegue en producción** de los mejores modelos
2. **Implementación de API** para predicciones en tiempo real
3. **Dashboard interactivo** para visualización de resultados
4. **Análisis de tendencias** temporales
5. **Optimización de inventario** basada en predicciones

---

**Proyecto desarrollado como parte del curso AI Fundamentals - Guayerd - IBM Skills Build**
**Autor:** Enith Gicela Vargas Vargas | **Fecha:** 27/11/2025
