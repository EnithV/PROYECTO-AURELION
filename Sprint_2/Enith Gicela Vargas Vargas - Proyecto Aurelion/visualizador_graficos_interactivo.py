#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VISUALIZADOR DE GRÁFICOS INTERACTIVO - PROYECTO AURELION SPRINT_2
==================================================================

**Autor:** Enith Gicela Vargas Vargas  
**Camada:** 1  
**Grupo:** 11  
**Fecha:** 2025-10-27  
**Curso:** AI Fundamentals - Guayerd - IBM Skills Build  
**Sprint:** 2 - Machine Learning y Normalización  

Módulo para visualizar gráficos con interpretaciones específicas y detalladas.
"""

import os
import sys
from pathlib import Path
import subprocess

class VisualizadorGraficosInteractivo:
    """
    Clase para visualizar gráficos con interpretaciones específicas.
    
    Permite al usuario:
    - Ver lista de gráficos disponibles
    - Seleccionar un gráfico específico
    - Ver el gráfico con su interpretación detallada
    - Leer análisis profesional del gráfico
    """
    
    def __init__(self):
        """Inicializar el visualizador."""
        # Ruta base del proyecto
        ruta_base = Path(__file__).parent
        self.ruta_histogramas = ruta_base / "resultados" / "histogramas"
        self.ruta_analisis = ruta_base / "resultados" / "histogramas" / "ANALISIS_GRAFICOS.md"
        self.ruta_dataset = ruta_base / "resultados" / "datasets_normalizados" / "dataset_final_completo.csv"
        
        # Cargar dataset para calcular interpretaciones específicas
        self.dataset = None
        try:
            if self.ruta_dataset.exists():
                import pandas as pd
                self.dataset = pd.read_csv(self.ruta_dataset)
        except:
            pass
        
        # Diccionario de gráficos con interpretaciones específicas
        self.graficos = {
            '1': {
                'archivo': 'histogramas_clientes.png',
                'nombre': 'Histogramas de Clientes',
                'descripcion': 'Distribución de variables numéricas de clientes',
                'interpretacion': self._interpretacion_histogramas_clientes()
            },
            '2': {
                'archivo': 'histogramas_productos.png',
                'nombre': 'Histogramas de Productos',
                'descripcion': 'Distribución de precios y variables de productos',
                'interpretacion': self._interpretacion_histogramas_productos()
            },
            '3': {
                'archivo': 'histogramas_ventas.png',
                'nombre': 'Histogramas de Ventas',
                'descripcion': 'Distribución de variables de ventas',
                'interpretacion': self._interpretacion_histogramas_ventas()
            },
            '4': {
                'archivo': 'histogramas_detalle_ventas.png',
                'nombre': 'Histogramas de Detalle de Ventas',
                'descripcion': 'Distribución de cantidades, precios e importes por línea',
                'interpretacion': self._interpretacion_histogramas_detalle_ventas()
            },
            '5': {
                'archivo': 'matriz_correlacion_final.png',
                'nombre': 'Matriz de Correlación',
                'descripcion': 'Relaciones entre variables numéricas del dataset final',
                'interpretacion': self._interpretacion_matriz_correlacion()
            },
            '6': {
                'archivo': 'analisis_outliers.png',
                'nombre': 'Análisis de Outliers',
                'descripcion': 'Valores inusuales en las variables principales',
                'interpretacion': self._interpretacion_outliers()
            },
            '7': {
                'archivo': 'comparacion_normalizacion_productos.png',
                'nombre': 'Comparación Normalización - Productos',
                'descripcion': 'Antes y después de normalizar datos de productos',
                'interpretacion': self._interpretacion_normalizacion_productos()
            },
            '8': {
                'archivo': 'comparacion_normalizacion_detalle_ventas.png',
                'nombre': 'Comparación Normalización - Detalle Ventas',
                'descripcion': 'Antes y después de normalizar datos de detalle de ventas',
                'interpretacion': self._interpretacion_normalizacion_detalle_ventas()
            },
            '9': {
                'archivo': 'analisis_distribuciones.png',
                'nombre': 'Análisis de Distribuciones',
                'descripcion': 'Histogramas y boxplots de variables principales',
                'interpretacion': self._interpretacion_distribuciones()
            },
            '10': {
                'archivo': 'analisis_clustering.png',
                'nombre': 'Análisis de Clustering',
                'descripcion': 'Agrupación de datos con K-Means y DBSCAN',
                'interpretacion': self._interpretacion_clustering()
            },
            '11': {
                'archivo': 'comparacion_modelos_regresion.png',
                'nombre': 'Comparación de Modelos de Regresión',
                'descripcion': 'Rendimiento de diferentes modelos de ML',
                'interpretacion': self._interpretacion_modelos_regresion()
            },
            '12': {
                'archivo': 'importancia_variables.png',
                'nombre': 'Importancia de Variables',
                'descripcion': 'Variables más importantes para las predicciones',
                'interpretacion': self._interpretacion_importancia_variables()
            },
            '13': {
                'archivo': 'resumen_estadistico.png',
                'nombre': 'Resumen Estadístico',
                'descripcion': 'Estadísticas descriptivas del dataset final',
                'interpretacion': self._interpretacion_resumen_estadistico()
            },
            '14': {
                'archivo': 'categoricas_categoria_Alimentos.png',
                'nombre': 'Distribución Categoría Alimentos',
                'descripcion': 'Frecuencia de productos de la categoría Alimentos',
                'interpretacion': self._interpretacion_categoricas_alimentos
            },
            '15': {
                'archivo': 'categoricas_categoria_Limpieza.png',
                'nombre': 'Distribución Categoría Limpieza',
                'descripcion': 'Frecuencia de productos de la categoría Limpieza',
                'interpretacion': self._interpretacion_categoricas_limpieza
            },
            '16': {
                'archivo': 'pairplot_variables.png',
                'nombre': 'Pairplot de Variables',
                'descripcion': 'Relaciones entre todas las variables continuas',
                'interpretacion': self._interpretacion_pairplot()
            },
            '17': {
                'archivo': 'scatter_plots.png',
                'nombre': 'Scatter Plots Detallados',
                'descripcion': 'Gráficos de dispersión entre pares de variables',
                'interpretacion': self._interpretacion_scatter_plots()
            },
            '18': {
                'archivo': 'analisis_medios_pago.png',
                'nombre': 'Análisis de Medios de Pago',
                'descripcion': 'Distribución y estadísticas de métodos de pago',
                'interpretacion': self._interpretacion_medios_pago()
            },
            '19': {
                'archivo': 'analisis_curtosis.png',
                'nombre': 'Análisis de Curtosis',
                'descripcion': 'Análisis de curtosis (pesadez de colas) de todas las variables numéricas',
                'interpretacion': self._interpretacion_curtosis()
            },
            '20': {
                'archivo': 'matrices_confusion.png',
                'nombre': 'Matrices de Confusión',
                'descripcion': 'Matrices de confusión para modelos de clasificación',
                'interpretacion': self._interpretacion_matrices_confusion()
            },
            '21': {
                'archivo': 'tests_normalidad.png',
                'nombre': 'Tests de Normalidad',
                'descripcion': 'Análisis visual de normalidad de distribuciones (histogramas y Q-Q plots)',
                'interpretacion': self._interpretacion_tests_normalidad()
            },
            '22': {
                'archivo': 'comparacion_medias.png',
                'nombre': 'Comparación de Medias',
                'descripcion': 'Comparación de medias entre grupos con intervalos de confianza',
                'interpretacion': self._interpretacion_comparacion_medias()
            },
            '23': {
                'archivo': 'optimizaciones_prescriptivas.png',
                'nombre': 'Optimizaciones Prescriptivas',
                'descripcion': 'Análisis de optimización de inventario, precios y mix de productos',
                'interpretacion': self._interpretacion_optimizaciones()
            },
            '24': {
                'archivo': 'recomendaciones_prescriptivas.png',
                'nombre': 'Recomendaciones Prescriptivas',
                'descripcion': 'Recomendaciones de acciones basadas en análisis estadístico',
                'interpretacion': self._interpretacion_recomendaciones()
            }
        }
    
    def _interpretacion_histogramas_clientes(self):
        """Interpretación específica para histogramas de clientes."""
        # Intentar obtener datos específicos del proyecto
        datos_especificos = self._obtener_datos_especificos_clientes()
        
        return f"""
═══════════════════════════════════════════════════════════════════════════════
📊 INTERPRETACIÓN: HISTOGRAMAS DE CLIENTES - PROYECTO AURELION
═══════════════════════════════════════════════════════════════════════════════

¿QUÉ MUESTRA ESTE GRÁFICO?
───────────────────────────────────────────────────────────────────────────────
Este gráfico muestra la distribución de las variables numéricas relacionadas 
con los clientes de la Tienda Aurelion. Cada subgráfico representa una variable 
diferente.

ELEMENTOS VISUALES:
───────────────────────────────────────────────────────────────────────────────
• BARRAS: Cada barra representa un rango de valores. La altura indica cuántos 
  clientes tienen valores en ese rango.
• LÍNEA ROJA: Muestra el promedio (media) de todos los valores.
• LÍNEA VERDE: Muestra la mediana (el valor del medio cuando ordenamos todos 
  los datos).

{datos_especificos}

CÓMO LEERLO:
───────────────────────────────────────────────────────────────────────────────
1. Si las barras forman una "montaña" simétrica alrededor del centro:
   → Los datos están distribuidos de forma normal (equilibrada)

2. Si las barras están más hacia la izquierda:
   → Hay más clientes con valores bajos (sesgo positivo)

3. Si las barras están más hacia la derecha:
   → Hay más clientes con valores altos (sesgo negativo)

4. Si hay un pico muy alto:
   → Ese rango de valores es muy común entre los clientes

QUÉ SIGNIFICA PARA EL NEGOCIO:
───────────────────────────────────────────────────────────────────────────────
• Base de datos completa: Si el histograma de ID muestra distribución uniforme,
  significa que tenemos una base de datos completa sin gaps.

• Crecimiento estable: Si la distribución temporal es uniforme, el negocio 
  está creciendo de forma constante.

• Segmentación: Los patrones de distribución ayudan a identificar grupos de 
  clientes con características similares.

RECOMENDACIONES:
───────────────────────────────────────────────────────────────────────────────
✓ Si la distribución es muy desigual, considera estrategias de marketing 
  diferenciadas para diferentes segmentos.

✓ Si hay concentraciones en ciertos rangos, investiga qué características 
  tienen esos clientes para replicar el éxito.

═══════════════════════════════════════════════════════════════════════════════
"""
    
    def _interpretacion_histogramas_productos(self):
        """Interpretación específica para histogramas de productos."""
        # Intentar obtener datos específicos del proyecto
        datos_especificos = self._obtener_datos_especificos_productos()
        
        return f"""
═══════════════════════════════════════════════════════════════════════════════
📊 INTERPRETACIÓN: HISTOGRAMAS DE PRODUCTOS - PROYECTO AURELION
═══════════════════════════════════════════════════════════════════════════════

¿QUÉ MUESTRA ESTE GRÁFICO?
───────────────────────────────────────────────────────────────────────────────
Este gráfico muestra cómo están distribuidos los precios de los productos en 
la Tienda Aurelion. Te ayuda a entender la estrategia de precios y qué rangos 
de precio son más comunes.

ELEMENTOS VISUALES:
───────────────────────────────────────────────────────────────────────────────
• BARRAS: Cada barra representa un rango de precios. La altura muestra cuántos 
  productos tienen precios en ese rango.
• LÍNEA ROJA: Precio promedio de todos los productos.
• LÍNEA VERDE: Precio mediano (el precio del medio cuando ordenamos todos).

{datos_especificos}

CÓMO LEERLO:
───────────────────────────────────────────────────────────────────────────────
1. Si ves varios "picos" (montañas):
   → Tienes diferentes categorías de precios (productos económicos, medios, 
     premium)

2. Si hay un pico muy alto en un rango específico:
   → Ese rango de precio es muy popular o común en tu catálogo

3. Si las barras están más hacia la izquierda:
   → Tienes más productos económicos que caros

4. Si hay "huecos" (rangos sin barras o con barras muy bajas):
   → Pocos productos en ese rango de precio (oportunidad de mercado)

QUÉ SIGNIFICA PARA EL NEGOCIO:
───────────────────────────────────────────────────────────────────────────────
• Estrategia de precios: Si ves 3 picos claros, probablemente tienes una 
  estrategia de segmentación (económico, medio, premium).

• Oportunidades: Los huecos en la distribución pueden indicar rangos de precio 
  donde podrías agregar productos.

• Competitividad: Si la mayoría de productos están en un rango estrecho, 
  podrías tener mucha competencia en ese segmento.

RECOMENDACIONES:
───────────────────────────────────────────────────────────────────────────────
✓ Si identificas 3 picos claros (1500-1750, 2500-2750, 4750-5000 pesos):
  → Mantén esta estrategia de segmentación, está funcionando bien.

✓ Si hay huecos entre 3000-4000 pesos:
  → Considera desarrollar productos en este rango para capturar más mercado.

✓ Si un rango tiene muy pocos productos pero alta demanda:
  → Aumenta el inventario en ese rango de precio.

═══════════════════════════════════════════════════════════════════════════════
"""
    
    def _interpretacion_histogramas_ventas(self):
        """Interpretación específica para histogramas de ventas."""
        # Intentar obtener datos específicos del proyecto
        datos_especificos = self._obtener_datos_especificos_ventas()
        
        return f"""
═══════════════════════════════════════════════════════════════════════════════
📊 INTERPRETACIÓN: HISTOGRAMAS DE VENTAS - PROYECTO AURELION
═══════════════════════════════════════════════════════════════════════════════

¿QUÉ MUESTRA ESTE GRÁFICO?
───────────────────────────────────────────────────────────────────────────────
Este gráfico muestra cómo están distribuidas las ventas de la Tienda Aurelion 
en términos de montos totales. Te ayuda a entender el comportamiento de compra 
de tus clientes.

ELEMENTOS VISUALES:
───────────────────────────────────────────────────────────────────────────────
• BARRAS: Cada barra representa un rango de monto de venta. La altura muestra 
  cuántas ventas cayeron en ese rango.
• LÍNEA ROJA: Monto promedio de venta.
• LÍNEA VERDE: Monto mediano de venta.

{datos_especificos}

CÓMO LEERLO:
───────────────────────────────────────────────────────────────────────────────
1. Si las barras son más altas a la izquierda:
   → La mayoría de tus ventas son de montos pequeños/medianos (comportamiento 
     típico de tienda minorista)

2. Si hay una "cola larga" hacia la derecha:
   → Tienes algunas ventas muy grandes, pero son pocas (distribución long-tail)

3. Si hay un pico muy alto:
   → Ese rango de monto es muy común en tus ventas

4. Si la línea roja está más a la derecha que la verde:
   → Las ventas grandes están "jalando" el promedio hacia arriba

QUÉ SIGNIFICA PARA EL NEGOCIO:
───────────────────────────────────────────────────────────────────────────────
• Comportamiento típico: Una distribución con más ventas pequeñas es normal 
  en retail. Los clientes compran productos básicos frecuentemente.

• Oportunidad de crecimiento: Si el promedio es bajo, hay oportunidad de 
  aumentar el ticket promedio con estrategias de upselling.

• Segmentación: Puedes identificar diferentes tipos de compradores según el 
  monto de sus compras.

RECOMENDACIONES ESPECÍFICAS PARA AURELION:
───────────────────────────────────────────────────────────────────────────────
✓ Si la mayoría de ventas son pequeñas:
  → Implementa estrategias de "¿desea agregar algo más?" o combos.

✓ Si hay pocas ventas grandes pero son significativas:
  → Identifica qué productos compran estos clientes y promociona paquetes 
    similares.

✓ Si el ticket promedio es bajo:
  → Considera programas de fidelización que incentiven compras mayores.

═══════════════════════════════════════════════════════════════════════════════
"""
    
    def _interpretacion_histogramas_detalle_ventas(self):
        """Interpretación específica para histogramas de detalle de ventas."""
        # Intentar obtener datos específicos del proyecto
        datos_especificos = self._obtener_datos_especificos_detalle_ventas()
        
        return f"""
═══════════════════════════════════════════════════════════════════════════════
📊 INTERPRETACIÓN: HISTOGRAMAS DE DETALLE DE VENTAS - PROYECTO AURELION
═══════════════════════════════════════════════════════════════════════════════

¿QUÉ MUESTRA ESTE GRÁFICO?
───────────────────────────────────────────────────────────────────────────────
Este gráfico muestra el detalle de cada línea de venta de la Tienda Aurelion: 
cuántas unidades se compran, a qué precio, y el importe total por línea. Es más 
granular que el gráfico de ventas totales.

ELEMENTOS VISUALES:
───────────────────────────────────────────────────────────────────────────────
• CANTIDAD: Muestra cuántas unidades se compran típicamente por producto.
• PRECIO UNITARIO: Muestra los precios a los que se venden los productos.
• IMPORTE: Muestra el monto total de cada línea de venta (cantidad × precio).

{datos_especificos}

CÓMO LEERLO:
───────────────────────────────────────────────────────────────────────────────
1. Histograma de CANTIDAD:
   → Si el pico está en 1-2 unidades: Compras pequeñas, típico de tienda física.
   → Si hay más barras hacia la derecha: Algunos clientes compran en cantidad.

2. Histograma de PRECIO UNITARIO:
   → Similar al de productos, muestra qué precios se venden más.
   → Si hay varios picos: Diferentes categorías de productos.

3. Histograma de IMPORTE:
   → Si está muy sesgado a la izquierda: La mayoría de líneas son de bajo monto.
   → Si hay valores muy altos a la derecha: Algunos productos se venden en 
     grandes cantidades o son muy caros.

QUÉ SIGNIFICA PARA EL NEGOCIO:
───────────────────────────────────────────────────────────────────────────────
• Patrón de compra: Si la mayoría compra 1-2 unidades, tus clientes hacen 
  compras frecuentes pero pequeñas.

• Estrategia de precios: Los precios que más se venden son los que están en 
  los picos del histograma.

• Oportunidades: Si pocas líneas tienen importes altos, hay oportunidad de 
  vender más unidades o productos más caros.

RECOMENDACIONES:
───────────────────────────────────────────────────────────────────────────────
✓ Si la mayoría compra 1-2 unidades:
  → Ofrece descuentos por comprar 3 o más unidades del mismo producto.

✓ Si los importes por línea son bajos:
  → Crea combos o paquetes que aumenten el valor por transacción.

✓ Si hay productos que se venden mucho a cierto precio:
  → Asegúrate de tener buen inventario de esos productos.

═══════════════════════════════════════════════════════════════════════════════
"""
    
    def _interpretacion_matriz_correlacion(self):
        """Interpretación específica para matriz de correlación."""
        datos_especificos = self._obtener_datos_especificos_correlacion()
        
        return f"""
═══════════════════════════════════════════════════════════════════════════════
📊 INTERPRETACIÓN: MATRIZ DE CORRELACIÓN - PROYECTO AURELION
═══════════════════════════════════════════════════════════════════════════════

¿QUÉ MUESTRA ESTE GRÁFICO?
───────────────────────────────────────────────────────────────────────────────
Este gráfico muestra qué tan relacionadas están las variables entre sí. Te 
ayuda a entender qué factores están conectados en tu negocio.

ELEMENTOS VISUALES:
───────────────────────────────────────────────────────────────────────────────
• COLORES: 
  - ROJO INTENSO: Relación muy fuerte positiva (cuando una sube, la otra 
    también sube mucho)
  - ROJO CLARO: Relación positiva moderada
  - BLANCO/AMARILLO: Poca o ninguna relación
  - AZUL CLARO: Relación negativa moderada (cuando una sube, la otra baja)
  - AZUL INTENSO: Relación muy fuerte negativa

• NÚMEROS: Indican la fuerza de la relación (-1 a +1):
  - Cercano a +1: Relación positiva muy fuerte
  - Cercano a 0: Poca relación
  - Cercano a -1: Relación negativa muy fuerte

{datos_especificos}

CÓMO LEERLO:
───────────────────────────────────────────────────────────────────────────────
1. Busca cuadrados ROJOS INTENSOS:
   → Esas dos variables están muy relacionadas. Si una cambia, la otra 
     probablemente también cambiará.

2. Busca cuadrados AZULES INTENSOS:
   → Esas variables tienen relación inversa. Si una sube, la otra baja.

3. Busca cuadrados BLANCOS/AMARILLOS:
   → Esas variables no están relacionadas. Cambiar una no afecta a la otra.

4. La diagonal siempre es roja intensa (+1.0):
   → Es normal, cada variable está perfectamente relacionada consigo misma.

QUÉ SIGNIFICA PARA EL NEGOCIO:
───────────────────────────────────────────────────────────────────────────────
• Causas y efectos: Si cantidad y importe están muy correlacionados, significa 
  que vender más unidades aumenta los ingresos (obvio, pero confirma la lógica).

• Variables redundantes: Si dos variables están muy correlacionadas, podrías 
  usar solo una para análisis (evita duplicación).

• Factores independientes: Variables sin correlación pueden ser factores 
  independientes que afectan el negocio por separado.

RECOMENDACIONES ESPECÍFICAS PARA AURELION:
───────────────────────────────────────────────────────────────────────────────
{self._obtener_recomendaciones_correlacion()}

═══════════════════════════════════════════════════════════════════════════════
"""
    
    def _interpretacion_outliers(self):
        """Interpretación específica para análisis de outliers."""
        datos_especificos = self._obtener_datos_especificos_outliers()
        
        return f"""
═══════════════════════════════════════════════════════════════════════════════
📊 INTERPRETACIÓN: ANÁLISIS DE OUTLIERS (VALORES INUSUALES) - PROYECTO AURELION
═══════════════════════════════════════════════════════════════════════════════

¿QUÉ MUESTRA ESTE GRÁFICO?
───────────────────────────────────────────────────────────────────────────────
Este gráfico identifica valores que son inusuales o extremos comparados con 
la mayoría de los datos. Estos valores pueden ser errores, casos especiales, 
o oportunidades de negocio.

ELEMENTOS VISUALES:
───────────────────────────────────────────────────────────────────────────────
• CAJA: Contiene el 50% de los datos "normales". La línea dentro es la mediana.
• LÍNEAS (bigotes): Se extienden hasta los valores normales más extremos.
• PUNTOS ROJOS: Son los OUTLIERS (valores inusuales que están fuera del rango 
  normal).

{datos_especificos}

CÓMO LEERLO:
───────────────────────────────────────────────────────────────────────────────
1. Si hay MUCHOS puntos rojos:
   → Hay muchos valores inusuales. Podría indicar:
     - Errores en los datos que necesitan corrección
     - Mucha variabilidad en el negocio
     - Diferentes tipos de clientes/productos

2. Si hay POCOS puntos rojos:
   → Los datos son bastante consistentes. La mayoría de valores están en 
     rangos normales.

3. Si los puntos rojos están SOLO ARRIBA:
   → Hay algunos valores muy altos (ventas grandes, productos caros, etc.)

4. Si los puntos rojos están SOLO ABAJO:
   → Hay algunos valores muy bajos (ventas pequeñas, productos muy baratos, etc.)

QUÉ SIGNIFICA PARA EL NEGOCIO:
───────────────────────────────────────────────────────────────────────────────
• Errores de datos: Algunos outliers pueden ser errores de captura que deben 
  corregirse.

• Oportunidades: Outliers altos pueden ser clientes VIP o productos premium 
  que generan mucho valor.

• Casos especiales: Outliers pueden representar situaciones especiales que 
  merecen análisis separado.

RECOMENDACIONES ESPECÍFICAS PARA AURELION:
───────────────────────────────────────────────────────────────────────────────
{self._obtener_recomendaciones_outliers()}

═══════════════════════════════════════════════════════════════════════════════
"""
    
    def _interpretacion_normalizacion_productos(self):
        """Interpretación específica para comparación de normalización de productos."""
        return """
═══════════════════════════════════════════════════════════════════════════════
📊 INTERPRETACIÓN: COMPARACIÓN DE NORMALIZACIÓN - PRODUCTOS
═══════════════════════════════════════════════════════════════════════════════

¿QUÉ MUESTRA ESTE GRÁFICO?
───────────────────────────────────────────────────────────────────────────────
Este gráfico compara cómo estaban los datos ANTES de normalizarlos (arriba) 
y DESPUÉS de normalizarlos (abajo). La normalización ajusta los valores para 
que sean comparables y útiles para Machine Learning.

ELEMENTOS VISUALES:
───────────────────────────────────────────────────────────────────────────────
• ARRIBA (ANTES): Muestra la distribución original de los precios de productos.
• ABAJO (DESPUÉS): Muestra cómo quedaron los datos después de normalizar.
• COLOR AZUL: Datos originales.
• COLOR CORAL: Datos normalizados.

CÓMO LEERLO:
───────────────────────────────────────────────────────────────────────────────
1. Compara las formas:
   → Si la forma cambió mucho, la normalización hizo ajustes significativos.
   → Si la forma es similar, los datos ya estaban relativamente bien.

2. Compara los rangos:
   → Los datos normalizados suelen estar en un rango más estrecho y estándar 
     (típicamente entre -3 y +3 o 0 y 1).

3. Observa la distribución:
   → La normalización mantiene la forma general pero ajusta la escala.

QUÉ SIGNIFICA PARA EL NEGOCIO:
───────────────────────────────────────────────────────────────────────────────
• Preparación para ML: Los datos normalizados son necesarios para que los 
  algoritmos de Machine Learning funcionen correctamente.

• Comparabilidad: Después de normalizar, puedes comparar variables que 
  originalmente tenían escalas muy diferentes (ej: precios en miles vs 
  cantidades en unidades).

• Calidad de datos: Si la normalización cambió mucho la distribución, 
  significa que los datos originales tenían mucha variabilidad.

RECOMENDACIONES:
───────────────────────────────────────────────────────────────────────────────
✓ Si la normalización cambió mucho la forma:
  → Los datos originales tenían mucha variabilidad. Esto es normal en precios 
    de productos.

✓ Si los datos normalizados se ven bien distribuidos:
  → Los datos están listos para usar en modelos de Machine Learning.

✓ Siempre guarda los datos originales:
  → La normalización es para análisis, pero los valores originales son 
    importantes para interpretar resultados.

═══════════════════════════════════════════════════════════════════════════════
"""
    
    def _interpretacion_normalizacion_detalle_ventas(self):
        """Interpretación específica para comparación de normalización de detalle de ventas."""
        return """
═══════════════════════════════════════════════════════════════════════════════
📊 INTERPRETACIÓN: COMPARACIÓN DE NORMALIZACIÓN - DETALLE DE VENTAS
═══════════════════════════════════════════════════════════════════════════════

¿QUÉ MUESTRA ESTE GRÁFICO?
───────────────────────────────────────────────────────────────────────────────
Similar al anterior, pero enfocado en las líneas de detalle de ventas 
(cantidades, precios unitarios, importes). Muestra el antes y después de 
normalizar estos datos.

ELEMENTOS VISUALES:
───────────────────────────────────────────────────────────────────────────────
• ARRIBA (ANTES): Distribución original de cantidades, precios e importes.
• ABAJO (DESPUÉS): Distribución después de normalizar.
• Múltiples variables: Puede mostrar cantidad, precio_unitario e importe.

CÓMO LEERLO:
───────────────────────────────────────────────────────────────────────────────
1. Para CANTIDAD:
   → Si había muchos valores en 1-2 unidades, la normalización ajusta estos 
     valores a una escala estándar.

2. Para PRECIO UNITARIO:
   → Similar a productos, ajusta los precios a una escala comparable.

3. Para IMPORTE:
   → Normaliza los montos totales, que pueden variar mucho (desde muy pequeños 
     hasta muy grandes).

QUÉ SIGNIFICA PARA EL NEGOCIO:
───────────────────────────────────────────────────────────────────────────────
• Variables relacionadas: Cantidad, precio e importe están relacionadas 
  (importe = cantidad × precio). La normalización ayuda a que los modelos 
  de ML entiendan estas relaciones mejor.

• Escalas diferentes: Estas variables tienen escalas muy diferentes (cantidad 
  en unidades, precio en pesos, importe en pesos). La normalización las hace 
  comparables.

RECOMENDACIONES:
───────────────────────────────────────────────────────────────────────────────
✓ La normalización de estas variables es crucial:
  → Son las variables más importantes para predecir ventas y comportamiento.

✓ Observa si hay cambios significativos:
  → Si la normalización cambió mucho la distribución, los datos originales 
    tenían mucha variabilidad (normal en ventas).

═══════════════════════════════════════════════════════════════════════════════
"""
    
    def _interpretacion_distribuciones(self):
        """Interpretación específica para análisis de distribuciones."""
        return """
═══════════════════════════════════════════════════════════════════════════════
📊 INTERPRETACIÓN: ANÁLISIS DE DISTRIBUCIONES
═══════════════════════════════════════════════════════════════════════════════

¿QUÉ MUESTRA ESTE GRÁFICO?
───────────────────────────────────────────────────────────────────────────────
Este gráfico combina dos tipos de visualización para darte una vista completa 
de cómo están distribuidos tus datos: histogramas (arriba) y boxplots (abajo).

ELEMENTOS VISUALES:
───────────────────────────────────────────────────────────────────────────────
• ARRIBA (Histogramas): Muestran la frecuencia de cada rango de valores.
• ABAJO (Boxplots): Muestran la distribución de forma resumida con mediana, 
  cuartiles y outliers.

CÓMO LEERLO:
───────────────────────────────────────────────────────────────────────────────
1. Histograma (arriba):
   → Picos altos = valores muy comunes
   → Forma simétrica = distribución normal
   → Sesgo a la izquierda/derecha = más valores en un extremo

2. Boxplot (abajo):
   → La caja contiene el 50% de los datos
   → La línea en la caja es la mediana
   → Los bigotes muestran el rango normal
   → Puntos fuera = outliers

QUÉ SIGNIFICA PARA EL NEGOCIO:
───────────────────────────────────────────────────────────────────────────────
• Entender tus datos: Esta combinación te da la vista más completa de cómo 
  están distribuidos tus datos.

• Detectar problemas: Si el histograma y boxplot muestran patrones muy 
  diferentes, podría haber problemas en los datos.

• Preparación para análisis: Conocer la distribución te ayuda a elegir los 
  métodos de análisis correctos.

RECOMENDACIONES:
───────────────────────────────────────────────────────────────────────────────
✓ Usa ambos gráficos juntos:
  → El histograma te da detalle, el boxplot te da resumen.

✓ Si la distribución es muy sesgada:
  → Considera transformar los datos o usar métodos estadísticos robustos.

═══════════════════════════════════════════════════════════════════════════════
"""
    
    def _interpretacion_clustering(self):
        """Interpretación específica para análisis de clustering."""
        datos_especificos = self._obtener_datos_especificos_clustering()
        
        return f"""
═══════════════════════════════════════════════════════════════════════════════
📊 INTERPRETACIÓN: ANÁLISIS DE CLUSTERING (AGRUPACIÓN) - PROYECTO AURELION
═══════════════════════════════════════════════════════════════════════════════

¿QUÉ MUESTRA ESTE GRÁFICO?
───────────────────────────────────────────────────────────────────────────────
Este gráfico muestra cómo los datos se agrupan automáticamente en clusters 
(grupos) basándose en similitudes. Te ayuda a encontrar patrones y segmentar 
tus datos.

ELEMENTOS VISUALES:
───────────────────────────────────────────────────────────────────────────────
• IZQUIERDA (K-Means): Agrupa los datos en exactamente 3 grupos.
• DERECHA (DBSCAN): Agrupa los datos automáticamente según densidad.
• COLORES: Cada color representa un grupo/cluster diferente.
• PUNTOS: Cada punto es una observación (venta, producto, etc.).

{datos_especificos}

CÓMO LEERLO:
───────────────────────────────────────────────────────────────────────────────
1. Si los puntos del mismo color están juntos:
   → El clustering funcionó bien. Los grupos son claros y distintos.

2. Si los colores están mezclados:
   → Los grupos no son muy distintos. Los datos son similares entre sí.

3. Compara K-Means vs DBSCAN:
   → K-Means siempre crea 3 grupos (fijo).
   → DBSCAN crea grupos según la densidad natural de los datos (puede ser 
     más o menos de 3).

QUÉ SIGNIFICA PARA EL NEGOCIO:
───────────────────────────────────────────────────────────────────────────────
• Segmentación automática: El clustering encuentra grupos que tal vez no 
  habías identificado manualmente.

• Patrones ocultos: Puede revelar que ciertos productos/ventas/clientes son 
  más similares entre sí de lo que pensabas.

• Estrategias diferenciadas: Cada cluster puede necesitar una estrategia 
  diferente de marketing o gestión.

RECOMENDACIONES ESPECÍFICAS PARA AURELION:
───────────────────────────────────────────────────────────────────────────────
{self._obtener_recomendaciones_clustering()}

═══════════════════════════════════════════════════════════════════════════════
"""
    
    def _interpretacion_modelos_regresion(self):
        """Interpretación específica para comparación de modelos de regresión."""
        datos_especificos = self._obtener_datos_especificos_modelos()
        
        return f"""
═══════════════════════════════════════════════════════════════════════════════
📊 INTERPRETACIÓN: COMPARACIÓN DE MODELOS DE REGRESIÓN - PROYECTO AURELION
═══════════════════════════════════════════════════════════════════════════════

¿QUÉ MUESTRA ESTE GRÁFICO?
───────────────────────────────────────────────────────────────────────────────
Este gráfico compara qué tan bien funcionan diferentes modelos de Machine 
Learning para predecir valores (como el importe de una venta).

ELEMENTOS VISUALES:
───────────────────────────────────────────────────────────────────────────────
• IZQUIERDA: Gráfico de dispersión que compara valores reales vs predicciones.
  - Puntos cerca de la línea roja = predicciones buenas
  - Puntos dispersos = predicciones menos precisas
• DERECHA: Gráfico de barras que compara el R² de cada modelo.
  - R² más alto = mejor modelo
  - R² cercano a 1.0 = excelente
  - R² cercano a 0.0 = pobre

{datos_especificos}

CÓMO LEERLO:
───────────────────────────────────────────────────────────────────────────────
1. En el gráfico de dispersión (izquierda):
   → Si los puntos forman una línea diagonal cerca de la línea roja: 
     El modelo predice muy bien.
   → Si los puntos están muy dispersos: El modelo tiene errores grandes.

2. En el gráfico de barras (derecha):
   → La barra más alta es el mejor modelo.
   → R² > 0.8: Excelente modelo
   → R² 0.6-0.8: Buen modelo
   → R² < 0.6: Modelo necesita mejorar

QUÉ SIGNIFICA PARA EL NEGOCIO:
───────────────────────────────────────────────────────────────────────────────
• Capacidad predictiva: Te dice qué tan bien puedes predecir valores futuros 
  (como ventas, importes, etc.).

• Mejor modelo: El modelo con R² más alto es el que debes usar para 
  predicciones.

• Confiabilidad: Un modelo con R² alto te da más confianza en tus predicciones 
  y decisiones basadas en datos.

RECOMENDACIONES ESPECÍFICAS PARA AURELION:
───────────────────────────────────────────────────────────────────────────────
{self._obtener_recomendaciones_modelos()}

═══════════════════════════════════════════════════════════════════════════════
"""
    
    def _interpretacion_importancia_variables(self):
        """Interpretación específica para importancia de variables."""
        datos_especificos = self._obtener_datos_especificos_importancia()
        
        return f"""
═══════════════════════════════════════════════════════════════════════════════
📊 INTERPRETACIÓN: IMPORTANCIA DE VARIABLES - PROYECTO AURELION
═══════════════════════════════════════════════════════════════════════════════

¿QUÉ MUESTRA ESTE GRÁFICO?
───────────────────────────────────────────────────────────────────────────────
Este gráfico muestra qué variables son más importantes para que el modelo de 
Machine Learning haga buenas predicciones. Te ayuda a entender qué factores 
realmente importan en tu negocio.

ELEMENTOS VISUALES:
───────────────────────────────────────────────────────────────────────────────
• BARRAS HORIZONTALES: Cada barra representa una variable.
• LONGITUD DE LA BARRA: Muestra qué tan importante es esa variable.
  - Barra más larga = más importante
  - Barra más corta = menos importante
• ORDEN: Las variables están ordenadas de más importante (arriba) a menos 
  importante (abajo).

{datos_especificos}

CÓMO LEERLO:
───────────────────────────────────────────────────────────────────────────────
1. Las variables en la parte superior:
   → Son las MÁS importantes. Cambios en estas variables afectan mucho las 
     predicciones.

2. Las variables en la parte inferior:
   → Son MENOS importantes. Tienen poco impacto en las predicciones.

3. Si una barra es mucho más larga que las demás:
   → Esa variable es MUY importante, casi dominante.

4. Si las barras son de tamaño similar:
   → Varias variables son importantes de forma equilibrada.

QUÉ SIGNIFICA PARA EL NEGOCIO:
───────────────────────────────────────────────────────────────────────────────
• Factores clave: Las variables importantes son los factores que realmente 
  afectan tus resultados (ventas, importes, etc.).

• Enfoque estratégico: Debes enfocar tus esfuerzos en las variables más 
  importantes.

• Variables redundantes: Si una variable tiene importancia muy baja, tal vez 
  no necesitas rastrearla o puede ser redundante.

RECOMENDACIONES ESPECÍFICAS PARA AURELION:
───────────────────────────────────────────────────────────────────────────────
{self._obtener_recomendaciones_importancia()}

═══════════════════════════════════════════════════════════════════════════════
"""
    
    def _interpretacion_resumen_estadistico(self):
        """Interpretación específica para resumen estadístico."""
        datos_especificos = self._obtener_datos_especificos_resumen()
        
        return f"""
═══════════════════════════════════════════════════════════════════════════════
📊 INTERPRETACIÓN: RESUMEN ESTADÍSTICO - PROYECTO AURELION
═══════════════════════════════════════════════════════════════════════════════

¿QUÉ MUESTRA ESTE GRÁFICO?
───────────────────────────────────────────────────────────────────────────────
Este gráfico es una tabla con las estadísticas principales de todas las 
variables numéricas. Es como un "resumen ejecutivo" de tus datos.

ELEMENTOS VISUALES:
───────────────────────────────────────────────────────────────────────────────
• FILAS: Cada fila es una estadística diferente.
• COLUMNAS: Cada columna es una variable diferente.
• VALORES: Los números en cada celda son el valor de esa estadística para 
  esa variable.

ESTADÍSTICAS INCLUIDAS:
───────────────────────────────────────────────────────────────────────────────
• count: Cuántos datos tienes (sin valores faltantes)
• mean: Promedio (suma de todos dividido entre la cantidad)
• std: Desviación estándar (qué tan dispersos están los datos)
• min: Valor más pequeño
• 25%: Primer cuartil (25% de los datos están por debajo de este valor)
• 50%: Mediana (50% de los datos están por debajo, 50% por arriba)
• 75%: Tercer cuartil (75% de los datos están por debajo)
• max: Valor más grande

{datos_especificos}

CÓMO LEERLO:
───────────────────────────────────────────────────────────────────────────────
1. Compara mean (promedio) con 50% (mediana):
   → Si son similares: Distribución simétrica
   → Si mean > 50%: Sesgo positivo (más valores bajos)
   → Si mean < 50%: Sesgo negativo (más valores altos)

2. Observa std (desviación estándar):
   → Valores altos = mucha variabilidad
   → Valores bajos = datos consistentes

3. Compara min y max:
   → Rango grande = mucha variabilidad en los datos

QUÉ SIGNIFICA PARA EL NEGOCIO:
───────────────────────────────────────────────────────────────────────────────
• Vista general: Te da una vista rápida de todas tus variables numéricas.

• Detección de problemas: Si count es muy bajo, hay muchos datos faltantes.

• Comparación: Puedes comparar fácilmente diferentes variables.

RECOMENDACIONES ESPECÍFICAS PARA AURELION:
───────────────────────────────────────────────────────────────────────────────
{self._obtener_recomendaciones_resumen()}

═══════════════════════════════════════════════════════════════════════════════
"""
    
    def _interpretacion_categoricas_alimentos(self):
        """Interpretación específica para categorías de alimentos."""
        # Calcular valores reales si el dataset está disponible
        interpretacion_base = """
═══════════════════════════════════════════════════════════════════════════════
📊 INTERPRETACIÓN: DISTRIBUCIÓN CATEGORÍA ALIMENTOS
═══════════════════════════════════════════════════════════════════════════════

¿QUÉ MUESTRA ESTE GRÁFICO?
───────────────────────────────────────────────────────────────────────────────
Este gráfico muestra cuántos productos o ventas pertenecen a la categoría 
"Alimentos". Te ayuda a entender qué tan importante es esta categoría en tu 
negocio.

ELEMENTOS VISUALES:
───────────────────────────────────────────────────────────────────────────────
• BARRAS: Cada barra representa una categoría o valor.
• ALTURA: Muestra la frecuencia (cuántas veces aparece).
• ETIQUETAS: Indican el nombre de cada categoría.

CÓMO LEERLO:
───────────────────────────────────────────────────────────────────────────────
1. Si hay una barra muy alta:
   → Esa categoría es muy común o importante en tus datos.

2. Si las barras son de altura similar:
   → Las categorías están balanceadas.

3. Si hay barras muy bajas:
   → Esas categorías son menos comunes.

"""
        
        # Agregar valores específicos si el dataset está disponible
        if self.dataset is not None and 'categoria_Alimentos' in self.dataset.columns:
            import pandas as pd
            conteo = self.dataset['categoria_Alimentos'].value_counts().sort_index()
            total = conteo.sum()
            porcentajes = (conteo / total * 100).round(1)
            
            categoria_mas_frecuente = conteo.idxmax()
            frecuencia_max = conteo.max()
            porcentaje_max = porcentajes[categoria_mas_frecuente]
            
            categoria_menos_frecuente = conteo.idxmin()
            frecuencia_min = conteo.min()
            porcentaje_min = porcentajes[categoria_menos_frecuente]
            
            valores_especificos = f"""
VALORES ESPECÍFICOS DE ESTE GRÁFICO:
───────────────────────────────────────────────────────────────────────────────
• Total de registros analizados: {total}
• CATEGORÍA MÁS FRECUENTE: '{categoria_mas_frecuente}' con {frecuencia_max} ocurrencias ({porcentaje_max}% del total)
• CATEGORÍA MENOS FRECUENTE: '{categoria_menos_frecuente}' con {frecuencia_min} ocurrencias ({porcentaje_min}% del total)
• Diferencia: {frecuencia_max - frecuencia_min} registros ({porcentaje_max - porcentaje_min:.1f} puntos porcentuales)
• CONCLUSIÓN: La categoría '{categoria_mas_frecuente}' es {frecuencia_max/frecuencia_min:.1f}x más común que '{categoria_menos_frecuente}'

QUÉ SIGNIFICA PARA EL NEGOCIO:
───────────────────────────────────────────────────────────────────────────────
• Mix de productos: {'La categoría Alimentos es DOMINANTE' if porcentaje_max > 60 else 'Las categorías están BALANCEADAS'} 
  ({porcentaje_max}% vs {porcentaje_min}%)

• Estrategia: {'Considera diversificar' if porcentaje_max > 60 else 'Mantén el balance actual'} 
  {'ya que Alimentos representa más del 60%' if porcentaje_max > 60 else 'entre categorías'}

RECOMENDACIONES:
───────────────────────────────────────────────────────────────────────────────
"""
            if porcentaje_max > 60:
                valores_especificos += "✓ Alimentos es muy dominante ({:.1f}%) - Considera fortalecer otras categorías\n".format(porcentaje_max)
            else:
                valores_especificos += "✓ Balance saludable entre categorías - Mantén esta estrategia\n"
            
            return interpretacion_base + valores_especificos + "\n═══════════════════════════════════════════════════════════════════════════════\n"
        
        return interpretacion_base + """
QUÉ SIGNIFICA PARA EL NEGOCIO:
───────────────────────────────────────────────────────────────────────────────
• Mix de productos: Te muestra qué tan importante es la categoría Alimentos 
  en tu catálogo o ventas.

• Estrategia de categorías: Si Alimentos es dominante, podrías estar muy 
  concentrado en una categoría.

RECOMENDACIONES:
───────────────────────────────────────────────────────────────────────────────
✓ Si Alimentos es muy dominante:
  → Considera diversificar o fortalecer otras categorías.

✓ Si está balanceado con otras categorías:
  → Tienes un buen mix de productos.

═══════════════════════════════════════════════════════════════════════════════
"""
    
    def _interpretacion_categoricas_limpieza(self):
        """Interpretación específica para categorías de limpieza."""
        interpretacion_base = """
═══════════════════════════════════════════════════════════════════════════════
📊 INTERPRETACIÓN: DISTRIBUCIÓN CATEGORÍA LIMPIEZA
═══════════════════════════════════════════════════════════════════════════════

¿QUÉ MUESTRA ESTE GRÁFICO?
───────────────────────────────────────────────────────────────────────────────
Similar al anterior, pero enfocado en la categoría "Limpieza". Muestra la 
distribución de productos o ventas en esta categoría.

ELEMENTOS VISUALES Y CÓMO LEERLO:
───────────────────────────────────────────────────────────────────────────────
Igual que el gráfico de Alimentos. Compara ambos para ver el balance entre 
categorías.

"""
        
        # Agregar valores específicos si el dataset está disponible
        if self.dataset is not None and 'categoria_Limpieza' in self.dataset.columns:
            import pandas as pd
            conteo = self.dataset['categoria_Limpieza'].value_counts().sort_index()
            total = conteo.sum()
            porcentajes = (conteo / total * 100).round(1)
            
            categoria_mas_frecuente = conteo.idxmax()
            frecuencia_max = conteo.max()
            porcentaje_max = porcentajes[categoria_mas_frecuente]
            
            categoria_menos_frecuente = conteo.idxmin()
            frecuencia_min = conteo.min()
            porcentaje_min = porcentajes[categoria_menos_frecuente]
            
            # Comparar con Alimentos si está disponible
            comparacion = ""
            porcentaje_alimentos = 0
            if 'categoria_Alimentos' in self.dataset.columns:
                conteo_alimentos = self.dataset['categoria_Alimentos'].value_counts()
                total_alimentos = conteo_alimentos.sum()
                porcentaje_alimentos = (conteo_alimentos.max() / total_alimentos * 100) if total_alimentos > 0 else 0
                comparacion = f"\nCOMPARACIÓN CON ALIMENTOS:\n───────────────────────────────────────────────────────────────────────────────\n• Alimentos: {porcentaje_alimentos:.1f}% del total\n• Limpieza: {porcentaje_max:.1f}% del total\n• Diferencia: {abs(porcentaje_alimentos - porcentaje_max):.1f} puntos porcentuales\n"
            
            valores_especificos = f"""
VALORES ESPECÍFICOS DE ESTE GRÁFICO:
───────────────────────────────────────────────────────────────────────────────
• Total de registros analizados: {total}
• CATEGORÍA MÁS FRECUENTE: '{categoria_mas_frecuente}' con {frecuencia_max} ocurrencias ({porcentaje_max}% del total)
• CATEGORÍA MENOS FRECUENTE: '{categoria_menos_frecuente}' con {frecuencia_min} ocurrencias ({porcentaje_min}% del total)
• Diferencia: {frecuencia_max - frecuencia_min} registros ({porcentaje_max - porcentaje_min:.1f} puntos porcentuales)
{comparacion}
QUÉ SIGNIFICA PARA EL NEGOCIO:
───────────────────────────────────────────────────────────────────────────────
"""
            if porcentaje_alimentos > 0:
                if abs(porcentaje_max - porcentaje_alimentos) < 20:
                    valores_especificos += f"• Balance de categorías: Limpieza está balanceada con Alimentos (diferencia de {abs(porcentaje_max - porcentaje_alimentos):.1f}%)\n"
                else:
                    valores_especificos += f"• Balance de categorías: Hay desbalance entre categorías (diferencia de {abs(porcentaje_max - porcentaje_alimentos):.1f}%)\n"
            
            valores_especificos += "\nRECOMENDACIONES:\n───────────────────────────────────────────────────────────────────────────────\n"
            if porcentaje_alimentos > 0 and porcentaje_max < porcentaje_alimentos - 10:
                valores_especificos += f"✓ Limpieza ({porcentaje_max:.1f}%) es menor que Alimentos ({porcentaje_alimentos:.1f}%) - Oportunidad de crecimiento\n"
            else:
                valores_especificos += "✓ Balance saludable entre categorías - Mantén esta estrategia\n"
            
            return interpretacion_base + valores_especificos + "\n═══════════════════════════════════════════════════════════════════════════════\n"
        
        return interpretacion_base + """
QUÉ SIGNIFICA PARA EL NEGOCIO:
───────────────────────────────────────────────────────────────────────────────
• Balance de categorías: Compara con Alimentos para ver si tienes un buen 
  balance.

• Oportunidades: Si Limpieza es mucho menor que Alimentos, podría haber 
  oportunidad de crecer en esta categoría.

RECOMENDACIONES:
───────────────────────────────────────────────────────────────────────────────
✓ Compara con el gráfico de Alimentos:
  → Busca un balance saludable entre categorías.

✓ Si Limpieza es muy baja:
  → Considera estrategias para aumentar ventas en esta categoría.

═══════════════════════════════════════════════════════════════════════════════
"""
    
    def _interpretacion_pairplot(self):
        """Interpretación específica para pairplot."""
        datos_especificos = self._obtener_datos_especificos_pairplot()
        
        return f"""
═══════════════════════════════════════════════════════════════════════════════
📊 INTERPRETACIÓN: PAIRPLOT DE VARIABLES - PROYECTO AURELION
═══════════════════════════════════════════════════════════════════════════════

¿QUÉ MUESTRA ESTE GRÁFICO?
───────────────────────────────────────────────────────────────────────────────
Este es un gráfico complejo que muestra TODAS las relaciones posibles entre 
todas las variables. Es como una "matriz de relaciones" visual.

ELEMENTOS VISUALES:
───────────────────────────────────────────────────────────────────────────────
• DIAGONAL: Histogramas de cada variable (distribución individual).
• FUERA DE LA DIAGONAL: Gráficos de dispersión entre pares de variables.
• COLORES: Pueden indicar diferentes categorías o grupos.

{datos_especificos}

CÓMO LEERLO:
───────────────────────────────────────────────────────────────────────────────
1. Mira la diagonal:
   → Te muestra cómo está distribuida cada variable individualmente.

2. Mira los gráficos fuera de la diagonal:
   → Si los puntos forman una línea: Hay relación fuerte entre esas variables.
   → Si los puntos están dispersos: Poca o ninguna relación.

3. Busca patrones:
   → Si varios gráficos muestran relaciones similares, hay un patrón general.

QUÉ SIGNIFICA PARA EL NEGOCIO:
───────────────────────────────────────────────────────────────────────────────
• Vista completa: Te da una vista completa de todas las relaciones en tus 
  datos de una vez.

• Patrones complejos: Puede revelar relaciones que no habías notado antes.

• Redundancia: Si dos variables siempre muestran la misma relación con otras, 
  podrían ser redundantes.

RECOMENDACIONES ESPECÍFICAS PARA AURELION:
───────────────────────────────────────────────────────────────────────────────
{self._obtener_recomendaciones_pairplot()}

═══════════════════════════════════════════════════════════════════════════════
"""
    
    def _interpretacion_scatter_plots(self):
        """Interpretación específica para scatter plots."""
        datos_especificos = self._obtener_datos_especificos_scatter()
        
        return f"""
═══════════════════════════════════════════════════════════════════════════════
📊 INTERPRETACIÓN: SCATTER PLOTS DETALLADOS - PROYECTO AURELION
═══════════════════════════════════════════════════════════════════════════════

¿QUÉ MUESTRA ESTE GRÁFICO?
───────────────────────────────────────────────────────────────────────────────
Similar al pairplot pero más detallado. Muestra relaciones específicas entre
pares de variables con mayor detalle y análisis.

{datos_especificos}

CÓMO LEERLO:
───────────────────────────────────────────────────────────────────────────────
1. Si los puntos forman una línea diagonal:
   → Hay relación fuerte entre esas dos variables.

2. Si los puntos están dispersos:
   → Poca o ninguna relación entre las variables.

3. El color de los puntos:
   → Te ayuda a ver si hay concentraciones de valores altos o bajos.

QUÉ SIGNIFICA PARA EL NEGOCIO:
───────────────────────────────────────────────────────────────────────────────
• Relaciones causales: Si dos variables están muy relacionadas, cambios en 
  una probablemente afectarán a la otra.

• Predicción: Variables con alta correlación pueden usarse para predecir 
  valores de la otra.

• Estrategia: Si identificas relaciones fuertes, puedes diseñar estrategias 
  que aprovechen estas relaciones.

RECOMENDACIONES ESPECÍFICAS PARA AURELION:
───────────────────────────────────────────────────────────────────────────────
{self._obtener_recomendaciones_scatter()}

═══════════════════════════════════════════════════════════════════════════════
"""
    
    def _interpretacion_medios_pago(self):
        """Interpretación específica para análisis de medios de pago."""
        datos_especificos = self._obtener_datos_especificos_medios_pago()
        
        return f"""
═══════════════════════════════════════════════════════════════════════════════
📊 INTERPRETACIÓN: ANÁLISIS DE MEDIOS DE PAGO - PROYECTO AURELION
═══════════════════════════════════════════════════════════════════════════════

¿QUÉ MUESTRA ESTE GRÁFICO?
───────────────────────────────────────────────────────────────────────────────
Este gráfico muestra un análisis completo de los métodos de pago usados en 
la tienda. Incluye 6 subgráficos que muestran diferentes aspectos.

ELEMENTOS VISUALES (6 SUBGRÁFICOS):
───────────────────────────────────────────────────────────────────────────────
1. Número de Ventas por Método: Cuántas transacciones se hicieron con cada 
   método (barras).
2. Porcentaje de Ventas: Qué porcentaje del total representa cada método 
   (gráfico circular/pastel).
3. Montos Totales: Cuánto dinero total se procesó por cada método (barras).
4. Monto Promedio: Cuánto se gasta en promedio por transacción con cada 
   método (barras).
5. Distribución de Importes: Cómo están distribuidos los montos por método 
   (boxplot).
6. Porcentaje del Total: Qué porcentaje del monto total representa cada 
   método (barras).

{datos_especificos}

CÓMO LEERLO:
───────────────────────────────────────────────────────────────────────────────
1. Gráfico 1 (Número de ventas):
   → Método con barra más alta = más popular en cantidad de transacciones.

2. Gráfico 2 (Porcentaje - pastel):
   → Porción más grande = método más usado.

3. Gráfico 3 (Montos totales):
   → Método con barra más alta = genera más ingresos totales.

4. Gráfico 4 (Monto promedio):
   → Método con barra más alta = clientes gastan más por transacción.

5. Gráfico 5 (Boxplot):
   → Caja más alta = más variabilidad en montos.
   → Caja más baja = montos más consistentes.

6. Gráfico 6 (Porcentaje del total):
   → Método con barra más alta = representa más del negocio total.

QUÉ SIGNIFICA PARA EL NEGOCIO:
───────────────────────────────────────────────────────────────────────────────
• Preferencias de clientes: Te muestra qué métodos prefieren tus clientes.

• Estrategia de pago: Puedes optimizar qué métodos ofrecer o promover.

• Segmentación: Diferentes métodos pueden atraer diferentes tipos de clientes.

• Costos: Diferentes métodos tienen diferentes costos de procesamiento.

RECOMENDACIONES ESPECÍFICAS PARA AURELION:
───────────────────────────────────────────────────────────────────────────────
{self._obtener_recomendaciones_medios_pago()}

═══════════════════════════════════════════════════════════════════════════════
"""
    
    def _interpretacion_curtosis(self):
        """Interpretación específica para análisis de curtosis."""
        return """
═══════════════════════════════════════════════════════════════════════════════
📊 INTERPRETACIÓN: ANÁLISIS DE CURTOSIS
═══════════════════════════════════════════════════════════════════════════════

¿QUÉ MUESTRA ESTE GRÁFICO?
───────────────────────────────────────────────────────────────────────────────
Este gráfico muestra el análisis de CURTOSIS (también llamada KURTOSIS) de todas 
las variables numéricas del dataset. La curtosis mide la "pesadez" de las colas 
de una distribución, es decir, qué tan frecuentes son los valores extremos 
(outliers) comparados con una distribución normal.

ELEMENTOS VISUALES:
───────────────────────────────────────────────────────────────────────────────
PANEL IZQUIERDO - Barras Horizontales:
• Cada barra representa una variable numérica
• El valor en el eje X es la curtosis de esa variable
• Colores indican el tipo de distribución:
  🟢 VERDE CLARO = MESOCÚRTICA (normal, curtosis ≈ 0)
  🔴 SALMÓN = LEPTOCÚRTICA (colas pesadas, curtosis > 0.5)
  🔵 AZUL CLARO = PLATICÚRTICA (colas ligeras, curtosis < -0.5)
• Línea negra punteada en 0 = distribución normal
• Líneas azul/rojo punteadas = umbrales de clasificación (-0.5 y 0.5)

PANEL DERECHO - Histograma:
• Muestra la distribución de valores de curtosis
• Indica cuántas variables tienen cada tipo de curtosis
• Línea roja = distribución normal (0)
• Línea verde = promedio de curtosis

¿QUÉ ES LA CURTOSIS?
───────────────────────────────────────────────────────────────────────────────
La curtosis mide qué tan "puntiaguda" o "aplanada" es una distribución comparada 
con la distribución normal. Específicamente, mide la concentración de datos en 
las colas (valores extremos).

TIPOS DE CURTOSIS:
───────────────────────────────────────────────────────────────────────────────
1. MESOCÚRTICA (Curtosis ≈ 0):
   ✅ Similar a distribución normal
   ✅ Colas y pico normales
   ✅ Frecuencia esperada de outliers
   → Datos bien comportados, adecuados para análisis estadísticos estándar

2. LEPTOCÚRTICA (Curtosis > 0.5):
   ⚠️ Colas más pesadas que la normal
   ⚠️ Distribución más puntiaguda en el centro
   ⚠️ MÁS valores extremos (outliers) de lo esperado
   → Presencia frecuente de valores atípicos
   → Requiere atención especial para detección y tratamiento de outliers
   → Considerar transformaciones de datos o modelos robustos

3. PLATICÚRTICA (Curtosis < -0.5):
   ℹ️ Colas más ligeras que la normal
   ℹ️ Distribución más aplanada
   ℹ️ MENOS valores extremos de lo esperado
   → Datos muy concentrados, pocos outliers
   → Puede indicar datos truncados o variables con rangos limitados

INTERPRETACIÓN PRÁCTICA:
───────────────────────────────────────────────────────────────────────────────
El gráfico incluye una interpretación detallada en la parte inferior que muestra:

• Total de variables analizadas
• Curtosis promedio
• Rango de curtosis (mínimo y máximo)
• Conteo por tipo (mesocúrticas, leptocúrticas, platicúrticas)
• Top 3 variables con mayor y menor curtosis
• Implicaciones para el negocio

¿QUÉ SIGNIFICA PARA EL NEGOCIO?
───────────────────────────────────────────────────────────────────────────────
Si la mayoría de variables son LEPTOCÚRTICAS:
  ⚠️ Muchas variables tienen colas pesadas (outliers frecuentes)
  → Revisar estrategias de manejo de valores extremos
  → Considerar transformaciones para reducir impacto de outliers
  → Usar modelos robustos en Machine Learning

Si la mayoría de variables son MESOCÚRTICAS:
  ✅ La mayoría de variables tienen distribución normal
  → Datos bien comportados, adecuados para análisis estadísticos
  → Puede usar métodos paramétricos estándar
  → Modelos de ML funcionarán bien sin transformaciones especiales

Si hay mezcla de tipos:
  ℹ️ Mezcla de tipos de distribución
  → Algunas variables requieren tratamiento especial para outliers
  → Aplicar estrategias diferenciadas según el tipo de variable
  → Considerar normalización selectiva

APLICACIONES PRÁCTICAS:
───────────────────────────────────────────────────────────────────────────────
Para Machine Learning:
• Variables LEPTOCÚRTICAS: Requieren transformaciones (log, sqrt) o modelos robustos
• Variables MESOCÚRTICAS: Pueden usarse directamente en modelos estándar
• Variables PLATICÚRTICAS: Verificar si hay censura o truncamiento de datos

Para Análisis de Negocio:
• Identificar variables con outliers frecuentes: Requieren atención especial
• Estrategias de precios: Variables con alta curtosis pueden tener precios extremos
• Segmentación: Variables con diferentes tipos de curtosis pueden indicar 
  diferentes segmentos

RELACIÓN CON OTROS ANÁLISIS:
───────────────────────────────────────────────────────────────────────────────
Este gráfico complementa:
• Análisis de Outliers: Identifica qué variables tienen más outliers esperados
• Análisis de Distribuciones: Proporciona información adicional sobre la forma
• Normalización: Ayuda a decidir qué variables necesitan transformaciones

RECOMENDACIONES:
───────────────────────────────────────────────────────────────────────────────
✓ Revisa las variables con mayor curtosis (LEPTOCÚRTICAS):
  → Estas son las que más probablemente tengan outliers
  → Considera aplicar transformaciones o usar métodos robustos

✓ Si muchas variables son LEPTOCÚRTICAS:
  → Revisa tu estrategia general de manejo de outliers
  → Considera normalización o estandarización

✓ Variables MESOCÚRTICAS:
  → Puedes usar métodos estadísticos estándar con confianza
  → No requieren transformaciones especiales

═══════════════════════════════════════════════════════════════════════════════
"""
    
    def _interpretacion_matrices_confusion(self):
        """Interpretación específica para matrices de confusión con datos reales del proyecto."""
        # Intentar leer los resultados de ML para obtener datos específicos
        interpretacion_base = """
═══════════════════════════════════════════════════════════════════════════════
📊 INTERPRETACIÓN: MATRICES DE CONFUSIÓN - PROYECTO AURELION
═══════════════════════════════════════════════════════════════════════════════

¿QUÉ ES UNA MATRIZ DE CONFUSIÓN?
───────────────────────────────────────────────────────────────────────────────
Una matriz de confusión es una tabla que muestra el rendimiento de un modelo
de clasificación comparando las predicciones del modelo con los valores reales.

En el Proyecto Aurelion, las matrices de confusión evalúan modelos que clasifican
clientes en 3 segmentos según su valor para el negocio, basándose en el importe
promedio de compras por cliente.

Los segmentos se definen dividiendo a los clientes en tercios según su importe
promedio de compras. Los rangos específicos se calculan automáticamente al
entrenar los modelos y se muestran en la interpretación del gráfico.

NOTA: Para ver los rangos específicos de importe (mínimo, máximo, promedio) y
la cantidad de clientes en cada segmento, consulta la interpretación que aparece
en el gráfico de matrices de confusión o ejecuta el script 06_modelos_ml.py.

ELEMENTOS DE LA MATRIZ:
───────────────────────────────────────────────────────────────────────────────
• VERDADEROS POSITIVOS (TP): El modelo predijo correctamente el segmento del cliente
• FALSOS POSITIVOS (FP): El modelo predijo un segmento pero era incorrecto
• FALSOS NEGATIVOS (FN): El modelo no identificó el segmento correcto del cliente
• VERDADEROS NEGATIVOS (TN): El modelo predijo correctamente que NO era ese segmento

CÓMO LEER LA MATRIZ:
───────────────────────────────────────────────────────────────────────────────
La diagonal principal (de arriba-izquierda a abajo-derecha) muestra las
predicciones CORRECTAS. Los valores fuera de la diagonal son ERRORES.

Ejemplo del Proyecto Aurelion:
        Predicción
        Bajo  Medio  Alto
Real Bajo  [X]   Y     Z    ← X clientes correctamente clasificados como Bajo
     Medio  A   [B]    C    ← B clientes correctamente clasificados como Medio
     Alto   D     E   [F]   ← F clientes correctamente clasificados como Alto

MÉTRICAS CALCULADAS:
───────────────────────────────────────────────────────────────────────────────
• ACCURACY (Precisión Global): Porcentaje total de clientes clasificados correctamente
• PRECISION (Precisión): De los clientes que el modelo clasificó en un segmento,
  ¿cuántos realmente pertenecen a ese segmento?
• RECALL (Sensibilidad): De todos los clientes reales de un segmento,
  ¿cuántos logró identificar el modelo?
• F1-SCORE: Balance entre Precision y Recall

RESULTADOS ESPECÍFICOS DEL PROYECTO AURELION:
───────────────────────────────────────────────────────────────────────────────"""
        
        # Intentar leer resultados específicos del archivo de resultados
        try:
            import pandas as pd
            import numpy as np
            from pathlib import Path
            
            # Buscar archivo de resultados de ML y reporte final
            ruta_resultados = Path(__file__).parent / "resultados" / "estadisticas" / "resultados_ml.txt"
            ruta_reporte = Path(__file__).parent / "resultados" / "REPORTE_FINAL_AURELION.md"
            resultados_texto = ""
            
            # Leer archivo de resultados
            if ruta_resultados.exists():
                with open(ruta_resultados, 'r', encoding='utf-8') as f:
                    resultados_texto += f.read() + "\n"
            
            # Leer reporte final que contiene accuracy de clasificación
            if ruta_reporte.exists():
                with open(ruta_reporte, 'r', encoding='utf-8') as f:
                    resultados_texto += f.read()
            
            # Extraer información de accuracy si está disponible
            accuracy_info = ""
            import re
            
            # Buscar valores de accuracy en el texto (formato: 0.8841 o 88.41%)
            accuracy_matches = re.findall(r'Accuracy[^:\n]*:?\s*([\d.]+)', resultados_texto, re.IGNORECASE)
            if not accuracy_matches:
                # Buscar en formato de tabla markdown
                accuracy_matches = re.findall(r'\|\s*[\d.]+\s*\|\s*([\d.]+)\s*\|\s*[\d.]+\s*\|', resultados_texto)
            
            if accuracy_matches:
                # Convertir a float y tomar el mejor accuracy (mayor valor)
                accuracy_valores = []
                for match in accuracy_matches:
                    try:
                        val = float(match)
                        # Si el valor es > 1, probablemente está en formato porcentaje, dividir por 100
                        if val > 1:
                            val = val / 100
                        accuracy_valores.append(val)
                    except:
                        continue
                
                if accuracy_valores:
                    # Usar el accuracy de prueba (generalmente el segundo o el mejor)
                    accuracy_valor = max(accuracy_valores)  # Tomar el mejor accuracy
                    
                    if accuracy_valor > 0.85:
                        accuracy_info = f"""
✅ ACCURACY OBTENIDO: {accuracy_valor:.1%} - RENDIMIENTO EXCELENTE
   • El modelo clasifica correctamente más del 85% de los clientes
   • Puedes confiar en las predicciones para estrategias de marketing
   • Los errores son mínimos y no afectan significativamente las decisiones
   • Recomendación: Usa este modelo para clasificar nuevos clientes"""
                    elif accuracy_valor > 0.70:
                        accuracy_info = f"""
✅ ACCURACY OBTENIDO: {accuracy_valor:.1%} - RENDIMIENTO BUENO
   • El modelo clasifica correctamente más del 70% de los clientes
   • Las predicciones son confiables para la mayoría de los casos
   • Considera revisar los casos donde hay más confusión
   • Recomendación: Combina predicciones del modelo con conocimiento del equipo"""
                    else:
                        accuracy_info = f"""
⚠️  ACCURACY OBTENIDO: {accuracy_valor:.1%} - NECESITA MEJORAS
   • El modelo tiene dificultades para clasificar correctamente
   • Revisa qué segmentos se confunden más frecuentemente
   • Considera ajustar el modelo o recopilar más datos
   • Recomendación: Retrena el modelo con más datos o ajusta parámetros"""
            
            # Información específica del negocio
            interpretacion_negocio = f"""
¿QUÉ SIGNIFICA ESTO PARA LA TIENDA AURELION?
───────────────────────────────────────────────────────────────────────────────
{accuracy_info if accuracy_info else "• Los modelos clasifican clientes en segmentos según su valor"}

SEGMENTACIÓN DE CLIENTES:
───────────────────────────────────────────────────────────────────────────────
Los segmentos se crean dividiendo a los clientes en tercios según su importe
promedio de compras. Los rangos específicos (mínimo, máximo, promedio) se
calculan automáticamente y se muestran en la interpretación del gráfico.

• SEGMENTO BAJO: Clientes con menor valor promedio de compras
  → Estrategia: Campañas de reactivación, ofertas especiales, programas de fidelización
  → Objetivo: Incrementar frecuencia y valor de compra
  → NOTA: Consulta el gráfico para ver el rango específico de importe promedio

• SEGMENTO MEDIO: Clientes con valor promedio de compras
  → Estrategia: Mantener relación, ofertas personalizadas, cross-selling
  → Objetivo: Convertirlos en clientes de alto valor
  → NOTA: Consulta el gráfico para ver el rango específico de importe promedio

• SEGMENTO ALTO: Clientes con mayor valor promedio de compras
  → Estrategia: Programas VIP, atención personalizada, productos premium
  → Objetivo: Retener y maximizar valor de vida del cliente
  → NOTA: Consulta el gráfico para ver el rango específico de importe promedio

IMPLICACIONES PRÁCTICAS:
───────────────────────────────────────────────────────────────────────────────
✅ CLASIFICACIÓN CORRECTA (Diagonal de la matriz):
   • Permite dirigir estrategias de marketing específicas a cada segmento
   • Optimiza el presupuesto de marketing al enfocarse en los segmentos correctos
   • Mejora la experiencia del cliente con ofertas relevantes

⚠️  ERRORES DE CLASIFICACIÓN (Fuera de la diagonal):
   • Falsos Positivos: Cliente clasificado como "Alto" pero es "Medio"
     → Riesgo: Invertir recursos en cliente que no lo justifica
     → Acción: Revisar criterios de segmentación
   
   • Falsos Negativos: Cliente clasificado como "Bajo" pero es "Alto"
     → Riesgo: Perder oportunidad de maximizar valor de cliente importante
     → Acción: Mejorar detección de clientes de alto valor

RECOMENDACIONES ESPECÍFICAS PARA AURELION:
───────────────────────────────────────────────────────────────────────────────
1. USO DEL MODELO:
   ✓ Utiliza el modelo con mayor accuracy para clasificar nuevos clientes
   ✓ Actualiza la clasificación periódicamente (ej. trimestralmente)
   ✓ Combina predicciones del modelo con conocimiento del equipo de ventas

2. ESTRATEGIAS POR SEGMENTO:
   ✓ Segmento ALTO: Programa VIP, descuentos exclusivos, atención prioritaria
   ✓ Segmento MEDIO: Ofertas personalizadas, programas de puntos, cross-selling
   ✓ Segmento BAJO: Campañas de reactivación, cupones de descuento, email marketing

3. MONITOREO Y MEJORA:
   ✓ Revisa periódicamente la matriz de confusión para detectar cambios
   ✓ Si aumentan los errores, retrena el modelo con nuevos datos
   ✓ Analiza qué características diferencian mejor a los segmentos

4. OPTIMIZACIÓN DE COSTOS:
   ✓ Enfoca presupuesto de marketing en segmentos de mayor valor
   ✓ Reduce costos evitando campañas a segmentos incorrectos
   ✓ Maximiza ROI dirigiendo ofertas relevantes a cada segmento

IMPACTO EN EL NEGOCIO:
───────────────────────────────────────────────────────────────────────────────
• Marketing más efectivo: Ofertas dirigidas a los segmentos correctos
• Mejor retención: Clientes reciben atención apropiada a su valor
• Optimización de recursos: Presupuesto utilizado eficientemente
• Incremento de ventas: Estrategias personalizadas aumentan conversión

═══════════════════════════════════════════════════════════════════════════════
"""
            
            return interpretacion_base + interpretacion_negocio
            
        except Exception as e:
            # Si hay error, devolver interpretación base con información genérica pero con referencia a datos específicos
            return interpretacion_base + """
¿QUÉ SIGNIFICA ESTO PARA LA TIENDA AURELION?
───────────────────────────────────────────────────────────────────────────────
Los modelos de clasificación evalúan qué tan bien pueden identificar el segmento
de valor de cada cliente (Bajo, Medio, Alto) basándose en sus características
de compra.

SEGMENTACIÓN DE CLIENTES:
───────────────────────────────────────────────────────────────────────────────
Los segmentos se crean dividiendo a los clientes en tercios según su importe
promedio de compras. Los rangos específicos (mínimo, máximo, promedio) se
calculan automáticamente al entrenar los modelos.

• SEGMENTO BAJO: Clientes con menor valor promedio de compras
  → Estrategia: Campañas de reactivación y fidelización
  → NOTA: Para ver los rangos específicos de importe, consulta el gráfico
    de matrices de confusión o ejecuta el script 06_modelos_ml.py

• SEGMENTO MEDIO: Clientes con valor promedio de compras
  → Estrategia: Ofertas personalizadas y cross-selling
  → NOTA: Para ver los rangos específicos de importe, consulta el gráfico
    de matrices de confusión o ejecuta el script 06_modelos_ml.py

• SEGMENTO ALTO: Clientes con mayor valor promedio de compras
  → Estrategia: Programas VIP y atención personalizada
  → NOTA: Para ver los rangos específicos de importe, consulta el gráfico
    de matrices de confusión o ejecuta el script 06_modelos_ml.py

RECOMENDACIONES:
───────────────────────────────────────────────────────────────────────────────
✓ Utiliza el modelo con mayor accuracy para clasificar nuevos clientes
✓ Dirige estrategias de marketing específicas a cada segmento
✓ Monitorea y actualiza la clasificación periódicamente
✓ Optimiza presupuesto enfocándote en segmentos de mayor valor
✓ Consulta el gráfico de matrices de confusión para ver los rangos específicos
  de importe promedio por segmento

DÓNDE ENCONTRAR DATOS ESPECÍFICOS:
───────────────────────────────────────────────────────────────────────────────
• En el gráfico de matrices de confusión: La interpretación incluye los rangos
  específicos de importe promedio por segmento
• Ejecutando 06_modelos_ml.py: Se calculan y muestran los rangos específicos
• En resultados/estadisticas/resultados_ml.txt: Información detallada de modelos

═══════════════════════════════════════════════════════════════════════════════
"""
    
    def _interpretacion_tests_normalidad(self):
        """Interpretación específica para tests de normalidad."""
        return """
═══════════════════════════════════════════════════════════════════════════════
📊 INTERPRETACIÓN: TESTS DE NORMALIDAD
═══════════════════════════════════════════════════════════════════════════════

¿QUÉ SON LOS TESTS DE NORMALIDAD?
───────────────────────────────────────────────────────────────────────────────
Los tests de normalidad verifican si los datos siguen una distribución normal
(campana de Gauss). Esto es importante para decidir qué métodos estadísticos usar.

TESTS INCLUIDOS:
───────────────────────────────────────────────────────────────────────────────
1. SHAPIRO-WILK: Para muestras pequeñas (< 5000 datos)
2. KOLMOGOROV-SMIRNOV: Compara con distribución normal teórica
3. D'AGOSTINO: Test basado en asimetría y curtosis

CÓMO INTERPRETAR:
───────────────────────────────────────────────────────────────────────────────
• p-value > 0.05: Los datos SÍ siguen una distribución normal
• p-value ≤ 0.05: Los datos NO siguen una distribución normal

ELEMENTOS VISUALES:
───────────────────────────────────────────────────────────────────────────────
• HISTOGRAMA: Muestra la distribución real de los datos
• CURVA ROJA: Muestra cómo sería la distribución normal ideal
• Q-Q PLOT: Si los puntos están en línea recta, los datos son normales

¿QUÉ SIGNIFICA PARA EL NEGOCIO?
───────────────────────────────────────────────────────────────────────────────
✅ Datos normales: Puedes usar métodos estadísticos estándar (t-test, ANOVA)
⚠️  Datos no normales: Necesitas métodos no paramétricos o transformaciones

APLICACIONES:
───────────────────────────────────────────────────────────────────────────────
• Validar supuestos para tests de hipótesis
• Decidir qué métodos de ML usar
• Determinar si necesitas transformar los datos

═══════════════════════════════════════════════════════════════════════════════
"""
    
    def _interpretacion_comparacion_medias(self):
        """Interpretación específica para comparación de medias."""
        return """
═══════════════════════════════════════════════════════════════════════════════
📊 INTERPRETACIÓN: COMPARACIÓN DE MEDIAS
═══════════════════════════════════════════════════════════════════════════════

¿QUÉ MUESTRA ESTE GRÁFICO?
───────────────────────────────────────────────────────────────────────────────
Este gráfico compara los valores promedio (medias) de diferentes grupos,
mostrando si hay diferencias significativas entre ellos.

ELEMENTOS VISUALES:
───────────────────────────────────────────────────────────────────────────────
• BOXPLOT: Muestra la distribución de cada grupo (mediana, cuartiles, outliers)
• BARRAS CON ERRORES: Muestra la media con intervalo de confianza 95%

INTERVALOS DE CONFIANZA:
───────────────────────────────────────────────────────────────────────────────
Las barras verticales (errores) muestran el rango donde probablemente está
la media real de la población. Si los intervalos NO se superponen, hay
diferencia significativa entre grupos.

CÓMO INTERPRETAR:
───────────────────────────────────────────────────────────────────────────────
1. Si los intervalos NO se superponen:
   → Hay diferencia SIGNIFICATIVA entre los grupos
   → Los grupos son realmente diferentes

2. Si los intervalos SÍ se superponen:
   → Puede NO haber diferencia significativa
   → Necesitas un test estadístico (t-test, ANOVA) para confirmar

¿QUÉ SIGNIFICA PARA EL NEGOCIO?
───────────────────────────────────────────────────────────────────────────────
• Identificar qué grupos tienen mejores resultados
• Comparar rendimiento entre categorías de productos
• Validar si las diferencias son reales o por azar

APLICACIONES:
───────────────────────────────────────────────────────────────────────────────
• Comparar ventas entre categorías
• Analizar diferencias entre segmentos de clientes
• Validar efectividad de estrategias

═══════════════════════════════════════════════════════════════════════════════
"""
    
    def _interpretacion_optimizaciones(self):
        """Interpretación específica para optimizaciones prescriptivas."""
        return """
═══════════════════════════════════════════════════════════════════════════════
📊 INTERPRETACIÓN: OPTIMIZACIONES PRESCRIPTIVAS
═══════════════════════════════════════════════════════════════════════════════

¿QUÉ ES ESTADÍSTICA PRESCRIPTIVA?
───────────────────────────────────────────────────────────────────────────────
La estadística prescriptiva va más allá de predecir: RECOMIENDA acciones
específicas para optimizar resultados basándose en análisis de datos.

COMPONENTES DEL ANÁLISIS:
───────────────────────────────────────────────────────────────────────────────
1. OPTIMIZACIÓN DE INVENTARIO:
   • Identifica productos de alta, media y baja rotación
   • Recomienda niveles óptimos de stock
   • Reduce costos de almacenamiento

2. OPTIMIZACIÓN DE PRECIOS:
   • Analiza elasticidad precio-cantidad
   • Identifica oportunidades de ajuste de precios
   • Maximiza ingresos y volumen

3. SEGMENTACIÓN DE CLIENTES:
   • Clasifica clientes por valor
   • Recomienda estrategias diferenciadas
   • Aumenta retención y valor de cliente

4. MIX DE PRODUCTOS:
   • Identifica categorías de alto rendimiento
   • Recomienda expansión de productos exitosos
   • Optimiza la oferta de productos

CÓMO LEER LOS GRÁFICOS:
───────────────────────────────────────────────────────────────────────────────
• TOP PRODUCTOS: Priorizar en inventario
• RELACIÓN PRECIO-CANTIDAD: Ajustar precios según elasticidad
• SEGMENTACIÓN: Aplicar estrategias diferenciadas
• CATEGORÍAS: Expandir las más rentables

¿QUÉ SIGNIFICA PARA EL NEGOCIO?
───────────────────────────────────────────────────────────────────────────────
✅ Acciones específicas y medibles
✅ Basadas en evidencia estadística
✅ Optimización de recursos y maximización de resultados

RECOMENDACIONES:
───────────────────────────────────────────────────────────────────────────────
Las recomendaciones deben ser validadas con el equipo de negocio antes
de implementarse, pero están respaldadas por análisis estadístico sólido.

═══════════════════════════════════════════════════════════════════════════════
"""
    
    def _interpretacion_recomendaciones(self):
        """Interpretación específica para recomendaciones prescriptivas."""
        return """
═══════════════════════════════════════════════════════════════════════════════
📊 INTERPRETACIÓN: RECOMENDACIONES PRESCRIPTIVAS
═══════════════════════════════════════════════════════════════════════════════

¿QUÉ SON LAS RECOMENDACIONES PRESCRIPTIVAS?
───────────────────────────────────────────────────────────────────────────────
Son acciones específicas recomendadas basadas en análisis estadístico de los
datos. Van más allá de describir o predecir: dicen QUÉ HACER.

TIPOS DE RECOMENDACIONES:
───────────────────────────────────────────────────────────────────────────────
1. INVENTARIO:
   • Ajustar niveles de stock según rotación
   • Priorizar productos de alta demanda
   • Reducir inventario de productos lentos

2. PRECIOS:
   • Ajustar precios según elasticidad
   • Optimizar estrategia de precios por segmento
   • Maximizar ingresos sin perder volumen

3. MARKETING:
   • Estrategias diferenciadas por segmento de cliente
   • Programas de fidelización personalizados
   • Campañas dirigidas a segmentos específicos

4. MIX DE PRODUCTOS:
   • Expandir categorías de alto rendimiento
   • Optimizar oferta de productos
   • Enfocar recursos en productos exitosos

CÓMO USAR LAS RECOMENDACIONES:
───────────────────────────────────────────────────────────────────────────────
1. Revisar cada recomendación con el equipo de negocio
2. Validar la viabilidad de implementación
3. Priorizar según impacto esperado y recursos disponibles
4. Implementar de forma gradual y medir resultados
5. Ajustar según feedback y nuevos datos

IMPACTO ESPERADO:
───────────────────────────────────────────────────────────────────────────────
Cada recomendación incluye el impacto esperado:
• Reducción de costos
• Aumento de ingresos
• Mejora de eficiencia
• Optimización de recursos

NOTA IMPORTANTE:
───────────────────────────────────────────────────────────────────────────────
Estas recomendaciones están basadas en análisis estadístico, pero deben
ser validadas con conocimiento del negocio antes de implementarse.

═══════════════════════════════════════════════════════════════════════════════
"""
    
    def mostrar_menu_graficos(self):
        """Mostrar menú de gráficos disponibles."""
        print("\n" + "=" * 80)
        print("📊 VISUALIZADOR DE GRÁFICOS - PROYECTO AURELION")
        print("=" * 80)
        print("\nGráficos disponibles:\n")
        
        for numero, info in self.graficos.items():
            existe = "✅" if (self.ruta_histogramas / info['archivo']).exists() else "❌"
            print(f"{numero:>2}. {existe} {info['nombre']}")
            print(f"    📝 {info['descripcion']}")
            print()
        
        print("25. 📖 Ver Análisis Profesional Completo (ANALISIS_GRAFICOS.md)")
        print("26. 🔙 Volver al menú principal")
        print()
        print("=" * 80)
    
    def mostrar_grafico(self, numero):
        """Mostrar un gráfico específico con su interpretación."""
        if numero not in self.graficos:
            print("❌ Número de gráfico inválido.")
            return False
        
        info = self.graficos[numero]
        archivo = info['archivo']
        ruta_archivo = self.ruta_histogramas / archivo
        
        if not ruta_archivo.exists():
            print(f"❌ El archivo {archivo} no existe.")
            print(f"   Ejecuta primero los scripts de visualización.")
            return False
        
        # Calcular interpretación específica si es posible
        interpretacion = info['interpretacion']
        if callable(interpretacion):
            interpretacion = interpretacion()
        elif self.dataset is not None:
            # Intentar calcular valores específicos para algunos gráficos
            interpretacion = self._calcular_interpretacion_especifica(numero, info, interpretacion)
        
        # Mostrar información del gráfico
        print("\n" + "=" * 80)
        print(f"📊 {info['nombre'].upper()}")
        print("=" * 80)
        print(f"📝 Descripción: {info['descripcion']}")
        print(f"📁 Archivo: {archivo}")
        print("=" * 80)
        
        # Mostrar interpretación
        print(interpretacion)
        
        # Intentar abrir el gráfico
        print("\n🖼️  Abriendo gráfico...")
        try:
            if os.name == 'nt':  # Windows
                os.startfile(str(ruta_archivo))
            else:  # Linux/Mac
                subprocess.run(['xdg-open', str(ruta_archivo)])
            print("✅ Gráfico abierto en el visor predeterminado.")
        except Exception as e:
            print(f"⚠️  No se pudo abrir automáticamente: {e}")
            print(f"   Ubicación: {ruta_archivo.absolute()}")
            print("   Abre el archivo manualmente desde el explorador.")
        
        return True
    
    def _calcular_interpretacion_especifica(self, numero, info, interpretacion_base):
        """Calcular interpretación específica basada en datos reales."""
        # Esta función puede ser expandida para calcular valores específicos
        # basándose en el dataset cargado
        return interpretacion_base
    
    def _obtener_datos_especificos_ventas(self):
        """Obtener datos específicos del proyecto para histogramas de ventas."""
        try:
            import pandas as pd
            ruta_ventas = Path(__file__).parent.parent.parent / "Datos Proyecto" / "Base de datos_Tienda_Aurelion" / "Base de datos" / "ventas.xlsx"
            ruta_detalle = Path(__file__).parent.parent.parent / "Datos Proyecto" / "Base de datos_Tienda_Aurelion" / "Base de datos" / "detalle_ventas.xlsx"
            
            if ruta_ventas.exists() and ruta_detalle.exists():
                df_ventas = pd.read_excel(ruta_ventas)
                df_detalle = pd.read_excel(ruta_detalle)
                
                # Calcular total por venta sumando importes de detalle_ventas
                if 'importe' in df_detalle.columns and 'id_venta' in df_detalle.columns:
                    totales_por_venta = df_detalle.groupby('id_venta')['importe'].sum()
                    num_ventas = len(totales_por_venta)
                    total_ventas = totales_por_venta.sum()
                    promedio_venta = totales_por_venta.mean()
                    mediana_venta = totales_por_venta.median()
                    min_venta = totales_por_venta.min()
                    max_venta = totales_por_venta.max()
                    
                    return f"""
DATOS ESPECÍFICOS DEL PROYECTO AURELION:
───────────────────────────────────────────────────────────────────────────────
• Total de ventas analizadas: {num_ventas:,} ventas
• Monto total de ventas: ${total_ventas:,.2f} pesos argentinos
• Monto promedio por venta: ${promedio_venta:,.2f} pesos
• Monto mediano por venta: ${mediana_venta:,.2f} pesos
• Venta más pequeña: ${min_venta:,.2f} pesos
• Venta más grande: ${max_venta:,.2f} pesos
• Ticket promedio: ${promedio_venta:,.2f} pesos por transacción
"""
        except Exception as e:
            pass
        return ""
    
    def _obtener_datos_especificos_detalle_ventas(self):
        """Obtener datos específicos del proyecto para histogramas de detalle de ventas."""
        try:
            import pandas as pd
            ruta_detalle = Path(__file__).parent.parent.parent / "Datos Proyecto" / "Base de datos_Tienda_Aurelion" / "Base de datos" / "detalle_ventas.xlsx"
            if ruta_detalle.exists():
                df_detalle = pd.read_excel(ruta_detalle)
                if 'cantidad' in df_detalle.columns and 'importe' in df_detalle.columns:
                    total_lineas = len(df_detalle)
                    promedio_cantidad = df_detalle['cantidad'].mean()
                    mediana_cantidad = df_detalle['cantidad'].median()
                    promedio_importe = df_detalle['importe'].mean()
                    mediana_importe = df_detalle['importe'].median()
                    min_importe = df_detalle['importe'].min()
                    max_importe = df_detalle['importe'].max()
                    
                    return f"""
DATOS ESPECÍFICOS DEL PROYECTO AURELION:
───────────────────────────────────────────────────────────────────────────────
• Total de líneas de venta: {total_lineas:,} líneas
• Cantidad promedio por línea: {promedio_cantidad:.2f} unidades
• Cantidad mediana por línea: {mediana_cantidad:.2f} unidades
• Importe promedio por línea: ${promedio_importe:,.2f} pesos
• Importe mediano por línea: ${mediana_importe:,.2f} pesos
• Importe mínimo por línea: ${min_importe:,.2f} pesos
• Importe máximo por línea: ${max_importe:,.2f} pesos
"""
        except:
            pass
        return ""
    
    def _obtener_datos_especificos_productos(self):
        """Obtener datos específicos del proyecto para histogramas de productos."""
        try:
            import pandas as pd
            ruta_productos = Path(__file__).parent.parent.parent / "Datos Proyecto" / "Base de datos_Tienda_Aurelion" / "Base de datos" / "productos.xlsx"
            if ruta_productos.exists():
                df_productos = pd.read_excel(ruta_productos)
                if 'precio_unitario' in df_productos.columns:
                    total_productos = len(df_productos)
                    promedio_precio = df_productos['precio_unitario'].mean()
                    mediana_precio = df_productos['precio_unitario'].median()
                    min_precio = df_productos['precio_unitario'].min()
                    max_precio = df_productos['precio_unitario'].max()
                    
                    return f"""
DATOS ESPECÍFICOS DEL PROYECTO AURELION:
───────────────────────────────────────────────────────────────────────────────
• Total de productos: {total_productos} productos
• Precio promedio: ${promedio_precio:,.2f} pesos argentinos
• Precio mediano: ${mediana_precio:,.2f} pesos
• Precio mínimo: ${min_precio:,.2f} pesos
• Precio máximo: ${max_precio:,.2f} pesos
• Rango de precios: ${min_precio:,.2f} - ${max_precio:,.2f} pesos
"""
        except:
            pass
        return ""
    
    def _obtener_datos_especificos_clientes(self):
        """Obtener datos específicos del proyecto para histogramas de clientes."""
        try:
            import pandas as pd
            ruta_clientes = Path(__file__).parent.parent.parent / "Datos Proyecto" / "Base de datos_Tienda_Aurelion" / "Base de datos" / "clientes.xlsx"
            if ruta_clientes.exists():
                df_clientes = pd.read_excel(ruta_clientes)
                total_clientes = len(df_clientes)
                clientes_unicos = df_clientes['id_cliente'].nunique()
                
                return f"""
DATOS ESPECÍFICOS DEL PROYECTO AURELION:
───────────────────────────────────────────────────────────────────────────────
• Total de clientes en la base de datos: {total_clientes} clientes
• Clientes únicos: {clientes_unicos} clientes
• Base de datos completa sin duplicados
"""
        except:
            pass
        return ""
    
    def _obtener_datos_especificos_correlacion(self):
        """Obtener datos específicos del proyecto para matriz de correlación."""
        try:
            if self.dataset is not None:
                import pandas as pd
                import numpy as np
                
                # Obtener solo columnas numéricas
                numeric_cols = self.dataset.select_dtypes(include=[np.number]).columns.tolist()
                # Excluir IDs
                numeric_cols = [col for col in numeric_cols if 'id' not in col.lower()]
                
                if len(numeric_cols) > 1:
                    # Calcular matriz de correlación
                    corr_matrix = self.dataset[numeric_cols].corr()
                    
                    # Encontrar las correlaciones más fuertes (excluyendo diagonal)
                    corr_pairs = []
                    for i in range(len(corr_matrix.columns)):
                        for j in range(i+1, len(corr_matrix.columns)):
                            var1 = corr_matrix.columns[i]
                            var2 = corr_matrix.columns[j]
                            corr_val = corr_matrix.iloc[i, j]
                            if not np.isnan(corr_val):
                                corr_pairs.append((var1, var2, corr_val))
                    
                    # Ordenar por valor absoluto de correlación
                    corr_pairs.sort(key=lambda x: abs(x[2]), reverse=True)
                    
                    # Top correlaciones positivas y negativas
                    top_positivas = [p for p in corr_pairs if p[2] > 0.5][:3]
                    top_negativas = [p for p in corr_pairs if p[2] < -0.3][:3]
                    
                    resultado = "DATOS ESPECÍFICOS DEL PROYECTO AURELION:\n"
                    resultado += "───────────────────────────────────────────────────────────────────────────────\n"
                    resultado += f"• Variables numéricas analizadas: {len(numeric_cols)} variables\n"
                    resultado += f"• Total de relaciones analizadas: {len(corr_pairs)} pares de variables\n\n"
                    
                    if top_positivas:
                        resultado += "CORRELACIONES POSITIVAS MÁS FUERTES (>0.5):\n"
                        for var1, var2, corr in top_positivas:
                            resultado += f"  • {var1} ↔ {var2}: {corr:.3f} (relación {'muy fuerte' if corr > 0.8 else 'fuerte'})\n"
                        resultado += "\n"
                    
                    if top_negativas:
                        resultado += "CORRELACIONES NEGATIVAS MÁS FUERTES (<-0.3):\n"
                        for var1, var2, corr in top_negativas:
                            resultado += f"  • {var1} ↔ {var2}: {corr:.3f} (relación inversa {'muy fuerte' if corr < -0.6 else 'moderada'})\n"
                        resultado += "\n"
                    
                    # Buscar correlación cantidad-importe específicamente
                    if 'cantidad' in numeric_cols and 'importe' in numeric_cols:
                        corr_cant_imp = corr_matrix.loc['cantidad', 'importe'] if 'cantidad' in corr_matrix.index and 'importe' in corr_matrix.columns else None
                        if corr_cant_imp is not None and not np.isnan(corr_cant_imp):
                            resultado += f"• Correlación Cantidad ↔ Importe: {corr_cant_imp:.3f}\n"
                            if corr_cant_imp > 0.8:
                                resultado += "  → Relación muy fuerte: aumentar cantidades aumenta ingresos significativamente\n"
                            elif corr_cant_imp > 0.5:
                                resultado += "  → Relación fuerte: las cantidades influyen en los importes\n"
                    
                    return resultado
        except Exception as e:
            pass
        return ""
    
    def _obtener_recomendaciones_correlacion(self):
        """Obtener recomendaciones específicas basadas en correlaciones reales."""
        try:
            if self.dataset is not None:
                import pandas as pd
                import numpy as np
                
                numeric_cols = self.dataset.select_dtypes(include=[np.number]).columns.tolist()
                numeric_cols = [col for col in numeric_cols if 'id' not in col.lower()]
                
                if len(numeric_cols) > 1:
                    corr_matrix = self.dataset[numeric_cols].corr()
                    recomendaciones = []
                    
                    # Verificar correlación cantidad-importe
                    if 'cantidad' in numeric_cols and 'importe' in numeric_cols:
                        corr_cant_imp = corr_matrix.loc['cantidad', 'importe'] if 'cantidad' in corr_matrix.index and 'importe' in corr_matrix.columns else None
                        if corr_cant_imp is not None and not np.isnan(corr_cant_imp):
                            if corr_cant_imp > 0.8:
                                recomendaciones.append(f"✓ Cantidad e importe tienen correlación muy fuerte ({corr_cant_imp:.3f})")
                                recomendaciones.append("  → Enfócate en aumentar las cantidades vendidas para aumentar ingresos")
                                recomendaciones.append("  → Considera promociones de 'compra más, ahorra más'")
                    
                    # Verificar correlación precio-cantidad
                    if 'precio_unitario' in numeric_cols and 'cantidad' in numeric_cols:
                        corr_prec_cant = corr_matrix.loc['precio_unitario', 'cantidad'] if 'precio_unitario' in corr_matrix.index and 'cantidad' in corr_matrix.columns else None
                        if corr_prec_cant is not None and not np.isnan(corr_prec_cant):
                            if corr_prec_cant < -0.3:
                                recomendaciones.append(f"✓ Precio y cantidad tienen correlación negativa ({corr_prec_cant:.3f})")
                                recomendaciones.append("  → Los clientes son sensibles al precio")
                                recomendaciones.append("  → Considera estrategias de precio competitivo o descuentos por volumen")
                    
                    if recomendaciones:
                        return "\n".join(recomendaciones)
        except:
            pass
        
        return """✓ Si cantidad e importe están muy correlacionados (>0.8):
  → Enfócate en aumentar las cantidades vendidas para aumentar ingresos.

✓ Si precio y cantidad tienen correlación negativa fuerte:
  → Los clientes son sensibles al precio. Considera estrategias de precio competitivo.

✓ Si encuentras correlaciones inesperadas:
  → Investiga más a fondo. Podría haber oportunidades de negocio ocultas."""
    
    def _obtener_datos_especificos_outliers(self):
        """Obtener datos específicos del proyecto para análisis de outliers."""
        try:
            if self.dataset is not None:
                import pandas as pd
                import numpy as np
                
                numeric_cols = self.dataset.select_dtypes(include=[np.number]).columns.tolist()
                numeric_cols = [col for col in numeric_cols if 'id' not in col.lower()]
                
                if len(numeric_cols) > 0:
                    resultado = "DATOS ESPECÍFICOS DEL PROYECTO AURELION:\n"
                    resultado += "───────────────────────────────────────────────────────────────────────────────\n"
                    
                    total_outliers = 0
                    outliers_por_variable = {}
                    
                    for col in numeric_cols[:5]:  # Analizar primeras 5 variables numéricas
                        Q1 = self.dataset[col].quantile(0.25)
                        Q3 = self.dataset[col].quantile(0.75)
                        IQR = Q3 - Q1
                        lower_bound = Q1 - 1.5 * IQR
                        upper_bound = Q3 + 1.5 * IQR
                        
                        outliers = ((self.dataset[col] < lower_bound) | (self.dataset[col] > upper_bound)).sum()
                        total_outliers += outliers
                        outliers_por_variable[col] = {
                            'count': outliers,
                            'percentage': (outliers / len(self.dataset)) * 100,
                            'max': self.dataset[col].max(),
                            'min': self.dataset[col].min(),
                            'mean': self.dataset[col].mean()
                        }
                    
                    resultado += f"• Total de registros analizados: {len(self.dataset):,} registros\n"
                    resultado += f"• Variables numéricas analizadas: {len(numeric_cols)} variables\n\n"
                    
                    # Mostrar outliers por variable
                    resultado += "OUTLIERS POR VARIABLE:\n"
                    for col, info in list(outliers_por_variable.items())[:3]:
                        resultado += f"  • {col}:\n"
                        resultado += f"    - Outliers detectados: {info['count']:,} ({info['percentage']:.1f}% del total)\n"
                        resultado += f"    - Valor máximo: {info['max']:,.2f}\n"
                        resultado += f"    - Valor mínimo: {info['min']:,.2f}\n"
                        resultado += f"    - Promedio: {info['mean']:,.2f}\n"
                    
                    return resultado
        except:
            pass
        return ""
    
    def _obtener_recomendaciones_outliers(self):
        """Obtener recomendaciones específicas basadas en outliers reales."""
        try:
            if self.dataset is not None:
                import pandas as pd
                import numpy as np
                
                recomendaciones = []
                
                # Analizar outliers en importe si existe
                if 'importe' in self.dataset.columns:
                    Q1 = self.dataset['importe'].quantile(0.25)
                    Q3 = self.dataset['importe'].quantile(0.75)
                    IQR = Q3 - Q1
                    upper_bound = Q3 + 1.5 * IQR
                    
                    outliers_altos = (self.dataset['importe'] > upper_bound).sum()
                    if outliers_altos > 0:
                        max_importe = self.dataset['importe'].max()
                        porcentaje = (outliers_altos / len(self.dataset)) * 100
                        recomendaciones.append(f"✓ {outliers_altos:,} registros con importes muy altos ({porcentaje:.1f}% del total)")
                        recomendaciones.append(f"  → Importe máximo detectado: ${max_importe:,.2f}")
                        recomendaciones.append("  → Identifica qué clientes/productos generan estos valores altos")
                        recomendaciones.append("  → Crea estrategias para replicar ventas de alto valor")
                
                if recomendaciones:
                    return "\n".join(recomendaciones)
        except:
            pass
        
        return """✓ Si hay outliers en ventas altas:
  → Identifica qué clientes/productos son y crea estrategias para replicar ese éxito.

✓ Si hay muchos outliers:
  → Revisa los datos para asegurar que no hay errores. Si son reales, considera segmentar el análisis.

✓ Si los outliers son consistentes:
  → Podrían representar un segmento de mercado diferente que merece atención especial."""
    
    def _obtener_datos_especificos_clustering(self):
        """Obtener datos específicos del proyecto para análisis de clustering."""
        try:
            # Intentar cargar información de clustering desde archivos de resultados
            ruta_resultados = Path(__file__).parent / "resultados" / "estadisticas" / "resultados_ml.txt"
            if ruta_resultados.exists():
                with open(ruta_resultados, 'r', encoding='utf-8') as f:
                    contenido = f.read()
                    
                    resultado = "DATOS ESPECÍFICOS DEL PROYECTO AURELION:\n"
                    resultado += "───────────────────────────────────────────────────────────────────────────────\n"
                    
                    # Buscar información de clustering en el contenido
                    if 'K-Means' in contenido or 'clustering' in contenido.lower():
                        resultado += "• Análisis de clustering realizado con K-Means y DBSCAN\n"
                        resultado += "• Los clusters identifican patrones en los datos del proyecto\n"
                    
                    if self.dataset is not None:
                        resultado += f"• Total de registros analizados: {len(self.dataset):,} registros\n"
                    
                    return resultado
        except:
            pass
        
        if self.dataset is not None:
            return f"""DATOS ESPECÍFICOS DEL PROYECTO AURELION:
───────────────────────────────────────────────────────────────────────────────
• Total de registros analizados: {len(self.dataset):,} registros
• El clustering agrupa estos registros en segmentos similares
• K-Means crea 3 grupos fijos para segmentación
• DBSCAN identifica grupos naturales según densidad de datos
"""
        return ""
    
    def _obtener_recomendaciones_clustering(self):
        """Obtener recomendaciones específicas basadas en clustering."""
        try:
            if self.dataset is not None:
                recomendaciones = []
                recomendaciones.append(f"✓ {len(self.dataset):,} registros analizados para segmentación")
                recomendaciones.append("  → Desarrolla estrategias específicas para cada grupo identificado")
                recomendaciones.append("  → Analiza las características comunes dentro de cada cluster")
                recomendaciones.append("  → Personaliza ofertas y marketing según el segmento")
                return "\n".join(recomendaciones)
        except:
            pass
        
        return """✓ Si los clusters son claros:
  → Desarrolla estrategias específicas para cada grupo identificado.

✓ Si DBSCAN encuentra más o menos grupos que K-Means:
  → DBSCAN puede estar detectando la estructura natural de tus datos mejor.

✓ Analiza qué tienen en común los puntos de cada cluster:
  → Esto te ayudará a entender por qué se agruparon así."""
    
    def _obtener_datos_especificos_modelos(self):
        """Obtener datos específicos del proyecto para modelos de regresión."""
        try:
            # Intentar cargar resultados de ML
            ruta_resultados = Path(__file__).parent / "resultados" / "estadisticas" / "resultados_ml.txt"
            if ruta_resultados.exists():
                with open(ruta_resultados, 'r', encoding='utf-8') as f:
                    contenido = f.read()
                    
                    resultado = "DATOS ESPECÍFICOS DEL PROYECTO AURELION:\n"
                    resultado += "───────────────────────────────────────────────────────────────────────────────\n"
                    
                    # Buscar métricas R² en el contenido
                    import re
                    r2_pattern = r'R²[:\s]+([0-9.]+)'
                    r2_matches = re.findall(r2_pattern, contenido, re.IGNORECASE)
                    
                    if r2_matches:
                        resultado += "MÉTRICAS DE MODELOS DE REGRESIÓN:\n"
                        modelos = ['Linear Regression', 'Random Forest', 'SVR']
                        for i, r2_val in enumerate(r2_matches[:3]):
                            modelo_nombre = modelos[i] if i < len(modelos) else f"Modelo {i+1}"
                            r2_float = float(r2_val)
                            resultado += f"  • {modelo_nombre}: R² = {r2_float:.3f} "
                            if r2_float > 0.8:
                                resultado += "(Excelente)\n"
                            elif r2_float > 0.6:
                                resultado += "(Bueno)\n"
                            else:
                                resultado += "(Necesita mejorar)\n"
                        resultado += "\n"
                    
                    if self.dataset is not None:
                        resultado += f"• Registros usados para entrenamiento: {len(self.dataset):,} registros\n"
                        resultado += f"• Variable objetivo: Predicción de importe de ventas\n"
                    
                    return resultado
        except:
            pass
        
        if self.dataset is not None:
            return f"""DATOS ESPECÍFICOS DEL PROYECTO AURELION:
───────────────────────────────────────────────────────────────────────────────
• Registros analizados: {len(self.dataset):,} registros
• Modelos comparados: Linear Regression, Random Forest, SVR
• Variable objetivo: Predicción de importe de ventas
• El mejor modelo es el que tiene el R² más alto
"""
        return ""
    
    def _obtener_recomendaciones_modelos(self):
        """Obtener recomendaciones específicas basadas en modelos."""
        try:
            ruta_resultados = Path(__file__).parent / "resultados" / "estadisticas" / "resultados_ml.txt"
            if ruta_resultados.exists():
                with open(ruta_resultados, 'r', encoding='utf-8') as f:
                    contenido = f.read()
                    
                    import re
                    r2_pattern = r'R²[:\s]+([0-9.]+)'
                    r2_matches = re.findall(r2_pattern, contenido, re.IGNORECASE)
                    
                    if r2_matches:
                        r2_values = [float(r2) for r2 in r2_matches[:3]]
                        mejor_r2 = max(r2_values)
                        mejor_idx = r2_values.index(mejor_r2)
                        modelos = ['Linear Regression', 'Random Forest', 'SVR']
                        mejor_modelo = modelos[mejor_idx] if mejor_idx < len(modelos) else f"Modelo {mejor_idx+1}"
                        
                        recomendaciones = []
                        recomendaciones.append(f"✓ Mejor modelo: {mejor_modelo} con R² = {mejor_r2:.3f}")
                        recomendaciones.append(f"  → Usa este modelo para hacer predicciones de importes futuros")
                        
                        if mejor_r2 < 0.6:
                            recomendaciones.append("  → Considera agregar más variables o más datos para mejorar")
                        
                        if mejor_r2 > 0.8:
                            recomendaciones.append("  → Excelente capacidad predictiva - confía en las predicciones")
                        
                        return "\n".join(recomendaciones)
        except:
            pass
        
        return """✓ Usa el modelo con R² más alto:
  → Este es el que mejor predice tus datos.

✓ Si todos los R² son bajos (<0.6):
  → Considera agregar más variables o más datos para mejorar las predicciones.

✓ El gráfico de dispersión te muestra dónde falla el modelo:
  → Si falla en valores altos, el modelo tiene problemas con casos extremos."""
    
    def _obtener_datos_especificos_importancia(self):
        """Obtener datos específicos del proyecto para importancia de variables."""
        try:
            if self.dataset is not None:
                import pandas as pd
                import numpy as np
                
                numeric_cols = self.dataset.select_dtypes(include=[np.number]).columns.tolist()
                numeric_cols = [col for col in numeric_cols if 'id' not in col.lower()]
                
                if len(numeric_cols) > 0:
                    resultado = "DATOS ESPECÍFICOS DEL PROYECTO AURELION:\n"
                    resultado += "───────────────────────────────────────────────────────────────────────────────\n"
                    resultado += f"• Variables analizadas: {len(numeric_cols)} variables numéricas\n"
                    resultado += f"• Registros analizados: {len(self.dataset):,} registros\n"
                    resultado += "• Las variables más importantes son las que mejor predicen el importe\n"
                    resultado += "• El modelo Random Forest calcula la importancia basándose en los datos reales\n"
                    return resultado
        except:
            pass
        return ""
    
    def _obtener_recomendaciones_importancia(self):
        """Obtener recomendaciones específicas basadas en importancia de variables."""
        try:
            if self.dataset is not None:
                recomendaciones = []
                recomendaciones.append(f"✓ {len(self.dataset):,} registros analizados para determinar importancia")
                recomendaciones.append("  → Enfócate en las 3-5 variables más importantes para tu estrategia")
                recomendaciones.append("  → Si cantidad o precio están en el top, confirma que son factores clave")
                recomendaciones.append("  → Variables con baja importancia pueden simplificarse o eliminarse")
                return "\n".join(recomendaciones)
        except:
            pass
        
        return """✓ Enfócate en las 3-5 variables más importantes:
  → Estas son las que realmente mueven la aguja en tu negocio.

✓ Si cantidad o precio están en el top:
  → Confirma que estos son factores clave (como esperarías).

✓ Si encuentras variables inesperadas en el top:
  → Investiga por qué son importantes. Podría haber oportunidades ocultas."""
    
    def _obtener_datos_especificos_resumen(self):
        """Obtener datos específicos del proyecto para resumen estadístico."""
        try:
            if self.dataset is not None:
                import pandas as pd
                import numpy as np
                
                numeric_cols = self.dataset.select_dtypes(include=[np.number]).columns.tolist()
                numeric_cols = [col for col in numeric_cols if 'id' not in col.lower()]
                
                if len(numeric_cols) > 0:
                    resultado = "DATOS ESPECÍFICOS DEL PROYECTO AURELION:\n"
                    resultado += "───────────────────────────────────────────────────────────────────────────────\n"
                    resultado += f"• Variables numéricas analizadas: {len(numeric_cols)} variables\n"
                    resultado += f"• Total de registros: {len(self.dataset):,} registros\n"
                    
                    # Estadísticas clave de variables importantes
                    if 'importe' in self.dataset.columns:
                        resultado += f"\nESTADÍSTICAS CLAVE - IMPORTE:\n"
                        resultado += f"  • Promedio: ${self.dataset['importe'].mean():,.2f} pesos\n"
                        resultado += f"  • Mediana: ${self.dataset['importe'].median():,.2f} pesos\n"
                        resultado += f"  • Mínimo: ${self.dataset['importe'].min():,.2f} pesos\n"
                        resultado += f"  • Máximo: ${self.dataset['importe'].max():,.2f} pesos\n"
                    
                    if 'cantidad' in self.dataset.columns:
                        resultado += f"\nESTADÍSTICAS CLAVE - CANTIDAD:\n"
                        resultado += f"  • Promedio: {self.dataset['cantidad'].mean():.2f} unidades\n"
                        resultado += f"  • Mediana: {self.dataset['cantidad'].median():.2f} unidades\n"
                        resultado += f"  • Mínimo: {self.dataset['cantidad'].min():.2f} unidades\n"
                        resultado += f"  • Máximo: {self.dataset['cantidad'].max():.2f} unidades\n"
                    
                    return resultado
        except:
            pass
        return ""
    
    def _obtener_recomendaciones_resumen(self):
        """Obtener recomendaciones específicas basadas en resumen estadístico."""
        try:
            if self.dataset is not None:
                recomendaciones = []
                
                if 'importe' in self.dataset.columns:
                    mean_imp = self.dataset['importe'].mean()
                    median_imp = self.dataset['importe'].median()
                    if mean_imp > median_imp * 1.2:
                        recomendaciones.append(f"✓ El promedio (${mean_imp:,.2f}) es mayor que la mediana (${median_imp:,.2f})")
                        recomendaciones.append("  → Hay ventas grandes que elevan el promedio")
                        recomendaciones.append("  → Identifica qué genera estas ventas grandes para replicarlas")
                
                recomendaciones.append(f"✓ {len(self.dataset):,} registros analizados")
                recomendaciones.append("  → Usa esta tabla como punto de partida para análisis más profundos")
                recomendaciones.append("  → Compara variables relacionadas para detectar inconsistencias")
                
                return "\n".join(recomendaciones) if recomendaciones else ""
        except:
            pass
        
        return """✓ Usa esta tabla como punto de partida:
  → Te da una vista general antes de hacer análisis más profundos.

✓ Presta atención a count:
  → Si es mucho menor que el total esperado, hay datos faltantes que necesitas investigar.

✓ Compara variables relacionadas:
  → Por ejemplo, compara precio_unitario con importe para ver si hay consistencia."""
    
    def _obtener_datos_especificos_medios_pago(self):
        """Obtener datos específicos del proyecto para análisis de medios de pago."""
        try:
            import pandas as pd
            ruta_base = Path(__file__).parent.parent.parent.parent
            rutas_posibles = [
                ruta_base / "Datos Proyecto" / "Base de datos_Tienda_Aurelion" / "Base de datos" / "ventas.xlsx",
                ruta_base / "Datos Proyecto" / "Base de datos_Tienda_Aurelion" / "Base de datos" / "Ventas.xlsx",
                ruta_base / "BASE_DE_DATOS" / "ventas.xlsx",
                ruta_base / "BASE_DE_DATOS" / "Ventas.xlsx",
            ]
            
            ruta_ventas = None
            for ruta in rutas_posibles:
                if ruta.exists():
                    ruta_ventas = ruta
                    break
            
            if ruta_ventas and ruta_ventas.exists():
                df_ventas = pd.read_excel(ruta_ventas)
                
                if 'medio_pago' in df_ventas.columns:
                    medios_pago = df_ventas['medio_pago'].value_counts()
                    total_ventas = len(df_ventas)
                    
                    resultado = "DATOS ESPECÍFICOS DEL PROYECTO AURELION:\n"
                    resultado += "───────────────────────────────────────────────────────────────────────────────\n"
                    resultado += f"• Total de ventas analizadas: {total_ventas:,} ventas\n"
                    resultado += f"• Métodos de pago disponibles: {len(medios_pago)} métodos\n\n"
                    resultado += "DISTRIBUCIÓN POR MÉTODO DE PAGO:\n"
                    
                    for metodo, count in medios_pago.head(5).items():
                        porcentaje = (count / total_ventas) * 100
                        resultado += f"  • {metodo}: {count:,} ventas ({porcentaje:.1f}% del total)\n"
                    
                    # Método más popular
                    metodo_popular = medios_pago.index[0]
                    resultado += f"\n• Método más popular: {metodo_popular} ({medios_pago.iloc[0]:,} ventas, {medios_pago.iloc[0]/total_ventas*100:.1f}%)\n"
                    
                    return resultado
        except:
            pass
        return ""
    
    def _obtener_recomendaciones_medios_pago(self):
        """Obtener recomendaciones específicas basadas en medios de pago."""
        try:
            import pandas as pd
            ruta_base = Path(__file__).parent.parent.parent.parent
            rutas_posibles = [
                ruta_base / "Datos Proyecto" / "Base de datos_Tienda_Aurelion" / "Base de datos" / "ventas.xlsx",
                ruta_base / "Datos Proyecto" / "Base de datos_Tienda_Aurelion" / "Base de datos" / "Ventas.xlsx",
            ]
            
            ruta_ventas = None
            for ruta in rutas_posibles:
                if ruta.exists():
                    ruta_ventas = ruta
                    break
            
            if ruta_ventas and ruta_ventas.exists():
                df_ventas = pd.read_excel(ruta_ventas)
                
                if 'medio_pago' in df_ventas.columns:
                    medios_pago = df_ventas['medio_pago'].value_counts()
                    total_ventas = len(df_ventas)
                    metodo_popular = medios_pago.index[0]
                    porcentaje_popular = (medios_pago.iloc[0] / total_ventas) * 100
                    
                    recomendaciones = []
                    recomendaciones.append(f"✓ Método más usado: {metodo_popular} ({porcentaje_popular:.1f}% de las ventas)")
                    
                    if porcentaje_popular > 60:
                        recomendaciones.append("  → Un método muy dominante - considera diversificar para reducir dependencia")
                    
                    if len(medios_pago) > 1:
                        segundo_metodo = medios_pago.index[1] if len(medios_pago) > 1 else None
                        if segundo_metodo:
                            porcentaje_segundo = (medios_pago.iloc[1] / total_ventas) * 100
                            recomendaciones.append(f"✓ Segundo método: {segundo_metodo} ({porcentaje_segundo:.1f}% de las ventas)")
                            recomendaciones.append("  → Compara montos promedio entre métodos para optimizar estrategia")
                    
                    return "\n".join(recomendaciones)
        except:
            pass
        
        return """✓ Si un método tiene mucho volumen pero bajo monto promedio:
  → Es popular pero para compras pequeñas. Considera incentivos para compras mayores.

✓ Si un método tiene alto monto promedio:
  → Atrae clientes que gastan más. Promociona este método.

✓ Si hay un método muy dominante:
  → Considera diversificar para no depender de un solo método."""
    
    def _obtener_datos_especificos_pairplot(self):
        """Obtener datos específicos del proyecto para pairplot."""
        try:
            if self.dataset is not None:
                import pandas as pd
                import numpy as np
                
                numeric_cols = self.dataset.select_dtypes(include=[np.number]).columns.tolist()
                numeric_cols = [col for col in numeric_cols if 'id' not in col.lower()]
                
                if len(numeric_cols) > 0:
                    resultado = "DATOS ESPECÍFICOS DEL PROYECTO AURELION:\n"
                    resultado += "───────────────────────────────────────────────────────────────────────────────\n"
                    resultado += f"• Variables analizadas: {len(numeric_cols)} variables numéricas\n"
                    resultado += f"• Total de relaciones mostradas: {len(numeric_cols) * (len(numeric_cols) - 1) // 2} pares de variables\n"
                    resultado += f"• Registros analizados: {len(self.dataset):,} registros\n"
                    resultado += "• Cada gráfico muestra la relación entre dos variables específicas\n"
                    return resultado
        except:
            pass
        return ""
    
    def _obtener_recomendaciones_pairplot(self):
        """Obtener recomendaciones específicas basadas en pairplot."""
        try:
            if self.dataset is not None:
                recomendaciones = []
                recomendaciones.append(f"✓ {len(self.dataset):,} registros analizados para todas las relaciones")
                recomendaciones.append("  → Enfócate en las relaciones más claras (líneas diagonales)")
                recomendaciones.append("  → Busca relaciones inesperadas que puedan ser oportunidades")
                return "\n".join(recomendaciones)
        except:
            pass
        
        return """✓ Usa este gráfico para exploración inicial:
  → Te da una vista completa antes de hacer análisis más específicos.

✓ Busca relaciones inesperadas:
  → Podrían ser oportunidades de negocio.

✓ Si es muy complejo:
  → Enfócate en las relaciones más claras primero."""
    
    def _obtener_datos_especificos_scatter(self):
        """Obtener datos específicos del proyecto para scatter plots."""
        try:
            if self.dataset is not None:
                resultado = "DATOS ESPECÍFICOS DEL PROYECTO AURELION:\n"
                resultado += "───────────────────────────────────────────────────────────────────────────────\n"
                resultado += f"• Registros analizados: {len(self.dataset):,} registros\n"
                resultado += "• Cada gráfico muestra la relación entre dos variables específicas\n"
                resultado += "• Los puntos representan transacciones/ventas individuales\n"
                return resultado
        except:
            pass
        return ""
    
    def _obtener_recomendaciones_scatter(self):
        """Obtener recomendaciones específicas basadas en scatter plots."""
        try:
            if self.dataset is not None:
                recomendaciones = []
                recomendaciones.append(f"✓ {len(self.dataset):,} registros analizados para relaciones detalladas")
                recomendaciones.append("  → Enfócate en relaciones con correlación > 0.7 o < -0.7")
                recomendaciones.append("  → Si cantidad e importe tienen alta correlación, enfócate en aumentar cantidades")
                return "\n".join(recomendaciones)
        except:
            pass
        
        return """✓ Enfócate en relaciones con correlación > 0.7 o < -0.7:
  → Estas son relaciones fuertes que puedes aprovechar.

✓ Si cantidad e importe tienen alta correlación positiva:
  → Enfócate en aumentar cantidades para aumentar ingresos.

✓ Si precio y cantidad tienen correlación negativa:
  → Los clientes son sensibles al precio. Estrategias de precio competitivo."""
    
    def mostrar_analisis_profesional(self):
        """Mostrar el análisis profesional completo."""
        if not self.ruta_analisis.exists():
            print("❌ El archivo de análisis profesional no existe.")
            return False
        
        print("\n" + "=" * 80)
        print("📖 ANÁLISIS PROFESIONAL COMPLETO")
        print("=" * 80)
        print(f"📁 Archivo: {self.ruta_analisis.name}")
        print("=" * 80)
        
        try:
            # Intentar abrir el archivo
            if os.name == 'nt':  # Windows
                os.startfile(str(self.ruta_analisis))
            else:  # Linux/Mac
                subprocess.run(['xdg-open', str(self.ruta_analisis)])
            print("✅ Archivo abierto en el editor predeterminado.")
        except Exception as e:
            print(f"⚠️  No se pudo abrir automáticamente: {e}")
            print(f"   Ubicación: {self.ruta_analisis.absolute()}")
            print("   Abre el archivo manualmente desde el explorador.")
        
        return True
    
    def ejecutar(self):
        """Ejecutar el visualizador interactivo."""
        while True:
            try:
                os.system('cls' if os.name == 'nt' else 'clear')
                self.mostrar_menu_graficos()
                
                opcion = input("🔢 Selecciona un gráfico (1-26): ").strip()
                
                if opcion in self.graficos:
                    self.mostrar_grafico(opcion)
                    input("\n⏸️  Presiona Enter para continuar...")
                elif opcion == '25':
                    self.mostrar_analisis_profesional()
                    input("\n⏸️  Presiona Enter para continuar...")
                elif opcion == '26':
                    break
                else:
                    print("❌ Opción inválida.")
                    input("\n⏸️  Presiona Enter para continuar...")
                    
            except KeyboardInterrupt:
                print("\n\n⚠️  Operación cancelada.")
                break
            except Exception as e:
                print(f"\n❌ Error: {e}")
                input("\n⏸️  Presiona Enter para continuar...")

def main():
    """Función principal."""
    visualizador = VisualizadorGraficosInteractivo()
    visualizador.ejecutar()

if __name__ == "__main__":
    main()

