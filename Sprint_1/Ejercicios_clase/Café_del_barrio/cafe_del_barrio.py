#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CAFÉ DEL BARRIO - ANÁLISIS DE DATOS - PROYECTO AURELION SPRINT_1
=================================================================

**Autor:** Enith Gicela Vargas Vargas  
**Fecha:** 2025-10-27  
**Curso:** AI Fundamentals - Guayerd - IBM Skills Build  
**Sprint:** 1 - Análisis de Datos Básico  
**Módulo:** Café del Barrio  

Sistema de análisis de datos para un café del barrio que incluye:
1. Calcular correlación entre temperatura y ventas
2. Identificar el mes con mejor retorno publicitario
3. Analizar relación personal vs satisfacción cliente
4. Proponer estrategia basada en datos

Autor: Enith Gicela Vargas Vargas
Fecha: 2025
"""

import pandas as pd          # Librería para manipulación y análisis de datos estructurados
import numpy as np           # Librería para cálculos numéricos y operaciones matemáticas
import matplotlib.pyplot as plt  # Librería para crear visualizaciones y gráficos
import seaborn as sns        # Librería para visualizaciones estadísticas avanzadas
from scipy.stats import pearsonr  # Función para calcular correlación de Pearson
import warnings             # Módulo para controlar avisos del sistema
warnings.filterwarnings('ignore')

class CafeDelBarrio:
    def __init__(self):
        """Inicializa el sistema con los datos del café del barrio."""
        self.datos = {
            'Mes': ['Ene', 'Feb', 'Mar', 'Abr', 'May'],
            'Ventas': [15000, 22000, 18000, 28000, 25000],
            'Temperatura': [18, 25, 22, 28, 30],
            'Publicidad': [800, 1200, 900, 1500, 1300],
            'Personal': [4, 5, 4, 6, 5],
            'Satisfaccion': [4.2, 4.5, 4.1, 4.8, 4.6]
        }
        
        self.df = pd.DataFrame(self.datos)
        self.df['Mes_Num'] = range(1, 6)  # Para cálculos numéricos
        
    def mostrar_datos(self):
        """Muestra los datos del café."""
        print("☕ DATOS DEL CAFÉ DEL BARRIO")
        print("=" * 50)
        print(self.df.to_string(index=False))
        print()
        
    def calcular_correlacion_temperatura_ventas(self):
        """Tarea 1: Calcular correlación entre temperatura y ventas."""
        print("🌡️ TAREA 1: CORRELACIÓN TEMPERATURA vs VENTAS")
        print("=" * 60)
        
        # Calcular correlación de Pearson
        correlacion, p_valor = pearsonr(self.df['Temperatura'], self.df['Ventas'])
        
        print(f"📊 Correlación de Pearson: {correlacion:.4f}")
        print(f"📈 P-valor: {p_valor:.4f}")
        
        # Interpretación
        if abs(correlacion) > 0.7:
            fuerza = "Fuerte"
        elif abs(correlacion) > 0.4:
            fuerza = "Moderada"
        else:
            fuerza = "Débil"
            
        if correlacion > 0:
            direccion = "positiva"
        else:
            direccion = "negativa"
            
        print(f"🔍 Interpretación: Correlación {fuerza} {direccion}")
        
        if p_valor < 0.05:
            print("✅ La correlación es estadísticamente significativa (p < 0.05)")
        else:
            print("❌ La correlación NO es estadísticamente significativa (p ≥ 0.05)")
            
        # Análisis detallado
        print(f"\n📋 ANÁLISIS DETALLADO:")
        print(f"   • Por cada grado de aumento en temperatura, las ventas")
        print(f"     {'aumentan' if correlacion > 0 else 'disminuyen'} en promedio")
        print(f"   • La temperatura explica el {correlacion**2*100:.1f}% de la variabilidad en ventas")
        
        return correlacion, p_valor
        
    def identificar_mejor_retorno_publicitario(self):
        """Tarea 2: Identificar el mes con mejor retorno publicitario."""
        print("\n📢 TAREA 2: MEJOR RETORNO PUBLICITARIO")
        print("=" * 60)
        
        # Calcular retorno publicitario (ROI)
        self.df['ROI_Publicidad'] = (self.df['Ventas'] - self.df['Ventas'].shift(1)) / self.df['Publicidad'] * 100
        self.df['ROI_Publicidad'] = self.df['ROI_Publicidad'].fillna(0)
        
        # Calcular ROI acumulado
        self.df['ROI_Acumulado'] = (self.df['Ventas'] - self.df['Ventas'].iloc[0]) / self.df['Publicidad'].cumsum() * 100
        
        print("📊 RETORNO PUBLICITARIO POR MES:")
        print("-" * 40)
        for i, row in self.df.iterrows():
            print(f"   {row['Mes']:3s}: ROI = {row['ROI_Publicidad']:6.1f}% | ROI Acum = {row['ROI_Acumulado']:6.1f}%")
        
        # Encontrar el mejor mes
        mejor_mes_roi = self.df.loc[self.df['ROI_Publicidad'].idxmax()]
        mejor_mes_acum = self.df.loc[self.df['ROI_Acumulado'].idxmax()]
        
        print(f"\n🏆 MEJOR MES POR ROI INCREMENTAL:")
        print(f"   Mes: {mejor_mes_roi['Mes']}")
        print(f"   ROI: {mejor_mes_roi['ROI_Publicidad']:.1f}%")
        print(f"   Ventas: ${mejor_mes_roi['Ventas']:,}")
        print(f"   Publicidad: ${mejor_mes_roi['Publicidad']:,}")
        
        print(f"\n🏆 MEJOR MES POR ROI ACUMULADO:")
        print(f"   Mes: {mejor_mes_acum['Mes']}")
        print(f"   ROI Acumulado: {mejor_mes_acum['ROI_Acumulado']:.1f}%")
        print(f"   Ventas: ${mejor_mes_acum['Ventas']:,}")
        print(f"   Publicidad: ${mejor_mes_acum['Publicidad']:,}")
        
        return mejor_mes_roi, mejor_mes_acum
        
    def analizar_relacion_personal_satisfaccion(self):
        """Tarea 3: Analizar relación personal vs satisfacción cliente."""
        print("\n👥 TAREA 3: RELACIÓN PERSONAL vs SATISFACCIÓN")
        print("=" * 60)
        
        # Calcular correlación
        correlacion, p_valor = pearsonr(self.df['Personal'], self.df['Satisfaccion'])
        
        print(f"📊 Correlación Personal-Satisfacción: {correlacion:.4f}")
        print(f"📈 P-valor: {p_valor:.4f}")
        
        # Interpretación
        if abs(correlacion) > 0.7:
            fuerza = "Fuerte"
        elif abs(correlacion) > 0.4:
            fuerza = "Moderada"
        else:
            fuerza = "Débil"
            
        if correlacion > 0:
            direccion = "positiva"
        else:
            direccion = "negativa"
            
        print(f"🔍 Interpretación: Correlación {fuerza} {direccion}")
        
        # Análisis detallado
        print(f"\n📋 ANÁLISIS DETALLADO:")
        print(f"   • Por cada persona adicional en el personal, la satisfacción")
        print(f"     {'aumenta' if correlacion > 0 else 'disminuye'} en promedio")
        print(f"   • El personal explica el {correlacion**2*100:.1f}% de la variabilidad en satisfacción")
        
        # Análisis por mes
        print(f"\n📅 SATISFACCIÓN POR MES:")
        print("-" * 30)
        for i, row in self.df.iterrows():
            print(f"   {row['Mes']:3s}: {row['Personal']} personas → Satisfacción {row['Satisfaccion']:.1f}")
        
        # Recomendaciones
        print(f"\n💡 RECOMENDACIONES:")
        if correlacion > 0.5:
            print("   ✅ Aumentar el personal mejora significativamente la satisfacción")
        elif correlacion > 0.3:
            print("   ⚠️ El personal tiene un impacto moderado en la satisfacción")
        else:
            print("   ❌ El personal no tiene un impacto significativo en la satisfacción")
            
        return correlacion, p_valor
        
    def proponer_estrategia_basada_datos(self):
        """Tarea 4: Proponer estrategia basada en datos."""
        print("\n🎯 TAREA 4: ESTRATEGIA BASADA EN DATOS")
        print("=" * 60)
        
        # Análisis de tendencias
        print("📈 ANÁLISIS DE TENDENCIAS:")
        print("-" * 30)
        
        # Tendencia de ventas
        ventas_tendencia = np.polyfit(self.df['Mes_Num'], self.df['Ventas'], 1)[0]
        print(f"   • Ventas: {'📈 Creciente' if ventas_tendencia > 0 else '📉 Decreciente'} ({ventas_tendencia:+.0f} $/mes)")
        
        # Tendencia de satisfacción
        satisfaccion_tendencia = np.polyfit(self.df['Mes_Num'], self.df['Satisfaccion'], 1)[0]
        print(f"   • Satisfacción: {'📈 Creciente' if satisfaccion_tendencia > 0 else '📉 Decreciente'} ({satisfaccion_tendencia:+.2f} puntos/mes)")
        
        # Análisis de eficiencia
        print(f"\n⚡ ANÁLISIS DE EFICIENCIA:")
        print("-" * 30)
        
        # Eficiencia publicitaria
        eficiencia_pub = self.df['Ventas'] / self.df['Publicidad']
        mejor_eficiencia_pub = self.df.loc[eficiencia_pub.idxmax()]
        print(f"   • Mejor eficiencia publicitaria: {mejor_eficiencia_pub['Mes']} ({eficiencia_pub.max():.1f} $ por $ invertido)")
        
        # Eficiencia del personal
        eficiencia_personal = self.df['Ventas'] / self.df['Personal']
        mejor_eficiencia_personal = self.df.loc[eficiencia_personal.idxmax()]
        print(f"   • Mejor eficiencia del personal: {mejor_eficiencia_personal['Mes']} ({eficiencia_personal.max():.0f} $ por persona)")
        
        # Estrategia recomendada
        print(f"\n🎯 ESTRATEGIA RECOMENDADA:")
        print("-" * 30)
        
        # Basada en correlaciones
        corr_temp_ventas, _ = pearsonr(self.df['Temperatura'], self.df['Ventas'])
        corr_personal_satisf, _ = pearsonr(self.df['Personal'], self.df['Satisfaccion'])
        
        print("1. 📊 GESTIÓN DE VENTAS:")
        if corr_temp_ventas > 0.5:
            print("   • Aprovechar la temporada de calor para aumentar ventas")
            print("   • Preparar promociones especiales para días calurosos")
        else:
            print("   • La temperatura no es un factor determinante")
            print("   • Enfocarse en otros factores de marketing")
            
        print("\n2. 👥 GESTIÓN DEL PERSONAL:")
        if corr_personal_satisf > 0.5:
            print("   • Mantener un personal adecuado para la satisfacción")
            print("   • Considerar contratación adicional en temporadas altas")
        else:
            print("   • El personal actual es suficiente")
            print("   • Enfocarse en capacitación y motivación")
            
        print("\n3. 📢 GESTIÓN PUBLICITARIA:")
        mejor_mes_pub = self.df.loc[self.df['ROI_Publicidad'].idxmax()]
        print(f"   • Replicar estrategia de {mejor_mes_pub['Mes']} (mejor ROI)")
        print(f"   • Invertir más en publicidad en meses con alta eficiencia")
        
        print("\n4. 🎯 OBJETIVOS ESPECÍFICOS:")
        print(f"   • Mantener satisfacción > 4.5 puntos")
        print(f"   • Aumentar ventas promedio a ${self.df['Ventas'].mean()*1.1:,.0f}")
        print(f"   • Optimizar ROI publicitario > {self.df['ROI_Publicidad'].mean():.1f}%")
        
        return {
            'ventas_tendencia': ventas_tendencia,
            'satisfaccion_tendencia': satisfaccion_tendencia,
            'mejor_eficiencia_pub': mejor_eficiencia_pub,
            'mejor_eficiencia_personal': mejor_eficiencia_personal
        }
        
    def generar_reporte_completo(self):
        """Genera un reporte completo con todas las tareas."""
        print("☕ CAFÉ DEL BARRIO - REPORTE COMPLETO DE ANÁLISIS")
        print("=" * 70)
        
        # Mostrar datos
        self.mostrar_datos()
        
        # Ejecutar todas las tareas
        corr_temp_ventas, p_temp = self.calcular_correlacion_temperatura_ventas()
        mejor_roi, mejor_roi_acum = self.identificar_mejor_retorno_publicitario()
        corr_personal_satisf, p_personal = self.analizar_relacion_personal_satisfaccion()
        estrategia = self.proponer_estrategia_basada_datos()
        
        # Resumen ejecutivo
        print("\n📋 RESUMEN EJECUTIVO")
        print("=" * 30)
        print(f"• Correlación temperatura-ventas: {corr_temp_ventas:.3f}")
        print(f"• Mejor mes por ROI: {mejor_roi['Mes']}")
        print(f"• Correlación personal-satisfacción: {corr_personal_satisf:.3f}")
        print(f"• Tendencia de ventas: {'📈' if estrategia['ventas_tendencia'] > 0 else '📉'}")
        print(f"• Tendencia de satisfacción: {'📈' if estrategia['satisfaccion_tendencia'] > 0 else '📉'}")
        
        print("\n✅ Análisis completado exitosamente")
        print("=" * 70)

def main():
    """Función principal del sistema."""
    print("☕ BIENVENIDO AL SISTEMA DE ANÁLISIS - CAFÉ DEL BARRIO")
    print("=" * 60)
    print("Este sistema analiza los datos del café del barrio para:")
    print("1. Calcular correlación entre temperatura y ventas")
    print("2. Identificar el mes con mejor retorno publicitario")
    print("3. Analizar relación personal vs satisfacción cliente")
    print("4. Proponer estrategia basada en datos")
    print()
    
    # Crear instancia del sistema
    cafe = CafeDelBarrio()
    
    # Mostrar menú
    while True:
        print("\n📋 MENÚ PRINCIPAL")
        print("-" * 20)
        print("1. Ver datos del café")
        print("2. Tarea 1: Correlación temperatura-ventas")
        print("3. Tarea 2: Mejor retorno publicitario")
        print("4. Tarea 3: Relación personal-satisfacción")
        print("5. Tarea 4: Estrategia basada en datos")
        print("6. Reporte completo")
        print("0. Salir")
        
        try:
            opcion = input("\nSelecciona una opción (0-6): ").strip()
            
            if opcion == '0':
                print("\n👋 ¡Gracias por usar el sistema de análisis del café del barrio!")
                break
            elif opcion == '1':
                cafe.mostrar_datos()
            elif opcion == '2':
                cafe.calcular_correlacion_temperatura_ventas()
            elif opcion == '3':
                cafe.identificar_mejor_retorno_publicitario()
            elif opcion == '4':
                cafe.analizar_relacion_personal_satisfaccion()
            elif opcion == '5':
                cafe.proponer_estrategia_basada_datos()
            elif opcion == '6':
                cafe.generar_reporte_completo()
            else:
                print("❌ Opción no válida. Intenta nuevamente.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Programa interrumpido por el usuario.")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()