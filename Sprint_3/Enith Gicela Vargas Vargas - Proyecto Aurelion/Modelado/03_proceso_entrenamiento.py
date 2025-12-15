#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
<!--
# PROCESO ENTRENAMIENTO ML - SPRINT_3
**Autor:** Enith Gicela Vargas Vargas  
**Camada:** 1  
**Grupo:** 11  
**Fecha:** 2025-11-11  
**Curso:** AI Fundamentals - Guayerd - IBM Skills Build  
**Sprint:** 3 - Machine Learning Fundamentals  
**Módulo:** Modelado - Proceso de Entrenamiento  
-->

PROCESO DE ENTRENAMIENTO ML - PROYECTO AURELION SPRINT_3
=========================================================

Script para entrenar modelos de Machine Learning, incluyendo:
- Carga de datos de entrenamiento
- Entrenamiento de múltiples modelos
- Evaluación básica
- Guardado de modelos
"""

import pandas as pd          # Librería para manipulación de datos
import numpy as np           # Librería para cálculos numéricos
import matplotlib.pyplot as plt  # Librería para visualizaciones
import seaborn as sns       # Librería para gráficos estadísticos
from sklearn.linear_model import LinearRegression, LogisticRegression  # Modelos lineales
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier  # Random Forest
from sklearn.svm import SVR, SVC  # Support Vector Machines
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, classification_report  # Métricas
import pickle               # Para guardar modelos
import warnings             # Módulo para controlar avisos
warnings.filterwarnings('ignore')

class TrainingProcess:
    """
    Clase para entrenar modelos de Machine Learning.
    
    Funcionalidades:
    - Carga de datos de entrenamiento
    - Entrenamiento de múltiples modelos
    - Evaluación básica
    - Guardado de modelos
    """
    
    def __init__(self):
        """Inicializar el proceso de entrenamiento."""
        print("PROCESO DE ENTRENAMIENTO DE MODELOS ML")
        print("Grupo 11 - Camada 1 | Enith Gicela Vargas Vargas")
        print("=" * 60)
        
    def load_data(self):
        """Cargar datos de entrenamiento y prueba."""
        print("\nCARGANDO DATOS DE ENTRENAMIENTO Y PRUEBA")
        print("-" * 50)
        
        try:
            # Cargar conjuntos de datos
            X_train = pd.read_csv("../resultados/X_train.csv")
            X_test = pd.read_csv("../resultados/X_test.csv")
            y_train = pd.read_csv("../resultados/y_train.csv")
            y_test = pd.read_csv("../resultados/y_test.csv")
            
            # Convertir y a series si es necesario
            if y_train.shape[1] == 1:
                y_train = y_train.iloc[:, 0]
            if y_test.shape[1] == 1:
                y_test = y_test.iloc[:, 0]
            
            print(f"[OK] Datos de entrenamiento: {X_train.shape}")
            print(f"[OK] Datos de prueba: {X_test.shape}")
            print(f"[OK] Target entrenamiento: {y_train.shape}")
            print(f"[OK] Target prueba: {y_test.shape}")
            
            return X_train, X_test, y_train, y_test
            
        except FileNotFoundError as e:
            print(f"[ERROR] Archivos no encontrados: {e}")
            print("Ejecutar primero 02_division_train_test.py")
            return None, None, None, None
        except Exception as e:
            print(f"[ERROR] Error al cargar datos: {e}")
            return None, None, None, None
    
    def determine_problem_type(self, y):
        """Determinar tipo de problema (regresión o clasificación)."""
        print("\nDETERMINANDO TIPO DE PROBLEMA")
        print("-" * 50)
        
        # Verificar si es problema de clasificación
        unique_values = len(np.unique(y))
        is_integer = all(isinstance(val, (int, np.integer)) for val in y if not pd.isna(val))
        
        if unique_values <= 10 and is_integer:
            problem_type = 'classification'
            print(f"[OK] Tipo de problema: CLASIFICACION")
            print(f"[OK] Número de clases: {unique_values}")
            print(f"[OK] Clases: {sorted(np.unique(y))}")
        else:
            problem_type = 'regression'
            print(f"[OK] Tipo de problema: REGRESION")
            print(f"[OK] Valores únicos: {unique_values}")
            print(f"[OK] Rango: {y.min():.2f} - {y.max():.2f}")
        
        return problem_type
    
    def train_model(self, X_train, y_train, X_test, y_test, problem_type):
        """Entrenar modelos según el tipo de problema."""
        print(f"\nENTRENANDO MODELOS - TIPO: {problem_type.upper()}")
        print("-" * 50)
        
        models = {}
        results = {}
        
        if problem_type == 'regression':
            # Modelos de regresión
            models = {
                'Linear Regression': LinearRegression(),
                'Random Forest Regressor': RandomForestRegressor(n_estimators=100, random_state=42),
                'SVR': SVR(kernel='rbf', C=1.0)
            }
            
            print("Modelos de regresión a entrenar:")
            for name in models.keys():
                print(f"  - {name}")
            
            # Entrenar y evaluar modelos
            for name, model in models.items():
                print(f"\nEntrenando {name}...")
                
                # Entrenar modelo
                model.fit(X_train, y_train)
                
                # Predicciones
                y_pred_train = model.predict(X_train)
                y_pred_test = model.predict(X_test)
                
                # Métricas
                train_mse = mean_squared_error(y_train, y_pred_train)
                test_mse = mean_squared_error(y_test, y_pred_test)
                train_r2 = r2_score(y_train, y_pred_train)
                test_r2 = r2_score(y_test, y_pred_test)
                
                results[name] = {
                    'model': model,
                    'train_mse': train_mse,
                    'test_mse': test_mse,
                    'train_r2': train_r2,
                    'test_r2': test_r2,
                    'y_pred_test': y_pred_test
                }
                
                print(f"  [OK] Train MSE: {train_mse:.4f}, R²: {train_r2:.4f}")
                print(f"  [OK] Test MSE: {test_mse:.4f}, R²: {test_r2:.4f}")
        
        else:  # classification
            # Modelos de clasificación
            models = {
                'Logistic Regression': LogisticRegression(random_state=42, max_iter=1000),
                'Random Forest Classifier': RandomForestClassifier(n_estimators=100, random_state=42),
                'SVC': SVC(random_state=42)
            }
            
            print("Modelos de clasificación a entrenar:")
            for name in models.keys():
                print(f"  - {name}")
            
            # Entrenar y evaluar modelos
            for name, model in models.items():
                print(f"\nEntrenando {name}...")
                
                # Entrenar modelo
                model.fit(X_train, y_train)
                
                # Predicciones
                y_pred_train = model.predict(X_train)
                y_pred_test = model.predict(X_test)
                
                # Métricas
                train_acc = accuracy_score(y_train, y_pred_train)
                test_acc = accuracy_score(y_test, y_pred_test)
                
                results[name] = {
                    'model': model,
                    'train_accuracy': train_acc,
                    'test_accuracy': test_acc,
                    'y_pred_test': y_pred_test
                }
                
                print(f"  [OK] Train Accuracy: {train_acc:.4f}")
                print(f"  [OK] Test Accuracy: {test_acc:.4f}")
        
        return results
    
    def compare_models(self, results, problem_type):
        """Comparar rendimiento de modelos."""
        print(f"\nCOMPARACION DE MODELOS")
        print("-" * 50)
        
        if problem_type == 'regression':
            # Crear DataFrame de comparación para regresión
            comparison_data = []
            for name, result in results.items():
                comparison_data.append({
                    'Modelo': name,
                    'Train_R2': result['train_r2'],
                    'Test_R2': result['test_r2'],
                    'Train_MSE': result['train_mse'],
                    'Test_MSE': result['test_mse']
                })
            
            comparison_df = pd.DataFrame(comparison_data)
            comparison_df = comparison_df.sort_values('Test_R2', ascending=False)
            
            print("Ranking por R² Score (Test):")
            print(comparison_df.round(4))
            
            # Mejor modelo
            best_model = comparison_df.iloc[0]['Modelo']
            print(f"\n[OK] Mejor modelo: {best_model}")
            print(f"  - Test R²: {comparison_df.iloc[0]['Test_R2']:.4f}")
            print(f"  - Test MSE: {comparison_df.iloc[0]['Test_MSE']:.4f}")
        
        else:  # classification
            # Crear DataFrame de comparación para clasificación
            comparison_data = []
            for name, result in results.items():
                comparison_data.append({
                    'Modelo': name,
                    'Train_Accuracy': result['train_accuracy'],
                    'Test_Accuracy': result['test_accuracy']
                })
            
            comparison_df = pd.DataFrame(comparison_data)
            comparison_df = comparison_df.sort_values('Test_Accuracy', ascending=False)
            
            print("Ranking por Accuracy (Test):")
            print(comparison_df.round(4))
            
            # Mejor modelo
            best_model = comparison_df.iloc[0]['Modelo']
            print(f"\n[OK] Mejor modelo: {best_model}")
            print(f"  - Test Accuracy: {comparison_df.iloc[0]['Test_Accuracy']:.4f}")
        
        return best_model
    
    def save_models(self, results, best_model):
        """Guardar modelos entrenados."""
        print(f"\nGUARDANDO MODELOS ENTRENADOS")
        print("-" * 50)
        
        # Crear directorio de resultados si no existe
        import os
        os.makedirs("../resultados/modelos", exist_ok=True)
        
        # Guardar todos los modelos
        for name, result in results.items():
            model_path = f"../resultados/modelos/{name.replace(' ', '_').lower()}.pkl"
            with open(model_path, 'wb') as f:
                pickle.dump(result['model'], f)
            print(f"[OK] {name} guardado en {model_path}")
        
        # Guardar mejor modelo por separado
        best_model_path = "../resultados/modelos/mejor_modelo.pkl"
        with open(best_model_path, 'wb') as f:
            pickle.dump(results[best_model]['model'], f)
        
        # Guardar información del mejor modelo
        with open("../resultados/modelos/mejor_modelo_info.txt", 'w') as f:
            f.write(f"Mejor modelo: {best_model}\n")
            f.write(f"Fecha: {pd.Timestamp.now()}\n")
        
        print(f"[OK] Mejor modelo guardado en {best_model_path}")
        print(f"[OK] Información guardada en ../resultados/modelos/mejor_modelo_info.txt")
    
    def execute(self):
        """Ejecutar proceso completo de entrenamiento."""
        # 1. Cargar datos
        X_train, X_test, y_train, y_test = self.load_data()
        
        if X_train is None:
            print("[ERROR] No se pudieron cargar los datos")
            return
        
        # 2. Determinar tipo de problema
        problem_type = self.determine_problem_type(y_train)
        
        # 3. Entrenar modelos
        results = self.train_model(X_train, y_train, X_test, y_test, problem_type)
        
        # 4. Comparar modelos
        best_model = self.compare_models(results, problem_type)
        
        # 5. Guardar modelos
        self.save_models(results, best_model)
        
        print(f"\n[OK] Proceso de entrenamiento completado!")
        print(f"[OK] Mejor modelo: {best_model}")

def main():
    """Función principal del módulo."""
    entrenador = TrainingProcess()
    entrenador.execute()

if __name__ == "__main__":
    main()
