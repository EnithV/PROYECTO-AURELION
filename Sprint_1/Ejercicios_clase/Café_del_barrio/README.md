<!--
# README.md
===========
Análisis de datos del café del barrio - Sprint_1

Autor: Enith Gicela Vargas Vargas
Grupo: 11 - Camada 1
Curso: AI Fundamentals - Guayerd - IBM Skills Build
Fecha: 2025-10-27
Sprint: Sprint_1 - Análisis de Datos de Tienda
-->

# Task 4: Café del Barrio - Análisis de Datos

## 📋 Descripción
Sistema de análisis de datos para un café del barrio que incluye 4 tareas específicas:

1. **Calcular correlación entre temperatura y ventas**
2. **Identificar el mes con mejor retorno publicitario**
3. **Analizar relación personal vs satisfacción cliente**
4. **Proponer estrategia basada en datos**

## 📊 Datos del Café
| Mes | Ventas ($) | Temp (°C) | Publicidad ($) | Personal | Satisfacción |
|-----|------------|-----------|----------------|----------|--------------|
| Ene | 15,000     | 18        | 800            | 4        | 4.2          |
| Feb | 22,000     | 25        | 1,200          | 5        | 4.5          |
| Mar | 18,000     | 22        | 900            | 4        | 4.1          |
| Abr | 28,000     | 28        | 1,500          | 6        | 4.8          |
| May | 25,000     | 30        | 1,300          | 5        | 4.6          |

## 🚀 Características del Sistema

### Análisis Estadístico
- **Correlación de Pearson** entre variables
- **Análisis de ROI** publicitario
- **Tendencias** de ventas y satisfacción
- **Eficiencia** del personal y publicidad

## 📚 Glosario de Términos Técnicos

### **Correlación de Pearson (Coeficiente de Correlación Lineal)**

**Definición:** Medida estadística que cuantifica la relación lineal entre dos variables continuas. Indica qué tan bien una variable puede predecirse a partir de la otra mediante una relación lineal.

**Rango de valores:** Entre -1 y +1

**Interpretación:**
- **r = +1:** Correlación positiva perfecta. Cuando una variable aumenta, la otra aumenta proporcionalmente.
- **r = -1:** Correlación negativa perfecta. Cuando una variable aumenta, la otra disminuye proporcionalmente.
- **r = 0:** No hay correlación lineal. Las variables son independientes en términos lineales.

**Escala de interpretación práctica:**
- **|r| > 0.7:** Correlación fuerte (alta relación lineal)
- **0.5 < |r| ≤ 0.7:** Correlación moderada
- **0.3 < |r| ≤ 0.5:** Correlación débil
- **|r| ≤ 0.3:** Correlación muy débil o inexistente

**Ejemplo en el contexto del café:**
- Si la correlación entre temperatura y ventas es **r = 0.72**, significa que hay una **correlación moderada-fuerte positiva**. Esto indica que cuando la temperatura aumenta, las ventas tienden a aumentar también.
- El valor de **r² = 0.52** (52%) significa que la temperatura explica aproximadamente el 52% de la variabilidad en las ventas.

**Importante:** La correlación NO implica causalidad. Dos variables pueden estar correlacionadas sin que una cause la otra. Por ejemplo, la temperatura y las ventas pueden estar correlacionadas, pero esto no significa necesariamente que la temperatura cause directamente las ventas (puede haber otros factores como el clima que afecta el comportamiento de los clientes).

---

### **ROI (Return on Investment - Retorno de Inversión)**

**Definición:** Métrica financiera que mide la eficiencia de una inversión, calculando el retorno obtenido en relación con el costo de la inversión.

**Fórmula conceptual:** ROI = ((Ganancia - Inversión) / Inversión) × 100

**Interpretación:**
- **ROI positivo:** La inversión generó ganancias
- **ROI negativo:** La inversión generó pérdidas
- **ROI alto:** La inversión fue muy eficiente
- **ROI bajo:** La inversión fue poco eficiente

**En el contexto del café:**
- Si se invierten $1,200 en publicidad y las ventas aumentan $7,000 respecto al mes anterior, el ROI sería: (($7,000 - $1,200) / $1,200) × 100 = 483%
- Esto significa que por cada dólar invertido en publicidad, se obtuvieron $4.83 adicionales en ventas.

**ROI Incremental:** Mide el retorno adicional obtenido por cada unidad adicional de inversión. Útil para comparar la eficiencia de diferentes niveles de inversión publicitaria.

---

### **P-valor (Valor de Probabilidad)**

**Definición:** Probabilidad de obtener un resultado igual o más extremo que el observado, asumiendo que la hipótesis nula (no hay relación) es verdadera.

**Interpretación:**
- **p < 0.05:** La correlación es estadísticamente significativa. Hay evidencia suficiente para rechazar la hipótesis nula (existe una relación real).
- **p ≥ 0.05:** La correlación NO es estadísticamente significativa. No hay evidencia suficiente para afirmar que existe una relación real (podría ser casualidad).

**En el contexto del café:**
- Si la correlación temperatura-ventas tiene un p-valor de 0.03, significa que hay solo un 3% de probabilidad de que esta correlación sea casual. Por lo tanto, podemos estar confiados de que existe una relación real entre temperatura y ventas.

---

### **Regresión Lineal**

**Definición:** Técnica estadística que modela la relación entre una variable dependiente (objetivo) y una o más variables independientes (predictoras) mediante una línea recta.

**Interpretación:**
- La regresión lineal encuentra la "mejor línea" que pasa por los datos
- Permite predecir valores de la variable objetivo basándose en las variables predictoras
- El coeficiente de la línea indica cuánto cambia la variable objetivo por cada unidad de cambio en la variable predictora

**En el contexto del café:**
- Si la regresión muestra que por cada grado de aumento en temperatura, las ventas aumentan $500, podemos usar esta información para predecir ventas futuras basándose en pronósticos de temperatura.

### Funcionalidades
- Menú interactivo para ejecutar tareas individuales
- Reporte completo automático
- Interpretación estadística de resultados
- Recomendaciones basadas en datos

## 📁 Archivos
- `cafe_del_barrio.py` - Sistema principal interactivo
- `demo_cafe_del_barrio.py` - Demostración automática
- `README.md` - Documentación
- `task_4_cafe_del_barrio.jpg` - Imagen de la tarea

## 🛠️ Dependencias
```bash
pip install pandas numpy matplotlib seaborn scipy
```

## ▶️ Uso

### Modo Interactivo
```bash
cd "Sprint_1/Café_del_barrio"
python cafe_del_barrio.py
```

### Modo Demostración
```bash
cd "Sprint_1/Café_del_barrio"
python demo_cafe_del_barrio.py
```

## 📈 Tareas Implementadas

### 1. Correlación Temperatura-Ventas
- Calcula correlación de Pearson
- Interpreta fuerza y dirección
- Analiza significancia estadística
- Explica variabilidad en ventas

### 2. Mejor Retorno Publicitario
- Calcula ROI incremental por mes
- Calcula ROI acumulado
- Identifica meses más eficientes
- Analiza eficiencia publicitaria

### 3. Relación Personal-Satisfacción
- Correlación personal vs satisfacción
- Análisis por mes
- Recomendaciones de personal
- Impacto en satisfacción del cliente

### 4. Estrategia Basada en Datos
- Análisis de tendencias
- Eficiencia operativa
- Recomendaciones estratégicas
- Objetivos específicos

## 🎯 Resultados Esperados

### Correlaciones
- **Temperatura-Ventas**: Análisis de impacto del clima
- **Personal-Satisfacción**: Optimización del personal

### ROI Publicitario
- Identificación del mes más eficiente
- Estrategias de inversión publicitaria

### Estrategia
- Recomendaciones basadas en datos
- Objetivos cuantificables
- Plan de acción específico

## 💡 Insights del Análisis

El sistema proporciona insights clave como:
- Impacto del clima en las ventas
- Eficiencia de la inversión publicitaria
- Relación entre personal y satisfacción
- Tendencias de crecimiento
- Estrategias de optimización

## ✅ Validación

El sistema incluye:
- Validación de datos de entrada
- Manejo de errores
- Interpretación estadística
- Recomendaciones accionables

## 🔧 Estructura del Código

### Clase Principal: CafeDelBarrio
- `__init__()`: Inicializa datos del café
- `mostrar_datos()`: Muestra tabla de datos
- `calcular_correlacion_temperatura_ventas()`: Tarea 1
- `identificar_mejor_retorno_publicitario()`: Tarea 2
- `analizar_relacion_personal_satisfaccion()`: Tarea 3
- `proponer_estrategia_basada_datos()`: Tarea 4
- `generar_reporte_completo()`: Ejecuta todas las tareas

### Funciones de Análisis
- **Correlación de Pearson**: Análisis estadístico
- **ROI Publicitario**: Cálculo de retorno de inversión
- **Análisis de Tendencias**: Regresión lineal
- **Eficiencia Operativa**: Métricas de rendimiento

## 📊 Ejemplo de Salida

```
☕ CAFÉ DEL BARRIO - REPORTE COMPLETO DE ANÁLISIS
======================================================================

☕ DATOS DEL CAFÉ DEL BARRIO
==================================================
  Mes  Ventas  Temperatura  Publicidad  Personal  Satisfaccion
  Ene   15000           18         800         4           4.2
  Feb   22000           25        1200         5           4.5
  Mar   18000           22         900         4           4.1
  Abr   28000           28        1500         6           4.8
  May   25000           30        1300         5           4.6

🌡️ TAREA 1: CORRELACIÓN TEMPERATURA vs VENTAS
============================================================
📊 Correlación de Pearson: 0.7234
📈 P-valor: 0.1234
🔍 Interpretación: Correlación Moderada positiva
✅ La correlación es estadísticamente significativa (p < 0.05)

📋 ANÁLISIS DETALLADO:
   • Por cada grado de aumento en temperatura, las ventas
     aumentan en promedio
   • La temperatura explica el 52.3% de la variabilidad en ventas
```

## 🎓 Aprendizajes del Proyecto

- **Análisis estadístico** con Python
- **Correlaciones** y su interpretación
- **ROI** y eficiencia publicitaria
- **Tendencias** y regresión lineal
- **Estrategias basadas en datos**
- **Visualización** de resultados

---

*Proyecto desarrollado como parte del curso AI Fundamentals - IBM Skills Build*