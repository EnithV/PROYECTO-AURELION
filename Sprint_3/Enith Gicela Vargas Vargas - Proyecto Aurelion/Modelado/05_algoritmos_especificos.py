#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
<!--
# ALGORITMOS ESPECIFICOS ML - SPRINT_3
**Autor:** Enith Gicela Vargas Vargas  
**Camada:** 1  
**Grupo:** 11  
**Fecha:** 2025-11-11  
**Curso:** AI Fundamentals - Guayerd - IBM Skills Build  
**Sprint:** 3 - Machine Learning Fundamentals  
**Módulo:** Modelado - Algoritmos Específicos  
-->

ALGORITMOS ESPECIFICOS ML - PROYECTO AURELION SPRINT_3
=======================================================

Script para implementar algoritmos específicos de Machine Learning, incluyendo:
- Random Forest Regressor
- Logistic Regression
- K-Means Clustering
- Comparación de algoritmos
"""

import pandas as pd          # Librería para manipulación de datos
import numpy as np           # Librería para cálculos numéricos
import matplotlib.pyplot as plt  # Librería para visualizaciones
import seaborn as sns       # Librería para gráficos estadísticos
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier  # Random Forest
from sklearn.linear_model import LogisticRegression  # Regresión logística
from sklearn.cluster import KMeans  # K-Means clustering
from sklearn.metrics import (  # Métricas
    mean_squared_error, r2_score, accuracy_score, 
    silhouette_score, classification_report
)
import warnings             # Módulo para controlar avisos
warnings.filterwarnings('ignore')

class SpecificAlgorithms:
    """
    Clase para implementar algoritmos específicos de ML.
    
    Funcionalidades:
    - Random Forest Regressor
    - Logistic Regression
    - K-Means Clustering
    - Comparación de algoritmos
    """
    
    def __init__(self):
        """Inicializar el implementador de algoritmos."""
        print("ALGORITMOS ESPECIFICOS DE MACHINE LEARNING")
        print("Grupo 11 - Camada 1 | Enith Gicela Vargas Vargas")
        print("=" * 60)
        
    def random_forest_regressor(self, X_train, y_train, X_test, y_test):
        """Implementar Random Forest Regressor."""
        print("\nRANDOM FOREST REGRESSOR")
        print("-" * 50)
        
        # Crear modelo con parámetros optimizados
        rf_regressor = RandomForestRegressor(
            n_estimators=100,
            max_depth=10,
            min_samples_split=5,
            min_samples_leaf=2,
            random_state=42
        )
        
        print("Parámetros del modelo:")
        print(f"  - n_estimators: {rf_regressor.n_estimators}")
        print(f"  - max_depth: {rf_regressor.max_depth}")
        print(f"  - min_samples_split: {rf_regressor.min_samples_split}")
        print(f"  - min_samples_leaf: {rf_regressor.min_samples_leaf}")
        
        # Entrenar modelo
        print("\nEntrenando modelo...")
        rf_regressor.fit(X_train, y_train)
        
        # Predicciones
        y_pred_train = rf_regressor.predict(X_train)
        y_pred_test = rf_regressor.predict(X_test)
        
        # Métricas
        train_mse = mean_squared_error(y_train, y_pred_train)
        test_mse = mean_squared_error(y_test, y_pred_test)
        train_r2 = r2_score(y_train, y_pred_train)
        test_r2 = r2_score(y_test, y_pred_test)
        
        print(f"\nResultados:")
        print(f"  ✓ Train MSE: {train_mse:.4f}")
        print(f"  ✓ Test MSE: {test_mse:.4f}")
        print(f"  ✓ Train R²: {train_r2:.4f}")
        print(f"  ✓ Test R²: {test_r2:.4f}")
        
        # Importancia de características
        feature_importance = pd.DataFrame({
            'feature': X_train.columns,
            'importance': rf_regressor.feature_importances_
        }).sort_values('importance', ascending=False)
        
        print(f"\nTop 5 características más importantes:")
        for i, row in feature_importance.head().iterrows():
            print(f"  {row['feature']}: {row['importance']:.4f}")
        
        return {
            'model': rf_regressor,
            'train_mse': train_mse,
            'test_mse': test_mse,
            'train_r2': train_r2,
            'test_r2': test_r2,
            'feature_importance': feature_importance
        }
    
    def logistic_regression_model(self, X_train, y_train, X_test, y_test):
        """Implementar Logistic Regression."""
        print("\nLOGISTIC REGRESSION")
        print("-" * 50)
        
        # Crear modelo con parámetros optimizados
        lr_model = LogisticRegression(
            max_iter=1000,
            random_state=42,
            solver='liblinear'
        )
        
        print("Parámetros del modelo:")
        print(f"  - max_iter: {lr_model.max_iter}")
        print(f"  - solver: {lr_model.solver}")
        print(f"  - random_state: {lr_model.random_state}")
        
        # Entrenar modelo
        print("\nEntrenando modelo...")
        lr_model.fit(X_train, y_train)
        
        # Predicciones
        y_pred_train = lr_model.predict(X_train)
        y_pred_test = lr_model.predict(X_test)
        
        # Métricas
        train_acc = accuracy_score(y_train, y_pred_train)
        test_acc = accuracy_score(y_test, y_pred_test)
        
        print(f"\nResultados:")
        print(f"  ✓ Train Accuracy: {train_acc:.4f}")
        print(f"  ✓ Test Accuracy: {test_acc:.4f}")
        
        # Coeficientes
        if hasattr(lr_model, 'coef_'):
            coefficients = pd.DataFrame({
                'feature': X_train.columns,
                'coefficient': lr_model.coef_[0]
            }).sort_values('coefficient', key=abs, ascending=False)
            
            print(f"\nTop 5 coeficientes más importantes:")
            for i, row in coefficients.head().iterrows():
                print(f"  {row['feature']}: {row['coefficient']:.4f}")
        
        return {
            'model': lr_model,
            'train_accuracy': train_acc,
            'test_accuracy': test_acc,
            'coefficients': coefficients if 'coefficients' in locals() else None
        }
    
    def kmeans_clustering_model(self, X):
        """Implementar K-Means Clustering."""
        print("\nK-MEANS CLUSTERING")
        print("-" * 50)
        
        # Determinar número óptimo de clusters usando Elbow Method
        print("Determinando número óptimo de clusters...")
        
        inertias = []
        silhouette_scores = []
        K_range = range(2, 11)
        
        for k in K_range:
            kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
            kmeans.fit(X)
            inertias.append(kmeans.inertia_)
            silhouette_scores.append(silhouette_score(X, kmeans.labels_))
        
        # Encontrar k óptimo (mayor silhouette score)
        optimal_k = K_range[np.argmax(silhouette_scores)]
        
        print(f"✓ Número óptimo de clusters: {optimal_k}")
        print(f"✓ Silhouette Score: {max(silhouette_scores):.4f}")
        
        # Entrenar modelo final
        print(f"\nEntrenando K-Means con {optimal_k} clusters...")
        kmeans_final = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
        kmeans_final.fit(X)
        
        # Predicciones
        cluster_labels = kmeans_final.predict(X)
        
        # Métricas
        inertia = kmeans_final.inertia_
        silhouette = silhouette_score(X, cluster_labels)
        
        print(f"\nResultados:")
        print(f"  ✓ Inertia: {inertia:.4f}")
        print(f"  ✓ Silhouette Score: {silhouette:.4f}")
        print(f"  ✓ Número de clusters: {optimal_k}")
        
        # Distribución de clusters
        cluster_counts = pd.Series(cluster_labels).value_counts().sort_index()
        print(f"\nDistribución de clusters:")
        for cluster, count in cluster_counts.items():
            print(f"  Cluster {cluster}: {count} muestras ({count/len(X)*100:.1f}%)")
        
        return {
            'model': kmeans_final,
            'optimal_k': optimal_k,
            'inertia': inertia,
            'silhouette_score': silhouette,
            'cluster_labels': cluster_labels,
            'cluster_counts': cluster_counts,
            'inertias': inertias,
            'silhouette_scores': silhouette_scores
        }
    
    def compare_algorithms(self, results):
        """Comparar diferentes algoritmos."""
        print("\nCOMPARACION DE ALGORITMOS")
        print("-" * 50)
        
        comparison_data = []
        
        # Agregar resultados de Random Forest si existe
        if 'random_forest' in results:
            rf_result = results['random_forest']
            comparison_data.append({
                'Algoritmo': 'Random Forest Regressor',
                'Tipo': 'Regresión',
                'Métrica_Principal': f"R² = {rf_result['test_r2']:.4f}",
                'MSE': rf_result['test_mse'],
                'R2': rf_result['test_r2']
            })
        
        # Agregar resultados de Logistic Regression si existe
        if 'logistic_regression' in results:
            lr_result = results['logistic_regression']
            comparison_data.append({
                'Algoritmo': 'Logistic Regression',
                'Tipo': 'Clasificación',
                'Métrica_Principal': f"Accuracy = {lr_result['test_accuracy']:.4f}",
                'Accuracy': lr_result['test_accuracy'],
                'R2': None
            })
        
        # Agregar resultados de K-Means si existe
        if 'kmeans' in results:
            km_result = results['kmeans']
            comparison_data.append({
                'Algoritmo': 'K-Means Clustering',
                'Tipo': 'Clustering',
                'Métrica_Principal': f"Silhouette = {km_result['silhouette_score']:.4f}",
                'Silhouette': km_result['silhouette_score'],
                'Clusters': km_result['optimal_k']
            })
        
        if comparison_data:
            comparison_df = pd.DataFrame(comparison_data)
            print(comparison_df.to_string(index=False))
            
            # Recomendaciones
            print(f"\nRECOMENDACIONES:")
            print("-" * 20)
            
            for _, row in comparison_df.iterrows():
                algoritmo = row['Algoritmo']
                tipo = row['Tipo']
                
                if tipo == 'Regresión':
                    r2 = row['R2']
                    if r2 > 0.8:
                        print(f"✓ {algoritmo}: Excelente para predicciones")
                    elif r2 > 0.6:
                        print(f"✓ {algoritmo}: Bueno para predicciones")
                    else:
                        print(f"⚠ {algoritmo}: Considerar mejoras")
                
                elif tipo == 'Clasificación':
                    acc = row['Accuracy']
                    if acc > 0.9:
                        print(f"✓ {algoritmo}: Excelente para clasificación")
                    elif acc > 0.8:
                        print(f"✓ {algoritmo}: Bueno para clasificación")
                    else:
                        print(f"⚠ {algoritmo}: Considerar mejoras")
                
                elif tipo == 'Clustering':
                    sil = row['Silhouette']
                    if sil > 0.5:
                        print(f"✓ {algoritmo}: Clusters bien definidos")
                    elif sil > 0.3:
                        print(f"✓ {algoritmo}: Clusters razonables")
                    else:
                        print(f"⚠ {algoritmo}: Clusters poco definidos")
        
        return comparison_df if comparison_data else None
    
    def execute(self):
        """Ejecutar implementación de algoritmos específicos."""
        print("\nCARGANDO DATOS PARA ALGORITMOS ESPECIFICOS")
        print("-" * 50)
        
        try:
            # Cargar datos
            X_train = pd.read_csv("../resultados/X_train.csv")
            X_test = pd.read_csv("../resultados/X_test.csv")
            y_train = pd.read_csv("../resultados/y_train.csv")
            y_test = pd.read_csv("../resultados/y_test.csv")
            
            # Convertir y a series si es necesario
            if y_train.shape[1] == 1:
                y_train = y_train.iloc[:, 0]
            if y_test.shape[1] == 1:
                y_test = y_test.iloc[:, 0]
            
            print(f"✓ Datos cargados: Train {X_train.shape}, Test {X_test.shape}")
            
        except FileNotFoundError:
            print("[ERROR] Archivos de datos no encontrados")
            print("Ejecutar primero los módulos de preparación y división")
            return
        
        # Determinar tipo de problema
        unique_values = len(np.unique(y_train))
        problem_type = 'classification' if unique_values <= 10 else 'regression'
        
        print(f"✓ Tipo de problema detectado: {problem_type.upper()}")
        
        results = {}
        
        # Ejecutar algoritmos según el tipo de problema
        if problem_type == 'regression':
            print(f"\nEJECUTANDO ALGORITMOS DE REGRESION")
            print("-" * 50)
            
            # Random Forest Regressor
            rf_result = self.random_forest_regressor(X_train, y_train, X_test, y_test)
            results['random_forest'] = rf_result
            
        else:  # classification
            print(f"\nEJECUTANDO ALGORITMOS DE CLASIFICACION")
            print("-" * 50)
            
            # Logistic Regression
            lr_result = self.logistic_regression_model(X_train, y_train, X_test, y_test)
            results['logistic_regression'] = lr_result
        
        # K-Means Clustering (siempre se ejecuta)
        print(f"\nEJECUTANDO ALGORITMOS DE CLUSTERING")
        print("-" * 50)
        
        km_result = self.kmeans_clustering_model(X_train)
        results['kmeans'] = km_result
        
        # Comparar algoritmos
        comparison_df = self.compare_algorithms(results)
        
        print(f"\n[OK] Implementación de algoritmos específicos completada!")

def main():
    """Función principal del módulo."""
    algoritmos = SpecificAlgorithms()
    algoritmos.execute()

if __name__ == "__main__":
    main()
