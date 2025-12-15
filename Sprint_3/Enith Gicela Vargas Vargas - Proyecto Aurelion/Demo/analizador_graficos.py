#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
<!--
# ANALIZADOR DE GRAFICOS - SPRINT_3
**Autor:** Enith Gicela Vargas Vargas  
**Camada:** 1  
**Grupo:** 11  
**Fecha:** 2025-11-11  
**Curso:** AI Fundamentals - Guayerd - IBM Skills Build  
**Sprint:** 3 - Machine Learning Fundamentals  
**Módulo:** Analizador de Gráficos  
-->

ANALIZADOR DE GRAFICOS - PROYECTO AURELION SPRINT_3
===================================================

Módulo para análisis automático y detallado de gráficos generados.
"""

import os               # Módulo del sistema operativo
import pandas as pd     # Módulo para manipulación de datos
import pickle           # Módulo para cargar modelos
import numpy as np      # Módulo para operaciones numéricas
from pathlib import Path  # Módulo para manejo de rutas

class AnalizadorGraficos:
    """
    Clase para análisis automático de gráficos generados.
    
    Funcionalidades:
    - Análisis detallado de gráficos
    - Interpretación de resultados
    - Conclusiones automáticas
    - Recomendaciones específicas
    """
    
    def __init__(self):
        """Inicializar el analizador de gráficos."""
        # Manejar el caso cuando se ejecuta con exec() donde __file__ no está definido
        try:
            base_path = Path(__file__).parent
        except NameError:
            base_path = Path(os.getcwd())
            if not (base_path / "analizador_graficos.py").exists():
                posibles = [
                    base_path / "Demo",
                    base_path.parent / "Demo",
                    base_path.parent.parent / "Enith Gicela Vargas Vargas - Proyecto Aurelion" / "Demo",
                ]
                for p in posibles:
                    if p.exists() and (p / "analizador_graficos.py").exists():
                        base_path = p
                        break
        
        self.resultados_dir = base_path.parent / "resultados"
        self.metricas_dir = self.resultados_dir / "metricas"
        
    def analizar_graficos(self):
        """Analizar todos los gráficos disponibles."""
        print("\nANÁLISIS DETALLADO DE GRÁFICOS")
        print("=" * 50)
        
        # Buscar archivos de imagen
        archivos_imagen = []
        for ext in ['.png', '.jpg', '.jpeg', '.svg', '.pdf']:
            archivos_imagen.extend(list(self.metricas_dir.glob(f"*{ext}")))
        
        if not archivos_imagen:
            print("No se encontraron gráficos para analizar.")
            print("Ejecuta primero la evaluación de modelos.")
            return
        
        print(f"Gráficos disponibles para análisis ({len(archivos_imagen)}):")
        for i, archivo in enumerate(archivos_imagen, 1):
            tamaño = archivo.stat().st_size
            print(f"{i}. {archivo.name} ({tamaño} bytes)")
        
        print(f"\n{len(archivos_imagen) + 1}. Análisis completo de todos los gráficos")
        print(f"{len(archivos_imagen) + 2}. Ver análisis del gráfico principal")
        print(f"{len(archivos_imagen) + 3}. Volver al menú principal")
        
        try:
            opcion = input(f"\nSelecciona una opción (1-{len(archivos_imagen) + 3}): ").strip()
            
            if opcion.isdigit():
                opcion_num = int(opcion)
                
                if 1 <= opcion_num <= len(archivos_imagen):
                    # Analizar gráfico específico
                    archivo_seleccionado = archivos_imagen[opcion_num - 1]
                    self._analizar_grafico_especifico(archivo_seleccionado)
                    
                elif opcion_num == len(archivos_imagen) + 1:
                    # Análisis completo
                    self._analisis_completo()
                    
                elif opcion_num == len(archivos_imagen) + 2:
                    # Análisis del gráfico principal
                    self._analizar_predicciones_vs_reales()
                    
                elif opcion_num == len(archivos_imagen) + 3:
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
    
    def _analizar_grafico_especifico(self, archivo_grafico):
        """Analizar un gráfico específico."""
        print(f"\nANÁLISIS DE: {archivo_grafico.name}")
        print("=" * 50)
        
        # Análisis basado en el nombre del archivo
        if "predicciones_vs_reales" in archivo_grafico.name.lower():
            self._analizar_predicciones_vs_reales()
        elif "correlacion" in archivo_grafico.name.lower():
            self._analizar_correlacion()
        elif "distribucion" in archivo_grafico.name.lower():
            self._analizar_distribucion()
        else:
            self._analizar_grafico_generico(archivo_grafico)
    
    def _analizar_predicciones_vs_reales(self):
        """Análisis detallado del gráfico predicciones vs reales."""
        print("\nANÁLISIS DETALLADO: PREDICCIONES VS VALORES REALES")
        print("=" * 60)
        
        print("DESCRIPCIÓN DEL GRÁFICO:")
        print("-" * 30)
        print("• Tipo: Gráfico de dispersión (Scatter Plot) 2x2")
        print("• Contenido: Comparación de predicciones vs valores reales")
        print("• Modelos: Linear Regression, Random Forest, SVR")
        print("• Línea roja: y=x (predicción perfecta)")
        
        # Cargar datos para análisis cuantitativo
        try:
            X_test = pd.read_csv(self.resultados_dir / "X_test.csv")
            y_test = pd.read_csv(self.resultados_dir / "y_test.csv")
            
            print(f"\nDATOS DEL ANÁLISIS:")
            print("-" * 20)
            print(f"• Muestras de prueba: {X_test.shape[0]}")
            print(f"• Características: {X_test.shape[1]}")
            print(f"• Rango de valores reales: {y_test.iloc[:, 0].min():.2f} - {y_test.iloc[:, 0].max():.2f}")
            
            # Evaluar cada modelo
            modelos = [
                ("Linear Regression", "linear_regression.pkl"),
                ("Random Forest Regressor", "random_forest_regressor.pkl"),
                ("SVR", "svr.pkl")
            ]
            
            print(f"\nANÁLISIS POR MODELO:")
            print("-" * 25)
            
            for nombre, archivo in modelos:
                try:
                    with open(self.resultados_dir / "modelos" / archivo, 'rb') as f:
                        modelo = pickle.load(f)
                    
                    predicciones = modelo.predict(X_test)
                    
                    # Calcular R²
                    ss_res = np.sum((y_test.iloc[:, 0] - predicciones) ** 2)
                    ss_tot = np.sum((y_test.iloc[:, 0] - y_test.iloc[:, 0].mean()) ** 2)
                    r2 = 1 - (ss_res / ss_tot) if ss_tot != 0 else 0
                    
                    # Calcular otras métricas
                    mse = np.mean((predicciones - y_test.iloc[:, 0]) ** 2)
                    mae = np.mean(np.abs(predicciones - y_test.iloc[:, 0]))
                    
                    print(f"\n{nombre.upper()}:")
                    print(f"  R² Score: {r2:.4f}")
                    print(f"  MSE: {mse:.2f}")
                    print(f"  MAE: {mae:.2f}")
                    print(f"  Rango predicciones: {predicciones.min():.2f} - {predicciones.max():.2f}")
                    
                    # Interpretación
                    if r2 > 0.7:
                        interpretacion = "Excelente rendimiento"
                    elif r2 > 0.5:
                        interpretacion = "Buen rendimiento"
                    elif r2 > 0.2:
                        interpretacion = "Rendimiento moderado"
                    elif r2 > 0:
                        interpretacion = "Rendimiento limitado"
                    else:
                        interpretacion = "Rendimiento muy pobre"
                    
                    print(f"  Interpretación: {interpretacion}")
                    
                except Exception as e:
                    print(f"\n{nombre.upper()}: Error al analizar - {e}")
            
            # Análisis comparativo
            print(f"\nANÁLISIS COMPARATIVO:")
            print("-" * 25)
            
            # Encontrar mejor modelo
            mejor_r2 = -float('inf')
            mejor_modelo = None
            
            for nombre, archivo in modelos:
                try:
                    with open(self.resultados_dir / "modelos" / archivo, 'rb') as f:
                        modelo = pickle.load(f)
                    
                    predicciones = modelo.predict(X_test)
                    ss_res = np.sum((y_test.iloc[:, 0] - predicciones) ** 2)
                    ss_tot = np.sum((y_test.iloc[:, 0] - y_test.iloc[:, 0].mean()) ** 2)
                    r2 = 1 - (ss_res / ss_tot) if ss_tot != 0 else 0
                    
                    if r2 > mejor_r2:
                        mejor_r2 = r2
                        mejor_modelo = nombre
                        
                except:
                    continue
            
            if mejor_modelo:
                print(f"• Mejor modelo: {mejor_modelo} (R² = {mejor_r2:.4f})")
                print(f"• Explica el {mejor_r2*100:.1f}% de la varianza")
                
                if mejor_r2 < 0.3:
                    print("• Rendimiento limitado - necesita mejoras")
                elif mejor_r2 < 0.6:
                    print("• Rendimiento moderado - aceptable para análisis")
                else:
                    print("• Rendimiento bueno - confiable para predicciones")
            
            # Conclusiones y recomendaciones
            print(f"\nCONCLUSIONES Y RECOMENDACIONES:")
            print("-" * 35)
            print("1. ANÁLISIS GENERAL:")
            print("   • Los gráficos muestran el rendimiento real de cada modelo")
            print("   • La línea roja (y=x) representa predicción perfecta")
            print("   • Puntos cerca de la línea = predicciones precisas")
            print("   • Puntos dispersos = predicciones imprecisas")
            
            print("\n2. INTERPRETACIÓN VISUAL:")
            print("   • Linear Regression: Dispersión moderada con tendencia positiva")
            print("   • Random Forest: Dispersión alta sin patrón claro")
            print("   • SVR: Agrupación horizontal (predicción constante)")
            
            print("\n3. RECOMENDACIONES:")
            print("   • Usar Linear Regression como modelo principal")
            print("   • Recopilar más datos para mejorar rendimiento")
            print("   • Considerar ingeniería de características adicionales")
            print("   • Tuning de hiperparámetros para Random Forest y SVR")
            
        except Exception as e:
            print(f"[ERROR] Error cargando datos: {e}")
            print("Análisis basado solo en información del archivo.")
    
    def _analizar_correlacion(self):
        """Análisis de gráficos de correlación."""
        print("\nANÁLISIS DE GRÁFICOS DE CORRELACIÓN")
        print("=" * 40)
        print("• Los gráficos de correlación muestran relaciones entre variables")
        print("• Colores cálidos (rojo) = correlación positiva fuerte")
        print("• Colores fríos (azul) = correlación negativa fuerte")
        print("• Colores neutros = correlación débil")
        print("• Valores cercanos a 1 o -1 = correlación fuerte")
        print("• Valores cercanos a 0 = correlación débil")
    
    def _analizar_distribucion(self):
        """Análisis de gráficos de distribución."""
        print("\nANÁLISIS DE GRÁFICOS DE DISTRIBUCIÓN")
        print("=" * 40)
        print("• Los histogramas muestran la frecuencia de valores")
        print("• Distribución normal = forma de campana simétrica")
        print("• Distribución sesgada = cola larga en un lado")
        print("• Múltiples picos = distribución multimodal")
        print("• Ancho de barras = rango de valores")
        print("• Altura de barras = frecuencia de ocurrencia")
    
    def _analizar_grafico_generico(self, archivo_grafico):
        """Análisis genérico para gráficos no específicos."""
        print(f"\nANÁLISIS GENÉRICO: {archivo_grafico.name}")
        print("=" * 50)
        
        tamaño = archivo_grafico.stat().st_size
        print(f"• Archivo: {archivo_grafico.name}")
        print(f"• Tamaño: {tamaño} bytes")
        print(f"• Ubicación: {archivo_grafico.absolute()}")
        
        print(f"\nINFORMACIÓN GENERAL:")
        print("-" * 20)
        print("• Este gráfico fue generado por el sistema de evaluación")
        print("• Contiene información visual sobre el análisis de datos")
        print("• Puede mostrar métricas, comparaciones o distribuciones")
        print("• Es parte del conjunto de resultados de Sprint_3")
        
        print(f"\nCÓMO INTERPRETAR:")
        print("-" * 18)
        print("• Ejes X e Y: Variables comparadas")
        print("• Colores: Diferentes categorías o valores")
        print("• Formas: Tipos de datos o modelos")
        print("• Tamaños: Magnitudes o frecuencias")
        print("• Patrones: Tendencias o relaciones")
    
    def _analisis_completo(self):
        """Análisis completo de todos los gráficos."""
        print(f"\nANÁLISIS COMPLETO DE TODOS LOS GRÁFICOS")
        print("=" * 50)
        
        # Buscar todos los gráficos
        archivos_imagen = []
        for ext in ['.png', '.jpg', '.jpeg', '.svg', '.pdf']:
            archivos_imagen.extend(list(self.metricas_dir.glob(f"*{ext}")))
        
        if not archivos_imagen:
            print("No se encontraron gráficos para análisis completo.")
            return
        
        print(f"Gráficos encontrados: {len(archivos_imagen)}")
        
        # Análisis de cada gráfico
        for i, archivo in enumerate(archivos_imagen, 1):
            print(f"\n{i}. {archivo.name}")
            print("-" * 30)
            
            tamaño = archivo.stat().st_size
            print(f"Tamaño: {tamaño} bytes")
            
            # Análisis específico basado en nombre
            if "predicciones_vs_reales" in archivo.name.lower():
                print("Tipo: Gráfico de evaluación de modelos")
                print("Contenido: Comparación predicciones vs valores reales")
                print("Modelos: Linear Regression, Random Forest, SVR")
            elif "correlacion" in archivo.name.lower():
                print("Tipo: Matriz de correlación")
                print("Contenido: Relaciones entre variables")
            elif "distribucion" in archivo.name.lower():
                print("Tipo: Histograma de distribución")
                print("Contenido: Frecuencia de valores")
            else:
                print("Tipo: Gráfico de análisis de datos")
                print("Contenido: Visualización de métricas o resultados")
        
        # Resumen general
        print(f"\nRESUMEN GENERAL:")
        print("-" * 20)
        print(f"• Total de gráficos: {len(archivos_imagen)}")
        print(f"• Tamaño total: {sum(f.stat().st_size for f in archivos_imagen)} bytes")
        print(f"• Ubicación: {self.metricas_dir.absolute()}")
        
        print(f"\nCONCLUSIONES GENERALES:")
        print("-" * 25)
        print("• Los gráficos proporcionan visualización de resultados")
        print("• Facilitan la interpretación de métricas de ML")
        print("• Son herramientas educativas valiosas")
        print("• Demuestran el rendimiento de los modelos entrenados")
        print("• Guían decisiones sobre mejoras futuras")

def main():
    """Función principal para pruebas."""
    analizador = AnalizadorGraficos()
    
    print("ANALIZADOR DE GRAFICOS - PROYECTO AURELION")
    print("Grupo 11 - Camada 1 | Enith Gicela Vargas Vargas")
    print("=" * 60)
    
    analizador.analizar_graficos()

if __name__ == "__main__":
    main()
