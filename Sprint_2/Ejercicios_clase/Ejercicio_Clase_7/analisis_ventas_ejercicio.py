#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ANALISIS DE VENTAS - EJERCICIO CLASE 7 - PROYECTO AURELION SPRINT_2
====================================================================

**Autor:** Enith Gicela Vargas Vargas  
**Fecha:** 2025-10-27  
**Curso:** AI Fundamentals - Guayerd - IBM Skills Build  
**Sprint:** 2 - Machine Learning y Normalización  
**Módulo:** Ejercicio Clase 7 - Análisis de Ventas  

Script para analizar los datos de ventas mensuales,
incluyendo metricas de rendimiento, correlaciones
y visualizaciones de tendencias.
"""

import pandas as pd          # Librería para manipulación y análisis de datos estructurados
import numpy as np           # Librería para cálculos numéricos y operaciones matemáticas
import matplotlib.pyplot as plt  # Librería para crear visualizaciones y gráficos
import seaborn as sns        # Librería para visualizaciones estadísticas avanzadas
import warnings             # Módulo para controlar avisos del sistema
warnings.filterwarnings('ignore')

class AnalisisVentas:
    """
    Clase para analizar datos de ventas.
    
    Funcionalidades:
    - Limpieza y preparacion de datos
    - Calculo de metricas de rendimiento
    - Analisis de correlaciones
    - Visualizaciones de tendencias
    """
    
    def __init__(self):
        """Inicializar el analizador."""
        self.datos_originales = None
        self.datos_limpios = None
        self.metricas = {}
        
    def cargar_y_limpiar_datos(self):
        """Cargar y limpiar los datos del Excel."""
        print("CARGANDO Y LIMPIANDO DATOS DE VENTAS")
        print("=" * 50)
        
        try:
            # Cargar datos
            self.datos_originales = pd.read_excel("Ejercicio_clase_7.xlsx")
            
            # Limpiar datos - usar la primera fila como encabezados
            datos_limpios = self.datos_originales.copy()
            
            # Renombrar columnas usando la primera fila
            nuevos_nombres = {
                'Unnamed: 0': 'Mes',
                'Unnamed: 1': 'Ventas',
                'Unnamed: 2': 'Visitantes',
                'Unnamed: 3': 'Conversion',
                'Unnamed: 4': 'Gasto_Publicidad',
                'Unnamed: 5': 'Productos_Vendidos'
            }
            
            datos_limpios = datos_limpios.rename(columns=nuevos_nombres)
            
            # Eliminar la primera fila (encabezados)
            datos_limpios = datos_limpios.drop(0).reset_index(drop=True)
            
            # Convertir tipos de datos
            datos_limpios['Ventas'] = pd.to_numeric(datos_limpios['Ventas'])
            datos_limpios['Visitantes'] = pd.to_numeric(datos_limpios['Visitantes'])
            datos_limpios['Conversion'] = pd.to_numeric(datos_limpios['Conversion'])
            datos_limpios['Gasto_Publicidad'] = pd.to_numeric(datos_limpios['Gasto_Publicidad'])
            datos_limpios['Productos_Vendidos'] = pd.to_numeric(datos_limpios['Productos_Vendidos'])
            
            self.datos_limpios = datos_limpios
            
            print("Datos limpiados exitosamente!")
            print(f"Dimensiones: {self.datos_limpios.shape}")
            print(f"Columnas: {list(self.datos_limpios.columns)}")
            print(f"\nDatos limpios:")
            print(self.datos_limpios)
            
            return True
            
        except Exception as e:
            print(f"Error al cargar y limpiar datos: {e}")
            return False
    
    def calcular_metricas_rendimiento(self):
        """Calcular metricas de rendimiento."""
        print("\nCALCULANDO METRICAS DE RENDIMIENTO")
        print("-" * 40)
        
        if self.datos_limpios is not None:
            # Metricas basicas
            self.metricas['ventas_totales'] = self.datos_limpios['Ventas'].sum()
            self.metricas['ventas_promedio'] = self.datos_limpios['Ventas'].mean()
            self.metricas['ventas_max'] = self.datos_limpios['Ventas'].max()
            self.metricas['ventas_min'] = self.datos_limpios['Ventas'].min()
            
            # Metricas de conversion
            self.metricas['conversion_promedio'] = self.datos_limpios['Conversion'].mean()
            self.metricas['conversion_max'] = self.datos_limpios['Conversion'].max()
            self.metricas['conversion_min'] = self.datos_limpios['Conversion'].min()
            
            # Metricas de visitantes
            self.metricas['visitantes_totales'] = self.datos_limpios['Visitantes'].sum()
            self.metricas['visitantes_promedio'] = self.datos_limpios['Visitantes'].mean()
            
            # Metricas de gasto publicitario
            self.metricas['gasto_publicidad_total'] = self.datos_limpios['Gasto_Publicidad'].sum()
            self.metricas['gasto_publicidad_promedio'] = self.datos_limpios['Gasto_Publicidad'].mean()
            
            # ROI (Return on Investment)
            self.metricas['roi'] = (self.metricas['ventas_totales'] - self.metricas['gasto_publicidad_total']) / self.metricas['gasto_publicidad_total']
            
            # Costo por adquisicion (CPA)
            self.metricas['cpa'] = self.metricas['gasto_publicidad_total'] / self.metricas['visitantes_totales']
            
            # Valor por visitante
            self.metricas['valor_por_visitante'] = self.metricas['ventas_totales'] / self.metricas['visitantes_totales']
            
            print("Metricas calculadas:")
            for metrica, valor in self.metricas.items():
                if isinstance(valor, float):
                    print(f"  {metrica}: ${valor:,.2f}" if 'ventas' in metrica or 'gasto' in metrica or 'valor' in metrica or 'cpa' in metrica else f"  {metrica}: {valor:.2f}%")
                else:
                    print(f"  {metrica}: {valor:,}")
    
    def analizar_correlaciones(self):
        """Analizar correlaciones entre variables."""
        print("\nANALISIS DE CORRELACIONES")
        print("-" * 30)
        
        if self.datos_limpios is not None:
            # Seleccionar solo variables numericas
            variables_numericas = ['Ventas', 'Visitantes', 'Conversion', 'Gasto_Publicidad', 'Productos_Vendidos']
            datos_numericos = self.datos_limpios[variables_numericas]
            
            # Calcular matriz de correlacion
            correlaciones = datos_numericos.corr()
            
            print("Matriz de correlaciones:")
            print(correlaciones.round(3))
            
            # Encontrar correlaciones fuertes
            print(f"\nCorrelaciones fuertes (|r| > 0.7):")
            for i in range(len(correlaciones.columns)):
                for j in range(i+1, len(correlaciones.columns)):
                    corr_val = correlaciones.iloc[i, j]
                    if abs(corr_val) > 0.7:
                        print(f"  {correlaciones.columns[i]} vs {correlaciones.columns[j]}: {corr_val:.3f}")
    
    def crear_visualizaciones(self):
        """Crear visualizaciones de los datos."""
        print("\nCREANDO VISUALIZACIONES")
        print("-" * 30)
        
        if self.datos_limpios is not None:
            # Configurar estilo
            plt.style.use('default')
            sns.set_palette("husl")
            
            # Crear figura con subplots
            fig, axes = plt.subplots(2, 3, figsize=(18, 12))
            
            # 1. Grafico de ventas por mes
            axes[0, 0].bar(self.datos_limpios['Mes'], self.datos_limpios['Ventas'], 
                          color='skyblue', alpha=0.8, edgecolor='black')
            axes[0, 0].set_title('Ventas por Mes', fontweight='bold', fontsize=12)
            axes[0, 0].set_ylabel('Ventas ($)')
            axes[0, 0].tick_params(axis='x', rotation=45)
            axes[0, 0].grid(True, alpha=0.3)
            
            # 2. Grafico de visitantes por mes
            axes[0, 1].bar(self.datos_limpios['Mes'], self.datos_limpios['Visitantes'], 
                          color='lightcoral', alpha=0.8, edgecolor='black')
            axes[0, 1].set_title('Visitantes por Mes', fontweight='bold', fontsize=12)
            axes[0, 1].set_ylabel('Visitantes')
            axes[0, 1].tick_params(axis='x', rotation=45)
            axes[0, 1].grid(True, alpha=0.3)
            
            # 3. Grafico de conversion por mes
            axes[0, 2].bar(self.datos_limpios['Mes'], self.datos_limpios['Conversion'], 
                          color='lightgreen', alpha=0.8, edgecolor='black')
            axes[0, 2].set_title('Tasa de Conversion por Mes', fontweight='bold', fontsize=12)
            axes[0, 2].set_ylabel('Conversion (%)')
            axes[0, 2].tick_params(axis='x', rotation=45)
            axes[0, 2].grid(True, alpha=0.3)
            
            # 4. Grafico de gasto publicitario por mes
            axes[1, 0].bar(self.datos_limpios['Mes'], self.datos_limpios['Gasto_Publicidad'], 
                          color='orange', alpha=0.8, edgecolor='black')
            axes[1, 0].set_title('Gasto Publicitario por Mes', fontweight='bold', fontsize=12)
            axes[1, 0].set_ylabel('Gasto Publicidad ($)')
            axes[1, 0].tick_params(axis='x', rotation=45)
            axes[1, 0].grid(True, alpha=0.3)
            
            # 5. Grafico de productos vendidos por mes
            axes[1, 1].bar(self.datos_limpios['Mes'], self.datos_limpios['Productos_Vendidos'], 
                          color='purple', alpha=0.8, edgecolor='black')
            axes[1, 1].set_title('Productos Vendidos por Mes', fontweight='bold', fontsize=12)
            axes[1, 1].set_ylabel('Productos Vendidos')
            axes[1, 1].tick_params(axis='x', rotation=45)
            axes[1, 1].grid(True, alpha=0.3)
            
            # 6. Matriz de correlacion
            variables_numericas = ['Ventas', 'Visitantes', 'Conversion', 'Gasto_Publicidad', 'Productos_Vendidos']
            datos_numericos = self.datos_limpios[variables_numericas]
            correlaciones = datos_numericos.corr()
            
            im = axes[1, 2].imshow(correlaciones, cmap='coolwarm', vmin=-1, vmax=1)
            axes[1, 2].set_title('Matriz de Correlaciones', fontweight='bold', fontsize=12)
            axes[1, 2].set_xticks(range(len(correlaciones.columns)))
            axes[1, 2].set_yticks(range(len(correlaciones.columns)))
            axes[1, 2].set_xticklabels(correlaciones.columns, rotation=45, ha='right')
            axes[1, 2].set_yticklabels(correlaciones.columns)
            
            # Agregar valores en la matriz
            for i in range(len(correlaciones.columns)):
                for j in range(len(correlaciones.columns)):
                    text = axes[1, 2].text(j, i, f'{correlaciones.iloc[i, j]:.2f}',
                                         ha="center", va="center", color="black", fontweight='bold')
            
            plt.colorbar(im, ax=axes[1, 2])
            
            plt.suptitle('ANALISIS COMPLETO DE VENTAS - EJERCICIO CLASE 7', 
                        fontsize=16, fontweight='bold', y=0.98)
            plt.tight_layout()
            
            # Guardar grafico
            archivo = "analisis_completo_ventas.png"
            plt.savefig(archivo, dpi=300, bbox_inches='tight')
            print(f"   Grafico guardado: {archivo}")
            plt.close()
    
    def generar_reporte_final(self):
        """Generar reporte final del analisis."""
        print("\nGENERANDO REPORTE FINAL")
        print("-" * 30)
        
        try:
            archivo = "reporte_final_ventas.txt"
            with open(archivo, 'w', encoding='utf-8') as f:
                f.write("REPORTE FINAL - ANALISIS DE VENTAS\n")
                f.write("Proyecto desarrollado como parte del curso AI Fundamentals - Guayerd - IBM Skills Build\n")
                f.write("=" * 70 + "\n\n")
                
                f.write("DATOS ANALIZADOS:\n")
                f.write(f"  Periodo: {len(self.datos_limpios)} meses\n")
                f.write(f"  Meses: {', '.join(self.datos_limpios['Mes'].tolist())}\n\n")
                
                f.write("METRICAS DE RENDIMIENTO:\n")
                f.write("-" * 30 + "\n")
                for metrica, valor in self.metricas.items():
                    if isinstance(valor, float):
                        if 'ventas' in metrica or 'gasto' in metrica or 'valor' in metrica or 'cpa' in metrica:
                            f.write(f"  {metrica.replace('_', ' ').title()}: ${valor:,.2f}\n")
                        else:
                            f.write(f"  {metrica.replace('_', ' ').title()}: {valor:.2f}%\n")
                    else:
                        f.write(f"  {metrica.replace('_', ' ').title()}: {valor:,}\n")
                
                f.write(f"\nANALISIS DE TENDENCIAS:\n")
                f.write("-" * 25 + "\n")
                
                # Analizar tendencias
                ventas_crecimiento = ((self.datos_limpios['Ventas'].iloc[-1] - self.datos_limpios['Ventas'].iloc[0]) / self.datos_limpios['Ventas'].iloc[0]) * 100
                f.write(f"  Crecimiento de ventas: {ventas_crecimiento:.1f}%\n")
                
                mejor_mes = self.datos_limpios.loc[self.datos_limpios['Ventas'].idxmax()]
                f.write(f"  Mejor mes: {mejor_mes['Mes']} (${mejor_mes['Ventas']:,})\n")
                
                peor_mes = self.datos_limpios.loc[self.datos_limpios['Ventas'].idxmin()]
                f.write(f"  Peor mes: {peor_mes['Mes']} (${peor_mes['Ventas']:,})\n")
                
                f.write(f"\nRECOMENDACIONES:\n")
                f.write("-" * 20 + "\n")
                f.write("1. Analizar factores que contribuyeron al mejor mes\n")
                f.write("2. Identificar causas del peor rendimiento\n")
                f.write("3. Optimizar gasto publicitario basado en ROI\n")
                f.write("4. Mejorar tasa de conversion\n")
                f.write("5. Aumentar numero de visitantes\n")
                
                f.write(f"\n---\n")
                f.write("Proyecto desarrollado como parte del curso AI Fundamentals - Guayerd - IBM Skills Build\n")
                f.write("Autor: Enith Gicela Vargas Vargas\n")
            
            print(f"   Reporte final guardado: {archivo}")
            
        except Exception as e:
            print(f"   Error al generar reporte final: {e}")
    
    def ejecutar_analisis_completo(self):
        """Ejecutar analisis completo de ventas."""
        print("ANALISIS DE VENTAS - EJERCICIO CLASE 7")
        print("Proyecto desarrollado como parte del curso AI Fundamentals - Guayerd - IBM Skills Build")
        print("=" * 70)
        
        # Cargar y limpiar datos
        if not self.cargar_y_limpiar_datos():
            return False
        
        # Calcular metricas
        self.calcular_metricas_rendimiento()
        
        # Analizar correlaciones
        self.analizar_correlaciones()
        
        # Crear visualizaciones
        self.crear_visualizaciones()
        
        # Generar reporte final
        self.generar_reporte_final()
        
        print(f"\n[OK] Analisis de ventas completado exitosamente!")
        print(f"[INFO] Archivos generados en el directorio actual")
        
        return True

def main():
    """Funcion principal del analisis."""
    analizador = AnalisisVentas()
    analizador.ejecutar_analisis_completo()

if __name__ == "__main__":
    main()
