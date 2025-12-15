<!--
# SPRINT_3 - MACHINE LEARNING FUNDAMENTALS
**Autor:** Enith Gicela Vargas Vargas  
**Fecha:** 2025-11-11  
**Curso:** AI Fundamentals - Guayerd - IBM Skills Build  
**Sprint:** 3 - Machine Learning Fundamentals  
-->

# SPRINT_3 - MACHINE LEARNING FUNDAMENTALS

## 📋 Descripción General

Sprint_3 se enfoca en los fundamentos de Machine Learning, incluyendo conceptos teóricos, implementación práctica con scikit-learn, y demostraciones interactivas.

## 🎯 Objetivos del Sprint

### Fundamentos de Machine Learning
- Definición y conceptos básicos
- Tipos de aprendizajes (Supervisado, No Supervisado, Refuerzo)
- Algoritmos básicos (Regresión, Clasificación, Clustering)
- Métricas de evaluación

### Modelado con scikit-learn
- Preparación de datos para ML
- División train/test
- Proceso de entrenamiento
- Evaluación de modelos
- Algoritmos específicos

### Demo Interactivo
- Sistema de menú navegable
- Ejecución de módulos
- Visualización de resultados

## 📁 Estructura del Proyecto

```
Sprint_3/
├── Fundamentos/           # Conceptos teóricos de ML
├── Modelado/             # Implementación práctica
├── Demo/                 # Sistema interactivo
├── resultados/           # Archivos de salida
└── README.md            # Este archivo
```

## 🚀 Inicio Rápido

### 1. Activar entorno virtual
```bash
# Solo en Git Bash (NO PowerShell)
cd "ENITH VARGAS - PROYECTO AURELION"
source venv/Scripts/activate
```

### 2. Ejecutar demo interactivo
```bash
cd Sprint_3/Demo
python demo_interactivo.py
```

### 3. Ejecutar módulos individuales
```bash
# Fundamentos
cd Sprint_3/Fundamentos
python 01_machine_learning_basico.py

# Modelado
cd Sprint_3/Modelado
python 01_preparacion_datos.py
```

## 📚 Módulos Disponibles

### Fundamentos
- `01_machine_learning_basico.py` - Conceptos fundamentales
- `02_tipos_aprendizajes.py` - Tipos de aprendizaje
- `03_algoritmos_basicos.py` - Algoritmos principales
- `04_metricas_evaluacion.py` - Métricas de evaluación

### Modelado
- `01_preparacion_datos.py` - Preparación de datos con category_encoders
- `02_imputaciones_avanzadas.py` - Imputaciones estadísticas inteligentes
- `02_division_train_test.py` - División de conjuntos
- `03_proceso_entrenamiento.py` - Entrenamiento de modelos
- `04_evaluacion_modelos.py` - Evaluación de modelos
- `05_algoritmos_especificos.py` - Algoritmos específicos

### Demo
- `demo_interactivo.py` - Sistema principal de navegación

## ⚠️ Requisitos

- Python 3.8+
- Entorno virtual activado
- Dependencias instaladas (ver requirements.txt)
- **Solo usar Git Bash** (NO PowerShell)

## 🔧 Dependencias

```bash
pip install pandas numpy matplotlib seaborn scikit-learn scipy category-encoders
```

## 📖 Documentación

Cada módulo incluye:
- Documentación completa en español
- Código en inglés (clases, funciones, variables)
- Comentarios explicativos
- Ejemplos prácticos con datos de Aurelion

## 📚 Glosario de Términos Técnicos

### **Métricas de Evaluación de Modelos**

#### **R² (R cuadrado o Coeficiente de Determinación)**
**Definición:** Medida que indica qué porcentaje de la variabilidad de la variable objetivo es explicada por el modelo.

**Rango:** 0 a 1 (0% a 100%)

**Interpretación:**
- **R² > 0.9:** Excelente capacidad predictiva
- **0.7 < R² ≤ 0.9:** Buena capacidad predictiva
- **0.5 < R² ≤ 0.7:** Capacidad predictiva moderada
- **R² ≤ 0.5:** Capacidad predictiva limitada

**Ejemplo:** R² = 0.85 significa que el modelo explica el 85% de la variabilidad en los datos.

---

#### **MSE (Mean Squared Error - Error Cuadrático Medio)**
**Definición:** Promedio de los cuadrados de las diferencias entre valores predichos y reales.

**Características:**
- Penaliza más los errores grandes (porque eleva al cuadrado)
- Se mide en unidades al cuadrado de la variable objetivo

**Interpretación:** MSE bajo = errores pequeños en promedio

---

#### **RMSE (Root Mean Squared Error)**
**Definición:** Raíz cuadrada del MSE. Error en las mismas unidades que la variable objetivo.

**Ventaja:** Más interpretable que MSE porque está en las mismas unidades.

**Ejemplo:** RMSE = $50 significa que, en promedio, las predicciones se desvían $50 del valor real.

---

#### **MAE (Mean Absolute Error - Error Absoluto Medio)**
**Definición:** Promedio de las diferencias absolutas entre valores predichos y reales.

**Características:**
- Trata todos los errores por igual
- Menos sensible a outliers que RMSE

**Ejemplo:** MAE = $30 significa que, en promedio, las predicciones se desvían $30 del valor real.

---

#### **Accuracy (Precisión o Exactitud)**
**Definición:** Proporción de predicciones correctas sobre el total.

**Rango:** 0 a 1 (0% a 100%)

**Interpretación:**
- **Accuracy = 0.95:** El 95% de las predicciones son correctas
- Puede ser engañosa cuando las clases están desbalanceadas

---

#### **Precision (Precisión)**
**Definición:** De todas las predicciones positivas, ¿cuántas fueron realmente positivas?

**Interpretación:** Precision alta = cuando el modelo predice una clase, generalmente tiene razón

---

#### **Recall (Sensibilidad)**
**Definición:** De todos los casos realmente positivos, ¿cuántos logró identificar el modelo?

**Interpretación:** Recall alto = el modelo encuentra la mayoría de los casos positivos

---

#### **F1-Score**
**Definición:** Media armónica entre Precision y Recall. Balancea ambas métricas.

**Ventaja:** Útil cuando necesitas balancear Precision y Recall

---

### **Conceptos de Machine Learning**

#### **Train/Test Split (División Entrenamiento/Prueba)**
**Definición:** División de los datos en dos conjuntos: uno para entrenar el modelo y otro para evaluar su rendimiento.

**Propósito:** Evaluar qué tan bien el modelo generaliza a datos nuevos que no ha visto durante el entrenamiento.

**Proporción típica:** 70-80% para entrenamiento, 20-30% para prueba

---

#### **Cross-Validation (Validación Cruzada)**
**Definición:** Técnica que divide los datos en múltiples subconjuntos (folds) y entrena/evalúa el modelo múltiples veces.

**Ventaja:** Proporciona una estimación más robusta del rendimiento del modelo

---

#### **Overfitting (Sobreajuste)**
**Definición:** Cuando el modelo se ajusta demasiado a los datos de entrenamiento y no generaliza bien a datos nuevos.

**Síntomas:** R² alto en entrenamiento pero bajo en prueba

---

#### **Underfitting (Subajuste)**
**Definición:** Cuando el modelo es demasiado simple y no captura los patrones en los datos.

**Síntomas:** R² bajo tanto en entrenamiento como en prueba

---

#### **Feature Scaling (Escalado de Características)**
**Definición:** Proceso de normalizar variables a una escala común.

**Tipos:**
- **Min-Max:** Escala a rango [0, 1]
- **Z-score:** Transforma a media 0 y desviación estándar 1

**Importancia:** Algunos algoritmos (SVM, K-Means) son sensibles a la escala

---

#### **Hyperparameters (Hiperparámetros)**
**Definición:** Parámetros del modelo que se configuran antes del entrenamiento (no se aprenden de los datos).

**Ejemplos:** Número de árboles en Random Forest, profundidad máxima, tasa de aprendizaje

---

### **Algoritmos Comunes**

#### **Linear Regression (Regresión Lineal)**
**Definición:** Modelo que encuentra una línea recta que mejor se ajusta a los datos.

**Uso:** Predicción de valores continuos (precios, ventas, etc.)

---

#### **Random Forest**
**Definición:** Algoritmo de ensemble que combina múltiples árboles de decisión.

**Ventajas:** Robusto, maneja relaciones no lineales, proporciona importancia de variables

---

#### **SVR (Support Vector Regression)**
**Definición:** Versión de regresión de Support Vector Machines.

**Características:** Efectivo para datos no lineales, sensible a la escala

---

#### **Logistic Regression (Regresión Logística)**
**Definición:** Modelo para clasificación binaria o multiclase.

**Uso:** Predicción de categorías (sí/no, clase A/B/C, etc.)

---

#### **K-Means Clustering**
**Definición:** Algoritmo no supervisado que agrupa datos en K grupos.

**Uso:** Segmentación de clientes, identificación de patrones

---

**Nota:** Para explicaciones más detalladas de términos estadísticos (skewness, kurtosis, correlación de Pearson), consulta el glosario completo en `Sprint_2/Enith Gicela Vargas Vargas - Proyecto Aurelion/resultados/histogramas/ANALISIS_GRAFICOS.md`.

**Nota:** Este archivo se genera automáticamente con datos reales del proyecto cada vez que se ejecutan las visualizaciones avanzadas en Sprint_2.

## 🎓 Resultados Esperados

Al completar Sprint_3, el estudiante habrá:
- Comprendido los fundamentos de Machine Learning
- Implementado algoritmos básicos con scikit-learn
- Evaluado modelos usando métricas apropiadas
- Creado un sistema interactivo funcional

---

*Proyecto desarrollado como parte del curso AI Fundamentals de Guayerd e IBM Skills Build*
