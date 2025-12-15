#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
<!--
# MACHINE LEARNING FUNDAMENTALS - SPRINT_3
**Autor:** Enith Gicela Vargas Vargas  
**Camada:** 1  
**Grupo:** 11  
**Fecha:** 2025-11-11  
**Curso:** AI Fundamentals - Guayerd - IBM Skills Build  
**Sprint:** 3 - Machine Learning Fundamentals  
**Módulo:** Fundamentos - Conceptos Básicos  
-->

MACHINE LEARNING FUNDAMENTALS - PROYECTO AURELION SPRINT_3
==========================================================

Script para explicar conceptos fundamentales de Machine Learning, incluyendo:
- Definición de ML
- Diferencias con IA tradicional
- Tipos de problemas
- Proceso típico
"""

import pandas as pd          # Librería para manipulación de datos estructurados
import numpy as np           # Librería para cálculos numéricos y matemáticos
import matplotlib.pyplot as plt  # Librería para crear visualizaciones
import seaborn as sns       # Librería para visualizaciones estadísticas
import warnings             # Módulo para controlar avisos del sistema
warnings.filterwarnings('ignore')

class MLFundamentals:
    """
    Clase para explicar conceptos fundamentales de Machine Learning.
    
    Funcionalidades:
    - Definir qué es Machine Learning
    - Diferenciar ML de IA tradicional
    - Clasificar tipos de problemas
    - Mostrar proceso típico de ML
    """
    
    def __init__(self):
        """Inicializar el explicador de fundamentos."""
        print("FUNDAMENTOS DE MACHINE LEARNING")
        print("Grupo 11 - Camada 1 | Enith Gicela Vargas Vargas")
        print("=" * 60)
        
    def define_ml(self):
        """Definir qué es Machine Learning."""
        print("\n¿QUÉ ES MACHINE LEARNING?")
        print("-" * 50)
        print("""
Machine Learning (Aprendizaje Automático) es una subdivisión de la 
Inteligencia Artificial que permite a las computadoras aprender y 
mejorar automáticamente a partir de la experiencia sin ser 
programadas explícitamente.

En lugar de programar reglas específicas, proporcionamos datos y 
permitimos que el algoritmo encuentre patrones por sí mismo.
        """)
        
    def traditional_ai_differences(self):
        """Explicar diferencias entre ML e IA tradicional."""
        print("\nML vs IA TRADICIONAL")
        print("-" * 50)
        print("""
+---------------------+-------------------------+
| IA TRADICIONAL      | MACHINE LEARNING        |
+---------------------+-------------------------+
| Reglas programadas  | Aprende de datos        |
| Logica explicita    | Encuentra patrones      |
| Basada en if-else   | Basada en estadisticas  |
| No mejora sola      | Mejora con mas datos    |
| Ejemplo: Ajedrez    | Ejemplo: Reconocimiento |
|                     |         de imagenes     |
+---------------------+-------------------------+
        """)
        
    def ml_problem_types(self):
        """Explicar tipos de problemas en ML."""
        print("\nTIPOS DE PROBLEMAS EN MACHINE LEARNING")
        print("-" * 50)
        
        tipos = {
            'Regresión': {
                'descripcion': 'Predecir valores continuos',
                'ejemplo': 'Predecir precio de una casa',
                'algoritmos': ['Linear Regression', 'Random Forest', 'SVR'],
                'evaluacion': 'MSE, RMSE, R²'
            },
            'Clasificación': {
                'descripcion': 'Predecir categorías o clases',
                'ejemplo': 'Diagnosticar enfermedad (Sano/Enfermo)',
                'algoritmos': ['Logistic Regression', 'SVM', 'Random Forest'],
                'evaluacion': 'Accuracy, Precision, Recall, F1-Score'
            },
            'Clustering': {
                'descripcion': 'Agrupar datos similares',
                'ejemplo': 'Segmentar clientes por comportamiento',
                'algoritmos': ['K-Means', 'DBSCAN', 'Hierarchical'],
                'evaluacion': 'Silhouette Score, Inertia'
            }
        }
        
        for tipo, info in tipos.items():
            print(f"\n• {tipo}:")
            print(f"   • Descripción: {info['descripcion']}")
            print(f"   • Ejemplo: {info['ejemplo']}")
            print(f"   • Algoritmos: {', '.join(info['algoritmos'])}")
            print(f"   • Evaluación: {info['evaluacion']}")
            
        return tipos
    
    def typical_ml_process(self):
        """Explicar el proceso típico de ML."""
        print("\nPROCESO TÍPICO DE MACHINE LEARNING")
        print("-" * 50)
        
        pasos = [
            ("1. DATOS", "Recopilar y limpiar datos históricos"),
            ("2. PREPARACIÓN", "Normalizar, codificar variables categóricas"),
            ("3. DIVISIÓN", "Train (80%) / Test (20%)"),
            ("4. ENTRENAMIENTO", "Algoritmo aprende del train set"),
            ("5. PREDICCIÓN", "Modelo genera predicciones"),
            ("6. EVALUACIÓN", "Métricas de rendimiento"),
            ("7. DESPLIEGUE", "Poner en producción")
        ]
        
        print("\nPASOS DEL PROCESO:")
        for paso, descripcion in pasos:
            print(f"   {paso}")
            print(f"      -> {descripcion}")
    
    def practical_example(self):
        """Mostrar ejemplo práctico con datos de Aurelion."""
        print("\nEJEMPLO PRÁCTICO CON AURELION")
        print("-" * 50)
        
        print("""
Ejemplo de problema de Regresión:
---------------------------------
Objetivo: Predecir el monto total de ventas para un cliente

Datos disponibles:
   • Historial de compras
   • Método de pago preferido
   • Frecuencia de compras
   • Antigüedad como cliente

Proceso:
   1. Cargar datos históricos de ventas
   2. Preparar: normalizar, codificar
   3. Entrenar modelo de regresión
   4. Evaluar con métricas (R², MSE)
   5. Predecir ventas futuras

Resultado esperado:
   • Modelo que predice monto de venta
   • Precisión del 85-90%
   • Útil para estrategias de marketing
        """)
    
    def show_summary(self):
        """Mostrar resumen de los fundamentos."""
        print("\n" + "=" * 60)
        print("RESUMEN DE FUNDAMENTOS DE ML")
        print("=" * 60)
        
        resumen = """
[OK] Machine Learning permite que las computadoras aprendan de datos

[OK] Tres tipos principales de problemas:
   • Regresion: Valores continuos
   • Clasificacion: Categorias
   • Clustering: Grupos similares

[OK] Proceso tipico:
   Datos → Preparacion → Train/Test → Entrenar → Evaluar

[OK] Ventajas del ML:
   • Automatizacion
   • Escalabilidad
   • Descubrimiento de patrones ocultos
   • Adaptacion continua

[NEXT] Proximos pasos:
   • Tipos de aprendizajes (Supervisado/No supervisado)
   • Algoritmos basicos
   • Metricas de evaluacion
        """
        
        print(resumen)
    
    def execute(self):
        """Ejecutar explicación completa de fundamentos."""
        self.define_ml()
        self.traditional_ai_differences()
        self.ml_problem_types()
        self.typical_ml_process()
        self.practical_example()
        self.show_summary()
        
        print("\n[OK] Modulo de Fundamentos de ML completado!")

def main():
    """Función principal del módulo de fundamentos."""
    fundamentos = MLFundamentals()
    fundamentos.execute()

if __name__ == "__main__":
    main()
