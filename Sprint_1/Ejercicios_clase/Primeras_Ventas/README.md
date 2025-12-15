<!--
# README.md
===========
Análisis de las primeras 10 ventas - Sprint_1

Autor: Enith Gicela Vargas Vargas
Grupo: 11 - Camada 1
Curso: AI Fundamentals - Guayerd - IBM Skills Build
Fecha: 2025-10-27
Sprint: Sprint_1 - Análisis de Datos de Tienda
-->

# TASK 3: PRIMERAS 10 VENTAS

## 📋 **Descripción de la Tarea**

Esta tarea analiza las primeras 10 ventas de una tienda recién abierta. El usuario ingresa los montos de estas ventas y el programa realiza un análisis completo para entender el arranque del negocio.

## 🎯 **Objetivos de la Tarea**

1. **Solicitar al usuario** el monto de las primeras 10 ventas
2. **Calcular el promedio** de estas ventas iniciales
3. **Identificar cuáles ventas** estuvieron por encima del promedio
4. **Calcular el total recaudado** en estas primeras ventas
5. **Determinar cuál fue** la mejor y peor venta inicial

## 📊 **Archivos del Proyecto**

### **Script Principal**
- `primeras_ventas.py` - Análisis interactivo de las primeras 10 ventas

### **Archivos de Referencia**
- `task_3_primeras_ventas.jpg` - Imagen de la tarea original
- `README.md` - Esta documentación

## 🚀 **Cómo Ejecutar**

### **Requisitos**
```bash
# No se requieren dependencias externas
# Solo Python estándar
```

### **Ejecución**
```bash
python primeras_ventas.py
```

## 🔍 **Funcionalidades del Programa**

### **1. Entrada de Datos**
- Solicita al usuario ingresar los montos de las primeras 10 ventas
- Validación de entrada (números positivos)
- Manejo de errores y interrupciones

### **2. Análisis Estadístico**
- **Promedio**: Cálculo del promedio de las 10 ventas
- **Total**: Suma total de todas las ventas
- **Mejor venta**: Identificación de la venta con mayor monto
- **Peor venta**: Identificación de la venta con menor monto

### **3. Análisis Comparativo**
- **Ventas sobre promedio**: Identifica cuáles ventas superan el promedio
- **Diferencia con promedio**: Muestra cuánto exceden el promedio
- **Variabilidad**: Calcula la diferencia entre la mejor y peor venta

### **4. Insights Adicionales**
- **Porcentaje sobre promedio**: Qué % de ventas superan el promedio
- **Tendencia**: Compara las primeras 3 vs las últimas 3 ventas
- **Consistencia**: Mide la variabilidad de las ventas

## 📈 **Ejemplo de Uso**

```
🏪 ANÁLISIS DE LAS PRIMERAS 10 VENTAS
==================================================
Acabas de abrir tu primera tienda y quieres analizar
tus primeras 10 ventas para entender el arranque del negocio.

Ingresa el monto de la venta 1: $150.50
Ingresa el monto de la venta 2: $200.00
Ingresa el monto de la venta 3: $175.25
...

============================================================
📊 ANÁLISIS DE LAS PRIMERAS 10 VENTAS
============================================================

💰 VENTAS INGRESADAS:
------------------------------
   Venta  1: $  150.50
   Venta  2: $  200.00
   Venta  3: $  175.25
   ...

📈 PROMEDIO DE VENTAS INICIALES:
----------------------------------------
   Promedio: $  187.50

⬆️ VENTAS POR ENCIMA DEL PROMEDIO:
----------------------------------------
   Total de ventas sobre promedio: 4
   Venta  2: $  200.00 (+$  12.50)
   Venta  5: $  195.00 (+$   7.50)
   ...

💵 TOTAL RECAUDADO:
------------------------------
   Total: $1,875.00

🏆 MEJOR Y PEOR VENTA:
------------------------------
   Mejor venta: #2 con $200.00
   Peor venta:  #7 con $150.00
   Diferencia:  $50.00

💡 INSIGHTS ADICIONALES:
------------------------------
   Variabilidad: 26.7% (diferencia entre mejor y peor venta)
   Ventas sobre promedio: 40.0% del total
   Tendencia: 📈 Mejorando (últimas 3 vs primeras 3)

✅ Análisis completado exitosamente
============================================================
```

## 🛠️ **Tecnologías Utilizadas**

- **Python 3.x** - Lenguaje de programación
- **Funciones nativas** - Sin dependencias externas
- **Manejo de entrada** - Input del usuario
- **Validación de datos** - Verificación de entrada

## 📋 **Estructura del Código**

### **Funciones Principales**
- `solicitar_primeras_10_ventas()` - Entrada de datos del usuario
- `calcular_promedio()` - Cálculo del promedio
- `identificar_ventas_sobre_promedio()` - Análisis comparativo
- `calcular_total_recaudado()` - Suma total
- `determinar_mejor_peor_venta()` - Identificación de extremos
- `mostrar_analisis()` - Presentación de resultados

### **Características del Código**
- ✅ **Interactivo**: Solicita datos al usuario
- ✅ **Validado**: Verifica entrada correcta
- ✅ **Robusto**: Maneja errores y interrupciones
- ✅ **Completo**: Cumple todos los requisitos de la tarea
- ✅ **Limpio**: Código bien estructurado y documentado

## 🎯 **Requisitos Cumplidos**

✅ **1. Solicitar al usuario el monto de las primeras 10 ventas**
✅ **2. Calcular el promedio de estas ventas iniciales**
✅ **3. Identificar cuáles ventas estuvieron por encima del promedio**
✅ **4. Calcular el total recaudado en estas primeras ventas**
✅ **5. Determinar cuál fue tu mejor y peor venta inicial**

## 💡 **Valor Agregado**

Además de cumplir con los requisitos básicos, el programa incluye:
- **Insights adicionales** para mejor comprensión del negocio
- **Análisis de tendencias** para identificar patrones
- **Métricas de consistencia** para evaluar estabilidad
- **Interfaz amigable** con emojis y formato claro

---

*Proyecto desarrollado como parte del curso AI Fundamentals - IBM Skills Build*