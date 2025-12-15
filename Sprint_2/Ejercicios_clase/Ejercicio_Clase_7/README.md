<!--
# README.md
===========
Ejercicio Clase 7 - Análisis de Ventas - Sprint_2

Autor: Enith Gicela Vargas Vargas
Grupo: 11 - Camada 1
Curso: AI Fundamentals - Guayerd - IBM Skills Build
Fecha: 2025-10-27
Sprint: Sprint_2 - Machine Learning y Normalización
-->

# EJERCICIO CLASE 7 - ANÁLISIS DE VENTAS

**Proyecto desarrollado como parte del curso AI Fundamentals - Guayerd - IBM Skills Build**

## 📋 Descripción del Ejercicio

Este ejercicio analiza datos de ventas mensuales de una empresa, incluyendo:
- Ventas por mes
- Número de visitantes
- Tasa de conversión
- Gasto en publicidad
- Productos vendidos

## 🎯 Objetivos del Análisis

1. **Identificar mes con mayor eficiencia** (ventas/gasto publicidad)
2. **Determinar mes con mejor tasa de conversión** y analizar causa
3. **Calcular ticket promedio** (ventas/productos) por mes
4. **Evaluar relación entre visitantes y ventas**

## 📊 Resultados Principales

### 1. Eficiencia Publicitaria
- **Mejor mes**: Abril con eficiencia de 5.45
- **Interpretación**: Abril generó $5.45 en ventas por cada $1 invertido en publicidad

### 2. Tasa de Conversión
- **Mejor mes**: Marzo con 3.8% de conversión
- **Análisis**: Marzo tuvo la mejor conversión a pesar de menos visitantes y gasto, indicando calidad superior de los visitantes

### 3. Ticket Promedio
- **Resultado**: $100.00 en TODOS los meses
- **Interpretación**: Ticket promedio consistente, indicando estabilidad en el precio por producto

### 4. Relación Visitantes-Ventas
- **Correlación**: 0.9896 (MUY FUERTE)
- **Mejor ratio**: Marzo con $3.04 por visitante
- **Interpretación**: Existe una relación casi perfecta entre visitantes y ventas

## 📁 Archivos del Proyecto

### Scripts de Análisis
- `analisis_especifico_ejercicio.py` - Análisis específico del ejercicio
- `analisis_ventas_ejercicio.py` - Análisis general de ventas
- `analizar_ejercicio_clase_7.py` - Análisis básico

### Datos Originales
- `Ejercicio_clase_7.xlsx` - Datos originales del ejercicio
- `Ejercicio_clase_7.jpg` - Imagen del ejercicio

### Reportes
- `reporte_especifico_ejercicio.txt` - Reporte detallado del análisis específico
- `reporte_final_ventas.txt` - Reporte general de ventas
- `reporte_ejercicio_clase_7.txt` - Reporte básico

### Visualizaciones
- `analisis_especifico_ejercicio.png` - Gráficos del análisis específico
- `analisis_completo_ventas.png` - Gráficos del análisis completo

## 🚀 Cómo Ejecutar

```bash
# Análisis específico del ejercicio
python analisis_especifico_ejercicio.py

# Análisis general de ventas
python analisis_ventas_ejercicio.py

# Análisis básico
python analizar_ejercicio_clase_7.py
```

## 📈 Métricas Calculadas

- **Eficiencia Publicitaria**: Ventas / Gasto Publicidad
- **Tasa de Conversión**: (Productos Vendidos / Visitantes) × 100
- **Ticket Promedio**: Ventas / Productos Vendidos
- **Ratio Ventas/Visitantes**: Ventas / Visitantes
- **Correlación**: Coeficiente de correlación entre variables

## 💡 Conclusiones

1. **Abril** es el mes más eficiente en publicidad
2. **Marzo** tiene la mejor conversión (calidad de visitantes)
3. **Ticket promedio constante** ($100) indica estabilidad
4. **Correlación perfecta** entre visitantes y ventas (r=0.9896)

## 🎯 Recomendaciones

1. **Replicar estrategias de Abril** para eficiencia publicitaria
2. **Analizar factores de Marzo** para mejorar calidad de visitantes
3. **Mantener ticket promedio** estable
4. **Invertir en canales** que generen visitantes de calidad

---

**Proyecto desarrollado como parte del curso AI Fundamentals - Guayerd - IBM Skills Build**  
**Autor**: Enith Gicela Vargas Vargas  
**Fecha**: 2025
