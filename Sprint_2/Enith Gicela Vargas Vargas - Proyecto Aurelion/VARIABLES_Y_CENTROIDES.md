# 📊 VARIABLES PREDICTORAS, VARIABLES OBJETIVO Y CENTROIDES - PROYECTO AURELION

**Proyecto desarrollado como parte del curso AI Fundamentals - Guayerd - IBM Skills Build**

**Autor:** Enith Gicela Vargas Vargas  
**Fecha:** 27/11/2025  
**Sprint:** 2 - Machine Learning y Normalización  
**Última actualización automática:** 27/11/2025 21:10:19

---

## 🎯 RESUMEN EJECUTIVO

Este documento detalla todas las variables utilizadas en los modelos de Machine Learning del Proyecto Aurelion, incluyendo variables predictoras (features), variables objetivo (targets), y el uso de centroides en algoritmos de clustering.

**NOTA:** Este archivo se genera AUTOMÁTICAMENTE con datos reales del proyecto. Se actualiza cada vez que se ejecutan los modelos ML.

---

## 📋 VARIABLES DEL DATASET FINAL

### Dataset Final: 343 registros × 24 columnas

El dataset final se crea mediante el merge de 4 tablas normalizadas:
- **clientes** (normalizada)
- **productos** (normalizada)
- **ventas** (normalizada)
- **detalle_ventas** (normalizada)

### Columnas del Dataset Final:

1. **id_venta** (int64)
2. **id_producto** (int64)
3. **nombre_producto_detalle** (object)
4. **cantidad** (float64)
5. **precio_unitario_detalle** (float64)
6. **importe** (float64)
7. **nombre_producto_producto** (object)
8. **categoria_Alimentos** (int64)
9. **categoria_Limpieza** (int64)
10. **precio_unitario_producto** (float64)
11. **fecha** (object)
12. **id_cliente** (int64)
13. **nombre_cliente_venta** (object)
14. **email_venta** (object)
15. **medio_pago_tarjeta** (int64)
16. **medio_pago_qr** (int64)
17. **medio_pago_transferencia** (int64)
18. **medio_pago_efectivo** (int64)
19. **nombre_cliente_cliente** (object)
20. **email_cliente** (object)
21. **ciudad_0** (int64)
22. **ciudad_1** (int64)
23. **ciudad_2** (int64)
24. **fecha_alta** (object)

**Total:** 24 columnas

---

## 🔍 VARIABLES PREDICTORAS (FEATURES)

Las variables predictoras son las características (features) que se utilizan para predecir o clasificar. Se seleccionan automáticamente excluyendo IDs y variables objetivo.

### Selección de Variables Predictoras

**Criterio de Selección:**
- Solo variables numéricas (int64, float64)
- Excluir identificadores (id_venta, id_cliente, id_producto)
- Excluir variable objetivo
- Incluir variables codificadas (One-Hot Encoding)

### Variables Predictoras por Tipo de Modelo

#### **1. MODELOS DE REGRESIÓN (Predicción de Importe)**

**Variable Objetivo:** `importe` (float64)

**Variables Predictoras Excluidas:**
- `id_venta`
- `id_cliente`
- `id_producto`
- `importe` (variable objetivo)

**Variables Predictoras Incluidas (ejemplos):**
- `cantidad`
- `precio_unitario_detalle`
- `categoria_Alimentos`
- `categoria_Limpieza`
- `precio_unitario_producto`
- `medio_pago_tarjeta`
- `medio_pago_qr`
- `medio_pago_transferencia`
- `medio_pago_efectivo`
- `ciudad_0`
- `ciudad_1`
- `ciudad_2`

**Total de Variables Predictoras:** Aproximadamente 12 variables numéricas

**Importancia de Variables (Random Forest):**
1. **Cantidad** - Mayor importancia (variable más predictiva)
2. **Precio unitario** - Segunda mayor importancia
3. **Categorías de productos** - Importancia moderada
4. **Medios de pago** - Importancia moderada
5. **Ciudad** - Importancia baja-moderada

#### **2. MODELOS DE CLASIFICACIÓN (Segmentación de Clientes)**

**Variable Objetivo:** `segmento_cliente` (categórica: 'Bajo', 'Medio', 'Alto')

**Creación de Variable Objetivo:**
```python
# Se crea basándose en el importe promedio por cliente
importe_promedio = dataset.groupby('id_cliente')['importe'].mean()
segmento_cliente = pd.cut(importe_promedio, bins=3, labels=['Bajo', 'Medio', 'Alto'])
```

**Rangos Específicos de Segmentos (Datos Reales del Proyecto):**

- **Bajo:**
  - Rango de importe promedio: $-1.08 - $0.08
  - Importe promedio: $-0.34
  - Mediana: $-0.30
  - Cantidad de clientes: 38

- **Medio:**
  - Rango de importe promedio: $0.10 - $1.21
  - Importe promedio: $0.52
  - Mediana: $0.44
  - Cantidad de clientes: 28

- **Alto:**
  - Rango de importe promedio: $2.45 - $2.45
  - Importe promedio: $2.45
  - Mediana: $2.45
  - Cantidad de clientes: 1

**Variables Predictoras Incluidas:**
- Mismas que regresión, excluyendo `importe` para evitar data leakage

**Total de Variables Predictoras:** Aproximadamente 11-14 variables numéricas

#### **3. MODELOS DE CLUSTERING (Agrupación de Transacciones)**

**Variables Utilizadas para Clustering:**
- `cantidad`
- `precio_unitario_detalle`
- `importe`

**Total de Variables:** 3 variables numéricas

**Normalización:** Las variables se normalizan usando `StandardScaler` antes del clustering para que todas tengan la misma escala.

---

## 🎯 VARIABLES OBJETIVO (TARGETS)

Las variables objetivo son las que queremos predecir o clasificar.

### **1. REGRESIÓN: Predicción de Importe**

**Variable Objetivo:** `importe` (float64)

**Descripción:**
- Variable continua numérica
- Representa el importe total de cada transacción
- Rango típico: Varía según los datos del proyecto

**Modelos Utilizados:**
- Linear Regression
- Random Forest Regressor (mejor modelo)
- SVR (Support Vector Regression)

**Métricas de Evaluación (Datos Reales del Proyecto):**

| Modelo | R² Prueba | MSE Prueba |
|--------|-----------|------------|
| LinearRegression | 0.8476 | 0.0985 |
| RandomForest | 0.9928 | 0.0046 |
| SVR | 0.9785 | 0.0139 |

### **2. CLASIFICACIÓN: Segmentación de Clientes**

**Variable Objetivo:** `segmento_cliente` (categórica)

**Descripción:**
- Variable categórica con 3 clases: 'Bajo', 'Medio', 'Alto'
- Se crea agrupando clientes por importe promedio de compras

**Modelos Utilizados:**
- Logistic Regression
- Random Forest Classifier
- SVC (Support Vector Classifier)

**Métricas de Evaluación:**
- Accuracy (Precisión Global)
- Precision (Precisión por clase)
- Recall (Sensibilidad por clase)
- F1-Score (Balance Precision-Recall)
- Matriz de Confusión

### **3. CLUSTERING: Agrupación de Transacciones**

**Variable Objetivo:** No hay variable objetivo (aprendizaje no supervisado)

**Algoritmos Utilizados:**
- **K-Means:** 3 clusters identificados
- **DBSCAN:** Clusters detectados automáticamente

---

## 📍 CENTROIDES

### ¿Qué son los Centroides?

Los **centroides** son los puntos centrales (promedios) de cada cluster en algoritmos de clustering como K-Means. Representan el "centro" o "prototipo" de cada grupo.

### Uso de Centroides en el Proyecto

#### **K-Means Clustering**

**Sí, utilizamos centroides** en el algoritmo K-Means.

**Características de los Centroides:**
- **Número de Centroides:** 3 (uno por cada cluster)
- **Dimensión:** 3 dimensiones (cantidad, precio_unitario_detalle, importe)
- **Interpretación:** Cada centroide representa el "cliente promedio" o "transacción promedio" de su cluster

**Centroides en el Código:**
```python
# K-Means se entrena y calcula centroides internamente
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
clusters_kmeans = kmeans.fit_predict(X_scaled)

# Los centroides están disponibles en:
# kmeans.cluster_centers_
# Shape: (3, 3) - 3 clusters × 3 variables
```

**Uso de Centroides:**
- **Asignación de nuevos puntos:** Para clasificar una nueva transacción, se calcula la distancia a cada centroide y se asigna al cluster del centroide más cercano
- **Interpretación de clusters:** Los valores del centroide describen las características típicas del cluster
- **Visualización:** Los centroides pueden visualizarse como puntos en el espacio de características

#### **DBSCAN Clustering**

**No utiliza centroides** de la misma manera que K-Means.

**Diferencias:**
- DBSCAN agrupa puntos basándose en densidad, no en distancia a centroides
- No tiene un concepto de "centroide" como K-Means
- Los clusters se forman por densidad de puntos vecinos

---

## 📊 RESUMEN DE VARIABLES POR MODELO

### **Regresión (Predicción de Importe)**

| Componente | Detalles |
|------------|----------|
| **Variable Objetivo** | `importe` (float64) |
| **Variables Predictoras** | ~12-15 variables numéricas (cantidad, precios, categorías, medios de pago, ciudad) |
| **Mejor Modelo** | Random Forest Regressor |
| **Variable Más Importante** | `cantidad` |
| **Centroides** | ❌ No aplica (regresión) |

### **Clasificación (Segmentación de Clientes)**

| Componente | Detalles |
|------------|----------|
| **Variable Objetivo** | `segmento_cliente` (categórica: 'Bajo', 'Medio', 'Alto') |
| **Variables Predictoras** | ~11-14 variables numéricas (excluyendo importe para evitar data leakage) |
| **Mejor Modelo** | SVC / Logistic Regression |
| **Clases** | 3 clases balanceadas |
| **Centroides** | ❌ No aplica (clasificación supervisada) |

### **Clustering (Agrupación de Transacciones)**

| Componente | Detalles |
|------------|----------|
| **Variable Objetivo** | ❌ No hay (aprendizaje no supervisado) |
| **Variables Utilizadas** | 3 variables: `cantidad`, `precio_unitario_detalle`, `importe` |
| **Algoritmos** | K-Means (3 clusters), DBSCAN |
| **Centroides** | ✅ **SÍ, utilizados en K-Means** (3 centroides, uno por cluster) |
| **Normalización** | ✅ StandardScaler aplicado antes del clustering |

---

## 🎓 CONCLUSIÓN

### Variables Predictoras
- **Regresión:** ~12-15 variables numéricas (cantidad, precios, categorías, medios de pago, ciudad)
- **Clasificación:** ~11-14 variables numéricas (mismas que regresión, excluyendo importe)
- **Clustering:** 3 variables (cantidad, precio_unitario_detalle, importe)

### Variables Objetivo
- **Regresión:** `importe` (variable continua)
- **Clasificación:** `segmento_cliente` (variable categórica: Bajo, Medio, Alto)
- **Clustering:** No hay variable objetivo (aprendizaje no supervisado)

### Centroides
- **✅ SÍ utilizamos centroides** en K-Means clustering
- **3 centroides** (uno por cada cluster)
- **3 dimensiones** por centroide (cantidad, precio_unitario_detalle, importe)
- Los centroides representan el "prototipo" de cada cluster
- Se utilizan para asignar nuevas transacciones a clusters

---

## ⚠️ NOTA IMPORTANTE

**Este archivo se genera AUTOMÁTICAMENTE** con datos reales del proyecto cada vez que se ejecutan los modelos ML.

**Para regenerar este archivo:**
1. Ejecutar los modelos ML: `python 06_modelos_ml.py`
2. Ejecutar este script: `python 11_generar_variables_centroides.py`
3. El archivo se actualizará automáticamente con los datos más recientes

**Ventajas de la generación automática:**
- ✅ Siempre sincronizado con los modelos entrenados
- ✅ Datos específicos y actualizados del proyecto
- ✅ No requiere edición manual
- ✅ Coherencia garantizada entre modelos y documentación

---

**Proyecto desarrollado como parte del curso AI Fundamentals - Guayerd - IBM Skills Build**  
**Autor:** Enith Gicela Vargas Vargas  
**Fecha:** {self.fecha_actual}  
**Generado automáticamente:** {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}
