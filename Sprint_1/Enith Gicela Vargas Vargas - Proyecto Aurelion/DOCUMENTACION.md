<!--
# DOCUMENTACION.md
==================
Documentación completa del proyecto Aurelion Sprint_1

**Autor:** Enith Gicela Vargas Vargas  
**Fecha:** 2025-10-27  
**Curso:** AI Fundamentals - Guayerd - IBM Skills Build  
**Sprint:** 1 - Análisis de Datos Básico  
**Módulo:** Documentación Completa  
-->

# DOCUMENTACIÓN - PROYECTO AURELION SPRINT_1
## Análisis de Datos de Tienda con Inteligencia Artificial

---

## 📋 **INFORMACIÓN DEL PROYECTO**

- **Estudiante**: Enith Gicela Vargas Vargas
- **Grupo**: 11 - Camada 1
- **Proyecto**: Análisis de Tienda Aurelion
- **Curso**: AI Fundamentals - Guayerd - IBM Skills Build
- **Fecha**: Octubre 2025

---

## 🎯 **PASO 4: PROBLEMA A RESOLVER**

### **Problema Principal**
La tienda Aurelion necesita optimizar sus operaciones comerciales y mejorar la toma de decisiones basada en datos para:

1. **Análisis de Ventas**: Comprender patrones de compra, productos más vendidos y tendencias temporales
2. **Segmentación de Clientes**: Identificar grupos de clientes con comportamientos similares para estrategias de marketing personalizadas
3. **Optimización de Inventario**: Predecir demanda de productos y optimizar niveles de stock
4. **Análisis de Medios de Pago**: Evaluar la efectividad de diferentes métodos de pago
5. **Predicción de Ventas**: Desarrollar modelos predictivos para pronosticar ventas futuras

### **Objetivos Específicos**
- Implementar algoritmos de Machine Learning para análisis predictivo
- Crear dashboards interactivos para visualización de datos
- Desarrollar modelos de clasificación y regresión
- Generar insights accionables para la gestión empresarial

---

## 🗄️ **PASO 5: ESTRUCTURA, TIPOS Y ESCALA DE LA BASE DE DATOS**

### **Estructura de la Base de Datos**

La base de datos de Tienda Aurelion está compuesta por **4 tablas principales** con relaciones bien definidas:

#### **1. TABLA: CLIENTES** (`clientes.xlsx`)
- **Registros**: 100 clientes
- **Columnas**: 5 campos
- **Estructura**:
  - `id_cliente` (int64): Identificador único del cliente
  - `nombre_cliente` (object): Nombre completo del cliente
  - `email` (object): Dirección de correo electrónico
  - `ciudad` (object): Ciudad de residencia
  - `fecha_alta` (datetime64[ns]): Fecha de registro del cliente

#### **2. TABLA: PRODUCTOS** (`productos.xlsx`)
- **Registros**: 100 productos
- **Columnas**: 4 campos
- **Estructura**:
  - `id_producto` (int64): Identificador único del producto
  - `nombre_producto` (object): Nombre del producto
  - `categoria` (object): Categoría del producto (Alimentos, Limpieza, etc.)
  - `precio_unitario` (int64): Precio unitario en pesos argentinos

#### **3. TABLA: VENTAS** (`ventas.xlsx`)
- **Registros**: 120 transacciones de venta
- **Columnas**: 6 campos
- **Estructura**:
  - `id_venta` (int64): Identificador único de la venta
  - `fecha` (datetime64[ns]): Fecha de la transacción
  - `id_cliente` (int64): ID del cliente (FK)
  - `nombre_cliente` (object): Nombre del cliente
  - `email` (object): Email del cliente
  - `medio_pago` (object): Método de pago utilizado (tarjeta, qr, efectivo)

#### **4. TABLA: DETALLE_VENTAS** (`detalle_ventas.xlsx`)
- **Registros**: 343 líneas de detalle
- **Columnas**: 6 campos
- **Estructura**:
  - `id_venta` (int64): ID de la venta (FK)
  - `id_producto` (int64): ID del producto (FK)
  - `nombre_producto` (object): Nombre del producto
  - `cantidad` (int64): Cantidad vendida
  - `precio_unitario` (int64): Precio unitario al momento de la venta
  - `importe` (int64): Importe total de la línea (cantidad × precio_unitario)

### **Relaciones entre Tablas**

```
CLIENTES (1) ←→ (N) VENTAS
    ↓
DETALLE_VENTAS (N) ←→ (1) VENTAS
    ↓
PRODUCTOS (1) ←→ (N) DETALLE_VENTAS
```

### **Clasificación de Datos según Estructura**

#### **Estructurados (Tabulares)**
- **Tipo**: Datos organizados en filas y columnas
- **Formato**: Excel (.xlsx), SQL
- **Características**: 
  - Campos (columnas): Representan características individuales de una entidad
  - Registros (filas): Instancias únicas u observaciones de la entidad
  - Tabla: Estructura que agrupa múltiples registros bajo un mismo conjunto de campos

#### **Identificadores y Relaciones**
- **Clave Primaria (PK)**: Campo/s que garantizan la unicidad de cada registro
  - `id_cliente`, `id_producto`, `id_venta`
- **Clave Foránea (FK)**: Campo que establece una relación lógica con la clave primaria
  - `id_cliente` en tabla ventas → PK en tabla clientes
  - `id_producto` en detalle_ventas → PK en tabla productos

### **Tipos de Datos Técnicos**

| Campo | Tipo | Descripción | Ejemplo |
|-------|------|-------------|---------|
| IDs | int64 | Identificadores únicos | 1, 2, 3... |
| Nombres/Textos | object | Cadenas de texto | "Mariana Lopez" |
| Fechas | datetime64[ns] | Fechas y timestamps | 2024-01-02 |
| Precios/Importes | int64 | Valores monetarios en pesos | 2347, 4973 |
| Cantidades | int64 | Números enteros | 1, 2, 5 |

### **Clasificación según Origen**

#### **Datos Secundarios**
- **Tipo**: Recopilados por otros (fuentes abiertas, sistemas previos)
- **Fuente**: Base de datos proporcionada por el curso
- **Características**:
  - Datos históricos de la Tienda Aurelion
  - Estructura predefinida y validada
  - Formato estándar Excel para facilitar análisis

### **Escala de la Base de Datos**

- **Tamaño Total**: ~52 KB (archivos Excel)
- **Registros Totales**: 663 registros distribuidos en 4 tablas
- **Período Temporal**: Datos desde 2023 hasta 2024
  - Clientes: 2023 (enero a abril)
  - Ventas: 2024 (enero a junio)
- **Cobertura Geográfica**: Múltiples ciudades argentinas
- **Categorías de Productos**: Alimentos, Limpieza, y otras categorías
- **Medios de Pago**: Tarjeta, QR, Efectivo

### **Calidad de los Datos**

✅ **Fortalezas**:
- Estructura relacional bien definida
- Integridad referencial mantenida
- Tipos de datos consistentes
- Cobertura temporal adecuada

⚠️ **Consideraciones**:
- Datos de muestra (escala pequeña para producción)
- Precios en formato entero (sin decimales)
- Necesidad de validación de datos faltantes

---

## 🚀 **PRÓXIMOS PASOS**

1. **Análisis Exploratorio de Datos (EDA)**
2. **Limpieza y Preprocesamiento de Datos**
3. **Desarrollo de Modelos de Machine Learning**
4. **Creación de Visualizaciones Interactivas**
5. **Implementación de Dashboards**
6. **Validación y Testing de Modelos**

---

## 📊 **TECNOLOGÍAS A UTILIZAR**

- **Python** para análisis de datos
- **Pandas** para manipulación de datos
- **Scikit-learn** para Machine Learning
- **Matplotlib/Seaborn** para visualizaciones
- **Jupyter Notebooks** para análisis interactivo
- **Streamlit** para dashboards web

---

*Documento creado como parte del proyecto AI Fundamentals - Guayerd - IBM Skills Build*
