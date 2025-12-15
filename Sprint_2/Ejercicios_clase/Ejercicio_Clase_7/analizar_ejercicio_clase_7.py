#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ANALISIS DEL EJERCICIO CLASE 7 - PROYECTO AURELION SPRINT_2
===========================================================

**Autor:** Enith Gicela Vargas Vargas  
**Fecha:** 2025-10-27  
**Curso:** AI Fundamentals - Guayerd - IBM Skills Build  
**Sprint:** 2 - Machine Learning y Normalización  
**Módulo:** Ejercicio Clase 7  

Script para analizar y resolver el ejercicio de clase 7,
incluyendo carga de datos, analisis exploratorio y
implementacion de soluciones.
"""

import pandas as pd          # Librería para manipulación y análisis de datos estructurados
import numpy as np           # Librería para cálculos numéricos y operaciones matemáticas
import matplotlib.pyplot as plt  # Librería para crear visualizaciones y gráficos
import seaborn as sns        # Librería para visualizaciones estadísticas avanzadas
import warnings             # Módulo para controlar avisos del sistema
warnings.filterwarnings('ignore')

class AnalizadorEjercicioClase7:
    """
    Clase para analizar el ejercicio de clase 7.
    
    Funcionalidades:
    - Carga de datos del Excel
    - Analisis exploratorio
    - Implementacion de soluciones
    - Generacion de reportes
    """
    
    def __init__(self):
        """Inicializar el analizador."""
        self.datos = None
        self.resultados = {}
        
    def cargar_datos(self):
        """Cargar datos del archivo Excel."""
        print("CARGANDO DATOS DEL EJERCICIO CLASE 7")
        print("=" * 50)
        
        try:
            # Cargar archivo Excel
            self.datos = pd.read_excel("Ejercicio_clase_7.xlsx")
            
            print(f"Datos cargados exitosamente!")
            print(f"Dimensiones: {self.datos.shape[0]} filas x {self.datos.shape[1]} columnas")
            print(f"Columnas: {list(self.datos.columns)}")
            
            return True
            
        except Exception as e:
            print(f"Error al cargar datos: {e}")
            return False
    
    def mostrar_informacion_basica(self):
        """Mostrar informacion basica de los datos."""
        print("\nINFORMACION BASICA DE LOS DATOS")
        print("-" * 40)
        
        if self.datos is not None:
            print(f"Dimensiones: {self.datos.shape}")
            print(f"Tipos de datos:")
            print(self.datos.dtypes)
            
            print(f"\nPrimeras 5 filas:")
            print(self.datos.head())
            
            print(f"\nEstadisticas descriptivas:")
            print(self.datos.describe())
            
            print(f"\nValores nulos por columna:")
            print(self.datos.isnull().sum())
    
    def analizar_datos(self):
        """Analizar los datos del ejercicio."""
        print("\nANALISIS DE LOS DATOS")
        print("-" * 30)
        
        if self.datos is not None:
            # Analisis por columnas
            for col in self.datos.columns:
                print(f"\nColumna: {col}")
                print(f"  Tipo: {self.datos[col].dtype}")
                print(f"  Valores unicos: {self.datos[col].nunique()}")
                print(f"  Valores nulos: {self.datos[col].isnull().sum()}")
                
                if self.datos[col].dtype in ['int64', 'float64']:
                    print(f"  Min: {self.datos[col].min()}")
                    print(f"  Max: {self.datos[col].max()}")
                    print(f"  Media: {self.datos[col].mean():.2f}")
                else:
                    print(f"  Valores mas frecuentes:")
                    print(self.datos[col].value_counts().head())
    
    def crear_visualizaciones(self):
        """Crear visualizaciones de los datos."""
        print("\nCREANDO VISUALIZACIONES")
        print("-" * 30)
        
        if self.datos is not None:
            # Configurar estilo
            plt.style.use('default')
            sns.set_palette("husl")
            
            # Obtener columnas numericas
            columnas_numericas = self.datos.select_dtypes(include=[np.number]).columns
            
            if len(columnas_numericas) > 0:
                # Crear histogramas
                n_cols = min(3, len(columnas_numericas))
                n_rows = (len(columnas_numericas) + n_cols - 1) // n_cols
                
                fig, axes = plt.subplots(n_rows, n_cols, figsize=(5*n_cols, 4*n_rows))
                if n_rows == 1 and n_cols == 1:
                    axes = [axes]
                elif n_rows == 1:
                    axes = axes.reshape(1, -1)
                elif n_cols == 1:
                    axes = axes.reshape(-1, 1)
                
                for i, col in enumerate(columnas_numericas):
                    row = i // n_cols
                    col_idx = i % n_cols
                    
                    if n_rows == 1:
                        ax = axes[col_idx]
                    else:
                        ax = axes[row, col_idx]
                    
                    # Histograma
                    ax.hist(self.datos[col].dropna(), bins=20, alpha=0.7, color='skyblue', edgecolor='black')
                    ax.set_title(f'Distribucion de {col}', fontweight='bold')
                    ax.set_xlabel(col)
                    ax.set_ylabel('Frecuencia')
                    ax.grid(True, alpha=0.3)
                
                # Ocultar ejes vacios
                for i in range(len(columnas_numericas), n_rows * n_cols):
                    row = i // n_cols
                    col_idx = i % n_cols
                    if n_rows == 1:
                        axes[col_idx].set_visible(False)
                    else:
                        axes[row, col_idx].set_visible(False)
                
                plt.suptitle('ANALISIS DE DISTRIBUCIONES - EJERCICIO CLASE 7', 
                           fontsize=14, fontweight='bold', y=0.98)
                plt.tight_layout()
                
                # Guardar grafico
                archivo = "analisis_ejercicio_clase_7.png"
                plt.savefig(archivo, dpi=300, bbox_inches='tight')
                print(f"   Grafico guardado: {archivo}")
                plt.close()
    
    def generar_reporte(self):
        """Generar reporte del ejercicio."""
        print("\nGENERANDO REPORTE")
        print("-" * 20)
        
        try:
            archivo = "reporte_ejercicio_clase_7.txt"
            with open(archivo, 'w', encoding='utf-8') as f:
                f.write("REPORTE EJERCICIO CLASE 7\n")
                f.write("Proyecto desarrollado como parte del curso AI Fundamentals - Guayerd - IBM Skills Build\n")
                f.write("=" * 60 + "\n\n")
                
                f.write(f"INFORMACION DEL DATASET:\n")
                f.write(f"  Dimensiones: {self.datos.shape[0]} filas x {self.datos.shape[1]} columnas\n")
                f.write(f"  Columnas: {list(self.datos.columns)}\n\n")
                
                f.write("ESTADISTICAS DESCRIPTIVAS:\n")
                f.write(str(self.datos.describe()))
                f.write("\n\n")
                
                f.write("VALORES NULOS:\n")
                nulos = self.datos.isnull().sum()
                for col, nulos_count in nulos.items():
                    f.write(f"  {col}: {nulos_count}\n")
                
                f.write(f"\nTIPOS DE DATOS:\n")
                for col, tipo in self.datos.dtypes.items():
                    f.write(f"  {col}: {tipo}\n")
            
            print(f"   Reporte guardado: {archivo}")
            
        except Exception as e:
            print(f"   Error al generar reporte: {e}")
    
    def ejecutar_analisis_completo(self):
        """Ejecutar analisis completo del ejercicio."""
        print("ANALISIS EJERCICIO CLASE 7")
        print("Proyecto desarrollado como parte del curso AI Fundamentals - Guayerd - IBM Skills Build")
        print("=" * 60)
        
        # Cargar datos
        if not self.cargar_datos():
            return False
        
        # Mostrar informacion basica
        self.mostrar_informacion_basica()
        
        # Analizar datos
        self.analizar_datos()
        
        # Crear visualizaciones
        self.crear_visualizaciones()
        
        # Generar reporte
        self.generar_reporte()
        
        print(f"\n[OK] Analisis del ejercicio completado!")
        print(f"[INFO] Archivos generados en el directorio actual")
        
        return True

def main():
    """Funcion principal del analisis."""
    analizador = AnalizadorEjercicioClase7()
    analizador.ejecutar_analisis_completo()

if __name__ == "__main__":
    main()
