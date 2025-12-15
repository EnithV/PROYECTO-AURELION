#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
<!--
# METRICAS EVALUACION ML - SPRINT_3
**Autor:** Enith Gicela Vargas Vargas  
**Camada:** 1  
**Grupo:** 11  
**Fecha:** 2025-11-11  
**Curso:** AI Fundamentals - Guayerd - IBM Skills Build  
**Sprint:** 3 - Machine Learning Fundamentals  
**Módulo:** Fundamentos - Métricas de Evaluación  
-->

METRICAS DE EVALUACION EN ML - PROYECTO AURELION SPRINT_3
=========================================================

Script para explicar las métricas de evaluación en Machine Learning:
- Métricas para Regresión
- Métricas para Clasificación
- Métricas para Clustering
- Interpretación de resultados
"""

import pandas as pd          # Librería para manipulación de datos
import numpy as np           # Librería para cálculos numéricos
import matplotlib.pyplot as plt  # Librería para visualizaciones
import seaborn as sns       # Librería para gráficos estadísticos
import warnings             # Módulo para controlar avisos
warnings.filterwarnings('ignore')

class EvaluationMetrics:
    """
    Clase para explicar métricas de evaluación en ML.
    
    Funcionalidades:
    - Métricas de Regresión
    - Métricas de Clasificación
    - Métricas de Clustering
    - Interpretación de resultados
    """
    
    def __init__(self):
        """Inicializar el explicador de métricas."""
        print("METRICAS DE EVALUACION EN MACHINE LEARNING")
        print("Grupo 11 - Camada 1 | Enith Gicela Vargas Vargas")
        print("=" * 60)
        
    def regression_metrics(self):
        """Explicar métricas de regresión."""
        print("\nMETRICAS PARA REGRESION")
        print("-" * 50)
        
        metricas = {
            'MSE (Mean Squared Error)': {
                'formula': 'MSE = sum(y_true - y_pred)^2 / n',
                'rango': '[0, inf]',
                'mejor_valor': 'Menor es mejor',
                'interpretacion': 'Promedio del error cuadratico',
                'ejemplo': 'MSE = 100 -> error promedio de ±10 unidades'
            },
            'RMSE (Root Mean Squared Error)': {
                'formula': 'RMSE = sqrt(MSE)',
                'rango': '[0, inf]',
                'mejor_valor': 'Menor es mejor',
                'interpretacion': 'Error en unidades originales',
                'ejemplo': 'RMSE = 5.2 -> error promedio de ±5.2 unidades'
            },
            'MAE (Mean Absolute Error)': {
                'formula': 'MAE = sum|y_true - y_pred| / n',
                'rango': '[0, inf]',
                'mejor_valor': 'Menor es mejor',
                'interpretacion': 'Error absoluto promedio',
                'ejemplo': 'MAE = 4 -> error promedio de 4 unidades'
            },
            'R² (R-squared)': {
                'formula': 'R² = 1 - (SS_res / SS_tot)',
                'rango': '[-inf, 1]',
                'mejor_valor': 'Cerca de 1 es mejor',
                'interpretacion': 'Proporcion de varianza explicada',
                'ejemplo': 'R² = 0.85 -> modelo explica 85% de varianza'
            }
        }
        
        for nombre, info in metricas.items():
            print(f"\n* {nombre}:")
            print(f"   - Formula: {info['formula']}")
            print(f"   - Rango: {info['rango']}")
            print(f"   - Mejor valor: {info['mejor_valor']}")
            print(f"   - Interpretacion: {info['interpretacion']}")
            print(f"   - Ejemplo: {info['ejemplo']}")
    
    def classification_metrics(self):
        """Explicar métricas de clasificación."""
        print("\n\nMETRICAS PARA CLASIFICACION")
        print("-" * 50)
        
        metricas = {
            'Accuracy (Precision)': {
                'formula': 'Accuracy = (TP + TN) / (TP + TN + FP + FN)',
                'rango': '[0, 1]',
                'mejor_valor': 'Cerca de 1 es mejor',
                'interpretacion': 'Porcentaje de predicciones correctas',
                'ejemplo': 'Accuracy = 0.92 -> 92% de aciertos'
            },
            'Precision': {
                'formula': 'Precision = TP / (TP + FP)',
                'rango': '[0, 1]',
                'mejor_valor': 'Cerca de 1 es mejor',
                'interpretacion': 'Precision en predicciones positivas',
                'ejemplo': 'Precision = 0.90 -> 90% de positivos son correctos'
            },
            'Recall (Sensibilidad)': {
                'formula': 'Recall = TP / (TP + FN)',
                'rango': '[0, 1]',
                'mejor_valor': 'Cerca de 1 es mejor',
                'interpretacion': 'Proporcion de positivos reales detectados',
                'ejemplo': 'Recall = 0.85 -> detecta 85% de todos los positivos'
            },
            'F1-Score': {
                'formula': 'F1 = 2 × (Precision × Recall) / (Precision + Recall)',
                'rango': '[0, 1]',
                'mejor_valor': 'Cerca de 1 es mejor',
                'interpretacion': 'Balance entre Precision y Recall',
                'ejemplo': 'F1 = 0.88 -> buen balance entre precision y recall'
            }
        }
        
        for nombre, info in metricas.items():
            print(f"\n* {nombre}:")
            print(f"   - Formula: {info['formula']}")
            print(f"   - Rango: {info['rango']}")
            print(f"   - Mejor valor: {info['mejor_valor']}")
            print(f"   - Interpretacion: {info['interpretacion']}")
            print(f"   - Ejemplo: {info['ejemplo']}")
        
        # Explicar matriz de confusión
        print("\nMATRIZ DE CONFUSION:")
        print("""
                Prediccion
            +-------------+---------+
            | Positivo    | Negativo|
     +------+-------------+---------+
     |Posit.|   TP        |   FN    |
     |Real  |   (OK)      |   (NO)  |
     +------+-------------+---------+
     |Negat.|   FP        |   TN    |
     |Real  |   (NO)      |   (OK)  |
     +------+-------------+---------+
     
     TP = True Positives  (Verdadero Positivo)
     TN = True Negatives  (Verdadero Negativo)
     FP = False Positives (Falso Positivo)
     FN = False Negatives (Falso Negativo)
        """)
    
    def clustering_metrics(self):
        """Explicar métricas de clustering."""
        print("\n\nMETRICAS PARA CLUSTERING")
        print("-" * 50)
        
        metricas = {
            'Silhouette Score': {
                'formula': 's(i) = (b(i) - a(i)) / max(a(i), b(i))',
                'rango': '[-1, 1]',
                'mejor_valor': 'Cerca de 1 es mejor',
                'interpretacion': 'Cohesion intra-cluster vs separacion',
                'ejemplo': 'Score = 0.7 -> clusters bien definidos'
            },
            'Inertia (Elbow Method)': {
                'formula': 'Suma de distancias a centroides',
                'rango': '[0, inf]',
                'mejor_valor': 'Buscar "codo" en grafico',
                'interpretacion': 'Menor cuando k optimo',
                'ejemplo': 'k=3 tiene menor reduccion de inertia'
            },
            'Davies-Bouldin Index': {
                'formula': 'DB = (1/n) sum max((sigma_i+sigma_j)/d(c_i,c_j))',
                'rango': '[0, inf]',
                'mejor_valor': 'Menor es mejor',
                'interpretacion': 'Ratio de tamaño y separacion',
                'ejemplo': 'DB = 0.5 -> clusters bien separados'
            }
        }
        
        for nombre, info in metricas.items():
            print(f"\n* {nombre}:")
            print(f"   - Formula: {info['formula']}")
            print(f"   - Rango: {info['rango']}")
            print(f"   - Mejor valor: {info['mejor_valor']}")
            print(f"   - Interpretacion: {info['interpretacion']}")
            print(f"   - Ejemplo: {info['ejemplo']}")
    
    def interpret_results(self):
        """Explicar cómo interpretar resultados de métricas."""
        print("\n\nINTERPRETACION DE RESULTADOS")
        print("-" * 50)
        
        print("""
INTERPRETACION GENERAL:

REGRESION:
   • R² > 0.7  -> Modelo bueno
   • R² 0.4-0.7 -> Modelo aceptable
   • R² < 0.4  -> Modelo pobre, considerar mejoras

   • RMSE bajo -> Predicciones precisas
   • RMSE alto -> Predicciones imprecisas

CLASIFICACION:
   • Accuracy > 0.9 -> Excelente
   • Accuracy 0.7-0.9 -> Bueno
   • Accuracy < 0.7 -> Mejorar modelo

   • Precision importante -> Evitar falsos positivos
   • Recall importante -> No perder casos reales
   • F1-Score -> Balance general

CLUSTERING:
   • Silhouette > 0.5 -> Clusters razonables
   • Silhouette > 0.7 -> Clusters fuertes
   • Silhouette < 0.2 -> Clusters debiles
        """)
    
    def quick_reference_table(self):
        """Crear tabla de referencia rápida."""
        print("\nTABLA DE REFERENCIA RAPIDA")
        print("-" * 50)
        
        tabla = pd.DataFrame({
            'Metrica': ['MSE', 'RMSE', 'R²', 'Accuracy', 'Precision', 'Recall', 'F1-Score', 'Silhouette'],
            'Rango': ['[0, inf]', '[0, inf]', '[-inf, 1]', '[0, 1]', '[0, 1]', '[0, 1]', '[0, 1]', '[-1, 1]'],
            'Mejor': ['Menor', 'Menor', 'Mayor', 'Mayor', 'Mayor', 'Mayor', 'Mayor', 'Mayor'],
            'Uso': ['Regresion', 'Regresion', 'Regresion', 'Clasificacion', 'Clasificacion', 'Clasificacion', 'Clasificacion', 'Clustering']
        })
        
        print(tabla.to_string(index=False))
    
    def execute(self):
        """Ejecutar explicacion completa."""
        self.regression_metrics()
        self.classification_metrics()
        self.clustering_metrics()
        self.interpret_results()
        self.quick_reference_table()
        
        print("\n[OK] Modulo de Metricas de Evaluacion completado!")

def main():
    """Función principal del módulo."""
    metricas = EvaluationMetrics()
    metricas.execute()

if __name__ == "__main__":
    main()
