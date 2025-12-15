#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ESTADÍSTICA PRESCRIPTIVA - PROYECTO AURELION SPRINT_2
======================================================

**Autor:** Enith Gicela Vargas Vargas  
**Camada:** 1  
**Grupo:** 11  
**Fecha:** 2025-10-27  
**Curso:** AI Fundamentals - Guayerd - IBM Skills Build  
**Sprint:** 2 - Machine Learning y Normalización  
**Módulo:** Estadística Prescriptiva  

Script para realizar análisis estadístico prescriptivo, incluyendo:
- Optimización de inventario
- Optimización de precios
- Recomendaciones de acciones basadas en datos
- Análisis de decisiones
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.optimize import minimize, linprog
import warnings
warnings.filterwarnings('ignore')

class EstadisticaPrescriptiva:
    """
    Clase para realizar análisis estadístico prescriptivo.
    
    Funcionalidades:
    - Optimización de inventario
    - Optimización de precios
    - Recomendaciones de acciones
    - Análisis de decisiones
    """
    
    def __init__(self):
        """Inicializar el analizador de estadística prescriptiva."""
        self.dataset = None
        self.recomendaciones = []
        
    def cargar_dataset(self):
        """Cargar dataset final normalizado."""
        print("CARGANDO DATASET PARA ANÁLISIS PRESCRIPTIVO")
        print("=" * 50)
        
        try:
            self.dataset = pd.read_csv("resultados/datasets_normalizados/dataset_final_completo.csv")
            print(f"✅ Dataset cargado: {self.dataset.shape[0]} registros × {self.dataset.shape[1]} columnas")
            return True
        except Exception as e:
            print(f"❌ Error al cargar dataset: {e}")
            return False
    
    def optimizar_inventario(self):
        """
        Optimizar niveles de inventario basado en análisis de demanda.
        
        Utiliza análisis de frecuencia de ventas y rotación de productos
        para recomendar niveles óptimos de inventario.
        """
        print("\n📦 OPTIMIZACIÓN DE INVENTARIO")
        print("=" * 50)
        
        # Análisis de frecuencia de ventas por producto
        ventas_por_producto = self.dataset.groupby('id_producto').agg({
            'cantidad': ['sum', 'mean', 'count'],
            'importe': 'sum'
        }).reset_index()
        ventas_por_producto.columns = ['id_producto', 'cantidad_total', 'cantidad_promedio', 'frecuencia_ventas', 'importe_total']
        
        # Clasificar productos por rotación
        ventas_por_producto['rotacion'] = pd.qcut(ventas_por_producto['frecuencia_ventas'], 
                                                  q=3, labels=['Baja', 'Media', 'Alta'])
        
        # Calcular niveles óptimos de inventario
        # Fórmula simplificada: inventario_optimo = demanda_promedio * tiempo_reposicion * factor_seguridad
        tiempo_reposicion = 7  # días
        factor_seguridad = 1.5
        
        ventas_por_producto['inventario_optimo'] = (
            ventas_por_producto['cantidad_promedio'] * tiempo_reposicion * factor_seguridad
        ).round(0)
        
        print("\n   Análisis de rotación de productos:")
        print(ventas_por_producto.groupby('rotacion').agg({
            'id_producto': 'count',
            'cantidad_total': 'sum',
            'importe_total': 'sum'
        }))
        
        print("\n   Recomendaciones de inventario:")
        print("     • Productos de ALTA rotación: Mantener inventario alto (factor 2.0)")
        print("     • Productos de MEDIA rotación: Inventario moderado (factor 1.5)")
        print("     • Productos de BAJA rotación: Inventario bajo (factor 1.0)")
        
        # Guardar recomendaciones
        self.recomendaciones.append({
            'tipo': 'Inventario',
            'descripcion': 'Optimización de niveles de inventario',
            'accion': 'Ajustar inventario según rotación de productos',
            'impacto_esperado': 'Reducción de costos de almacenamiento y mejora de disponibilidad'
        })
        
        return ventas_por_producto
    
    def optimizar_precios(self):
        """
        Optimizar estrategia de precios basada en elasticidad y demanda.
        
        Analiza la relación precio-cantidad para recomendar ajustes de precios.
        """
        print("\n💰 OPTIMIZACIÓN DE PRECIOS")
        print("=" * 50)
        
        # Análisis de elasticidad precio-cantidad
        if 'precio_unitario_detalle' in self.dataset.columns and 'cantidad' in self.dataset.columns:
            # Calcular correlación precio-cantidad
            correlacion = self.dataset['precio_unitario_detalle'].corr(self.dataset['cantidad'])
            
            print(f"\n   Análisis de elasticidad:")
            print(f"     Correlación precio-cantidad: {correlacion:.4f}")
            
            if correlacion < -0.3:
                print("     ⚠️  Elasticidad alta: Reducir precios puede aumentar significativamente las ventas")
            elif correlacion > 0.3:
                print("     ✅ Elasticidad baja: Aumentar precios puede aumentar ingresos sin reducir mucho ventas")
            else:
                print("     ℹ️  Elasticidad moderada: Precios actuales están bien balanceados")
            
            # Análisis por segmento de precio
            self.dataset['segmento_precio'] = pd.qcut(self.dataset['precio_unitario_detalle'], 
                                                      q=3, labels=['Bajo', 'Medio', 'Alto'])
            
            analisis_segmentos = self.dataset.groupby('segmento_precio').agg({
                'cantidad': 'mean',
                'importe': 'mean',
                'id_venta': 'count'
            })
            
            print("\n   Análisis por segmento de precio:")
            print(analisis_segmentos)
            
            # Recomendaciones
            print("\n   Recomendaciones de precios:")
            segmento_alto = analisis_segmentos.loc['Alto']
            segmento_bajo = analisis_segmentos.loc['Bajo']
            
            if segmento_alto['id_venta'] < segmento_bajo['id_venta'] * 0.5:
                print("     • Reducir precios en segmento ALTO para aumentar volumen")
            else:
                print("     • Mantener estrategia de precios actual")
            
            self.recomendaciones.append({
                'tipo': 'Precios',
                'descripcion': 'Optimización de estrategia de precios',
                'accion': 'Ajustar precios según elasticidad y demanda',
                'impacto_esperado': 'Maximización de ingresos y volumen de ventas'
            })
            
            return analisis_segmentos
        
        return None
    
    def recomendar_acciones_marketing(self):
        """
        Recomendar acciones de marketing basadas en análisis de clientes y productos.
        """
        print("\n📢 RECOMENDACIONES DE MARKETING")
        print("=" * 50)
        
        # Análisis de clientes por valor
        if 'id_cliente' in self.dataset.columns:
            clientes_valor = self.dataset.groupby('id_cliente').agg({
                'importe': ['sum', 'mean', 'count']
            }).reset_index()
            clientes_valor.columns = ['id_cliente', 'valor_total', 'ticket_promedio', 'frecuencia']
            
            # Clasificar clientes
            clientes_valor['segmento'] = pd.qcut(clientes_valor['valor_total'], 
                                                 q=3, labels=['Bajo', 'Medio', 'Alto'])
            
            print("\n   Segmentación de clientes por valor:")
            segmentacion = clientes_valor.groupby('segmento').agg({
                'id_cliente': 'count',
                'valor_total': 'sum',
                'ticket_promedio': 'mean'
            })
            print(segmentacion)
            
            # Recomendaciones
            print("\n   Recomendaciones de marketing:")
            print("     • Clientes ALTO valor: Programas VIP, atención personalizada")
            print("     • Clientes MEDIO valor: Programas de fidelización, ofertas especiales")
            print("     • Clientes BAJO valor: Campañas de reactivación, incentivos de primera compra")
            
            self.recomendaciones.append({
                'tipo': 'Marketing',
                'descripcion': 'Estrategias de marketing segmentadas',
                'accion': 'Implementar programas diferenciados por segmento de cliente',
                'impacto_esperado': 'Aumento de retención y valor de cliente'
            })
            
            return clientes_valor
        
        return None
    
    def optimizar_categoria_productos(self):
        """
        Optimizar mix de productos por categoría.
        """
        print("\n📊 OPTIMIZACIÓN DE MIX DE PRODUCTOS")
        print("=" * 50)
        
        if 'categoria' in self.dataset.columns:
            analisis_categorias = self.dataset.groupby('categoria').agg({
                'id_producto': 'nunique',
                'cantidad': 'sum',
                'importe': 'sum',
                'id_venta': 'count'
            })
            analisis_categorias.columns = ['productos_unicos', 'cantidad_total', 'ingresos_totales', 'ventas_totales']
            analisis_categorias['ingreso_por_producto'] = analisis_categorias['ingresos_totales'] / analisis_categorias['productos_unicos']
            analisis_categorias['ingreso_por_venta'] = analisis_categorias['ingresos_totales'] / analisis_categorias['ventas_totales']
            
            print("\n   Análisis por categoría:")
            print(analisis_categorias)
            
            # Identificar categorías con mejor rendimiento
            mejor_categoria = analisis_categorias['ingresos_totales'].idxmax()
            mejor_ingreso_por_producto = analisis_categorias['ingreso_por_producto'].idxmax()
            
            print(f"\n   Recomendaciones:")
            print(f"     • Categoría con mayor ingresos: {mejor_categoria}")
            print(f"     • Categoría con mejor ingreso por producto: {mejor_ingreso_por_producto}")
            print(f"     • Acción: Expandir productos en categorías de alto rendimiento")
            
            self.recomendaciones.append({
                'tipo': 'Mix de Productos',
                'descripcion': 'Optimización de mix de productos',
                'accion': f'Expandir categoría {mejor_categoria} y productos de alto rendimiento',
                'impacto_esperado': 'Aumento de ingresos totales'
            })
            
            return analisis_categorias
        
        return None
    
    def crear_visualizaciones_prescriptivas(self):
        """Crear visualizaciones de análisis prescriptivo."""
        print(f"\n📊 CREANDO VISUALIZACIONES PRESCRIPTIVAS")
        print("-" * 50)
        
        import os
        os.makedirs("resultados/histogramas", exist_ok=True)
        
        # Visualización de recomendaciones
        self._visualizar_recomendaciones()
        
        # Visualización de optimizaciones
        self._visualizar_optimizaciones()
        
        print("   ✅ Visualizaciones prescriptivas guardadas")
    
    def _visualizar_recomendaciones(self):
        """Visualizar resumen de recomendaciones."""
        if not self.recomendaciones:
            return
        
        fig, ax = plt.subplots(figsize=(14, 8))
        ax.axis('off')
        
        # Crear texto con recomendaciones
        texto = "RECOMENDACIONES PRESCRIPTIVAS - PROYECTO AURELION\n"
        texto += "=" * 70 + "\n\n"
        
        for i, rec in enumerate(self.recomendaciones, 1):
            texto += f"{i}. {rec['tipo'].upper()}\n"
            texto += f"   Descripción: {rec['descripcion']}\n"
            texto += f"   Acción Recomendada: {rec['accion']}\n"
            texto += f"   Impacto Esperado: {rec['impacto_esperado']}\n\n"
        
        texto += "\n" + "=" * 70 + "\n"
        texto += "Estas recomendaciones están basadas en análisis estadístico de los datos\n"
        texto += "y deben ser validadas con el equipo de negocio antes de implementarse."
        
        ax.text(0.05, 0.95, texto, transform=ax.transAxes,
               fontsize=10, verticalalignment='top', family='monospace',
               bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.8))
        
        plt.title('ANÁLISIS PRESCRIPTIVO - RECOMENDACIONES DE ACCIÓN', 
                 fontsize=14, fontweight='bold', pad=20)
        plt.tight_layout()
        plt.savefig("resultados/histogramas/recomendaciones_prescriptivas.png", dpi=300, bbox_inches='tight')
        plt.close()
        print("   ✅ Gráfico de recomendaciones guardado")
    
    def _visualizar_optimizaciones(self):
        """Visualizar resultados de optimizaciones."""
        fig = plt.figure(figsize=(16, 13))
        gs = fig.add_gridspec(3, 2, height_ratios=[3, 3, 1.5], hspace=0.3, wspace=0.3)
        
        datos_interpretacion = {}
        
        # 1. Optimización de inventario
        if 'id_producto' in self.dataset.columns:
            ventas_producto = self.dataset.groupby('id_producto')['cantidad'].sum().sort_values(ascending=False).head(10)
            ax1 = fig.add_subplot(gs[0, 0])
            ax1.barh(range(len(ventas_producto)), ventas_producto.values, color='skyblue', edgecolor='black')
            ax1.set_yticks(range(len(ventas_producto)))
            ax1.set_yticklabels([f'Prod {p}' for p in ventas_producto.index])
            ax1.set_xlabel('Cantidad Total Vendida')
            ax1.set_title('Top 10 Productos por Ventas\n(Priorizar en Inventario)', fontweight='bold')
            ax1.grid(alpha=0.3, axis='x')
            
            # Guardar datos para interpretación
            datos_interpretacion['inventario'] = {
                'top_producto': ventas_producto.index[0],
                'cantidad_top': ventas_producto.values[0],
                'total_top10': ventas_producto.sum(),
                'total_general': self.dataset.groupby('id_producto')['cantidad'].sum().sum()
            }
        
        # 2. Optimización de precios
        if 'precio_unitario_detalle' in self.dataset.columns and 'cantidad' in self.dataset.columns:
            ax2 = fig.add_subplot(gs[0, 1])
            scatter = ax2.scatter(self.dataset['precio_unitario_detalle'], 
                                self.dataset['cantidad'], 
                                alpha=0.5, c=self.dataset['importe'], 
                                cmap='viridis', s=50)
            ax2.set_xlabel('Precio Unitario')
            ax2.set_ylabel('Cantidad')
            ax2.set_title('Relación Precio-Cantidad\n(Análisis de Elasticidad)', fontweight='bold')
            ax2.grid(alpha=0.3)
            plt.colorbar(scatter, ax=ax2, label='Importe')
            
            # Calcular correlación para interpretación
            corr_precio_cantidad = self.dataset['precio_unitario_detalle'].corr(self.dataset['cantidad'])
            datos_interpretacion['precios'] = {
                'correlacion': corr_precio_cantidad,
                'precio_promedio': self.dataset['precio_unitario_detalle'].mean(),
                'cantidad_promedio': self.dataset['cantidad'].mean()
            }
        
        # 3. Segmentación de clientes
        if 'id_cliente' in self.dataset.columns:
            clientes_valor = self.dataset.groupby('id_cliente')['importe'].sum().sort_values(ascending=False)
            segmentos = pd.qcut(clientes_valor, q=3, labels=['Bajo', 'Medio', 'Alto'])
            segmentos_counts = segmentos.value_counts()
            ax3 = fig.add_subplot(gs[1, 0])
            ax3.pie(segmentos_counts.values, labels=segmentos_counts.index, autopct='%1.1f%%',
                   colors=['lightcoral', 'lightblue', 'lightgreen'], startangle=90)
            ax3.set_title('Segmentación de Clientes por Valor\n(Estrategias Diferenciadas)', fontweight='bold')
            
            # Guardar datos para interpretación
            datos_interpretacion['segmentacion'] = {
                'bajo': segmentos_counts.get('Bajo', 0),
                'medio': segmentos_counts.get('Medio', 0),
                'alto': segmentos_counts.get('Alto', 0),
                'total_clientes': len(clientes_valor)
            }
        
        # 4. Análisis de categorías
        if 'categoria' in self.dataset.columns:
            cat_ingresos = self.dataset.groupby('categoria')['importe'].sum().sort_values(ascending=False)
            ax4 = fig.add_subplot(gs[1, 1])
            ax4.bar(range(len(cat_ingresos)), cat_ingresos.values, color='orange', edgecolor='black', alpha=0.7)
            ax4.set_xticks(range(len(cat_ingresos)))
            ax4.set_xticklabels(cat_ingresos.index, rotation=45, ha='right')
            ax4.set_ylabel('Ingresos Totales')
            ax4.set_title('Ingresos por Categoría\n(Optimizar Mix de Productos)', fontweight='bold')
            ax4.grid(alpha=0.3, axis='y')
            
            # Agregar valores en las barras
            for i, valor in enumerate(cat_ingresos.values):
                ax4.text(i, valor + valor*0.02, f'${valor:,.0f}', ha='center', va='bottom', fontweight='bold', fontsize=9)
            
            # Guardar datos para interpretación
            datos_interpretacion['categorias'] = {
                'top_categoria': cat_ingresos.index[0],
                'ingresos_top': cat_ingresos.values[0],
                'total_ingresos': cat_ingresos.sum(),
                'porcentaje_top': (cat_ingresos.values[0] / cat_ingresos.sum() * 100) if cat_ingresos.sum() > 0 else 0
            }
        
        # Agregar interpretación específica
        ax_interpretacion = fig.add_subplot(gs[2, :])
        ax_interpretacion.axis('off')
        
        interpretacion_lineas = ["INTERPRETACIÓN ESPECÍFICA - OPTIMIZACIONES PRESCRIPTIVAS:"]
        interpretacion_lineas.append("=" * 70)
        
        if 'inventario' in datos_interpretacion:
            inv = datos_interpretacion['inventario']
            porcentaje_top10 = (inv['total_top10'] / inv['total_general'] * 100) if inv['total_general'] > 0 else 0
            interpretacion_lineas.append(f"\n1. OPTIMIZACIÓN DE INVENTARIO:")
            interpretacion_lineas.append(f"   • Producto más vendido: ID {inv['top_producto']} ({inv['cantidad_top']} unidades)")
            interpretacion_lineas.append(f"   • Top 10 productos representan: {porcentaje_top10:.1f}% del total de ventas")
            interpretacion_lineas.append(f"   → RECOMENDACIÓN: Priorizar stock de estos 10 productos")
        
        if 'precios' in datos_interpretacion:
            prec = datos_interpretacion['precios']
            interpretacion_lineas.append(f"\n2. OPTIMIZACIÓN DE PRECIOS:")
            interpretacion_lineas.append(f"   • Correlación precio-cantidad: {prec['correlacion']:.3f}")
            if prec['correlacion'] < -0.3:
                interpretacion_lineas.append(f"   → Elasticidad ALTA: Aumentar precios reduce cantidad significativamente")
            elif prec['correlacion'] > 0.3:
                interpretacion_lineas.append(f"   → Elasticidad BAJA: Aumentar precios no reduce cantidad mucho")
            else:
                interpretacion_lineas.append(f"   → Elasticidad MODERADA: Relación precio-cantidad equilibrada")
            interpretacion_lineas.append(f"   • Precio promedio: ${prec['precio_promedio']:.2f} | Cantidad promedio: {prec['cantidad_promedio']:.2f}")
        
        if 'segmentacion' in datos_interpretacion:
            seg = datos_interpretacion['segmentacion']
            pct_bajo = (seg['bajo'] / seg['total_clientes'] * 100) if seg['total_clientes'] > 0 else 0
            pct_medio = (seg['medio'] / seg['total_clientes'] * 100) if seg['total_clientes'] > 0 else 0
            pct_alto = (seg['alto'] / seg['total_clientes'] * 100) if seg['total_clientes'] > 0 else 0
            interpretacion_lineas.append(f"\n3. SEGMENTACIÓN DE CLIENTES:")
            interpretacion_lineas.append(f"   • Bajo: {seg['bajo']} clientes ({pct_bajo:.1f}%)")
            interpretacion_lineas.append(f"   • Medio: {seg['medio']} clientes ({pct_medio:.1f}%)")
            interpretacion_lineas.append(f"   • Alto: {seg['alto']} clientes ({pct_alto:.1f}%)")
            interpretacion_lineas.append(f"   → RECOMENDACIÓN: Estrategias diferenciadas por segmento")
        
        if 'categorias' in datos_interpretacion:
            cat = datos_interpretacion['categorias']
            interpretacion_lineas.append(f"\n4. OPTIMIZACIÓN DE MIX DE PRODUCTOS:")
            interpretacion_lineas.append(f"   • Categoría líder: {cat['top_categoria']} (${cat['ingresos_top']:,.2f})")
            interpretacion_lineas.append(f"   • Representa: {cat['porcentaje_top']:.1f}% de ingresos totales")
            interpretacion_lineas.append(f"   → RECOMENDACIÓN: Expandir categoría líder, optimizar mix")
        
        interpretacion_lineas.append(f"\nCONCLUSIÓN GENERAL:")
        interpretacion_lineas.append(f"  Estas optimizaciones están basadas en análisis estadístico de los datos")
        interpretacion_lineas.append(f"  y deben ser validadas con el equipo de negocio antes de implementarse.")
        
        interpretacion = "\n".join(interpretacion_lineas)
        ax_interpretacion.text(0.05, 0.95, interpretacion, transform=ax_interpretacion.transAxes,
                              fontsize=7, verticalalignment='top', family='monospace',
                              bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.9))
        
        plt.suptitle('ANÁLISIS PRESCRIPTIVO - OPTIMIZACIONES Y RECOMENDACIONES', 
                    fontsize=14, fontweight='bold', y=0.98)
        plt.tight_layout()
        plt.savefig("resultados/histogramas/optimizaciones_prescriptivas.png", dpi=300, bbox_inches='tight')
        plt.close()
        print("   ✅ Gráfico de optimizaciones guardado")
    
    def ejecutar_analisis_completo(self):
        """Ejecutar análisis prescriptivo completo."""
        print("=" * 80)
        print("ESTADÍSTICA PRESCRIPTIVA - PROYECTO AURELION")
        print("=" * 80)
        print("Proyecto desarrollado como parte del curso AI Fundamentals - Guayerd - IBM Skills Build")
        print()
        
        if not self.cargar_dataset():
            return False
        
        print("\n" + "=" * 80)
        print("EJECUTANDO ANÁLISIS PRESCRIPTIVO COMPLETO")
        print("=" * 80)
        
        # Optimización de inventario
        print("\n1️⃣  OPTIMIZACIÓN DE INVENTARIO")
        self.optimizar_inventario()
        
        # Optimización de precios
        print("\n2️⃣  OPTIMIZACIÓN DE PRECIOS")
        self.optimizar_precios()
        
        # Recomendaciones de marketing
        print("\n3️⃣  RECOMENDACIONES DE MARKETING")
        self.recomendar_acciones_marketing()
        
        # Optimización de mix de productos
        print("\n4️⃣  OPTIMIZACIÓN DE MIX DE PRODUCTOS")
        self.optimizar_categoria_productos()
        
        # Crear visualizaciones
        print("\n5️⃣  VISUALIZACIONES")
        self.crear_visualizaciones_prescriptivas()
        
        # Guardar resultados
        self.guardar_resultados()
        
        # Mostrar resumen de recomendaciones
        print("\n" + "=" * 80)
        print("📋 RESUMEN DE RECOMENDACIONES")
        print("=" * 80)
        for i, rec in enumerate(self.recomendaciones, 1):
            print(f"\n{i}. {rec['tipo']}:")
            print(f"   Acción: {rec['accion']}")
            print(f"   Impacto: {rec['impacto_esperado']}")
        
        print("\n" + "=" * 80)
        print("✅ ANÁLISIS PRESCRIPTIVO COMPLETADO EXITOSAMENTE")
        print("=" * 80)
        print("📁 Resultados guardados en: resultados/estadisticas/estadistica_prescriptiva.txt")
        print("📊 Gráficos guardados en: resultados/histogramas/")
        
        return True
    
    def guardar_resultados(self):
        """Guardar resultados de análisis prescriptivo."""
        try:
            archivo = "resultados/estadisticas/estadistica_prescriptiva.txt"
            with open(archivo, 'w', encoding='utf-8') as f:
                f.write("ESTADÍSTICA PRESCRIPTIVA - PROYECTO AURELION\n")
                f.write("=" * 80 + "\n\n")
                f.write("Este análisis proporciona recomendaciones de acciones basadas en datos:\n\n")
                
                for i, rec in enumerate(self.recomendaciones, 1):
                    f.write(f"{i}. {rec['tipo']}\n")
                    f.write(f"   Descripción: {rec['descripcion']}\n")
                    f.write(f"   Acción Recomendada: {rec['accion']}\n")
                    f.write(f"   Impacto Esperado: {rec['impacto_esperado']}\n\n")
                
                f.write("\n" + "=" * 80 + "\n")
                f.write("NOTA: Estas recomendaciones deben ser validadas con el equipo de negocio\n")
                f.write("antes de implementarse.\n")
            
            print(f"   ✅ Resultados guardados: {archivo}")
        except Exception as e:
            print(f"   ⚠️  Error al guardar resultados: {e}")

def main():
    """Función principal."""
    analizador = EstadisticaPrescriptiva()
    analizador.ejecutar_analisis_completo()

if __name__ == "__main__":
    main()

