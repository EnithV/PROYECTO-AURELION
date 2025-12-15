#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
<!--
# COMPARADOR DE MODELOS - SPRINT_3
**Autor:** Enith Gicela Vargas Vargas  
**Camada:** 1  
**Grupo:** 11  
**Fecha:** 2025-11-11  
**Curso:** AI Fundamentals - Guayerd - IBM Skills Build  
**Sprint:** 3 - Machine Learning Fundamentals  
**Módulo:** Comparador de Modelos  
-->

COMPARADOR DE MODELOS - PROYECTO AURELION SPRINT_3
==================================================

Módulo para comparación detallada de modelos entrenados.
"""

import os               # Módulo del sistema operativo
import pandas as pd     # Módulo para manipulación de datos
import pickle           # Módulo para cargar modelos
import numpy as np      # Módulo para operaciones numéricas
from pathlib import Path  # Módulo para manejo de rutas

class ComparadorModelos:
    """
    Clase para comparación detallada de modelos entrenados.
    
    Funcionalidades:
    - Comparación exhaustiva de modelos
    - Análisis de rendimiento
    - Visualización de diferencias
    - Recomendaciones de uso
    """
    
    def __init__(self):
        """Inicializar el comparador de modelos."""
        # Manejar el caso cuando se ejecuta con exec() donde __file__ no está definido
        try:
            base_path = Path(__file__).parent
        except NameError:
            base_path = Path(os.getcwd())
            if not (base_path / "comparador_modelos.py").exists():
                posibles = [
                    base_path / "Demo",
                    base_path.parent / "Demo",
                    base_path.parent.parent / "Enith Gicela Vargas Vargas - Proyecto Aurelion" / "Demo",
                ]
                for p in posibles:
                    if p.exists() and (p / "comparador_modelos.py").exists():
                        base_path = p
                        break
        
        self.resultados_dir = base_path.parent / "resultados"
        self.modelos_dir = self.resultados_dir / "modelos"
        
    def comparar_modelos(self):
        """Realizar comparación detallada de todos los modelos."""
        print("\nCOMPARACIÓN DETALLADA DE MODELOS")
        print("=" * 50)
        
        # Verificar que existen los archivos necesarios
        if not self._verificar_archivos():
            return
        
        try:
            # Cargar datos
            print("Cargando datos para comparación...")
            X_test = pd.read_csv(self.resultados_dir / "X_test.csv")
            y_test = pd.read_csv(self.resultados_dir / "y_test.csv")
            X_train = pd.read_csv(self.resultados_dir / "X_train.csv")
            y_train = pd.read_csv(self.resultados_dir / "y_train.csv")
            
            print(f"[OK] Datos de prueba: {X_test.shape[0]} muestras")
            print(f"[OK] Datos de entrenamiento: {X_train.shape[0]} muestras")
            
            # Evaluar todos los modelos
            resultados = self._evaluar_todos_modelos(X_test, y_test, X_train, y_train)
            
            # Mostrar comparación detallada
            self._mostrar_comparacion_detallada(resultados)
            
            # Mostrar análisis de rendimiento
            self._mostrar_analisis_rendimiento(resultados)
            
            # Mostrar recomendaciones
            self._mostrar_recomendaciones(resultados)
            
        except Exception as e:
            print(f"[ERROR] Error en comparación: {e}")
    
    def _verificar_archivos(self):
        """Verificar que existen los archivos necesarios."""
        archivos_requeridos = [
            "X_test.csv", "y_test.csv",
            "X_train.csv", "y_train.csv",
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
    
    def _evaluar_todos_modelos(self, X_test, y_test, X_train, y_train):
        """Evaluar todos los modelos y recopilar resultados."""
        modelos = [
            ("Linear Regression", "linear_regression.pkl"),
            ("Random Forest Regressor", "random_forest_regressor.pkl"),
            ("SVR", "svr.pkl")
        ]
        
        resultados = []
        
        for nombre, archivo in modelos:
            try:
                print(f"Evaluando {nombre}...")
                
                # Cargar modelo
                with open(self.modelos_dir / archivo, 'rb') as f:
                    modelo = pickle.load(f)
                
                # Predicciones en test
                pred_test = modelo.predict(X_test)
                pred_train = modelo.predict(X_train)
                
                # Calcular métricas
                metricas_test = self._calcular_metricas(pred_test, y_test.iloc[:, 0])
                metricas_train = self._calcular_metricas(pred_train, y_train.iloc[:, 0])
                
                # Detectar sobreajuste
                sobreajuste = metricas_train['r2'] - metricas_test['r2']
                
                resultado = {
                    'nombre': nombre,
                    'archivo': archivo,
                    'modelo': modelo,
                    'metricas_test': metricas_test,
                    'metricas_train': metricas_train,
                    'sobreajuste': sobreajuste,
                    'predicciones_test': pred_test,
                    'predicciones_train': pred_train
                }
                
                resultados.append(resultado)
                print(f"[OK] {nombre} evaluado")
                
            except Exception as e:
                print(f"[ERROR] Error evaluando {nombre}: {e}")
        
        return resultados
    
    def _calcular_metricas(self, predicciones, valores_reales):
        """Calcular métricas de evaluación."""
        # MSE
        mse = np.mean((predicciones - valores_reales) ** 2)
        
        # RMSE
        rmse = np.sqrt(mse)
        
        # MAE
        mae = np.mean(np.abs(predicciones - valores_reales))
        
        # R²
        ss_res = np.sum((valores_reales - predicciones) ** 2)
        ss_tot = np.sum((valores_reales - valores_reales.mean()) ** 2)
        r2 = 1 - (ss_res / ss_tot) if ss_tot != 0 else 0
        
        # MAPE
        mape = np.mean(np.abs((valores_reales - predicciones) / valores_reales)) * 100
        
        return {
            'mse': mse,
            'rmse': rmse,
            'mae': mae,
            'r2': r2,
            'mape': mape
        }
    
    def _mostrar_comparacion_detallada(self, resultados):
        """Mostrar comparación detallada de modelos."""
        print(f"\nTABLA COMPARATIVA DETALLADA")
        print("=" * 80)
        
        # Encabezados
        print(f"{'Modelo':<20} {'MSE':<12} {'RMSE':<12} {'MAE':<12} {'R²':<12} {'MAPE':<12}")
        print("-" * 80)
        
        # Datos de test
        print("RENDIMIENTO EN TEST:")
        for resultado in resultados:
            m = resultado['metricas_test']
            print(f"{resultado['nombre']:<20} {m['mse']:<12.2f} {m['rmse']:<12.2f} {m['mae']:<12.2f} {m['r2']:<12.4f} {m['mape']:<12.2f}")
        
        print("\nRENDIMIENTO EN TRAIN:")
        for resultado in resultados:
            m = resultado['metricas_train']
            print(f"{resultado['nombre']:<20} {m['mse']:<12.2f} {m['rmse']:<12.2f} {m['mae']:<12.2f} {m['r2']:<12.4f} {m['mape']:<12.2f}")
        
        # Ranking de modelos
        print(f"\nRANKING DE MODELOS (por R² en test):")
        print("-" * 50)
        modelos_ordenados = sorted(resultados, key=lambda x: x['metricas_test']['r2'], reverse=True)
        
        for i, resultado in enumerate(modelos_ordenados, 1):
            r2 = resultado['metricas_test']['r2']
            print(f"{i}. {resultado['nombre']:<20} R² = {r2:.4f}")
    
    def _mostrar_analisis_rendimiento(self, resultados):
        """Mostrar análisis de rendimiento."""
        print(f"\nANÁLISIS DE RENDIMIENTO")
        print("=" * 50)
        
        # Mejor modelo por cada métrica
        mejor_mse = min(resultados, key=lambda x: x['metricas_test']['mse'])
        mejor_r2 = max(resultados, key=lambda x: x['metricas_test']['r2'])
        mejor_mae = min(resultados, key=lambda x: x['metricas_test']['mae'])
        
        print(f"Mejor modelo por MSE: {mejor_mse['nombre']} ({mejor_mse['metricas_test']['mse']:.2f})")
        print(f"Mejor modelo por R²: {mejor_r2['nombre']} ({mejor_r2['metricas_test']['r2']:.4f})")
        print(f"Mejor modelo por MAE: {mejor_mae['nombre']} ({mejor_mae['metricas_test']['mae']:.2f})")
        
        # Análisis de sobreajuste
        print(f"\nANÁLISIS DE SOBREAJUSTE:")
        print("-" * 30)
        for resultado in resultados:
            nombre = resultado['nombre']
            sobreajuste = resultado['sobreajuste']
            r2_train = resultado['metricas_train']['r2']
            r2_test = resultado['metricas_test']['r2']
            
            if sobreajuste > 0.1:
                estado = "ALTO sobreajuste"
            elif sobreajuste > 0.05:
                estado = "MEDIO sobreajuste"
            elif sobreajuste > 0:
                estado = "BAJO sobreajuste"
            else:
                estado = "Sin sobreajuste"
            
            print(f"{nombre:<20}: {estado} (R² train: {r2_train:.4f}, R² test: {r2_test:.4f})")
        
        # Análisis de estabilidad
        print(f"\nANÁLISIS DE ESTABILIDAD:")
        print("-" * 30)
        for resultado in resultados:
            nombre = resultado['nombre']
            mse_train = resultado['metricas_train']['mse']
            mse_test = resultado['metricas_test']['mse']
            diferencia = abs(mse_test - mse_train) / mse_train * 100
            
            if diferencia < 10:
                estabilidad = "MUY ESTABLE"
            elif diferencia < 25:
                estabilidad = "ESTABLE"
            elif diferencia < 50:
                estabilidad = "MODERADAMENTE ESTABLE"
            else:
                estabilidad = "INESTABLE"
            
            print(f"{nombre:<20}: {estabilidad} ({diferencia:.1f}% diferencia)")
    
    def _mostrar_recomendaciones(self, resultados):
        """Mostrar recomendaciones basadas en el análisis."""
        print(f"\nRECOMENDACIONES")
        print("=" * 50)
        
        # Mejor modelo general
        mejor_modelo = max(resultados, key=lambda x: x['metricas_test']['r2'])
        print(f"MEJOR MODELO GENERAL: {mejor_modelo['nombre']}")
        print(f"Razón: Mayor R² en datos de prueba ({mejor_modelo['metricas_test']['r2']:.4f})")
        
        # Análisis de casos de uso
        print(f"\nCASOS DE USO RECOMENDADOS:")
        print("-" * 30)
        
        for resultado in resultados:
            nombre = resultado['nombre']
            r2 = resultado['metricas_test']['r2']
            sobreajuste = resultado['sobreajuste']
            
            if nombre == "Linear Regression":
                if r2 > 0.2:
                    recomendacion = "Ideal para análisis interpretable y predicciones estables"
                else:
                    recomendacion = "Útil como baseline, considerar modelos más complejos"
            elif nombre == "Random Forest Regressor":
                if sobreajuste < 0.1:
                    recomendacion = "Excelente para datos complejos con buena generalización"
                else:
                    recomendacion = "Potente pero puede sobreajustar, usar con regularización"
            elif nombre == "SVR":
                if r2 > 0:
                    recomendacion = "Bueno para datos no lineales, requiere tuning de hiperparámetros"
                else:
                    recomendacion = "Rendimiento pobre, considerar otros algoritmos"
            
            print(f"{nombre:<20}: {recomendacion}")
        
        # Recomendaciones generales
        print(f"\nRECOMENDACIONES GENERALES:")
        print("-" * 30)
        print("1. Para este dataset de Aurelion:")
        print("   - Linear Regression ofrece el mejor balance rendimiento/interpretabilidad")
        print("   - Random Forest muestra sobreajuste, necesita regularización")
        print("   - SVR requiere más tuning de hiperparámetros")
        
        print("\n2. Para mejorar el rendimiento:")
        print("   - Recopilar más datos de Aurelion")
        print("   - Ingeniería de características adicionales")
        print("   - Tuning de hiperparámetros")
        print("   - Ensamblaje de modelos")
        
        print("\n3. Para producción:")
        print("   - Usar Linear Regression por su estabilidad")
        print("   - Implementar monitoreo de deriva de datos")
        print("   - Re-entrenar periódicamente con nuevos datos")

def main():
    """Función principal para pruebas."""
    comparador = ComparadorModelos()
    
    print("COMPARADOR DE MODELOS - PROYECTO AURELION")
    print("Grupo 11 - Camada 1 | Enith Gicela Vargas Vargas")
    print("=" * 60)
    
    comparador.comparar_modelos()

if __name__ == "__main__":
    main()
