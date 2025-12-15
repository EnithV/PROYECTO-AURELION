# DOCUMENTACIÓN TÉCNICA - PROYECTO AURELION

**Proyecto desarrollado como parte del curso AI Fundamentals - Guayerd - IBM Skills Build**

---

## ARQUITECTURA DEL PROYECTO

### Estructura de Archivos
```
Sprint_2/Enith Gicela Vargas Vargas - Proyecto Aurelion/
├── 00_analisis_esquema_simple.py
├── 01_analisis_exploratorio_simple.py
├── 02_normalizacion_datos.py
├── 03_merge_tablas.py
├── 04_resumen_final.py
├── 05_visualizaciones_avanzadas.py
├── 06_modelos_ml.py
├── 07_reporte_final.py
└── resultados/
    ├── datasets_normalizados/
    ├── estadisticas/
    └── histogramas/
```

## METODOLOGÍA IMPLEMENTADA

### Fase 1: Análisis Exploratorio
- **Objetivo**: Comprender la estructura y calidad de los datos
- **Técnicas**: Análisis de esquema, identificación de PK/FK, EDA
- **Herramientas**: Pandas, NumPy, Matplotlib, Seaborn

### Fase 2: Normalización de Datos
- **Objetivo**: Preparar datos para machine learning
- **Técnicas**: Winsorization, MinMax/Standard/Robust Scaling, OneHot/Label Encoding
- **Herramientas**: Scikit-learn preprocessing

### Fase 3: Machine Learning
- **Objetivo**: Implementar modelos predictivos
- **Técnicas**: Regresión, Clasificación, Clustering
- **Herramientas**: Scikit-learn, Cross-validation

## ESPECIFICACIONES TÉCNICAS

### Entorno de Desarrollo
- **Python**: 3.13.2
- **Pandas**: Manipulación de datos
- **NumPy**: Cálculos numéricos
- **Scikit-learn**: Machine Learning
- **Matplotlib/Seaborn**: Visualizaciones

### Métricas de Calidad
- **Completitud**: 100% (sin valores nulos)
- **Consistencia**: Validada con integridad referencial
- **Precisión**: 99.62% en mejores modelos
- **Escalabilidad**: Preparado para datos en crecimiento

## RESULTADOS TÉCNICOS

### Performance de Modelos
| Métrica | Mejor Modelo | Valor |
|---------|--------------|-------|
| R² Regresión | Random Forest | 0.9962 |
| Accuracy Clasificación | SVC | 0.8841 |
| Silhouette Clustering | K-Means | 0.3863 |

### Validación Cruzada
- **Folds**: 5
- **Métricas**: R², Accuracy, Silhouette Score
- **Consistencia**: Desviación estándar < 0.1

---

**Proyecto desarrollado como parte del curso AI Fundamentals - Guayerd - IBM Skills Build**
**Autor:** Enith Gicela Vargas Vargas
