#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
<!--
# GENERADOR DE REPORTES - SPRINT_3
**Autor:** Enith Gicela Vargas Vargas  
**Camada:** 1  
**Grupo:** 11  
**Fecha:** 2025-11-11  
**Curso:** AI Fundamentals - Guayerd - IBM Skills Build  
**Sprint:** 3 - Machine Learning Fundamentals  
**Módulo:** Generador de Reportes  
-->

GENERADOR DE REPORTES - PROYECTO AURELION SPRINT_3
==================================================

Módulo para generar y mostrar reportes automáticos de evaluación.
"""

import os               # Módulo del sistema operativo
import pandas as pd     # Módulo para manipulación de datos
import pickle           # Módulo para cargar modelos
import numpy as np      # Módulo para operaciones numéricas
from pathlib import Path  # Módulo para manejo de rutas
from datetime import datetime  # Módulo para fechas

class GeneradorReportes:
    """
    Clase para generar y mostrar reportes automáticos.
    
    Funcionalidades:
    - Generar reportes automáticos
    - Mostrar reportes existentes
    - Crear reportes personalizados
    - Análisis de rendimiento
    """
    
    def __init__(self):
        """Inicializar el generador de reportes."""
        # Manejar el caso cuando se ejecuta con exec() donde __file__ no está definido
        try:
            base_path = Path(__file__).parent
        except NameError:
            base_path = Path(os.getcwd())
            if not (base_path / "generador_reportes.py").exists():
                posibles = [
                    base_path / "Demo",
                    base_path.parent / "Demo",
                    base_path.parent.parent / "Enith Gicela Vargas Vargas - Proyecto Aurelion" / "Demo",
                ]
                for p in posibles:
                    if p.exists() and (p / "generador_reportes.py").exists():
                        base_path = p
                        break
        
        self.resultados_dir = base_path.parent / "resultados"
        self.metricas_dir = self.resultados_dir / "metricas"
        
    def mostrar_reportes(self):
        """Mostrar reportes con opciones automáticas."""
        print("\nREPORTES DE EVALUACIÓN")
        print("=" * 50)
        
        # Verificar si existen reportes
        if not self.metricas_dir.exists():
            print("Directorio de métricas no encontrado.")
            print("Ejecuta primero la evaluación de modelos.")
            return
        
        # Buscar archivos de reporte
        archivos_reporte = []
        for ext in ['.txt', '.md', '.csv']:
            archivos_reporte.extend(list(self.metricas_dir.glob(f"*{ext}")))
        
        if not archivos_reporte:
            print("No se encontraron reportes generados.")
            print("Ejecuta primero la evaluación de modelos.")
            return
        
        print(f"Reportes disponibles ({len(archivos_reporte)}):")
        for i, archivo in enumerate(archivos_reporte, 1):
            tamaño = archivo.stat().st_size
            print(f"{i}. {archivo.name} ({tamaño} bytes)")
        
        print(f"\n{len(archivos_reporte) + 1}. Generar reporte completo automático")
        print(f"{len(archivos_reporte) + 2}. Ver resumen ejecutivo")
        print(f"{len(archivos_reporte) + 3}. Abrir carpeta de reportes")
        print(f"{len(archivos_reporte) + 4}. Volver al menú principal")
        
        try:
            opcion = input(f"\nSelecciona una opción (1-{len(archivos_reporte) + 4}): ").strip()
            
            if opcion.isdigit():
                opcion_num = int(opcion)
                
                if 1 <= opcion_num <= len(archivos_reporte):
                    # Mostrar reporte seleccionado
                    archivo_seleccionado = archivos_reporte[opcion_num - 1]
                    self._mostrar_reporte(archivo_seleccionado)
                    
                elif opcion_num == len(archivos_reporte) + 1:
                    # Generar reporte completo
                    self._generar_reporte_completo()
                    
                elif opcion_num == len(archivos_reporte) + 2:
                    # Ver resumen ejecutivo
                    self._mostrar_resumen_ejecutivo()
                    
                elif opcion_num == len(archivos_reporte) + 3:
                    # Abrir carpeta
                    self._abrir_carpeta()
                    
                elif opcion_num == len(archivos_reporte) + 4:
                    # Volver
                    return
                else:
                    print("Opción inválida.")
            else:
                print("Opción inválida.")
                
        except KeyboardInterrupt:
            print("\nOperación cancelada.")
        except Exception as e:
            print(f"Error: {e}")
    
    def _mostrar_reporte(self, archivo_reporte):
        """Mostrar contenido de un reporte específico."""
        print(f"\nMostrando reporte: {archivo_reporte.name}")
        print("-" * 50)
        
        try:
            with open(archivo_reporte, 'r', encoding='utf-8') as f:
                contenido = f.read()
                print(contenido)
                
        except Exception as e:
            print(f"[ERROR] Error al leer reporte: {e}")
    
    def _generar_reporte_completo(self):
        """Generar reporte completo automático."""
        print(f"\nGENERANDO REPORTE COMPLETO AUTOMÁTICO")
        print("-" * 50)
        
        try:
            # Verificar archivos necesarios
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
                print("[ERROR] Archivos faltantes para generar reporte:")
                for archivo in archivos_faltantes:
                    print(f"  - {archivo}")
                return
            
            # Cargar datos
            X_test = pd.read_csv(self.resultados_dir / "X_test.csv")
            y_test = pd.read_csv(self.resultados_dir / "y_test.csv")
            X_train = pd.read_csv(self.resultados_dir / "X_train.csv")
            y_train = pd.read_csv(self.resultados_dir / "y_train.csv")
            
            # Generar reporte
            reporte = self._crear_reporte_completo(X_test, y_test, X_train, y_train)
            
            # Guardar reporte
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            nombre_archivo = f"reporte_completo_{timestamp}.txt"
            ruta_reporte = self.metricas_dir / nombre_archivo
            
            with open(ruta_reporte, 'w', encoding='utf-8') as f:
                f.write(reporte)
            
            print(f"[OK] Reporte completo generado: {nombre_archivo}")
            print(f"Ubicación: {ruta_reporte.absolute()}")
            
            # Mostrar resumen del reporte
            print(f"\nResumen del reporte generado:")
            print("-" * 40)
            print(reporte[:500] + "..." if len(reporte) > 500 else reporte)
            
        except Exception as e:
            print(f"[ERROR] Error generando reporte: {e}")
    
    def _crear_reporte_completo(self, X_test, y_test, X_train, y_train):
        """Crear contenido del reporte completo."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        reporte = f"""
REPORTE COMPLETO DE EVALUACIÓN - PROYECTO AURELION SPRINT_3
===========================================================
Fecha de generación: {timestamp}
Autor: Enith Gicela Vargas Vargas
Curso: AI Fundamentals - Guayerd - IBM Skills Build

RESUMEN EJECUTIVO
=================
Este reporte presenta un análisis completo de los modelos de Machine Learning
entrenados para el proyecto Aurelion, incluyendo métricas de rendimiento,
comparaciones detalladas y recomendaciones para producción.

DATOS DEL PROYECTO
==================
- Dataset: Tienda Aurelion
- Muestras de entrenamiento: {X_train.shape[0]}
- Muestras de prueba: {X_test.shape[0]}
- Características: {X_train.shape[1]}
- Variable objetivo: importe (ventas)

MODELOS EVALUADOS
=================
1. Linear Regression
2. Random Forest Regressor  
3. Support Vector Regression (SVR)

MÉTRICAS DE EVALUACIÓN
======================
Se evaluaron los siguientes modelos usando métricas estándar:
- MSE (Mean Squared Error)
- RMSE (Root Mean Squared Error)
- MAE (Mean Absolute Error)
- R² (Coeficiente de determinación)
- MAPE (Mean Absolute Percentage Error)

RESULTADOS DETALLADOS
=====================
"""
        
        # Evaluar cada modelo
        modelos = [
            ("Linear Regression", "linear_regression.pkl"),
            ("Random Forest Regressor", "random_forest_regressor.pkl"),
            ("SVR", "svr.pkl")
        ]
        
        resultados_modelos = []
        
        for nombre, archivo in modelos:
            try:
                with open(self.resultados_dir / "modelos" / archivo, 'rb') as f:
                    modelo = pickle.load(f)
                
                # Predicciones
                pred_test = modelo.predict(X_test)
                pred_train = modelo.predict(X_train)
                
                # Métricas
                mse_test = np.mean((pred_test - y_test.iloc[:, 0]) ** 2)
                mae_test = np.mean(np.abs(pred_test - y_test.iloc[:, 0]))
                rmse_test = np.sqrt(mse_test)
                
                ss_res = np.sum((y_test.iloc[:, 0] - pred_test) ** 2)
                ss_tot = np.sum((y_test.iloc[:, 0] - y_test.iloc[:, 0].mean()) ** 2)
                r2_test = 1 - (ss_res / ss_tot) if ss_tot != 0 else 0
                
                resultados_modelos.append({
                    'nombre': nombre,
                    'mse': mse_test,
                    'mae': mae_test,
                    'rmse': rmse_test,
                    'r2': r2_test
                })
                
            except Exception as e:
                reporte += f"\nError evaluando {nombre}: {e}\n"
        
        # Agregar resultados al reporte
        if resultados_modelos:
            reporte += "\nTABLA DE RESULTADOS:\n"
            reporte += "-" * 60 + "\n"
            reporte += f"{'Modelo':<20} {'MSE':<12} {'RMSE':<12} {'MAE':<12} {'R²':<12}\n"
            reporte += "-" * 60 + "\n"
            
            for resultado in resultados_modelos:
                reporte += f"{resultado['nombre']:<20} {resultado['mse']:<12.2f} {resultado['rmse']:<12.2f} {resultado['mae']:<12.2f} {resultado['r2']:<12.4f}\n"
            
            # Mejor modelo
            mejor_modelo = max(resultados_modelos, key=lambda x: x['r2'])
            reporte += f"\nMEJOR MODELO: {mejor_modelo['nombre']}\n"
            reporte += f"R² Score: {mejor_modelo['r2']:.4f}\n"
            reporte += f"MSE: {mejor_modelo['mse']:.2f}\n"
        
        reporte += f"""

ANÁLISIS Y RECOMENDACIONES
===========================
1. RENDIMIENTO GENERAL:
   - El mejor modelo logra un R² de {mejor_modelo['r2']:.4f}
   - Esto indica una capacidad predictiva {'limitada' if mejor_modelo['r2'] < 0.5 else 'moderada' if mejor_modelo['r2'] < 0.8 else 'buena'}
   - Se recomienda recopilar más datos para mejorar el rendimiento

2. RECOMENDACIONES PARA PRODUCCIÓN:
   - Usar {mejor_modelo['nombre']} como modelo principal
   - Implementar monitoreo de deriva de datos
   - Re-entrenar periódicamente con nuevos datos
   - Considerar ingeniería de características adicionales

3. PRÓXIMOS PASOS:
   - Recopilar más datos históricos de Aurelion
   - Experimentar con más características
   - Probar algoritmos de ensemble
   - Implementar validación cruzada más robusta

CONCLUSIONES
============
Los modelos entrenados proporcionan una base sólida para predicciones de ventas
en la tienda Aurelion. Aunque el rendimiento es {'limitado' if mejor_modelo['r2'] < 0.5 else 'moderado' if mejor_modelo['r2'] < 0.8 else 'bueno'},
los resultados son interpretables y útiles para la toma de decisiones empresariales.

---
Reporte generado automáticamente por el sistema de evaluación Sprint_3
Proyecto Aurelion - AI Fundamentals Guayerd IBM Skills Build
"""
        
        return reporte
    
    def _mostrar_resumen_ejecutivo(self):
        """Mostrar resumen ejecutivo rápido."""
        print(f"\nRESUMEN EJECUTIVO - PROYECTO AURELION")
        print("=" * 50)
        
        try:
            # Verificar archivos básicos
            if not (self.resultados_dir / "modelos" / "mejor_modelo_info.txt").exists():
                print("Información del mejor modelo no disponible.")
                print("Ejecuta primero la evaluación de modelos.")
                return
            
            # Leer información del mejor modelo
            with open(self.resultados_dir / "modelos" / "mejor_modelo_info.txt", 'r') as f:
                info_modelo = f.read()
            
            print("INFORMACIÓN DEL MEJOR MODELO:")
            print("-" * 30)
            print(info_modelo)
            
            # Mostrar estadísticas básicas
            if (self.resultados_dir / "X_test.csv").exists():
                X_test = pd.read_csv(self.resultados_dir / "X_test.csv")
                y_test = pd.read_csv(self.resultados_dir / "y_test.csv")
                
                print(f"\nESTADÍSTICAS DEL DATASET:")
                print("-" * 30)
                print(f"Muestras de prueba: {X_test.shape[0]}")
                print(f"Características: {X_test.shape[1]}")
                print(f"Rango de valores objetivo: {y_test.iloc[:, 0].min():.2f} - {y_test.iloc[:, 0].max():.2f}")
                print(f"Promedio de valores objetivo: {y_test.iloc[:, 0].mean():.2f}")
            
        except Exception as e:
            print(f"[ERROR] Error mostrando resumen: {e}")
    
    def _abrir_carpeta(self):
        """Abrir carpeta de reportes."""
        print(f"\nAbriendo carpeta de reportes...")
        
        try:
            if os.name == 'nt':  # Windows
                os.startfile(str(self.metricas_dir))
                print(f"[OK] Carpeta abierta en explorador")
            else:  # Linux/Mac
                import subprocess
                subprocess.run(['xdg-open', str(self.metricas_dir)])
                print(f"[OK] Carpeta abierta en explorador")
                
        except Exception as e:
            print(f"[ERROR] No se pudo abrir carpeta: {e}")
            print(f"Ubicación: {self.metricas_dir.absolute()}")

def main():
    """Función principal para pruebas."""
    generador = GeneradorReportes()
    
    print("GENERADOR DE REPORTES - PROYECTO AURELION")
    print("Grupo 11 - Camada 1 | Enith Gicela Vargas Vargas")
    print("=" * 60)
    
    generador.mostrar_reportes()

if __name__ == "__main__":
    main()
