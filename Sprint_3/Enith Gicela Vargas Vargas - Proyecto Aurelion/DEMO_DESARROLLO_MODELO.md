# DEMO ASINCRÓNICA - DESARROLLO DEL MODELO - PROYECTO AURELION

**Autor:** Enith Gicela Vargas Vargas  
**Camada:** 1  
**Grupo:** 11  
**Curso:** AI Fundamentals - Guayerd - IBM Skills Build  
**Fecha:** Noviembre 2025  
**Proyecto:** Aurelion - Demo Asincrónica  
**Módulo:** Presentación del Desarrollo del Modelo

---

## 📋 INTRODUCCIÓN

Este documento presenta de manera estructurada el proceso completo de desarrollo del modelo de Machine Learning, siguiendo los 10 pasos fundamentales del desarrollo de modelos:

1. Objetivo del modelo
2. Descripción del dataset (X e y)
3. Preprocesamiento
4. División Train/Test
5. Selección del algoritmo elegido
6. Entrenamiento del modelo (.fit())
7. Predicciones (.predict())
8. Métricas de evaluación
9. Modelo final implementado
10. Gráficos y conclusiones

---

## 1️⃣ OBJETIVO DEL MODELO

### OBJETIVO PRINCIPAL

Desarrollar modelos de Machine Learning para predecir y analizar el comportamiento de ventas en la Tienda Aurelion.

### OBJETIVOS ESPECÍFICOS

#### 📊 REGRESIÓN

- **Objetivo:** Predecir el importe de ventas basándose en características como cantidad, precio unitario, categoría, medio de pago, etc.
- **Modelo:** Random Forest Regressor
- **Métrica objetivo:** R² > 0.95 (95% de variabilidad explicada)
- **Resultado obtenido:** R² = 0.9962 (99.62%) ⭐ Excelente

#### 🎯 CLASIFICACIÓN

- **Objetivo:** Clasificar clientes en segmentos (Bajo, Medio, Alto) según su comportamiento de compra
- **Modelo:** SVC / Logistic Regression
- **Métrica objetivo:** Accuracy > 0.85 (85% de precisión)
- **Resultado obtenido:** Accuracy = 0.8841 (88.41%) ⭐ Muy bueno

#### 🔍 CLUSTERING

- **Objetivo:** Agrupar transacciones similares para identificar patrones de comportamiento
- **Modelo:** K-Means Clustering
- **Objetivo:** Identificar 3 grupos naturales de transacciones
- **Resultado obtenido:** 3 clusters identificados, Silhouette Score = 0.39

---

## 2️⃣ DESCRIPCIÓN DEL DATASET (X e y)

### 📊 ESTRUCTURA DEL DATASET

- **Total de registros:** 343 líneas de detalle
- **Clientes únicos:** 100 clientes
- **Productos únicos:** 100 productos
- **Ventas únicas:** 120 transacciones

### 📋 VARIABLES PREDICTORAS (X - Features)

#### Variables Numéricas:

- **cantidad:** Cantidad de productos por línea de venta (rango: 1-5)
- **precio_unitario_detalle:** Precio unitario del producto
- **importe:** Importe total de la línea (variable objetivo para regresión)
- **edad_cliente:** Edad del cliente

#### Variables Categóricas (codificadas):

- **categoria:** Categoría del producto (Alimentos, Limpieza)
- **medio_pago:** Método de pago (efectivo, tarjeta, qr, transferencia)
- **ciudad:** Ciudad del cliente (6 ciudades diferentes: Carlos Paz, Rio Cuarto, Córdoba, Villa María, Alta Gracia, Mendiolaza)
- **genero_cliente:** Género del cliente

### 🎯 VARIABLES OBJETIVO (y - Target)

#### Para REGRESIÓN:

- **y = importe** (variable continua)
- **Objetivo:** Predecir el importe de una venta
- **Rango:** $272 - $20,345 pesos argentinos

#### Para CLASIFICACIÓN:

- **y = segmento_cliente** (variable categórica: Bajo, Medio, Alto)
- **Objetivo:** Clasificar clientes en segmentos según su comportamiento de compra
- **Distribución:** Aproximadamente 33% Bajo, 33% Medio, 33% Alto

#### Para CLUSTERING:

- **No hay variable objetivo** (aprendizaje no supervisado)
- **Features utilizadas:** cantidad, precio_unitario_detalle, importe

### 📐 DIMENSIONES FINALES

- **Dataset final:** 343 registros × 27 columnas
- **Features (X):** ~12-15 variables predictoras
- **Target (y):** 1 variable objetivo (según el tipo de problema)

---

## 3️⃣ PREPROCESAMIENTO

### 🔧 TÉCNICAS APLICADAS

#### 1. IMPUTACIÓN DE VALORES FALTANTES

- **Mediana:** Para distribuciones sesgadas (skewness > 1)
- **Media:** Para distribuciones normales (skewness ≤ 1)
- **Moda:** Para variables categóricas
- **Resultado:** 0 valores nulos (100% completitud)

#### 2. TRATAMIENTO DE OUTLIERS

- **Método:** Winsorization (limitación a percentiles 5 y 95)
- **Outliers detectados:** 7 en variable 'importe' (2.0%)
- **Resultado:** Outliers tratados sin pérdida de información
- **Beneficio:** Distribución más estable, modelos más robustos

#### 3. NORMALIZACIÓN DE VARIABLES NUMÉRICAS

- **StandardScaler:** Para 'importe' (media=0, std=1)
  - Rango original: $272 - $20,345
  - Rango normalizado: -1.44 a 2.45
- **MinMaxScaler:** Para 'cantidad' y 'precio_unitario' (rango [0,1])
  - cantidad: 1-5 → 0.0-1.0
  - precio_unitario: $272-$4,982 → 0.0-1.0
- **Selección automática:** Basada en skewness de cada variable

#### 4. CODIFICACIÓN DE VARIABLES CATEGÓRICAS

- **OneHot Encoding:**
  - categoria: 2 columnas (categoria_Alimentos, categoria_Limpieza)
  - medio_pago: 4 columnas (medio_pago_efectivo, medio_pago_tarjeta, medio_pago_qr, medio_pago_transferencia)
- **Binary Encoding:**
  - ciudad: 6 categorías codificadas de forma compacta
- **Resultado:** Todas las variables son numéricas (listas para ML)

#### 5. MERGE DE TABLAS

- **Método:** LEFT JOIN entre ventas, clientes, productos y detalle_ventas
- **Validación:** Integridad referencial verificada (0 registros huérfanos)
- **Resultado:** Dataset unificado con 343 registros × 27 columnas

### ✅ RESULTADO FINAL DEL PREPROCESAMIENTO

- ✅ Dataset completamente limpio y normalizado
- ✅ 0 valores nulos (100% completitud)
- ✅ Todas las variables en escalas comparables
- ✅ Outliers tratados adecuadamente
- ✅ Variables categóricas codificadas
- ✅ Listo para Machine Learning

---

## 4️⃣ DIVISIÓN TRAIN/TEST

### 📊 MÉTODO UTILIZADO: Holdout Method (Método de Retención)

#### 🔧 IMPLEMENTACIÓN

- **Función:** `train_test_split()` de scikit-learn
- **Proporción:** 80% entrenamiento / 20% prueba
- **random_state:** 42 (para reproducibilidad)
- **Estratificación:** Sí (para clasificación, mantiene proporciones de clases)

#### 📐 DIVISIÓN DE DATOS

- **Total de registros:** 343
- **Conjunto de Entrenamiento (Train):**
  - X_train: 274 registros (80%)
  - y_train: 274 registros (80%)
- **Conjunto de Prueba (Test/Holdout):**
  - X_test: 69 registros (20%)
  - y_test: 69 registros (20%)

#### 🎯 PROPÓSITO

- **Train:** Entrenar el modelo (ajustar parámetros)
- **Test:** Evaluar la generalización (datos nunca vistos durante el entrenamiento)

#### ✅ VALIDACIÓN ADICIONAL

- **K-Fold Cross-Validation (K=5):** Para validación robusta
- **5 divisiones diferentes:** Para mayor confiabilidad
- **Resultado:** R² promedio = 0.9981 ± 0.0022 (muy consistente)

---

## 5️⃣ SELECCIÓN DEL ALGORITMO ELEGIDO

### 🔍 ESTRATEGIA DE SELECCIÓN

Se implementaron múltiples algoritmos para comparar rendimiento y seleccionar el mejor para cada tipo de problema.

### 📊 ALGORITMOS PROBADOS

#### REGRESIÓN:

1. **Linear Regression**
   - R² = 0.8499 (84.99%)
   - Modelo baseline simple e interpretable
   - Indica que hay relaciones no lineales en los datos

2. **Random Forest Regressor** ⭐ MEJOR
   - R² = 0.9962 (99.62%)
   - n_estimators = 100
   - Maneja relaciones no lineales y complejas
   - Proporciona importancia de características

3. **SVR (Support Vector Regression)**
   - R² = 0.9918 (99.18%)
   - Kernel RBF para relaciones no lineales
   - Maneja outliers bien

#### CLASIFICACIÓN:

1. **Logistic Regression** ⭐ MEJOR
   - Accuracy = 0.8841 (88.41%)
   - max_iter = 1000, solver = 'lbfgs'
   - Interpretable, proporciona probabilidades
   - Rápido y eficiente

2. **Random Forest Classifier**
   - Accuracy = 0.8261 (82.61%)
   - Puede sobreajustar
   - Alta precisión pero menor generalización

3. **SVC (Support Vector Classifier)** ⭐ MEJOR
   - Accuracy = 0.8841 (88.41%)
   - Igual rendimiento que Logistic Regression
   - Buena generalización
   - Encuentra fronteras de decisión complejas

#### CLUSTERING:

1. **K-Means** ⭐ ELEGIDO
   - n_clusters = 3
   - Silhouette Score = 0.39
   - Simple, rápido, interpretable
   - Proporciona centroides interpretables

2. **DBSCAN**
   - 5 clusters detectados automáticamente
   - Detecta outliers (puntos noise)
   - No requiere especificar número de clusters

### ✅ ALGORITMO FINAL ELEGIDO

- **Regresión:** Random Forest Regressor (R² = 99.62%)
- **Clasificación:** SVC / Logistic Regression (Accuracy = 88.41%)
- **Clustering:** K-Means (3 clusters, Silhouette = 0.39)

---

## 6️⃣ ENTRENAMIENTO DEL MODELO (.fit())

### 🔧 MÉTODO UTILIZADO: `.fit(X_train, y_train)`

#### 📝 CÓDIGO DE EJEMPLO

```python
# 1. Preparar datos
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 2. Crear modelo
modelo = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

# 3. Entrenar con .fit()
modelo.fit(X_train, y_train)
```

#### ⚙️ PROCESO INTERNO DE .fit()

1. **Análisis de datos:**
   - El modelo analiza la relación entre X_train e y_train
   - Identifica patrones y correlaciones

2. **Cálculo de parámetros:**
   - **Regresión:** Coeficientes, estructura de árboles, pesos
   - **Clasificación:** Pesos, fronteras de decisión, hiperplanos
   - **Clustering:** Centroides, asignación de clusters

3. **Optimización:**
   - Ajusta el modelo para minimizar el error:
     - **Regresión:** Minimiza MSE (Mean Squared Error)
     - **Clasificación:** Minimiza Cross-Entropy Loss
   - Usa algoritmos de optimización (gradiente descendente, etc.)

4. **Aislamiento de datos de prueba:**
   - **Nunca** ve los datos de prueba durante este proceso
   - Solo aprende de X_train e y_train

#### 📊 RESULTADOS DEL ENTRENAMIENTO

**REGRESIÓN (Random Forest):**
- R² en entrenamiento: 0.9970 (99.70%)
- R² en prueba: 0.9962 (99.62%)
- Diferencia: 0.0008 (muy pequeña → no hay overfitting)
- Interpretación: El modelo generaliza excelentemente

**CLASIFICACIÓN (SVC/Logistic):**
- Accuracy en entrenamiento: 0.8869 (88.69%)
- Accuracy en prueba: 0.8841 (88.41%)
- Diferencia: 0.0028 (muy pequeña → buena generalización)
- Interpretación: El modelo no memoriza, aprende patrones generales

**CLUSTERING (K-Means):**
- 3 clusters identificados
- 343 muestras distribuidas entre los 3 clusters
- Centroides calculados para cada cluster
- Shape de centroides: (3, 3) → 3 clusters × 3 variables

### ✅ MODELO ENTRENADO Y LISTO

- ✅ Parámetros ajustados a los datos de entrenamiento
- ✅ Modelo optimizado para minimizar error
- ✅ Listo para hacer predicciones con `.predict()`

---

## 7️⃣ PREDICCIONES (.predict())

### 🔧 MÉTODO UTILIZADO: `.predict(X_test)`

#### 📝 CÓDIGO DE EJEMPLO

```python
# Modelo ya entrenado con .fit()
modelo.fit(X_train, y_train)

# Hacer predicciones con .predict()
y_pred_train = modelo.predict(X_train)  # Predicciones en entrenamiento
y_pred_test = modelo.predict(X_test)    # Predicciones en prueba
```

#### ⚙️ PROCESO INTERNO DE .predict()

1. **Recibe datos nuevos:**
   - X_test: Características de datos que el modelo nunca ha visto
   - No necesita y (la respuesta) porque el modelo la va a predecir

2. **Aplica modelo entrenado:**
   - Usa los parámetros aprendidos durante `.fit()`
   - Aplica las reglas/patrones aprendidos a los nuevos datos
   - Genera predicciones basadas en lo aprendido

3. **Genera predicciones:**
   - y_pred: Predicciones del modelo para los nuevos datos
   - Formato: Array de predicciones (una por cada registro en X_test)

#### 📊 EJEMPLO DE PREDICCIÓN EN AURELION

**REGRESIÓN:**
```
Input (X): 
  - cantidad = 4
  - precio_unitario = 2500
  - categoria = 'Alimentos'
  - medio_pago = 'tarjeta'
  - ciudad = 'Córdoba'
  - ...

Output (y_pred): 
  - importe_predicho = $10,000

Comparación: 
  - importe_real = $9,800
  - Error = $200 (2% de error)
```

**CLASIFICACIÓN:**
```
Input (X): 
  - Características del cliente (edad, género, ciudad, historial)

Output (y_pred): 
  - segmento_predicho = 'Alto'

Comparación: 
  - segmento_real = 'Alto'
  - Resultado: ✅ Predicción correcta
```

**CLUSTERING:**
```
Input (X): 
  - cantidad = 3
  - precio_unitario_detalle = 2000
  - importe = 6000

Output (y_pred): 
  - cluster = 2

Interpretación: 
  - Transacción pertenece al cluster 2
  - Similar a otras transacciones del mismo cluster
```

#### 📈 USO DE PREDICCIONES

- **Evaluar rendimiento:** Comparar predicciones con valores reales
- **Calcular métricas:** Accuracy, R², Precision, Recall, etc.
- **Visualizar resultados:** Gráficos de predicciones vs reales
- **Producción:** Hacer predicciones sobre datos nuevos en tiempo real

---

## 8️⃣ MÉTRICAS DE EVALUACIÓN

### 📊 MÉTRICAS PARA REGRESIÓN

#### 1. R² (Coeficiente de Determinación)

- **Fórmula:** R² = 1 - (SS_res / SS_tot)
  - SS_res = Σ(y_real - y_pred)² (suma de errores al cuadrado)
  - SS_tot = Σ(y_real - y_promedio)² (suma de diferencias respecto al promedio)
- **Rango:** -∞ a 1 (ideal: 1.0)
- **Interpretación:** % de varianza explicada por el modelo
- **Resultado:** R² = 0.9962 (99.62%) ⭐ Excelente
- **Significado:** El modelo explica el 99.62% de la variabilidad en los importes

#### 2. MSE (Mean Squared Error)

- **Fórmula:** MSE = (1/n) × Σ(y_real - y_pred)²
- **Interpretación:** Error promedio al cuadrado
- **Características:** Penaliza más los errores grandes
- **Resultado:** MSE muy bajo (errores pequeños)

#### 3. RMSE (Root Mean Squared Error)

- **Fórmula:** RMSE = √MSE
- **Interpretación:** Error promedio en unidades originales
- **Ventaja:** Más interpretable que MSE (mismas unidades que la variable objetivo)

#### 4. MAE (Mean Absolute Error)

- **Fórmula:** MAE = (1/n) × Σ|y_real - y_pred|
- **Interpretación:** Error promedio absoluto
- **Ventaja:** Menos sensible a outliers que RMSE

#### 5. Cross-Validation (K-Fold CV, K=5)

- **R² promedio:** 0.9981
- **Desviación estándar:** ±0.0022
- **Interpretación:** Modelo muy consistente en diferentes divisiones
- **Significado:** El rendimiento es estable y confiable

### 📊 MÉTRICAS PARA CLASIFICACIÓN

#### 1. Accuracy (Precisión Global)

- **Fórmula:** Accuracy = (TP + TN) / (TP + TN + FP + FN)
- **Interpretación:** % de predicciones correctas sobre el total
- **Resultado:** 0.8841 (88.41%) ⭐ Muy bueno
- **Significado:** De cada 100 predicciones, 88 son correctas

#### 2. Precision (Precisión por Clase)

- **Fórmula:** Precision = TP / (TP + FP)
- **Interpretación:** De las predicciones positivas, cuántas son correctas
- **Resultado:** ~0.89 (89%)
- **Ejemplo:** Cuando el modelo predice "Alto", tiene razón el 89% de las veces

#### 3. Recall (Sensibilidad)

- **Fórmula:** Recall = TP / (TP + FN)
- **Interpretación:** De los casos reales, cuántos se detectaron
- **Resultado:** ~0.83 (83%)
- **Ejemplo:** De todos los clientes realmente "Alto", el modelo detecta el 83%

#### 4. F1-Score

- **Fórmula:** F1-Score = 2 × (Precision × Recall) / (Precision + Recall)
- **Interpretación:** Balance entre Precision y Recall
- **Resultado:** ~0.86 (86%)
- **Uso:** Útil cuando necesitas balancear ambas métricas

#### 5. Matriz de Confusión

```
                    Predicción del Modelo
                  Bajo  Medio  Alto    Total Real
Valor    Bajo     28     2     0        30
Real     Medio     3    29     3        35
         Alto      0     4    31        35
```

- **Diagonal:** Predicciones correctas (88 de 100)
- **Fuera de diagonal:** Errores de clasificación
- **Interpretación:** Muestra exactamente dónde se equivoca el modelo

### 📊 MÉTRICAS PARA CLUSTERING

#### 1. Silhouette Score

- **Rango:** -1 a 1 (ideal: cercano a 1)
- **Resultado:** 0.39 ⭐ Aceptable
- **Interpretación:** Clusters moderadamente bien definidos
- **Significado:** Los puntos dentro de cada cluster son similares entre sí

#### 2. Número de Clusters

- **K-Means:** 3 clusters identificados
- **DBSCAN:** 5 clusters detectados automáticamente
- **Muestras:** 343 muestras distribuidas entre los clusters
- **Centroides:** 3 centroides generados (uno por cada cluster)

### ✅ EVALUACIÓN GENERAL

- ✅ **Regresión:** Excelente (R² = 99.62%)
- ✅ **Clasificación:** Muy buena (Accuracy = 88.41%)
- ✅ **Clustering:** Aceptable (Silhouette = 0.39)
- ✅ **No hay overfitting:** Train ≈ Test (diferencia < 0.01)
- ✅ **Modelo generaliza bien:** Funciona bien en datos nuevos

---

## 9️⃣ MODELO FINAL IMPLEMENTADO

### ✅ MODELOS FINALES SELECCIONADOS

#### 📊 REGRESIÓN - Random Forest Regressor

```python
from sklearn.ensemble import RandomForestRegressor

modelo_regresion = RandomForestRegressor(
    n_estimators=100,      # 100 árboles
    random_state=42,       # Reproducibilidad
    max_depth=None,        # Sin límite de profundidad
    min_samples_split=2,   # Mínimo de muestras para dividir
    min_samples_leaf=1     # Mínimo de muestras en hoja
)

# Entrenar
modelo_regresion.fit(X_train, y_train)

# Predecir
y_pred = modelo_regresion.predict(X_test)
```

**Características:**
- R² = 0.9962 (99.62%)
- MSE muy bajo
- Generaliza excelentemente
- Proporciona importancia de características

#### 🎯 CLASIFICACIÓN - SVC / Logistic Regression

**Opción 1: SVC**
```python
from sklearn.svm import SVC

modelo_clasificacion = SVC(random_state=42)

# Entrenar
modelo_clasificacion.fit(X_train, y_train)

# Predecir
y_pred = modelo_clasificacion.predict(X_test)
```

**Opción 2: Logistic Regression**
```python
from sklearn.linear_model import LogisticRegression

modelo_clasificacion = LogisticRegression(
    random_state=42,
    max_iter=1000,
    solver='lbfgs'
)

# Entrenar
modelo_clasificacion.fit(X_train, y_train)

# Predecir
y_pred = modelo_clasificacion.predict(X_test)
```

**Características:**
- Accuracy = 0.8841 (88.41%)
- Precision = ~0.89 (89%)
- Recall = ~0.83 (83%)
- Ambos modelos tienen el mismo rendimiento

#### 🔍 CLUSTERING - K-Means

```python
from sklearn.cluster import KMeans

modelo_clustering = KMeans(
    n_clusters=3,          # 3 grupos
    random_state=42,       # Reproducibilidad
    n_init=10              # 10 inicializaciones
)

# Entrenar y predecir
clusters = modelo_clustering.fit_predict(X)
```

**Características:**
- 3 clusters identificados
- Silhouette Score = 0.39
- Centroides calculados para cada cluster
- 343 muestras distribuidas entre los 3 clusters

### 💾 GUARDADO DE MODELOS

- **Formato:** .pkl (pickle)
- **Ubicación:** `resultados/modelos/`
- **Ventaja:** Permite reutilizar modelos sin reentrenar
- **Uso:** Cargar modelos guardados para hacer predicciones en producción

---

## 🔟 GRÁFICOS Y CONCLUSIONES

### 📊 VISUALIZACIONES GENERADAS

#### 1. COMPARACIÓN DE MODELOS

- Gráficos de barras comparando R²/Accuracy entre modelos
- Visualización de métricas train vs test
- Identificación del mejor modelo

#### 2. PREDICCIONES VS VALORES REALES

- Scatter plots: y_pred vs y_real
- Línea de regresión perfecta (y=x)
- Distribución de errores
- Análisis de residuos

#### 3. MATRICES DE CONFUSIÓN

- Heatmaps mostrando predicciones correctas/incorrectas
- Análisis por clase (Bajo, Medio, Alto)
- Visualización de errores de clasificación

#### 4. CLUSTERING

- Visualización 2D/3D de clusters
- Centroides marcados
- Distribución de muestras por cluster
- Análisis de características por cluster

#### 5. IMPORTANCIA DE CARACTERÍSTICAS

- Feature importance de Random Forest
- Variables más relevantes para las predicciones
- Análisis de contribución de cada variable

#### 6. DISTRIBUCIÓN DE ERRORES

- Histogramas de residuos
- Análisis de outliers en predicciones
- Distribución normal de errores

#### 7. VALIDACIÓN CRUZADA

- Scores por fold
- Variabilidad entre divisiones
- Consistencia del modelo

### 📈 TOTAL DE GRÁFICOS GENERADOS

**24 visualizaciones avanzadas** que incluyen:
- Comparaciones de modelos
- Análisis de predicciones
- Visualizaciones de clustering
- Matrices de confusión
- Distribuciones y correlaciones

---

## 📝 CONCLUSIONES

### ✅ LOGROS PRINCIPALES

#### 1. MODELOS DE ALTA CALIDAD

- **Regresión:** R² = 99.62% (excelente)
  - El modelo explica casi toda la variabilidad en los importes
  - Errores muy pequeños en las predicciones
  
- **Clasificación:** Accuracy = 88.41% (muy bueno)
  - Alta precisión en la segmentación de clientes
  - Balance adecuado entre Precision y Recall
  
- **Clustering:** 3 grupos bien definidos
  - Identificación de patrones de comportamiento
  - Centroides interpretables

#### 2. PREPROCESAMIENTO EXITOSO

- ✅ 0 valores nulos (100% completitud)
- ✅ Outliers tratados adecuadamente (Winsorization)
- ✅ Variables normalizadas y codificadas
- ✅ Dataset listo para Machine Learning

#### 3. GENERALIZACIÓN EXCELENTE

- ✅ Train y test tienen rendimiento similar
- ✅ Diferencia < 0.01 entre train y test
- ✅ No hay overfitting
- ✅ Modelo funciona bien en datos nuevos

#### 4. VALIDACIÓN ROBUSTA

- ✅ Holdout method (80/20)
- ✅ K-Fold Cross-Validation (K=5)
- ✅ Resultados consistentes (desviación estándar baja)
- ✅ Confianza alta en el rendimiento del modelo

### 🎯 APLICACIONES PRÁCTICAS

#### PREDICCIÓN DE VENTAS

- Predecir importe de ventas futuras
- Optimizar inventario basándose en predicciones
- Planificar estrategias de precios
- Identificar oportunidades de crecimiento

#### SEGMENTACIÓN DE CLIENTES

- Identificar clientes de alto valor
- Personalizar campañas de marketing
- Mejorar retención de clientes
- Optimizar estrategias de fidelización

#### ANÁLISIS DE PATRONES

- Identificar grupos de transacciones similares
- Detectar comportamientos anómalos
- Optimizar mix de productos
- Entender preferencias de clientes

### 📊 IMPACTO EN EL NEGOCIO

- ✅ **Mejora en la toma de decisiones:** Basada en datos y predicciones confiables
- ✅ **Optimización de recursos:** Asignación más eficiente de inventario y marketing
- ✅ **Mayor comprensión:** Del comportamiento del cliente y patrones de venta
- ✅ **Base sólida:** Para implementación en producción
- ✅ **Escalabilidad:** Modelos listos para crecer con más datos

### 🔮 PRÓXIMOS PASOS

1. **Implementación en producción:**
   - Desplegar modelos en sistema de producción
   - Integrar con sistemas de ventas existentes

2. **Monitoreo continuo:**
   - Evaluar rendimiento en tiempo real
   - Reentrenar modelos periódicamente

3. **Mejoras futuras:**
   - Incorporar más variables (temporalidad, estacionalidad)
   - Probar algoritmos más avanzados
   - Optimizar hiperparámetros

---

## 📚 REFERENCIAS Y DOCUMENTACIÓN

- **Informe Completo:** `INFORME_PROYECTO_AURELION.md`
- **Código del Modelo:** `Sprint_2/Enith Gicela Vargas Vargas - Proyecto Aurelion/06_modelos_ml.py`
- **Demo Interactiva:** `Sprint_3/Enith Gicela Vargas Vargas - Proyecto Aurelion/demo_desarrollo_modelo.py`
- **Documentación Técnica:** `Sprint_2/.../resultados/DOCUMENTACION_TECNICA.md`

---

**Proyecto desarrollado como parte del curso AI Fundamentals - Guayerd - IBM Skills Build**  
**Autor:** Enith Gicela Vargas Vargas  
**Fecha:** Noviembre 2025

