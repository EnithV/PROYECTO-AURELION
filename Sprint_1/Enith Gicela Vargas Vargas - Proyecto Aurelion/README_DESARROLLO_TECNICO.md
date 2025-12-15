<!--
# README_DESARROLLO_TECNICO.md
==============================
Desarrollo técnico del proyecto Aurelion Sprint_1

**Autor:** Enith Gicela Vargas Vargas  
**Fecha:** 2025-10-27  
**Curso:** AI Fundamentals - Guayerd - IBM Skills Build  
**Sprint:** 1 - Análisis de Datos Básico  
**Módulo:** Desarrollo Técnico  
-->

# DESARROLLO TÉCNICO - PROYECTO AURELION SPRINT_1

## 📋 Descripción
Sistema completo de análisis de datos para la optimización de operaciones de la Tienda Aurelion utilizando técnicas de Inteligencia Artificial.

## 🎯 Objetivos del Desarrollo
- **Análisis de Ventas**: Métricas, tendencias y patrones de ventas
- **Segmentación de Clientes**: Análisis RFM para estrategias de marketing
- **Análisis de Productos**: Rentabilidad y optimización de inventario
- **Análisis de Pagos**: Eficiencia de métodos de pago
- **Reportes Ejecutivos**: Dashboards y recomendaciones

## 📊 Diagrama de Flujo
El sistema sigue un flujo estructurado que incluye:
1. **Carga de Datos** desde archivos Excel
2. **Validación** de estructura y calidad
3. **Preparación** de datos para análisis
4. **Procesamiento** de análisis específicos
5. **Visualización** de resultados
6. **Generación** de reportes

## 🐍 Archivos Python

### **aurelion_analisis.py** - Sistema Principal
Sistema completo e interactivo con las siguientes funcionalidades:

#### **Clase AurelionAnalisis**
- `__init__()`: Inicialización del sistema
- `cargar_datos()`: Carga desde archivos Excel
- `_validar_datos()`: Validación de estructura
- `_preparar_datos()`: Preparación para análisis

#### **Métodos de Análisis**
- `analisis_ventas()`: Análisis completo de ventas
- `segmentacion_clientes_rfm()`: Segmentación RFM
- `analisis_productos()`: Análisis de productos y rentabilidad
- `analisis_pagos()`: Análisis de métodos de pago
- `reporte_completo()`: Reporte ejecutivo completo

#### **Interfaz de Usuario**
- `mostrar_menu_principal()`: Menú interactivo
- `mostrar_info_sistema()`: Información del sistema
- `ejecutar()`: Bucle principal del sistema

### **demo_aurelion.py** - Demostración
Script de demostración que muestra las capacidades del sistema con datos de ejemplo:

#### **Funciones de Demostración**
- `generar_datos_ejemplo()`: Genera datos sintéticos
- `demo_analisis_ventas()`: Demo de análisis de ventas
- `demo_segmentacion_rfm()`: Demo de segmentación RFM
- `demo_analisis_productos()`: Demo de análisis de productos
- `demo_analisis_pagos()`: Demo de análisis de pagos

## 🛠️ Dependencias

### **Librerías Principales**
```python
pandas          # Manipulación de datos
numpy           # Cálculos numéricos
matplotlib      # Visualizaciones
seaborn         # Gráficos estadísticos
openpyxl        # Lectura de archivos Excel
```

### **Instalación**
```bash
pip install pandas numpy matplotlib seaborn openpyxl
```

## 🚀 Uso del Sistema

### **Sistema Principal**
```bash
cd "Sprint_1/Enith Gicela Vargas Vargas - Proyecto Aurelion"
python aurelion_analisis.py
```

### **Demostración**
```bash
cd "Sprint_1/Enith Gicela Vargas Vargas - Proyecto Aurelion"
python demo_aurelion.py
```

## 📁 Estructura de Datos Requerida

### **clientes.xlsx**
- `id_cliente`: Identificador único
- `nombre_cliente`: Nombre del cliente
- `email`: Correo electrónico
- `telefono`: Número de teléfono
- `fecha_registro`: Fecha de registro

### **productos.xlsx**
- `id_producto`: Identificador único
- `nombre_producto`: Nombre del producto
- `categoria`: Categoría del producto
- `precio_unitario`: Precio de venta
- `costo_unitario`: Costo del producto

### **ventas.xlsx**
- `id_venta`: Identificador único
- `id_cliente`: ID del cliente
- `fecha_venta`: Fecha de la venta
- `metodo_pago`: Método de pago
- `total_venta`: Total de la venta

### **detalle_ventas.xlsx**
- `id_venta`: ID de la venta
- `id_producto`: ID del producto
- `cantidad`: Cantidad vendida
- `precio_unitario`: Precio unitario
- `subtotal`: Subtotal del producto

## 🔍 Funcionalidades Detalladas

### **1. Análisis de Ventas**
- **Métricas Básicas**: Total, promedio, mejor/peor venta
- **Análisis Temporal**: Ventas por mes, tendencias
- **Top Productos**: Productos más vendidos
- **Top Clientes**: Clientes con mayores compras

### **2. Segmentación RFM**
- **Recency**: Días desde la última compra
- **Frequency**: Frecuencia de compras
- **Monetary**: Valor total gastado
- **Segmentos**: Campeones, Leales, Potenciales, Nuevos, En Riesgo, Perdidos

### **3. Análisis de Productos**
- **Métricas por Producto**: Unidades vendidas, ingresos, margen
- **Análisis por Categoría**: Ventas por categoría
- **Rentabilidad**: Productos más rentables
- **Optimización**: Recomendaciones de inventario

### **4. Análisis de Pagos**
- **Distribución**: Ventas por método de pago
- **Métricas**: Número de ventas, totales, promedios
- **Porcentajes**: Distribución porcentual
- **Recomendaciones**: Estrategias de pago

## 📈 Características Técnicas

### **Manejo de Errores**
- Validación de archivos existentes
- Verificación de estructura de datos
- Manejo de errores de carga
- Mensajes informativos

### **Optimización**
- Carga eficiente de datos
- Cálculos vectorizados con pandas
- Memoria optimizada
- Procesamiento rápido

### **Interfaz de Usuario**
- Menú interactivo intuitivo
- Mensajes claros y descriptivos
- Navegación fácil
- Validación de entrada

## 🎯 Resultados Esperados

### **Insights de Negocio**
- Identificación de patrones de ventas
- Segmentación efectiva de clientes
- Optimización de productos
- Estrategias de pago

### **Métricas Clave**
- KPIs de ventas
- Métricas de clientes
- Rentabilidad de productos
- Eficiencia operativa

### **Recomendaciones**
- Estrategias de marketing
- Optimización de inventario
- Mejoras operativas
- Objetivos de crecimiento

## 🔧 Personalización

### **Configuración**
- Ajuste de parámetros RFM
- Personalización de métricas
- Configuración de visualizaciones
- Adaptación de reportes

### **Extensiones**
- Nuevos análisis
- Integración con APIs
- Exportación de datos
- Automatización

## ✅ Validación

### **Pruebas**
- Datos de ejemplo incluidos
- Validación de funcionalidades
- Manejo de errores
- Rendimiento

### **Calidad**
- Código documentado
- Estructura modular
- Manejo de excepciones
- Optimización

---

*Desarrollado por Enith Gicela Vargas Vargas - Grupo 11 - Camada 1*  
*Curso AI Fundamentals - Guayerd - IBM Skills Build*
