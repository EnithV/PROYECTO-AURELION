#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VISUALIZACIONES AVANZADAS - PROYECTO AURELION SPRINT_2
======================================================

**Autor:** Enith Gicela Vargas Vargas  
**Camada:** 1  
**Grupo:** 11  
**Fecha:** 2025-10-27  
**Curso:** AI Fundamentals - Guayerd - IBM Skills Build  
**Sprint:** 2 - Machine Learning y Normalización  
**Módulo:** Visualizaciones Avanzadas  

Script para crear visualizaciones avanzadas del proyecto de normalizacion,
incluyendo:
- Comparacion antes/despues de normalizacion
- Matrices de correlacion
- Distribuciones de variables
- Analisis de outliers
- Visualizaciones del dataset final
"""

import pandas as pd          # Manipulación y análisis de datos estructurados
import numpy as np           # Operaciones numéricas y matemáticas
import matplotlib.pyplot as plt  # Interfaz de matplotlib para crear gráficos
import seaborn as sns       # Librería para visualizaciones estadísticas avanzadas
from matplotlib.patches import Rectangle  # Módulo para formas geométricas en matplotlib
from scipy import stats     # Módulo de SciPy para análisis estadístico
import warnings             # Módulo para controlar avisos del sistema
warnings.filterwarnings('ignore')

# Configurar estilo de matplotlib para gráficos consistentes
plt.style.use('default')

# Configurar paleta de colores de seaborn (husl: tono, saturación, luminosidad)
sns.set_palette("husl")

class VisualizacionesAvanzadas:
    """
    Clase para crear visualizaciones avanzadas del proyecto.
    
    Funcionalidades:
    - Comparacion antes/despues normalizacion
    - Matrices de correlacion
    - Distribuciones y boxplots
    - Analisis de outliers
    - Visualizaciones del dataset final
    """
    
    def __init__(self):
        """Inicializar el visualizador."""
        self.base_path = "../../Datos Proyecto/Base de datos_Tienda_Aurelion/Base de datos"
        self.tablas_originales = {}
        self.tablas_normalizadas = {}
        self.dataset_final = None
        
    def cargar_datos(self):
        """Cargar datos originales y normalizados."""
        print("CARGANDO DATOS PARA VISUALIZACIONES")
        print("=" * 50)
        
        try:
            # Cargar tablas originales
            self.tablas_originales['clientes'] = pd.read_excel(f"{self.base_path}/clientes.xlsx")
            self.tablas_originales['productos'] = pd.read_excel(f"{self.base_path}/productos.xlsx")
            self.tablas_originales['ventas'] = pd.read_excel(f"{self.base_path}/ventas.xlsx")
            self.tablas_originales['detalle_ventas'] = pd.read_excel(f"{self.base_path}/detalle_ventas.xlsx")
            
            # Cargar tablas normalizadas
            self.tablas_normalizadas['clientes'] = pd.read_csv("resultados/datasets_normalizados/clientes_normalizada.csv")
            self.tablas_normalizadas['productos'] = pd.read_csv("resultados/datasets_normalizados/productos_normalizada.csv")
            self.tablas_normalizadas['ventas'] = pd.read_csv("resultados/datasets_normalizados/ventas_normalizada.csv")
            self.tablas_normalizadas['detalle_ventas'] = pd.read_csv("resultados/datasets_normalizados/detalle_ventas_normalizada.csv")
            
            # Cargar dataset final
            self.dataset_final = pd.read_csv("resultados/datasets_normalizados/dataset_final_completo.csv")
            
            print("Datos cargados exitosamente!")
            return True
            
        except Exception as e:
            print(f"Error al cargar datos: {e}")
            return False
    
    def crear_comparacion_normalizacion(self):
        """Crear comparacion antes/despues de normalizacion."""
        print("\nCREANDO COMPARACION DE NORMALIZACION")
        print("-" * 45)
        
        # Variables numericas importantes para comparar
        variables_comparar = {
            'productos': ['precio_unitario'],
            'detalle_ventas': ['cantidad', 'precio_unitario', 'importe']
        }
        
        for tabla, variables in variables_comparar.items():
            if tabla in self.tablas_originales and tabla in self.tablas_normalizadas:
                fig, axes = plt.subplots(2, len(variables), figsize=(5*len(variables), 8))
                if len(variables) == 1:
                    axes = axes.reshape(-1, 1)
                
                # Calcular estadísticas para interpretación
                stats_antes = {}
                stats_despues = {}
                
                for i, var in enumerate(variables):
                    if var in self.tablas_originales[tabla].columns:
                        datos_antes = self.tablas_originales[tabla][var].dropna()
                        # Antes de normalizacion
                        axes[0, i].hist(datos_antes, 
                                       bins=20, alpha=0.7, color='skyblue', edgecolor='black')
                        axes[0, i].set_title(f'{var} - ANTES\n(Original)', fontsize=10, fontweight='bold')
                        axes[0, i].set_xlabel(var)
                        axes[0, i].set_ylabel('Frecuencia')
                        
                        # Guardar estadísticas antes
                        stats_antes[var] = {
                            'min': datos_antes.min(),
                            'max': datos_antes.max(),
                            'media': datos_antes.mean(),
                            'std': datos_antes.std()
                        }
                        
                        # Despues de normalizacion
                        if var in self.tablas_normalizadas[tabla].columns:
                            datos_despues = self.tablas_normalizadas[tabla][var].dropna()
                            axes[1, i].hist(datos_despues, 
                                           bins=20, alpha=0.7, color='lightcoral', edgecolor='black')
                            axes[1, i].set_title(f'{var} - DESPUES\n(Normalizado)', fontsize=10, fontweight='bold')
                            axes[1, i].set_xlabel(var)
                            axes[1, i].set_ylabel('Frecuencia')
                            
                            # Guardar estadísticas después
                            stats_despues[var] = {
                                'min': datos_despues.min(),
                                'max': datos_despues.max(),
                                'media': datos_despues.mean(),
                                'std': datos_despues.std()
                            }
                
                plt.suptitle(f'COMPARACION DE NORMALIZACION - {tabla.upper()}', 
                           fontsize=14, fontweight='bold', y=0.98)
                
                # Crear interpretación específica con valores reales
                interpretacion_lineas = ["INTERPRETACIÓN ESPECÍFICA:"]
                for var in variables:
                    if var in stats_antes and var in stats_despues:
                        interpretacion_lineas.append(f"\n{var.upper()}:")
                        interpretacion_lineas.append(f"  ANTES: Rango [{stats_antes[var]['min']:.2f}, {stats_antes[var]['max']:.2f}], Media={stats_antes[var]['media']:.2f}")
                        interpretacion_lineas.append(f"  DESPUÉS: Rango [{stats_despues[var]['min']:.2f}, {stats_despues[var]['max']:.2f}], Media={stats_despues[var]['media']:.2f}")
                        reduccion_rango = ((stats_antes[var]['max'] - stats_antes[var]['min']) / (stats_despues[var]['max'] - stats_despues[var]['min'])) if (stats_despues[var]['max'] - stats_despues[var]['min']) > 0 else 1
                        interpretacion_lineas.append(f"  CONCLUSIÓN: Rango reducido {reduccion_rango:.1f}x, valores ahora entre 0-1 (normalizado)")
                
                interpretacion = "\n".join(interpretacion_lineas)
                fig.text(0.5, 0.01, interpretacion, ha='center', fontsize=7,
                        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8),
                        wrap=True)
                
                plt.tight_layout()
                plt.subplots_adjust(bottom=0.15)
                
                # Guardar grafico
                archivo = f"resultados/histogramas/comparacion_normalizacion_{tabla}.png"
                plt.savefig(archivo, dpi=300, bbox_inches='tight')
                print(f"   Grafico guardado: {archivo}")
                plt.close()
    
    def crear_matrices_correlacion(self):
        """Crear matrices de correlacion."""
        print("\nCREANDO MATRICES DE CORRELACION")
        print("-" * 40)
        
        # Dataset final - matriz de correlacion completa
        if self.dataset_final is not None:
            # Seleccionar solo variables numericas
            variables_numericas = self.dataset_final.select_dtypes(include=[np.number]).columns
            
            if len(variables_numericas) > 1:
                # Crear matriz de correlacion
                corr_matrix = self.dataset_final[variables_numericas].corr()
                
                # Grafico de matriz de correlacion
                plt.figure(figsize=(12, 10))
                mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
                sns.heatmap(corr_matrix, mask=mask, annot=True, cmap='coolwarm', center=0,
                           square=True, fmt='.2f', cbar_kws={"shrink": .8})
                plt.title('MATRIZ DE CORRELACION - DATASET FINAL', 
                         fontsize=16, fontweight='bold', pad=20)
                
                # Encontrar correlaciones más fuertes para interpretación
                correlaciones_fuertes = []
                for i in range(len(corr_matrix.columns)):
                    for j in range(i+1, len(corr_matrix.columns)):
                        corr_val = corr_matrix.iloc[i, j]
                        if abs(corr_val) > 0.7:
                            correlaciones_fuertes.append((
                                corr_matrix.columns[i],
                                corr_matrix.columns[j],
                                corr_val
                            ))
                
                # Ordenar por valor absoluto
                correlaciones_fuertes.sort(key=lambda x: abs(x[2]), reverse=True)
                
                # Crear interpretación específica
                interpretacion_lineas = ["INTERPRETACIÓN ESPECÍFICA:"]
                if correlaciones_fuertes:
                    interpretacion_lineas.append("CORRELACIONES FUERTES IDENTIFICADAS (|r| > 0.7):")
                    for var1, var2, corr_val in correlaciones_fuertes[:5]:  # Top 5
                        tipo = "POSITIVA" if corr_val > 0 else "NEGATIVA"
                        interpretacion_lineas.append(f"  • {var1} ↔ {var2}: r = {corr_val:.3f} ({tipo})")
                    interpretacion_lineas.append(f"\nCONCLUSIÓN: Se encontraron {len(correlaciones_fuertes)} pares con correlación fuerte.")
                    if correlaciones_fuertes[0][2] > 0.9:
                        interpretacion_lineas.append(f"  La relación más fuerte es {correlaciones_fuertes[0][0]} ↔ {correlaciones_fuertes[0][1]} (r={correlaciones_fuertes[0][2]:.3f})")
                else:
                    interpretacion_lineas.append("No se encontraron correlaciones fuertes (|r| > 0.7)")
                    interpretacion_lineas.append("Las variables son relativamente independientes entre sí.")
                
                interpretacion = "\n".join(interpretacion_lineas)
                plt.figtext(0.5, 0.02, interpretacion, ha='center', fontsize=8,
                           bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8),
                           wrap=True)
                
                plt.tight_layout()
                plt.subplots_adjust(bottom=0.2)
                
                # Guardar grafico
                archivo = "resultados/histogramas/matriz_correlacion_final.png"
                plt.savefig(archivo, dpi=300, bbox_inches='tight')
                print(f"   Matriz de correlacion guardada: {archivo}")
                plt.close()
    
    def crear_analisis_distribuciones(self):
        """Crear analisis de distribuciones."""
        print("\nCREANDO ANALISIS DE DISTRIBUCIONES")
        print("-" * 40)
        
        if self.dataset_final is not None:
            # Variables numericas principales
            variables_principales = ['cantidad', 'precio_unitario_detalle', 'importe']
            variables_disponibles = [v for v in variables_principales if v in self.dataset_final.columns]
            
            if variables_disponibles:
                fig, axes = plt.subplots(2, len(variables_disponibles), figsize=(5*len(variables_disponibles), 10))
                if len(variables_disponibles) == 1:
                    axes = axes.reshape(-1, 1)
                
                # Calcular estadísticas para interpretación
                stats_distribuciones = {}
                
                for i, var in enumerate(variables_disponibles):
                    # Histograma con tipo de distribucion
                    datos_var = self.dataset_final[var].dropna()
                    axes[0, i].hist(datos_var, bins=20, alpha=0.7, 
                                   color='lightgreen', edgecolor='black')
                    
                    # Calcular estadisticas de forma
                    media = datos_var.mean()
                    mediana = datos_var.median()
                    q25 = datos_var.quantile(0.25)
                    q75 = datos_var.quantile(0.75)
                    skewness = stats.skew(datos_var)
                    kurtosis_val = stats.kurtosis(datos_var)
                    
                    # Guardar para interpretación
                    stats_distribuciones[var] = {
                        'media': media,
                        'mediana': mediana,
                        'q25': q25,
                        'q75': q75,
                        'skewness': skewness,
                        'kurtosis': kurtosis_val
                    }
                    
                    # Determinar tipo de distribucion
                    if abs(skewness) < 0.5:
                        tipo_dist = "Normal (Simetrica)"
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
                    
                    axes[0, i].set_title(f'Distribucion de {var}\nTipo: {tipo_dist}', 
                                        fontweight='bold', color=color_dist, fontsize=10)
                    axes[0, i].set_xlabel(var)
                    axes[0, i].set_ylabel('Frecuencia')
                    
                    # Agregar estadisticas de forma
                    texto = f'Skew: {skewness:.2f} | Kurt: {kurtosis_val:.2f}'
                    axes[0, i].text(0.02, 0.98, texto, transform=axes[0, i].transAxes,
                                  verticalalignment='top', fontsize=8,
                                  bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.7))
                    
                    # Boxplot
                    axes[1, i].boxplot(self.dataset_final[var].dropna(), patch_artist=True,
                                      boxprops=dict(facecolor='lightblue', alpha=0.7))
                    axes[1, i].set_title(f'Boxplot de {var}', fontweight='bold')
                    axes[1, i].set_ylabel(var)
                
                plt.suptitle('ANALISIS DE DISTRIBUCIONES - DATASET FINAL', 
                           fontsize=14, fontweight='bold', y=0.98)
                
                # Crear interpretación específica
                interpretacion_lineas = ["INTERPRETACIÓN ESPECÍFICA:"]
                for var, estadisticas in stats_distribuciones.items():
                    interpretacion_lineas.append(f"\n{var.upper()}:")
                    interpretacion_lineas.append(f"  Media: {estadisticas['media']:.2f} | Mediana: {estadisticas['mediana']:.2f}")
                    interpretacion_lineas.append(f"  50% de datos entre: {estadisticas['q25']:.2f} y {estadisticas['q75']:.2f}")
                    if abs(estadisticas['skewness']) < 0.5:
                        interpretacion_lineas.append(f"  Tipo: SIMÉTRICA (normal) - Skewness: {estadisticas['skewness']:.2f}")
                    elif estadisticas['skewness'] > 0.5:
                        interpretacion_lineas.append(f"  Tipo: SESGADA DERECHA - Skewness: {estadisticas['skewness']:.2f} (más valores bajos)")
                    else:
                        interpretacion_lineas.append(f"  Tipo: SESGADA IZQUIERDA - Skewness: {estadisticas['skewness']:.2f} (más valores altos)")
                
                interpretacion = "\n".join(interpretacion_lineas)
                fig.text(0.5, 0.01, interpretacion, ha='center', fontsize=7,
                        bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.8),
                        wrap=True)
                
                plt.tight_layout()
                plt.subplots_adjust(bottom=0.18)
                
                # Guardar grafico
                archivo = "resultados/histogramas/analisis_distribuciones.png"
                plt.savefig(archivo, dpi=300, bbox_inches='tight')
                print(f"   Analisis de distribuciones guardado: {archivo}")
                plt.close()
    
    def crear_analisis_categoricas(self):
        """Crear analisis de variables categoricas."""
        print("\nCREANDO ANALISIS DE VARIABLES CATEGORICAS")
        print("-" * 50)
        
        if self.dataset_final is not None:
            # Variables categoricas importantes
            variables_categoricas = ['ciudad', 'categoria_Alimentos', 'categoria_Limpieza', 'medio_pago']
            variables_disponibles = [v for v in variables_categoricas if v in self.dataset_final.columns]
            
            if variables_disponibles:
                # Crear un grafico por variable
                for var in variables_disponibles:
                    plt.figure(figsize=(10, 6))
                    
                    # Contar valores
                    conteo = self.dataset_final[var].value_counts().sort_index()
                    total = conteo.sum()
                    
                    # Calcular porcentajes
                    porcentajes = (conteo / total * 100).round(1)
                    
                    # Identificar categoría más y menos frecuente
                    categoria_mas_frecuente = conteo.idxmax()
                    frecuencia_max = conteo.max()
                    porcentaje_max = porcentajes[categoria_mas_frecuente]
                    
                    categoria_menos_frecuente = conteo.idxmin()
                    frecuencia_min = conteo.min()
                    porcentaje_min = porcentajes[categoria_menos_frecuente]
                    
                    # Grafico de barras
                    plt.bar(range(len(conteo)), conteo.values, color='lightcoral', alpha=0.8)
                    plt.title(f'Distribucion de {var}', fontweight='bold', fontsize=14)
                    plt.xlabel(var, fontsize=12)
                    plt.ylabel('Frecuencia', fontsize=12)
                    plt.xticks(range(len(conteo)), conteo.index, rotation=45)
                    plt.grid(axis='y', alpha=0.3)
                    
                    # Agregar valores en las barras
                    for i, (idx, val) in enumerate(conteo.items()):
                        plt.text(i, val, f'{int(val)}\n({porcentajes[idx]}%)', 
                                ha='center', va='bottom', fontweight='bold', fontsize=9)
                    
                    # Crear interpretación específica con valores reales
                    interpretacion = (
                        f"INTERPRETACIÓN ESPECÍFICA:\n"
                        f"• Total de registros analizados: {total}\n"
                        f"• CATEGORÍA MÁS FRECUENTE: '{categoria_mas_frecuente}' con {frecuencia_max} ocurrencias ({porcentaje_max}% del total)\n"
                        f"• CATEGORÍA MENOS FRECUENTE: '{categoria_menos_frecuente}' con {frecuencia_min} ocurrencias ({porcentaje_min}% del total)\n"
                        f"• Diferencia: {frecuencia_max - frecuencia_min} registros ({porcentaje_max - porcentaje_min:.1f} puntos porcentuales)\n"
                        f"• CONCLUSIÓN: La categoría '{categoria_mas_frecuente}' es {frecuencia_max/frecuencia_min:.1f}x más común que '{categoria_menos_frecuente}'"
                    )
                    plt.figtext(0.5, 0.02, interpretacion, ha='center', fontsize=8,
                               bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.8),
                               wrap=True)
                    
                    plt.tight_layout()
                    plt.subplots_adjust(bottom=0.30)
                    
                    # Guardar grafico individual
                    archivo = f"resultados/histogramas/categoricas_{var}.png"
                    plt.savefig(archivo, dpi=300, bbox_inches='tight')
                    print(f"   Grafico {var} guardado: {archivo}")
                    plt.close()
    
    def crear_analisis_outliers(self):
        """Crear analisis de outliers."""
        print("\nCREANDO ANALISIS DE OUTLIERS")
        print("-" * 35)
        
        if self.dataset_final is not None:
            # Variables numericas para analisis de outliers
            variables_numericas = self.dataset_final.select_dtypes(include=[np.number]).columns
            variables_principales = [v for v in ['cantidad', 'precio_unitario_detalle', 'importe'] 
                                   if v in variables_numericas]
            
            if variables_principales:
                fig, axes = plt.subplots(1, len(variables_principales), figsize=(5*len(variables_principales), 6))
                if len(variables_principales) == 1:
                    axes = [axes]
                
                # Calcular estadísticas de outliers para interpretación
                stats_outliers = {}
                
                for i, var in enumerate(variables_principales):
                    datos_var = self.dataset_final[var].dropna()
                    # Boxplot con outliers destacados
                    box_plot = axes[i].boxplot(datos_var, patch_artist=True,
                                              boxprops=dict(facecolor='lightblue', alpha=0.7),
                                              flierprops=dict(marker='o', markerfacecolor='red', 
                                                            markersize=8, alpha=0.7))
                    axes[i].set_title(f'Outliers en {var}', fontweight='bold')
                    axes[i].set_ylabel(var)
                    
                    # Calcular estadisticas de outliers
                    Q1 = datos_var.quantile(0.25)
                    Q3 = datos_var.quantile(0.75)
                    IQR = Q3 - Q1
                    limite_inferior = Q1 - 1.5 * IQR
                    limite_superior = Q3 + 1.5 * IQR
                    mediana = datos_var.median()
                    
                    outliers = datos_var[(datos_var < limite_inferior) | (datos_var > limite_superior)]
                    total = len(datos_var)
                    porcentaje_outliers = (len(outliers) / total * 100) if total > 0 else 0
                    
                    # Guardar para interpretación
                    stats_outliers[var] = {
                        'total': total,
                        'outliers': len(outliers),
                        'porcentaje': porcentaje_outliers,
                        'q1': Q1,
                        'mediana': mediana,
                        'q3': Q3,
                        'limite_inf': limite_inferior,
                        'limite_sup': limite_superior
                    }
                    
                    axes[i].text(0.02, 0.98, f'Outliers: {len(outliers)} ({porcentaje_outliers:.1f}%)', 
                               transform=axes[i].transAxes, verticalalignment='top',
                               bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
                
                plt.suptitle('ANALISIS DE OUTLIERS - DATASET FINAL', 
                           fontsize=14, fontweight='bold', y=0.98)
                
                # Crear interpretación específica
                interpretacion_lineas = ["INTERPRETACIÓN ESPECÍFICA:"]
                for var, estadisticas in stats_outliers.items():
                    interpretacion_lineas.append(f"\n{var.upper()}:")
                    interpretacion_lineas.append(f"  Total de registros: {estadisticas['total']}")
                    interpretacion_lineas.append(f"  OUTLIERS detectados: {estadisticas['outliers']} ({estadisticas['porcentaje']:.1f}% del total)")
                    interpretacion_lineas.append(f"  Rango normal (Q1-Q3): [{estadisticas['q1']:.2f}, {estadisticas['q3']:.2f}], Mediana: {estadisticas['mediana']:.2f}")
                    interpretacion_lineas.append(f"  Límites: [{estadisticas['limite_inf']:.2f}, {estadisticas['limite_sup']:.2f}]")
                    if estadisticas['porcentaje'] > 5:
                        interpretacion_lineas.append(f"  CONCLUSIÓN: {estadisticas['porcentaje']:.1f}% de outliers - Revisar si son errores o casos especiales")
                    else:
                        interpretacion_lineas.append(f"  CONCLUSIÓN: {estadisticas['porcentaje']:.1f}% de outliers - Proporción normal")
                
                interpretacion = "\n".join(interpretacion_lineas)
                fig.text(0.5, 0.01, interpretacion, ha='center', fontsize=7,
                        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8),
                        wrap=True)
                
                plt.tight_layout()
                plt.subplots_adjust(bottom=0.18)
                
                # Guardar grafico
                archivo = "resultados/histogramas/analisis_outliers.png"
                plt.savefig(archivo, dpi=300, bbox_inches='tight')
                print(f"   Analisis de outliers guardado: {archivo}")
                plt.close()
    
    def crear_resumen_estadistico(self):
        """Crear resumen estadistico visual."""
        print("\nCREANDO RESUMEN ESTADISTICO")
        print("-" * 35)
        
        if self.dataset_final is not None:
            # Estadisticas descriptivas
            variables_numericas = self.dataset_final.select_dtypes(include=[np.number]).columns
            stats = self.dataset_final[variables_numericas].describe()
            
            # Crear grafico de estadisticas
            fig, ax = plt.subplots(figsize=(12, 8))
            
            # Crear tabla de estadisticas
            ax.axis('tight')
            ax.axis('off')
            
            # Preparar datos para la tabla
            stats_rounded = stats.round(3)
            
            # Crear tabla
            table = ax.table(cellText=stats_rounded.values,
                           rowLabels=stats_rounded.index,
                           colLabels=stats_rounded.columns,
                           cellLoc='center',
                           loc='center')
            
            table.auto_set_font_size(False)
            table.set_fontsize(9)
            table.scale(1.2, 1.5)
            
            # Colorear encabezados
            for i in range(len(stats_rounded.columns)):
                table[(0, i)].set_facecolor('#4CAF50')
                table[(0, i)].set_text_props(weight='bold', color='white')
            
            plt.title('ESTADISTICAS DESCRIPTIVAS - DATASET FINAL', 
                     fontsize=16, fontweight='bold', pad=20)
            
            # Crear interpretación específica con valores destacados
            interpretacion_lineas = ["INTERPRETACIÓN ESPECÍFICA:"]
            interpretacion_lineas.append(f"• Total de variables numéricas analizadas: {len(variables_numericas)}")
            
            # Encontrar variable con mayor y menor media
            if len(variables_numericas) > 0:
                medias = stats.loc['mean']
                variable_mayor_media = medias.idxmax()
                variable_menor_media = medias.idxmin()
                
                interpretacion_lineas.append(f"\nVALORES DESTACADOS:")
                interpretacion_lineas.append(f"  • Variable con MAYOR promedio: {variable_mayor_media} = {medias[variable_mayor_media]:.2f}")
                interpretacion_lineas.append(f"  • Variable con MENOR promedio: {variable_menor_media} = {medias[variable_menor_media]:.2f}")
                
                # Variable con mayor variabilidad
                desv_std = stats.loc['std']
                variable_mayor_var = desv_std.idxmax()
                interpretacion_lineas.append(f"  • Variable con MAYOR variabilidad: {variable_mayor_var} (std = {desv_std[variable_mayor_var]:.2f})")
                
                interpretacion_lineas.append(f"\nSIGNIFICADO DE LAS ESTADÍSTICAS:")
                interpretacion_lineas.append(f"  • count: Cantidad de datos válidos (sin valores faltantes)")
                interpretacion_lineas.append(f"  • mean: Promedio de todos los valores")
                interpretacion_lineas.append(f"  • std: Desviación estándar (dispersión de los datos)")
                interpretacion_lineas.append(f"  • min/max: Valores mínimo y máximo observados")
                interpretacion_lineas.append(f"  • 25%/50%/75%: Cuartiles (dividen los datos en 4 partes iguales)")
            
            interpretacion = "\n".join(interpretacion_lineas)
            fig.text(0.5, 0.01, interpretacion, ha='center', fontsize=7,
                    bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8),
                    wrap=True)
            
            plt.tight_layout()
            plt.subplots_adjust(bottom=0.15)
            
            # Guardar grafico
            archivo = "resultados/histogramas/resumen_estadistico.png"
            plt.savefig(archivo, dpi=300, bbox_inches='tight')
            print(f"   Resumen estadistico guardado: {archivo}")
            plt.close()
    
    def crear_pairplots_scatter(self):
        """Crear pairplots y scatter plots para analizar relaciones entre variables continuas normalizadas."""
        print("\nCREANDO PAIRPLOTS Y SCATTER PLOTS - VARIABLES CONTINUAS NORMALIZADAS")
        print("-" * 65)
        
        if self.dataset_final is not None:
            # Obtener todas las variables numericas continuas (excluir IDs y variables binarias categoricas)
            todas_numericas = self.dataset_final.select_dtypes(include=[np.number]).columns.tolist()
            
            # Variables a excluir: IDs, variables binarias categoricas (one-hot encoding)
            excluir = ['id_venta', 'id_producto', 'id_cliente', 
                      'categoria_Alimentos', 'categoria_Limpieza',
                      'medio_pago_tarjeta', 'medio_pago_qr', 'medio_pago_transferencia', 'medio_pago_efectivo',
                      'ciudad_0', 'ciudad_1', 'ciudad_2']
            
            # Variables continuas normalizadas (las que tienen valores decimales y no son binarias)
            variables_continuas = []
            for var in todas_numericas:
                if var not in excluir:
                    # Verificar que tenga valores decimales (no solo 0/1) para confirmar que es continua normalizada
                    valores_unicos = self.dataset_final[var].dropna().unique()
                    if len(valores_unicos) > 2 or (len(valores_unicos) == 2 and not all(v in [0, 1] for v in valores_unicos)):
                        variables_continuas.append(var)
            
            # Si no encontramos suficientes, usar las principales
            if len(variables_continuas) < 2:
                variables_principales = ['cantidad', 'precio_unitario_detalle', 'importe', 'precio_unitario_producto']
                variables_continuas = [v for v in variables_principales 
                                      if v in self.dataset_final.select_dtypes(include=[np.number]).columns]
            
            variables_disponibles = variables_continuas
            print(f"   Variables continuas normalizadas identificadas: {len(variables_disponibles)}")
            print(f"   Variables: {', '.join(variables_disponibles)}")
            
            if len(variables_disponibles) >= 2:
                # Crear scatter plots entre pares de variables
                n_vars = len(variables_disponibles)
                fig, axes = plt.subplots(n_vars, n_vars, figsize=(5*n_vars, 5*n_vars))
                
                # Si solo hay una variable, convertir axes a array
                if n_vars == 1:
                    axes = np.array([[axes]])
                
                for i, var1 in enumerate(variables_disponibles):
                    for j, var2 in enumerate(variables_disponibles):
                        if i == j:
                            # Diagonal: Histograma de la variable
                            axes[i, j].hist(self.dataset_final[var1].dropna(), bins=30, 
                                          alpha=0.7, color='skyblue', edgecolor='black')
                            axes[i, j].set_title(f'Distribución de {var1}', fontweight='bold')
                            axes[i, j].set_xlabel(var1)
                            axes[i, j].set_ylabel('Frecuencia')
                        else:
                            # Scatter plot entre variables
                            axes[i, j].scatter(self.dataset_final[var2].dropna(), 
                                             self.dataset_final[var1].dropna(),
                                             alpha=0.5, s=20, color='steelblue')
                            axes[i, j].set_xlabel(var2)
                            axes[i, j].set_ylabel(var1)
                            axes[i, j].grid(True, alpha=0.3)
                            
                            # Calcular correlacion
                            corr = self.dataset_final[[var1, var2]].corr().iloc[0, 1]
                            axes[i, j].set_title(f'r = {corr:.3f}', fontweight='bold', 
                                               color='red' if abs(corr) > 0.7 else 'black')
                
                plt.suptitle('PAIRPLOT - VARIABLES CONTINUAS NORMALIZADAS', 
                           fontsize=16, fontweight='bold', y=0.995)
                
                # Calcular correlaciones para interpretación
                correlaciones_identificadas = []
                for i, var1 in enumerate(variables_disponibles):
                    for j, var2 in enumerate(variables_disponibles):
                        if i < j:  # Solo pares únicos
                            corr = self.dataset_final[[var1, var2]].corr().iloc[0, 1]
                            if abs(corr) > 0.5:  # Correlaciones moderadas o fuertes
                                correlaciones_identificadas.append((var1, var2, corr))
                
                # Ordenar por valor absoluto
                correlaciones_identificadas.sort(key=lambda x: abs(x[2]), reverse=True)
                
                # Crear interpretación específica
                interpretacion_lineas = ["INTERPRETACIÓN ESPECÍFICA:"]
                interpretacion_lineas.append(f"• Total de variables analizadas: {len(variables_disponibles)}")
                interpretacion_lineas.append(f"• Variables: {', '.join(variables_disponibles)}")
                
                if correlaciones_identificadas:
                    interpretacion_lineas.append(f"\nRELACIONES IDENTIFICADAS (|r| > 0.5):")
                    for var1, var2, corr in correlaciones_identificadas[:5]:  # Top 5
                        tipo = "FUERTE POSITIVA" if corr > 0.7 else "MODERADA POSITIVA" if corr > 0.5 else "MODERADA NEGATIVA" if corr < -0.5 else "FUERTE NEGATIVA"
                        interpretacion_lineas.append(f"  • {var1} ↔ {var2}: r = {corr:.3f} ({tipo})")
                    
                    mejor_corr = correlaciones_identificadas[0]
                    interpretacion_lineas.append(f"\nCONCLUSIÓN:")
                    interpretacion_lineas.append(f"  • La relación más fuerte es {mejor_corr[0]} ↔ {mejor_corr[1]} (r={mejor_corr[2]:.3f})")
                    interpretacion_lineas.append(f"  • Se encontraron {len(correlaciones_identificadas)} pares con correlación moderada o fuerte")
                else:
                    interpretacion_lineas.append(f"\nCONCLUSIÓN: No se encontraron correlaciones fuertes (|r| > 0.5)")
                    interpretacion_lineas.append(f"  Las variables son relativamente independientes")
                
                interpretacion = "\n".join(interpretacion_lineas)
                fig.text(0.5, 0.01, interpretacion, ha='center', fontsize=7,
                        bbox=dict(boxstyle='round', facecolor='lightcyan', alpha=0.8),
                        wrap=True)
                
                plt.tight_layout()
                plt.subplots_adjust(bottom=0.15)
                
                # Guardar grafico
                archivo = "resultados/histogramas/pairplot_variables.png"
                plt.savefig(archivo, dpi=300, bbox_inches='tight')
                print(f"   Pairplot guardado: {archivo}")
                plt.close()
                
                # Crear scatter plots individuales con más detalle
                if len(variables_disponibles) >= 2:
                    fig, axes = plt.subplots(1, len(variables_disponibles)-1, 
                                           figsize=(6*(len(variables_disponibles)-1), 6))
                    if len(variables_disponibles) == 2:
                        axes = [axes]
                    
                    for idx in range(len(variables_disponibles)-1):
                        var1 = variables_disponibles[idx]
                        var2 = variables_disponibles[idx+1]
                        
                        scatter = axes[idx].scatter(self.dataset_final[var2].dropna(), 
                                                   self.dataset_final[var1].dropna(),
                                                   alpha=0.6, s=30, 
                                                   c=self.dataset_final[var1].dropna(),
                                                   cmap='viridis')
                        axes[idx].set_xlabel(var2, fontsize=12)
                        axes[idx].set_ylabel(var1, fontsize=12)
                        axes[idx].grid(True, alpha=0.3)
                        
                        # Calcular correlacion y linea de tendencia
                        corr = self.dataset_final[[var1, var2]].corr().iloc[0, 1]
                        axes[idx].set_title(f'{var1} vs {var2}\nCorrelación: {corr:.3f}', 
                                          fontweight='bold', fontsize=12)
                        
                        # Agregar colorbar
                        plt.colorbar(scatter, ax=axes[idx], label=var1)
                    
                    plt.suptitle('SCATTER PLOTS - VARIABLES CONTINUAS NORMALIZADAS', 
                               fontsize=14, fontweight='bold')
                    
                    # Calcular correlaciones específicas para interpretación
                    correlaciones_scatter = []
                    for idx in range(len(variables_disponibles)-1):
                        var1 = variables_disponibles[idx]
                        var2 = variables_disponibles[idx+1]
                        corr = self.dataset_final[[var1, var2]].corr().iloc[0, 1]
                        correlaciones_scatter.append((var1, var2, corr))
                    
                    # Crear interpretación específica
                    interpretacion_lineas = ["INTERPRETACIÓN ESPECÍFICA:"]
                    interpretacion_lineas.append(f"• Total de relaciones analizadas: {len(correlaciones_scatter)}")
                    
                    for var1, var2, corr in correlaciones_scatter:
                        tipo_relacion = ""
                        if abs(corr) > 0.7:
                            tipo_relacion = "FUERTE" + (" POSITIVA" if corr > 0 else " NEGATIVA")
                        elif abs(corr) > 0.5:
                            tipo_relacion = "MODERADA" + (" POSITIVA" if corr > 0 else " NEGATIVA")
                        else:
                            tipo_relacion = "DÉBIL"
                        
                        interpretacion_lineas.append(f"  • {var1} vs {var2}: r = {corr:.3f} ({tipo_relacion})")
                        if abs(corr) > 0.7:
                            interpretacion_lineas.append(f"    → Cuando {var1} aumenta, {var2} {'también aumenta' if corr > 0 else 'disminuye'} significativamente")
                    
                    mejor_relacion = max(correlaciones_scatter, key=lambda x: abs(x[2]))
                    interpretacion_lineas.append(f"\nCONCLUSIÓN:")
                    interpretacion_lineas.append(f"  • La relación más fuerte es {mejor_relacion[0]} ↔ {mejor_relacion[1]} (r={mejor_relacion[2]:.3f})")
                    if abs(mejor_relacion[2]) > 0.8:
                        interpretacion_lineas.append(f"  • Esta relación es MUY FUERTE - cambios en una variable afectan mucho a la otra")
                    
                    interpretacion = "\n".join(interpretacion_lineas)
                    fig.text(0.5, 0.01, interpretacion, ha='center', fontsize=7,
                            bbox=dict(boxstyle='round', facecolor='lavender', alpha=0.8),
                            wrap=True)
                    
                    plt.tight_layout()
                    plt.subplots_adjust(bottom=0.25)
                    
                    # Guardar grafico
                    archivo = "resultados/histogramas/scatter_plots.png"
                    plt.savefig(archivo, dpi=300, bbox_inches='tight')
                    print(f"   Scatter plots guardado: {archivo}")
                    plt.close()
    
    def crear_histograma_curtosis(self):
        """Crear histograma comparativo de curtosis para todas las variables numéricas."""
        print("\nCREANDO HISTOGRAMA DE CURTOSIS")
        print("-" * 50)
        
        if self.dataset_final is None:
            print("   ⚠️ Dataset final no cargado. Cargando datos...")
            if not self.cargar_datos():
                return
        
        # Obtener todas las variables numéricas
        variables_numericas = self.dataset_final.select_dtypes(include=[np.number]).columns.tolist()
        
        if not variables_numericas:
            print("   ⚠️ No hay variables numéricas para analizar")
            return
        
        # Calcular curtosis para cada variable
        kurtosis_data = []
        for var in variables_numericas:
            datos = self.dataset_final[var].dropna()
            if len(datos) > 0:
                kurtosis_val = stats.kurtosis(datos)
                kurtosis_data.append({
                    'variable': var,
                    'curtosis': kurtosis_val
                })
        
        if not kurtosis_data:
            print("   ⚠️ No se pudo calcular curtosis para ninguna variable")
            return
        
        df_kurtosis = pd.DataFrame(kurtosis_data).sort_values('curtosis', ascending=False)
        
        # Crear figura con 3 subplots: barras, scatter plot alternativo, y histograma
        fig = plt.figure(figsize=(20, 8))
        gs = fig.add_gridspec(2, 2, hspace=0.3, wspace=0.3)
        ax1 = fig.add_subplot(gs[0, 0])  # Barras horizontales (superior izquierda)
        ax2 = fig.add_subplot(gs[0, 1])  # Scatter plot alternativo (superior derecha)
        ax3 = fig.add_subplot(gs[1, :])  # Histograma (inferior, ancho completo)
        
        # Gráfico 1: Barras horizontales de curtosis (representación estándar)
        colores = []
        interpretaciones_curtosis = []
        
        for idx, row in df_kurtosis.iterrows():
            kurt = row['curtosis']
            var = row['variable']
            
            # Determinar color según tipo de curtosis
            if kurt < -0.5:
                color = 'lightblue'  # Platicúrtica (colas ligeras)
                tipo = "PLATICÚRTICA"
                interpretacion = "Colas más ligeras que la normal. Menos valores extremos, distribución más aplanada."
            elif kurt > 0.5:
                color = 'salmon'  # Leptocúrtica (colas pesadas)
                tipo = "LEPTOCÚRTICA"
                interpretacion = "Colas más pesadas que la normal. Más valores extremos (outliers), distribución más puntiaguda."
            else:
                color = 'lightgreen'  # Mesocúrtica (normal)
                tipo = "MESOCÚRTICA"
                interpretacion = "Similar a distribución normal. Colas y pico normales."
            
            colores.append(color)
            interpretaciones_curtosis.append({
                'variable': var,
                'curtosis': kurt,
                'tipo': tipo,
                'interpretacion': interpretacion
            })
        
        # Crear gráfico de barras horizontales
        bars = ax1.barh(range(len(df_kurtosis)), df_kurtosis['curtosis'], color=colores, edgecolor='black', alpha=0.7)
        ax1.set_yticks(range(len(df_kurtosis)))
        ax1.set_yticklabels(df_kurtosis['variable'], fontsize=8)
        ax1.set_xlabel('Curtosis (Kurtosis)', fontsize=10, fontweight='bold')
        ax1.set_title('CURTOSIS POR VARIABLE\n(Barras - Comparación de "pesadez" de colas)', 
                     fontsize=11, fontweight='bold', pad=10)
        ax1.axvline(x=0, color='black', linestyle='--', linewidth=1.5, alpha=0.6, label='Normal (0)')
        ax1.axvline(x=-0.5, color='blue', linestyle=':', linewidth=1, alpha=0.5, label='Umbral Platicúrtica')
        ax1.axvline(x=0.5, color='red', linestyle=':', linewidth=1, alpha=0.5, label='Umbral Leptocúrtica')
        ax1.grid(axis='x', alpha=0.3)
        ax1.legend(loc='lower right', fontsize=7)
        
        # Agregar valores en las barras
        for i, (idx, row) in enumerate(df_kurtosis.iterrows()):
            offset = 0.05 if row['curtosis'] >= 0 else -0.1
            ax1.text(row['curtosis'] + offset, i, f'{row["curtosis"]:.2f}', 
                    va='center', fontweight='bold', fontsize=7)
        
        # Gráfico 2: Scatter plot alternativo con líneas de referencia (representación alternativa)
        # Ordenar por índice para mejor visualización
        indices = range(len(df_kurtosis))
        scatter_colors = colores
        
        scatter = ax2.scatter(df_kurtosis['curtosis'], indices, c=scatter_colors, 
                             s=100, alpha=0.7, edgecolors='black', linewidths=1.5)
        ax2.set_xlabel('Curtosis (Kurtosis)', fontsize=10, fontweight='bold')
        ax2.set_ylabel('Índice de Variable', fontsize=10, fontweight='bold')
        ax2.set_title('CURTOSIS POR VARIABLE\n(Scatter Plot - Vista Alternativa)', 
                     fontsize=11, fontweight='bold', pad=10)
        ax2.axvline(x=0, color='black', linestyle='--', linewidth=1.5, alpha=0.6, label='Normal (0)')
        ax2.axvline(x=-0.5, color='blue', linestyle=':', linewidth=1, alpha=0.5)
        ax2.axvline(x=0.5, color='red', linestyle=':', linewidth=1, alpha=0.5)
        ax2.grid(alpha=0.3)
        ax2.legend(fontsize=7)
        
        # Agregar etiquetas para las variables más importantes
        for i, (idx, row) in enumerate(df_kurtosis.iterrows()):
            if abs(row['curtosis']) > 1.0 or abs(row['curtosis']) < 0.1:  # Variables extremas o cercanas a normal
                ax2.annotate(row['variable'][:15], 
                           (row['curtosis'], i),
                           xytext=(5, 0), textcoords='offset points',
                           fontsize=6, alpha=0.7)
        
        # Gráfico 3: Histograma de distribución de valores de curtosis (inferior, ancho completo)
        n, bins, patches = ax3.hist(df_kurtosis['curtosis'], bins=15, color='steelblue', 
                                    edgecolor='black', alpha=0.7)
        # Colorear las barras según el tipo de curtosis
        for i, (patch, bin_left) in enumerate(zip(patches, bins[:-1])):
            if bin_left < -0.5:
                patch.set_facecolor('lightblue')  # Platicúrtica
            elif bin_left > 0.5:
                patch.set_facecolor('salmon')  # Leptocúrtica
            else:
                patch.set_facecolor('lightgreen')  # Mesocúrtica
        
        ax3.axvline(x=0, color='red', linestyle='--', linewidth=2, label='Normal (0)', alpha=0.7)
        ax3.axvline(x=df_kurtosis['curtosis'].mean(), color='green', linestyle='--', 
                   linewidth=2, label=f'Media: {df_kurtosis["curtosis"].mean():.2f}', alpha=0.7)
        ax3.axvline(x=-0.5, color='blue', linestyle=':', linewidth=1.5, alpha=0.5, label='Umbral Platicúrtica')
        ax3.axvline(x=0.5, color='orange', linestyle=':', linewidth=1.5, alpha=0.5, label='Umbral Leptocúrtica')
        ax3.set_xlabel('Curtosis (Kurtosis)', fontsize=11, fontweight='bold')
        ax3.set_ylabel('Frecuencia (Número de Variables)', fontsize=11, fontweight='bold')
        ax3.set_title('DISTRIBUCIÓN DE VALORES DE CURTOSIS\n(¿Cuántas variables tienen cada tipo?)', 
                     fontsize=12, fontweight='bold', pad=15)
        ax3.grid(axis='y', alpha=0.3)
        ax3.legend(fontsize=9)
        
        plt.suptitle('ANÁLISIS DE CURTOSIS - TODAS LAS VARIABLES NUMÉRICAS', 
                    fontsize=14, fontweight='bold', y=0.98)
        
        # Crear interpretación detallada
        interpretacion_lineas = ["INTERPRETACIÓN ESPECÍFICA:"]
        interpretacion_lineas.append(f"• Total de variables analizadas: {len(df_kurtosis)}")
        interpretacion_lineas.append(f"• Curtosis promedio: {df_kurtosis['curtosis'].mean():.2f}")
        interpretacion_lineas.append(f"• Rango de curtosis: [{df_kurtosis['curtosis'].min():.2f}, {df_kurtosis['curtosis'].max():.2f}]")
        
        # Contar por tipo
        platicurticas = [x for x in interpretaciones_curtosis if x['tipo'] == 'PLATICÚRTICA']
        mesocurticas = [x for x in interpretaciones_curtosis if x['tipo'] == 'MESOCÚRTICA']
        leptocurticas = [x for x in interpretaciones_curtosis if x['tipo'] == 'LEPTOCÚRTICA']
        
        interpretacion_lineas.append(f"\nTIPOS DE DISTRIBUCIÓN:")
        interpretacion_lineas.append(f"  • MESOCÚRTICAS (normal, curtosis ≈ 0): {len(mesocurticas)} variables")
        interpretacion_lineas.append(f"    → Distribución normal, colas y pico normales")
        interpretacion_lineas.append(f"  • LEPTOCÚRTICAS (colas pesadas, curtosis > 0.5): {len(leptocurticas)} variables")
        interpretacion_lineas.append(f"    → Más valores extremos (outliers) de lo esperado, distribución más puntiaguda")
        interpretacion_lineas.append(f"  • PLATICÚRTICAS (colas ligeras, curtosis < -0.5): {len(platicurticas)} variables")
        interpretacion_lineas.append(f"    → Menos valores extremos, distribución más aplanada")
        
        # Top 3 variables con mayor y menor curtosis
        top3_alta = df_kurtosis.head(3)
        top3_baja = df_kurtosis.tail(3)
        
        interpretacion_lineas.append(f"\nVARIABLES CON MAYOR CURTOSIS (más outliers esperados):")
        for idx, row in top3_alta.iterrows():
            interpretacion_lineas.append(f"  {idx+1}. {row['variable']}: {row['curtosis']:.2f} (LEPTOCÚRTICA)")
        
        interpretacion_lineas.append(f"\nVARIABLES CON MENOR CURTOSIS (menos outliers):")
        for idx, row in top3_baja.iterrows():
            interpretacion_lineas.append(f"  {idx+1}. {row['variable']}: {row['curtosis']:.2f} ({'PLATICÚRTICA' if row['curtosis'] < -0.5 else 'MESOCÚRTICA'})")
        
        interpretacion_lineas.append(f"\n¿QUÉ SIGNIFICA ESTO PARA EL NEGOCIO?")
        if len(leptocurticas) > len(mesocurticas) + len(platicurticas):
            interpretacion_lineas.append(f"  ⚠️ Muchas variables tienen colas pesadas (outliers frecuentes)")
            interpretacion_lineas.append(f"  → Revisar estrategias de manejo de valores extremos")
            interpretacion_lineas.append(f"  → Considerar transformaciones para reducir impacto de outliers")
        elif len(mesocurticas) > len(leptocurticas) + len(platicurticas):
            interpretacion_lineas.append(f"  ✅ La mayoría de variables tienen distribución normal")
            interpretacion_lineas.append(f"  → Datos bien comportados, adecuados para análisis estadísticos")
        else:
            interpretacion_lineas.append(f"  ℹ️ Mezcla de tipos de distribución")
            interpretacion_lineas.append(f"  → Algunas variables requieren tratamiento especial para outliers")
        
        interpretacion = "\n".join(interpretacion_lineas)
        fig.text(0.5, 0.01, interpretacion, ha='center', fontsize=7,
                bbox=dict(boxstyle='round', facecolor='lavender', alpha=0.9),
                wrap=True)
        
        plt.tight_layout()
        plt.subplots_adjust(bottom=0.20)
        
        # Guardar gráfico
        archivo = "resultados/histogramas/analisis_curtosis.png"
        plt.savefig(archivo, dpi=300, bbox_inches='tight')
        print(f"   Histograma de curtosis guardado: {archivo}")
        plt.close()
    
    def ejecutar_visualizaciones_completas(self):
        """Ejecutar todas las visualizaciones."""
        print("VISUALIZACIONES AVANZADAS - PROYECTO AURELION")
        print("Grupo 11 - Camada 1 | Enith Gicela Vargas Vargas")
        print("=" * 80)
        
        # Cargar datos
        if not self.cargar_datos():
            return False
        
        # Crear todas las visualizaciones
        self.crear_comparacion_normalizacion()
        self.crear_matrices_correlacion()
        self.crear_analisis_distribuciones()
        self.crear_analisis_categoricas()
        self.crear_analisis_outliers()
        self.crear_resumen_estadistico()
        self.crear_pairplots_scatter()
        self.crear_histograma_curtosis()
        
        print(f"\n[OK] Visualizaciones avanzadas completadas!")
        print(f"[INFO] Graficos guardados en: resultados/histogramas/")
        
        # Generar automáticamente ANALISIS_GRAFICOS.md
        print(f"\n📝 Generando ANALISIS_GRAFICOS.md automáticamente...")
        try:
            import sys
            import os
            ruta_script = os.path.join(os.path.dirname(__file__), '10_generar_analisis_graficos.py')
            if os.path.exists(ruta_script):
                import subprocess
                subprocess.run([sys.executable, ruta_script], check=False)
            else:
                print(f"   ⚠️ Script 10_generar_analisis_graficos.py no encontrado")
        except Exception as e:
            print(f"   ⚠️ No se pudo generar ANALISIS_GRAFICOS.md automáticamente: {e}")
            print(f"   💡 Puedes ejecutarlo manualmente: python 10_generar_analisis_graficos.py")
        
        return True

def main():
    """Funcion principal de visualizaciones."""
    visualizador = VisualizacionesAvanzadas()
    visualizador.ejecutar_visualizaciones_completas()

if __name__ == "__main__":
    main()
