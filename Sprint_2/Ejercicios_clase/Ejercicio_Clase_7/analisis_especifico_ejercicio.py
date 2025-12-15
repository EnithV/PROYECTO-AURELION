#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ANALISIS ESPECIFICO - EJERCICIO CLASE 7 - PROYECTO AURELION SPRINT_2
=====================================================================

**Autor:** Enith Gicela Vargas Vargas  
**Fecha:** 2025-10-27  
**Curso:** AI Fundamentals - Guayerd - IBM Skills Build  
**Sprint:** 2 - Machine Learning y Normalización  
**Módulo:** Ejercicio Clase 7 - Análisis Específico  

Script para analisis especifico del ejercicio de clase 7,
incluyendo:
1. Identificar mes con mayor eficiencia (ventas/gasto publicidad)
2. Determinar mes con mejor tasa de conversion y analizar causa
3. Calcular ticket promedio (ventas/productos) por mes
4. Evaluar relacion entre visitantes y ventas

Autor: Enith Gicela Vargas Vargas
Fecha: 2025
Curso: AI Fundamentals - Guayerd - IBM Skills Build
Proyecto desarrollado como parte del curso AI Fundamentals - Guayerd - IBM Skills Build
"""

import pandas as pd          # Librería para manipulación y análisis de datos estructurados
import numpy as np           # Librería para cálculos numéricos y operaciones matemáticas
import matplotlib.pyplot as plt  # Librería para crear visualizaciones y gráficos
import seaborn as sns        # Librería para visualizaciones estadísticas avanzadas
import warnings             # Módulo para controlar avisos del sistema
warnings.filterwarnings('ignore')

class AnalisisEspecificoEjercicio:
    """
    Clase para analisis especifico del ejercicio.
    
    Funcionalidades:
    - Eficiencia publicitaria por mes
    - Analisis de tasa de conversion
    - Calculo de ticket promedio
    - Relacion visitantes-ventas
    """
    
    def __init__(self):
        """Inicializar el analizador."""
        self.datos = None
        self.resultados = {}
        
    def cargar_datos(self):
        """Cargar y limpiar datos."""
        print("CARGANDO DATOS PARA ANALISIS ESPECIFICO")
        print("=" * 50)
        
        try:
            # Cargar datos
            datos_originales = pd.read_excel("Ejercicio_clase_7.xlsx")
            
            # Limpiar datos
            datos_limpios = datos_originales.copy()
            nuevos_nombres = {
                'Unnamed: 0': 'Mes',
                'Unnamed: 1': 'Ventas',
                'Unnamed: 2': 'Visitantes',
                'Unnamed: 3': 'Conversion',
                'Unnamed: 4': 'Gasto_Publicidad',
                'Unnamed: 5': 'Productos_Vendidos'
            }
            
            datos_limpios = datos_limpios.rename(columns=nuevos_nombres)
            datos_limpios = datos_limpios.drop(0).reset_index(drop=True)
            
            # Convertir tipos
            datos_limpios['Ventas'] = pd.to_numeric(datos_limpios['Ventas'])
            datos_limpios['Visitantes'] = pd.to_numeric(datos_limpios['Visitantes'])
            datos_limpios['Conversion'] = pd.to_numeric(datos_limpios['Conversion'])
            datos_limpios['Gasto_Publicidad'] = pd.to_numeric(datos_limpios['Gasto_Publicidad'])
            datos_limpios['Productos_Vendidos'] = pd.to_numeric(datos_limpios['Productos_Vendidos'])
            
            self.datos = datos_limpios
            
            print("Datos cargados exitosamente!")
            print(f"Dimensiones: {self.datos.shape}")
            print(f"\nDatos:")
            print(self.datos)
            
            return True
            
        except Exception as e:
            print(f"Error al cargar datos: {e}")
            return False
    
    def analizar_eficiencia_publicitaria(self):
        """1. Identificar mes con mayor eficiencia (ventas/gasto publicidad)."""
        print("\n" + "="*60)
        print("1. ANALISIS DE EFICIENCIA PUBLICITARIA")
        print("="*60)
        
        if self.datos is not None:
            # Calcular eficiencia = Ventas / Gasto Publicidad
            self.datos['Eficiencia_Publicitaria'] = self.datos['Ventas'] / self.datos['Gasto_Publicidad']
            
            print("Eficiencia Publicitaria por Mes:")
            print("-" * 40)
            for _, row in self.datos.iterrows():
                print(f"  {row['Mes']}: ${row['Ventas']:,} / ${row['Gasto_Publicidad']:,} = {row['Eficiencia_Publicitaria']:.2f}")
            
            # Encontrar mes con mayor eficiencia
            mejor_eficiencia_idx = self.datos['Eficiencia_Publicitaria'].idxmax()
            mejor_eficiencia = self.datos.loc[mejor_eficiencia_idx]
            
            print(f"\n[RESULTADO]")
            print(f"   Mes con MAYOR eficiencia: {mejor_eficiencia['Mes']}")
            print(f"   Eficiencia: {mejor_eficiencia['Eficiencia_Publicitaria']:.2f}")
            print(f"   Ventas: ${mejor_eficiencia['Ventas']:,}")
            print(f"   Gasto Publicidad: ${mejor_eficiencia['Gasto_Publicidad']:,}")
            
            self.resultados['mejor_eficiencia'] = {
                'mes': mejor_eficiencia['Mes'],
                'eficiencia': mejor_eficiencia['Eficiencia_Publicitaria'],
                'ventas': mejor_eficiencia['Ventas'],
                'gasto': mejor_eficiencia['Gasto_Publicidad']
            }
    
    def analizar_tasa_conversion(self):
        """2. Determinar mes con mejor tasa de conversion y analizar causa."""
        print("\n" + "="*60)
        print("2. ANALISIS DE TASA DE CONVERSION")
        print("="*60)
        
        if self.datos is not None:
            print("Tasa de Conversion por Mes:")
            print("-" * 35)
            for _, row in self.datos.iterrows():
                print(f"  {row['Mes']}: {row['Conversion']}%")
            
            # Encontrar mes con mejor conversion
            mejor_conversion_idx = self.datos['Conversion'].idxmax()
            mejor_conversion = self.datos.loc[mejor_conversion_idx]
            
            print(f"\n[RESULTADO]")
            print(f"   Mes con MEJOR tasa de conversion: {mejor_conversion['Mes']}")
            print(f"   Tasa de conversion: {mejor_conversion['Conversion']}%")
            
            # Analizar causa - comparar con otros meses
            print(f"\n[ANALISIS DE CAUSA]")
            print(f"   Ventas en {mejor_conversion['Mes']}: ${mejor_conversion['Ventas']:,}")
            print(f"   Visitantes en {mejor_conversion['Mes']}: {mejor_conversion['Visitantes']:,}")
            print(f"   Gasto publicidad en {mejor_conversion['Mes']}: ${mejor_conversion['Gasto_Publicidad']:,}")
            
            # Comparar con promedio
            conversion_promedio = self.datos['Conversion'].mean()
            print(f"\n   Comparacion con promedio:")
            print(f"   - Conversion promedio: {conversion_promedio:.2f}%")
            print(f"   - Diferencia: {mejor_conversion['Conversion'] - conversion_promedio:.2f}%")
            
            # Analizar factores
            print(f"\n[FACTORES QUE CONTRIBUYERON]")
            if mejor_conversion['Visitantes'] > self.datos['Visitantes'].mean():
                print(f"   [OK] Mayor numero de visitantes ({mejor_conversion['Visitantes']:,} vs promedio {self.datos['Visitantes'].mean():.0f})")
            else:
                print(f"   [NO] Menor numero de visitantes ({mejor_conversion['Visitantes']:,} vs promedio {self.datos['Visitantes'].mean():.0f})")
            
            if mejor_conversion['Gasto_Publicidad'] > self.datos['Gasto_Publicidad'].mean():
                print(f"   [OK] Mayor gasto publicitario (${mejor_conversion['Gasto_Publicidad']:,} vs promedio ${self.datos['Gasto_Publicidad'].mean():.0f})")
            else:
                print(f"   [NO] Menor gasto publicitario (${mejor_conversion['Gasto_Publicidad']:,} vs promedio ${self.datos['Gasto_Publicidad'].mean():.0f})")
            
            self.resultados['mejor_conversion'] = {
                'mes': mejor_conversion['Mes'],
                'conversion': mejor_conversion['Conversion'],
                'ventas': mejor_conversion['Ventas'],
                'visitantes': mejor_conversion['Visitantes'],
                'gasto': mejor_conversion['Gasto_Publicidad']
            }
    
    def calcular_ticket_promedio(self):
        """3. Calcular ticket promedio (ventas/productos) por mes."""
        print("\n" + "="*60)
        print("3. CALCULO DE TICKET PROMEDIO")
        print("="*60)
        
        if self.datos is not None:
            # Calcular ticket promedio = Ventas / Productos Vendidos
            self.datos['Ticket_Promedio'] = self.datos['Ventas'] / self.datos['Productos_Vendidos']
            
            print("Ticket Promedio por Mes:")
            print("-" * 30)
            for _, row in self.datos.iterrows():
                print(f"  {row['Mes']}: ${row['Ventas']:,} / {row['Productos_Vendidos']} = ${row['Ticket_Promedio']:.2f}")
            
            # Estadisticas del ticket promedio
            ticket_promedio_general = self.datos['Ticket_Promedio'].mean()
            ticket_max = self.datos['Ticket_Promedio'].max()
            ticket_min = self.datos['Ticket_Promedio'].min()
            
            print(f"\n[ESTADISTICAS DEL TICKET PROMEDIO]")
            print(f"   Ticket promedio general: ${ticket_promedio_general:.2f}")
            print(f"   Ticket mas alto: ${ticket_max:.2f}")
            print(f"   Ticket mas bajo: ${ticket_min:.2f}")
            
            # Mes con mayor ticket
            mayor_ticket_idx = self.datos['Ticket_Promedio'].idxmax()
            mayor_ticket = self.datos.loc[mayor_ticket_idx]
            
            print(f"\n[RESULTADO]")
            print(f"   Mes con MAYOR ticket promedio: {mayor_ticket['Mes']}")
            print(f"   Ticket promedio: ${mayor_ticket['Ticket_Promedio']:.2f}")
            
            self.resultados['ticket_promedio'] = {
                'general': ticket_promedio_general,
                'maximo': ticket_max,
                'minimo': ticket_min,
                'mes_mayor_ticket': mayor_ticket['Mes'],
                'valor_mayor_ticket': mayor_ticket['Ticket_Promedio']
            }
    
    def evaluar_relacion_visitantes_ventas(self):
        """4. Evaluar relacion entre visitantes y ventas."""
        print("\n" + "="*60)
        print("4. RELACION ENTRE VISITANTES Y VENTAS")
        print("="*60)
        
        if self.datos is not None:
            # Calcular correlacion
            correlacion = self.datos['Visitantes'].corr(self.datos['Ventas'])
            
            print(f"[CORRELACION ENTRE VISITANTES Y VENTAS]")
            print(f"   Coeficiente de correlacion: {correlacion:.4f}")
            
            if correlacion > 0.8:
                print(f"   [OK] Correlacion MUY FUERTE (r > 0.8)")
            elif correlacion > 0.6:
                print(f"   [OK] Correlacion FUERTE (r > 0.6)")
            elif correlacion > 0.4:
                print(f"   [WARN] Correlacion MODERADA (r > 0.4)")
            else:
                print(f"   [NO] Correlacion DEBIL (r < 0.4)")
            
            # Analizar por mes
            print(f"\n[ANALISIS POR MES]")
            print(f"   {'Mes':<6} {'Visitantes':<12} {'Ventas':<10} {'Ratio':<8}")
            print(f"   {'-'*6} {'-'*12} {'-'*10} {'-'*8}")
            
            for _, row in self.datos.iterrows():
                ratio = row['Ventas'] / row['Visitantes']
                print(f"   {row['Mes']:<6} {row['Visitantes']:<12,} ${row['Ventas']:<9,} ${ratio:<7.2f}")
            
            # Calcular ratio promedio
            ratio_promedio = (self.datos['Ventas'] / self.datos['Visitantes']).mean()
            print(f"\n   Ratio promedio (Ventas/Visitantes): ${ratio_promedio:.2f}")
            
            # Mes con mejor ratio
            self.datos['Ratio_Ventas_Visitantes'] = self.datos['Ventas'] / self.datos['Visitantes']
            mejor_ratio_idx = self.datos['Ratio_Ventas_Visitantes'].idxmax()
            mejor_ratio = self.datos.loc[mejor_ratio_idx]
            
            print(f"\n[RESULTADO]")
            print(f"   Mes con MEJOR ratio ventas/visitantes: {mejor_ratio['Mes']}")
            print(f"   Ratio: ${mejor_ratio['Ratio_Ventas_Visitantes']:.2f}")
            print(f"   Ventas: ${mejor_ratio['Ventas']:,}")
            print(f"   Visitantes: {mejor_ratio['Visitantes']:,}")
            
            self.resultados['relacion_visitantes_ventas'] = {
                'correlacion': correlacion,
                'ratio_promedio': ratio_promedio,
                'mejor_ratio_mes': mejor_ratio['Mes'],
                'mejor_ratio_valor': mejor_ratio['Ratio_Ventas_Visitantes']
            }
    
    def crear_visualizaciones_especificas(self):
        """Crear visualizaciones especificas del analisis."""
        print("\n" + "="*60)
        print("CREANDO VISUALIZACIONES ESPECIFICAS")
        print("="*60)
        
        if self.datos is not None:
            # Configurar estilo
            plt.style.use('default')
            sns.set_palette("husl")
            
            # Crear figura con 4 subplots
            fig, axes = plt.subplots(2, 2, figsize=(16, 12))
            
            # 1. Eficiencia Publicitaria
            axes[0, 0].bar(self.datos['Mes'], self.datos['Eficiencia_Publicitaria'], 
                          color='skyblue', alpha=0.8, edgecolor='black')
            axes[0, 0].set_title('Eficiencia Publicitaria por Mes\n(Ventas / Gasto Publicidad)', 
                               fontweight='bold', fontsize=12)
            axes[0, 0].set_ylabel('Eficiencia')
            axes[0, 0].grid(True, alpha=0.3)
            
            # Agregar valores en las barras
            for i, v in enumerate(self.datos['Eficiencia_Publicitaria']):
                axes[0, 0].text(i, v + 0.1, f'{v:.2f}', ha='center', va='bottom', fontweight='bold')
            
            # 2. Tasa de Conversion
            axes[0, 1].bar(self.datos['Mes'], self.datos['Conversion'], 
                          color='lightcoral', alpha=0.8, edgecolor='black')
            axes[0, 1].set_title('Tasa de Conversion por Mes', 
                               fontweight='bold', fontsize=12)
            axes[0, 1].set_ylabel('Conversion (%)')
            axes[0, 1].grid(True, alpha=0.3)
            
            # Agregar valores en las barras
            for i, v in enumerate(self.datos['Conversion']):
                axes[0, 1].text(i, v + 0.05, f'{v}%', ha='center', va='bottom', fontweight='bold')
            
            # 3. Ticket Promedio
            axes[1, 0].bar(self.datos['Mes'], self.datos['Ticket_Promedio'], 
                          color='lightgreen', alpha=0.8, edgecolor='black')
            axes[1, 0].set_title('Ticket Promedio por Mes\n(Ventas / Productos Vendidos)', 
                               fontweight='bold', fontsize=12)
            axes[1, 0].set_ylabel('Ticket Promedio ($)')
            axes[1, 0].grid(True, alpha=0.3)
            
            # Agregar valores en las barras
            for i, v in enumerate(self.datos['Ticket_Promedio']):
                axes[1, 0].text(i, v + 1, f'${v:.0f}', ha='center', va='bottom', fontweight='bold')
            
            # 4. Relacion Visitantes vs Ventas
            axes[1, 1].scatter(self.datos['Visitantes'], self.datos['Ventas'], 
                              s=100, alpha=0.7, color='purple', edgecolor='black')
            axes[1, 1].set_title('Relacion Visitantes vs Ventas', 
                               fontweight='bold', fontsize=12)
            axes[1, 1].set_xlabel('Visitantes')
            axes[1, 1].set_ylabel('Ventas ($)')
            axes[1, 1].grid(True, alpha=0.3)
            
            # Agregar etiquetas de mes
            for i, row in self.datos.iterrows():
                axes[1, 1].annotate(row['Mes'], (row['Visitantes'], row['Ventas']), 
                                  xytext=(5, 5), textcoords='offset points', fontweight='bold')
            
            # Agregar linea de tendencia
            z = np.polyfit(self.datos['Visitantes'], self.datos['Ventas'], 1)
            p = np.poly1d(z)
            axes[1, 1].plot(self.datos['Visitantes'], p(self.datos['Visitantes']), 
                           "r--", alpha=0.8, linewidth=2)
            
            plt.suptitle('ANALISIS ESPECIFICO - EJERCICIO CLASE 7\n'
                        'Proyecto desarrollado como parte del curso AI Fundamentals - Guayerd - IBM Skills Build', 
                        fontsize=14, fontweight='bold', y=0.98)
            plt.tight_layout()
            
            # Guardar grafico
            archivo = "analisis_especifico_ejercicio.png"
            plt.savefig(archivo, dpi=300, bbox_inches='tight')
            print(f"   Grafico guardado: {archivo}")
            plt.close()
    
    def generar_reporte_especifico(self):
        """Generar reporte especifico del analisis."""
        print("\n" + "="*60)
        print("GENERANDO REPORTE ESPECIFICO")
        print("="*60)
        
        try:
            archivo = "reporte_especifico_ejercicio.txt"
            with open(archivo, 'w', encoding='utf-8') as f:
                f.write("REPORTE ESPECIFICO - EJERCICIO CLASE 7\n")
                f.write("Proyecto desarrollado como parte del curso AI Fundamentals - Guayerd - IBM Skills Build\n")
                f.write("=" * 70 + "\n\n")
                
                # 1. Eficiencia Publicitaria
                f.write("1. EFICIENCIA PUBLICITARIA\n")
                f.write("-" * 30 + "\n")
                if 'mejor_eficiencia' in self.resultados:
                    resultado = self.resultados['mejor_eficiencia']
                    f.write(f"Mes con MAYOR eficiencia: {resultado['mes']}\n")
                    f.write(f"Eficiencia: {resultado['eficiencia']:.2f}\n")
                    f.write(f"Ventas: ${resultado['ventas']:,}\n")
                    f.write(f"Gasto Publicidad: ${resultado['gasto']:,}\n\n")
                
                # 2. Tasa de Conversion
                f.write("2. TASA DE CONVERSION\n")
                f.write("-" * 25 + "\n")
                if 'mejor_conversion' in self.resultados:
                    resultado = self.resultados['mejor_conversion']
                    f.write(f"Mes con MEJOR conversion: {resultado['mes']}\n")
                    f.write(f"Tasa de conversion: {resultado['conversion']}%\n")
                    f.write(f"Ventas: ${resultado['ventas']:,}\n")
                    f.write(f"Visitantes: {resultado['visitantes']:,}\n")
                    f.write(f"Gasto Publicidad: ${resultado['gasto']:,}\n\n")
                
                # 3. Ticket Promedio
                f.write("3. TICKET PROMEDIO\n")
                f.write("-" * 20 + "\n")
                if 'ticket_promedio' in self.resultados:
                    resultado = self.resultados['ticket_promedio']
                    f.write(f"Ticket promedio general: ${resultado['general']:.2f}\n")
                    f.write(f"Ticket mas alto: ${resultado['maximo']:.2f}\n")
                    f.write(f"Ticket mas bajo: ${resultado['minimo']:.2f}\n")
                    f.write(f"Mes con mayor ticket: {resultado['mes_mayor_ticket']}\n")
                    f.write(f"Valor mayor ticket: ${resultado['valor_mayor_ticket']:.2f}\n\n")
                
                # 4. Relacion Visitantes-Ventas
                f.write("4. RELACION VISITANTES-VENTAS\n")
                f.write("-" * 35 + "\n")
                if 'relacion_visitantes_ventas' in self.resultados:
                    resultado = self.resultados['relacion_visitantes_ventas']
                    f.write(f"Correlacion: {resultado['correlacion']:.4f}\n")
                    f.write(f"Ratio promedio: ${resultado['ratio_promedio']:.2f}\n")
                    f.write(f"Mejor ratio - Mes: {resultado['mejor_ratio_mes']}\n")
                    f.write(f"Mejor ratio - Valor: ${resultado['mejor_ratio_valor']:.2f}\n\n")
                
                f.write("CONCLUSIONES:\n")
                f.write("-" * 15 + "\n")
                f.write("1. El mes con mayor eficiencia publicitaria es el que genera mas ventas por dolar invertido\n")
                f.write("2. La tasa de conversion indica la efectividad en convertir visitantes en clientes\n")
                f.write("3. El ticket promedio muestra el valor promedio por transaccion\n")
                f.write("4. La correlacion entre visitantes y ventas indica la fuerza de la relacion\n\n")
                
                f.write("RECOMENDACIONES:\n")
                f.write("-" * 18 + "\n")
                f.write("1. Replicar estrategias del mes con mayor eficiencia\n")
                f.write("2. Analizar factores del mes con mejor conversion\n")
                f.write("3. Optimizar para aumentar ticket promedio\n")
                f.write("4. Invertir mas en canales que generen visitantes de calidad\n\n")
                
                f.write("---\n")
                f.write("Proyecto desarrollado como parte del curso AI Fundamentals - Guayerd - IBM Skills Build\n")
                f.write("Autor: Enith Gicela Vargas Vargas\n")
            
            print(f"   Reporte especifico guardado: {archivo}")
            
        except Exception as e:
            print(f"   Error al generar reporte especifico: {e}")
    
    def ejecutar_analisis_especifico(self):
        """Ejecutar analisis especifico completo."""
        print("ANALISIS ESPECIFICO - EJERCICIO CLASE 7")
        print("Proyecto desarrollado como parte del curso AI Fundamentals - Guayerd - IBM Skills Build")
        print("=" * 70)
        
        # Cargar datos
        if not self.cargar_datos():
            return False
        
        # 1. Analizar eficiencia publicitaria
        self.analizar_eficiencia_publicitaria()
        
        # 2. Analizar tasa de conversion
        self.analizar_tasa_conversion()
        
        # 3. Calcular ticket promedio
        self.calcular_ticket_promedio()
        
        # 4. Evaluar relacion visitantes-ventas
        self.evaluar_relacion_visitantes_ventas()
        
        # Crear visualizaciones
        self.crear_visualizaciones_especificas()
        
        # Generar reporte
        self.generar_reporte_especifico()
        
        print(f"\n[OK] Analisis especifico completado exitosamente!")
        print(f"[INFO] Archivos generados en el directorio actual")
        
        return True

def main():
    """Funcion principal del analisis especifico."""
    analizador = AnalisisEspecificoEjercicio()
    analizador.ejecutar_analisis_especifico()

if __name__ == "__main__":
    main()
