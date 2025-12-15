#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
<!--
# TIPOS DE APRENDIZAJES - SPRINT_3
**Autor:** Enith Gicela Vargas Vargas  
**Camada:** 1  
**Grupo:** 11  
**Fecha:** 2025-11-11  
**Curso:** AI Fundamentals - Guayerd - IBM Skills Build  
**Sprint:** 3 - Machine Learning Fundamentals  
**Módulo:** Fundamentos - Tipos de Aprendizajes  
-->

TIPOS DE APRENDIZAJES EN ML - PROYECTO AURELION SPRINT_3
========================================================

Script para explicar los diferentes tipos de aprendizajes en Machine Learning:
- Aprendizaje Supervisado
- Aprendizaje No Supervisado
- Aprendizaje por Refuerzo
- Comparaciones y ejemplos
"""

import pandas as pd          # Librería para manipulación de datos
import numpy as np           # Librería para cálculos numéricos
import matplotlib.pyplot as plt  # Librería para visualizaciones
import seaborn as sns       # Librería para gráficos estadísticos
import warnings             # Módulo para controlar avisos
warnings.filterwarnings('ignore')

class LearningTypes:
    """
    Clase para explicar tipos de aprendizajes en Machine Learning.
    
    Funcionalidades:
    - Aprendizaje Supervisado
    - Aprendizaje No Supervisado
    - Aprendizaje por Refuerzo
    - Comparaciones y ejemplos
    """
    
    def __init__(self):
        """Inicializar el explicador de tipos de aprendizajes."""
        print("TIPOS DE APRENDIZAJES EN MACHINE LEARNING")
        print("Grupo 11 - Camada 1 | Enith Gicela Vargas Vargas")
        print("=" * 60)
        
    def supervised_learning(self):
        """Explicar aprendizaje supervisado."""
        print("\nAPRENDIZAJE SUPERVISADO")
        print("-" * 50)
        
        print("""
DEFINICIÓN:
El algoritmo aprende a partir de ejemplos etiquetados (input-output).
El modelo se entrena con pares (X, y) donde sabemos la respuesta correcta.

CARACTERISTICAS:
- Datos etiquetados disponibles
- Objetivo claro (funcion objetivo)
- Ejemplos de entrenamiento
- Generalizacion a datos nuevos

CASOS DE USO:
• Prediccion de ventas (Regresion)
• Clasificacion de emails (Spam/No Spam)
• Diagnostico medico
• Reconocimiento de imagenes

EJEMPLO CON AURELION:
   Input: Caracteristicas del cliente
   Output: Monto de venta predicho
   Algoritmo: Random Forest Regressor

ALGORITMOS PRINCIPALES:
• Regresion: Linear Regression, Random Forest, SVR
• Clasificacion: Logistic Regression, SVM, Random Forest
        """)
        
        # Ejemplo visual simple
        self._visualize_supervised()
        
    def _visualize_supervised(self):
        """Crear visualización de aprendizaje supervisado."""
        print("\nEJEMPLO VISUAL: Aprendizaje Supervisado")
        print("-" * 50)
        
        # Datos de ejemplo
        np.random.seed(42)
        X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # Input (features)
        y = np.array([2, 4, 5, 8, 9, 10, 13, 15, 17, 20])  # Output (etiquetas)
        
        # Regresión simple
        from sklearn.linear_model import LinearRegression
        
        model = LinearRegression()
        X_reshaped = X.reshape(-1, 1)
        model.fit(X_reshaped, y)
        
        print(f"   Entrenamiento: {len(X)} ejemplos con etiquetas")
        print(f"   Ecuación: y = {model.coef_[0]:.2f}x + {model.intercept_:.2f}")
        print(f"   R² Score: {model.score(X_reshaped, y):.3f}")
        
    def unsupervised_learning(self):
        """Explicar aprendizaje no supervisado."""
        print("\n\nAPRENDIZAJE NO SUPERVISADO")
        print("-" * 50)
        
        print("""
DEFINICIÓN:
El algoritmo encuentra patrones en datos sin etiquetas.
No hay salida esperada, solo estructura en los datos.

CARACTERÍSTICAS:
✓ Sin datos etiquetados
✓ Descubrimiento de patrones
✓ Agrupación de datos similares
✓ Reducción de dimensionalidad

CASOS DE USO:
• Segmentación de clientes (Clustering)
• Detección de anomalías
• Reducción de dimensionalidad (PCA)
• Análisis exploratorio

EJEMPLO CON AURELION:
   Input: Características de clientes
   Output: Grupos de clientes similares
   Algoritmo: K-Means Clustering

ALGORITMOS PRINCIPALES:
• Clustering: K-Means, DBSCAN, Hierarchical
• Reducción: PCA, t-SNE
• Asociación: Apriori, FP-Growth
        """)
        
        # Ejemplo visual simple
        self._visualize_unsupervised()
        
    def _visualize_unsupervised(self):
        """Crear visualización de aprendizaje no supervisado."""
        print("\nEJEMPLO VISUAL: Aprendizaje No Supervisado")
        print("-" * 50)
        
        # Datos de ejemplo para clustering
        np.random.seed(42)
        from sklearn.cluster import KMeans
        
        # Generar datos sintéticos
        X = np.random.randn(100, 2)
        
        # Aplicar K-Means
        kmeans = KMeans(n_clusters=3, random_state=42)
        clusters = kmeans.fit_predict(X)
        
        print(f"   Datos: {len(X)} puntos sin etiquetas")
        print(f"   Clusters encontrados: {len(np.unique(clusters))} grupos")
        print(f"   Centroides: {len(kmeans.cluster_centers_)}")
        
    def reinforcement_learning(self):
        """Explicar aprendizaje por refuerzo."""
        print("\n\nAPRENDIZAJE POR REFUERZO")
        print("-" * 50)
        
        print("""
DEFINICIÓN:
El agente aprende a través de prueba y error, recibiendo 
recompensas o castigos por sus acciones.

CARACTERÍSTICAS:
✓ Interacción con el entorno
✓ Sistema de recompensas
✓ Aprendizaje por prueba y error
✓ Optimización de política

CASOS DE USO:
• Juegos (Chess, Go, Videojuegos)
• Robots autónomos
• Sistemas de recomendación
• Trading algorítmico

EJEMPLO TEÓRICO:
   Agente: Robot de limpieza
   Acciones: Moverse, Limpiar, Descansar
   Recompensa: +10 por área limpia, -1 por batería usada
   Objetivo: Maximizar recompensa total

NOTE: Más avanzado, menos común en proyectos básicos
        """)
        
    def compare_types(self):
        """Comparar los tres tipos de aprendizajes."""
        print("\nCOMPARACIÓN DE TIPOS DE APRENDIZAJES")
        print("=" * 60)
        
        comparacion = {
            'Característica': [
                'Datos etiquetados',
                'Supervisión',
                'Objetivo',
                'Ejemplos'
            ],
            'Supervisado': [
                '✅ Sí',
                'Humano',
                'Predecir función',
                'Regresión/Clasificación'
            ],
            'No Supervisado': [
                '❌ No',
                'Ninguna',
                'Encontrar patrones',
                'Clustering'
            ],
            'Refuerzo': [
                '⚠️ Parcial',
                'Entorno',
                'Maximizar recompensa',
                'Gaming/Robots'
            ]
        }
        
        df = pd.DataFrame(comparacion)
        print(df.to_string(index=False))
        
    def when_to_use_each(self):
        """Explicar cuándo usar cada tipo."""
        print("\n\n¿CUÁNDO USAR CADA UNO?")
        print("-" * 50)
        
        print("""
┌─────────────────────┬──────────────────────────────┐
│ USO                 │ SITUACIÓN                    │
├─────────────────────┼──────────────────────────────┤
│ SUPERVISADO         │                              │
│ • Tienes ejemplos   │ • Historial con resultados   │
│ • Objetivo claro    │ • Quieres predecir algo      │
│ • Datos suficientes │ • Tienes muchas muestras     │
│                     │                              │
│ NO SUPERVISADO      │                              │
│ • Sin etiquetas     │ • Datos nuevos sin historia  │
│ • Explorar datos    │ • Buscar grupos naturales     │
│ • Agrupar similar   │ • Segmentar clientes          │
│                     │                              │
│ REFUERZO            │                              │
│ • Decisiones seq.   │ • Juegos, robots             │
│ • Maximizar recomp. │ • Trading, optimización      │
│ • Interactivo       │ • Sistemas autónomos         │
└─────────────────────┴──────────────────────────────┘
        """)
    
    def aurelion_examples(self):
        """Mostrar ejemplos específicos para Aurelion."""
        print("\n\nEJEMPLOS ESPECÍFICOS PARA AURELION")
        print("-" * 50)
        
        ejemplos = {
            'Supervisado - Regresión': {
                'problema': 'Predecir monto de venta',
                'entrada': 'Historial cliente, productos comprados',
                'salida': 'Monto total predicho',
                'algoritmo': 'Random Forest Regressor'
            },
            'Supervisado - Clasificación': {
                'problema': 'Clasificar clientes VIP',
                'entrada': 'Frecuencia compras, monto gastado',
                'salida': 'VIP / Regular / Nuevo',
                'algoritmo': 'Logistic Regression'
            },
            'No Supervisado - Clustering': {
                'problema': 'Segmentar productos similares',
                'entrada': 'Categoría, precio, stock',
                'salida': 'Grupos de productos',
                'algoritmo': 'K-Means'
            }
        }
        
        for tipo, info in ejemplos.items():
            print(f"\n• {tipo.upper()}:")
            print(f"   • Problema: {info['problema']}")
            print(f"   • Entrada: {info['entrada']}")
            print(f"   • Salida: {info['salida']}")
            print(f"   • Algoritmo: {info['algoritmo']}")
    
    def execute(self):
        """Ejecutar explicación completa."""
        self.supervised_learning()
        self.unsupervised_learning()
        self.reinforcement_learning()
        self.compare_types()
        self.when_to_use_each()
        self.aurelion_examples()
        
        print("\n[OK] Modulo de Tipos de Aprendizajes completado!")

def main():
    """Función principal del módulo."""
    tipos = LearningTypes()
    tipos.execute()

if __name__ == "__main__":
    main()
