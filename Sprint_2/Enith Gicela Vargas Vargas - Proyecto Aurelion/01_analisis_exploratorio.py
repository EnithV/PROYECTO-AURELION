#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ANÁLISIS EXPLORATORIO DE DATOS (EDA) - PROYECTO AURELION SPRINT_2
=================================================================

**Autor:** Enith Gicela Vargas Vargas  
**Camada:** 1  
**Grupo:** 11  
**Fecha:** 2025-10-27  
**Curso:** AI Fundamentals - Guayerd - IBM Skills Build  
**Sprint:** 2 - Machine Learning y Normalización  
**Módulo:** Análisis Exploratorio  

Script para realizar análisis exploratorio completo de cada tabla
de la base de datos Aurelion, incluyendo:
- Estadísticas descriptivas
- Análisis de distribuciones
- Detección de outliers
- Histogramas y visualizaciones
"""

import pandas as pd          # Librería para manipulación y análisis de datos estructurados
import numpy as np           # Librería para cálculos numéricos y matemáticos con arrays
import matplotlib.pyplot as plt  # Librería para crear visualizaciones y gráficos
import seaborn as sns       # Librería para visualizaciones estadísticas avanzadas
from scipy import stats     # Módulo de SciPy para análisis estadístico
import warnings             # Módulo para controlar avisos del sistema
warnings.filterwarnings('ignore')

class AnalisisExploratorio:
    """
    Clase para realizar análisis exploratorio de datos.
    
    Funcionalidades:
    - Análisis estadístico descriptivo
    - Visualizaciones de distribuciones
    - Detección de outliers
    - Análisis de correlaciones
    """
    
    def __init__(self):
        """Inicializar el analizador exploratorio."""
        self.base_path = "../../Datos Proyecto/Base de datos_Tienda_Aurelion/Base de datos"
        self.tablas = {}
        self.resultados = {}
        
        # Configurar matplotlib para guardar gráficos
        plt.style.use('default')
        sns.set_palette("husl")
        
    def cargar_tablas(self):
        """Cargar todas las tablas de la base de datos."""
        print("📊 CARGANDO TABLAS PARA ANÁLISIS EXPLORATORIO")
        print("=" * 60)
        
        try:
            # Cargar cada tabla
            self.tablas['clientes'] = pd.read_excel(f"{self.base_path}/clientes.xlsx")
            self.tablas['productos'] = pd.read_excel(f"{self.base_path}/productos.xlsx")
            self.tablas['ventas'] = pd.read_excel(f"{self.base_path}/ventas.xlsx")
            self.tablas['detalle_ventas'] = pd.read_excel(f"{self.base_path}/detalle_ventas.xlsx")
            
            print("✅ Todas las tablas cargadas exitosamente!")
            return True
            
        except Exception as e:
            print(f"❌ Error al cargar tablas: {e}")
            return False
    
    def analisis_estadistico_descriptivo(self, nombre_tabla, df):
        """Realizar análisis estadístico descriptivo de una tabla."""
        print(f"\n📈 ANÁLISIS ESTADÍSTICO DESCRIPTIVO: {nombre_tabla.upper()}")
        print("-" * 60)
        
        # Información general
        print(f"📊 Dimensiones: {df.shape[0]} filas × {df.shape[1]} columnas")
        print(f"📊 Memoria utilizada: {df.memory_usage(deep=True).sum() / 1024:.1f} KB")
        
        # Análisis por tipo de columna
        columnas_numericas = df.select_dtypes(include=[np.number]).columns
        columnas_categoricas = df.select_dtypes(include=['object', 'category']).columns
        columnas_fecha = df.select_dtypes(include=['datetime64']).columns
        
        print(f"\n🔢 Columnas numéricas: {len(columnas_numericas)}")
        print(f"📝 Columnas categóricas: {len(columnas_categoricas)}")
        print(f"📅 Columnas de fecha: {len(columnas_fecha)}")
        
        # Estadísticas descriptivas para columnas numéricas
        if len(columnas_numericas) > 0:
            print(f"\n📊 ESTADÍSTICAS DESCRIPTIVAS (NUMÉRICAS):")
            stats_desc = df[columnas_numericas].describe()
            print(stats_desc.round(2))
            
            # Análisis adicional
            print(f"\n🔍 ANÁLISIS ADICIONAL:")
            for col in columnas_numericas:
                skewness = stats.skew(df[col].dropna())
                kurtosis = stats.kurtosis(df[col].dropna())
                print(f"   {col}:")
                print(f"     • Asimetría (Skewness): {skewness:.3f}")
                print(f"     • Curtosis: {kurtosis:.3f}")
        
        # Análisis para columnas categóricas
        if len(columnas_categoricas) > 0:
            print(f"\n📝 ANÁLISIS CATEGÓRICAS:")
            for col in columnas_categoricas:
                valores_unicos = df[col].nunique()
                valor_mas_frecuente = df[col].mode().iloc[0] if not df[col].mode().empty else "N/A"
                frecuencia_max = df[col].value_counts().iloc[0]
                print(f"   {col}:")
                print(f"     • Valores únicos: {valores_unicos}")
                print(f"     • Valor más frecuente: {valor_mas_frecuente} ({frecuencia_max} veces)")
        
        return {
            'dimensiones': df.shape,
            'columnas_numericas': list(columnas_numericas),
            'columnas_categoricas': list(columnas_categoricas),
            'columnas_fecha': list(columnas_fecha),
            'estadisticas': stats_desc if len(columnas_numericas) > 0 else None
        }
    
    def detectar_outliers(self, nombre_tabla, df):
        """Detectar outliers en columnas numéricas."""
        print(f"\n🔍 DETECCIÓN DE OUTLIERS: {nombre_tabla.upper()}")
        print("-" * 50)
        
        columnas_numericas = df.select_dtypes(include=[np.number]).columns
        outliers_info = {}
        
        for col in columnas_numericas:
            if df[col].notna().sum() > 0:  # Solo si hay datos válidos
                # Método IQR
                Q1 = df[col].quantile(0.25)
                Q3 = df[col].quantile(0.75)
                IQR = Q3 - Q1
                limite_inferior = Q1 - 1.5 * IQR
                limite_superior = Q3 + 1.5 * IQR
                
                outliers_iqr = df[(df[col] < limite_inferior) | (df[col] > limite_superior)]
                
                # Método Z-score
                z_scores = np.abs(stats.zscore(df[col].dropna()))
                outliers_zscore = df[col].dropna()[z_scores > 3]
                
                print(f"   📊 {col}:")
                print(f"     • Outliers (IQR): {len(outliers_iqr)} ({len(outliers_iqr)/len(df)*100:.1f}%)")
                print(f"     • Outliers (Z-score): {len(outliers_zscore)} ({len(outliers_zscore)/len(df)*100:.1f}%)")
                print(f"     • Rango: [{df[col].min():.2f}, {df[col].max():.2f}]")
                
                outliers_info[col] = {
                    'iqr_count': len(outliers_iqr),
                    'iqr_percentage': len(outliers_iqr)/len(df)*100,
                    'zscore_count': len(outliers_zscore),
                    'zscore_percentage': len(outliers_zscore)/len(df)*100,
                    'range': [df[col].min(), df[col].max()]
                }
        
        return outliers_info
    
    def crear_histogramas(self, nombre_tabla, df):
        """Crear histogramas para columnas numéricas."""
        print(f"\n📊 CREANDO HISTOGRAMAS: {nombre_tabla.upper()}")
        print("-" * 50)
        
        columnas_numericas = df.select_dtypes(include=[np.number]).columns
        
        if len(columnas_numericas) == 0:
            print("   ⚠️ No hay columnas numéricas para histogramas")
            return
        
        # Calcular número de subplots
        n_cols = min(3, len(columnas_numericas))
        n_rows = (len(columnas_numericas) + n_cols - 1) // n_cols
        
        fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 5*n_rows))
        if n_rows == 1:
            axes = [axes] if n_cols == 1 else axes
        else:
            axes = axes.flatten()
        
        # Calcular estadísticas globales para interpretación
        estadisticas_globales = {}
        
        for i, col in enumerate(columnas_numericas):
            if i < len(axes):
                # Crear histograma
                datos_col = df[col].dropna()
                axes[i].hist(datos_col, bins=30, alpha=0.7, color='skyblue', edgecolor='black')
                
                # Calcular estadísticas y tipo de distribución
                media = datos_col.mean()
                mediana = datos_col.median()
                desv_std = datos_col.std()
                minimo = datos_col.min()
                maximo = datos_col.max()
                q25 = datos_col.quantile(0.25)
                q75 = datos_col.quantile(0.75)
                skewness = stats.skew(datos_col)
                kurtosis_val = stats.kurtosis(datos_col)
                
                # Guardar para interpretación
                estadisticas_globales[col] = {
                    'media': media,
                    'mediana': mediana,
                    'desv_std': desv_std,
                    'min': minimo,
                    'max': maximo,
                    'q25': q25,
                    'q75': q75,
                    'skewness': skewness,
                    'kurtosis': kurtosis_val,
                    'total': len(datos_col)
                }
                
                # Determinar tipo de distribución
                if abs(skewness) < 0.5:
                    tipo_dist = "Normal (Simétrica)"
                    color_dist = "green"
                elif skewness > 0.5:
                    tipo_dist = "Sesgada a la Derecha"
                    color_dist = "orange"
                elif skewness < -0.5:
                    tipo_dist = "Sesgada a la Izquierda"
                    color_dist = "purple"
                else:
                    tipo_dist = "Ligeramente Sesgada"
                    color_dist = "blue"
                
                # Agregar título con tipo de distribución
                axes[i].set_title(f'Distribución de {col}\nTipo: {tipo_dist}', 
                                 fontsize=12, fontweight='bold', color=color_dist)
                axes[i].set_xlabel(col)
                axes[i].set_ylabel('Frecuencia')
                axes[i].grid(True, alpha=0.3)
                
                # Agregar estadísticas
                axes[i].axvline(media, color='red', linestyle='--', label=f'Media: {media:.2f}')
                axes[i].axvline(mediana, color='green', linestyle='--', label=f'Mediana: {mediana:.2f}')
                
                # Agregar texto con estadísticas de forma
                texto_stats = f'Skew: {skewness:.2f} | Kurt: {kurtosis_val:.2f}'
                axes[i].text(0.02, 0.98, texto_stats, transform=axes[i].transAxes,
                           verticalalignment='top', bbox=dict(boxstyle='round', 
                           facecolor='wheat', alpha=0.8), fontsize=9)
                axes[i].legend(loc='upper right', fontsize=8)
        
        # Ocultar subplots vacíos
        for i in range(len(columnas_numericas), len(axes)):
            axes[i].set_visible(False)
        
        # Crear interpretación específica con valores reales
        interpretacion_lineas = ["INTERPRETACIÓN ESPECÍFICA:"]
        interpretacion_lineas.append(f"• Total de registros analizados: {len(df)}")
        
        for col, estadisticas in estadisticas_globales.items():
            interpretacion_lineas.append(f"\n{col.upper()}:")
            interpretacion_lineas.append(f"  - Media: {estadisticas['media']:.2f} | Mediana: {estadisticas['mediana']:.2f}")
            interpretacion_lineas.append(f"  - Rango: [{estadisticas['min']:.2f}, {estadisticas['max']:.2f}]")
            interpretacion_lineas.append(f"  - 50% de datos entre: {estadisticas['q25']:.2f} y {estadisticas['q75']:.2f}")
            if abs(estadisticas['skewness']) < 0.5:
                interpretacion_lineas.append(f"  - Distribución SIMÉTRICA (normal)")
            elif estadisticas['skewness'] > 0.5:
                interpretacion_lineas.append(f"  - Distribución SESGADA A LA DERECHA (más valores bajos)")
            else:
                interpretacion_lineas.append(f"  - Distribución SESGADA A LA IZQUIERDA (más valores altos)")
        
        interpretacion = "\n".join(interpretacion_lineas)
        fig.text(0.5, 0.01, interpretacion, ha='center', fontsize=7,
                bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8),
                wrap=True)
        
        plt.tight_layout()
        plt.subplots_adjust(bottom=0.15)
        
        # Guardar histograma
        nombre_archivo = f"resultados/histogramas/histogramas_{nombre_tabla}.png"
        plt.savefig(nombre_archivo, dpi=300, bbox_inches='tight')
        print(f"   💾 Histograma guardado: {nombre_archivo}")
        
        plt.close()
    
    def analizar_correlaciones(self, nombre_tabla, df):
        """Analizar correlaciones entre variables numéricas."""
        print(f"\n🔗 ANÁLISIS DE CORRELACIONES: {nombre_tabla.upper()}")
        print("-" * 50)
        
        columnas_numericas = df.select_dtypes(include=[np.number]).columns
        
        if len(columnas_numericas) < 2:
            print("   ⚠️ Se necesitan al menos 2 columnas numéricas para correlaciones")
            return None
        
        # Calcular matriz de correlación
        matriz_corr = df[columnas_numericas].corr()
        
        print("📊 Matriz de correlaciones:")
        print(matriz_corr.round(3))
        
        # Encontrar correlaciones fuertes
        print(f"\n🔍 CORRELACIONES FUERTES (|r| > 0.7):")
        correlaciones_fuertes = []
        for i in range(len(matriz_corr.columns)):
            for j in range(i+1, len(matriz_corr.columns)):
                corr_val = matriz_corr.iloc[i, j]
                if abs(corr_val) > 0.7:
                    var1 = matriz_corr.columns[i]
                    var2 = matriz_corr.columns[j]
                    print(f"   • {var1} ↔ {var2}: {corr_val:.3f}")
                    correlaciones_fuertes.append((var1, var2, corr_val))
        
        if not correlaciones_fuertes:
            print("   ℹ️ No se encontraron correlaciones fuertes")
        
        return matriz_corr
    
    def analisis_estadistico_medios_pago(self):
        """
        Realizar análisis estadístico detallado de medios de pago.
        
        Esta función calcula y muestra:
        1. Distribución de ventas por método de pago (frecuencia y porcentajes)
        2. Análisis de montos totales por método de pago
        3. Estadísticas descriptivas de importes por medio de pago
        4. Análisis temporal de preferencias de pago
        5. Visualizaciones completas
        6. Reporte detallado guardado en archivo
        """
        print(f"\n{'='*80}")
        print(f"💳 ANÁLISIS ESTADÍSTICO DETALLADO: MEDIOS DE PAGO")
        print(f"{'='*80}")
        
        # Verificar que las tablas necesarias estén cargadas
        if 'ventas' not in self.tablas or 'detalle_ventas' not in self.tablas:
            print("❌ Error: Las tablas 'ventas' y 'detalle_ventas' deben estar cargadas")
            return None
        
        df_ventas = self.tablas['ventas'].copy()
        df_detalle = self.tablas['detalle_ventas'].copy()
        
        # Verificar que existe la columna medio_pago
        if 'medio_pago' not in df_ventas.columns:
            print("❌ Error: La tabla 'ventas' no contiene la columna 'medio_pago'")
            return None
        
        # ============================================================
        # 1. ANÁLISIS DE DISTRIBUCIÓN DE VENTAS POR MÉTODO DE PAGO
        # ============================================================
        print(f"\n📊 1. DISTRIBUCIÓN DE VENTAS POR MÉTODO DE PAGO")
        print("-" * 60)
        
        # Agrupar ventas por método de pago
        distribucion_ventas = df_ventas.groupby('medio_pago').agg({
            'id_venta': 'count'
        }).rename(columns={'id_venta': 'numero_ventas'})
        
        # Ordenar por número de ventas (descendente)
        distribucion_ventas = distribucion_ventas.sort_values('numero_ventas', ascending=False)
        
        # Calcular porcentajes
        total_ventas = distribucion_ventas['numero_ventas'].sum()
        distribucion_ventas['porcentaje'] = (distribucion_ventas['numero_ventas'] / total_ventas) * 100
        
        # Mostrar resultados
        print(f"\n📈 Resumen por método de pago:")
        for metodo, row in distribucion_ventas.iterrows():
            print(f"   • {metodo.upper()}:")
            print(f"     - Número de ventas: {row['numero_ventas']}")
            print(f"     - Porcentaje: {row['porcentaje']:.2f}%")
        
        # ============================================================
        # 2. ANÁLISIS DE MONTOS TOTALES POR MÉTODO DE PAGO
        # ============================================================
        print(f"\n💰 2. ANÁLISIS DE MONTOS TOTALES POR MÉTODO DE PAGO")
        print("-" * 60)
        
        # Unir ventas con detalle_ventas para obtener montos
        df_completo = df_ventas.merge(df_detalle, on='id_venta', how='inner')
        
        # Calcular montos totales por método de pago
        montos_por_metodo = df_completo.groupby('medio_pago').agg({
            'importe': ['sum', 'mean', 'median', 'std', 'min', 'max', 'count']
        }).round(2)
        
        montos_por_metodo.columns = ['total', 'promedio', 'mediana', 'desv_std', 'minimo', 'maximo', 'cantidad']
        montos_por_metodo = montos_por_metodo.sort_values('total', ascending=False)
        
        # Calcular porcentaje del total por método
        total_general = montos_por_metodo['total'].sum()
        montos_por_metodo['porcentaje_total'] = (montos_por_metodo['total'] / total_general) * 100
        
        print(f"\n💵 Estadísticas de importes por método de pago:")
        print(montos_por_metodo.to_string())
        
        # ============================================================
        # 3. ESTADÍSTICAS DESCRIPTIVAS DETALLADAS
        # ============================================================
        print(f"\n📈 3. ESTADÍSTICAS DESCRIPTIVAS DETALLADAS")
        print("-" * 60)
        
        estadisticas_detalladas = {}
        for metodo in df_ventas['medio_pago'].unique():
            # Filtrar importes por método de pago
            importes_metodo = df_completo[df_completo['medio_pago'] == metodo]['importe']
            
            if len(importes_metodo) > 0:
                # Calcular estadísticas
                estadisticas = {
                    'count': len(importes_metodo),
                    'mean': importes_metodo.mean(),
                    'median': importes_metodo.median(),
                    'std': importes_metodo.std(),
                    'min': importes_metodo.min(),
                    'max': importes_metodo.max(),
                    'q25': importes_metodo.quantile(0.25),
                    'q75': importes_metodo.quantile(0.75),
                    'skewness': stats.skew(importes_metodo),
                    'kurtosis': stats.kurtosis(importes_metodo)
                }
                
                estadisticas_detalladas[metodo] = estadisticas
                
                print(f"\n   📊 {metodo.upper()}:")
                print(f"     • Cantidad de transacciones: {estadisticas['count']}")
                print(f"     • Media: ${estadisticas['mean']:.2f}")
                print(f"     • Mediana: ${estadisticas['median']:.2f}")
                print(f"     • Desviación estándar: ${estadisticas['std']:.2f}")
                print(f"     • Mínimo: ${estadisticas['min']:.2f}")
                print(f"     • Máximo: ${estadisticas['max']:.2f}")
                print(f"     • Q1 (25%): ${estadisticas['q25']:.2f}")
                print(f"     • Q3 (75%): ${estadisticas['q75']:.2f}")
                print(f"     • Asimetría (Skewness): {estadisticas['skewness']:.3f}")
                print(f"     • Curtosis: {estadisticas['kurtosis']:.3f}")
        
        # ============================================================
        # 4. ANÁLISIS TEMPORAL DE PREFERENCIAS DE PAGO
        # ============================================================
        print(f"\n📅 4. ANÁLISIS TEMPORAL DE PREFERENCIAS DE PAGO")
        print("-" * 60)
        
        ventas_por_mes = None
        ventas_por_año = None
        
        # Verificar si existe columna de fecha
        if 'fecha' in df_ventas.columns:
            try:
                # Crear copia para análisis temporal
                df_ventas_temp = df_ventas.copy()
                
                # Convertir fecha a datetime si no lo es
                df_ventas_temp['fecha'] = pd.to_datetime(df_ventas_temp['fecha'])
                
                # Agregar columnas de año y mes
                df_ventas_temp['año'] = df_ventas_temp['fecha'].dt.year
                df_ventas_temp['mes'] = df_ventas_temp['fecha'].dt.month
                df_ventas_temp['mes_año'] = df_ventas_temp['fecha'].dt.to_period('M')
                
                # Análisis por mes
                ventas_por_mes = df_ventas_temp.groupby(['mes_año', 'medio_pago']).size().unstack(fill_value=0)
                
                print(f"\n📊 Distribución de ventas por mes y método de pago:")
                print(ventas_por_mes.to_string())
                
                # Análisis por año
                ventas_por_año = df_ventas_temp.groupby(['año', 'medio_pago']).size().unstack(fill_value=0)
                
                print(f"\n📊 Distribución de ventas por año y método de pago:")
                print(ventas_por_año.to_string())
                
            except Exception as e:
                print(f"   ⚠️ No se pudo realizar análisis temporal: {e}")
        else:
            print("   ℹ️ No se encontró columna de fecha para análisis temporal")
        
        # ============================================================
        # 5. CREAR VISUALIZACIONES
        # ============================================================
        print(f"\n📊 5. CREANDO VISUALIZACIONES")
        print("-" * 60)
        
        try:
            # Crear figura con múltiples subplots
            fig = plt.figure(figsize=(18, 12))
            
            # Subplot 1: Gráfico de barras - Número de ventas por método
            ax1 = plt.subplot(2, 3, 1)
            distribucion_ventas['numero_ventas'].plot(kind='bar', color='skyblue', edgecolor='black', ax=ax1)
            ax1.set_title('Número de Ventas por Método de Pago', fontsize=12, fontweight='bold')
            ax1.set_xlabel('Método de Pago')
            ax1.set_ylabel('Cantidad de Ventas')
            ax1.set_xticklabels(ax1.get_xticklabels(), rotation=45, ha='right')
            ax1.grid(True, alpha=0.3)
            
            # Agregar valores en las barras
            for i, v in enumerate(distribucion_ventas['numero_ventas']):
                ax1.text(i, v, str(int(v)), ha='center', va='bottom', fontweight='bold')
            
            # Agregar interpretación al gráfico 1
            ax1.text(0.02, 0.98, 'Interpretación: La altura de cada barra muestra\ncuántas ventas se hicieron con ese método de pago.',
                    transform=ax1.transAxes, verticalalignment='top', fontsize=8,
                    bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.7))
            
            # Subplot 2: Gráfico de pastel - Porcentaje de ventas
            ax2 = plt.subplot(2, 3, 2)
            distribucion_ventas['porcentaje'].plot(kind='pie', autopct='%1.1f%%', startangle=90, ax=ax2, labels=distribucion_ventas.index)
            ax2.set_title('Distribución Porcentual de Ventas', fontsize=12, fontweight='bold')
            ax2.set_ylabel('')
            
            # Agregar interpretación al gráfico 2
            ax2.text(0.5, -0.15, 'Interpretación: Cada porción muestra qué porcentaje\ndel total de ventas corresponde a cada método.',
                    transform=ax2.transAxes, ha='center', fontsize=8,
                    bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.7))
            
            # Subplot 3: Gráfico de barras - Montos totales por método
            ax3 = plt.subplot(2, 3, 3)
            montos_por_metodo['total'].plot(kind='bar', color='lightgreen', edgecolor='black', ax=ax3)
            ax3.set_title('Montos Totales por Método de Pago', fontsize=12, fontweight='bold')
            ax3.set_xlabel('Método de Pago')
            ax3.set_ylabel('Monto Total ($)')
            ax3.set_xticklabels(ax3.get_xticklabels(), rotation=45, ha='right')
            ax3.grid(True, alpha=0.3)
            
            # Subplot 4: Gráfico de barras - Monto promedio por método
            ax4 = plt.subplot(2, 3, 4)
            montos_por_metodo['promedio'].plot(kind='bar', color='coral', edgecolor='black', ax=ax4)
            ax4.set_title('Monto Promedio por Transacción', fontsize=12, fontweight='bold')
            ax4.set_xlabel('Método de Pago')
            ax4.set_ylabel('Monto Promedio ($)')
            ax4.set_xticklabels(ax4.get_xticklabels(), rotation=45, ha='right')
            ax4.grid(True, alpha=0.3)
            
            # Subplot 5: Boxplot - Distribución de importes por método
            ax5 = plt.subplot(2, 3, 5)
            datos_boxplot = [df_completo[df_completo['medio_pago'] == metodo]['importe'].values 
                           for metodo in distribucion_ventas.index]
            ax5.boxplot(datos_boxplot, labels=distribucion_ventas.index)
            ax5.set_title('Distribución de Importes por Método', fontsize=12, fontweight='bold')
            ax5.set_xlabel('Método de Pago')
            ax5.set_ylabel('Importe ($)')
            ax5.set_xticklabels(ax5.get_xticklabels(), rotation=45, ha='right')
            ax5.grid(True, alpha=0.3)
            
            # Subplot 6: Gráfico de barras apiladas - Porcentaje del total
            ax6 = plt.subplot(2, 3, 6)
            montos_por_metodo['porcentaje_total'].plot(kind='bar', color='plum', edgecolor='black', ax=ax6)
            ax6.set_title('Porcentaje del Total por Método', fontsize=12, fontweight='bold')
            ax6.set_xlabel('Método de Pago')
            ax6.set_ylabel('Porcentaje del Total (%)')
            ax6.set_xticklabels(ax6.get_xticklabels(), rotation=45, ha='right')
            ax6.grid(True, alpha=0.3)
            
            # Agregar valores en las barras
            for i, v in enumerate(montos_por_metodo['porcentaje_total']):
                ax6.text(i, v, f'{v:.1f}%', ha='center', va='bottom', fontweight='bold')
            
            # Crear interpretación específica con valores reales
            metodo_mas_ventas = distribucion_ventas.index[0]
            metodo_mas_monto = montos_por_metodo.index[0]
            metodo_mayor_promedio = montos_por_metodo['promedio'].idxmax()
            
            # Determinar conclusión según si los métodos coinciden o no
            if metodo_mas_ventas == metodo_mayor_promedio:
                # Si el mismo método es el más usado Y tiene mayor promedio
                conclusion = f"CONCLUSIÓN: {metodo_mas_ventas} es el método más usado ({distribucion_ventas.loc[metodo_mas_ventas, 'numero_ventas']} transacciones, {distribucion_ventas.loc[metodo_mas_ventas, 'porcentaje']:.1f}%) Y también genera el mayor valor por transacción (${montos_por_metodo.loc[metodo_mayor_promedio, 'promedio']:.2f} por transacción). Es el método dominante en ambos aspectos."
            else:
                # Si son diferentes métodos
                conclusion = f"CONCLUSIÓN: {metodo_mas_ventas} es el método más usado ({distribucion_ventas.loc[metodo_mas_ventas, 'numero_ventas']} transacciones, {distribucion_ventas.loc[metodo_mas_ventas, 'porcentaje']:.1f}%), mientras que {metodo_mayor_promedio} genera mayor valor por transacción (${montos_por_metodo.loc[metodo_mayor_promedio, 'promedio']:.2f} por transacción)."
            
            interpretacion_general = (
                f"INTERPRETACIÓN ESPECÍFICA:\n"
                f"• GRÁFICO 1: {metodo_mas_ventas} tiene MÁS ventas ({distribucion_ventas.loc[metodo_mas_ventas, 'numero_ventas']} transacciones, {distribucion_ventas.loc[metodo_mas_ventas, 'porcentaje']:.1f}%)\n"
                f"• GRÁFICO 2: {metodo_mas_ventas} representa {distribucion_ventas.loc[metodo_mas_ventas, 'porcentaje']:.1f}% del total de ventas\n"
                f"• GRÁFICO 3: {metodo_mas_monto} genera MÁS dinero total (${montos_por_metodo.loc[metodo_mas_monto, 'total']:,.2f})\n"
                f"• GRÁFICO 4: {metodo_mayor_promedio} tiene MAYOR ticket promedio (${montos_por_metodo.loc[metodo_mayor_promedio, 'promedio']:.2f} por transacción)\n"
                f"• GRÁFICO 5: Distribución de importes - {metodo_mayor_promedio} tiene mayor variabilidad\n"
                f"• GRÁFICO 6: {metodo_mas_monto} representa {montos_por_metodo.loc[metodo_mas_monto, 'porcentaje_total']:.1f}% del monto total\n"
                f"• {conclusion}"
            )
            fig.text(0.5, 0.01, interpretacion_general, ha='center', fontsize=7,
                    bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8),
                    wrap=True)
            
            plt.tight_layout()
            plt.subplots_adjust(bottom=0.2)
            
            # Guardar visualización
            nombre_archivo = "resultados/histogramas/analisis_medios_pago.png"
            plt.savefig(nombre_archivo, dpi=300, bbox_inches='tight')
            print(f"   💾 Visualización guardada: {nombre_archivo}")
            
            plt.close()
            
        except Exception as e:
            print(f"   ⚠️ Error al crear visualizaciones: {e}")
        
        # ============================================================
        # 6. GUARDAR REPORTE DETALLADO
        # ============================================================
        print(f"\n💾 6. GUARDANDO REPORTE DETALLADO")
        print("-" * 60)
        
        try:
            archivo_reporte = "resultados/estadisticas/analisis_medios_pago.txt"
            with open(archivo_reporte, 'w', encoding='utf-8') as f:
                f.write("ANÁLISIS ESTADÍSTICO DETALLADO: MEDIOS DE PAGO\n")
                f.write("=" * 80 + "\n\n")
                
                f.write("1. DISTRIBUCIÓN DE VENTAS POR MÉTODO DE PAGO\n")
                f.write("-" * 80 + "\n")
                f.write(f"Total de ventas analizadas: {total_ventas}\n\n")
                for metodo, row in distribucion_ventas.iterrows():
                    f.write(f"{metodo.upper()}:\n")
                    f.write(f"  - Número de ventas: {row['numero_ventas']}\n")
                    f.write(f"  - Porcentaje: {row['porcentaje']:.2f}%\n\n")
                
                f.write("\n2. ANÁLISIS DE MONTOS TOTALES POR MÉTODO DE PAGO\n")
                f.write("-" * 80 + "\n")
                f.write(f"Monto total general: ${total_general:,.2f}\n\n")
                f.write(montos_por_metodo.to_string())
                f.write("\n\n")
                
                f.write("3. ESTADÍSTICAS DESCRIPTIVAS DETALLADAS\n")
                f.write("-" * 80 + "\n")
                for metodo, stats_dict in estadisticas_detalladas.items():
                    f.write(f"\n{metodo.upper()}:\n")
                    f.write(f"  - Cantidad de transacciones: {stats_dict['count']}\n")
                    f.write(f"  - Media: ${stats_dict['mean']:.2f}\n")
                    f.write(f"  - Mediana: ${stats_dict['median']:.2f}\n")
                    f.write(f"  - Desviación estándar: ${stats_dict['std']:.2f}\n")
                    f.write(f"  - Mínimo: ${stats_dict['min']:.2f}\n")
                    f.write(f"  - Máximo: ${stats_dict['max']:.2f}\n")
                    f.write(f"  - Q1 (25%): ${stats_dict['q25']:.2f}\n")
                    f.write(f"  - Q3 (75%): ${stats_dict['q75']:.2f}\n")
                    f.write(f"  - Asimetría (Skewness): {stats_dict['skewness']:.3f}\n")
                    f.write(f"  - Curtosis: {stats_dict['kurtosis']:.3f}\n")
                
                # Agregar análisis temporal si está disponible
                if ventas_por_mes is not None and ventas_por_año is not None:
                    try:
                        f.write("\n\n4. ANÁLISIS TEMPORAL DE PREFERENCIAS DE PAGO\n")
                        f.write("-" * 80 + "\n")
                        f.write("\nDistribución por mes:\n")
                        f.write(ventas_por_mes.to_string())
                        f.write("\n\nDistribución por año:\n")
                        f.write(ventas_por_año.to_string())
                        f.write("\n")
                    except:
                        pass
                
                f.write("\n\n" + "=" * 80 + "\n")
                f.write("Reporte generado automáticamente por el sistema de análisis\n")
                f.write("=" * 80 + "\n")
            
            print(f"   💾 Reporte guardado: {archivo_reporte}")
            
        except Exception as e:
            print(f"   ⚠️ Error al guardar reporte: {e}")
        
        # Compilar resultados
        resultados = {
            'distribucion_ventas': distribucion_ventas,
            'montos_por_metodo': montos_por_metodo,
            'estadisticas_detalladas': estadisticas_detalladas
        }
        
        print(f"\n✅ Análisis estadístico de medios de pago completado exitosamente!")
        return resultados
    
    def generar_reporte_tabla(self, nombre_tabla, df):
        """Generar reporte completo para una tabla."""
        print(f"\n{'='*80}")
        print(f"📋 REPORTE COMPLETO: {nombre_tabla.upper()}")
        print(f"{'='*80}")
        
        # Análisis estadístico descriptivo
        stats_info = self.analisis_estadistico_descriptivo(nombre_tabla, df)
        
        # Detección de outliers
        outliers_info = self.detectar_outliers(nombre_tabla, df)
        
        # Crear histogramas
        self.crear_histogramas(nombre_tabla, df)
        
        # Análisis de correlaciones
        correlaciones = self.analizar_correlaciones(nombre_tabla, df)
        
        # Guardar resultados
        self.guardar_resultados_tabla(nombre_tabla, {
            'estadisticas': stats_info,
            'outliers': outliers_info,
            'correlaciones': correlaciones
        })
        
        return {
            'estadisticas': stats_info,
            'outliers': outliers_info,
            'correlaciones': correlaciones
        }
    
    def guardar_resultados_tabla(self, nombre_tabla, resultados):
        """Guardar resultados del análisis en archivos."""
        try:
            # Guardar estadísticas descriptivas
            if resultados['estadisticas']['estadisticas'] is not None:
                archivo_stats = f"resultados/estadisticas/stats_{nombre_tabla}.csv"
                resultados['estadisticas']['estadisticas'].to_csv(archivo_stats)
                print(f"   💾 Estadísticas guardadas: {archivo_stats}")
            
            # Guardar información de outliers
            if resultados['outliers']:
                archivo_outliers = f"resultados/estadisticas/outliers_{nombre_tabla}.txt"
                with open(archivo_outliers, 'w', encoding='utf-8') as f:
                    f.write(f"ANÁLISIS DE OUTLIERS - {nombre_tabla.upper()}\n")
                    f.write("=" * 50 + "\n\n")
                    for col, info in resultados['outliers'].items():
                        f.write(f"Columna: {col}\n")
                        f.write(f"  Outliers IQR: {info['iqr_count']} ({info['iqr_percentage']:.1f}%)\n")
                        f.write(f"  Outliers Z-score: {info['zscore_count']} ({info['zscore_percentage']:.1f}%)\n")
                        f.write(f"  Rango: [{info['range'][0]:.2f}, {info['range'][1]:.2f}]\n\n")
                print(f"   💾 Outliers guardados: {archivo_outliers}")
            
            # Guardar correlaciones
            if resultados['correlaciones'] is not None:
                archivo_corr = f"resultados/estadisticas/correlaciones_{nombre_tabla}.csv"
                resultados['correlaciones'].to_csv(archivo_corr)
                print(f"   💾 Correlaciones guardadas: {archivo_corr}")
                
        except Exception as e:
            print(f"❌ Error al guardar resultados: {e}")
    
    def ejecutar_analisis_completo(self):
        """Ejecutar análisis exploratorio completo."""
        print("🔍 ANÁLISIS EXPLORATORIO DE DATOS (EDA) - AURELION")
        print("Grupo 11 - Camada 1 | Enith Gicela Vargas Vargas")
        print("=" * 80)
        
        # Cargar tablas
        if not self.cargar_tablas():
            return False
        
        # Analizar cada tabla
        for nombre_tabla, df in self.tablas.items():
            self.generar_reporte_tabla(nombre_tabla, df)
        
        # Realizar análisis estadístico detallado de medios de pago
        self.analisis_estadistico_medios_pago()
        
        print(f"\n✅ Análisis exploratorio completado exitosamente!")
        print(f"📁 Resultados guardados en: resultados/")
        return True

def main():
    """Función principal del análisis exploratorio."""
    analizador = AnalisisExploratorio()
    analizador.ejecutar_analisis_completo()

if __name__ == "__main__":
    main()
