#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ESTADÍSTICA INFERENCIAL AVANZADA - PROYECTO AURELION SPRINT_2
==============================================================

**Autor:** Enith Gicela Vargas Vargas  
**Camada:** 1  
**Grupo:** 11  
**Fecha:** 2025-10-27  
**Curso:** AI Fundamentals - Guayerd - IBM Skills Build  
**Sprint:** 2 - Machine Learning y Normalización  
**Módulo:** Estadística Inferencial Avanzada  

Script para realizar análisis estadístico inferencial avanzado, incluyendo:
- Tests de hipótesis (t-test, chi-cuadrado, ANOVA)
- Tests de normalidad (Shapiro-Wilk, Kolmogorov-Smirnov)
- Intervalos de confianza
- Análisis de significancia estadística
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from scipy.stats import ttest_ind, chi2_contingency, f_oneway, shapiro, kstest, normaltest
import warnings
warnings.filterwarnings('ignore')

class EstadisticaInferencial:
    """
    Clase para realizar análisis estadístico inferencial avanzado.
    
    Funcionalidades:
    - Tests de hipótesis (t-test, chi-cuadrado, ANOVA)
    - Tests de normalidad
    - Intervalos de confianza
    - Análisis de significancia estadística
    """
    
    def __init__(self):
        """Inicializar el analizador de estadística inferencial."""
        self.dataset = None
        self.resultados_tests = {}
        
    def cargar_dataset(self):
        """Cargar dataset final normalizado."""
        print("CARGANDO DATASET PARA ANÁLISIS INFERENCIAL")
        print("=" * 50)
        
        try:
            self.dataset = pd.read_csv("resultados/datasets_normalizados/dataset_final_completo.csv")
            print(f"✅ Dataset cargado: {self.dataset.shape[0]} registros × {self.dataset.shape[1]} columnas")
            return True
        except Exception as e:
            print(f"❌ Error al cargar dataset: {e}")
            return False
    
    def test_normalidad(self, variable):
        """
        Realizar tests de normalidad para una variable.
        
        Args:
            variable (str): Nombre de la variable a analizar
        
        Returns:
            dict: Resultados de los tests de normalidad
        """
        if variable not in self.dataset.columns:
            print(f"❌ Variable '{variable}' no encontrada en el dataset")
            return None
        
        datos = self.dataset[variable].dropna()
        
        print(f"\n📊 TESTS DE NORMALIDAD: {variable}")
        print("-" * 50)
        
        resultados = {}
        
        # Test de Shapiro-Wilk (para muestras pequeñas < 5000)
        if len(datos) <= 5000:
            stat_sw, p_sw = shapiro(datos)
            resultados['Shapiro-Wilk'] = {
                'estadistico': stat_sw,
                'p_value': p_sw,
                'normal': p_sw > 0.05
            }
            print(f"   Shapiro-Wilk:")
            print(f"     Estadístico: {stat_sw:.4f}")
            print(f"     p-value: {p_sw:.4f}")
            print(f"     Conclusión: {'Distribución normal' if p_sw > 0.05 else 'Distribución NO normal'} (α=0.05)")
        
        # Test de Kolmogorov-Smirnov
        stat_ks, p_ks = kstest(datos, 'norm', args=(datos.mean(), datos.std()))
        resultados['Kolmogorov-Smirnov'] = {
            'estadistico': stat_ks,
            'p_value': p_ks,
            'normal': p_ks > 0.05
        }
        print(f"\n   Kolmogorov-Smirnov:")
        print(f"     Estadístico: {stat_ks:.4f}")
        print(f"     p-value: {p_ks:.4f}")
        print(f"     Conclusión: {'Distribución normal' if p_ks > 0.05 else 'Distribución NO normal'} (α=0.05)")
        
        # Test de D'Agostino (normalidad)
        stat_da, p_da = normaltest(datos)
        resultados['D\'Agostino'] = {
            'estadistico': stat_da,
            'p_value': p_da,
            'normal': p_da > 0.05
        }
        print(f"\n   D'Agostino:")
        print(f"     Estadístico: {stat_da:.4f}")
        print(f"     p-value: {p_da:.4f}")
        print(f"     Conclusión: {'Distribución normal' if p_da > 0.05 else 'Distribución NO normal'} (α=0.05)")
        
        return resultados
    
    def t_test_medias(self, variable, grupo1, grupo2, columna_grupo):
        """
        Realizar t-test para comparar medias entre dos grupos.
        
        Args:
            variable (str): Variable numérica a comparar
            grupo1: Valor del primer grupo
            grupo2: Valor del segundo grupo
            columna_grupo (str): Columna que define los grupos
        
        Returns:
            dict: Resultados del t-test
        """
        print(f"\n📊 T-TEST: Comparación de medias de '{variable}'")
        print(f"   Grupo 1: {grupo1} vs Grupo 2: {grupo2}")
        print("-" * 50)
        
        datos_grupo1 = self.dataset[self.dataset[columna_grupo] == grupo1][variable].dropna()
        datos_grupo2 = self.dataset[self.dataset[columna_grupo] == grupo2][variable].dropna()
        
        if len(datos_grupo1) == 0 or len(datos_grupo2) == 0:
            print("❌ No hay suficientes datos para realizar el test")
            return None
        
        # Estadísticas descriptivas
        print(f"\n   Estadísticas descriptivas:")
        print(f"     Grupo 1 ({grupo1}): n={len(datos_grupo1)}, media={datos_grupo1.mean():.4f}, std={datos_grupo1.std():.4f}")
        print(f"     Grupo 2 ({grupo2}): n={len(datos_grupo2)}, media={datos_grupo2.mean():.4f}, std={datos_grupo2.std():.4f}")
        
        # T-test independiente
        stat, p_value = ttest_ind(datos_grupo1, datos_grupo2)
        
        # Calcular diferencia de medias e intervalo de confianza
        diferencia = datos_grupo1.mean() - datos_grupo2.mean()
        se = np.sqrt(datos_grupo1.var()/len(datos_grupo1) + datos_grupo2.var()/len(datos_grupo2))
        df = len(datos_grupo1) + len(datos_grupo2) - 2
        t_critico = stats.t.ppf(0.975, df)
        ic_inferior = diferencia - t_critico * se
        ic_superior = diferencia + t_critico * se
        
        resultados = {
            'estadistico': stat,
            'p_value': p_value,
            'diferencia_medias': diferencia,
            'ic_95_inferior': ic_inferior,
            'ic_95_superior': ic_superior,
            'significativo': p_value < 0.05
        }
        
        print(f"\n   Resultados del t-test:")
        print(f"     Estadístico t: {stat:.4f}")
        print(f"     p-value: {p_value:.4f}")
        print(f"     Diferencia de medias: {diferencia:.4f}")
        print(f"     Intervalo de confianza 95%: [{ic_inferior:.4f}, {ic_superior:.4f}]")
        print(f"     Conclusión: {'Hay diferencia significativa' if p_value < 0.05 else 'NO hay diferencia significativa'} (α=0.05)")
        
        return resultados
    
    def test_chi_cuadrado(self, variable1, variable2):
        """
        Realizar test de chi-cuadrado para independencia entre variables categóricas.
        
        Args:
            variable1 (str): Primera variable categórica
            variable2 (str): Segunda variable categórica
        
        Returns:
            dict: Resultados del test chi-cuadrado
        """
        print(f"\n📊 TEST CHI-CUADRADO: Independencia entre '{variable1}' y '{variable2}'")
        print("-" * 50)
        
        # Crear tabla de contingencia
        tabla_contingencia = pd.crosstab(self.dataset[variable1], self.dataset[variable2])
        
        print(f"\n   Tabla de contingencia:")
        print(tabla_contingencia)
        
        # Test chi-cuadrado
        chi2, p_value, dof, expected = chi2_contingency(tabla_contingencia)
        
        resultados = {
            'chi2': chi2,
            'p_value': p_value,
            'grados_libertad': dof,
            'tabla_esperada': expected,
            'independientes': p_value > 0.05
        }
        
        print(f"\n   Resultados del test chi-cuadrado:")
        print(f"     Estadístico χ²: {chi2:.4f}")
        print(f"     Grados de libertad: {dof}")
        print(f"     p-value: {p_value:.4f}")
        print(f"     Conclusión: {'Variables independientes' if p_value > 0.05 else 'Variables NO independientes (hay relación)'} (α=0.05)")
        
        return resultados
    
    def anova(self, variable, columna_grupo):
        """
        Realizar análisis de varianza (ANOVA) para comparar medias entre múltiples grupos.
        
        Args:
            variable (str): Variable numérica a comparar
            columna_grupo (str): Columna que define los grupos
        
        Returns:
            dict: Resultados del ANOVA
        """
        print(f"\n📊 ANOVA: Comparación de medias de '{variable}' entre grupos de '{columna_grupo}'")
        print("-" * 50)
        
        grupos = self.dataset[columna_grupo].unique()
        datos_grupos = [self.dataset[self.dataset[columna_grupo] == grupo][variable].dropna() 
                       for grupo in grupos]
        
        # Estadísticas por grupo
        print(f"\n   Estadísticas por grupo:")
        for grupo, datos in zip(grupos, datos_grupos):
            print(f"     {grupo}: n={len(datos)}, media={datos.mean():.4f}, std={datos.std():.4f}")
        
        # ANOVA
        f_stat, p_value = f_oneway(*datos_grupos)
        
        resultados = {
            'f_statistic': f_stat,
            'p_value': p_value,
            'grupos': grupos.tolist(),
            'hay_diferencias': p_value < 0.05
        }
        
        print(f"\n   Resultados del ANOVA:")
        print(f"     Estadístico F: {f_stat:.4f}")
        print(f"     p-value: {p_value:.4f}")
        print(f"     Conclusión: {'Hay diferencias significativas entre grupos' if p_value < 0.05 else 'NO hay diferencias significativas entre grupos'} (α=0.05)")
        
        return resultados
    
    def intervalo_confianza_media(self, variable, confianza=0.95):
        """
        Calcular intervalo de confianza para la media de una variable.
        
        Args:
            variable (str): Variable numérica
            confianza (float): Nivel de confianza (default: 0.95)
        
        Returns:
            dict: Intervalo de confianza
        """
        datos = self.dataset[variable].dropna()
        n = len(datos)
        media = datos.mean()
        std = datos.std()
        se = std / np.sqrt(n)
        
        # Valor crítico t
        alpha = 1 - confianza
        t_critico = stats.t.ppf(1 - alpha/2, n - 1)
        
        ic_inferior = media - t_critico * se
        ic_superior = media + t_critico * se
        
        resultados = {
            'media': media,
            'desviacion_estandar': std,
            'n': n,
            'ic_inferior': ic_inferior,
            'ic_superior': ic_superior,
            'nivel_confianza': confianza
        }
        
        print(f"\n📊 INTERVALO DE CONFIANZA {confianza*100}%: {variable}")
        print("-" * 50)
        print(f"   Media: {media:.4f}")
        print(f"   Desviación estándar: {std:.4f}")
        print(f"   Tamaño de muestra: {n}")
        print(f"   Intervalo de confianza: [{ic_inferior:.4f}, {ic_superior:.4f}]")
        print(f"   Interpretación: Con {confianza*100}% de confianza, la media poblacional está entre {ic_inferior:.4f} y {ic_superior:.4f}")
        
        return resultados
    
    def crear_visualizaciones_inferenciales(self):
        """Crear visualizaciones de los análisis inferenciales."""
        print(f"\n📊 CREANDO VISUALIZACIONES INFERENCIALES")
        print("-" * 50)
        
        # Crear directorio si no existe
        import os
        os.makedirs("resultados/histogramas", exist_ok=True)
        
        # Visualización de tests de normalidad
        self._visualizar_tests_normalidad()
        
        # Visualización de comparaciones de medias
        self._visualizar_comparaciones_medias()
        
        print("   ✅ Visualizaciones inferenciales guardadas")
    
    def _visualizar_tests_normalidad(self):
        """Visualizar resultados de tests de normalidad."""
        variables_numericas = self.dataset.select_dtypes(include=[np.number]).columns.tolist()
        variables_principales = ['importe', 'cantidad', 'precio_unitario_detalle']
        variables_analizar = [v for v in variables_principales if v in variables_numericas][:5]
        
        if not variables_analizar:
            return
        
        fig = plt.figure(figsize=(5*len(variables_analizar), 11))
        gs = fig.add_gridspec(3, len(variables_analizar), height_ratios=[3, 3, 1], hspace=0.3)
        
        resultados_tests = {}
        
        for idx, var in enumerate(variables_analizar):
            datos = self.dataset[var].dropna()
            
            # Histograma con curva normal
            ax1 = fig.add_subplot(gs[0, idx])
            ax1.hist(datos, bins=30, density=True, alpha=0.7, color='skyblue', edgecolor='black')
            x = np.linspace(datos.min(), datos.max(), 100)
            ax1.plot(x, stats.norm.pdf(x, datos.mean(), datos.std()), 'r-', lw=2, label='Distribución Normal')
            ax1.set_title(f'{var}\nHistograma vs Normal', fontweight='bold')
            ax1.set_xlabel('Valor')
            ax1.set_ylabel('Densidad')
            ax1.legend()
            ax1.grid(alpha=0.3)
            
            # Q-Q plot
            ax2 = fig.add_subplot(gs[1, idx])
            stats.probplot(datos, dist="norm", plot=ax2)
            ax2.set_title(f'{var}\nQ-Q Plot', fontweight='bold')
            ax2.grid(alpha=0.3)
            
            # Realizar tests estadísticos de normalidad
            from scipy.stats import shapiro, normaltest
            try:
                # Shapiro-Wilk (para muestras pequeñas)
                if len(datos) <= 5000:
                    stat_shapiro, p_shapiro = shapiro(datos)
                    resultados_tests[var] = {
                        'shapiro_stat': stat_shapiro,
                        'shapiro_p': p_shapiro,
                        'shapiro_normal': p_shapiro > 0.05,
                        'media': datos.mean(),
                        'std': datos.std(),
                        'n': len(datos)
                    }
                else:
                    # D'Agostino para muestras grandes
                    stat_dagostino, p_dagostino = normaltest(datos)
                    resultados_tests[var] = {
                        'dagostino_stat': stat_dagostino,
                        'dagostino_p': p_dagostino,
                        'dagostino_normal': p_dagostino > 0.05,
                        'media': datos.mean(),
                        'std': datos.std(),
                        'n': len(datos)
                    }
            except:
                resultados_tests[var] = {
                    'media': datos.mean(),
                    'std': datos.std(),
                    'n': len(datos),
                    'error': True
                }
        
        # Agregar interpretación específica
        ax_interpretacion = fig.add_subplot(gs[2, :])
        ax_interpretacion.axis('off')
        
        interpretacion_lineas = ["INTERPRETACIÓN ESPECÍFICA - TESTS DE NORMALIDAD:"]
        interpretacion_lineas.append("=" * 70)
        
        for var, resultados in resultados_tests.items():
            interpretacion_lineas.append(f"\n{var.upper()}:")
            interpretacion_lineas.append(f"  • Media: {resultados['media']:.2f} | Desv. Estándar: {resultados['std']:.2f}")
            interpretacion_lineas.append(f"  • Número de observaciones: {resultados['n']}")
            
            if 'error' not in resultados:
                if 'shapiro_p' in resultados:
                    interpretacion_lineas.append(f"  • Test Shapiro-Wilk: p-value = {resultados['shapiro_p']:.4f}")
                    if resultados['shapiro_normal']:
                        interpretacion_lineas.append(f"    → Distribución NORMAL (p > 0.05)")
                    else:
                        interpretacion_lineas.append(f"    → Distribución NO NORMAL (p ≤ 0.05)")
                elif 'dagostino_p' in resultados:
                    interpretacion_lineas.append(f"  • Test D'Agostino: p-value = {resultados['dagostino_p']:.4f}")
                    if resultados['dagostino_normal']:
                        interpretacion_lineas.append(f"    → Distribución NORMAL (p > 0.05)")
                    else:
                        interpretacion_lineas.append(f"    → Distribución NO NORMAL (p ≤ 0.05)")
            
            # Interpretación visual
            interpretacion_lineas.append(f"  • Interpretación visual:")
            interpretacion_lineas.append(f"    - Histograma: Si coincide con línea roja → Normal")
            interpretacion_lineas.append(f"    - Q-Q Plot: Si puntos siguen línea diagonal → Normal")
        
        interpretacion_lineas.append(f"\n¿QUÉ SIGNIFICA?")
        interpretacion_lineas.append(f"  • Distribución NORMAL: Puedes usar tests paramétricos (t-test, ANOVA)")
        interpretacion_lineas.append(f"  • Distribución NO NORMAL: Usa tests no paramétricos (Mann-Whitney, Kruskal-Wallis)")
        
        interpretacion = "\n".join(interpretacion_lineas)
        ax_interpretacion.text(0.05, 0.95, interpretacion, transform=ax_interpretacion.transAxes,
                              fontsize=7, verticalalignment='top', family='monospace',
                              bbox=dict(boxstyle='round', facecolor='lavender', alpha=0.9))
        
        plt.suptitle('TESTS DE NORMALIDAD - ANÁLISIS VISUAL Y ESTADÍSTICO', fontsize=14, fontweight='bold', y=0.98)
        plt.tight_layout()
        plt.savefig("resultados/histogramas/tests_normalidad.png", dpi=300, bbox_inches='tight')
        plt.close()
        print("   ✅ Gráfico de tests de normalidad guardado")
    
    def _visualizar_comparaciones_medias(self):
        """Visualizar comparaciones de medias entre grupos."""
        # Comparar importes por categoría de producto
        # Las categorías están codificadas como One-Hot: categoria_Alimentos, categoria_Limpieza
        if 'importe' in self.dataset.columns:
            # Crear variable categórica a partir de las columnas One-Hot
            categorias_cols = [col for col in self.dataset.columns if col.startswith('categoria_')]
            
            if len(categorias_cols) > 0:
                # Crear columna categórica temporal
                self.dataset['categoria_temp'] = 'Otra'
                for col in categorias_cols:
                    categoria_nombre = col.replace('categoria_', '')
                    self.dataset.loc[self.dataset[col] == 1, 'categoria_temp'] = categoria_nombre
                
                fig, axes = plt.subplots(1, 2, figsize=(14, 6))
                
                # Boxplot
                categorias = self.dataset['categoria_temp'].unique()
                datos_por_categoria = [self.dataset[self.dataset['categoria_temp'] == cat]['importe'].dropna() 
                                     for cat in categorias if len(self.dataset[self.dataset['categoria_temp'] == cat]) > 0]
                categorias_validas = [cat for cat in categorias if len(self.dataset[self.dataset['categoria_temp'] == cat]) > 0]
                
                if len(datos_por_categoria) > 0:
                    axes[0].boxplot(datos_por_categoria, labels=categorias_validas)
                    axes[0].set_title('Comparación de Importes por Categoría\n(Boxplot)', fontweight='bold')
                    axes[0].set_ylabel('Importe')
                    axes[0].grid(alpha=0.3)
                    
                    # Barras con intervalos de confianza
                    medias = [datos.mean() for datos in datos_por_categoria]
                    stds = [datos.std() / np.sqrt(len(datos)) for datos in datos_por_categoria]
                    
                    x_pos = np.arange(len(categorias_validas))
                    axes[1].bar(x_pos, medias, yerr=stds, capsize=5, alpha=0.7, color='lightcoral', edgecolor='black')
                    axes[1].set_xticks(x_pos)
                    axes[1].set_xticklabels(categorias_validas)
                    axes[1].set_title('Medias con Intervalos de Confianza 95%', fontweight='bold')
                    axes[1].set_ylabel('Importe Promedio')
                    axes[1].grid(alpha=0.3, axis='y')
                    
                    # Agregar valores en las barras
                    for i, (media, std) in enumerate(zip(medias, stds)):
                        axes[1].text(i, media + std + media*0.05, f'{media:.2f}', 
                                    ha='center', va='bottom', fontweight='bold', fontsize=9)
                    
                    # Crear interpretación
                    interpretacion_lineas = ["INTERPRETACIÓN ESPECÍFICA:"]
                    interpretacion_lineas.append(f"\nCOMPARACIÓN DE MEDIAS POR CATEGORÍA:")
                    for i, (cat, media, std) in enumerate(zip(categorias_validas, medias, stds)):
                        n = len(datos_por_categoria[i])
                        ic_inf = media - 1.96 * std
                        ic_sup = media + 1.96 * std
                        interpretacion_lineas.append(f"  • {cat}:")
                        interpretacion_lineas.append(f"    - Media: ${media:.2f}")
                        interpretacion_lineas.append(f"    - Intervalo 95%: [${ic_inf:.2f}, ${ic_sup:.2f}]")
                        interpretacion_lineas.append(f"    - Número de observaciones: {n}")
                    
                    # Identificar categoría con mayor y menor importe promedio
                    categoria_mayor = categorias_validas[np.argmax(medias)]
                    categoria_menor = categorias_validas[np.argmin(medias)]
                    diferencia = max(medias) - min(medias)
                    
                    interpretacion_lineas.append(f"\n¿QUÉ SIGNIFICA?")
                    interpretacion_lineas.append(f"  • Si los intervalos NO se superponen: Hay diferencia significativa entre categorías")
                    interpretacion_lineas.append(f"  • Si los intervalos SÍ se superponen: Puede no haber diferencia significativa")
                    interpretacion_lineas.append(f"\nCONCLUSIÓN:")
                    interpretacion_lineas.append(f"  • Categoría con MAYOR importe promedio: {categoria_mayor} (${max(medias):.2f})")
                    interpretacion_lineas.append(f"  • Categoría con MENOR importe promedio: {categoria_menor} (${min(medias):.2f})")
                    interpretacion_lineas.append(f"  • Diferencia: ${diferencia:.2f}")
                    
                    interpretacion = "\n".join(interpretacion_lineas)
                    fig.text(0.5, 0.01, interpretacion, ha='center', fontsize=7,
                            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8),
                            wrap=True)
                    
                    plt.suptitle('COMPARACIÓN DE MEDIAS - ANÁLISIS INFERENCIAL', fontsize=14, fontweight='bold')
                    plt.tight_layout()
                    plt.subplots_adjust(bottom=0.25)
                    plt.savefig("resultados/histogramas/comparacion_medias.png", dpi=300, bbox_inches='tight')
                    plt.close()
                    print("   ✅ Gráfico de comparación de medias guardado")
                    
                    # Eliminar columna temporal
                    self.dataset.drop('categoria_temp', axis=1, inplace=True, errors='ignore')
                else:
                    print("   ⚠️  No hay suficientes datos para comparar categorías")
            else:
                # Si no hay columnas de categoría, comparar por otra variable disponible
                # Por ejemplo, comparar por medio de pago
                medios_pago_cols = [col for col in self.dataset.columns if col.startswith('medio_pago_')]
                if len(medios_pago_cols) > 0:
                    self.dataset['medio_pago_temp'] = 'Otro'
                    for col in medios_pago_cols:
                        medio_nombre = col.replace('medio_pago_', '').capitalize()
                        self.dataset.loc[self.dataset[col] == 1, 'medio_pago_temp'] = medio_nombre
                    
                    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
                    
                    medios_pago = self.dataset['medio_pago_temp'].unique()
                    datos_por_medio = [self.dataset[self.dataset['medio_pago_temp'] == mp]['importe'].dropna() 
                                     for mp in medios_pago if len(self.dataset[self.dataset['medio_pago_temp'] == mp]) > 0]
                    medios_validos = [mp for mp in medios_pago if len(self.dataset[self.dataset['medio_pago_temp'] == mp]) > 0]
                    
                    if len(datos_por_medio) > 0:
                        fig, axes = plt.subplots(1, 2, figsize=(14, 7))
                        
                        axes[0].boxplot(datos_por_medio, labels=medios_validos)
                        axes[0].set_title('Comparación de Importes por Medio de Pago\n(Boxplot)', fontweight='bold')
                        axes[0].set_ylabel('Importe')
                        axes[0].tick_params(axis='x', rotation=45)
                        axes[0].grid(alpha=0.3)
                        
                        medias = [datos.mean() for datos in datos_por_medio]
                        stds = [datos.std() / np.sqrt(len(datos)) for datos in datos_por_medio]
                        
                        x_pos = np.arange(len(medios_validos))
                        axes[1].bar(x_pos, medias, yerr=stds, capsize=5, alpha=0.7, color='lightcoral', edgecolor='black')
                        axes[1].set_xticks(x_pos)
                        axes[1].set_xticklabels(medios_validos, rotation=45, ha='right')
                        axes[1].set_title('Medias con Intervalos de Confianza 95%', fontweight='bold')
                        axes[1].set_ylabel('Importe Promedio')
                        axes[1].grid(alpha=0.3, axis='y')
                        
                        # Agregar valores en las barras
                        for i, (media, std) in enumerate(zip(medias, stds)):
                            axes[1].text(i, media + std + media*0.05, f'{media:.2f}', 
                                        ha='center', va='bottom', fontweight='bold', fontsize=9)
                        
                        # Crear interpretación
                        interpretacion_lineas = ["INTERPRETACIÓN ESPECÍFICA:"]
                        interpretacion_lineas.append(f"\nCOMPARACIÓN DE MEDIAS POR MEDIO DE PAGO:")
                        for i, (medio, media, std) in enumerate(zip(medios_validos, medias, stds)):
                            n = len(datos_por_medio[i])
                            ic_inf = media - 1.96 * std
                            ic_sup = media + 1.96 * std
                            interpretacion_lineas.append(f"  • {medio}:")
                            interpretacion_lineas.append(f"    - Media: ${media:.2f}")
                            interpretacion_lineas.append(f"    - Intervalo 95%: [${ic_inf:.2f}, ${ic_sup:.2f}]")
                            interpretacion_lineas.append(f"    - Número de transacciones: {n}")
                        
                        interpretacion_lineas.append(f"\n¿QUÉ SIGNIFICA?")
                        interpretacion_lineas.append(f"  • Si los intervalos NO se superponen: Hay diferencia significativa entre medios de pago")
                        interpretacion_lineas.append(f"  • Si los intervalos SÍ se superponen: Puede no haber diferencia significativa")
                        
                        # Identificar medio con mayor y menor importe promedio
                        medio_mayor = medios_validos[np.argmax(medias)]
                        medio_menor = medios_validos[np.argmin(medias)]
                        diferencia = max(medias) - min(medias)
                        interpretacion_lineas.append(f"\nCONCLUSIÓN:")
                        interpretacion_lineas.append(f"  • Medio con MAYOR importe promedio: {medio_mayor} (${max(medias):.2f})")
                        interpretacion_lineas.append(f"  • Medio con MENOR importe promedio: {medio_menor} (${min(medias):.2f})")
                        interpretacion_lineas.append(f"  • Diferencia: ${diferencia:.2f}")
                        
                        interpretacion = "\n".join(interpretacion_lineas)
                        fig.text(0.5, 0.01, interpretacion, ha='center', fontsize=7,
                                bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8),
                                wrap=True)
                        
                        plt.suptitle('COMPARACIÓN DE MEDIAS - ANÁLISIS INFERENCIAL', fontsize=14, fontweight='bold')
                        plt.tight_layout()
                        plt.subplots_adjust(bottom=0.25)
                        plt.savefig("resultados/histogramas/comparacion_medias.png", dpi=300, bbox_inches='tight')
                        plt.close()
                        print("   ✅ Gráfico de comparación de medias guardado")
                        
                        self.dataset.drop('medio_pago_temp', axis=1, inplace=True, errors='ignore')
    
    def ejecutar_analisis_completo(self):
        """Ejecutar análisis inferencial completo."""
        print("=" * 80)
        print("ESTADÍSTICA INFERENCIAL AVANZADA - PROYECTO AURELION")
        print("=" * 80)
        print("Proyecto desarrollado como parte del curso AI Fundamentals - Guayerd - IBM Skills Build")
        print()
        
        if not self.cargar_dataset():
            return False
        
        print("\n" + "=" * 80)
        print("EJECUTANDO ANÁLISIS INFERENCIAL COMPLETO")
        print("=" * 80)
        
        # Tests de normalidad para variables principales
        print("\n1️⃣  TESTS DE NORMALIDAD")
        variables_analizar = ['importe', 'cantidad', 'precio_unitario_detalle']
        for var in variables_analizar:
            if var in self.dataset.columns:
                self.test_normalidad(var)
        
        # Intervalos de confianza
        print("\n2️⃣  INTERVALOS DE CONFIANZA")
        for var in variables_analizar:
            if var in self.dataset.columns:
                self.intervalo_confianza_media(var)
        
        # T-tests si hay grupos categóricos
        print("\n3️⃣  T-TESTS (Comparación de Medias)")
        # Crear variable categórica temporal para t-test
        categorias_cols = [col for col in self.dataset.columns if col.startswith('categoria_')]
        if len(categorias_cols) >= 2 and 'importe' in self.dataset.columns:
            self.dataset['categoria_temp'] = 'Otra'
            for col in categorias_cols:
                categoria_nombre = col.replace('categoria_', '')
                self.dataset.loc[self.dataset[col] == 1, 'categoria_temp'] = categoria_nombre
            
            categorias = self.dataset['categoria_temp'].unique()
            categorias_validas = [cat for cat in categorias if cat != 'Otra' and len(self.dataset[self.dataset['categoria_temp'] == cat]) > 0]
            if len(categorias_validas) >= 2:
                self.t_test_medias('importe', categorias_validas[0], categorias_validas[1], 'categoria_temp')
                self.dataset.drop('categoria_temp', axis=1, inplace=True, errors='ignore')
        
        # ANOVA
        print("\n4️⃣  ANOVA (Análisis de Varianza)")
        # Crear variable categórica temporal para ANOVA
        categorias_cols = [col for col in self.dataset.columns if col.startswith('categoria_')]
        if len(categorias_cols) > 0 and 'importe' in self.dataset.columns:
            self.dataset['categoria_temp'] = 'Otra'
            for col in categorias_cols:
                categoria_nombre = col.replace('categoria_', '')
                self.dataset.loc[self.dataset[col] == 1, 'categoria_temp'] = categoria_nombre
            
            if self.dataset['categoria_temp'].nunique() > 1:
                self.anova('importe', 'categoria_temp')
                self.dataset.drop('categoria_temp', axis=1, inplace=True, errors='ignore')
        
        # Chi-cuadrado
        print("\n5️⃣  TEST CHI-CUADRADO (Independencia)")
        # Crear variables categóricas temporales para chi-cuadrado
        categorias_cols = [col for col in self.dataset.columns if col.startswith('categoria_')]
        medios_pago_cols = [col for col in self.dataset.columns if col.startswith('medio_pago_')]
        
        if len(categorias_cols) > 0 and len(medios_pago_cols) > 0:
            # Crear variable categórica de categoría
            self.dataset['categoria_temp'] = 'Otra'
            for col in categorias_cols:
                categoria_nombre = col.replace('categoria_', '')
                self.dataset.loc[self.dataset[col] == 1, 'categoria_temp'] = categoria_nombre
            
            # Crear variable categórica de medio de pago
            self.dataset['medio_pago_temp'] = 'Otro'
            for col in medios_pago_cols:
                medio_nombre = col.replace('medio_pago_', '').capitalize()
                self.dataset.loc[self.dataset[col] == 1, 'medio_pago_temp'] = medio_nombre
            
            if self.dataset['categoria_temp'].nunique() > 1 and self.dataset['medio_pago_temp'].nunique() > 1:
                self.test_chi_cuadrado('categoria_temp', 'medio_pago_temp')
            
            self.dataset.drop(['categoria_temp', 'medio_pago_temp'], axis=1, inplace=True, errors='ignore')
        
        # Crear visualizaciones
        print("\n6️⃣  VISUALIZACIONES")
        self.crear_visualizaciones_inferenciales()
        
        # Guardar resultados
        self.guardar_resultados()
        
        print("\n" + "=" * 80)
        print("✅ ANÁLISIS INFERENCIAL COMPLETADO EXITOSAMENTE")
        print("=" * 80)
        print("📁 Resultados guardados en: resultados/estadisticas/estadistica_inferencial.txt")
        print("📊 Gráficos guardados en: resultados/histogramas/")
        
        return True
    
    def guardar_resultados(self):
        """Guardar resultados de análisis inferencial."""
        try:
            archivo = "resultados/estadisticas/estadistica_inferencial.txt"
            with open(archivo, 'w', encoding='utf-8') as f:
                f.write("ESTADÍSTICA INFERENCIAL AVANZADA - PROYECTO AURELION\n")
                f.write("=" * 80 + "\n\n")
                f.write("Este análisis incluye:\n")
                f.write("- Tests de normalidad (Shapiro-Wilk, Kolmogorov-Smirnov, D'Agostino)\n")
                f.write("- T-tests para comparación de medias\n")
                f.write("- ANOVA para comparación de múltiples grupos\n")
                f.write("- Test chi-cuadrado para independencia\n")
                f.write("- Intervalos de confianza\n\n")
                f.write("Los resultados detallados se muestran en la consola durante la ejecución.\n")
            
            print(f"   ✅ Resultados guardados: {archivo}")
        except Exception as e:
            print(f"   ⚠️  Error al guardar resultados: {e}")

def main():
    """Función principal."""
    analizador = EstadisticaInferencial()
    analizador.ejecutar_analisis_completo()

if __name__ == "__main__":
    main()

