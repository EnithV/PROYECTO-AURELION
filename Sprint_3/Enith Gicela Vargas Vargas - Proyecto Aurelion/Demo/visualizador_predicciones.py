#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
<!--
# VISUALIZADOR DE PREDICCIONES - SPRINT_3
**Autor:** Enith Gicela Vargas Vargas  
**Camada:** 1  
**Grupo:** 11  
**Fecha:** 2025-11-11  
**Curso:** AI Fundamentals - Guayerd - IBM Skills Build  
**Sprint:** 3 - Machine Learning Fundamentals  
**Módulo:** Visualizador de Predicciones  
-->

VISUALIZADOR DE PREDICCIONES - PROYECTO AURELION SPRINT_3
=========================================================

Módulo para mostrar predicciones reales de modelos entrenados.
"""

import os               # Módulo del sistema operativo
import pandas as pd     # Módulo para manipulación de datos
import pickle           # Módulo para cargar modelos
import numpy as np      # Módulo para operaciones numéricas
from pathlib import Path  # Módulo para manejo de rutas

class VisualizadorPredicciones:
    """
    Clase para mostrar predicciones reales de modelos entrenados.
    
    Funcionalidades:
    - Cargar modelos entrenados
    - Cargar datos de prueba
    - Generar predicciones
    - Mostrar comparaciones
    - Visualizar resultados
    """
    
    def __init__(self):
        """Inicializar el visualizador de predicciones."""
        # Manejar el caso cuando se ejecuta con exec() donde __file__ no está definido
        try:
            base_path = Path(__file__).parent
        except NameError:
            base_path = Path(os.getcwd())
            if not (base_path / "visualizador_predicciones.py").exists():
                posibles = [
                    base_path / "Demo",
                    base_path.parent / "Demo",
                    base_path.parent.parent / "Enith Gicela Vargas Vargas - Proyecto Aurelion" / "Demo",
                ]
                for p in posibles:
                    if p.exists() and (p / "visualizador_predicciones.py").exists():
                        base_path = p
                        break
        
        self.resultados_dir = base_path.parent / "resultados"
        self.modelos_dir = self.resultados_dir / "modelos"
        
    def mostrar_predicciones(self):
        """Mostrar predicciones de todos los modelos entrenados."""
        print("\nPREDICCIONES DE MODELOS ENTRENADOS")
        print("=" * 50)
        
        # Verificar que existen los archivos necesarios
        if not self._verificar_archivos():
            return
        
        try:
            # Cargar datos de prueba
            print("Cargando datos de prueba...")
            X_test = pd.read_csv(self.resultados_dir / "X_test.csv")
            y_test = pd.read_csv(self.resultados_dir / "y_test.csv")
            
            print(f"[OK] Datos de prueba cargados: {X_test.shape[0]} muestras")
            
            # Cargar escalador
            print("Cargando escalador...")
            with open(self.resultados_dir / "scaler.pkl", 'rb') as f:
                scaler = pickle.load(f)
            print("[OK] Escalador cargado")
            
            # Mostrar predicciones de cada modelo
            self._mostrar_predicciones_modelo("Linear Regression", X_test, y_test, scaler)
            self._mostrar_predicciones_modelo("Random Forest Regressor", X_test, y_test, scaler)
            self._mostrar_predicciones_modelo("SVR", X_test, y_test, scaler)
            
            # Mostrar comparación general
            self._mostrar_comparacion_general(X_test, y_test, scaler)
            
        except Exception as e:
            print(f"[ERROR] Error al cargar datos: {e}")
            print("Verifica que los archivos de datos y modelos existan.")
    
    def _verificar_archivos(self):
        """Verificar que existen los archivos necesarios."""
        archivos_requeridos = [
            "X_test.csv",
            "y_test.csv", 
            "scaler.pkl",
            "modelos/linear_regression.pkl",
            "modelos/random_forest_regressor.pkl",
            "modelos/svr.pkl"
        ]
        
        archivos_faltantes = []
        for archivo in archivos_requeridos:
            ruta_archivo = self.resultados_dir / archivo
            if not ruta_archivo.exists():
                archivos_faltantes.append(archivo)
        
        if archivos_faltantes:
            print("[ERROR] Archivos faltantes:")
            for archivo in archivos_faltantes:
                print(f"  - {archivo}")
            print("\nEjecuta primero:")
            print("1. Preparación de datos (Opción 5)")
            print("2. Entrenamiento de modelos (Opción 6)")
            return False
        
        return True
    
    def _mostrar_predicciones_modelo(self, nombre_modelo, X_test, y_test, scaler):
        """Mostrar predicciones de un modelo específico."""
        print(f"\n{nombre_modelo.upper()}")
        print("-" * 40)
        
        try:
            # Cargar modelo
            archivo_modelo = nombre_modelo.lower().replace(" ", "_") + ".pkl"
            ruta_modelo = self.modelos_dir / archivo_modelo
            
            with open(ruta_modelo, 'rb') as f:
                modelo = pickle.load(f)
            
            # Generar predicciones
            predicciones = modelo.predict(X_test)
            
            # Mostrar estadísticas básicas
            print(f"Predicciones generadas: {len(predicciones)}")
            print(f"Valor mínimo predicho: {predicciones.min():.2f}")
            print(f"Valor máximo predicho: {predicciones.max():.2f}")
            print(f"Valor promedio predicho: {predicciones.mean():.2f}")
            
            # Mostrar primeras predicciones vs valores reales
            print(f"\nPrimeras 10 predicciones vs valores reales:")
            print("Index | Predicción | Valor Real | Diferencia | Error %")
            print("-" * 55)
            
            for i in range(min(10, len(predicciones))):
                pred = predicciones[i]
                real = y_test.iloc[i, 0]  # Asumiendo que y_test tiene una columna
                diff = pred - real
                error_pct = abs(diff / real * 100) if real != 0 else 0
                
                print(f"{i:5d} | {pred:10.2f} | {real:10.2f} | {diff:10.2f} | {error_pct:7.1f}%")
            
            # Calcular métricas básicas
            mse = np.mean((predicciones - y_test.iloc[:, 0]) ** 2)
            mae = np.mean(np.abs(predicciones - y_test.iloc[:, 0]))
            
            print(f"\nMétricas básicas:")
            print(f"  MSE: {mse:.2f}")
            print(f"  MAE: {mae:.2f}")
            
        except Exception as e:
            print(f"[ERROR] Error con {nombre_modelo}: {e}")
    
    def _mostrar_comparacion_general(self, X_test, y_test, scaler):
        """Mostrar comparación general de todos los modelos."""
        print(f"\nCOMPARACIÓN GENERAL DE MODELOS")
        print("=" * 50)
        
        modelos_info = []
        
        # Evaluar cada modelo
        modelos = [
            ("Linear Regression", "linear_regression.pkl"),
            ("Random Forest Regressor", "random_forest_regressor.pkl"),
            ("SVR", "svr.pkl")
        ]
        
        for nombre, archivo in modelos:
            try:
                with open(self.modelos_dir / archivo, 'rb') as f:
                    modelo = pickle.load(f)
                
                predicciones = modelo.predict(X_test)
                
                # Calcular métricas
                mse = np.mean((predicciones - y_test.iloc[:, 0]) ** 2)
                mae = np.mean(np.abs(predicciones - y_test.iloc[:, 0]))
                rmse = np.sqrt(mse)
                
                # Calcular R²
                ss_res = np.sum((y_test.iloc[:, 0] - predicciones) ** 2)
                ss_tot = np.sum((y_test.iloc[:, 0] - y_test.iloc[:, 0].mean()) ** 2)
                r2 = 1 - (ss_res / ss_tot) if ss_tot != 0 else 0
                
                modelos_info.append({
                    'nombre': nombre,
                    'mse': mse,
                    'mae': mae,
                    'rmse': rmse,
                    'r2': r2
                })
                
            except Exception as e:
                print(f"[ERROR] Error evaluando {nombre}: {e}")
        
        # Mostrar tabla comparativa
        if modelos_info:
            print(f"\nTabla comparativa de métricas:")
            print("-" * 80)
            print(f"{'Modelo':<20} {'MSE':<12} {'MAE':<12} {'RMSE':<12} {'R²':<12}")
            print("-" * 80)
            
            for info in modelos_info:
                print(f"{info['nombre']:<20} {info['mse']:<12.2f} {info['mae']:<12.2f} {info['rmse']:<12.2f} {info['r2']:<12.4f}")
            
            # Identificar mejor modelo
            mejor_modelo = min(modelos_info, key=lambda x: x['mse'])
            print(f"\nMejor modelo por MSE: {mejor_modelo['nombre']}")
            print(f"MSE: {mejor_modelo['mse']:.2f}")
            print(f"R²: {mejor_modelo['r2']:.4f}")
    
    def mostrar_predicciones_especificas(self, modelo_nombre):
        """Mostrar predicciones de un modelo específico con más detalle."""
        print(f"\nPREDICCIONES DETALLADAS - {modelo_nombre.upper()}")
        print("=" * 50)
        
        if not self._verificar_archivos():
            return
        
        try:
            # Cargar datos
            X_test = pd.read_csv(self.resultados_dir / "X_test.csv")
            y_test = pd.read_csv(self.resultados_dir / "y_test.csv")
            
            # Cargar modelo específico
            archivo_modelo = modelo_nombre.lower().replace(" ", "_") + ".pkl"
            ruta_modelo = self.modelos_dir / archivo_modelo
            
            if not ruta_modelo.exists():
                print(f"[ERROR] Modelo {modelo_nombre} no encontrado.")
                return
            
            with open(ruta_modelo, 'rb') as f:
                modelo = pickle.load(f)
            
            # Generar predicciones
            predicciones = modelo.predict(X_test)
            
            # Mostrar todas las predicciones
            print(f"Todas las predicciones ({len(predicciones)} muestras):")
            print("Index | Predicción | Valor Real | Diferencia | Error %")
            print("-" * 60)
            
            for i in range(len(predicciones)):
                pred = predicciones[i]
                real = y_test.iloc[i, 0]
                diff = pred - real
                error_pct = abs(diff / real * 100) if real != 0 else 0
                
                print(f"{i:5d} | {pred:10.2f} | {real:10.2f} | {diff:10.2f} | {error_pct:7.1f}%")
            
        except Exception as e:
            print(f"[ERROR] Error: {e}")

def main():
    """Función principal para pruebas."""
    visualizador = VisualizadorPredicciones()
    
    print("VISUALIZADOR DE PREDICCIONES - PROYECTO AURELION")
    print("Grupo 11 - Camada 1 | Enith Gicela Vargas Vargas")
    print("=" * 60)
    
    while True:
        print("\nMENU DE PREDICCIONES:")
        print("1. Ver predicciones de todos los modelos")
        print("2. Ver predicciones detalladas - Linear Regression")
        print("3. Ver predicciones detalladas - Random Forest")
        print("4. Ver predicciones detalladas - SVR")
        print("5. Salir")
        
        opcion = input("\nSelecciona una opción (1-5): ").strip()
        
        if opcion == '1':
            visualizador.mostrar_predicciones()
        elif opcion == '2':
            visualizador.mostrar_predicciones_especificas("Linear Regression")
        elif opcion == '3':
            visualizador.mostrar_predicciones_especificas("Random Forest Regressor")
        elif opcion == '4':
            visualizador.mostrar_predicciones_especificas("SVR")
        elif opcion == '5':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()
