#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
<!--
# ALGORITMOS BASICOS ML - SPRINT_3
**Autor:** Enith Gicela Vargas Vargas  
**Camada:** 1  
**Grupo:** 11  
**Fecha:** 2025-11-11  
**Curso:** AI Fundamentals - Guayerd - IBM Skills Build  
**Sprint:** 3 - Machine Learning Fundamentals  
**Módulo:** Fundamentos - Algoritmos Básicos  
-->

ALGORITMOS BASICOS DE ML - PROYECTO AURELION SPRINT_3
======================================================

Script para explicar los algoritmos básicos de Machine Learning:
- Algoritmos de Regresión
- Algoritmos de Clasificación
- Algoritmos de Clustering
- Visualizaciones y ejemplos
"""

import pandas as pd          # Librería para manipulación de datos
import numpy as np           # Librería para cálculos numéricos
import matplotlib.pyplot as plt  # Librería para visualizaciones
import seaborn as sns       # Librería para gráficos estadísticos
import warnings             # Módulo para controlar avisos
warnings.filterwarnings('ignore')

class BasicAlgorithms:
    """
    Clase para explicar algoritmos básicos de ML.
    
    Funcionalidades:
    - Algoritmos de Regresión
    - Algoritmos de Clasificación
    - Algoritmos de Clustering
    - Visualizaciones y ejemplos
    """
    
    def __init__(self):
        """Inicializar el explicador de algoritmos."""
        print("ALGORITMOS BASICOS DE MACHINE LEARNING")
        print("Grupo 11 - Camada 1 | Enith Gicela Vargas Vargas")
        print("=" * 60)
        
    def cost_function(self):
        """Explicar función costo en Machine Learning."""
        print("\nFUNCION COSTO (COST FUNCTION)")
        print("-" * 50)
        
        print("""
DEFINICION:
La funcion costo (tambien llamada funcion de perdida o loss function) 
mide que tan mal esta funcionando nuestro modelo. Es una metrica que 
cuantifica el error entre las predicciones del modelo y los valores reales.

OBJETIVO:
Minimizar la funcion costo para obtener el mejor modelo posible.

TIPOS DE FUNCIONES COSTO:

1. REGRESION:
   • MSE (Mean Squared Error) - Error Cuadratico Medio
     Formula: J(θ) = (1/2m) * Σ(y_pred - y_true)²
     Caracteristicas:
       - Penaliza mas los errores grandes
       - Siempre positiva
       - Diferentiable (importante para optimizacion)
     
   • MAE (Mean Absolute Error) - Error Absoluto Medio
     Formula: J(θ) = (1/m) * Σ|y_pred - y_true|
     Caracteristicas:
       - Penaliza errores de forma lineal
       - Menos sensible a outliers que MSE
       - No es diferenciable en cero

2. CLASIFICACION:
   • Cross-Entropy Loss (Log Loss)
     Formula: J(θ) = -(1/m) * Σ[y*log(p) + (1-y)*log(1-p)]
     Caracteristicas:
       - Usada en clasificacion binaria
       - Penaliza predicciones incorrectas con alta confianza
       - Diferentiable

   • Hinge Loss (SVM)
     Formula: J(θ) = max(0, 1 - y*y_pred)
     Caracteristicas:
       - Usada en Support Vector Machines
       - Penaliza solo predicciones incorrectas

EJEMPLO PRACTICO - REGRESION LINEAL:
------------------------------------
Para regresion lineal, la funcion costo es MSE:

  J(θ₀, θ₁) = (1/2m) * Σ(h(x) - y)²

Donde:
  - h(x) = θ₀ + θ₁*x  (hipotesis/prediccion)
  - y = valor real
  - m = numero de ejemplos
  - θ₀, θ₁ = parametros del modelo (pendiente e intercepto)

PROCESO DE OPTIMIZACION:
1. Inicializar parametros (θ₀, θ₁) aleatoriamente
2. Calcular funcion costo con esos parametros
3. Ajustar parametros para reducir el costo
4. Repetir hasta encontrar minimo

EJEMPLO VISUAL:
""")
        
        # Ejemplo visual simple de función costo
        try:
            # Crear datos de ejemplo
            np.random.seed(42)
            X = np.array([1, 2, 3, 4, 5])
            y = np.array([2, 4, 5, 8, 9])
            
            # Calcular MSE para diferentes pendientes
            pendientes = np.linspace(0, 3, 50)
            costos = []
            
            for m in pendientes:
                y_pred = m * X
                mse = np.mean((y_pred - y) ** 2)
                costos.append(mse)
            
            print(f"   Ejemplo con datos: X={X}, y={y}")
            print(f"   Funcion costo (MSE) calculada para diferentes pendientes")
            min_idx = np.argmin(costos)
            print(f"   Pendiente optima: {pendientes[min_idx]:.2f}")
            print(f"   Costo minimo: {costos[min_idx]:.2f}")
            
        except Exception as e:
            print(f"   (Ejemplo visual no disponible: {e})")
        
        print("""
IMPORTANCIA:
- La funcion costo guia el aprendizaje del modelo
- Diferentes funciones costo dan diferentes resultados
- La eleccion depende del tipo de problema
- Debe ser diferenciable para usar gradiente descendente

RELACION CON OPTIMIZACION:
El objetivo del entrenamiento es encontrar los parametros que 
minimizan la funcion costo. Esto se hace mediante algoritmos de 
optimizacion como:
  • Gradiente Descendente (Gradient Descent)
  • Descenso de Gradiente Estocastico (SGD)
  • Adam, RMSprop (para redes neuronales)
        """)
    
    def regression_algorithms(self):
        """Explicar algoritmos de regresión."""
        print("\nALGORITMOS DE REGRESION")
        print("-" * 50)
        
        algoritmos = {
            'Linear Regression': {
                'descripcion': 'Prediccion lineal usando minimos cuadrados',
                'ecuacion': 'y = mx + b',
                'funcion_costo': 'MSE (Mean Squared Error) - Minimiza suma de errores cuadrados',
                'optimizacion': 'Gradiente Descendente o Ecuacion Normal',
                'ventajas': ['Simple', 'Interpretable', 'Rapido'],
                'desventajas': ['Solo relaciones lineales', 'Sensible a outliers'],
                'cuando_usar': 'Relacion lineal clara entre variables'
            },
            'Random Forest Regressor': {
                'descripcion': 'Conjunto de arboles de decision para prediccion',
                'ecuacion': 'Promedio de predicciones de multiples arboles',
                'ventajas': ['Robusto', 'No sobreajusta', 'Maneja no-linealidad'],
                'desventajas': ['Menos interpretable', 'Mas lento'],
                'cuando_usar': 'Relaciones complejas y no lineales'
            },
            'SVR (Support Vector Regression)': {
                'descripcion': 'Regresion usando vectores de soporte',
                'ecuacion': 'Optimiza margen de separacion',
                'ventajas': ['Efectivo con poca data', 'Flexible (kernels)'],
                'desventajas': ['Escalabilidad limitada', 'Parametros sensibles'],
                'cuando_usar': 'Conjuntos pequeños y relaciones complejas'
            }
        }
        
        for nombre, info in algoritmos.items():
            print(f"\n* {nombre}:")
            print(f"   - Descripcion: {info['descripcion']}")
            print(f"   - Ecuacion: {info['ecuacion']}")
            if 'funcion_costo' in info:
                print(f"   - Funcion Costo: {info['funcion_costo']}")
            if 'optimizacion' in info:
                print(f"   - Optimizacion: {info['optimizacion']}")
            print(f"   - Ventajas: {', '.join(info['ventajas'])}")
            print(f"   - Desventajas: {', '.join(info['desventajas'])}")
            print(f"   - Cuando usar: {info['cuando_usar']}")
    
    def classification_algorithms(self):
        """Explicar algoritmos de clasificación."""
        print("\n\nALGORITMOS DE CLASIFICACION")
        print("-" * 50)
        
        algoritmos = {
            'Logistic Regression': {
                'descripcion': 'Clasificacion mediante funcion logistica',
                'ecuacion': 'p = 1 / (1 + e^(-z))',
                'ventajas': ['Probabilidades', 'Interpretable', 'Rapido'],
                'desventajas': ['Asume linealidad', 'Sensible a correlacion'],
                'cuando_usar': 'Clasificacion binaria con relacion lineal'
            },
            'Random Forest Classifier': {
                'descripcion': 'Conjunto de arboles de decision para clasificar',
                'ecuacion': 'Votacion por mayoria de multiples arboles',
                'ventajas': ['Alta precision', 'Maneja outliers', 'No sobreajusta'],
                'desventajas': ['Menos interpretable', 'Mas lento', 'Memoria alta'],
                'cuando_usar': 'Clasificacion compleja con muchas clases'
            },
            'SVM (Support Vector Machine)': {
                'descripcion': 'Clasificacion usando hiperplanos optimos',
                'ecuacion': 'Maximiza margen entre clases',
                'ventajas': ['Efectivo en espacios de alta dim', 'Usa kernels'],
                'desventajas': ['Solo escalable con datasets pequeños'],
                'cuando_usar': 'Clasificacion con muchas caracteristicas'
            }
        }
        
        for nombre, info in algoritmos.items():
            print(f"\n* {nombre}:")
            print(f"   - Descripcion: {info['descripcion']}")
            print(f"   - Ecuacion: {info['ecuacion']}")
            print(f"   - Ventajas: {', '.join(info['ventajas'])}")
            print(f"   - Desventajas: {', '.join(info['desventajas'])}")
            print(f"   - Cuando usar: {info['cuando_usar']}")
    
    def clustering_algorithms(self):
        """Explicar algoritmos de clustering."""
        print("\n\nALGORITMOS DE CLUSTERING")
        print("-" * 50)
        
        algoritmos = {
            'K-Means': {
                'descripcion': 'Agrupa datos en k clusters por distancia',
                'ecuacion': 'Minimiza suma de distancias al centroide',
                'ventajas': ['Simple', 'Escalable', 'Rapido'],
                'desventajas': ['Requiere k inicial', 'Solo clusters esfericos'],
                'cuando_usar': 'Numero de grupos conocido, clusters esfericos'
            },
            'DBSCAN': {
                'descripcion': 'Clustering por densidad de puntos',
                'ecuacion': 'Agrupa puntos densos, marca puntos ruidosos',
                'ventajas': ['Encuentra k automaticamente', 'Deteccion de outliers'],
                'desventajas': ['Sensible a parametros', 'No funciona con datos mixtos'],
                'cuando_usar': 'Clusters con formas arbitrarias, presencia de ruido'
            },
            'Hierarchical Clustering': {
                'descripcion': 'Construye jerarquia de clusters',
                'ecuacion': 'Dendrograma de similitud',
                'ventajas': ['No requiere k', 'Visualizable'],
                'desventajas': ['Computacionalmente costoso', 'No es robusto a outliers'],
                'cuando_usar': 'Exploracion de estructura jerarquica'
            }
        }
        
        for nombre, info in algoritmos.items():
            print(f"\n* {nombre}:")
            print(f"   - Descripcion: {info['descripcion']}")
            print(f"   - Ecuacion: {info['ecuacion']}")
            print(f"   - Ventajas: {', '.join(info['ventajas'])}")
            print(f"   - Desventajas: {', '.join(info['desventajas'])}")
            print(f"   - Cuando usar: {info['cuando_usar']}")
    
    def comparison_table(self):
        """Crear tabla comparativa de algoritmos."""
        print("\n\nTABLA COMPARATIVA DE ALGORITMOS")
        print("-" * 60)
        
        tabla = pd.DataFrame({
            'Algoritmo': ['Linear Regression', 'Random Forest', 'SVM', 'K-Means'],
            'Tipo': ['Regresion', 'Regresion/Clasificacion', 'Clasificacion', 'Clustering'],
            'Complejidad': ['Baja', 'Media', 'Media', 'Baja'],
            'Interpretabilidad': ['Alta', 'Media', 'Baja', 'Media'],
            'Tiempo Entrenamiento': ['Rapido', 'Medio', 'Medio', 'Rapido']
        })
        
        print(tabla.to_string(index=False))
    
    def selection_tips(self):
        """Dar consejos para seleccionar algoritmos."""
        print("\n\nCONSEJOS PARA SELECCIONAR ALGORITMOS")
        print("-" * 50)
        
        print("""
+------------------+----------------------------------+
| TIPO DATOS       | ALGORITMO RECOMENDADO            |
+------------------+----------------------------------+
| Pequeño dataset  | SVM, Logistic Regression         |
| (< 1000 samples) |                                  |
|                  |                                  |
| Dataset mediano  | Random Forest, Gradient Boosting  |
| (1K-100K samples)|                                  |
|                  |                                  |
| Dataset grande   | Linear/Logistic Regression        |
| (> 100K samples) |                                  |
|                  |                                  |
| Datos lineales   | Linear Regression, Logistic Reg   |
|                  |                                  |
| Datos no lineales| Random Forest, Neural Networks    |
|                  |                                  |
| Muchas features  | Dimensionality Reduction + RF    |
| (> 100)          |                                  |
|                  |                                  |
| Datos categoricos| Random Forest (maneja bien)      |
+------------------+----------------------------------+

RECOMENDACION GENERAL:
1. Empezar con algoritmos simples (Linear/Logistic Reg)
2. Si no funciona, probar Random Forest
3. Si necesitas mejor rendimiento, optimizar hiperparametros
4. Usar validacion cruzada para comparar
        """)
    
    def execute(self):
        """Ejecutar explicacion completa."""
        self.cost_function()
        self.regression_algorithms()
        self.classification_algorithms()
        self.clustering_algorithms()
        self.comparison_table()
        self.selection_tips()
        
        print("\n[OK] Modulo de Algoritmos Basicos completado!")

def main():
    """Función principal del módulo."""
    algoritmos = BasicAlgorithms()
    algoritmos.execute()

if __name__ == "__main__":
    main()
