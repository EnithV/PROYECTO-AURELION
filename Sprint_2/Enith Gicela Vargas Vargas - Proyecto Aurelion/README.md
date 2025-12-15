<!--
# README.md
===========
Proyecto Aurelion Sprint_2 - Normalización y Machine Learning

**Autor:** Enith Gicela Vargas Vargas  
**Fecha:** 2025-10-27  
**Curso:** AI Fundamentals - Guayerd - IBM Skills Build  
**Sprint:** 2 - Machine Learning y Normalización  
**Módulo:** README Principal  
-->

# Proyecto Aurelion Sprint_2 - Normalización de Datos y Machine Learning

## 📋 Descripción del Proyecto

Este proyecto se enfoca en la **normalización de datos** y preparación para **machine learning** utilizando la base de datos de la Tienda Aurelion. El objetivo es transformar los datos para optimizar el rendimiento de algoritmos de ML.

## 🎯 Objetivos

1. **Análisis de Esquema**: Identificar PK y FK de la base de datos
2. **Análisis Exploratorio**: Estadísticas descriptivas y detección de outliers
3. **Normalización**: Transformación de datos por tabla
4. **Merge**: Combinación de tablas normalizadas
5. **Preparación ML**: Dataset final para machine learning

## 📚 Glosario de Términos Técnicos

Este proyecto utiliza varios términos técnicos y estadísticos. Para una explicación completa y detallada de todos los términos utilizados (skewness, kurtosis, correlación de Pearson, R², MSE, MAE, Accuracy, Precision, Recall, F1-Score, normalización, outliers, clustering, etc.), consulta el **Glosario de Términos Técnicos** en:

📖 **`resultados/histogramas/ANALISIS_GRAFICOS.md`** - Sección "📚 GLOSARIO DE TÉRMINOS TÉCNICOS"

**Nota:** Este archivo se genera **automáticamente** con datos reales del proyecto cada vez que se ejecutan las visualizaciones avanzadas.

El glosario incluye:
- Definiciones claras y profesionales
- Interpretaciones prácticas
- Ejemplos en el contexto del negocio
- Escalas de interpretación
- Explicaciones accesibles para personas sin conocimiento estadístico previo

## 🔄 Generación Automática de Documentación

Este proyecto incluye scripts que generan automáticamente archivos de documentación con datos reales:

- **`10_generar_analisis_graficos.py`**: Genera `ANALISIS_GRAFICOS.md` con interpretaciones específicas de todos los gráficos
  - Se ejecuta automáticamente después de `05_visualizaciones_avanzadas.py`
  - Contiene datos reales del proyecto (estadísticas, rangos, porcentajes)

- **`11_generar_variables_centroides.py`**: Genera `VARIABLES_Y_CENTROIDES.md` con información real de modelos ML
  - Se ejecuta automáticamente después de `06_modelos_ml.py`
  - Contiene métricas reales, centroides, rangos de segmentos

**Ventajas:**
- ✅ Documentación siempre sincronizada con los datos
- ✅ Datos específicos y actualizados del proyecto
- ✅ No requiere edición manual
- ✅ Coherencia garantizada

---

## 📊 Estructura del Proyecto

```
Sprint_2/Enith Gicela Vargas Vargas - Proyecto Aurelion/
├── 00_analisis_esquema.py          # Análisis de PK/FK y esquema
├── 01_analisis_exploratorio.py    # EDA y estadísticas
├── 02_normalizacion_datos.py      # Normalización por tabla
├── 03_merge_tablas.py             # Merge de tablas normalizadas
├── 04_resumen_final.py            # Resumen estadístico del dataset final
├── 05_visualizaciones_avanzadas.py # Visualizaciones (24 gráficos) - ⚡ Genera ANALISIS_GRAFICOS.md
├── 06_modelos_ml.py               # Modelos de ML con matrices de confusión - ⚡ Genera VARIABLES_Y_CENTROIDES.md
├── 07_reporte_final.py            # Reporte final del proyecto
├── 08_estadistica_inferencial.py  # Estadística inferencial avanzada
├── 09_estadistica_prescriptiva.py # Estadística prescriptiva
├── 10_generar_analisis_graficos.py # 🔄 Generador automático de ANALISIS_GRAFICOS.md
├── 11_generar_variables_centroides.py # 🔄 Generador automático de VARIABLES_Y_CENTROIDES.md
├── resultados/
│   ├── histogramas/               # Gráficos de distribuciones
│   ├── estadisticas/              # Archivos CSV con estadísticas
│   └── datasets_normalizados/     # Datasets procesados
└── README.md                      # Este archivo
```

## 🚀 Fases del Proyecto

### **FASE 0: Análisis de Esquema**
- ✅ Identificar Primary Keys (PK)
- ✅ Identificar Foreign Keys (FK)
- ✅ Mapear relaciones entre tablas
- ✅ Definir esquema final

### **FASE 1: Análisis Exploratorio (EDA)**
- ✅ Estadísticas descriptivas
- ✅ Análisis de distribuciones
- ✅ Detección de outliers
- ✅ Histogramas y visualizaciones
- ✅ Análisis de correlaciones

### **FASE 2: Normalización de Datos Avanzada**
- ✅ Imputaciones estadísticas inteligentes (mediana, media, moda)
- ✅ Encoding avanzado con category_encoders
- ✅ Tratamiento de outliers con Winsorization
- ✅ Normalización de variables numéricas
- ✅ Validación de transformaciones con fit_transform

### **FASE 3: Merge y Preparación Final**
- ✅ Merge de tablas normalizadas
- ✅ Verificación de integridad
- ✅ Feature engineering
- ✅ Dataset final para ML

### **FASE 4: Machine Learning**
- ✅ Modelos de regresión (Linear, Random Forest, SVR)
- ✅ Modelos de clasificación (Logistic, Random Forest, SVC)
- ✅ Modelos de clustering (K-Means, DBSCAN)
- ✅ Matrices de confusión con visualizaciones
- ✅ Evaluación con métricas apropiadas

### **FASE 5: Estadística Inferencial Avanzada**
- ✅ Tests de normalidad (Shapiro-Wilk, Kolmogorov-Smirnov, D'Agostino)
- ✅ T-tests para comparación de medias
- ✅ ANOVA para comparación de múltiples grupos
- ✅ Test chi-cuadrado para independencia
- ✅ Intervalos de confianza

### **FASE 6: Estadística Prescriptiva**
- ✅ Optimización de inventario
- ✅ Optimización de precios
- ✅ Recomendaciones de marketing
- ✅ Optimización de mix de productos

## 🛠️ Tecnologías Utilizadas

- **Python 3.x**: Lenguaje principal
- **pandas**: Manipulación de datos
- **numpy**: Cálculos numéricos
- **matplotlib/seaborn**: Visualizaciones
- **scipy**: Análisis estadístico

## 📈 Técnicas de Normalización

### **Para Variables Numéricas:**
- **Min-Max Scaling**: `(x - min) / (max - min)`
- **Standardization**: `(x - μ) / σ`
- **Robust Scaling**: `(x - mediana) / IQR`
- **Log Transformation**: `log(x + 1)`

### **Para Variables Categóricas:**
- **OneHot Encoding**: Para pocas categorías (≤5)
- **Binary Encoding**: Para categorías moderadas (≤20)
- **Target Encoding**: Para muchas categorías (>20)
- **Label Encoding**: Fallback para casos especiales

## 🎯 Métricas de Calidad

### **Completitud:**
- % de valores nulos por columna
- % de registros completos
- Patrones de datos faltantes

### **Consistencia:**
- Duplicados en el dataset
- Valores fuera de rango
- Inconsistencias lógicas

### **Distribución:**
- Skewness (asimetría)
- Kurtosis (curtosis)
- Tests de normalidad

## ▶️ Cómo Ejecutar

### **1. Análisis de Esquema**
```bash
python 00_analisis_esquema.py
```

### **2. Análisis Exploratorio**
```bash
python 01_analisis_exploratorio.py
```

### **3. Normalización Avanzada**
```bash
python 02_normalizacion_datos.py          # Normalización mejorada
python 02_normalizacion_avanzada.py      # Normalización con category_encoders
```

### **4. Merge Final**
```bash
python 03_merge_tablas.py
```

## 📊 Resultados Esperados

### **Análisis de Esquema:**
- Esquema de PK/FK definido
- Relaciones entre tablas mapeadas
- Estructura de datos documentada

### **Análisis Exploratorio:**
- Estadísticas descriptivas por tabla
- Histogramas de distribuciones
- Detección de outliers
- Matrices de correlación

### **Normalización:**
- Variables categóricas codificadas
- Variables numéricas normalizadas
- Outliers tratados apropiadamente
- Datasets listos para merge

### **Dataset Final:**
- Tablas mergeadas correctamente
- Datos normalizados y limpios
- Listo para algoritmos de ML
- Integridad referencial verificada

## 🔍 Análisis Estadístico

Este proyecto incluye análisis estadístico completo:

- **Estadística Descriptiva**: Media, mediana, desviación
- **Análisis de Distribuciones**: Histogramas, Q-Q plots
- **Tests Estadísticos**: Normalidad, homocedasticidad
- **Análisis de Outliers**: IQR, Z-score, métodos robustos
- **Transformaciones**: Log, Box-Cox, normalización

## 📁 Archivos de Resultados

### **Histogramas:**
- `histogramas_clientes.png`
- `histogramas_productos.png`
- `histogramas_ventas.png`
- `histogramas_detalle_ventas.png`
- `analisis_curtosis.png` (Nuevo - Análisis de curtosis de todas las variables)

### **Estadísticas:**
- `stats_clientes.csv`
- `stats_productos.csv`
- `stats_ventas.csv`
- `stats_detalle_ventas.csv`

### **Outliers:**
- `outliers_clientes.txt`
- `outliers_productos.txt`
- `outliers_ventas.txt`
- `outliers_detalle_ventas.txt`

### **Correlaciones:**
- `correlaciones_clientes.csv`
- `correlaciones_productos.csv`
- `correlaciones_ventas.csv`
- `correlaciones_detalle_ventas.csv`

## 🎓 Aprendizajes del Proyecto

- **Análisis estadístico** con Python
- **Normalización de datos** para ML
- **Detección y tratamiento** de outliers
- **Encoding de variables** categóricas
- **Preparación de datasets** para ML
- **Análisis de integridad** de datos

---

*Proyecto desarrollado como parte del curso AI Fundamentals - Guayerd - IBM Skills Build*
*Autor: Enith Gicela Vargas Vargas | Grupo 11 - Camada 1*
