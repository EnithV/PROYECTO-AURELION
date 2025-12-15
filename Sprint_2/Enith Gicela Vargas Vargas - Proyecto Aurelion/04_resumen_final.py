#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RESUMEN FINAL - PROYECTO AURELION SPRINT_2
==========================================

**Autor:** Enith Gicela Vargas Vargas  
**Camada:** 1  
**Grupo:** 11  
**Fecha:** 2025-10-27  
**Curso:** AI Fundamentals - Guayerd - IBM Skills Build  
**Sprint:** 2 - Machine Learning y Normalización  
**Módulo:** Resumen Final  

Script para mostrar un resumen completo del proyecto de normalizacion
de datos, incluyendo estadisticas, archivos generados y resultados.
"""

import pandas as pd          # Librería para manipulación de datos estructurados
import os                    # Módulo del sistema operativo
import glob                  # Módulo para búsqueda de archivos con patrones

class ResumenFinal:
    """
    Clase para generar resumen final del proyecto.
    """
    
    def __init__(self):
        """Inicializar el generador de resumen."""
        self.base_path = "../../Datos Proyecto/Base de datos_Tienda_Aurelion/Base de datos"
        
    def mostrar_resumen_proyecto(self):
        """Mostrar resumen completo del proyecto."""
        print("RESUMEN FINAL - PROYECTO AURELION")
        print("Grupo 11 - Camada 1 | Enith Gicela Vargas Vargas")
        print("=" * 80)
        
        # Informacion del proyecto
        print("\nINFORMACION DEL PROYECTO:")
        print("-" * 40)
        print("   Objetivo: Normalizacion de datos para Machine Learning")
        print("   Base de datos: Tienda Aurelion")
        print("   Tablas procesadas: 4 (clientes, productos, ventas, detalle_ventas)")
        print("   Fases completadas: 3")
        print("   Dataset final: 343 registros x 27 columnas")
        
        # Archivos generados
        self.mostrar_archivos_generados()
        
        # Estadisticas del dataset final
        self.mostrar_estadisticas_dataset_final()
        
        # Resumen de normalizacion
        self.mostrar_resumen_normalizacion()
        
        # Recomendaciones
        self.mostrar_recomendaciones()
    
    def mostrar_archivos_generados(self):
        """Mostrar archivos generados en el proyecto."""
        print(f"\nARCHIVOS GENERADOS:")
        print("-" * 30)
        
        # Scripts principales
        print("   SCRIPTS PRINCIPALES:")
        scripts = [
            "00_analisis_esquema_simple.py",
            "01_analisis_exploratorio_simple.py", 
            "02_normalizacion_datos.py",
            "03_merge_tablas.py",
            "04_resumen_final.py"
        ]
        for script in scripts:
            if os.path.exists(script):
                print(f"     [OK] {script}")
            else:
                print(f"     [NO] {script}")
        
        # Datasets normalizados
        print("\n   DATASETS NORMALIZADOS:")
        datasets_path = "resultados/datasets_normalizados/"
        if os.path.exists(datasets_path):
            archivos = os.listdir(datasets_path)
            for archivo in archivos:
                if archivo.endswith('.csv'):
                    print(f"     [OK] {archivo}")
        
        # Estadisticas
        print("\n   ARCHIVOS DE ESTADISTICAS:")
        stats_path = "resultados/estadisticas/"
        if os.path.exists(stats_path):
            archivos = os.listdir(stats_path)
            for archivo in archivos:
                if archivo.endswith('.txt') or archivo.endswith('.csv'):
                    print(f"     [OK] {archivo}")
    
    def mostrar_estadisticas_dataset_final(self):
        """Mostrar estadisticas del dataset final."""
        print(f"\nESTADISTICAS DEL DATASET FINAL:")
        print("-" * 40)
        
        try:
            # Cargar dataset final
            dataset = pd.read_csv("resultados/datasets_normalizados/dataset_final_completo.csv")
            
            print(f"   Dimensiones: {dataset.shape[0]} filas x {dataset.shape[1]} columnas")
            print(f"   Memoria: {dataset.memory_usage(deep=True).sum() / 1024:.1f} KB")
            print(f"   Valores nulos: {dataset.isnull().sum().sum()}")
            
            # Tipos de datos
            tipos = dataset.dtypes.value_counts()
            print(f"\n   TIPOS DE DATOS:")
            for tipo, cantidad in tipos.items():
                print(f"     - {tipo}: {cantidad} columnas")
            
            # Columnas numericas
            numericas = dataset.select_dtypes(include=['number']).columns
            print(f"\n   COLUMNAS NUMERICAS: {len(numericas)}")
            for col in numericas[:5]:  # Mostrar solo las primeras 5
                print(f"     - {col}")
            if len(numericas) > 5:
                print(f"     ... y {len(numericas) - 5} mas")
            
            # Columnas categoricas
            categoricas = dataset.select_dtypes(include=['object', 'bool']).columns
            print(f"\n   COLUMNAS CATEGORICAS: {len(categoricas)}")
            for col in categoricas[:5]:  # Mostrar solo las primeras 5
                print(f"     - {col}")
            if len(categoricas) > 5:
                print(f"     ... y {len(categoricas) - 5} mas")
                
        except Exception as e:
            print(f"   Error al cargar dataset final: {e}")
    
    def mostrar_resumen_normalizacion(self):
        """Mostrar resumen de normalizacion."""
        print(f"\nRESUMEN DE NORMALIZACION:")
        print("-" * 35)
        
        # Leer archivos de normalizacion
        archivos_normalizacion = [
            "resultados/estadisticas/normalizacion_clientes.txt",
            "resultados/estadisticas/normalizacion_productos.txt",
            "resultados/estadisticas/normalizacion_ventas.txt",
            "resultados/estadisticas/normalizacion_detalle_ventas.txt"
        ]
        
        for archivo in archivos_normalizacion:
            if os.path.exists(archivo):
                nombre_tabla = archivo.split('_')[-1].replace('.txt', '')
                print(f"   {nombre_tabla.upper()}:")
                
                try:
                    with open(archivo, 'r', encoding='utf-8') as f:
                        contenido = f.read()
                        lineas = contenido.split('\n')
                        
                        # Contar outliers
                        outliers = [l for l in lineas if 'outliers' in l and 'detectados' in l]
                        if outliers:
                            print(f"     - {len(outliers)} variables con outliers tratados")
                        
                        # Contar normalizaciones
                        normalizaciones = [l for l in lineas if 'Normalizando' in l or 'Metodo:' in l]
                        if normalizaciones:
                            print(f"     - {len(normalizaciones)} variables normalizadas")
                        
                        # Contar codificaciones
                        codificaciones = [l for l in lineas if 'Codificando' in l or 'categorias' in l]
                        if codificaciones:
                            print(f"     - {len(codificaciones)} variables codificadas")
                            
                except Exception as e:
                    print(f"     - Error al leer archivo: {e}")
    
    def mostrar_recomendaciones(self):
        """Mostrar recomendaciones para el siguiente paso."""
        print(f"\nRECOMENDACIONES PARA MACHINE LEARNING:")
        print("-" * 50)
        
        print("   1. VARIABLES OBJETIVO SUGERIDAS:")
        print("      - importe: Prediccion de valor de venta")
        print("      - cantidad: Prediccion de cantidad vendida")
        print("      - categoria_cliente: Clasificacion de clientes")
        
        print("\n   2. ALGORITMOS RECOMENDADOS:")
        print("      - Regresion: Random Forest, XGBoost, Linear Regression")
        print("      - Clasificacion: Random Forest, SVM, Logistic Regression")
        print("      - Clustering: K-Means, DBSCAN")
        
        print("\n   3. PREPROCESAMIENTO ADICIONAL:")
        print("      - Feature selection (eliminar variables irrelevantes)")
        print("      - Cross-validation para evaluar modelos")
        print("      - Grid search para optimizar hiperparametros")
        
        print("\n   4. METRICAS DE EVALUACION:")
        print("      - Regresion: RMSE, MAE, R²")
        print("      - Clasificacion: Accuracy, Precision, Recall, F1-Score")
        print("      - Clustering: Silhouette Score, Inertia")
        
        print(f"\n[INFO] Dataset final listo para implementar modelos de ML!")
        print(f"[INFO] Archivos disponibles en: resultados/datasets_normalizados/")
    
    def ejecutar_resumen(self):
        """Ejecutar resumen completo."""
        self.mostrar_resumen_proyecto()

def main():
    """Funcion principal del resumen."""
    resumen = ResumenFinal()
    resumen.ejecutar_resumen()

if __name__ == "__main__":
    main()
