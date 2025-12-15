#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
<!--
# DIVISION TRAIN TEST - SPRINT_3
**Autor:** Enith Gicela Vargas Vargas  
**Camada:** 1  
**Grupo:** 11  
**Fecha:** 2025-11-11  
**Curso:** AI Fundamentals - Guayerd - IBM Skills Build  
**Sprint:** 3 - Machine Learning Fundamentals  
**Módulo:** Modelado - División Train/Test  
-->

DIVISION TRAIN/TEST PARA ML - PROYECTO AURELION SPRINT_3
=========================================================

Script para dividir datos en conjuntos de entrenamiento y prueba, incluyendo:
- Carga de datos preparados
- División train/test
- Validación cruzada
- Guardado de conjuntos
"""

import pandas as pd          # Librería para manipulación de datos
import numpy as np           # Librería para cálculos numéricos
import matplotlib.pyplot as plt  # Librería para visualizaciones
import seaborn as sns       # Librería para gráficos estadísticos
from sklearn.model_selection import train_test_split, cross_val_score  # División y validación cruzada
from sklearn.linear_model import LinearRegression  # Modelo para validación cruzada
from sklearn.preprocessing import StandardScaler  # Normalización de datos
from sklearn.pipeline import Pipeline  # Pipeline para combinar transformaciones
import warnings             # Módulo para controlar avisos
warnings.filterwarnings('ignore')

class TrainTestSplit:
    """
    Clase para dividir datos en conjuntos de entrenamiento y prueba.
    
    Funcionalidades:
    - Carga de datos preparados
    - División train/test
    - Validación cruzada
    - Guardado de conjuntos
    """
    
    def __init__(self):
        """Inicializar el divisor de datos."""
        print("DIVISION TRAIN/TEST PARA MACHINE LEARNING")
        print("Grupo 11 - Camada 1 | Enith Gicela Vargas Vargas")
        print("=" * 60)
        
    def load_prepared_dataset(self):
        """Cargar dataset preparado."""
        print("\nCARGANDO DATASET PREPARADO")
        print("-" * 50)
        
        try:
            # Cargar características y target
            X = pd.read_csv("../resultados/dataset_ml_preparado.csv")
            y = pd.read_csv("../resultados/target_ml.csv")
            
            # Si y tiene múltiples columnas, tomar la primera
            if y.shape[1] > 1:
                y = y.iloc[:, 0]
            else:
                y = y.iloc[:, 0]
            
            print(f"[OK] Características cargadas: {X.shape}")
            print(f"[OK] Target cargado: {y.shape}")
            print(f"[OK] Columnas de características: {list(X.columns)}")
            
            return X, y
            
        except FileNotFoundError:
            print("[ERROR] Archivos de datos preparados no encontrados")
            print("Ejecutar primero 01_preparacion_datos.py")
            return None, None
        except Exception as e:
            print(f"[ERROR] Error al cargar datos: {e}")
            return None, None
    
    def prepare_features_target(self, X, y):
        """Preparar características y target."""
        print("\nPREPARANDO FEATURES Y TARGET")
        print("-" * 50)
        
        # Verificar que no hay valores faltantes
        if X.isnull().sum().sum() > 0:
            print("Tratando valores faltantes...")
            X = X.fillna(X.mean())
        
        if y.isnull().sum() > 0:
            print("Tratando valores faltantes en target...")
            y = y.fillna(y.mean())
        
        # Verificar tipos de datos
        print(f"[OK] Features shape: {X.shape}")
        print(f"[OK] Target shape: {y.shape}")
        print(f"[OK] Tipos de datos en features: {X.dtypes.value_counts().to_dict()}")
        
        return X, y
    
    def split_train_test(self, X, y, test_size=0.2, random_state=42, normalize=True):
        """
        Dividir datos en conjuntos de entrenamiento y prueba.
        
        IMPORTANTE: Normaliza DESPUÉS de dividir para evitar data leakage.
        Usa fit_transform en training y transform en test.
        """
        print(f"\nDIVISION TRAIN/TEST")
        print("-" * 50)
        
        # IMPORTANTE: Dividir PRIMERO en entrenamiento y prueba
        # División estratificada si es posible (para clasificación)
        stratify = None
        if len(np.unique(y)) <= 10:  # Si hay pocas clases únicas
            stratify = y
        
        X_train_raw, X_test_raw, y_train, y_test = train_test_split(
            X, y, 
            test_size=test_size, 
            random_state=random_state,
            stratify=stratify
        )
        
        # IMPORTANTE: Normalizar DESPUÉS de dividir (evita data leakage)
        if normalize:
            print(f"\nNORMALIZACION DESPUES DE DIVISION (evita data leakage)")
            print("-" * 50)
            scaler = StandardScaler()
            X_train = scaler.fit_transform(X_train_raw)  # Aprende SOLO de training
            X_test = scaler.transform(X_test_raw)         # Aplica parámetros de training
            
            # Convertir a DataFrame para mantener nombres de columnas
            X_train = pd.DataFrame(X_train, columns=X.columns, index=X_train_raw.index)
            X_test = pd.DataFrame(X_test, columns=X.columns, index=X_test_raw.index)
            
            # Guardar scaler para uso posterior
            self.scaler = scaler
            print(f"  ✅ fit_transform aplicado en training")
            print(f"  ✅ transform aplicado en test")
        else:
            # Si no se normaliza, usar datos originales
            X_train = X_train_raw
            X_test = X_test_raw
            self.scaler = None
        
        print(f"\n[OK] División realizada:")
        print(f"  - Train: {X_train.shape[0]} muestras ({X_train.shape[0]/len(X)*100:.1f}%)")
        print(f"  - Test: {X_test.shape[0]} muestras ({X_test.shape[0]/len(X)*100:.1f}%)")
        print(f"  - Features: {X_train.shape[1]} columnas")
        
        # Mostrar estadísticas básicas
        print(f"\nEstadísticas del target:")
        print(f"  - Train mean: {y_train.mean():.2f}")
        print(f"  - Test mean: {y_test.mean():.2f}")
        print(f"  - Train std: {y_train.std():.2f}")
        print(f"  - Test std: {y_test.std():.2f}")
        
        return X_train, X_test, y_train, y_test
    
    def cross_validation_example(self, X, y, modelo, cv=5):
        """
        Ejemplo de validación cruzada.
        
        IMPORTANTE: Usa Pipeline para normalizar dentro de cada fold,
        evitando data leakage en validación cruzada.
        """
        print(f"\nVALIDACION CRUZADA - {cv} FOLDS")
        print("-" * 50)
        
        try:
            # IMPORTANTE: Usar Pipeline para normalizar dentro de cada fold
            # Esto asegura que cada fold normalice solo con sus datos de training
            pipeline = Pipeline([
                ('scaler', StandardScaler()),
                ('model', modelo)
            ])
            
            # Realizar validación cruzada con pipeline
            cv_scores = cross_val_score(pipeline, X, y, cv=cv, scoring='r2')
            
            print(f"[OK] Validación cruzada completada:")
            print(f"  - Scores por fold: {cv_scores}")
            print(f"  - Score promedio: {cv_scores.mean():.4f}")
            print(f"  - Desviación estándar: {cv_scores.std():.4f}")
            print(f"  - Score mínimo: {cv_scores.min():.4f}")
            print(f"  - Score máximo: {cv_scores.max():.4f}")
            
            return cv_scores
            
        except Exception as e:
            print(f"[ERROR] Error en validación cruzada: {e}")
            return None
    
    def save_splits(self, X_train, X_test, y_train, y_test):
        """Guardar conjuntos de entrenamiento y prueba."""
        print(f"\nGUARDANDO CONJUNTOS TRAIN/TEST")
        print("-" * 50)
        
        # Crear directorio de resultados si no existe
        import os
        os.makedirs("../resultados", exist_ok=True)
        
        # Guardar conjuntos
        X_train.to_csv("../resultados/X_train.csv", index=False)
        X_test.to_csv("../resultados/X_test.csv", index=False)
        y_train.to_csv("../resultados/y_train.csv", index=False)
        y_test.to_csv("../resultados/y_test.csv", index=False)
        
        print(f"[OK] Conjuntos guardados en ../resultados/:")
        print(f"  - X_train.csv: {X_train.shape}")
        print(f"  - X_test.csv: {X_test.shape}")
        print(f"  - y_train.csv: {y_train.shape}")
        print(f"  - y_test.csv: {y_test.shape}")
    
    def show_statistics(self, X_train, X_test, y_train, y_test):
        """Mostrar estadísticas de los conjuntos."""
        print(f"\nESTADISTICAS DE LOS CONJUNTOS")
        print("-" * 50)
        
        # Estadísticas de características
        print("Estadísticas de características (Train):")
        train_stats = X_train.describe()
        print(train_stats.round(2))
        
        print("\nEstadísticas de características (Test):")
        test_stats = X_test.describe()
        print(test_stats.round(2))
        
        # Estadísticas del target
        print(f"\nEstadísticas del target:")
        print(f"Train - Media: {y_train.mean():.2f}, Std: {y_train.std():.2f}")
        print(f"Test  - Media: {y_test.mean():.2f}, Std: {y_test.std():.2f}")
        
        # Verificar distribución similar
        train_mean = X_train.mean()
        test_mean = X_test.mean()
        diff_percent = ((train_mean - test_mean) / train_mean * 100).abs()
        
        print(f"\nDiferencia entre medias (Train vs Test):")
        print(f"Promedio de diferencia: {diff_percent.mean():.2f}%")
        
        if diff_percent.mean() < 5:
            print("[OK] Distribuciones similares entre train y test")
        else:
            print("[WARNING] Distribuciones diferentes entre train y test")
    
    def execute(self):
        """Ejecutar proceso completo de división train/test."""
        # 1. Cargar datos preparados
        X, y = self.load_prepared_dataset()
        
        if X is None or y is None:
            print("[ERROR] No se pudieron cargar los datos")
            return
        
        # 2. Preparar características y target
        X, y = self.prepare_features_target(X, y)
        
        # 3. Dividir en train/test
        X_train, X_test, y_train, y_test = self.split_train_test(X, y)
        
        # 4. Ejemplo de validación cruzada
        modelo_ejemplo = LinearRegression()
        cv_scores = self.cross_validation_example(X_train, y_train, modelo_ejemplo, cv=5)
        
        # 5. Guardar conjuntos
        self.save_splits(X_train, X_test, y_train, y_test)
        
        # 6. Mostrar estadísticas
        self.show_statistics(X_train, X_test, y_train, y_test)
        
        print(f"\n[OK] División train/test completada!")

def main():
    """Función principal del módulo."""
    divisor = TrainTestSplit()
    divisor.execute()

if __name__ == "__main__":
    main()
