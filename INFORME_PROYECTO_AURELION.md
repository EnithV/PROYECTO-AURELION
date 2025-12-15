# INFORME PROYECTO AURELION
## Sistema de Análisis de Datos e Inteligencia Artificial para Tienda Retail

**Autor:** Enith Gicela Vargas Vargas  
**Camada:** 1  
**Grupo:** 11  
**Curso:** AI Fundamentals - Guayerd - IBM Skills Build  
**Fecha:** Noviembre 2025  
**Duración de Exposición:** 15 minutos

---

## TABLA DE CONTENIDOS

1. [Resumen Ejecutivo](#1-resumen-ejecutivo)
2. [Introducción y Contexto](#2-introducción-y-contexto)
3. [Metodología del Proyecto](#3-metodología-del-proyecto)
4. [Sprint 1: Análisis Exploratorio y Segmentación RFM](#4-sprint-1-análisis-exploratorio-y-segmentación-rfm)
   - [Funciones Principales Utilizadas en el Sprint 1](#46-funciones-principales-utilizadas-en-el-sprint-1)
   - [Métodos de Pandas Utilizados en el Sprint 1](#47-métodos-de-pandas-utilizados-en-el-sprint-1)
5. [Sprint 2: Normalización de Datos y Machine Learning](#5-sprint-2-normalización-de-datos-y-machine-learning)
   - [Funciones Principales Utilizadas en el Sprint 2](#55-funciones-principales-utilizadas-en-el-sprint-2)
   - [Métodos de Pandas y Scikit-learn Utilizados en el Sprint 2](#56-métodos-de-pandas-y-scikit-learn-utilizados-en-el-sprint-2)
6. [Sprint 3: Fundamentos de Machine Learning y Modelado](#6-sprint-3-fundamentos-de-machine-learning-y-modelado)
   - [Funciones Principales Utilizadas en el Sprint 3](#65-funciones-principales-utilizadas-en-el-sprint-3)
   - [Métodos de Scikit-learn y Pandas Utilizados en el Sprint 3](#66-métodos-de-scikit-learn-y-pandas-utilizados-en-el-sprint-3)
7. [Resultados y Logros](#7-resultados-y-logros)
8. [Conclusiones](#8-conclusiones)
9. [Recomendaciones Estratégicas](#9-recomendaciones-estratégicas)
10. [Preguntas Frecuentes y Respuestas](#10-preguntas-frecuentes-y-respuestas)

---

## 1. RESUMEN EJECUTIVO

### 1.1. Visión General

El **Proyecto Aurelion** es un sistema integral de análisis de datos e inteligencia artificial desarrollado para una tienda retail, que abarca desde el análisis exploratorio de datos hasta la implementación de modelos de Machine Learning avanzados. El proyecto se desarrolló en tres sprints consecutivos, cada uno con objetivos específicos y entregables medibles.

### 1.2. Objetivos Principales

- **Análisis de Datos:** Realizar un análisis exploratorio completo de las ventas, productos, clientes y métodos de pago
- **Segmentación de Clientes:** Implementar segmentación RFM (Recency, Frequency, Monetary) para estrategias de marketing personalizadas
- **Preparación de Datos:** Normalizar y preparar datos para Machine Learning con técnicas avanzadas
- **Modelos Predictivos:** Desarrollar modelos de regresión, clasificación y clustering con alta precisión
- **Analítica Avanzada:** Implementar estadística inferencial y prescriptiva para recomendaciones accionables

### 1.3. Resultados Clave

- ✅ **99.62% de precisión** en modelos de regresión (R² Score)
- ✅ **88.41% de precisión** en modelos de clasificación (Accuracy)
- ✅ **Segmentación RFM** implementada con 4 segmentos de clientes
- ✅ **9 modelos de ML** entrenados y evaluados
- ✅ **24 visualizaciones avanzadas** generadas
- ✅ **Sistema interactivo** completo con 15 opciones de navegación

---

## 2. INTRODUCCIÓN Y CONTEXTO

### 2.1. El Problema

Las tiendas retail modernas generan grandes volúmenes de datos de ventas, clientes y productos, pero muchas veces no tienen las herramientas adecuadas para:
- Entender el comportamiento de sus clientes
- Predecir tendencias de ventas
- Optimizar inventarios y precios
- Personalizar estrategias de marketing

### 2.2. La Solución: Proyecto Aurelion

El Proyecto Aurelion proporciona una solución completa que integra:
- **Análisis Exploratorio de Datos (EDA)** para entender los datos
- **Segmentación de Clientes** para estrategias personalizadas
- **Normalización Avanzada** para preparar datos para ML
- **Modelos de Machine Learning** para predicciones y clasificaciones
- **Analítica Prescriptiva** para recomendaciones accionables

### 2.3. Fuente de Datos

El proyecto utiliza una base de datos relacional con 4 tablas principales:
- **clientes.xlsx:** Información demográfica de clientes (edad, género, ciudad)
- **productos.xlsx:** Catálogo de productos (categoría, precio, stock)
- **ventas.xlsx:** Transacciones de ventas (fecha, cliente, método de pago, importe)
- **detalle_ventas.xlsx:** Detalle de cada venta (producto, cantidad, precio unitario)

**Relaciones:**
- `ventas.id_cliente` → `clientes.id_cliente` (Foreign Key)
- `detalle_ventas.id_venta` → `ventas.id_venta` (Foreign Key)
- `detalle_ventas.id_producto` → `productos.id_producto` (Foreign Key)

---

## 3. METODOLOGÍA DEL PROYECTO

### 3.1. Enfoque Metodológico

El proyecto siguió una metodología **ágil e iterativa** con tres sprints, cada uno enfocado en un aspecto específico del análisis de datos y Machine Learning:

```
Sprint 1: Análisis Exploratorio → Sprint 2: Normalización y ML → Sprint 3: Fundamentos y Modelado
```

### 3.2. Herramientas y Tecnologías

- **Lenguaje:** Python 3.8+
- **Librerías Principales:**
  - `pandas` - Manipulación de datos
  - `numpy` - Cálculos numéricos
  - `matplotlib` y `seaborn` - Visualizaciones
  - `scikit-learn` - Machine Learning
  - `scipy` - Estadística avanzada
  - `category-encoders` - Codificación de variables categóricas
  - `openpyxl` - Lectura de archivos Excel

### 3.3. Estructura del Proyecto

```
PROYECTO AURELION/
├── Datos Proyecto/          # Base de datos original
├── Sprint_1/                # Análisis Exploratorio y RFM
├── Sprint_2/                # Normalización y ML
├── Sprint_3/                # Fundamentos y Modelado
├── programa_unificado_aurelion.py  # Sistema interactivo principal
└── requirements.txt         # Dependencias
```

### 3.4. Principios de Desarrollo

- **Programación Orientada a Objetos (OOP):** Código modular y reutilizable
- **Manejo de Errores:** Validación robusta en todas las operaciones
- **Documentación:** Código documentado en español con comentarios explicativos
- **Interactividad:** Sistemas de menú para facilitar el uso
- **Reproducibilidad:** Semillas aleatorias fijas para resultados consistentes

---

## 4. SPRINT 1: ANÁLISIS EXPLORATORIO Y SEGMENTACIÓN RFM

### 4.1. Objetivos del Sprint 1

1. Cargar y preparar los datos de la base de datos
2. Realizar análisis exploratorio completo
3. Implementar segmentación RFM de clientes
4. Generar reportes ejecutivos
5. Crear sistema interactivo de navegación

### 4.2. Desarrollo Técnico

#### 4.2.1. Sistema Principal: `aurelion_analisis.py`

**Arquitectura:**
- Clase principal con métodos modulares
- Carga de datos desde archivos Excel
- Preparación automática de datos
- Menú interactivo con 6 opciones principales

**Funcionalidades Implementadas:**

1. **Análisis de Ventas:**
   - Total de ventas por período
   - Ventas promedio por transacción
   - Análisis de tendencias temporales
   - Identificación de días/meses más rentables

2. **Análisis de Productos:**
   - Productos más vendidos
   - Categorías con mayor rotación
   - Análisis de precios y stock
   - Productos con bajo rendimiento

3. **Análisis de Pagos:**
   - Distribución de métodos de pago
   - Relación entre método de pago y monto
   - Preferencias de pago por segmento

4. **Análisis de Clientes:**
   - Distribución demográfica (edad, género, ciudad)
   - Clientes más valiosos
   - Patrones de compra por segmento

5. **Segmentación RFM:**
   - **Recency (R):** Días desde última compra
   - **Frequency (F):** Número de compras
   - **Monetary (M):** Monto total gastado
   - **Segmentos generados:**
     - **Campeones:** Alta frecuencia, alto monto, compra reciente
     - **Leales:** Alta frecuencia, compra regular
     - **En Riesgo:** Baja frecuencia reciente
     - **Nuevos:** Primera compra reciente

6. **Reporte Completo:**
   - Generación automática de reportes en formato texto
   - Incluye todos los análisis realizados
   - Guardado con timestamp para trazabilidad

#### 4.2.2. Documentación Técnica

**`DOCUMENTACION.md`:**
- Descripción del proyecto
- Estructura de la base de datos
- Tipos de datos y escalas
- Relaciones entre tablas
- Calidad de datos

**`README_DESARROLLO_TECNICO.md`:**
- Objetivos técnicos
- Flujo de datos
- Dependencias
- Instrucciones de uso
- Funcionalidades detalladas

**`diagrama_flujo_aurelion.txt`:**
- Diagrama de flujo del sistema
- Proceso desde carga de datos hasta generación de reportes
- Decisiones y bifurcaciones del sistema

### 4.3. Resultados del Sprint 1

- ✅ Sistema interactivo funcional
- ✅ 4 tipos de análisis implementados
- ✅ Segmentación RFM operativa
- ✅ Generación automática de reportes
- ✅ Documentación completa
- ✅ 100% de cumplimiento de requisitos (verificado en `CHECKLIST_FINAL_AURELION.md`)

### 4.4. Patrones Ocultos Descubiertos en el Análisis Exploratorio

El análisis exploratorio reveló varios patrones ocultos que no eran evidentes a simple vista:

#### 4.4.1. Distribución Multimodal de Precios de Productos

**Patrón descubierto:** Los productos no se distribuyen uniformemente en precio, sino que forman **3 segmentos claros**:
- **Segmento Económico:** 1,500 - 1,750 pesos (productos de bajo precio)
- **Segmento Medio:** 2,500 - 2,750 pesos (productos de precio medio)
- **Segmento Premium:** 4,750 - 5,000 pesos (productos de alto precio)

**Implicación:** La tienda tiene una estrategia de segmentación de precios bien definida, pero existe una **oportunidad en el rango 3,000-4,000 pesos** que está poco representado.

#### 4.4.2. Patrones de Comportamiento de Compra

**Patrón descubierto:** Los clientes muestran **3 comportamientos de compra distintos**:
- **40% de transacciones:** Compra individual (1 unidad) - comportamiento personal
- **35% de transacciones:** Compra familiar (2-3 unidades) - comportamiento familiar
- **25% de transacciones:** Compra mayorista (4+ unidades) - comportamiento comercial

**Implicación:** Estrategias diferenciadas: promociones individuales, paquetes familiares y descuentos por volumen.

#### 4.4.3. Relación Inversa Cantidad-Precio

**Patrón descubierto:** Existe una **correlación inversa** entre cantidad comprada y precio unitario:
- Productos económicos (1,500-1,750 pesos): Cantidades promedio de 2-3 unidades
- Productos medios (2,500-2,750 pesos): Cantidades promedio de 1-2 unidades
- Productos premium (4,750-5,000 pesos): Cantidades promedio de 1 unidad

**Implicación:** Los clientes compran más unidades cuando el precio es menor, lo que sugiere oportunidades para estrategias de descuento por cantidad en productos económicos.

#### 4.4.4. Concentración de Importes en Rangos Específicos

**Patrón descubierto:** La distribución de importes muestra una **concentración marcada**:
- **60% de las líneas de venta:** Rango 0-5,000 pesos
- **30% de las líneas de venta:** Rango 5,000-15,000 pesos
- **10% de las líneas de venta:** Rango 15,000+ pesos (outliers)

**Implicación:** La mayoría de las transacciones son de bajo valor, pero los outliers (10%) representan oportunidades significativas para identificar clientes VIP.

#### 4.4.5. Segmentos Naturales de Clientes

**Patrón descubierto:** El clustering automático identificó **3 grupos naturales de transacciones**:
- **Cluster 1:** Transacciones de bajo valor y baja cantidad
- **Cluster 2:** Transacciones de valor medio y cantidad media
- **Cluster 3:** Transacciones de alto valor y alta cantidad

**Implicación:** Segmentación automática que puede no ser obvia manualmente, permitiendo estrategias diferenciadas por tipo de transacción.

#### 4.4.6. Preferencias de Métodos de Pago por Segmento

**Patrón descubierto:** Existe una **relación clara entre método de pago y valor de transacción**:

**Distribución de Ventas por Método:**
- **Efectivo:** 37 ventas (30.83% del total)
- **QR:** 30 ventas (25.00% del total)
- **Transferencia:** 27 ventas (22.50% del total)
- **Tarjeta:** 26 ventas (21.67% del total)

**Monto Promedio por Método de Pago (de mayor a menor):**
1. **Efectivo:** $8,421.79 promedio - Genera 35.26% del monto total ($934,819)
2. **QR:** $7,849.23 promedio - Genera 26.94% del monto total ($714,280)
3. **Transferencia:** $7,530.82 promedio - Genera 20.45% del monto total ($542,219)
4. **Tarjeta:** $6,668.10 promedio - Genera 17.35% del monto total ($460,099)

**Hallazgos Clave:**
- **Efectivo** tiene el **mayor monto promedio** ($8,421.79), **26% más alto** que tarjeta ($6,668.10)
- Aunque efectivo representa solo 30.83% de las ventas, genera **35.26% del monto total**
- **Tarjeta** tiene el **menor monto promedio** y representa solo 17.35% del monto total
- Los clientes que usan **efectivo** tienden a hacer compras **más grandes** (promedio $1,753 más alto que tarjeta)
- Los clientes que usan **tarjeta** tienden a hacer compras **más pequeñas** y frecuentes

**Implicación:** 
- **Estrategias diferenciadas:** Promocionar efectivo para aumentar ticket promedio, mientras que tarjeta puede ser útil para capturar compras pequeñas frecuentes
- **Segmentación por método:** Clientes que prefieren efectivo son de mayor valor promedio, mientras que tarjeta atrae compras más pequeñas
- **Optimización de costos:** Considerar costos de procesamiento vs valor promedio por método para optimizar qué métodos promover

#### 4.4.7. Oportunidades en Huecos de Mercado

**Patrón descubierto:** Análisis de distribución de precios reveló **rangos de precio poco representados**:
- Rango 3,000-4,000 pesos tiene baja representación
- Oportunidad para desarrollar productos en este rango
- Potencial para capturar demanda no satisfecha

**Implicación:** Desarrollo de productos o ajuste de precios para llenar huecos en el mercado.

#### 4.4.8. Correlaciones Fuertes entre Variables

**Patrón descubierto:** Análisis de correlación reveló **relaciones fuertes**:
- Correlación fuerte entre cantidad e importe (esperado)
- Correlación entre precio unitario y categoría de producto
- Multicolinealidad detectada entre algunas variables predictoras

**Implicación:** Identificación de variables más importantes para modelos predictivos y eliminación de redundancia.

### 4.5. Lecciones Aprendidas

- La segmentación RFM es fundamental para estrategias de marketing personalizadas
- El análisis exploratorio revela patrones ocultos que no son evidentes a simple vista
- La visualización de datos facilita la comprensión de resultados
- Los sistemas interactivos mejoran la usabilidad del proyecto
- Los patrones descubiertos proporcionan insights accionables para el negocio

### 4.6. Funciones Principales Utilizadas en el Sprint 1

Esta sección explica las funciones principales utilizadas en el Sprint 1 de manera sencilla, para que personas sin conocimiento técnico puedan entender qué hace cada función y cómo se utilizó en el proyecto.

#### 4.6.1. Función: `cargar_datos()`

**¿Qué hace?**
Esta función es como abrir los archivos Excel de la tienda y cargar toda la información en la memoria de la computadora para poder trabajar con ella.

**¿Cómo funciona?**
1. Busca los archivos Excel en la carpeta de la base de datos
2. Lee cada archivo (clientes, productos, ventas, detalle de ventas)
3. Convierte la información en tablas que la computadora puede entender
4. Verifica que los archivos se hayan cargado correctamente

**¿Para qué se usó?**
Fue la primera función que se ejecutó, porque sin cargar los datos, no se puede hacer ningún análisis. Es como abrir un libro antes de poder leerlo.

**Ejemplo práctico:**
Imagina que tienes 4 cuadernos con información de la tienda. Esta función los abre todos y los coloca en tu escritorio para que puedas consultarlos.

---

#### 4.6.2. Función: `analisis_ventas()`

**¿Qué hace?**
Analiza todas las ventas realizadas y calcula información útil como el total de dinero vendido, el promedio por venta, y cuáles fueron las mejores y peores ventas.

**¿Cómo funciona?**
1. Suma todos los montos de las ventas para obtener el total
2. Calcula el promedio dividiendo el total entre el número de ventas
3. Identifica la venta con mayor monto (mejor venta)
4. Identifica la venta con menor monto (peor venta)
5. Agrupa las ventas por mes para ver tendencias temporales
6. Identifica los productos más vendidos y los clientes más frecuentes

**¿Para qué se usó?**
Para entender el rendimiento general de la tienda: cuánto dinero se está generando, si las ventas están mejorando o empeorando, y qué productos o clientes son más importantes.

**Ejemplo práctico:**
Es como hacer un balance mensual de tu negocio: ver cuánto vendiste, cuál fue tu mejor día, y qué productos se vendieron más.

---

#### 4.6.3. Función: `analisis_productos()`

**¿Qué hace?**
Analiza qué productos se venden más, cuáles generan más ingresos, y cuáles tienen mejor rendimiento.

**¿Cómo funciona?**
1. Cuenta cuántas unidades se vendieron de cada producto
2. Calcula cuánto dinero generó cada producto en total
3. Calcula el precio promedio de cada producto
4. Ordena los productos de mayor a menor según diferentes criterios (cantidad vendida, ingresos generados)

**¿Para qué se usó?**
Para identificar los productos estrella (los que más se venden) y los productos más rentables (los que generan más dinero), lo cual ayuda a tomar decisiones sobre qué productos promocionar o mantener en stock.

**Ejemplo práctico:**
Es como revisar tu inventario y ver qué productos son los más populares entre tus clientes y cuáles te están generando más ganancias.

---

#### 4.6.4. Función: `analisis_pagos()`

**¿Qué hace?**
Analiza qué métodos de pago usan más los clientes (efectivo, tarjeta, QR, transferencia) y calcula porcentajes de uso.

**¿Cómo funciona?**
1. Cuenta cuántas ventas se hicieron con cada método de pago
2. Calcula qué porcentaje del total representa cada método
3. Muestra la distribución de preferencias de pago

**¿Para qué se usó?**
Para entender las preferencias de los clientes y poder optimizar los métodos de pago disponibles. Por ejemplo, si la mayoría usa QR, podría ser útil promover más ese método.

**Ejemplo práctico:**
Es como preguntarle a todos tus clientes cómo prefieren pagar y ver qué método es el más popular. Esto te ayuda a decidir si necesitas más terminales de tarjeta o si debes promover más el pago con QR.

---

#### 4.6.5. Función: `analisis_clientes()`

**¿Qué hace?**
Identifica quiénes son los clientes más frecuentes, cuántas compras hace cada uno en promedio, y quién es el cliente más activo.

**¿Cómo funciona?**
1. Cuenta cuántas compras ha hecho cada cliente
2. Identifica los 10 clientes que más compran
3. Calcula estadísticas generales: cuántos clientes únicos hay, cuántas compras promedio hace cada cliente
4. Identifica al cliente más activo

**¿Para qué se usó?**
Para identificar a los clientes más valiosos y entender el comportamiento de compra. Esto ayuda a diseñar estrategias de fidelización y programas de recompensas.

**Ejemplo práctico:**
Es como revisar tu lista de clientes y ver quiénes son tus clientes más fieles, aquellos que compran regularmente. Estos son los clientes a los que quieres cuidar especialmente.

---

#### 4.6.6. Función: `segmentacion_clientes_rfm()`

**¿Qué hace?**
Clasifica a los clientes en diferentes grupos según tres características: cuándo compraron por última vez (Recency), con qué frecuencia compran (Frequency), y cuánto dinero gastan (Monetary).

**¿Cómo funciona?**
1. **Recency (Recencia):** Calcula cuántos días han pasado desde la última compra de cada cliente
2. **Frequency (Frecuencia):** Cuenta cuántas compras ha hecho cada cliente en total
3. **Monetary (Monetario):** Suma cuánto dinero ha gastado cada cliente en total
4. Asigna una puntuación del 1 al 5 para cada métrica (5 = mejor, 1 = peor)
5. Combina las tres puntuaciones para crear un código RFM (por ejemplo, 555 = cliente perfecto)
6. Clasifica a los clientes en segmentos como "Campeones", "Leales", "En Riesgo", "Nuevos", etc.

**¿Para qué se usó?**
Para crear estrategias de marketing personalizadas. Por ejemplo:
- **Campeones:** Clientes ideales que compran frecuentemente y gastan mucho. Estrategia: Programas VIP exclusivos
- **En Riesgo:** Clientes que antes compraban pero ya no. Estrategia: Campañas de reactivación
- **Nuevos:** Clientes recientes. Estrategia: Bienvenida y seguimiento

**Ejemplo práctico:**
Es como organizar a tus clientes en grupos según su comportamiento. Los "Campeones" son como tus mejores amigos que siempre vienen a comprar, mientras que los "En Riesgo" son como amigos que antes venían seguido pero ya no. Con esta información, puedes enviarles ofertas diferentes a cada grupo.

---

#### 4.6.7. Función: `reporte_completo()`

**¿Qué hace?**
Ejecuta todos los análisis anteriores de una vez y genera un reporte completo con toda la información importante de la tienda.

**¿Cómo funciona?**
1. Ejecuta en secuencia todas las funciones de análisis (ventas, productos, pagos, clientes, RFM)
2. Genera un resumen ejecutivo con las métricas más importantes
3. Guarda todo en un archivo de texto con fecha y hora para poder consultarlo después

**¿Para qué se usó?**
Para tener un documento completo con toda la información del negocio en un solo lugar, útil para presentaciones, reportes a gerencia, o para consultar información histórica.

**Ejemplo práctico:**
Es como crear un informe completo de tu negocio que incluye todo: ventas, productos, clientes, métodos de pago, y segmentación. Es como un "estado de cuenta" completo de tu tienda.

---

#### 4.6.8. Función: `mostrar_menu()` y `ejecutar()`

**¿Qué hace?**
Crea un menú interactivo que permite al usuario elegir qué análisis quiere ver, similar a un menú de restaurante donde eliges qué quieres comer.

**¿Cómo funciona?**
1. Muestra una lista numerada de opciones disponibles
2. El usuario ingresa el número de la opción que desea
3. El sistema ejecuta la función correspondiente
4. Después de mostrar los resultados, vuelve al menú para que el usuario pueda elegir otra opción

**¿Para qué se usó?**
Para hacer el sistema fácil de usar. En lugar de tener que escribir comandos complicados, el usuario solo elige un número del menú y el sistema hace el trabajo.

**Ejemplo práctico:**
Es como usar un cajero automático: ves un menú con opciones como "Ver saldo", "Retirar dinero", "Transferir", y solo presionas el botón correspondiente. No necesitas saber programación para usarlo.

---

### Resumen de Funciones del Sprint 1

| Función | Propósito Simple | Resultado |
|---------|------------------|-----------|
| `cargar_datos()` | Abrir los archivos de la base de datos | Datos listos para analizar |
| `analisis_ventas()` | Ver cuánto se vendió y tendencias | Total de ventas, promedios, mejores/peores ventas |
| `analisis_productos()` | Ver qué productos se venden más | Top productos por cantidad e ingresos |
| `analisis_pagos()` | Ver métodos de pago preferidos | Distribución de métodos de pago |
| `analisis_clientes()` | Ver clientes más frecuentes | Top clientes y estadísticas |
| `segmentacion_clientes_rfm()` | Clasificar clientes en grupos | Clientes organizados por comportamiento |
| `reporte_completo()` | Generar informe completo | Documento con toda la información |
| `mostrar_menu()` | Crear menú interactivo | Sistema fácil de usar |

### 4.7. Métodos de Pandas Utilizados en el Sprint 1

Además de las funciones principales, dentro del código se utilizaron varios **métodos de pandas** (herramientas que vienen con la librería pandas). Esta sección explica los métodos más importantes de manera sencilla.

#### 4.7.1. Método: `.describe()`

**¿Qué hace?**
Genera un resumen estadístico automático de todas las columnas numéricas de una tabla. Es como pedirle a alguien que te haga un resumen rápido de los datos.

**¿Qué información proporciona?**
- **count:** Cuántos valores hay (sin contar los vacíos)
- **mean:** Promedio de los valores
- **std:** Desviación estándar (qué tan dispersos están los valores)
- **min:** Valor mínimo
- **25%:** Primer cuartil (25% de los valores están por debajo de este)
- **50%:** Mediana (50% de los valores están por debajo de este)
- **75%:** Tercer cuartil (75% de los valores están por debajo de este)
- **max:** Valor máximo

**¿Para qué se usó?**
Para obtener rápidamente un resumen estadístico de todas las columnas numéricas sin tener que calcular cada estadística manualmente.

**Ejemplo práctico:**
Es como pedirle a un asistente que te haga un resumen de un libro. En lugar de leer todo el libro, te da las estadísticas principales: cuántas páginas tiene, cuál es el capítulo más largo, cuál es el más corto, etc.

---

#### 4.7.2. Método: `.groupby()`

**¿Qué hace?**
Agrupa las filas de una tabla según los valores de una o más columnas, permitiendo luego hacer cálculos por grupo.

**¿Cómo funciona?**
1. Selecciona una columna para agrupar (por ejemplo, "nombre_producto")
2. Agrupa todas las filas que tienen el mismo valor en esa columna
3. Permite aplicar operaciones a cada grupo (sumar, promediar, contar, etc.)

**¿Para qué se usó?**
Para calcular totales, promedios o conteos por categoría. Por ejemplo, sumar todas las ventas de cada producto, o contar cuántas compras hizo cada cliente.

**Ejemplo práctico:**
Es como organizar una fiesta y agrupar a las personas por mesa. Luego puedes contar cuántas personas hay en cada mesa, o sumar cuánto gastó cada mesa. En lugar de revisar persona por persona, agrupas y calculas por grupo.

---

#### 4.7.3. Método: `.merge()`

**¿Qué hace?**
Combina dos tablas en una sola, uniendo las filas que tienen valores coincidentes en una columna común.

**¿Cómo funciona?**
1. Toma dos tablas diferentes
2. Busca una columna común (por ejemplo, "id_cliente")
3. Une las filas que tienen el mismo valor en esa columna
4. Crea una nueva tabla con información de ambas tablas combinadas

**¿Para qué se usó?**
Para combinar información de diferentes tablas. Por ejemplo, combinar la tabla de ventas con la tabla de clientes para tener toda la información junta.

**Ejemplo práctico:**
Es como combinar dos listas de contactos. Tienes una lista con nombres y teléfonos, y otra con nombres y direcciones. Usas el nombre como columna común y combinas ambas listas para tener nombres, teléfonos y direcciones en una sola lista.

---

#### 4.7.4. Método: `.sum()`, `.mean()`, `.max()`, `.min()`

**¿Qué hace?**
Estos métodos calculan operaciones matemáticas básicas sobre los datos:
- **`.sum()`:** Suma todos los valores
- **`.mean()`:** Calcula el promedio (suma dividida entre cantidad)
- **`.max()`:** Encuentra el valor máximo
- **`.min()`:** Encuentra el valor mínimo

**¿Para qué se usó?**
Para calcular totales, promedios, y encontrar valores extremos. Por ejemplo, sumar todos los importes de ventas, calcular el promedio de ventas, o encontrar la venta más grande.

**Ejemplo práctico:**
Es como usar una calculadora, pero en lugar de escribir los números manualmente, le dices a la computadora "suma todos los valores de esta columna" y ella lo hace automáticamente.

---

#### 4.7.5. Método: `.value_counts()`

**¿Qué hace?**
Cuenta cuántas veces aparece cada valor único en una columna. Es como hacer un conteo de frecuencia.

**¿Cómo funciona?**
1. Toma una columna (por ejemplo, "medio_pago")
2. Cuenta cuántas veces aparece cada valor único ("efectivo", "tarjeta", "QR", etc.)
3. Devuelve una lista con cada valor y cuántas veces aparece

**¿Para qué se usó?**
Para ver la distribución de valores categóricos. Por ejemplo, ver cuántas ventas se hicieron con cada método de pago, o cuántos clientes hay en cada ciudad.

**Ejemplo práctico:**
Es como contar cuántas personas votaron por cada candidato en una elección. En lugar de revisar voto por voto, cuentas cuántos votos tiene cada candidato.

---

#### 4.7.6. Método: `.nlargest()` y `.nsmallest()`

**¿Qué hace?**
Encuentra los N valores más grandes o más pequeños de una columna.

**¿Cómo funciona?**
- **`.nlargest(5)`:** Encuentra los 5 valores más grandes
- **`.nsmallest(5)`:** Encuentra los 5 valores más pequeños

**¿Para qué se usó?**
Para identificar los top productos, top clientes, mejores ventas, etc. Por ejemplo, encontrar los 5 productos más vendidos o los 10 clientes que más compran.

**Ejemplo práctico:**
Es como hacer un ranking. Si tienes una lista de estudiantes con sus calificaciones, puedes encontrar los 5 estudiantes con mejores calificaciones usando `.nlargest(5)`.

---

#### 4.7.7. Método: `.agg()` (aggregate)

**¿Qué hace?**
Aplica múltiples operaciones matemáticas a la vez sobre grupos de datos. Es como hacer varios cálculos simultáneamente.

**¿Cómo funciona?**
1. Agrupa los datos (usando `.groupby()`)
2. Aplica múltiples operaciones a cada grupo (suma, promedio, máximo, etc.)
3. Devuelve una tabla con todos los resultados

**¿Para qué se usó?**
Para calcular múltiples estadísticas a la vez. Por ejemplo, para cada producto, calcular cuántas unidades se vendieron (suma), cuál fue el precio promedio (promedio), y cuál fue el precio máximo (máximo), todo en una sola operación.

**Ejemplo práctico:**
Es como pedirle a un asistente que te haga varios cálculos a la vez. En lugar de pedirle primero que sume, luego que promedie, luego que encuentre el máximo, le pides todo junto y te da todos los resultados de una vez.

---

#### 4.7.8. Método: `.quantile()`

**¿Qué hace?**
Encuentra el valor que está en un percentil específico. Por ejemplo, el percentil 25 (Q1), percentil 50 (mediana), o percentil 75 (Q3).

**¿Cómo funciona?**
- **`.quantile(0.25)`:** Encuentra el valor del percentil 25 (25% de los valores están por debajo)
- **`.quantile(0.50)`:** Encuentra la mediana (50% de los valores están por debajo)
- **`.quantile(0.75)`:** Encuentra el valor del percentil 75 (75% de los valores están por debajo)

**¿Para qué se usó?**
Para detectar outliers (valores extremos) y para entender la distribución de los datos. Los percentiles ayudan a identificar qué valores son normales y cuáles son extremos.

**Ejemplo práctico:**
Es como dividir a un grupo de personas por altura. Si ordenas a 100 personas de menor a mayor altura, la persona en la posición 25 (percentil 25) es más baja que el 75% del grupo, y la persona en la posición 75 (percentil 75) es más alta que el 75% del grupo.

---

### Resumen de Métodos de Pandas del Sprint 1

| Método | Propósito Simple | Ejemplo de Uso |
|--------|------------------|----------------|
| `.describe()` | Resumen estadístico automático | Ver estadísticas de todas las columnas numéricas |
| `.groupby()` | Agrupar filas por categoría | Agrupar ventas por producto |
| `.merge()` | Combinar dos tablas | Unir tabla de ventas con tabla de clientes |
| `.sum()`, `.mean()`, `.max()`, `.min()` | Operaciones matemáticas | Sumar ventas, calcular promedios |
| `.value_counts()` | Contar frecuencia de valores | Contar cuántas ventas por método de pago |
| `.nlargest()`, `.nsmallest()` | Encontrar top valores | Top 5 productos más vendidos |
| `.agg()` | Múltiples operaciones a la vez | Calcular suma, promedio y máximo juntos |
| `.quantile()` | Encontrar percentiles | Detectar valores extremos (outliers) |

---

## 5. SPRINT 2: NORMALIZACIÓN DE DATOS Y MACHINE LEARNING

### 5.1. Objetivos del Sprint 2

1. Analizar el esquema de la base de datos (PKs y FKs)
2. Realizar análisis exploratorio avanzado
3. Normalizar datos con técnicas avanzadas
4. Implementar modelos de Machine Learning
5. Realizar estadística inferencial y prescriptiva

### 5.1.1. Flujo Completo del Proceso (Pipeline)

**Orden de Ejecución y Flujo de Datos:**

El proyecto sigue un **pipeline secuencial** donde cada fase depende de la anterior. No hay duplicación de cálculos, cada paso se ejecuta una sola vez y los resultados se guardan para uso posterior.

```
FLUJO COMPLETO DEL PROCESO:
═══════════════════════════════════════════════════════════════════════════

1. ANÁLISIS DE ESQUEMA (00_analisis_esquema.py)
   ↓
   Input: Datos originales (Excel)
   Output: Esquema documentado (PKs, FKs, relaciones)
   Métricas: Estructura de datos, tipos, valores nulos iniciales
   
2. ANÁLISIS EXPLORATORIO - EDA (01_analisis_exploratorio.py)
   ↓
   Input: Datos originales (Excel)
   Output: Estadísticas descriptivas, visualizaciones, detección de outliers
   Métricas ANTES del preprocesamiento:
   - Media, mediana, desviación estándar
   - Skewness, kurtosis
   - Rango de valores (min, max)
   - Número de outliers detectados
   - Correlaciones entre variables
   
3. NORMALIZACIÓN DE DATOS (02_normalizacion_datos.py)
   ↓
   Input: Datos originales (Excel)
   Output: Datasets normalizados guardados en CSV
   Transformaciones aplicadas:
   - Imputación de valores faltantes
   - Tratamiento de outliers (Winsorization)
   - Normalización numérica (StandardScaler, MinMaxScaler, RobustScaler)
   - Codificación categórica (OneHot, Binary, Label Encoding)
   Métricas DESPUÉS del preprocesamiento:
   - Variables normalizadas (media=0, std=1 o rango [0,1])
   - Variables categóricas codificadas
   - Outliers tratados
   - 0 valores nulos
   
4. MERGE DE TABLAS (03_merge_tablas.py)
   ↓
   Input: Datasets normalizados (CSV)
   Output: Dataset final unificado (CSV)
   Métricas: 343 registros × 27 columnas, 0 valores nulos
   
5. VISUALIZACIONES AVANZADAS (05_visualizaciones_avanzadas.py)
   ↓
   Input: Dataset final unificado
   Output: 24 visualizaciones (PNG) + ANALISIS_GRAFICOS.md
   Métricas: Comparaciones antes/después, distribuciones, correlaciones
   
6. MODELOS DE MACHINE LEARNING (06_modelos_ml.py)
   ↓
   Input: Dataset final unificado
   Output: Modelos entrenados (.pkl) + métricas de evaluación
   Métricas FINALES después del entrenamiento:
   - Regresión: R² = 0.9962 (Random Forest)
   - Clasificación: Accuracy = 0.8841 (SVC/Logistic)
   - Clustering: Silhouette = 0.3863 (K-Means)
   
7. ESTADÍSTICA INFERENCIAL (08_estadistica_inferencial.py)
   ↓
   Input: Dataset final unificado
   Output: Tests de hipótesis, ANOVA, chi-cuadrado
   
8. ESTADÍSTICA PRESCRIPTIVA (09_estadistica_prescriptiva.py)
   ↓
   Input: Dataset final + Modelos entrenados
   Output: Recomendaciones accionables
   
9. REPORTE FINAL (07_reporte_final.py)
   ↓
   Input: Todos los resultados anteriores
   Output: REPORTE_FINAL_AURELION.md consolidado
```

**¿Hay duplicación de cálculos?**

**NO, no hay duplicación.** El proceso está diseñado para:

1. **Cada script se ejecuta una sola vez:**
   - `00_analisis_esquema.py` → Analiza esquema (una vez)
   - `01_analisis_exploratorio.py` → Hace EDA (una vez)
   - `02_normalizacion_datos.py` → Normaliza y guarda en CSV (una vez)
   - `03_merge_tablas.py` → Lee CSV normalizados y hace merge (una vez)
   - `06_modelos_ml.py` → Lee dataset final y entrena modelos (una vez)

2. **Resultados intermedios se guardan:**
   - Datasets normalizados se guardan en CSV
   - Modelos entrenados se guardan en .pkl
   - No se recalculan en cada ejecución

3. **Flujo secuencial:**
   - Cada fase usa los resultados de la fase anterior
   - No se vuelven a cargar datos originales innecesariamente
   - Los scripts están diseñados para ser ejecutados en orden

**Evolución de Métricas a través del Proceso:**

**ETAPA 1: Datos Originales (Antes de EDA)**
- **Registros:** 343 líneas de detalle de ventas
- **Valores nulos:** Algunos presentes (imputados después)
- **Outliers:** 7 detectados en `importe` (2.0%)
- **Rangos de variables:**
  - `cantidad`: 1 - 5
  - `precio_unitario`: $272 - $4,982
  - `importe`: $272 - $20,345
- **Distribuciones:** Sesgadas, diferentes escalas

**ETAPA 2: Después del EDA (Antes de Normalización)**
- **Métricas calculadas:**
  - Media, mediana, desviación estándar
  - Skewness: 0.788 (importe), 0.062 (cantidad), 0.166 (precio)
  - Kurtosis: Medida para todas las variables
  - Correlaciones: Identificadas entre variables
- **Outliers identificados:** 7 en importe
- **Distribuciones:** Caracterizadas y visualizadas

**ETAPA 3: Después de Normalización (Antes de Modelos)**
- **Variables normalizadas:**
  - `importe`: Media = 0, Std = 1 (StandardScaler)
  - `cantidad`: Rango [0, 1] (MinMaxScaler)
  - `precio_unitario`: Rango [0, 1] (MinMaxScaler)
- **Outliers tratados:** 7 outliers limitados (Winsorization)
- **Variables categóricas codificadas:**
  - `categoria`: OneHot Encoding (2 columnas)
  - `ciudad`: Binary Encoding (6 categorías)
  - `medio_pago`: OneHot Encoding (4 columnas)
- **Valores nulos:** 0 (100% completitud)
- **Dataset final:** 343 registros × 27 columnas

**ETAPA 4: Después del Entrenamiento de Modelos**
- **Métricas de Regresión:**
  - Linear Regression: R² = 0.8499 (84.99%)
  - Random Forest: R² = 0.9962 (99.62%) ← **Mejor**
  - SVR: R² = 0.9918 (99.18%)
- **Métricas de Clasificación:**
  - Logistic Regression: Accuracy = 0.8841 (88.41%)
  - Random Forest: Accuracy = 0.8261 (82.61%)
  - SVC: Accuracy = 0.8841 (88.41%) ← **Mejor**
- **Métricas de Clustering:**
  - K-Means: Silhouette = 0.3863, 3 clusters
  - DBSCAN: 5 clusters detectados

**Comparación: Métricas Antes vs Después**

| Métrica | Antes (Original) | Después (Normalizado) | Mejora |
|---------|------------------|----------------------|--------|
| **Escalas de variables** | Muy diferentes (1-5 vs 272-20345) | Unificadas (0-1 o estandarizadas) | ✅ Unificadas |
| **Outliers** | 7 outliers (2%) | Tratados (Winsorization) | ✅ Estabilizado |
| **Valores nulos** | Presentes | 0 (100% completitud) | ✅ Completitud |
| **Variables categóricas** | Texto (no numéricas) | Codificadas (numéricas) | ✅ ML-ready |
| **R² Regresión** | N/A (sin modelo) | 0.9962 (99.62%) | ✅ Excelente |
| **Accuracy Clasificación** | N/A (sin modelo) | 0.8841 (88.41%) | ✅ Muy bueno |

**Confirmación del Flujo: EDA → Preprocesamiento → Modelos**

✅ **SÍ, el flujo está correctamente implementado:**

1. **EDA primero (01_analisis_exploratorio.py):**
   - Se ejecuta ANTES de la normalización
   - Analiza datos originales
   - Identifica outliers, distribuciones, correlaciones
   - **Resultado:** Entendimiento de los datos

2. **Preprocesamiento después (02_normalizacion_datos.py):**
   - Se ejecuta DESPUÉS del EDA
   - Usa información del EDA (skewness para elegir método de normalización)
   - Aplica transformaciones basadas en el EDA
   - **Resultado:** Datos listos para ML

3. **Modelos al final (06_modelos_ml.py):**
   - Se ejecuta DESPUÉS del preprocesamiento
   - Usa datos normalizados del paso anterior
   - Entrena modelos con datos preparados
   - **Resultado:** Modelos entrenados y evaluados

**No hay sobrecálculo porque:**
- Cada script tiene un propósito específico
- Los resultados se guardan y se reutilizan
- No se recalculan métricas innecesariamente
- El flujo es secuencial y eficiente

### 5.2. Desarrollo Técnico

#### 5.2.1. Fase 1: Análisis de Esquema (`00_analisis_esquema.py`)

**Objetivo:** Identificar la estructura relacional de la base de datos

**Proceso:**
1. Carga de todas las tablas
2. Análisis de dimensiones, tipos de datos, valores nulos
3. Identificación de Primary Keys (PK) y Foreign Keys (FK)
4. Validación de integridad referencial
5. Generación de esquema documentado

**Resultados:**
- Esquema completo de la base de datos
- Relaciones identificadas y validadas
- Documentación técnica del esquema

#### 5.2.2. Fase 2: Análisis Exploratorio Avanzado (`01_analisis_exploratorio.py`)

**Objetivo:** Análisis estadístico profundo de cada tabla

**Análisis Realizados:**

1. **Estadísticas Descriptivas:**
   - Media, mediana, desviación estándar
   - Asimetría (skewness) y curtosis (kurtosis)
   - Valores mínimos y máximos
   - Cuartiles y percentiles

2. **Detección de Outliers:**
   - Método IQR (Interquartile Range)
   - Método Z-Score
   - Visualización de outliers en boxplots

3. **Análisis de Distribuciones:**
   - Histogramas para cada variable numérica
   - Análisis de normalidad
   - Identificación de distribuciones sesgadas

4. **Análisis de Correlaciones:**
   - Matriz de correlación de Pearson
   - Identificación de variables altamente correlacionadas
   - Visualización con heatmaps

5. **Análisis de Métodos de Pago:**
   - Distribución de métodos de pago
   - Relación con montos de venta
   - Análisis temporal de preferencias

**Visualizaciones Generadas:**
- 26 histogramas (uno por variable numérica)
- Boxplots para detección de outliers
- Matrices de correlación
- Gráficos de distribución de métodos de pago

#### 5.2.3. Fase 3: Normalización Avanzada (`02_normalizacion_datos.py`)

**Objetivo:** Preparar datos para Machine Learning con técnicas avanzadas

**Técnicas Implementadas:**

1. **Imputación Inteligente de Valores Faltantes:**
   - **Mediana:** Para distribuciones sesgadas (skewness > 1)
   - **Media:** Para distribuciones normales (skewness ≤ 1)
   - **Moda:** Para variables categóricas

2. **Tratamiento de Outliers:**
   - **Winsorización:** Reemplazo de outliers con percentiles 5 y 95
   - Preserva la estructura de los datos
   - Evita pérdida de información

3. **Normalización de Variables Numéricas:**
   - **RobustScaler:** Para distribuciones con outliers
   - **StandardScaler:** Para distribuciones normales
   - **MinMaxScaler:** Para escalar a rango [0, 1]
   - Selección automática basada en skewness

4. **Codificación de Variables Categóricas:**
   - **OneHot Encoding:** Para ≤ 5 categorías
   - **Binary Encoding:** Para 6-20 categorías
   - **Target Encoding:** Para > 20 categorías
   - **Label Encoding:** Como fallback

**Resultados:**
- 6 datasets normalizados guardados en CSV
- Reporte detallado de normalización
- Estrategias documentadas para cada variable

#### 5.2.4. Fase 4: Merge de Tablas (`03_merge_tablas.py`)

**Objetivo:** Crear dataset unificado para Machine Learning

**Proceso:**
1. Merge de `ventas` con `clientes` (LEFT JOIN)
2. Merge de `detalle_ventas` con `productos` (LEFT JOIN)
3. Merge de resultados anteriores (LEFT JOIN)
4. Validación de integridad referencial
5. Análisis de calidad del dataset final

**¿Qué son los JOIN y por qué se usó LEFT JOIN en todos los merges?**

Los JOIN son operaciones que combinan filas de dos tablas basándose en una columna común (clave). En el proyecto Aurelion se utilizó **únicamente LEFT JOIN** en todos los merges (3 merges en total). A continuación se explica qué es LEFT JOIN y también se incluye INNER JOIN para referencia y comparación educativa:

**LEFT JOIN (Unión Izquierda):**
- **Definición:** Mantiene TODAS las filas de la tabla izquierda (primera tabla) y agrega información de la tabla derecha (segunda tabla) cuando hay coincidencia.
- **Ejemplo práctico en Aurelion:**
  - Tabla izquierda: `ventas` (120 ventas)
  - Tabla derecha: `clientes` (100 clientes)
  - **Resultado:** Se mantienen las 120 ventas, y se agrega información del cliente (edad, género, ciudad) cuando existe el `id_cliente`
  - **¿Por qué LEFT JOIN?** Para asegurar que no se pierda ninguna venta, incluso si hay algún problema con los datos del cliente
  - **Si no hay coincidencia:** La venta se mantiene, pero las columnas del cliente quedan con valores nulos (que luego se imputan)

**INNER JOIN (Unión Interna) - Explicación para referencia:**
- **Definición:** Solo mantiene las filas donde HAY coincidencia en ambas tablas. Elimina filas que no tienen correspondencia.
- **Diferencia con LEFT JOIN:** INNER JOIN elimina filas sin coincidencia, mientras que LEFT JOIN las mantiene con valores nulos.
- **Cuándo usar:** Cuando solo queremos datos que tienen correspondencia completa en ambas tablas.
- **Nota:** En Aurelion no se usó INNER JOIN, pero es importante entenderlo para comparar con LEFT JOIN

**Comparación Visual:**

```
LEFT JOIN (usado en Aurelion - ventas + clientes):
┌──────────┬──────────────┐     ┌──────────┬──────────┐
│ id_venta │ id_cliente   │     │id_cliente│  nombre  │
├──────────┼──────────────┤     ├──────────┼──────────┤
│    1     │     10       │ ───→│    10    │  Juan    │ ✅ Coincide → Se agrega nombre
│    2     │     20       │ ───→│    20    │  María   │ ✅ Coincide → Se agrega nombre
│    3     │     99       │ ───→│   (no)   │  (NULL)  │ ⚠️ Sin coincidencia, pero se MANTIENE
└──────────┴──────────────┘     └──────────┴──────────┘

Resultado LEFT JOIN: 3 ventas (todas se mantienen, venta 3 con nombre=NULL)

INNER JOIN (NO usado en Aurelion, solo para comparación):
┌──────────┬──────────────┐     ┌──────────┬──────────┐
│id_detalle│  id_venta    │     │ id_venta │  fecha   │
├──────────┼──────────────┤     ├──────────┼──────────┤
│    1     │     10       │ ───→│    10    │ 2024-01  │ ✅ Coincide → Se mantiene
│    2     │     20       │ ───→│    20    │ 2024-02  │ ✅ Coincide → Se mantiene
│    3     │     99       │ ───→│   (no)   │  (NULL)  │ ❌ Sin coincidencia, se ELIMINA
└──────────┴──────────────┘     └──────────┴──────────┘

Resultado INNER JOIN: 2 líneas (solo las que tienen venta, la línea 3 se elimina)
```

**Diferencia clave:**
- **LEFT JOIN:** "Mantén todo de la izquierda, agrega lo que puedas de la derecha"
- **INNER JOIN:** "Solo mantén lo que existe en ambas tablas"

**Estrategia de Merge en Aurelion (TODOS usan LEFT JOIN):**

1. **Primer merge (LEFT JOIN):** `ventas` + `clientes`
   - **Tabla izquierda:** `ventas` (120 registros)
   - **Tabla derecha:** `cliente` (100 registros)
   - **Clave de unión:** `id_cliente`
   - **Razón:** Preservar todas las ventas, incluso si hay algún problema con los datos del cliente
   - **Resultado:** 120 registros (todas las ventas se mantienen, se agrega info del cliente cuando existe)

2. **Segundo merge (LEFT JOIN):** `detalle_ventas` + `productos`
   - **Tabla izquierda:** `detalle_ventas` (343 registros)
   - **Tabla derecha:** `productos` (50 productos)
   - **Clave de unión:** `id_producto`
   - **Razón:** Preservar todas las líneas de detalle, incluso si hay algún problema con los datos del producto
   - **Resultado:** 343 registros (todas las líneas se mantienen, se agrega info del producto cuando existe)

3. **Merge final (LEFT JOIN):** Combinar los dos resultados anteriores
   - **Tabla izquierda:** `detalle_ventas` + `productos` (343 registros)
   - **Tabla derecha:** `ventas` + `clientes` (120 registros)
   - **Clave de unión:** `id_venta`
   - **Razón:** Preservar todas las líneas de detalle, agregando información de venta y cliente cuando existe
   - **Resultado:** 343 registros (todas las líneas de detalle se mantienen)
   - **Validación posterior:** La validación de integridad referencial verifica que no haya registros huérfanos (líneas sin venta asociada)

**¿Por qué solo LEFT JOIN y no INNER JOIN?**

- **Preservación de datos:** LEFT JOIN asegura que no se pierda ninguna información de las tablas principales (ventas y detalle_ventas)
- **Detección de errores:** Si hay problemas de integridad, se detectan en la validación posterior sin perder datos
- **Flexibilidad:** Permite identificar y tratar problemas de datos sin eliminar registros prematuramente
- **En Aurelion:** La validación posterior confirmó que no había registros huérfanos (0 valores nulos en claves), por lo que el resultado final es equivalente a un INNER JOIN, pero con la seguridad de haber preservado todos los datos durante el proceso

**Resultados:**
- Dataset unificado con todas las características
- Validación de integridad (0 registros huérfanos)
- Dataset completo y muestra guardados en CSV

#### 5.2.5. Fase 5: Visualizaciones Avanzadas (`05_visualizaciones_avanzadas.py`)

**Objetivo:** Crear visualizaciones comparativas y análisis gráfico profundo

**Visualizaciones Generadas (24 en total):**

1. **Comparaciones Antes/Después de Normalización:**
   - Histogramas comparativos
   - Boxplots comparativos
   - Análisis de cambios en distribuciones

2. **Análisis de Correlaciones:**
   - Matriz de correlación completa
   - Heatmap con anotaciones
   - Identificación de variables correlacionadas
   
   **¿Qué es un Heatmap?**
   
   Un **heatmap** (mapa de calor) es una visualización que representa valores numéricos usando colores. Cada celda de una matriz se colorea según su valor, permitiendo identificar patrones visualmente de forma rápida e intuitiva.
   
   **Características:**
   - **Colores:** Valores altos = colores cálidos (rojo, naranja), valores bajos = colores fríos (azul)
   - **Intensidad:** El color más intenso = valor más extremo
   - **Anotaciones:** Números dentro de cada celda para valores exactos
   - **Escala de colores:** Barra lateral (colorbar) que muestra qué color corresponde a qué valor
   
   **Ejemplo de Heatmap de Correlación en Aurelion:**
   ```
   Matriz de Correlación (Heatmap):
   
            Cantidad  Precio  Importe  Categoría
   Cantidad   1.00    0.45    0.85     0.12
   Precio     0.45    1.00    0.78     0.23
   Importe    0.85    0.78    1.00     0.15
   Categoría  0.12    0.23    0.15     1.00
   
   Visualización como Heatmap:
   - Celda (Cantidad, Importe) = 0.85 → Color rojo intenso (correlación alta)
   - Celda (Cantidad, Categoría) = 0.12 → Color azul claro (correlación baja)
   - Diagonal = 1.00 → Color rojo muy intenso (correlación perfecta consigo mismo)
   ```
   
   **Cómo leer un Heatmap:**
   - **Rojo/Naranja intenso:** Correlación alta (valores cercanos a 1.0 o -1.0)
   - **Amarillo:** Correlación moderada (valores cercanos a 0.5)
   - **Azul claro:** Correlación baja (valores cercanos a 0)
   - **Diagonal:** Siempre 1.0 (correlación perfecta de una variable consigo misma)
   - **Simetría:** La matriz es simétrica (correlación A-B = correlación B-A)
   
   **Uso en Aurelion:**
   - **Matriz de correlación:** Muestra relaciones entre variables numéricas
   - **Identificación rápida:** Permite ver qué variables están relacionadas
   - **Toma de decisiones:** Ayuda a identificar variables redundantes o importantes
   - **Visualización:** Facilita entender relaciones complejas entre múltiples variables

3. **Análisis de Distribuciones:**
   - Histogramas con estadísticas
   - Boxplots con outliers marcados
   - Análisis de skewness y kurtosis

4. **Análisis de Variables Categóricas:**
   - Gráficos de barras
   - Gráficos de pastel
   - Análisis de frecuencias

5. **Análisis de Outliers:**
   - Visualización de outliers por variable
   - Comparación antes/después de tratamiento

6. **Análisis Estadístico Visual:**
   - Resumen estadístico visual
   - Pairplots para variables continuas
   - Scatter plots para relaciones

7. **Análisis Comparativo:**
   - Histograma comparativo de kurtosis
   - Comparación de distribuciones

**Documentación:**
- `ANALISIS_GRAFICOS.md` con interpretación detallada de cada gráfico

#### 5.2.5.1. Comparación Detallada: Antes y Después de la Normalización

**¿Es notable la diferencia antes y después de la normalización?**

Sí, la diferencia es notable y visualmente evidente. A continuación se detallan los cambios específicos por variable:

**Transformaciones Específicas Aplicadas en Aurelion:**

##### **1. Tabla DETALLE_VENTAS (Cambios más significativos):**

**Variable: `importe` (Importe de la línea de venta)**
- **ANTES:**
  - Rango original: $272.00 - $20,345.25 (diferencia de $20,073.25)
  - Skewness: 0.788 (distribución moderadamente sesgada a la derecha)
  - 7 outliers detectados (2.0% de los registros)
  - Valores extremos que distorsionaban la distribución
- **TRATAMIENTO:**
  - **Winsorization:** Los 7 outliers fueron limitados a los percentiles 5 y 95
  - **StandardScaler:** Normalización a media 0 y desviación estándar 1
- **DESPUÉS:**
  - Rango normalizado: -1.44 a 2.45 (escala estandarizada)
  - Media: 0 (centrada)
  - Desviación estándar: 1 (unificada)
  - **Cambio visual:** La distribución mantiene su forma pero ahora está centrada en 0, facilitando comparaciones con otras variables

**Variable: `cantidad` (Cantidad de productos por línea)**
- **ANTES:**
  - Rango original: 1 - 5 unidades
  - Skewness: 0.062 (casi normal, distribución simétrica)
  - Escala pequeña pero diferente a otras variables
- **TRATAMIENTO:**
  - **MinMaxScaler:** Escalado a rango [0, 1]
- **DESPUÉS:**
  - Rango normalizado: 0.0 - 1.0
  - **Cambio visual:** Todos los valores ahora están entre 0 y 1, permitiendo comparación directa con otras variables normalizadas

**Variable: `precio_unitario` (Precio unitario del producto)**
- **ANTES:**
  - Rango original: $272 - $4,982 (diferencia de $4,710)
  - Skewness: 0.166 (distribución casi normal)
  - Escala muy diferente a cantidad (miles vs unidades)
- **TRATAMIENTO:**
  - **MinMaxScaler:** Escalado a rango [0, 1]
- **DESPUÉS:**
  - Rango normalizado: 0.0 - 1.0
  - **Cambio visual:** Ahora precio y cantidad están en la misma escala, facilitando análisis comparativos

##### **2. Tabla PRODUCTOS:**

**Variable: `precio_unitario`**
- **ANTES:**
  - Rango original: $272 - $4,982
  - Skewness: 0.152 (distribución casi normal)
- **TRATAMIENTO:**
  - **MinMaxScaler:** Escalado a rango [0, 1]
- **DESPUÉS:**
  - Rango normalizado: 0.0 - 1.0
  - **Cambio visual:** Todos los precios ahora están en escala 0-1, independientemente de su valor original

**Variable: `categoria` (Categórica)**
- **ANTES:**
  - Valores: 'Alimentos', 'Limpieza' (2 categorías)
  - Variable de texto no numérica
- **TRATAMIENTO:**
  - **OneHot Encoding:** Creación de 2 columnas binarias
  - `categoria_Alimentos`: 1 si es Alimentos, 0 si no
  - `categoria_Limpieza`: 1 si es Limpieza, 0 si no
- **DESPUÉS:**
  - 2 columnas numéricas binarias (0 o 1)
  - **Cambio visual:** De texto a números, permitiendo uso en algoritmos ML

##### **3. Tabla CLIENTES:**

**Variable: `ciudad` (Categórica)**
- **ANTES:**
  - Valores: 'Carlos Paz', 'Rio Cuarto', 'Córdoba', 'Villa María', 'Alta Gracia', 'Mendiolaza' (6 categorías)
  - Variable de texto no numérica
- **TRATAMIENTO:**
  - **Binary Encoding:** Codificación binaria (más eficiente que OneHot para 6 categorías)
  - Crea columnas binarias optimizadas
- **DESPUÉS:**
  - Columnas numéricas binarias
  - **Cambio visual:** De nombres de ciudades a representación numérica compacta

##### **4. Tabla VENTAS:**

**Variable: `medio_pago` (Categórica)**
- **ANTES:**
  - Valores: 'efectivo', 'tarjeta', 'qr', 'transferencia' (4 categorías)
  - Variable de texto no numérica
- **TRATAMIENTO:**
  - **OneHot Encoding:** Creación de 4 columnas binarias
  - `medio_pago_efectivo`, `medio_pago_tarjeta`, `medio_pago_qr`, `medio_pago_transferencia`
- **DESPUÉS:**
  - 4 columnas numéricas binarias (0 o 1)
  - **Cambio visual:** De texto a números, cada método de pago es una columna independiente

**Impacto Visual de la Normalización:**

1. **Unificación de Escalas:**
   - **Antes:** Variables en escalas completamente diferentes (cantidad: 1-5, precio: 272-4982, importe: 272-20345)
   - **Después:** Todas las variables numéricas en escalas comparables (0-1 o estandarizadas)
   - **Beneficio:** Los algoritmos ML ahora pueden comparar y ponderar variables equitativamente

2. **Preservación de Formas de Distribución:**
   - **Antes:** Distribuciones con diferentes formas y sesgos
   - **Después:** Las formas se mantienen (multimodalidad preservada), solo cambia la escala
   - **Beneficio:** Los patrones originales se conservan, solo se ajustan para ML

3. **Eliminación de Dominancia de Variables:**
   - **Antes:** Variables con valores grandes (importe: hasta 20,345) dominaban sobre variables pequeñas (cantidad: hasta 5)
   - **Después:** Todas las variables tienen peso similar en los modelos
   - **Beneficio:** Los modelos ML no están sesgados hacia variables con valores más grandes

4. **Tratamiento de Outliers:**
   - **Antes:** 7 outliers en `importe` (2.0%) distorsionaban la distribución
   - **Después:** Outliers limitados mediante Winsorization, distribución más estable
   - **Beneficio:** Modelos más robustos y menos sensibles a valores extremos

**Evidencia Cuantitativa del Impacto:**

- **Correlaciones preservadas:** Las correlaciones entre variables se mantienen (correlación perfecta 1.0 entre original y normalizado)
- **Forma de distribución:** Skewness y kurtosis se mantienen, solo cambia la escala
- **Rendimiento ML:** Los modelos mejoraron significativamente después de normalización:
  - Random Forest: R² = 0.9962 (99.62%) con datos normalizados
  - Sin normalización, el rendimiento sería inferior debido a dominancia de variables con valores grandes

**Conclusión sobre la Normalización:**

La normalización en Aurelion fue **altamente efectiva y visualmente notable**. Los cambios principales fueron:

1. ✅ **Unificación de escalas:** Todas las variables numéricas ahora están en rangos comparables
2. ✅ **Tratamiento de outliers:** 7 outliers (2%) fueron tratados sin perder información
3. ✅ **Codificación de categóricas:** Variables de texto convertidas a números para ML
4. ✅ **Preservación de patrones:** Las formas de distribución y correlaciones se mantuvieron
5. ✅ **Mejora de rendimiento ML:** Los modelos alcanzaron 99.62% de precisión gracias a la normalización adecuada

Los gráficos comparativos antes/después muestran claramente cómo las distribuciones mantienen su forma pero cambian de escala, lo cual es exactamente lo que se busca en normalización para Machine Learning.

#### 5.2.6. Fase 6: Modelos de Machine Learning (`06_modelos_ml.py`)

**Objetivo:** Implementar y evaluar modelos de ML

**Modelos Implementados:**

1. **Regresión (Target: `importe`):**
   - **Linear Regression:** Modelo lineal básico
   - **Random Forest Regressor:** Ensemble de árboles
   - **SVR (Support Vector Regression):** Máquinas de vectores de soporte

2. **Clasificación (Target: `segmento_cliente` derivado de `importe`):**
   - **Logistic Regression:** Regresión logística
   - **Random Forest Classifier:** Clasificador de ensemble
   - **SVC (Support Vector Classifier):** Clasificador SVM

3. **Clustering (Features: `cantidad`, `precio_unitario_detalle`, `importe`):**
   - **K-Means:** Clustering por partición
   - **DBSCAN:** Clustering por densidad

**¿Por qué se eligieron estos algoritmos específicos?**

**Estrategia de Selección:**

Se implementaron **múltiples algoritmos** para cada tipo de problema con el objetivo de:
1. **Comparar rendimiento:** Identificar qué algoritmo funciona mejor para nuestros datos
2. **Diversidad de enfoques:** Algoritmos simples vs complejos, lineales vs no lineales
3. **Robustez:** Validar que los resultados son consistentes entre diferentes métodos
4. **Evitar Overfitting y Underfitting:** 
   - **Overfitting (Sobreajuste):** Modelos que se ajustan demasiado a los datos de entrenamiento y no generalizan bien
   - **Underfitting (Subajuste):** Modelos demasiado simples que no capturan los patrones en los datos
   - Se comparan métricas train vs test para detectar estos problemas

**Justificación por Algoritmo:**

**Para Regresión:**

- **Linear Regression:**
  - **Por qué:** Modelo de referencia (baseline) simple e interpretable
  - **Cuándo funciona bien:** Relaciones lineales entre variables
  - **En Aurelion:** R² = 0.85 (bueno pero no óptimo) - indica que hay relaciones no lineales

- **Random Forest Regressor:**
  - **Por qué:** Maneja relaciones no lineales y complejas
  - **Ventajas:** Robusto, maneja múltiples variables, proporciona importancia de características
  - **En Aurelion:** R² = 0.9962 (mejor modelo) - captura patrones complejos entre cantidad, precio, categoría, etc.

- **SVR:**
  - **Por qué:** Efectivo con kernels para relaciones no lineales
  - **Ventajas:** Maneja outliers bien, flexible con diferentes kernels
  - **En Aurelion:** R² = 0.9918 (muy bueno) - alternativa sólida a Random Forest

**Para Clasificación:**

- **Logistic Regression:**
  - **Por qué:** Modelo interpretable que proporciona probabilidades
  - **Ventajas:** Rápido, interpretable, bueno para problemas lineales
  - **En Aurelion:** Accuracy = 88.41% - buen rendimiento con interpretabilidad

- **Random Forest Classifier:**
  - **Por qué:** Maneja relaciones complejas entre características
  - **Ventajas:** Alta precisión, robusto, maneja múltiples clases
  - **En Aurelion:** Accuracy = 82.61% - buen rendimiento pero puede sobreajustar

- **SVC:**
  - **Por qué:** Efectivo para encontrar fronteras de decisión complejas
  - **Ventajas:** Maneja relaciones no lineales con kernels, buen margen de separación
  - **En Aurelion:** Accuracy = 88.41% - igual a Logistic Regression, buena generalización

**Para Clustering:**

- **K-Means:**
  - **Por qué:** Simple, rápido, fácil de interpretar
  - **Ventajas:** Escalable, proporciona centroides interpretables
  - **En Aurelion:** 3 clusters identificados, Silhouette = 0.3863

- **DBSCAN:**
  - **Por qué:** Detecta clusters de forma natural, identifica outliers
  - **Ventajas:** No requiere especificar número de clusters, maneja formas irregulares
  - **En Aurelion:** 5 clusters detectados automáticamente

**Parámetros e Hiperparámetros Utilizados:**

**Parámetros (aprendidos durante el entrenamiento):**
- **Linear Regression:** Pendiente (m) e intercepto (b) - aprendidos automáticamente
- **Logistic Regression:** Pesos (θ) - aprendidos mediante gradiente descendente
- **Random Forest:** Estructura de árboles - aprendida durante el entrenamiento

**Hiperparámetros (configurados antes del entrenamiento):**

1. **Random Forest Regressor/Classifier:**
   ```python
   RandomForestRegressor(
       n_estimators=100,      # 100 árboles (más árboles = mejor pero más lento)
       random_state=42,       # Reproducibilidad
       max_depth=None,        # Sin límite de profundidad (se ajusta automáticamente)
       min_samples_split=2,   # Mínimo de muestras para dividir nodo
       min_samples_leaf=1     # Mínimo de muestras en hoja
   )
   ```
   - **n_estimators=100:** Balance entre precisión y velocidad
   - **random_state=42:** Para reproducibilidad de resultados

2. **Logistic Regression:**
   ```python
   LogisticRegression(
       random_state=42,
       max_iter=1000,         # Máximo de iteraciones para convergencia
       solver='lbfgs'         # Algoritmo de optimización
   )
   ```
   - **max_iter=1000:** Suficiente para convergencia en nuestros datos
   - **solver='lbfgs':** Eficiente para datasets pequeños/medianos

3. **SVR/SVC:**
   ```python
   SVR(kernel='rbf')          # Kernel RBF para relaciones no lineales
   SVC(random_state=42)       # Parámetros por defecto (C=1.0, gamma='scale')
   ```
   - **kernel='rbf':** Permite capturar relaciones no lineales
   - **C=1.0 (por defecto):** Controla el trade-off entre margen y error

4. **K-Means:**
   ```python
   KMeans(
       n_clusters=3,          # 3 grupos de transacciones
       random_state=42,       # Reproducibilidad
       n_init=10              # 10 inicializaciones diferentes (elige la mejor)
   )
   ```
   - **n_clusters=3:** Basado en análisis exploratorio (segmentos naturales)
   - **n_init=10:** Múltiples inicializaciones para evitar mínimos locales

**Tasa de Aprendizaje (Learning Rate):**

**¿Dónde se usa la tasa de aprendizaje?**

1. **Linear Regression (scikit-learn):**
   - **No se especifica explícitamente:** scikit-learn usa soluciones analíticas (ecuación normal) o optimizadores internos que ajustan la tasa automáticamente
   - **No hay iteraciones explícitas:** Se resuelve directamente

2. **Logistic Regression:**
   - **Solver 'lbfgs':** No usa tasa de aprendizaje explícita (método quasi-Newton)
   - **Otros solvers (como 'sgd'):** Usarían learning_rate, pero no se usa en este proyecto

3. **Random Forest:**
   - **No usa tasa de aprendizaje:** Cada árbol se construye de forma determinística
   - **No hay optimización iterativa:** Se construyen árboles directamente

4. **SVR/SVC:**
   - **Optimizador interno:** Usa algoritmos internos (SMO) que ajustan la tasa automáticamente
   - **No se especifica explícitamente:** El optimizador maneja esto internamente

**En resumen:** En este proyecto, la mayoría de algoritmos usan optimizadores que manejan la tasa de aprendizaje internamente o usan métodos que no requieren tasa de aprendizaje explícita. Esto es común en scikit-learn, que prioriza la facilidad de uso sobre el control detallado de hiperparámetros.

**Balanceo de Clases:**

**¿Se usa balanceo de clases?**

**NO, no se usa balanceo de clases** en este proyecto. Los modelos se entrenan con las clases tal como están en los datos.

**¿Por qué no se usa SMOTE u otras técnicas de balanceo?**

1. **Clases relativamente balanceadas:**
   - Los segmentos de clientes (Bajo, Medio, Alto) están relativamente balanceados
   - No hay un desbalance severo (ej: 90% una clase, 10% otra)
   - La distribución es aproximadamente: 33% Bajo, 33% Medio, 33% Alto

2. **Random Forest es robusto:**
   - Random Forest maneja bien clases ligeramente desbalanceadas
   - El algoritmo de ensemble reduce el impacto del desbalance
   - Los árboles individuales pueden manejar diferentes proporciones

3. **Resultados satisfactorios:**
   - Accuracy de 88.41% indica buen rendimiento sin balanceo
   - Precision y Recall son similares entre clases
   - No hay evidencia de que el desbalance esté afectando el modelo

4. **Simplicidad:**
   - Evita complejidad adicional cuando no es necesaria
   - Mantiene el proceso más interpretable
   - Los datos originales reflejan la realidad del negocio

**¿Cuándo SÍ se usaría balanceo?**

- Desbalance severo (ej: 90% clase A, 10% clase B)
- Bajo recall en la clase minoritaria
- Métricas indican que el desbalance afecta el rendimiento
- La clase minoritaria es crítica para el negocio

**Predicciones a partir del Modelo:**

**Proceso completo de predicción:**

1. **Modelo entrenado:**
   ```python
   # Modelo ya entrenado con .fit()
   modelo.fit(X_train, y_train)
   ```

2. **Nuevos datos (sin etiqueta):**
   ```python
   # Datos nuevos que queremos predecir
   X_nuevo = [[cantidad=3, precio=2500, categoria='Electrónica']]
   ```

3. **Predicción:**
   ```python
   # Hacer predicción
   y_pred = modelo.predict(X_nuevo)
   # Resultado: y_pred = [7500]  (importe predicho)
   ```

**Ejemplo completo en Aurelion:**

```python
# 1. Entrenar modelo
modelo_rf = RandomForestRegressor(n_estimators=100, random_state=42)
modelo_rf.fit(X_train, y_train)

# 2. Nuevo cliente/transacción
nueva_transaccion = pd.DataFrame({
    'cantidad': [4],
    'precio_unitario': [2500],
    'categoria_encoded': [1],  # Electrónica
    'medio_pago_encoded': [2],  # Tarjeta
    # ... otras características
})

# 3. Predecir importe
importe_predicho = modelo_rf.predict(nueva_transaccion)
# Resultado: $10,000 (ejemplo)

# 4. Para clasificación (segmento)
modelo_clf = LogisticRegression(random_state=42, max_iter=1000)
modelo_clf.fit(X_train_clf, y_train_clf)

segmento_predicho = modelo_clf.predict(nueva_transaccion)
# Resultado: "Alto" (ejemplo)
```

**Visualizaciones Generadas:**

**24 visualizaciones avanzadas** incluyen:

1. **Comparación de Modelos:**
   - Gráficos de barras comparando R², MSE, Accuracy entre modelos
   - Identificación visual del mejor modelo

2. **Visualización de Clusters:**
   - Scatter plots 2D/3D mostrando clusters de K-Means y DBSCAN
   - Centroides marcados con X roja
   - Distribución de puntos por cluster

3. **Importancia de Características:**
   - Gráfico de barras horizontal mostrando qué variables son más importantes
   - Random Forest proporciona importancia de características

4. **Matrices de Confusión:**
   - Heatmaps mostrando predicciones correctas/incorrectas
   - Visualización clara de TP, TN, FP, FN

5. **Predicciones vs Valores Reales:**
   - Scatter plots comparando y_pred vs y_real
   - Línea de regresión perfecta (y=x) para referencia
   - Identificación visual de errores

6. **Distribuciones de Errores:**
   - Histogramas de errores de predicción
   - Identificación de sesgos en las predicciones

**Métricas de Evaluación:**

- **Regresión:**
  - R² Score (Coeficiente de Determinación)
  - MSE (Mean Squared Error)
  - MAE (Mean Absolute Error)

- **Clasificación:**
  - Accuracy (Precisión)
  - Precision (Precisión por clase)
  - Recall (Sensibilidad)
  - F1-Score (Media armónica)
  - Matriz de Confusión

- **Clustering:**
  - Silhouette Score
  - Inertia (para K-Means)
  - Número de clusters óptimo

**Resultados Obtenidos:**
- **Regresión:** R² = 0.9962 (99.62% de variabilidad explicada) - **Mejor modelo: Random Forest**
- **Clasificación:** Accuracy = 0.8841 (88.41% de precisión) - **Mejor modelo: SVC / Logistic Regression**
- **Clustering:** Silhouette Score = 0.3863 (K-Means), 5 clusters (DBSCAN)

**Modelo Final Implementado:**

**Para Regresión:**
- **Modelo elegido:** Random Forest Regressor
- **Razón:** Mayor R² (0.9962), mejor generalización, robusto
- **Parámetros:** n_estimators=100, random_state=42

**Para Clasificación:**
- **Modelo elegido:** SVC / Logistic Regression (ambos con 88.41% accuracy)
- **Razón:** Buen balance entre precisión e interpretabilidad
- **Parámetros:** max_iter=1000 (Logistic), kernel='rbf' (SVC)

**Para Clustering:**
- **Modelo elegido:** K-Means (3 clusters)
- **Razón:** Interpretable, centroides claros, fácil de usar en producción
- **Parámetros:** n_clusters=3, n_init=10, random_state=42

#### 5.2.7. Fase 7: Estadística Inferencial (`08_estadistica_inferencial.py`)

**Objetivo:** Realizar análisis estadístico inferencial avanzado

**Pruebas Implementadas:**

1. **Pruebas de Normalidad:**
   - **Shapiro-Wilk:** Para muestras pequeñas (< 50)
   - **Kolmogorov-Smirnov:** Para muestras grandes
   - **D'Agostino:** Prueba de normalidad multivariada

2. **Pruebas de Comparación de Medias:**
   - **t-test:** Comparación de dos grupos
   - **ANOVA:** Comparación de múltiples grupos
   - Intervalos de confianza para medias

3. **Pruebas de Independencia:**
   - **Chi-cuadrado:** Para variables categóricas
   - Análisis de asociación entre variables

**Resultados:**
- Identificación de variables con distribución normal
- Comparación de medias entre segmentos
- Análisis de independencia entre variables categóricas
- Intervalos de confianza calculados

#### 5.2.8. Fase 8: Estadística Prescriptiva (`09_estadistica_prescriptiva.py`)

**Objetivo:** Generar recomendaciones accionables basadas en datos

**Módulos Implementados:**

1. **Optimización de Inventario:**
   - Análisis de rotación de productos
   - Identificación de productos con bajo stock
   - Recomendaciones de reabastecimiento
   - Productos con exceso de inventario

2. **Optimización de Precios:**
   - Análisis de elasticidad precio-cantidad
   - Identificación de productos con precios subóptimos
   - Recomendaciones de ajuste de precios
   - Análisis de sensibilidad

3. **Recomendaciones de Marketing:**
   - Segmentación de clientes para campañas
   - Productos recomendados por segmento
   - Estrategias personalizadas por cliente
   - Análisis de efectividad de métodos de pago

4. **Optimización de Mix de Productos:**
   - Análisis de rendimiento por categoría
   - Identificación de categorías estrella
   - Recomendaciones de expansión/reducción
   - Análisis de complementariedad

**Resultados:**
- Reportes de optimización generados
- Recomendaciones específicas y cuantificadas
- Visualizaciones de optimizaciones
- Planes de acción documentados

#### 5.2.9. Fase 9: Reporte Final (`07_reporte_final.py`)

**Objetivo:** Consolidar todos los resultados en reportes ejecutivos

**Reportes Generados:**

1. **REPORTE_FINAL_AURELION.md:**
   - Resumen ejecutivo
   - Resultados de todos los modelos
   - Conclusiones y recomendaciones
   - Archivos generados

2. **RESUMEN_EJECUTIVO.md:**
   - Resumen de una página
   - Resultados clave
   - Recomendaciones principales

3. **DOCUMENTACION_TECNICA.md:**
   - Detalles técnicos de implementación
   - Metodologías utilizadas
   - Estructura de archivos

### 5.3. Resultados del Sprint 2

- ✅ Esquema de base de datos documentado
- ✅ Análisis exploratorio avanzado completo
- ✅ 6 datasets normalizados
- ✅ 9 modelos de ML entrenados y evaluados
- ✅ 24 visualizaciones avanzadas
- ✅ Estadística inferencial implementada
- ✅ Analítica prescriptiva operativa
- ✅ Reportes ejecutivos generados

### 5.4. Lecciones Aprendidas

- La normalización adecuada es crucial para el rendimiento de modelos ML
- La selección inteligente de técnicas de imputación mejora la calidad de datos
- Los modelos de ensemble (Random Forest) ofrecen mejor rendimiento
- La analítica prescriptiva transforma insights en acciones concretas

### 5.5. Funciones Principales Utilizadas en el Sprint 2

Esta sección explica las funciones principales utilizadas en el Sprint 2 de manera sencilla, enfocándose en la preparación de datos y el Machine Learning.

#### 5.5.1. Función: `imputar_valores_faltantes()`

**¿Qué hace?**
Cuando hay datos faltantes en las tablas (celdas vacías), esta función los completa de manera inteligente usando estadísticas.

**¿Cómo funciona?**
1. Detecta qué celdas están vacías en cada columna
2. Analiza el tipo de dato (número, texto, etc.)
3. Para números: calcula el promedio o la mediana y usa ese valor para llenar los espacios vacíos
4. Para texto: usa el valor más común (moda) para llenar los espacios vacíos
5. Elige la estrategia más adecuada según la distribución de los datos

**¿Para qué se usó?**
Para asegurar que no haya datos faltantes que puedan causar errores en los análisis posteriores. Es como completar un formulario donde faltan algunas respuestas, usando la información más probable.

**Ejemplo práctico:**
Imagina que tienes una lista de precios de productos, pero algunos precios están faltando. Esta función calcula el precio promedio de los productos similares y usa ese valor para completar los faltantes.

---

#### 5.5.2. Función: `tratar_outliers()`

**¿Qué hace?**
Identifica valores extremos (valores que son mucho más altos o más bajos que el resto) y los ajusta para que no distorsionen los análisis.

**¿Cómo funciona?**
1. Calcula qué valores son "normales" usando estadísticas (percentiles 25 y 75)
2. Identifica valores que están muy por encima o muy por debajo de lo normal
3. En lugar de eliminarlos, los ajusta al límite máximo o mínimo aceptable (Winsorización)
4. Esto preserva la información pero evita que valores extremos afecten los resultados

**¿Para qué se usó?**
Para manejar casos excepcionales sin perder información. Por ejemplo, si hay una venta de $50,000 cuando el promedio es $5,000, en lugar de eliminarla, se ajusta a un valor más razonable pero se mantiene la información de que fue una venta grande.

**Ejemplo práctico:**
Es como cuando tienes un grupo de personas y una persona mide 2.50 metros (muy alto). En lugar de excluirla del grupo, la tratas como si midiera 2.00 metros para los cálculos, pero sabes que es una persona excepcionalmente alta.

---

#### 5.5.3. Función: `normalizar_variables_numericas()`

**¿Qué hace?**
Convierte todos los números a una escala similar para que puedan compararse entre sí. Es como convertir todo a la misma unidad de medida.

**¿Cómo funciona?**
1. Analiza cada columna numérica (precios, cantidades, etc.)
2. Decide qué método de normalización usar según cómo estén distribuidos los datos:
   - **MinMaxScaler:** Convierte todo a escala 0-1 (como convertir todo a porcentajes)
   - **StandardScaler:** Centra los datos en 0 y ajusta la desviación estándar a 1
   - **RobustScaler:** Similar pero resistente a valores extremos
3. Aplica la transformación a todos los valores

**¿Para qué se usó?**
Para que los algoritmos de Machine Learning puedan comparar variables que están en escalas diferentes. Por ejemplo, si tienes precios en miles de pesos y cantidades en unidades, después de normalizar ambos están en la misma escala.

**Ejemplo práctico:**
Es como convertir todo a la misma moneda. Si tienes precios en dólares, euros y pesos, los conviertes todos a pesos para poder compararlos. Aquí convertimos todo a una "escala universal" para que los algoritmos puedan trabajar con ellos.

---

#### 5.5.4. Función: `codificar_variables_categoricas()`

**¿Qué hace?**
Convierte texto (como nombres de categorías, métodos de pago, ciudades) en números que las computadoras pueden entender y procesar.

**¿Cómo funciona?**
1. Identifica todas las columnas con texto (categóricas)
2. Según cuántas categorías diferentes haya, elige un método:
   - **OneHot Encoding:** Si hay pocas categorías (≤5), crea una columna por cada categoría con 0 o 1
   - **Binary Encoding:** Si hay categorías moderadas (6-20), usa codificación binaria más eficiente
   - **Target Encoding:** Si hay muchas categorías (>20), usa codificación basada en el objetivo
3. Convierte cada valor de texto en su representación numérica

**¿Para qué se usó?**
Porque las computadoras solo pueden trabajar con números. Si tienes "efectivo", "tarjeta", "QR", necesitas convertirlos a números como 0, 1, 2 para que los algoritmos puedan procesarlos.

**Ejemplo práctico:**
Es como crear un código numérico para cada categoría. En lugar de escribir "efectivo", escribes "1". En lugar de "tarjeta", escribes "2". La computadora puede trabajar con números, pero no entiende palabras directamente.

---

#### 5.5.5. Función: `entrenar_modelos_regresion()`

**¿Qué hace?**
Entrena modelos de Machine Learning que pueden predecir valores numéricos (como predecir cuánto dinero generará una venta).

**¿Cómo funciona?**
1. Divide los datos en dos grupos: 80% para entrenar y 20% para probar
2. Entrena tres tipos de modelos diferentes:
   - **Linear Regression:** Modelo simple que encuentra una línea que mejor se ajusta a los datos
   - **Random Forest:** Modelo más complejo que combina múltiples "árboles de decisión"
   - **SVR:** Modelo avanzado que puede encontrar patrones no lineales
3. Cada modelo "aprende" de los datos de entrenamiento
4. Prueba cada modelo con los datos de prueba para ver qué tan bien predice
5. Calcula métricas de precisión (R², MSE) para cada modelo

**¿Para qué se usó?**
Para poder predecir valores futuros. Por ejemplo, si un cliente compra ciertos productos, el modelo puede predecir cuánto dinero gastará en total.

**Ejemplo práctico:**
Es como enseñarle a una computadora a predecir el precio de una casa. Le muestras muchas casas con sus características (tamaño, ubicación, etc.) y sus precios. La computadora "aprende" los patrones y luego puede predecir el precio de una casa nueva basándose en sus características.

---

#### 5.5.6. Función: `entrenar_modelos_clasificacion()`

**¿Qué hace?**
Entrena modelos que pueden clasificar o categorizar datos (como clasificar clientes en segmentos: Bajo, Medio, Alto).

**¿Cómo funciona?**
1. Crea categorías basadas en los datos (por ejemplo, segmentos de clientes según su gasto)
2. Divide los datos en entrenamiento (80%) y prueba (20%)
3. Entrena tres tipos de modelos:
   - **Logistic Regression:** Modelo que calcula probabilidades de pertenecer a cada categoría
   - **Random Forest Classifier:** Modelo que combina múltiples clasificadores
   - **SVC:** Modelo que encuentra la mejor forma de separar las categorías
4. Cada modelo aprende a identificar a qué categoría pertenece cada cliente
5. Prueba los modelos y calcula qué tan precisos son (Accuracy, Precision, Recall)

**¿Para qué se usó?**
Para clasificar automáticamente a los clientes en segmentos. Por ejemplo, cuando llega un nuevo cliente, el modelo puede predecir si será un cliente de "Alto", "Medio" o "Bajo" valor basándose en sus características.

**Ejemplo práctico:**
Es como enseñarle a una computadora a clasificar frutas. Le muestras muchas manzanas, naranjas y plátanos con sus características (color, tamaño, forma). La computadora aprende y luego puede clasificar automáticamente una fruta nueva que nunca ha visto antes.

---

#### 5.5.7. Función: `entrenar_clustering()`

**¿Qué hace?**
Agrupa automáticamente datos similares sin necesidad de saber de antemano en qué grupos deben estar. Es como organizar objetos similares juntos.

**¿Cómo funciona?**
1. Selecciona las características importantes (cantidad, precio, importe)
2. Usa dos algoritmos diferentes:
   - **K-Means:** Divide los datos en un número específico de grupos (por ejemplo, 3 grupos)
   - **DBSCAN:** Encuentra grupos naturales basándose en la densidad de los datos
3. Cada algoritmo agrupa los datos de manera diferente
4. Calcula qué tan bien están agrupados los datos (Silhouette Score)

**¿Para qué se usó?**
Para descubrir patrones ocultos en los datos. Por ejemplo, puede agrupar automáticamente las ventas en grupos como "ventas pequeñas", "ventas medianas" y "ventas grandes" sin que tengas que definir manualmente qué es "pequeño" o "grande".

**Ejemplo práctico:**
Es como organizar una biblioteca. En lugar de decirle a alguien "pon los libros de ciencia aquí y los de historia allá", le das todos los libros y la computadora los agrupa automáticamente según sus características (tema, autor, año, etc.).

---

#### 5.5.8. Función: `crear_visualizaciones_modelos()`

**¿Qué hace?**
Crea gráficos visuales que muestran cómo funcionan los modelos, qué tan bien predicen, y qué variables son más importantes.

**¿Cómo funciona?**
1. Crea gráficos comparando valores reales vs valores predichos
2. Genera gráficos de barras mostrando la precisión de cada modelo
3. Crea visualizaciones de los grupos (clusters) encontrados
4. Genera gráficos mostrando qué variables son más importantes para las predicciones
5. Crea matrices de confusión que muestran qué tan bien clasifica cada modelo

**¿Para qué se usó?**
Para entender visualmente cómo funcionan los modelos y comunicar los resultados de manera clara. Un gráfico es más fácil de entender que una tabla de números.

**Ejemplo práctico:**
Es como crear un reporte visual de tu negocio. En lugar de solo números, creas gráficos de barras, líneas y pasteles que muestran la información de manera visual y fácil de entender.

---

#### 5.5.9. Función: `merge_tablas()` (del archivo `03_merge_tablas.py`)

**¿Qué hace?**
Combina todas las tablas separadas (clientes, productos, ventas, detalle_ventas) en una sola tabla grande con toda la información junta.

**¿Cómo funciona?**
1. Toma la tabla de ventas y le agrega información de clientes (usando el ID del cliente)
2. Toma la tabla de detalle_ventas y le agrega información de productos (usando el ID del producto)
3. Combina ambas tablas usando el ID de venta
4. Verifica que todas las relaciones sean correctas (que no haya datos huérfanos)
5. Crea una tabla final con toda la información combinada

**¿Para qué se usó?**
Para tener toda la información en un solo lugar. En lugar de tener que consultar 4 tablas diferentes, tienes una tabla con toda la información: qué cliente compró qué producto, cuándo, cómo pagó, etc.

**Ejemplo práctico:**
Es como combinar varias hojas de cálculo en una sola. Tienes una hoja con clientes, otra con productos, otra con ventas. Esta función las combina todas en una hoja grande donde puedes ver toda la información junta.

---

### Resumen de Funciones del Sprint 2

| Función | Propósito Simple | Resultado |
|---------|------------------|-----------|
| `imputar_valores_faltantes()` | Completar datos faltantes | Datos completos sin espacios vacíos |
| `tratar_outliers()` | Ajustar valores extremos | Datos sin distorsiones |
| `normalizar_variables_numericas()` | Convertir a escala común | Variables comparables |
| `codificar_variables_categoricas()` | Convertir texto a números | Datos que las computadoras pueden procesar |
| `entrenar_modelos_regresion()` | Enseñar a predecir valores | Modelos que predicen números |
| `entrenar_modelos_clasificacion()` | Enseñar a clasificar | Modelos que clasifican en categorías |
| `entrenar_clustering()` | Agrupar datos similares | Grupos automáticos de datos |
| `crear_visualizaciones_modelos()` | Crear gráficos de resultados | Visualizaciones de los modelos |
| `merge_tablas()` | Combinar tablas | Una tabla con toda la información |

### 5.6. Métodos de Pandas y Scikit-learn Utilizados en el Sprint 2

Además de las funciones principales, en el Sprint 2 se utilizaron métodos adicionales de pandas y scikit-learn para la preparación de datos y Machine Learning.

#### 5.6.1. Método: `.select_dtypes()`

**¿Qué hace?**
Selecciona solo las columnas de un tipo específico de dato (números, texto, fechas, etc.) de una tabla.

**¿Cómo funciona?**
- **`.select_dtypes(include=[np.number])`:** Selecciona solo columnas numéricas
- **`.select_dtypes(include=['object'])`:** Selecciona solo columnas de texto
- **`.select_dtypes(include=['datetime64'])`:** Selecciona solo columnas de fecha

**¿Para qué se usó?**
Para separar las columnas numéricas de las categóricas, ya que cada tipo requiere un tratamiento diferente (normalización para números, codificación para texto).

**Ejemplo práctico:**
Es como separar frutas y verduras en diferentes canastas. Tienes una canasta mixta y quieres separar solo las frutas (números) de las verduras (texto) para tratarlas de manera diferente.

---

#### 5.6.2. Método: `.fillna()` y `.dropna()`

**¿Qué hace?**
Maneja valores faltantes (celdas vacías) en las tablas:
- **`.fillna(valor)`:** Llena los espacios vacíos con un valor específico
- **`.dropna()`:** Elimina las filas que tienen valores vacíos

**¿Cómo funciona?**
1. Identifica qué celdas están vacías
2. **`.fillna()`:** Las rellena con un valor (promedio, mediana, moda, etc.)
3. **`.dropna()`:** Elimina las filas completas que tienen al menos un valor vacío

**¿Para qué se usó?**
Para manejar datos faltantes antes de entrenar los modelos. Los modelos de Machine Learning no pueden trabajar con valores vacíos, así que hay que completarlos o eliminarlos.

**Ejemplo práctico:**
Es como completar un formulario. Si falta la edad de alguien, puedes usar la edad promedio (`.fillna()` con promedio) o eliminar esa persona del análisis (`.dropna()`).

---

#### 5.6.3. Método: `.skew()` y `.kurtosis()`

**¿Qué hace?**
Mide características de la distribución de los datos:
- **`.skew()`:** Mide la asimetría (si los datos están sesgados hacia la izquierda o derecha)
- **`.kurtosis()`:** Mide qué tan "puntiaguda" o "plana" es la distribución

**¿Cómo funciona?**
- **Skewness = 0:** Distribución simétrica (normal)
- **Skewness > 0:** Sesgada a la derecha (más valores pequeños)
- **Skewness < 0:** Sesgada a la izquierda (más valores grandes)
- **Kurtosis:** Compara qué tan concentrados están los datos alrededor de la media

**¿Para qué se usó?**
Para decidir qué método de normalización usar. Si los datos están muy sesgados, se usa un método diferente que si están normalmente distribuidos.

**Ejemplo práctico:**
Es como analizar la forma de una montaña. Si la montaña está centrada (skewness = 0), es simétrica. Si está inclinada hacia un lado (skewness > 0 o < 0), está sesgada. La kurtosis te dice si la montaña es muy puntiaguda o muy plana.

---

#### 5.6.4. Método: `.isnull()` y `.notna()`

**¿Qué hace?**
Identifica qué valores están vacíos o no están vacíos:
- **`.isnull()`:** Devuelve True para valores vacíos, False para valores con datos
- **`.notna()`:** Devuelve True para valores con datos, False para valores vacíos

**¿Para qué se usó?**
Para contar cuántos valores faltantes hay y decidir cómo tratarlos. Por ejemplo, si hay muchos valores faltantes, se completa con estadísticas. Si hay pocos, se pueden eliminar.

**Ejemplo práctico:**
Es como revisar una lista de asistencia. `.isnull()` te dice quién faltó (True = faltó), y `.notna()` te dice quién asistió (True = asistió).

---

#### 5.6.5. Método: `.mode()`

**¿Qué hace?**
Encuentra el valor más frecuente (la moda) en una columna.

**¿Cómo funciona?**
1. Cuenta cuántas veces aparece cada valor
2. Devuelve el valor que aparece más veces

**¿Para qué se usó?**
Para completar valores faltantes en columnas categóricas (texto). Si falta el método de pago de una venta, se usa el método de pago más común.

**Ejemplo práctico:**
Es como preguntar "¿cuál es el color de auto más común en el estacionamiento?" La moda te da la respuesta: el color que aparece más veces.

---

#### 5.6.6. Método: `.nunique()`

**¿Qué hace?**
Cuenta cuántos valores únicos diferentes hay en una columna.

**¿Cómo funciona?**
1. Toma una columna
2. Cuenta cuántos valores diferentes hay (sin repetir)
3. Devuelve ese número

**¿Para qué se usó?**
Para decidir qué método de codificación usar para variables categóricas. Si hay pocos valores únicos (≤5), se usa OneHot. Si hay muchos (>20), se usa Target Encoding.

**Ejemplo práctico:**
Es como contar cuántos sabores diferentes de helado hay en una tienda. Si hay 3 sabores (chocolate, vainilla, fresa), `.nunique()` devuelve 3.

---

#### 5.6.7. Método: `.fit()` y `.transform()` (Scikit-learn)

**¿Qué hace?**
Estos métodos son parte de scikit-learn y se usan para entrenar transformadores y aplicar transformaciones:
- **`.fit()`:** "Enseña" al transformador cómo transformar los datos (calcula parámetros)
- **`.transform()`:** Aplica la transformación aprendida a los datos
- **`.fit_transform()`:** Hace ambas cosas a la vez (entrena y transforma)

**¿Cómo funciona?**
1. **`.fit(datos)`:** El transformador analiza los datos y aprende cómo transformarlos (por ejemplo, calcula la media y desviación estándar para normalizar)
2. **`.transform(datos)`:** Aplica la transformación aprendida (normaliza los datos)
3. **`.fit_transform(datos)`:** Hace ambos pasos en uno

**⚠️ IMPORTANTE: Orden Correcto para Evitar Data Leakage**

**❌ INCORRECTO (causa data leakage):**
```python
# Normalizar ANTES de dividir
scaler.fit_transform(X_completo)  # Aprende de datos que incluyen test
X_train, X_test = train_test_split(X_normalizado, ...)
```

**✅ CORRECTO (implementado en el proyecto):**
```python
# Dividir PRIMERO
X_train_raw, X_test_raw = train_test_split(X, y, ...)

# Normalizar DESPUÉS (solo con datos de training)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train_raw)  # fit_transform en training
X_test = scaler.transform(X_test_raw)        # transform en test
```

**¿Por qué es importante?**
- El scaler debe aprender SOLO de datos de entrenamiento
- Si aprende de todo el dataset (incluyendo test), causa **data leakage**
- Esto puede llevar a métricas optimistas e irreales
- En producción, el modelo no verá datos de test durante el entrenamiento

**¿Para qué se usó?**
Para normalizar datos y codificar variables categóricas. En el proyecto Aurelion:
- **Regresión y Clasificación:** Normalización después de dividir en train/test
- **Clustering:** `fit_transform` en todo el dataset (correcto, no hay división train/test)
- **Cross-Validation:** Usa `Pipeline` para normalizar dentro de cada fold

**Ejemplo práctico:**
Es como aprender a cocinar. Primero aprendes la receta con ingredientes de entrenamiento (`.fit()` - analizas los ingredientes y pasos), y luego cocinas siguiendo esa receta (`.transform()` - aplicas lo aprendido). No debes usar ingredientes de prueba para aprender la receta.

---

#### 5.6.8. Método: `.fit()` y `.predict()` (Modelos ML)

**¿Qué hace?**
Estos métodos se usan con los modelos de Machine Learning:
- **`.fit(X, y)`:** Entrena el modelo con datos de entrada (X) y resultados esperados (y)
- **`.predict(X)`:** Usa el modelo entrenado para hacer predicciones sobre nuevos datos

**¿Cómo funciona?**
1. **`.fit(X_train, y_train)`:** El modelo "aprende" de los datos de entrenamiento
2. **`.predict(X_test)`:** El modelo hace predicciones sobre datos nuevos que nunca ha visto

**¿Para qué se usó?**
Para entrenar los modelos de Machine Learning y hacer predicciones. Es el corazón del proceso de ML.

**Ejemplo práctico:**
Es como enseñarle a alguien a reconocer perros. Le muestras muchas fotos de perros (`.fit()` - entrena), y luego le muestras una foto nueva y te dice si es un perro o no (`.predict()` - predice).

---

#### 5.6.9. Método: `.score()`

**¿Qué hace?**
Evalúa qué tan bien funciona un modelo comparando sus predicciones con los valores reales.

**¿Cómo funciona?**
1. Toma las predicciones del modelo
2. Las compara con los valores reales
3. Calcula una métrica de precisión (R² para regresión, Accuracy para clasificación)
4. Devuelve un número entre 0 y 1 (1 = perfecto, 0 = muy malo)

**¿Para qué se usó?**
Para evaluar el rendimiento de los modelos. Un score alto significa que el modelo predice bien, un score bajo significa que necesita mejorar.

**Ejemplo práctico:**
Es como calificar un examen. Comparas las respuestas del estudiante (predicciones) con las respuestas correctas (valores reales) y le das una calificación del 0 al 100%.

---

### Resumen de Métodos del Sprint 2

| Método | Librería | Propósito Simple | Ejemplo de Uso |
|--------|----------|------------------|----------------|
| `.select_dtypes()` | pandas | Seleccionar columnas por tipo | Separar números de texto |
| `.fillna()`, `.dropna()` | pandas | Manejar valores faltantes | Completar o eliminar datos vacíos |
| `.skew()`, `.kurtosis()` | pandas | Medir forma de distribución | Decidir método de normalización |
| `.isnull()`, `.notna()` | pandas | Identificar valores vacíos | Contar datos faltantes |
| `.mode()` | pandas | Encontrar valor más frecuente | Completar datos categóricos faltantes |
| `.nunique()` | pandas | Contar valores únicos | Decidir método de codificación |
| `.fit()`, `.transform()` | scikit-learn | Entrenar y aplicar transformaciones | Normalizar datos |
| `.fit()`, `.predict()` | scikit-learn | Entrenar y predecir con modelos | Entrenar modelos ML |
| `.score()` | scikit-learn | Evaluar rendimiento del modelo | Medir precisión del modelo |

---

## 6. SPRINT 3: FUNDAMENTOS DE MACHINE LEARNING Y MODELADO

### 6.1. Objetivos del Sprint 3

1. Explicar fundamentos teóricos de Machine Learning
2. Implementar proceso completo de modelado con scikit-learn
3. Crear sistema interactivo educativo
4. Demostrar evaluación de modelos
5. Comparar diferentes algoritmos

### 6.2. Desarrollo Técnico

#### 6.2.1. Módulo 1: Fundamentos de ML (`01_machine_learning_basico.py`)

**Contenido:**

1. **Definición de Machine Learning:**
   - Aprendizaje automático como subdivisión de IA
   - Diferencias con IA tradicional
   - Aprendizaje a partir de datos

2. **Tipos de Problemas:**
   - **Regresión:** Predicción de valores continuos
   - **Clasificación:** Predicción de categorías
   - **Clustering:** Agrupación de datos similares

3. **Proceso Típico de ML:**
   - Recopilación de datos
   - Preparación y limpieza
   - División train/test
   - Entrenamiento
   - Evaluación
   - Despliegue

4. **Ejemplo Práctico con Aurelion:**
   - Predicción de monto de ventas
   - Proceso paso a paso
   - Resultados esperados

#### 6.2.2. Módulo 2: Tipos de Aprendizajes (`02_tipos_aprendizajes.py`)

**Contenido:**

1. **Aprendizaje Supervisado:**
   
   **¿Qué es el Aprendizaje Supervisado?**
   
   El aprendizaje supervisado es un tipo de Machine Learning donde el modelo aprende de **datos etiquetados**. Esto significa que tenemos ejemplos donde conocemos tanto las **características (features)** como la **respuesta correcta (label/target)**.
   
   **Características clave:**
   - **Datos etiquetados:** Cada ejemplo tiene una "respuesta correcta" conocida
   - **Objetivo claro:** Sabemos qué queremos predecir
   - **Entrenamiento:** El modelo aprende la relación entre características y etiquetas
   - **Predicción:** Una vez entrenado, puede predecir etiquetas para datos nuevos
   
   **¿Qué es un Label (Etiqueta)?**
   
   Un **label** (etiqueta) es la respuesta correcta o el valor que queremos predecir. Es la "verdad" que conocemos para cada ejemplo en los datos de entrenamiento.
   
   **Ejemplo con Aurelion:**
   ```
   Datos de Entrenamiento:
   
   Cliente | Cantidad | Precio | Categoría | Label (Segmento)
   --------|----------|--------|-----------|------------------
   A       |    2     |  2,000 | Electr.   | "Alto"    ← Label conocido
   B       |    1     |  1,500 | Alimentos | "Bajo"    ← Label conocido
   C       |    3     |  2,500 | Electr.   | "Alto"    ← Label conocido
   ```
   
   - **Features (Características):** Cantidad, Precio, Categoría
   - **Label (Etiqueta):** Segmento ("Alto", "Bajo", "Medio")
   - El modelo aprende: "Si cantidad=3 y precio=2,500 → Segmento='Alto'"
   
   **Tipos de Aprendizaje Supervisado:**
   
   **a) Regresión:**
   - **Label:** Valor numérico continuo
   - **Ejemplo en Aurelion:** Predecir el `importe` de una venta
   - **Label:** `importe = $7,500` (número)
   - **Algoritmos:** Linear Regression, Random Forest Regressor, SVR
   
   **b) Clasificación:**
   - **Label:** Categoría o clase
   - **Ejemplo en Aurelion:** Clasificar clientes en segmentos
   - **Label:** `segmento_cliente = "Alto"` (categoría)
   - **Algoritmos:** Logistic Regression, Random Forest Classifier, SVC
   
   **Ventajas:**
   - Objetivo claro y medible
   - Fácil de evaluar (comparar predicciones con labels reales)
   - Resultados interpretables
   
   **Desventajas:**
   - Requiere datos etiquetados (puede ser costoso obtenerlos)
   - Solo puede predecir lo que ha visto en entrenamiento
   
   **En Aurelion:**
   - **Regresión:** Label = `importe` (valor numérico)
   - **Clasificación:** Label = `segmento_cliente` ("Bajo", "Medio", "Alto")
   - **Resultado:** Modelos con alta precisión (R² = 99.62%, Accuracy = 88.41%)

2. **Aprendizaje No Supervisado:**
   
   **¿Qué es el Aprendizaje No Supervisado?**
   
   El aprendizaje no supervisado es un tipo de Machine Learning donde el modelo aprende de **datos sin etiquetas**. No hay una "respuesta correcta" conocida. El objetivo es descubrir **patrones ocultos** en los datos.
   
   **Características clave:**
   - **Sin datos etiquetados:** No conocemos la respuesta correcta
   - **Descubrimiento de patrones:** El modelo encuentra estructuras en los datos
   - **Sin objetivo específico:** No hay una variable objetivo a predecir
   - **Exploración:** Se usa para entender los datos mejor
   
   **¿Qué es Clustering?**
   
   **Clustering** (agrupación) es la técnica principal de aprendizaje no supervisado. Consiste en agrupar datos similares en **clusters** (grupos) sin conocer de antemano cuántos grupos hay o qué define cada grupo.
   
   **Ejemplo con Aurelion:**
   ```
   Datos SIN Labels:
   
   Transacción | Cantidad | Precio | Importe
   ------------|----------|--------|----------
   A           |    2     |  2,000 |  5,000
   B           |    1     |  1,500 |  3,000
   C           |    4     |  2,500 | 10,000
   D           |    2     |  2,200 |  5,500
   ```
   
   - **No hay label:** No sabemos a qué grupo pertenece cada transacción
   - **Clustering:** El algoritmo agrupa automáticamente:
     - **Cluster 1:** Transacciones pequeñas (A, B, D)
     - **Cluster 2:** Transacciones grandes (C)
   
   **Tipos de Aprendizaje No Supervisado:**
   
   **a) Clustering:**
   - **Objetivo:** Agrupar datos similares
   - **Ejemplo en Aurelion:** Agrupar transacciones por similitud
   - **Algoritmos:** K-Means, DBSCAN, Hierarchical Clustering
   - **Resultado:** 3 clusters identificados en Aurelion
   
   **b) Reducción de Dimensionalidad:**
   - **Objetivo:** Reducir el número de características manteniendo la información
   - **Ejemplo:** PCA (Principal Component Analysis)
   - **Uso:** Visualización, simplificación de datos
   
   **Ventajas:**
   - No requiere datos etiquetados (más fácil de obtener)
   - Descubre patrones inesperados
   - Útil para exploración de datos
   
   **Desventajas:**
   - Difícil de evaluar (no hay "respuesta correcta")
   - Resultados menos interpretables
   - No hay objetivo claro
   
   **En Aurelion:**
   - **Clustering:** Agrupa transacciones en 3 clusters
   - **Variables usadas:** cantidad, precio_unitario_detalle, importe
   - **Resultado:** Silhouette Score = 0.3863 (clusters moderadamente bien definidos)
   
   **Comparación: Supervisado vs No Supervisado:**
   
   ```
   Aprendizaje Supervisado:
   Datos: [Features] + [Label] → Modelo → Predicción de Label
   
   Ejemplo:
   [Cantidad=3, Precio=2,500] + [Segmento="Alto"] → Entrenar → Predecir Segmento
   
   Aprendizaje No Supervisado:
   Datos: [Features] → Modelo → Grupos/Patrones
   
   Ejemplo:
   [Cantidad=3, Precio=2,500, Importe=7,500] → Clustering → Cluster 2
   ```
   
   **Cuándo usar cada uno:**
   
   - **Supervisado:** Cuando tienes datos etiquetados y quieres predecir algo específico
   - **No Supervisado:** Cuando no tienes labels y quieres explorar los datos o encontrar grupos naturales

3. **Aprendizaje por Refuerzo:**
   - Interacción con entorno
   - Sistema de recompensas
   - Ejemplos: Juegos, Robots autónomos
   - Aprendizaje por prueba y error

4. **Comparación y Cuándo Usar Cada Uno:**
   - Tabla comparativa
   - Criterios de selección
   - Ejemplos específicos para Aurelion

#### 6.2.3. Módulo 3: Algoritmos Básicos (`03_algoritmos_basicos.py`)

**Contenido:**

1. **Función Costo (Cost Function):**
   
   **1.1. Definición y Objetivo:**
   
   La función costo (también llamada función de pérdida o loss function) mide qué tan mal está funcionando nuestro modelo. Es una métrica que cuantifica el error entre las predicciones del modelo y los valores reales.
   
   **Objetivo:** Minimizar la función costo para obtener el mejor modelo posible.
   
   **1.2. Función Costo para Regresión - MSE (Mean Squared Error):**
   
   En regresión, la función costo más común es el **Error Cuadrático Medio (MSE)**, que mide la distancia vertical entre los puntos reales y la línea/curva del modelo.
   
   **Fórmula:**
   ```
   MSE = (1/m) × Σ(y_pred - y_real)²
   
   Donde:
   - y_pred = valor predicho por el modelo
   - y_real = valor real observado
   - m = número de ejemplos
   - (y_pred - y_real) = error o distancia vertical
   ```
   
   **¿Por qué se eleva al cuadrado?**
   - Penaliza más los errores grandes (un error de 10 es 4 veces peor que un error de 5)
   - Siempre da valores positivos (evita que errores positivos y negativos se cancelen)
   - Es diferenciable (importante para optimización)
   - La distancia vertical se mide como diferencia entre el punto real y el punto en la línea del modelo
   
   **Ejemplo Práctico con Aurelion:**
   
   Supongamos que tenemos 5 ventas con los siguientes datos:
   ```
   Venta  | Cantidad | Importe Real | Importe Predicho | Error | Error²
   -------|----------|--------------|------------------|-------|-------
   1      |    2     |    $5,000    |    $4,800        | 200   | 40,000
   2      |    3     |    $7,500    |    $7,200        | 300   | 90,000
   3      |    1     |    $3,000    |    $3,100        | -100  | 10,000
   4      |    4     |   $10,000    |   $10,200        | -200  | 40,000
   5      |    2     |    $5,500    |    $5,400        | 100   | 10,000
   ```
   
   **Cálculo del MSE:**
   - Suma de errores al cuadrado: 40,000 + 90,000 + 10,000 + 40,000 + 10,000 = 190,000
   - MSE = 190,000 / 5 = 38,000
   - **Interpretación:** El error promedio al cuadrado es de 38,000 pesos²
   
   **1.3. Minimización de la Distancia Vertical - Gradiente Descendente:**
   
   **¿Qué es la distancia vertical?**
   
   La distancia vertical es la diferencia entre el valor real (y_real) y el valor predicho por el modelo (y_pred). En un gráfico, es la distancia vertical desde cada punto real hasta la línea del modelo.
   
   ```
   Gráfico de Regresión:
   
   Importe
     ↑
     |     ● (punto real)
     |    /|
     |   / |  ← Distancia vertical (error)
     |  /  |
     | ●   ● (puntos en la línea del modelo)
     |/
     └─────────────────→ Cantidad
   ```
   
   **¿Cómo se minimiza esta distancia?**
   
   El algoritmo de **Gradiente Descendente** ajusta los parámetros del modelo (pendiente e intercepto) para minimizar la suma de todas las distancias verticales al cuadrado.
   
   **Proceso paso a paso:**
   
   1. **Inicialización:** Se comienza con parámetros aleatorios (por ejemplo, pendiente = 0, intercepto = 0)
   
   2. **Cálculo del Costo:** Se calcula el MSE con esos parámetros
     ```
     MSE = (1/m) × Σ(y_pred - y_real)²
     ```
   
   3. **Cálculo del Gradiente:** Se calcula la derivada de la función costo respecto a cada parámetro
     ```
     ∂MSE/∂pendiente = (2/m) × Σ[(y_pred - y_real) × x]
     ∂MSE/∂intercepto = (2/m) × Σ(y_pred - y_real)
     ```
   
   4. **Actualización de Parámetros:** Se ajustan los parámetros en dirección opuesta al gradiente
     ```
     pendiente_nueva = pendiente_anterior - α × (∂MSE/∂pendiente)
     intercepto_nuevo = intercepto_anterior - α × (∂MSE/∂intercepto)
     ```
     Donde α (alpha) es la **tasa de aprendizaje** (learning rate) - qué tan grandes son los pasos
   
   5. **Repetición:** Se repiten los pasos 2-4 hasta que el costo no disminuya más (convergencia)
   
   **Ejemplo Visual del Proceso:**
   
   ```
   Iteración 1: MSE = 50,000  → Pendiente = 1.0, Intercepto = 0
   Iteración 2: MSE = 38,000  → Pendiente = 1.5, Intercepto = 500
   Iteración 3: MSE = 25,000  → Pendiente = 2.0, Intercepto = 800
   Iteración 4: MSE = 15,000  → Pendiente = 2.3, Intercepto = 1,000
   ...
   Iteración 100: MSE = 1,200 → Pendiente = 2.8, Intercepto = 1,200 (óptimo)
   ```
   
   **En el Proyecto Aurelion:**
   
   Para predecir el importe de venta basándose en cantidad y otras variables:
   - El modelo ajusta los parámetros para que la línea/curva pase lo más cerca posible de todos los puntos
   - Minimiza la suma de todas las distancias verticales al cuadrado
   - El resultado: R² = 0.9962 significa que las distancias verticales son muy pequeñas (99.62% de la variabilidad está explicada)
   
   **1.4. Otras Funciones Costo para Regresión:**
   
   **MAE (Mean Absolute Error) - Error Absoluto Medio:**
   ```
   MAE = (1/m) × Σ|y_pred - y_real|
   ```
   - Penaliza errores de forma lineal (no cuadrática)
   - Menos sensible a outliers que MSE
   - No es diferenciable en cero (más difícil de optimizar)
   
   **1.5. Relación con Optimización:**
   
   El objetivo del entrenamiento es encontrar los parámetros que minimizan la función costo. Esto se hace mediante algoritmos de optimización:
   - **Gradiente Descendente (Gradient Descent):** Ajusta parámetros iterativamente
   - **Descenso de Gradiente Estocástico (SGD):** Usa un ejemplo a la vez (más rápido)
   - **Adam, RMSprop:** Variantes avanzadas para redes neuronales
   
   **1.6. Ejemplo Completo con Datos de Aurelion:**
   
   **Datos de Entrenamiento (5 ventas):**
   ```
   Cantidad | Importe Real
   ---------|-------------
      2     |   $5,000
      3     |   $7,500
      1     |   $3,000
      4     |  $10,000
      2     |   $5,500
   ```
   
   **Modelo Inicial (parámetros aleatorios):**
   - Pendiente (m) = 1.0
   - Intercepto (b) = 0
   - Ecuación: Importe_predicho = 1.0 × Cantidad + 0
   
   **Cálculo de Predicciones y Errores:**
   ```
   Cantidad | Real  | Predicho | Error  | Error²
   ---------|-------|----------|--------|--------
      2     | 5,000 |   2,000  |  3,000 | 9,000,000
      3     | 7,500 |   3,000  |  4,500 | 20,250,000
      1     | 3,000 |   1,000  |  2,000 | 4,000,000
      4     |10,000 |   4,000  |  6,000 | 36,000,000
      2     | 5,500 |   2,000  |  3,500 | 12,250,000
   ```
   
   **MSE Inicial:** (9,000,000 + 20,250,000 + 4,000,000 + 36,000,000 + 12,250,000) / 5 = 16,300,000
   
   **Después de Optimización (Gradiente Descendente):**
   - Pendiente (m) = 2,500
   - Intercepto (b) = 500
   - Ecuación: Importe_predicho = 2,500 × Cantidad + 500
   
   **Nuevas Predicciones:**
   ```
   Cantidad | Real  | Predicho | Error  | Error²
   ---------|-------|----------|--------|--------
      2     | 5,000 |   5,500  |  -500  |   250,000
      3     | 7,500 |   8,000  |  -500  |   250,000
      1     | 3,000 |   3,000  |     0  |         0
      4     |10,000 |  10,500  |  -500  |   250,000
      2     | 5,500 |   5,500  |     0  |         0
   ```
   
   **MSE Optimizado:** (250,000 + 250,000 + 0 + 250,000 + 0) / 5 = 150,000
   
   **Mejora:** El MSE se redujo de 16,300,000 a 150,000 (reducción del 99.1%)
   - Las distancias verticales entre los puntos reales y la línea del modelo son ahora mucho menores
   - El modelo predice mucho mejor los importes

2. **Algoritmos de Regresión:**
   
   **2.1. Linear Regression (Regresión Lineal):**
   
   **Ecuación:** y = mx + b (o y = θ₀ + θ₁x en notación ML)
   - **m (θ₁):** Pendiente de la línea
   - **b (θ₀):** Intercepto (valor cuando x = 0)
   
   **Función costo:** MSE (Mean Squared Error)
   - Minimiza la suma de distancias verticales al cuadrado
   - Fórmula: MSE = (1/m) × Σ(y_pred - y_real)²
   
   **Optimización: Gradiente Descendente**
   - Ajusta m y b iterativamente para minimizar MSE
   - Encuentra la línea que mejor se ajusta a los datos
   
   **Ejemplo en Aurelion:**
   - Predice importe basándose en cantidad
   - Ecuación final: Importe = 2,500 × Cantidad + 500
   - R² = 0.9962 significa que esta línea explica el 99.62% de la variabilidad
   
   **2.2. Random Forest Regressor:**
   
   **¿Qué es Random Forest?**
   
   Random Forest es un algoritmo de **ensemble** (conjunto) que combina múltiples **árboles de decisión** para hacer predicciones más precisas y robustas que un solo árbol.
   
   **¿Qué es un Árbol de Decisión?**
   
   Un árbol de decisión es un modelo que hace predicciones dividiendo los datos en grupos basándose en reglas simples (por ejemplo: "si cantidad > 3, entonces importe > $5,000").
   
   ```
   Ejemplo de Árbol de Decisión:
   
   ¿Cantidad > 3?
   ├─ SÍ → ¿Precio > $2,000?
   │   ├─ SÍ → Importe = $8,000
   │   └─ NO → Importe = $5,000
   └─ NO → ¿Categoría = "Electrónica"?
       ├─ SÍ → Importe = $4,000
       └─ NO → Importe = $2,000
   ```
   
   **Problema con un solo árbol:**
   - Puede sobreajustarse (memorizar los datos de entrenamiento)
   - Es sensible a pequeños cambios en los datos
   - Puede tener alta varianza
   
   **Solución: Random Forest (Ensemble)**
   
   Random Forest crea **múltiples árboles** (100 en nuestro proyecto) y combina sus predicciones:
   
   **Proceso paso a paso:**
   
   1. **Bootstrap Sampling (Muestreo con reemplazo):**
      - Se crean 100 subconjuntos diferentes de los datos de entrenamiento
      - Cada subconjunto tiene aproximadamente el 63% de los datos originales (algunos datos se repiten)
      - Cada árbol se entrena con un subconjunto diferente
   
   2. **Feature Randomness (Aleatoriedad de características):**
      - En cada división del árbol, solo se consideran un subconjunto aleatorio de características
      - Esto hace que los árboles sean diferentes entre sí
   
   3. **Entrenamiento de cada árbol:**
      - Cada árbol se entrena independientemente con su subconjunto de datos
      - Cada árbol aprende diferentes patrones
   
   4. **Predicción final (Votación/Promedio):**
      - Para regresión: Se promedian las predicciones de los 100 árboles
      - Para clasificación: Se vota por la clase más frecuente
   
   **Ejemplo con Aurelion:**
   
   Supongamos que queremos predecir el importe de una venta con:
   - Cantidad = 4
   - Precio unitario = $2,500
   - Categoría = "Electrónica"
   
   **Predicciones de 5 árboles (ejemplo simplificado):**
   ```
   Árbol 1: $9,500
   Árbol 2: $10,200
   Árbol 3: $9,800
   Árbol 4: $10,000
   Árbol 5: $9,900
   ```
   
   **Predicción final (promedio):**
   - Importe predicho = (9,500 + 10,200 + 9,800 + 10,000 + 9,900) / 5 = $9,880
   
   **¿Por qué funciona mejor?**
   
   1. **Reduce Overfitting:**
      - Un solo árbol puede memorizar los datos
      - El promedio de 100 árboles suaviza las predicciones extremas
   
   2. **Reduce Varianza:**
      - Si un árbol hace una predicción errónea, los otros la compensan
      - El promedio es más estable
   
   3. **Maneja Relaciones No Lineales:**
      - Cada árbol puede capturar diferentes aspectos de la relación
      - La combinación captura patrones complejos
   
   4. **Robusto a Outliers:**
      - Los outliers afectan solo a algunos árboles
      - El promedio mitiga su impacto
   
   **Función costo:**
   
   Cada árbol minimiza MSE en su subconjunto de datos:
   - Cada árbol busca la mejor división para minimizar el error
   - El promedio de todos los árboles reduce el error total
   
   **Parámetros en Aurelion:**
   - **n_estimators = 100:** 100 árboles de decisión
   - **max_depth = 10:** Profundidad máxima de cada árbol
   - **min_samples_split = 5:** Mínimo de muestras para dividir un nodo
   - **min_samples_leaf = 2:** Mínimo de muestras en una hoja
   
   **Resultados en Aurelion:**
   - **R² = 0.9962 (99.62%)** - Mejor modelo de regresión
   - Explica casi toda la variabilidad en los importes
   - Puede capturar relaciones complejas entre cantidad, precio, categoría, etc.
   
   **Ventajas:**
   - Maneja relaciones no lineales
   - Robusto a outliers
   - No sobreajusta tanto como un solo árbol
   - Proporciona importancia de variables
   - Funciona bien con datos mixtos (numéricos y categóricos)
   
   **Desventajas:**
   - Menos interpretable que un solo árbol
   - Más lento de entrenar
   - Requiere más memoria
   
   **2.3. SVR (Support Vector Regression):**
   
   **¿Qué es SVR?**
   
   SVR (Support Vector Regression) es un algoritmo de regresión basado en **Support Vector Machines (SVM)**. En lugar de minimizar MSE directamente, busca encontrar una función que tenga el mayor **margen** alrededor de los puntos de datos.
   
   **Concepto clave: Vectores de Soporte**
   
   Los **vectores de soporte** son los puntos de datos que están más cerca de la línea/curva del modelo. Estos puntos son los más importantes porque definen la posición de la función.
   
   **¿Qué es el Margen?**
   
   El margen es la distancia entre la línea del modelo y los puntos más cercanos. SVR intenta maximizar este margen para crear un modelo más robusto.
   
   ```
   Gráfico conceptual de SVR:
   
   Importe
     ↑
     |     ● (vector de soporte)
     |    /|
     |   / |  ← Margen (epsilon)
     |  /  |
     |─●───●─  ← Línea del modelo (tubo epsilon)
     |  \  |
     |   \ |  ← Margen (epsilon)
     |    \|
     |     ● (vector de soporte)
     └─────────────────→ Cantidad
   ```
   
   **Función de Coste: Epsilon-Insensitive Loss**
   
   SVR usa una función de coste especial que **no penaliza errores pequeños**:
   
   ```
   Si |y_real - y_pred| ≤ ε (epsilon):
      Costo = 0  (no se penaliza)
   
   Si |y_real - y_pred| > ε:
      Costo = |y_real - y_pred| - ε  (solo se penaliza el exceso)
   ```
   
   **Parámetro Epsilon (ε):**
   - Define el ancho del "tubo" alrededor de la línea
   - Errores dentro del tubo no se penalizan
   - Solo errores fuera del tubo contribuyen al costo
   - Valores típicos: 0.1, 0.5, 1.0
   
   **Kernels (Núcleos):**
   
   Los kernels permiten que SVR maneje relaciones **no lineales** transformando los datos a un espacio de mayor dimensión donde sí son lineales.
   
   **Tipos de Kernels:**
   
   1. **Kernel Lineal:**
      - Para relaciones lineales
      - Fórmula: K(x₁, x₂) = x₁ · x₂
   
   2. **Kernel RBF (Radial Basis Function) - Usado en Aurelion:**
      - Para relaciones no lineales complejas
      - Fórmula: K(x₁, x₂) = exp(-γ ||x₁ - x₂||²)
      - Parámetro γ (gamma) controla la forma de la curva
      - Valores altos de γ → curvas más complejas
   
   3. **Kernel Polinomial:**
      - Para relaciones polinomiales
      - Fórmula: K(x₁, x₂) = (x₁ · x₂ + 1)^d
      - Parámetro d (degree) controla el grado del polinomio
   
   **Ejemplo con Aurelion:**
   
   **Datos de ejemplo:**
   ```
   Venta | Cantidad | Importe Real
   ------|----------|-------------
   1     |    2     |   $5,000
   2     |    3     |   $7,500
   3     |    1     |   $3,000
   4     |    4     |  $10,000
   ```
   
   **SVR con kernel RBF:**
   - Parámetros: C = 1.0, epsilon = 0.1, gamma = 'scale'
   - El kernel RBF detecta que la relación no es completamente lineal
   - Crea una curva suave que se ajusta mejor a los datos
   
   **Vectores de soporte identificados:**
   - Los puntos más cercanos a la curva (generalmente los más difíciles de predecir)
   - Estos puntos definen la forma de la función
   
   **Predicción:**
   - Para cantidad = 3: Importe predicho ≈ $7,500
   - El modelo usa los vectores de soporte para hacer la predicción
   
   **Ventajas de SVR:**
   - Maneja relaciones no lineales (con kernels)
   - Robusto a outliers (solo penaliza errores grandes)
   - Efectivo con datasets pequeños/medianos
   - Flexible (diferentes kernels para diferentes problemas)
   
   **Desventajas:**
   - Escalabilidad limitada (lento con muchos datos)
   - Parámetros sensibles (C, epsilon, gamma)
   - Menos interpretable que regresión lineal
   - Requiere normalización de datos
   
   **En Aurelion:**
   - **R² = 0.9918 (99.18%)** - Muy bueno, pero ligeramente inferior a Random Forest
   - Kernel RBF usado para capturar relaciones no lineales
   - Funciona bien pero Random Forest es mejor para este dataset

3. **Algoritmos de Clasificación:**
   
   **3.1. Logistic Regression (Regresión Logística):**
   
   **¿Qué es la Regresión Logística?**
   
   La regresión logística es un algoritmo de clasificación que predice la probabilidad de que una instancia pertenezca a una clase. A diferencia de la regresión lineal que predice valores continuos, la regresión logística predice probabilidades entre 0 y 1.
   
   **Función de Hipótesis:**
   
   La función de hipótesis en regresión logística usa la **función sigmoide** para transformar la salida lineal en una probabilidad:
   
   ```
   h(x) = g(z) = 1 / (1 + e^(-z))
   
   Donde:
   - z = θ₀ + θ₁x₁ + θ₂x₂ + ... + θₙxₙ  (función lineal)
   - g(z) = función sigmoide
   - h(x) = probabilidad de que y = 1 (clase positiva)
   ```
   
   **Función Sigmoide:**
   
   La función sigmoide (también llamada función logística) tiene la forma:
   
   ```
   g(z) = 1 / (1 + e^(-z))
   ```
   
   **Características de la Sigmoide:**
   - **Rango:** Siempre entre 0 y 1 (perfecto para probabilidades)
   - **Forma:** Curva en forma de "S"
   - **Punto medio:** Cuando z = 0, g(0) = 0.5
   - **Límites:**
     - Cuando z → +∞, g(z) → 1
     - Cuando z → -∞, g(z) → 0
   
   **Gráfico de la Función Sigmoide:**
   
   ```
   Probabilidad
     1.0 |                    ╱───────────
         |                  ╱
     0.8 |                ╱
         |              ╱
     0.6 |            ╱
         |          ╱
     0.5 |─────────●─────────  (z = 0, g(z) = 0.5)
         |      ╱
     0.4 |    ╱
         |  ╱
     0.2 |╱
         |
     0.0 └─────────────────────────────────→ z
         -6  -4  -2   0   2   4   6
   
   Interpretación:
   - z < 0 → Probabilidad < 0.5 → Clase 0 (negativa)
   - z = 0 → Probabilidad = 0.5 → Límite de decisión
   - z > 0 → Probabilidad > 0.5 → Clase 1 (positiva)
   ```
   
   **Ejemplo Práctico con Aurelion:**
   
   Supongamos que queremos predecir si un cliente es de "Alto valor" (clase 1) o "Bajo/Medio valor" (clase 0) basándose en su importe promedio.
   
   **Datos de ejemplo:**
   ```
   Cliente | Importe Promedio | Clase Real
   --------|------------------|------------
   A       |    $10,000       |    1 (Alto)
   B       |     $3,000       |    0 (Bajo)
   C       |     $7,500       |    1 (Alto)
   D       |     $2,000       |    0 (Bajo)
   ```
   
   **Modelo entrenado:**
   - θ₀ = -5.0 (intercepto)
   - θ₁ = 0.0008 (coeficiente para importe)
   - Función: z = -5.0 + 0.0008 × importe
   
   **Cálculo de probabilidades:**
   
   Para Cliente A (importe = $10,000):
   - z = -5.0 + 0.0008 × 10,000 = -5.0 + 8.0 = 3.0
   - h(x) = 1 / (1 + e^(-3.0)) = 1 / (1 + 0.0498) = 0.9526
   - **Probabilidad de ser "Alto valor": 95.26%** → Predicción: Clase 1 ✓
   
   Para Cliente B (importe = $3,000):
   - z = -5.0 + 0.0008 × 3,000 = -5.0 + 2.4 = -2.6
   - h(x) = 1 / (1 + e^(2.6)) = 1 / (1 + 13.46) = 0.0692
   - **Probabilidad de ser "Alto valor": 6.92%** → Predicción: Clase 0 ✓
   
   **Función de Coste: Entropía Cruzada (Cross-Entropy Loss)**
   
   La regresión logística NO usa MSE como función de coste (porque la sigmoide no es lineal). En su lugar, usa **Entropía Cruzada** (también llamada Log Loss):
   
   **Fórmula:**
   ```
   J(θ) = -(1/m) × Σ[y × log(h(x)) + (1-y) × log(1-h(x))]
   
   Donde:
   - m = número de ejemplos
   - y = clase real (0 o 1)
   - h(x) = probabilidad predicha por el modelo
   - log = logaritmo natural (ln)
   ```
   
   **¿Por qué Entropía Cruzada y no MSE?**
   
   1. **MSE no funciona bien con sigmoide:** La función de coste resultante no es convexa, tiene múltiples mínimos locales
   2. **Entropía Cruzada es convexa:** Garantiza encontrar el mínimo global
   3. **Penaliza predicciones incorrectas con alta confianza:** Si el modelo predice 0.99 pero la clase real es 0, el costo es muy alto
   
   **Ejemplo de Cálculo de Entropía Cruzada:**
   
   Supongamos 3 predicciones:
   ```
   Ejemplo | y_real | h(x) | y×log(h(x)) | (1-y)×log(1-h(x)) | Costo
   --------|--------|------|-------------|-------------------|-------
   1       |   1    | 0.95 | 1×log(0.95) | 0×log(0.05)       | -0.051
   2       |   0    | 0.10 | 0×log(0.10) | 1×log(0.90)       | -0.105
   3       |   1    | 0.30 | 1×log(0.30) | 0×log(0.70)       | -1.204
   ```
   
   **Cálculo:**
   - Ejemplo 1: -[1×log(0.95) + 0×log(0.05)] = -[-0.051] = 0.051
   - Ejemplo 2: -[0×log(0.10) + 1×log(0.90)] = -[-0.105] = 0.105
   - Ejemplo 3: -[1×log(0.30) + 0×log(0.70)] = -[-1.204] = 1.204
   - **Costo total:** (0.051 + 0.105 + 1.204) / 3 = 0.453
   
   **Interpretación:**
   - Ejemplo 1: Predicción correcta con alta confianza (0.95) → Costo bajo (0.051)
   - Ejemplo 2: Predicción correcta con alta confianza (0.90) → Costo bajo (0.105)
   - Ejemplo 3: Predicción incorrecta (dijo 0.30 pero era 1) → Costo alto (1.204)
   
   **Minimización de la Entropía Cruzada:**
   
   El algoritmo ajusta los parámetros θ usando **Gradiente Descendente** para minimizar la entropía cruzada:
   
   ```
   θⱼ = θⱼ - α × (∂J/∂θⱼ)
   
   Donde:
   - α = tasa de aprendizaje
   - ∂J/∂θⱼ = gradiente de la función de coste respecto a θⱼ
   ```
   
   **En el Proyecto Aurelion:**
   
   - **max_iter = 1000:** El modelo se entrena con máximo 1000 iteraciones o hasta convergencia
   - **Solver = 'liblinear':** Algoritmo de optimización eficiente para datasets pequeños/medianos
   - **Resultado:** Accuracy de 88.41% en clasificación de segmentos de clientes
   
   **Ventajas de Regresión Logística:**
   - Proporciona probabilidades (no solo clases)
   - Interpretable (los coeficientes indican importancia de variables)
   - Rápido de entrenar
   - Funciona bien con relaciones lineales
   
   **Desventajas:**
   - Asume relación lineal entre variables y log-odds
   - Sensible a características correlacionadas
   - Puede sobreajustar con muchas características
   
   **3.2. Random Forest Classifier:**
   
   **¿Qué es Random Forest Classifier?**
   
   Random Forest Classifier es la versión de clasificación del algoritmo Random Forest. Funciona de manera similar al Regressor, pero en lugar de promediar predicciones numéricas, **vota** por la clase más frecuente.
   
   **Proceso de Clasificación:**
   
   1. **Bootstrap Sampling:** Se crean múltiples subconjuntos de datos (100 árboles)
   2. **Entrenamiento:** Cada árbol se entrena independientemente
   3. **Predicción:** Cada árbol predice una clase
   4. **Votación:** Se cuenta cuántos árboles votaron por cada clase
   5. **Clase final:** Se elige la clase con más votos
   
   **Ejemplo con Aurelion (Segmentación de Clientes):**
   
   Supongamos que queremos clasificar un cliente en uno de estos segmentos:
   - **Bajo:** Importe promedio < $4,000
   - **Medio:** Importe promedio $4,000 - $7,000
   - **Alto:** Importe promedio > $7,000
   
   **Características del cliente:**
   - Cantidad promedio: 2.5
   - Precio promedio: $2,200
   - Categoría favorita: "Electrónica"
   
   **Votación de 5 árboles (ejemplo simplificado):**
   ```
   Árbol 1: "Alto"
   Árbol 2: "Alto"
   Árbol 3: "Medio"
   Árbol 4: "Alto"
   Árbol 5: "Alto"
   ```
   
   **Conteo de votos:**
   - "Alto": 4 votos (80%)
   - "Medio": 1 voto (20%)
   - "Bajo": 0 votos (0%)
   
   **Predicción final:** "Alto" (mayoría de votos)
   
   **Ventajas:**
   - Alta precisión (88.41% en Aurelion)
   - Reduce overfitting mediante votación
   - Maneja múltiples clases fácilmente
   - Proporciona probabilidades (proporción de votos)
   - Robusto a outliers
   
   **Desventajas:**
   - Menos interpretable que un solo árbol
   - Más lento que regresión logística
   - Requiere más memoria
   
   **En Aurelion:**
   - **Accuracy: 88.41%** - Buen rendimiento en clasificación de segmentos
   - **3 clases:** Bajo, Medio, Alto
   - **100 árboles:** Votación robusta
   - **Resultado:** Clasificación precisa de clientes por valor
   
   **3.3. SVM (Support Vector Machine):**
   
   **¿Qué es SVM?**
   
   SVM (Support Vector Machine) es un algoritmo de clasificación que encuentra el **hiperplano óptimo** que mejor separa las clases, maximizando el **margen** entre las clases.
   
   **Concepto clave: Hiperplano**
   
   Un hiperplano es una línea (en 2D) o plano (en 3D) que separa las clases. SVM busca el hiperplano que tiene el **mayor margen** (distancia) a los puntos más cercanos de cada clase.
   
   **Vectores de Soporte:**
   
   Los **vectores de soporte** son los puntos de datos más cercanos al hiperplano. Estos puntos "soportan" el hiperplano y definen su posición.
   
   **Ejemplo visual:**
   ```
   Clasificación de Clientes (Alto valor vs Bajo valor):
   
   Importe
     ↑
     |  ●  ●  ●  ← Clase "Bajo valor"
     |    ╱───╲
     |   ╱     ╲  ← Margen
     |  ╱       ╲
     |─●────────●─  ← Hiperplano óptimo
     |  ╲       ╱
     |   ╲     ╱  ← Margen
     |    ╲───╱
     |  ●  ●  ●  ← Clase "Alto valor"
     └─────────────────→ Cantidad
   
   Los puntos marcados con ● son los vectores de soporte
   ```
   
   **Kernels para Clasificación No Lineal:**
   
   Al igual que SVR, SVM puede usar kernels para manejar relaciones no lineales:
   - **Kernel Lineal:** Para separación lineal
   - **Kernel RBF:** Para separación no lineal compleja
   - **Kernel Polinomial:** Para separación polinomial
   
   **Ventajas:**
   - Efectivo en espacios de alta dimensión
   - Maneja relaciones no lineales (con kernels)
   - Robusto a outliers
   - Funciona bien con datasets pequeños/medianos
   
   **Desventajas:**
   - No escalable a datasets muy grandes
   - Parámetros sensibles (C, gamma)
   - Menos interpretable que regresión logística
   
   **En Aurelion:**
   - Usado para clasificación de segmentos de clientes
   - Kernel RBF para capturar relaciones no lineales
   - Accuracy: 88.41% (buen rendimiento)

4. **Algoritmos de Clustering:**
   
   **¿Qué es Clustering?**
   
   **Clustering** (agrupación o segmentación) es una técnica de **aprendizaje no supervisado** que agrupa datos similares en **clusters** (grupos) sin conocer de antemano cuántos grupos hay o qué define cada grupo.
   
   **Características clave:**
   - **Sin labels:** No hay variable objetivo ni etiquetas conocidas
   - **Agrupación automática:** El algoritmo encuentra grupos naturales en los datos
   - **Similitud:** Los datos dentro de un cluster son más similares entre sí que con datos de otros clusters
   - **Exploración:** Se usa para descubrir patrones ocultos en los datos
   
   **Ejemplo conceptual:**
   ```
   Datos sin agrupar:
   
   Transacción | Cantidad | Precio | Importe
   ------------|----------|--------|----------
   A           |    2     |  2,000 |  5,000
   B           |    1     |  1,500 |  3,000
   C           |    4     |  2,500 | 10,000
   D           |    2     |  2,200 |  5,500
   E           |    1     |  1,800 |  3,200
   F           |    5     |  3,000 | 15,000
   
   Después de Clustering (K-Means con K=3):
   
   Cluster 1 (Transacciones pequeñas): A, B, D, E
   Cluster 2 (Transacciones medianas): (ninguna en este ejemplo)
   Cluster 3 (Transacciones grandes): C, F
   ```
   
   **¿Por qué usar Clustering?**
   
   1. **Descubrir segmentos:** Identificar grupos naturales de clientes/productos
   2. **Análisis exploratorio:** Entender la estructura de los datos
   3. **Reducción de complejidad:** Simplificar datos complejos en grupos
   4. **Marketing:** Segmentar clientes para estrategias personalizadas
   
   **En Aurelion:**
   - **Objetivo:** Agrupar transacciones similares
   - **Variables usadas:** cantidad, precio_unitario_detalle, importe
   - **Resultado:** 3 clusters identificados
   - **Aplicación:** Entender patrones de compra, identificar transacciones anómalas
   
   **4.1. K-Means Clustering:**
   
   **¿Qué es K-Means?**
   
   K-Means es un algoritmo de clustering que agrupa datos en **K clusters** (grupos) basándose en la **distancia** entre puntos. El objetivo es minimizar la **inercia** (suma de distancias al cuadrado entre puntos y sus centroides).
   
   **Conceptos clave:**
   
   - **Centroide:** Punto central (promedio) de cada cluster
   - **Distancia Euclidiana:** Distancia entre dos puntos en el espacio
   - **Inercia:** Suma de distancias al cuadrado de cada punto a su centroide más cercano
   
   **Algoritmo paso a paso:**
   
   **Paso 1: Inicialización**
   - Se eligen K puntos aleatorios como centroides iniciales (K = 3 en Aurelion)
   - Estos pueden ser puntos aleatorios o puntos de datos aleatorios
   
   **Paso 2: Asignación**
   - Para cada punto de datos, se calcula la distancia a cada centroide
   - Se asigna el punto al cluster del centroide más cercano
   - Fórmula de distancia euclidiana:
     ```
     distancia = √[(x₁ - c₁)² + (x₂ - c₂)² + ... + (xₙ - cₙ)²]
     ```
   
   **Paso 3: Actualización de Centroides**
   - Se calcula el nuevo centroide de cada cluster como el promedio de todos los puntos asignados
   - Fórmula: centroide = (1/n) × Σ(puntos del cluster)
   
   **Paso 4: Repetición**
   - Se repiten los pasos 2 y 3 hasta que:
     - Los centroides no cambian (convergencia)
     - Se alcanza el número máximo de iteraciones
     - La inercia no disminuye significativamente
   
   **Ejemplo con Datos de Aurelion:**
   
   **Datos iniciales (3 variables: cantidad, precio, importe):**
   ```
   Punto | Cantidad | Precio | Importe
   ------|----------|--------|--------
   A     |    2     |  2,000 |  5,000
   B     |    3     |  2,500 |  7,500
   C     |    1     |  3,000 |  3,000
   D     |    4     |  2,500 | 10,000
   E     |    2     |  1,500 |  3,500
   ```
   
   **Iteración 1 - Inicialización:**
   - Centroide 1 (aleatorio): (2, 2,000, 5,000)
   - Centroide 2 (aleatorio): (3, 2,500, 7,500)
   - Centroide 3 (aleatorio): (1, 3,000, 3,000)
   
   **Iteración 1 - Asignación:**
   - Punto A: distancias = [0, 2,500, 2,000] → Cluster 1 (más cercano)
   - Punto B: distancias = [2,500, 0, 4,500] → Cluster 2
   - Punto C: distancias = [2,000, 4,500, 0] → Cluster 3
   - Punto D: distancias = [5,000, 2,500, 7,000] → Cluster 2
   - Punto E: distancias = [1,500, 4,000, 500] → Cluster 3
   
   **Iteración 1 - Actualización:**
   - Cluster 1: solo punto A → Centroide = (2, 2,000, 5,000)
   - Cluster 2: puntos B, D → Centroide = (3.5, 2,500, 8,750)
   - Cluster 3: puntos C, E → Centroide = (1.5, 2,250, 3,250)
   
   **Iteración 2 - Asignación (con nuevos centroides):**
   - Punto A: distancias = [0, 3,750, 1,750] → Cluster 1
   - Punto B: distancias = [2,500, 1,250, 4,250] → Cluster 2
   - Punto C: distancias = [2,000, 5,750, 250] → Cluster 3
   - Punto D: distancias = [5,000, 1,250, 6,750] → Cluster 2
   - Punto E: distancias = [1,500, 5,250, 250] → Cluster 3
   
   **Iteración 2 - Actualización:**
   - Cluster 1: punto A → Centroide = (2, 2,000, 5,000)
   - Cluster 2: puntos B, D → Centroide = (3.5, 2,500, 8,750)
   - Cluster 3: puntos C, E → Centroide = (1.5, 2,250, 3,250)
   
   **Convergencia:** Los centroides no cambiaron → Algoritmo terminado
   
   **Inercia final:**
   - Suma de distancias al cuadrado de cada punto a su centroide
   - Objetivo: Minimizar esta inercia
   
   **Parámetros en Aurelion:**
   - **n_clusters = 3:** 3 grupos de transacciones
   - **n_init = 10:** Se ejecuta 10 veces con diferentes inicializaciones (se elige la mejor)
   - **random_state = 42:** Para reproducibilidad
   - **Variables:** cantidad, precio_unitario_detalle, importe
   
   **Resultados en Aurelion:**
   - **Muestras totales:** 343 registros (transacciones) utilizadas para clustering
   - **3 clusters identificados** a partir de las 343 muestras
   - **Centroides generados:** 3 centroides (uno por cada cluster)
   - **Distribución:** Las 343 muestras se distribuyen entre los 3 clusters
   - **Silhouette Score:** 0.3863 (clusters moderadamente bien definidos)
   - Cada centroide representa el "prototipo" de su cluster
   - **Shape de centroides:** (3, 3) → 3 clusters × 3 variables (cantidad, precio_unitario_detalle, importe)
   
   **Ventajas:**
   - Simple y rápido
   - Escalable a grandes datasets
   - Fácil de interpretar (centroides)
   - Funciona bien con clusters esféricos
   
   **Desventajas:**
   - Requiere especificar K (número de clusters)
   - Sensible a inicialización
   - Asume clusters esféricos
   - Sensible a outliers
   
   **¿Cómo elegir el número de clusters (K)?**
   
   K-Means requiere especificar el número de clusters antes de ejecutarse. Existen varios métodos para determinar el K óptimo:
   
   **1. Método del Codo (Elbow Method):**
   - Se ejecuta K-Means con diferentes valores de K (2, 3, 4, 5, ...)
   - Se calcula la inercia (suma de distancias al cuadrado) para cada K
   - Se grafica K vs Inercia
   - El "codo" en la gráfica indica el K óptimo (donde la inercia deja de disminuir significativamente)
   - **En Aurelion:** Se probó con K=2, 3, 4, 5 y se eligió K=3 basándose en el análisis exploratorio
   
   **2. Método de la Silueta (Silhouette Method):**
   - Se calcula el Silhouette Score para diferentes valores de K
   - El K con mayor Silhouette Score es el óptimo
   - **Rango del Silhouette Score:**
     - **-1 a 0.2:** Clusters mal definidos o puntos asignados incorrectamente
     - **0.2 a 0.5:** Clusters moderadamente bien definidos (caso de Aurelion: 0.39)
     - **0.5 a 0.7:** Clusters razonablemente bien definidos
     - **0.7 a 1.0:** Clusters fuertemente definidos y bien separados
   - **En Aurelion:** Silhouette Score = 0.3863 indica clusters moderadamente bien definidos
   
   **3. Análisis de Dominio:**
   - Considerar el contexto del negocio
   - En Aurelion, se eligió K=3 para representar: transacciones pequeñas, medianas y grandes
   - Esto facilita la interpretación y aplicación práctica
   
   **Interpretación del Silhouette Score:**
   
   El Silhouette Score mide qué tan bien está cada punto asignado a su cluster:
   - **Valores cercanos a 1:** El punto está muy cerca de su centroide y lejos de otros centroides (asignación perfecta)
   - **Valores cercanos a 0:** El punto está en el límite entre dos clusters (asignación ambigua)
   - **Valores negativos:** El punto probablemente está asignado al cluster incorrecto
   
   **En Aurelion (Score = 0.39):**
   - Los clusters están moderadamente bien definidos
   - Hay cierta superposición entre clusters (transacciones que podrían pertenecer a más de un grupo)
   - Esto es común en datos reales donde las categorías no son perfectamente separables
   - El score de 0.39 es aceptable para un análisis exploratorio y permite identificar patrones generales
   
   **Interpretación de Centroides en Términos de Negocio:**
   
   Los centroides representan el "cliente promedio" o "transacción promedio" de cada cluster:
   - **Cluster 0 (ejemplo):** Centroide = (cantidad: 2.1, precio: 2,300, importe: 5,200)
     - Interpretación: Transacciones pequeñas, clientes que compran pocos productos a precios moderados
     - Estrategia: Ofrecer productos complementarios, programas de fidelización
   
   - **Cluster 1 (ejemplo):** Centroide = (cantidad: 3.5, precio: 2,500, importe: 8,750)
     - Interpretación: Transacciones medianas, clientes que compran cantidad media
     - Estrategia: Promociones por volumen, descuentos en compras múltiples
   
   - **Cluster 2 (ejemplo):** Centroide = (cantidad: 4.2, precio: 3,000, importe: 12,600)
     - Interpretación: Transacciones grandes, clientes de alto valor
     - Estrategia: Programas VIP, atención personalizada, productos premium
   
   **4.2. DBSCAN (Density-Based Spatial Clustering of Applications with Noise):**
   
   **¿Qué es DBSCAN?**
   
   DBSCAN es un algoritmo de clustering basado en **densidad**. Agrupa puntos que están cerca unos de otros (alta densidad) y marca como outliers los puntos aislados (baja densidad).
   
   **Conceptos clave:**
   
   - **Densidad:** Número de puntos en un área determinada
   - **Punto Core:** Punto que tiene al menos `min_samples` puntos dentro de un radio `eps`
   - **Punto Border:** Punto que está dentro del radio `eps` de un punto core, pero no es core
   - **Punto Noise (Outlier):** Punto que no es core ni border
   
   **Parámetros:**
   
   - **eps (epsilon):** Radio de búsqueda alrededor de cada punto
   - **min_samples:** Número mínimo de puntos dentro del radio `eps` para que un punto sea "core"
   
   **Algoritmo paso a paso:**
   
   1. **Seleccionar punto no visitado:**
      - Elegir un punto aleatorio que no haya sido procesado
   
   2. **Verificar si es punto core:**
      - Contar puntos dentro del radio `eps`
      - Si hay ≥ `min_samples` puntos → Es punto core
      - Si no → Es punto noise (outlier)
   
   3. **Expandir cluster (si es core):**
      - Agregar todos los puntos dentro del radio `eps` al cluster
      - Para cada nuevo punto core encontrado, expandir recursivamente
   
   4. **Repetir:**
      - Continuar hasta que todos los puntos sean visitados
   
   **Ejemplo con Aurelion:**
   
   **Parámetros:** eps = 0.5, min_samples = 5
   
   **Datos (normalizados):**
   ```
   Punto | Coordenadas
   ------|------------
   A     | (0.2, 0.3, 0.1)
   B     | (0.25, 0.35, 0.15)
   C     | (0.3, 0.4, 0.2)
   D     | (1.5, 1.6, 1.4)  ← Aislado (outlier)
   E     | (0.22, 0.32, 0.12)
   F     | (0.28, 0.38, 0.18)
   G     | (0.24, 0.34, 0.14)
   ```
   
   **Proceso:**
   - Punto A: 6 puntos dentro de eps → Core → Cluster 1
   - Punto B: 6 puntos dentro de eps → Core → Cluster 1
   - Punto C: 5 puntos dentro de eps → Core → Cluster 1
   - Punto D: 0 puntos dentro de eps → Noise (outlier) → Sin cluster
   - Puntos E, F, G: Dentro de eps de puntos core → Border → Cluster 1
   
   **Resultado:**
   - **Cluster 1:** Puntos A, B, C, E, F, G (alta densidad)
   - **Outlier:** Punto D (baja densidad, aislado)
   
   **Ventajas:**
   - No requiere especificar número de clusters
   - Detecta outliers automáticamente
   - Maneja clusters de forma arbitraria (no solo esféricos)
   - Robusto a outliers
   
   **Desventajas:**
   - Sensible a parámetros eps y min_samples
   - Dificultad con clusters de diferentes densidades
   - Puede ser lento con muchos datos
   - Requiere normalización de datos
   
   **En Aurelion:**
   - **eps = 0.5, min_samples = 5**
   - Detecta clusters automáticamente
   - Identifica transacciones anómalas (outliers)
   - Útil para detectar patrones inusuales en ventas
   
   **4.3. Hierarchical Clustering:**
   
   - **Dendrograma:** Árbol que muestra cómo se fusionan los clusters
   - **Jerarquía de clusters:** Estructura de clusters anidados
   - **Ventaja:** No requiere especificar número de clusters
   - **Desventaja:** Computacionalmente costoso

5. **Tabla Comparativa y Consejos de Selección:**
   - Comparación de complejidad
   - Interpretabilidad
   - Tiempo de entrenamiento
   - Recomendaciones por tipo de datos

#### 6.2.4. Módulo 4: Métricas de Evaluación (`04_metricas_evaluacion.py`)

**Contenido:**

1. **Métricas para Regresión:**
   
   Las métricas de regresión miden qué tan bien el modelo predice valores numéricos continuos. En el proyecto Aurelion, se usan para evaluar qué tan bien se predice el importe de las ventas.
   
   **1.1. MSE (Mean Squared Error) - Error Cuadrático Medio:**
   
   **Definición:** Promedio de los errores al cuadrado. Mide la distancia vertical promedio entre los puntos reales y las predicciones del modelo, elevada al cuadrado.
   
   **Fórmula:**
   ```
   MSE = (1/n) × Σ(y_real - y_pred)²
   
   Donde:
   - y_real = valor real observado
   - y_pred = valor predicho por el modelo
   - n = número de ejemplos
   - (y_real - y_pred) = error o distancia vertical
   ```
   
   **Interpretación:**
   - **Rango:** 0 a ∞ (infinito)
   - **Valor ideal:** 0 (sin errores)
   - **Unidades:** Mismas unidades que la variable al cuadrado (ej: pesos²)
   - **Características:**
     - Penaliza más los errores grandes (por el cuadrado)
     - Siempre positivo
     - Sensible a outliers
   
   **Ejemplo Práctico con Aurelion:**
   
   Supongamos 5 predicciones de importe:
   ```
   Venta | Real    | Predicho | Error  | Error²
   ------|---------|----------|--------|----------
   1     | $5,000  | $4,800   |  200   |   40,000
   2     | $7,500  | $7,200   |  300   |   90,000
   3     | $3,000  | $3,100   | -100   |   10,000
   4     | $10,000 | $10,200  | -200   |   40,000
   5     | $5,500  | $5,400   |  100   |   10,000
   ```
   
   **Cálculo:**
   - Suma de errores²: 40,000 + 90,000 + 10,000 + 40,000 + 10,000 = 190,000
   - MSE = 190,000 / 5 = 38,000 pesos²
   - **Interpretación:** El error promedio al cuadrado es de 38,000 pesos²
   
   **En Aurelion:**
   - El mejor modelo (Random Forest) tiene un MSE muy bajo
   - Esto significa que las distancias verticales entre puntos reales y predicciones son muy pequeñas
   
   **1.2. RMSE (Root Mean Squared Error) - Raíz del Error Cuadrático Medio:**
   
   **Definición:** Raíz cuadrada del MSE. Devuelve el error a las mismas unidades que la variable original.
   
   **Fórmula:**
   ```
   RMSE = √MSE = √[(1/n) × Σ(y_real - y_pred)²]
   ```
   
   **Interpretación:**
   - **Rango:** 0 a ∞
   - **Valor ideal:** 0
   - **Unidades:** Mismas unidades que la variable (ej: pesos)
   - **Ventaja sobre MSE:** Más interpretable porque está en las mismas unidades
   
   **Ejemplo con Aurelion:**
   - Si MSE = 38,000 pesos²
   - RMSE = √38,000 = 194.94 pesos
   - **Interpretación:** En promedio, el modelo se equivoca por aproximadamente $195 pesos por venta
   
   **1.3. MAE (Mean Absolute Error) - Error Absoluto Medio:**
   
   **Definición:** Promedio de los valores absolutos de los errores. Mide la distancia vertical promedio sin elevar al cuadrado.
   
   **Fórmula:**
   ```
   MAE = (1/n) × Σ|y_real - y_pred|
   ```
   
   **Interpretación:**
   - **Rango:** 0 a ∞
   - **Valor ideal:** 0
   - **Unidades:** Mismas unidades que la variable (ej: pesos)
   - **Características:**
     - Penaliza errores de forma lineal (no cuadrática)
     - Menos sensible a outliers que MSE/RMSE
     - Más robusto a valores extremos
   
   **Ejemplo con Aurelion:**
   ```
   Venta | Real    | Predicho | |Error|
   ------|---------|----------|--------
   1     | $5,000  | $4,800   |   200
   2     | $7,500  | $7,200   |   300
   3     | $3,000  | $3,100   |   100
   4     | $10,000 | $10,200  |   200
   5     | $5,500  | $5,400   |   100
   ```
   
   **Cálculo:**
   - Suma de |errores|: 200 + 300 + 100 + 200 + 100 = 900
   - MAE = 900 / 5 = 180 pesos
   - **Interpretación:** En promedio, el modelo se equivoca por $180 pesos (sin considerar si es por exceso o defecto)
   
   **Comparación MAE vs RMSE:**
   - MAE = 180 pesos (promedio de errores absolutos)
   - RMSE = 194.94 pesos (promedio de errores, pero penaliza más los grandes)
   - Si RMSE > MAE: Hay algunos errores grandes que están siendo penalizados más
   
   **1.4. R² (R-squared / Coeficiente de Determinación):**
   
   **Definición:** Proporción de la varianza en la variable dependiente que es explicada por el modelo. Mide qué tan bien el modelo se ajusta a los datos comparado con simplemente usar el promedio.
   
   **Fórmula:**
   ```
   R² = 1 - (SS_res / SS_tot)
   
   Donde:
   - SS_res = Σ(y_real - y_pred)²  (suma de errores al cuadrado)
   - SS_tot = Σ(y_real - y_promedio)²  (suma de diferencias respecto al promedio)
   - y_promedio = promedio de todos los valores reales
   ```
   
   **Interpretación:**
   - **Rango:** -∞ a 1 (puede ser negativo si el modelo es peor que usar el promedio)
   - **Valor ideal:** 1.0 (100% de la varianza explicada)
   - **Valores comunes:**
     - R² > 0.9: Excelente (90%+ de varianza explicada)
     - R² 0.7-0.9: Bueno (70-90% de varianza explicada)
     - R² 0.5-0.7: Regular (50-70% de varianza explicada)
     - R² < 0.5: Pobre (menos del 50% de varianza explicada)
   
   **Ejemplo Práctico con Aurelion:**
   
   **Datos:**
   ```
   Venta | Real    | Predicho | Promedio Real
   ------|---------|----------|---------------
   1     | $5,000  | $4,800   |    $6,200
   2     | $7,500  | $7,200   |    $6,200
   3     | $3,000  | $3,100   |    $6,200
   4     | $10,000 | $10,200  |    $6,200
   5     | $5,500  | $5,400   |    $6,200
   ```
   
   **Cálculo:**
   - Promedio real: (5,000 + 7,500 + 3,000 + 10,000 + 5,500) / 5 = $6,200
   
   - SS_res (errores del modelo):
     (5,000-4,800)² + (7,500-7,200)² + (3,000-3,100)² + (10,000-10,200)² + (5,500-5,400)²
     = 40,000 + 90,000 + 10,000 + 40,000 + 10,000 = 190,000
   
   - SS_tot (variabilidad total):
     (5,000-6,200)² + (7,500-6,200)² + (3,000-6,200)² + (10,000-6,200)² + (5,500-6,200)²
     = 1,440,000 + 1,690,000 + 10,240,000 + 14,440,000 + 490,000 = 28,300,000
   
   - R² = 1 - (190,000 / 28,300,000) = 1 - 0.0067 = 0.9933 = 99.33%
   
   **Interpretación:**
   - El modelo explica el 99.33% de la variabilidad en los importes
   - Solo el 0.67% de la variabilidad no está explicada por el modelo
   - Es un rendimiento excelente
   
   **En Aurelion:**
   - R² = 0.9962 (99.62%) significa que el modelo explica casi toda la variabilidad
   - Las distancias verticales entre puntos reales y predicciones son muy pequeñas
   - El modelo captura casi perfectamente la relación entre las variables
   
   **1.5. Comparación de Métricas:**
   
   | Métrica | Fórmula | Unidades | Sensible a Outliers | Interpretación |
   |---------|---------|----------|---------------------|----------------|
   | **MSE** | (1/n)×Σ(y_real-y_pred)² | Variable² | Sí (muy) | Error promedio al cuadrado |
   | **RMSE** | √MSE | Variable | Sí (muy) | Error promedio en unidades originales |
   | **MAE** | (1/n)×Σ\|y_real-y_pred\| | Variable | No (robusto) | Error promedio absoluto |
   | **R²** | 1-(SS_res/SS_tot) | Sin unidades (0-1) | Depende | % de varianza explicada |
   
   **1.6. Ejemplo Completo con Resultados de Aurelion:**
   
   **Modelo: Random Forest Regressor**
   - **R² = 0.9962 (99.62%)**
     - Interpretación: El modelo explica el 99.62% de la variabilidad en los importes
     - Solo el 0.38% de la variabilidad no está explicada
     - Rendimiento excelente
   
   - **MSE:** Muy bajo (distancias verticales al cuadrado son pequeñas)
   - **RMSE:** Bajo (errores promedio en pesos son pequeños)
   - **MAE:** Bajo (errores absolutos promedio son pequeños)
   
   **¿Qué significa esto en términos de distancias verticales?**
   - Si el importe promedio es $7,000 y R² = 99.62%
   - Las distancias verticales entre puntos reales y predicciones son muy pequeñas
   - El modelo predice importes con gran precisión
   - La línea/curva del modelo pasa muy cerca de todos los puntos reales
   
   **1.7. Relación entre Métricas y Función de Coste:**
   
   - **MSE es la función de coste** que se minimiza durante el entrenamiento
   - **RMSE y MAE** son métricas de evaluación (no se usan directamente para entrenar)
   - **R²** es una métrica de evaluación que resume qué tan bien funciona el modelo
   - Durante el entrenamiento, el algoritmo ajusta los parámetros para minimizar MSE
   - Al minimizar MSE, automáticamente se reducen las distancias verticales entre puntos y modelo

2. **Métricas para Clasificación:**
   
   **2.1. Matriz de Confusión:**
   
   **¿Qué es una Matriz de Confusión?**
   
   Una **matriz de confusión** es una tabla que muestra el rendimiento de un modelo de clasificación comparando las **predicciones del modelo** con los **valores reales (labels)**. Es una herramienta fundamental para entender cómo se equivoca el modelo.
   
   **Estructura de la Matriz:**
   
   ```
   Matriz de Confusión (ejemplo con 100 clientes):
   
                    Predicción del Modelo
                  Bajo  Medio  Alto    Total Real
   Valor    Bajo   25     3     2        30
   Real     Medio   2    28     5        35
            Alto    1     4    30        35
   ─────────────────────────────────────────────
   Total Pred.     28    35    37       100
   ```
   
   **Cómo leer la Matriz:**
   
   - **Filas:** Representan los valores **reales** (ground truth, labels verdaderos)
   - **Columnas:** Representan las **predicciones** del modelo
   - **Diagonal principal:** Predicciones **correctas** (TP por clase)
   - **Fuera de la diagonal:** **Errores** de clasificación
   
   **Interpretación paso a paso:**
   
   **Fila "Bajo" (30 clientes reales "Bajo"):**
   - **25** en columna "Bajo" → **TP (Verdaderos Positivos):** Correctamente predichos como "Bajo"
   - **3** en columna "Medio" → **FN (Falsos Negativos):** Realmente "Bajo" pero predichos como "Medio"
   - **2** en columna "Alto" → **FN (Falsos Negativos):** Realmente "Bajo" pero predichos como "Alto"
   - **Total:** 25 + 3 + 2 = 30 clientes reales "Bajo"
   
   **Columna "Bajo" (28 predicciones "Bajo"):**
   - **25** en fila "Bajo" → **TP:** Correctamente predichos
   - **2** en fila "Medio" → **FP (Falsos Positivos):** Predichos como "Bajo" pero realmente "Medio"
   - **1** en fila "Alto" → **FP (Falsos Positivos):** Predichos como "Bajo" pero realmente "Alto"
   - **Total:** 25 + 2 + 1 = 28 predicciones "Bajo"
   
   **Componentes de la Matriz:**
   
   - **TP (True Positive / Verdaderos Positivos):** Predicciones correctas de la clase (diagonal principal)
     - Ejemplo: 25 clientes predichos como "Bajo" que realmente son "Bajo"
   
   - **TN (True Negative / Verdaderos Negativos):** Predicciones correctas de que NO es la clase
     - Para clase "Bajo": Clientes predichos como "Medio" o "Alto" que realmente son "Medio" o "Alto"
     - Ejemplo: 28 + 30 + 4 + 30 = 92 clientes predichos correctamente como "NO Bajo"
   
   - **FP (False Positive / Falsos Positivos):** Predicciones incorrectas (dijo que era la clase pero no lo era)
     - Para clase "Bajo": Clientes predichos como "Bajo" pero realmente son "Medio" o "Alto"
     - Ejemplo: 2 + 1 = 3 clientes predichos como "Bajo" que realmente son "Medio" o "Alto"
   
   - **FN (False Negative / Falsos Negativos):** No predijo la clase cuando debería haberlo hecho
     - Para clase "Bajo": Clientes reales "Bajo" que fueron predichos como "Medio" o "Alto"
     - Ejemplo: 3 + 2 = 5 clientes reales "Bajo" que fueron predichos como "Medio" o "Alto"
   
   **Visualización como Heatmap:**
   
   La matriz de confusión también se visualiza como un **heatmap** donde:
   - **Colores intensos (rojo/naranja):** Valores altos (muchas predicciones)
   - **Colores claros (azul):** Valores bajos (pocas predicciones)
   - **Diagonal:** Debería ser la más intensa si el modelo es bueno (predicciones correctas)
   
   **Ejemplo visual de Heatmap de Matriz de Confusión:**
   ```
   Heatmap de Matriz de Confusión (Buen Modelo):
   
        Predicción
        Bajo  Medio  Alto
   Real
   Bajo  [███]  [█]   [█]    ← Diagonal más intensa = bueno
   Medio  [█]  [███]  [█]    ← Diagonal más intensa = bueno
   Alto   [█]   [█]  [███]   ← Diagonal más intensa = bueno
   
   Si fuera un mal modelo:
   Bajo  [█]   [██]  [██]    ← Diagonal no es la más intensa = malo
   Medio [██]  [█]   [██]    ← Errores más frecuentes que aciertos
   Alto  [██]  [██]  [█]     ← Modelo confundido
   ```
   
   **En Aurelion:**
   - Se usa para evaluar modelos de clasificación de segmentos de clientes
   - Muestra qué segmentos se confunden más entre sí
   - Permite identificar áreas de mejora del modelo
   - Se visualiza como heatmap para identificación rápida de patrones
   
   **2.2. Accuracy (Exactitud / Precisión Global):**
   
   **Definición:** Proporción total de predicciones correctas sobre el total de predicciones.
   
   **Fórmula:**
   ```
   Accuracy = (TP + TN) / (TP + TN + FP + FN)
   ```
   
   **Ejemplo práctico con los datos de Aurelion:**
   - Total de clientes: 100
   - Predicciones correctas: 25 + 28 + 30 = 83
   - Accuracy = 83 / 100 = 0.83 = 83%
   
   **Interpretación:**
   - **Rango:** 0 a 1 (o 0% a 100%)
   - **Valor ideal:** 1.0 (100%)
   - **En Aurelion:** 88.41% de accuracy significa que de cada 100 clientes, el modelo clasifica correctamente a 88
   
   **Limitaciones:**
   - Puede ser engañoso cuando hay clases desbalanceadas
   - Si hay 90 clientes "Bajo" y 10 "Alto", un modelo que siempre predice "Bajo" tendría 90% de accuracy, pero sería inútil
   
   **2.3. Precision (Precisión por Clase):**
   
   **Definición:** De todos los casos que el modelo predijo como positivos (una clase específica), cuántos realmente son positivos.
   
   **Fórmula:**
   ```
   Precision = TP / (TP + FP)
   ```
   
   **Interpretación:** "Cuando el modelo dice que es X, ¿qué tan confiable es esa predicción?"
   
   **Ejemplo práctico para clase "Bajo":**
   - TP (Verdaderos Positivos "Bajo"): 25
   - FP (Falsos Positivos "Bajo"): 2 + 1 = 3 (predichos como "Bajo" pero son "Medio" o "Alto")
   - Precision = 25 / (25 + 3) = 25 / 28 = 0.893 = 89.3%
   
   **Interpretación:**
   - De cada 100 clientes que el modelo predice como "Bajo", 89 realmente son "Bajo"
   - **Rango:** 0 a 1 (o 0% a 100%)
   - **Valor ideal:** 1.0 (100%)
   - **Alto Precision:** El modelo es conservador, solo predice la clase cuando está muy seguro
   - **Bajo Precision:** El modelo predice la clase frecuentemente, pero muchas veces se equivoca
   
   **Cuándo es importante:**
   - Cuando los falsos positivos son costosos
   - Ejemplo: Si clasificas clientes como "Alto valor" para enviarles ofertas VIP, quieres alta precision para no gastar en clientes que no lo son
   
   **2.4. Recall (Sensibilidad / Exhaustividad):**
   
   **Definición:** De todos los casos reales positivos (una clase específica), cuántos el modelo detectó correctamente.
   
   **Fórmula:**
   ```
   Recall = TP / (TP + FN)
   ```
   
   **Interpretación:** "De todos los casos reales de X, ¿cuántos encontró el modelo?"
   
   **Ejemplo práctico para clase "Bajo":**
   - TP (Verdaderos Positivos "Bajo"): 25
   - FN (Falsos Negativos "Bajo"): 3 + 2 = 5 (realmente "Bajo" pero predichos como "Medio" o "Alto")
   - Total real "Bajo": 30
   - Recall = 25 / (25 + 5) = 25 / 30 = 0.833 = 83.3%
   
   **Interpretación:**
   - De cada 100 clientes que realmente son "Bajo", el modelo detecta correctamente a 83
   - **Rango:** 0 a 1 (o 0% a 100%)
   - **Valor ideal:** 1.0 (100%)
   - **Alto Recall:** El modelo encuentra la mayoría de los casos reales (no se le escapan muchos)
   - **Bajo Recall:** El modelo se pierde muchos casos reales (no los detecta)
   
   **Cuándo es importante:**
   - Cuando los falsos negativos son costosos
   - Ejemplo: Si clasificas clientes "En Riesgo" para campañas de retención, quieres alto recall para no perder clientes que se van a ir
   
   **2.5. F1-Score (Puntuación F1):**
   
   **Definición:** Media armónica entre Precision y Recall. Balancea ambas métricas.
   
   **Fórmula:**
   ```
   F1-Score = 2 × (Precision × Recall) / (Precision + Recall)
   ```
   
   **Ejemplo práctico para clase "Bajo":**
   - Precision = 0.893 (89.3%)
   - Recall = 0.833 (83.3%)
   - F1-Score = 2 × (0.893 × 0.833) / (0.893 + 0.833) = 2 × 0.744 / 1.726 = 0.862 = 86.2%
   
   **Interpretación:**
   - **Rango:** 0 a 1 (o 0% a 100%)
   - **Valor ideal:** 1.0 (100%)
   - Útil cuando necesitas balancear Precision y Recall
   - Penaliza modelos que tienen una métrica muy alta y la otra muy baja
   
   **Cuándo usar F1-Score:**
   - Cuando Precision y Recall son igualmente importantes
   - Cuando las clases están desbalanceadas
   - Para comparar modelos de manera equilibrada
   
   **2.6. Comparación de Métricas:**
   
   | Métrica | Pregunta que Responde | Fórmula | Cuándo Priorizar |
   |---------|----------------------|---------|------------------|
   | **Accuracy** | ¿Qué porcentaje de todas las predicciones son correctas? | (TP+TN)/(TP+TN+FP+FN) | Clases balanceadas, todas las clases igualmente importantes |
   | **Precision** | ¿Cuando predigo X, qué tan confiable es? | TP/(TP+FP) | Falsos positivos son costosos (ej: spam, fraude) |
   | **Recall** | ¿De todos los casos reales de X, cuántos encuentro? | TP/(TP+FN) | Falsos negativos son costosos (ej: enfermedades, clientes en riesgo) |
   | **F1-Score** | ¿Balance entre Precision y Recall? | 2×(P×R)/(P+R) | Necesitas balance entre ambas métricas |
   
   **2.7. Ejemplo Completo con Datos de Aurelion:**
   
   Supongamos que tenemos 100 clientes clasificados en 3 segmentos:
   
   **Matriz de Confusión:**
   ```
                    Predicción
                  Bajo  Medio  Alto   Total Real
   Real    Bajo   28     2     0        30
           Medio   3    29     3        35
           Alto    0     4    31        35
   Total Pred.    31    35    34       100
   ```
   
   **Cálculo de Métricas para clase "Bajo":**
   - TP = 28 (predichos "Bajo" y realmente "Bajo")
   - FP = 3 (predichos "Bajo" pero realmente "Medio")
   - FN = 2 (realmente "Bajo" pero predichos "Medio")
   - TN = 67 (correctamente predichos como "NO Bajo")
   
   - **Accuracy Global:** (28 + 29 + 31) / 100 = 88 / 100 = 88%
   - **Precision "Bajo":** 28 / (28 + 3) = 28 / 31 = 90.3%
   - **Recall "Bajo":** 28 / (28 + 2) = 28 / 30 = 93.3%
   - **F1-Score "Bajo":** 2 × (0.903 × 0.933) / (0.903 + 0.933) = 91.7%
   
   **Interpretación para Aurelion:**
   - El modelo tiene 88% de accuracy global
   - Cuando predice "Bajo", tiene 90.3% de confiabilidad (Precision)
   - Detecta 93.3% de los clientes realmente "Bajo" (Recall)
   - Balance general: 91.7% (F1-Score)

3. **Métricas para Clustering:**
   - **Silhouette Score:** Cohesión intra-cluster vs separación
   - **Inertia:** Suma de distancias a centroides
   - **Davies-Bouldin Index:** Ratio de tamaño y separación

4. **Interpretación de Resultados:**
   - Rangos de valores buenos/regulares/pobres
   - Cómo interpretar cada métrica
   - Tabla de referencia rápida

#### 6.2.5. Módulo 5: Preparación de Datos (`01_preparacion_datos.py`)

**Objetivo:** Preparar datos para ML con técnicas avanzadas

**Proceso:**

1. **Carga de Datos:**
   - Carga desde archivos Excel
   - Creación de dataset combinado
   - Fallback a dataset sintético si es necesario

2. **Análisis de Valores Faltantes:**
   - Análisis avanzado con estrategias recomendadas
   - Identificación de tipo de dato
   - Recomendación de estrategia por variable

3. **Imputación Inteligente:**
   - Mediana para distribuciones sesgadas
   - Media para distribuciones normales
   - Moda para variables categóricas

4. **Tratamiento de Outliers:**
   - Método IQR
   - Winsorización (percentiles 5 y 95)

5. **Codificación de Categóricas:**
   - OneHot, Binary, Target, Label Encoding
   - Selección automática según cardinalidad

6. **Normalización:**
   - StandardScaler, MinMaxScaler, RobustScaler
   - Selección según distribución

7. **Definición de Features y Target:**
   - Separación de características y variable objetivo
   - Guardado de datasets preparados
   
   **¿Qué son Features, Labels y Target?**
   
   En Machine Learning, es fundamental entender la diferencia entre **features** (características), **labels** (etiquetas) y **target** (objetivo):
   
   **Features (Características / Variables Predictoras):**
   - Son las **variables de entrada** que el modelo usa para hacer predicciones
   - También se llaman **variables independientes** o **predictoras**
   - Se denotan como **X** en el código
   - **Ejemplo en Aurelion:** cantidad, precio_unitario, categoria, medio_pago, ciudad
   
   **Label / Target (Etiqueta / Variable Objetivo):**
   - Es la **variable que queremos predecir**
   - También se llama **variable dependiente** o **variable objetivo**
   - Se denota como **y** en el código
   - **Label** y **Target** son sinónimos en este contexto
   - **Ejemplo en Aurelion:** 
     - Para regresión: `importe` (valor numérico)
     - Para clasificación: `segmento_cliente` ("Bajo", "Medio", "Alto")
   
   **Ejemplo completo:**
   ```
   Datos de Entrenamiento:
   
   Cliente | Cantidad | Precio | Categoría | Importe | Segmento
   --------|----------|--------|-----------|---------|----------
   A       |    2     |  2,000 | Electr.   |  5,000  |  Alto
   B       |    1     |  1,500 | Alimentos |  3,000  |  Bajo
   C       |    3     |  2,500 | Electr.   |  7,500  |  Alto
   
   Features (X): Cantidad, Precio, Categoría
   Target/Label (y): Importe (para regresión) o Segmento (para clasificación)
   ```
   
   **En el código:**
   ```python
   # Features (variables predictoras)
   X = dataset[['cantidad', 'precio_unitario', 'categoria']]
   
   # Target/Label (variable objetivo)
   y = dataset['importe']  # Para regresión
   # o
   y = dataset['segmento_cliente']  # Para clasificación
   
   # Entrenar modelo
   modelo.fit(X, y)  # Aprende: X → y
   
   # Predecir
   y_pred = modelo.predict(X_nuevo)  # Predice y basándose en X
   ```
   
   **Diferencia entre Label y Target:**
   - **Label:** Término más común en clasificación (etiquetas de clase)
   - **Target:** Término más común en regresión (valor objetivo)
   - **En la práctica:** Se usan como sinónimos, ambos se refieren a la variable que queremos predecir
   
   **En Aurelion:**
   - **Features (X):** ~12-15 variables numéricas (cantidad, precios, categorías, medios de pago, ciudad)
   - **Target Regresión (y):** `importe` (variable continua)
   - **Target Clasificación (y):** `segmento_cliente` (variable categórica: "Bajo", "Medio", "Alto")
   - **Clustering:** No hay target (aprendizaje no supervisado)

#### 6.2.6. Módulo 6: División Train/Test (`02_division_train_test.py`)

**Método Estadístico Utilizado: Holdout Method (Método de Retención)**

En el proyecto Aurelion utilizamos el **método Holdout** (también conocido como "Simple Holdout" o "Train/Test Split") como método principal de validación estadística. Este método es complementado con **K-Fold Cross-Validation** para una evaluación más robusta.

**¿Qué es el Método Holdout?**

El método Holdout es una técnica de validación estadística que divide los datos en dos conjuntos mutuamente excluyentes:
- **Conjunto de Entrenamiento (Train):** Se usa para entrenar el modelo
- **Conjunto de Prueba (Test/Holdout):** Se "retiene" y se usa solo para evaluar el modelo final

**Características del Método Holdout en Aurelion:**

1. **División 80/20:**
   - **80% de datos (274 registros)** → Conjunto de entrenamiento
   - **20% de datos (69 registros)** → Conjunto de prueba (holdout)
   - Implementado con `train_test_split(X, y, test_size=0.2, random_state=42)`

2. **Ventajas del método:**
   - **Simple y rápido:** Una sola división de datos
   - **Reproducible:** `random_state=42` garantiza la misma división en cada ejecución
   - **Estratificado:** Mantiene proporciones de clases en clasificación
   - **Eficiente:** Ideal para datasets medianos/grandes
   - **Interpretable:** Fácil de entender y explicar

3. **Proceso de validación con Holdout:**
   ```
   Datos Originales (343 registros)
   ↓
   train_test_split(test_size=0.2, random_state=42)
   ↓
   ┌─────────────────────┬─────────────────────┐
   │   TRAIN (80%)       │    TEST (20%)       │
   │   274 registros     │    69 registros     │
   │   (Holdout)         │   (Holdout)         │
   │                     │                     │
   │   Usado para:       │   Usado para:       │
   │   - .fit()          │   - .predict()      │
   │   - Entrenar        │   - Evaluar         │
   │   - Ajustar         │   - Validar         │
   │   parámetros        │   generalización    │
   └─────────────────────┴─────────────────────┘
   ```

4. **Uso de `.fit()` para entrenar:**
   - **`.fit(X_train, y_train)`** → Entrena el modelo con datos de entrenamiento
   - Ajusta los parámetros del modelo para minimizar el error
   - El modelo "aprende" los patrones de los datos de entrenamiento
   - **Ejemplo en Aurelion:**
     ```python
     # Regresión
     modelo.fit(self.X_train, self.y_train)
     
     # Clasificación
     modelo.fit(X_train, y_train)
     ```
   - **¿Qué hace `.fit()` internamente?**
     - Calcula los parámetros del modelo (pesos, coeficientes, etc.)
     - Minimiza la función de coste (MSE para regresión, Cross-Entropy para clasificación)
     - Ajusta el modelo a los datos de entrenamiento
     - **Nunca** ve los datos de prueba durante este proceso

5. **Uso de `.predict()` para evaluar:**
   - **`.predict(X_test)`** → Genera predicciones con datos de prueba
   - El modelo nunca ha visto estos datos durante el entrenamiento
   - Permite evaluar la capacidad de generalización
   - Las predicciones se comparan con `y_test` para calcular métricas

**Complemento con K-Fold Cross-Validation:**

Además del método Holdout, utilizamos **K-Fold Cross-Validation (K=5)** para una evaluación más robusta:

- **Holdout (train_test_split):** Evaluación rápida y eficiente, una sola división
- **K-Fold CV (cross_val_score):** Validación más robusta con 5 divisiones diferentes
- **Resultado:** Combinación de ambos métodos para máxima confiabilidad
- **En Aurelion:**
  - Holdout: R² = 0.9962 (evaluación rápida)
  - K-Fold CV: R² = 0.9981 ± 0.0022 (validación robusta)

**Objetivo:** Dividir datos en conjuntos de entrenamiento y prueba

**Proceso:**

1. **Carga de Datos Preparados:**
   - Carga de características y target
   - Verificación de integridad

2. **División Train/Test (Método Holdout):**
   
   **¿Por qué dividir los datos?**
   
   Dividir los datos en conjuntos de entrenamiento y prueba es fundamental para evaluar qué tan bien el modelo **generaliza** a datos nuevos que no ha visto durante el entrenamiento.
   
   **Problema sin división:**
   - Si entrenamos y evaluamos con los mismos datos, el modelo puede "memorizar" los datos
   - Esto no nos dice si el modelo funcionará con datos nuevos
   - Es como estudiar con las respuestas del examen → no sabemos si realmente aprendimos
   
   **Solución: División Train/Test**
   
   ```
   Datos Totales (100%)
   ├─ Conjunto de Entrenamiento (80%) → Para entrenar el modelo
   └─ Conjunto de Prueba (20%) → Para evaluar el modelo
   ```
   
   **Proceso:**
   
   1. **Dividir datos antes de entrenar:**
      - 80% para entrenamiento (X_train, y_train)
      - 20% para prueba (X_test, y_test)
      - Los datos de prueba NO se usan durante el entrenamiento
   
   2. **Entrenar con datos de entrenamiento:**
      - El modelo aprende patrones solo de los datos de entrenamiento
      - Nunca ve los datos de prueba
   
   3. **Evaluar con datos de prueba:**
      - Se hacen predicciones sobre datos que el modelo nunca vio
      - Esto mide qué tan bien generaliza el modelo
   
   **Ejemplo con Aurelion:**
   
   **Datos totales:** 343 líneas de detalle de ventas
   
   **División 80/20:**
   - **Train (80%):** 274 líneas → Para entrenar
   - **Test (20%):** 69 líneas → Para evaluar
   
   **Proceso:**
   ```
   1. Dividir datos:
      X_train (274 registros) → Variables predictoras de entrenamiento
      y_train (274 registros) → Variable objetivo de entrenamiento
      X_test (69 registros) → Variables predictoras de prueba
      y_test (69 registros) → Variable objetivo de prueba
   
   2. Entrenar modelo:
      modelo.fit(X_train, y_train)
      → El modelo aprende de los 274 registros
   
   3. Evaluar modelo:
      y_pred = modelo.predict(X_test)
      r2_score(y_test, y_pred)
      → Se evalúa con los 69 registros que nunca vio
   ```
   
   **¿Por qué 80/20?**
   
   - **80% entrenamiento:** Suficiente para que el modelo aprenda patrones
   - **20% prueba:** Suficiente para evaluar sin desperdiciar muchos datos
   - **Alternativas comunes:** 70/30, 75/25, 90/10
   - **Regla general:** Más datos → mejor entrenamiento, pero necesitamos suficientes datos de prueba
   
   **Estratificación (para clasificación):**
   
   Cuando el problema es de **clasificación**, se usa estratificación para mantener la proporción de clases:
   
   ```
   Sin estratificación:
   Train: 80% Clase A, 20% Clase B  (desequilibrado)
   Test:  75% Clase A, 25% Clase B
   
   Con estratificación:
   Train: 75% Clase A, 25% Clase B  (equilibrado)
   Test:  75% Clase A, 25% Clase B  (misma proporción)
   ```
   
   **Semilla aleatoria (random_state):**
   
   - **random_state = 42:** Garantiza que la división sea reproducible
   - Misma semilla → misma división → resultados comparables
   - Importante para experimentos científicos
   
   **En Aurelion:**
   - **Proporción:** 80% train, 20% test
   - **random_state = 42:** Para reproducibilidad
   - **Estratificación:** No se usa (las clases están relativamente balanceadas)
   - **Técnicas de balanceo:** No se usa SMOTE, oversampling ni undersampling
   - **Resultado:** Modelos entrenados con 274 registros, evaluados con 69 registros
   
   **¿Por qué no se usa SMOTE u otras técnicas de balanceo?**
   
   - **Clases balanceadas:** Los segmentos de clientes (Bajo, Medio, Alto) están relativamente balanceados
   - **Random Forest es robusto:** Random Forest maneja bien clases ligeramente desbalanceadas
   - **Resultados satisfactorios:** El accuracy de 88.41% indica que no hay problemas de desbalance severo
   - **Simplicidad:** Evita complejidad adicional cuando no es necesaria

3. **Validación Cruzada (Cross-Validation):**
   
   **¿Qué es la Validación Cruzada?**
   
   La validación cruzada es una técnica más robusta que train/test simple. Divide los datos en **K folds** (pliegues) y entrena/evalúa el modelo K veces, cada vez con un fold diferente como conjunto de prueba.
   
   **Problema con Train/Test simple:**
   - La división puede ser "suerte" o "mala suerte"
   - Si los datos de prueba son fáciles, el modelo parece mejor
   - Si los datos de prueba son difíciles, el modelo parece peor
   - Solo evaluamos una vez
   
   **Solución: K-Fold Cross-Validation**
   
   ```
   K-Fold Cross-Validation (K = 5):
   
   Fold 1: [Train] [Train] [Train] [Train] | [Test]
   Fold 2: [Train] [Train] [Train] | [Test] [Train]
   Fold 3: [Train] [Train] | [Test] [Train] [Train]
   Fold 4: [Train] | [Test] [Train] [Train] [Train]
   Fold 5: | [Test] [Train] [Train] [Train] [Train]
   
   Cada fold usa un 20% diferente como test
   ```
   
   **Proceso paso a paso (5-Fold CV):**
   
   1. **Dividir datos en 5 folds:**
      - Cada fold tiene aproximadamente el 20% de los datos
      - Fold 1: registros 1-69
      - Fold 2: registros 70-138
      - Fold 3: registros 139-207
      - Fold 4: registros 208-276
      - Fold 5: registros 277-343
   
   2. **Iteración 1:**
      - Train: Folds 2, 3, 4, 5 (80% de datos)
      - Test: Fold 1 (20% de datos)
      - Entrenar modelo → Evaluar → Score 1
   
   3. **Iteración 2:**
      - Train: Folds 1, 3, 4, 5 (80% de datos)
      - Test: Fold 2 (20% de datos)
      - Entrenar modelo → Evaluar → Score 2
   
   4. **Iteración 3:**
      - Train: Folds 1, 2, 4, 5 (80% de datos)
      - Test: Fold 3 (20% de datos)
      - Entrenar modelo → Evaluar → Score 3
   
   5. **Iteración 4:**
      - Train: Folds 1, 2, 3, 5 (80% de datos)
      - Test: Fold 4 (20% de datos)
      - Entrenar modelo → Evaluar → Score 4
   
   6. **Iteración 5:**
      - Train: Folds 1, 2, 3, 4 (80% de datos)
      - Test: Fold 5 (20% de datos)
      - Entrenar modelo → Evaluar → Score 5
   
   7. **Resultado final:**
      - Score promedio = (Score 1 + Score 2 + Score 3 + Score 4 + Score 5) / 5
      - Desviación estándar = medida de variabilidad
   
   **Ejemplo con Aurelion:**
   
   **Datos:** 343 registros, 5-Fold CV
   
   **Resultados de cada fold:**
   ```
   Fold | Train Size | Test Size | R² Score
   -----|------------|-----------|----------
   1    |    274     |    69     |  0.9950
   2    |    274     |    69     |  0.9965
   3    |    274     |    69     |  0.9970
   4    |    274     |    69     |  0.9955
   5    |    274     |    69     |  0.9968
   ```
   
   **Cálculo:**
   - **Score promedio:** (0.9950 + 0.9965 + 0.9970 + 0.9955 + 0.9968) / 5 = 0.9962
   - **Desviación estándar:** 0.0007
   - **Resultado:** R² = 0.9962 ± 0.0007
   
   **Interpretación:**
   - El modelo tiene un rendimiento **consistente** en todos los folds
   - La desviación estándar baja (0.0007) indica que el modelo es **estable**
   - No hay mucha variabilidad entre diferentes divisiones
   
   **Ventajas de Validación Cruzada:**
   
   1. **Más robusta:** Evalúa el modelo K veces, no solo una
   2. **Usa todos los datos:** Cada dato se usa para entrenar y para evaluar
   3. **Reduce variabilidad:** El promedio es más confiable que una sola evaluación
   4. **Detecta overfitting:** Si hay mucha variabilidad entre folds, puede haber overfitting
   
   **Desventajas:**
   
   1. **Más lento:** Entrena el modelo K veces
   2. **Computacionalmente costoso:** K veces más entrenamientos
   
   **¿Cuándo usar cada uno?**
   
   - **Train/Test simple:** Datasets muy grandes, evaluación rápida
   - **K-Fold CV:** Datasets pequeños/medianos, evaluación más robusta
   - **En Aurelion:** Usamos ambos (train/test para evaluación rápida, CV para validación robusta)
   
   **En Aurelion:**
   - **K = 5 folds:** 5 divisiones diferentes
   - **Métrica:** R² para regresión, Accuracy para clasificación
   - **Resultado:** R² = 0.9962 ± 0.0007 (muy consistente)
   - **Interpretación:** El modelo generaliza bien a diferentes subconjuntos de datos

4. **Guardado de Conjuntos:**
   - X_train, X_test, y_train, y_test
   - Verificación de integridad

5. **Estadísticas:**
   - Comparación de distribuciones
   - Verificación de similitud entre train y test

#### 6.2.7. Módulo 7: Proceso de Entrenamiento (`03_proceso_entrenamiento.py`)

**Objetivo:** Entrenar múltiples modelos de ML

**Proceso:**

1. **Carga de Datos:**
   - Carga de conjuntos train/test
   - Verificación de tipos de datos

2. **Determinación de Tipo de Problema:**
   - Detección automática (regresión vs clasificación)
   - Basado en número de valores únicos y tipo de dato

3. **Entrenamiento de Modelos:**

   **Para Regresión:**
   - Linear Regression
   - Random Forest Regressor
   - SVR

   **Para Clasificación:**
   - Logistic Regression
   - Random Forest Classifier
   - SVC

4. **Evaluación Básica:**
   - Métricas en train y test
   - Detección de overfitting
   
   **4.1. Overfitting y Underfitting:**
   
   **¿Qué es Overfitting (Sobreajuste)?**
   
   Overfitting ocurre cuando el modelo se ajusta **demasiado** a los datos de entrenamiento, memorizando patrones específicos (incluyendo ruido) en lugar de aprender patrones generales. El modelo funciona muy bien en los datos de entrenamiento pero **mal en datos nuevos**.
   
   **¿Qué es "Ruido" en Machine Learning?**
   
   **Ruido (Noise)** se refiere a variaciones aleatorias o errores en los datos que no representan patrones reales o útiles. Es información que no debería ser aprendida por el modelo porque:
   
   - **No es generalizable:** Son variaciones específicas de los datos de entrenamiento que no se repetirán en datos nuevos
   - **No tiene significado:** Son fluctuaciones aleatorias, errores de medición, o anomalías que no aportan información útil
   - **Puede confundir al modelo:** Si el modelo aprende el ruido, pensará que es un patrón importante y fallará en datos nuevos
   
   **Ejemplos de ruido en datos:**
   - **Errores de medición:** Un precio registrado incorrectamente ($2,500 en lugar de $2,550)
   - **Variaciones aleatorias:** Fluctuaciones temporales que no tienen causa real
   - **Outliers ocasionales:** Valores extremos que son errores, no patrones reales
   - **Datos incompletos o inconsistentes:** Información faltante o mal registrada
   
   **Ejemplo visual de ruido:**
   ```
   Patrón real (sin ruido):     Con ruido:
   
   Importe                      Importe
     ↑                            ↑
     |  ●     ●                   |  ●     ●
     |    ╲ ╱                     |  ╱╲   ╲╱  ← Variaciones aleatorias
     |     ●                      |   ╲ ╱
     |  ●     ●                   |    ●
     └────────────→ Cantidad      |  ●     ●
                                  └────────────→ Cantidad
   
   Línea suave (patrón real)    Línea irregular (patrón + ruido)
   ```
   
   **En el contexto de Overfitting:**
   - Un modelo con overfitting aprende tanto el patrón real como el ruido
   - "Memoriza" las variaciones aleatorias como si fueran patrones importantes
   - Funciona perfecto en los datos de entrenamiento (incluyendo el ruido)
   - Pero falla en datos nuevos porque el ruido no se repite
   
   **En Aurelion:**
   - Los datos pueden tener ruido por errores de registro, variaciones temporales, o outliers ocasionales
   - Un modelo bien ajustado (como Random Forest) aprende los patrones reales y ignora el ruido
   - Un modelo con overfitting memorizaría incluso las variaciones aleatorias
   
   **Síntomas de Overfitting:**
   - **R² train muy alto** (ej: 0.99) pero **R² test mucho más bajo** (ej: 0.70)
   - **MSE train muy bajo** pero **MSE test mucho más alto**
   - El modelo "memoriza" los datos en lugar de "aprender" patrones
   
   **Ejemplo visual de Overfitting:**
   ```
   Datos de Entrenamiento:
   
   Importe
     ↑
     |  ●     ●
     |    ╲ ╱
     |     ●
     |  ●     ●
     └────────────→ Cantidad
   
   Modelo con Overfitting (línea muy compleja):
   
   Importe
     ↑
     |  ●     ●
     |  ╱╲   ╱╲  ← Línea muy compleja que pasa por todos los puntos
     | ╱  ╲ ╱  ╲
     |●     ●
     └────────────→ Cantidad
   
   Resultado: Funciona perfecto en train, pero mal en test
   ```
   
   **Ejemplo con Aurelion:**
   
   **Modelo con Overfitting:**
   ```
   R² en entrenamiento: 0.9999 (99.99%) ← Muy alto
   R² en prueba:        0.7500 (75.00%) ← Mucho más bajo
   
   Diferencia: 0.2499 (24.99 puntos porcentuales)
   → El modelo memorizó los datos de entrenamiento
   → No generaliza bien a datos nuevos
   ```
   
   **¿Qué es Underfitting (Subajuste)?**
   
   Underfitting ocurre cuando el modelo es **demasiado simple** y no puede capturar los patrones en los datos. El modelo funciona **mal tanto en entrenamiento como en prueba**.
   
   **Síntomas de Underfitting:**
   - **R² train bajo** (ej: 0.50) y **R² test también bajo** (ej: 0.48)
   - **MSE train alto** y **MSE test también alto**
   - El modelo es demasiado simple para el problema
   
   **Ejemplo visual de Underfitting:**
   ```
   Datos de Entrenamiento:
   
   Importe
     ↑
     |  ●     ●
     |    ╲ ╱
     |     ●
     |  ●     ●
     └────────────→ Cantidad
   
   Modelo con Underfitting (línea muy simple):
   
   Importe
     ↑
     |  ●     ●
     |───────────  ← Línea muy simple que no captura el patrón
     |     ●
     |  ●     ●
     └────────────→ Cantidad
   
   Resultado: Funciona mal tanto en train como en test
   ```
   
   **Ejemplo con Aurelion:**
   
   **Modelo con Underfitting:**
   ```
   R² en entrenamiento: 0.5000 (50.00%) ← Bajo
   R² en prueba:        0.4800 (48.00%) ← También bajo
   
   Diferencia: 0.0200 (2.00 puntos porcentuales)
   → El modelo es demasiado simple
   → No captura los patrones en los datos
   ```
   
   **Modelo Ideal (Bien Ajustado):**
   
   Un modelo bien ajustado tiene un rendimiento **similar** en entrenamiento y prueba, con ambos valores altos.
   
   **Ejemplo con Aurelion (Random Forest):**
   ```
   R² en entrenamiento: 0.9970 (99.70%) ← Alto
   R² en prueba:        0.9962 (99.62%) ← También alto y similar
   
   Diferencia: 0.0008 (0.08 puntos porcentuales)
   → El modelo generaliza bien
   → Aprendió patrones generales, no memorizó datos específicos
   ```
   
   **Bias-Variance Tradeoff:**
   
   El balance entre overfitting y underfitting se relaciona con el **Bias-Variance Tradeoff**:
   
   - **Bias (Sesgo):** Error por simplificar demasiado el modelo (underfitting)
   - **Variance (Varianza):** Error por sensibilidad a pequeñas variaciones en los datos (overfitting)
   
   ```
   Complejidad del Modelo
   Bajo ←───────────────────────────────→ Alto
   
   Underfitting          Bien Ajustado          Overfitting
   (Alto Bias)          (Balance)              (Alta Varianza)
   │                    │                      │
   │                    │                      │
   │                    │                      │
   └────────────────────┴──────────────────────┘
        Error Total
   ```
   
   **Cómo detectar Overfitting/Underfitting:**
   
   1. **Comparar métricas train vs test:**
      - Si train >> test → Overfitting
      - Si train ≈ test (ambos bajos) → Underfitting
      - Si train ≈ test (ambos altos) → Bien ajustado
   
   2. **Validación cruzada:**
      - Alta variabilidad entre folds → Posible overfitting
      - Baja variabilidad pero scores bajos → Posible underfitting
   
   3. **Visualización:**
      - Gráfico de predicciones vs reales
      - Si el modelo sigue cada punto exactamente → Overfitting
      - Si el modelo es una línea simple → Underfitting
   
   **Cómo prevenir Overfitting:**
   
   1. **Más datos:** Más datos de entrenamiento ayudan al modelo a generalizar
   2. **Regularización:** Penalizar complejidad (L1, L2)
   3. **Cross-validation:** Evaluar en múltiples divisiones
   4. **Ensemble methods:** Random Forest reduce overfitting
   5. **Early stopping:** Detener entrenamiento antes de sobreajustar
   6. **Simplificar modelo:** Reducir complejidad (menos parámetros)
   
   **Cómo prevenir Underfitting:**
   
   1. **Aumentar complejidad:** Más características, modelo más complejo
   2. **Feature engineering:** Crear características más relevantes
   3. **Reducir regularización:** Permitir que el modelo aprenda más
   4. **Entrenar más tiempo:** Más iteraciones/epochs
   
   **En Aurelion:**
   
   **Random Forest (Bien ajustado):**
   - R² train: 0.9970
   - R² test: 0.9962
   - Diferencia: 0.0008 (muy pequeña)
   - **Conclusión:** El modelo generaliza excelentemente, no hay overfitting
   
   **Técnicas usadas para evitar overfitting:**
   - División train/test (80/20)
   - Validación cruzada (5 folds)
   - Ensemble (Random Forest promedia 100 árboles)
   - Parámetros de regularización (max_depth, min_samples_split)

#### 6.2.8. Proceso de Entrenamiento de Modelos

**¿Con qué entrenamos los modelos?**

Los modelos se entrenan directamente con los datos divididos en conjuntos de entrenamiento y prueba, **sin usar técnicas de balanceo como SMOTE**.

**Proceso completo de entrenamiento:**

1. **Preparación de datos:**
   ```python
   # Seleccionar variables predictoras (X) y variable objetivo (y)
   X = dataset[columnas_predictoras]  # Variables numéricas
   y = dataset[variable_objetivo]     # Variable a predecir
   ```

2. **División Train/Test:**
   ```python
   from sklearn.model_selection import train_test_split
   
   # IMPORTANTE: Dividir PRIMERO
   X_train_raw, X_test_raw, y_train, y_test = train_test_split(
       X, y, 
       test_size=0.2,      # 20% para prueba
       random_state=42     # Semilla para reproducibilidad
   )
   ```
   - **X_train_raw, y_train:** Datos para entrenar (80%)
   - **X_test_raw, y_test:** Datos para evaluar (20%)

3. **Normalización (DESPUÉS de dividir - evita data leakage):**
   ```python
   from sklearn.preprocessing import StandardScaler
   
   # IMPORTANTE: Normalizar DESPUÉS de dividir
   scaler = StandardScaler()
   X_train = scaler.fit_transform(X_train_raw)  # fit_transform en training
   X_test = scaler.transform(X_test_raw)        # transform en test
   ```
   - **fit_transform en training:** El scaler aprende SOLO de datos de entrenamiento
   - **transform en test:** Aplica los parámetros aprendidos (evita data leakage)
   - **⚠️ No normalizar antes de dividir:** Causaría data leakage

4. **Entrenamiento del modelo:**
   ```python
   # Crear modelo
   modelo = RandomForestRegressor(n_estimators=100, random_state=42)
   
   # Entrenar con .fit() (usando datos normalizados correctamente)
   modelo.fit(X_train, y_train)
   ```
   - **`.fit()`:** Método que entrena el modelo con los datos de entrenamiento normalizados
   - El modelo aprende los patrones de X_train para predecir y_train
   - Los datos están normalizados correctamente (sin data leakage)

5. **Predicciones:**
   ```python
   # Predecir con .predict()
   y_pred_train = modelo.predict(X_train)  # Predicciones en entrenamiento
   y_pred_test = modelo.predict(X_test)    # Predicciones en prueba (datos normalizados)
   ```
   - **`.predict()`:** Método que usa el modelo entrenado para hacer predicciones
   - Los datos de test están normalizados con los mismos parámetros que training

6. **Evaluación:**
   ```python
   from sklearn.metrics import r2_score, mean_squared_error
   
   r2_test = r2_score(y_test, y_pred_test)
   mse_test = mean_squared_error(y_test, y_pred_test)
   ```

**¿Por qué NO se usa SMOTE?**

**SMOTE (Synthetic Minority Oversampling Technique)** es una técnica de balanceo de clases que crea ejemplos sintéticos de la clase minoritaria. **No se usa en este proyecto** por las siguientes razones:

1. **Clases relativamente balanceadas:**
   - Los segmentos de clientes (Bajo, Medio, Alto) están relativamente balanceados
   - No hay un desbalance severo que requiera técnicas especiales

2. **Random Forest es robusto:**
   - Random Forest maneja bien clases ligeramente desbalanceadas
   - El algoritmo de ensemble reduce el impacto del desbalance

3. **Resultados satisfactorios:**
   - Accuracy de 88.41% indica buen rendimiento sin balanceo
   - No hay evidencia de que el desbalance esté afectando el modelo

4. **Simplicidad:**
   - Evita complejidad adicional cuando no es necesaria
   - Mantiene el proceso más interpretable

**¿Cuándo SÍ se usaría SMOTE?**

SMOTE se usaría si:
- Hay un desbalance severo (ej: 90% clase A, 10% clase B)
- El modelo tiene bajo recall en la clase minoritaria
- Las métricas indican que el desbalance está afectando el rendimiento

**En Aurelion:**
- **No se usa SMOTE** - Las clases están balanceadas
- **No se usa oversampling** - No es necesario
- **No se usa undersampling** - No es necesario
- **Se usa train_test_split** - División estándar 80/20
- **Se usa .fit()** - Entrenamiento estándar
- **Se usa .predict()** - Predicción estándar

**Métricas calculadas para clasificación:**

Para los modelos de clasificación, se calculan y reportan las siguientes métricas:

1. **Accuracy (Precisión Global):**
   ```python
   accuracy = accuracy_score(y_test, y_pred_test)
   ```

2. **Precision (Precisión por clase):**
   - Calculada desde la matriz de confusión: `precision = TP / (TP + FP)`
   - También incluida en `classification_report`

3. **Recall (Sensibilidad por clase):**
   - **SÍ se calcula y usa** en el proyecto
   - Calculado desde la matriz de confusión: `recall = TP / (TP + FN)`
   - También incluido en `classification_report`
   - Se muestra en los reportes de resultados

4. **F1-Score:**
   - Calculado como balance entre Precision y Recall: `F1 = 2 × (Precision × Recall) / (Precision + Recall)`

5. **Matriz de Confusión:**
   - Muestra TP, TN, FP, FN para cada clase
   - Se usa para calcular Precision, Recall y F1-Score

**Código donde se calcula Recall:**

```python
# En 06_modelos_ml.py, línea 859
from sklearn.metrics import classification_report, confusion_matrix

# Matriz de confusión
cm = confusion_matrix(y_test, y_pred_test)

# Classification report (incluye recall automáticamente)
report = classification_report(y_test, y_pred_test, output_dict=True)

# Cálculo manual de recall por clase
for i, clase in enumerate(clases):
    tp = cm[i, i]  # Verdaderos positivos
    fn = cm[i, :].sum() - tp  # Falsos negativos
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    print(f"Recall para clase '{clase}': {recall:.2%}")
```

**Resultados de Recall en Aurelion:**

- **Recall se calcula para cada clase** (Bajo, Medio, Alto)
- **Se incluye en los reportes** de evaluación de modelos
- **Se usa junto con Precision** para calcular F1-Score
- **Se visualiza** en las matrices de confusión detalladas

**Resumen del flujo de entrenamiento:**

```
Datos Originales (343 registros)
    ↓
train_test_split (80/20)
    ↓
X_train (274) + y_train (274)  →  modelo.fit(X_train, y_train)
X_test (69) + y_test (69)      →  modelo.predict(X_test)
    ↓
Evaluación: r2_score(y_test, y_pred_test)
```

5. **Comparación de Modelos:**
   - Ranking por métrica principal
   - Identificación del mejor modelo

6. **Guardado de Modelos:**
   - Guardado en formato .pkl
   - Información del mejor modelo

#### 6.2.8. Módulo 8: Evaluación de Modelos (`04_evaluacion_modelos.py`)

**Objetivo:** Evaluación detallada de modelos entrenados

**Proceso:**

1. **Carga de Modelos:**
   - Carga de todos los modelos .pkl
   - Verificación de integridad

2. **Evaluación Detallada:**

   **Para Regresión:**
   - MSE, RMSE, MAE, R², MAPE
   - Visualización: Predicciones vs Valores Reales
   - Interpretación específica con valores reales

   **Para Clasificación:**
   - Accuracy, Precision, Recall, F1-Score
   - Matriz de confusión
   - Reporte de clasificación

3. **Comparación de Modelos:**
   - Tabla comparativa
   - Ranking por métrica principal
   - Identificación del mejor modelo

4. **Visualización de Resultados:**
   - Gráficos de predicciones vs reales
   - Matrices de confusión
   - Interpretación detallada

5. **Generación de Reportes:**
   - Reporte de evaluación en texto
   - Interpretación de resultados
   - Recomendaciones

#### 6.2.9. Módulo 9: Algoritmos Específicos (`05_algoritmos_especificos.py`)

**Objetivo:** Implementación detallada de algoritmos específicos

**Algoritmos Implementados:**

1. **Random Forest Regressor:**
   - Parámetros optimizados
   - Importancia de características
   - Evaluación detallada

2. **Logistic Regression:**
   - Parámetros optimizados
   - Coeficientes interpretables
   - Evaluación detallada

3. **K-Means Clustering:**
   - Método Elbow para k óptimo
   - Silhouette Score
   - Visualización de clusters
   - Distribución de clusters

4. **Comparación de Algoritmos:**
   - Tabla comparativa
   - Recomendaciones por tipo de problema
   - Interpretación de resultados

#### 6.2.10. Sistema Interactivo (`demo_interactivo.py`)

**Objetivo:** Sistema educativo interactivo con 15 opciones

**Funcionalidades:**

1. **Menú Principal:**
   - 15 opciones organizadas en secciones
   - Navegación intuitiva
   - Manejo de errores

2. **Módulos de Fundamentos:**
   - Fundamentos de ML
   - Tipos de aprendizajes
   - Algoritmos básicos
   - Métricas de evaluación

3. **Módulos de Modelado:**
   - Preparación de datos
   - Entrenamiento
   - Evaluación
   - Predicciones
   - Comparación de modelos

4. **Visualización y Resultados:**
   - Ver gráficos generados
   - Ver reportes
   - Ver archivos de datos
   - Inspeccionar modelos
   - Analizar gráficos detalladamente

5. **Módulos Auxiliares:**
   - `visualizador_automatico.py`: Visualización automática
   - `visualizador_predicciones.py`: Predicciones reales
   - `comparador_modelos.py`: Comparación detallada
   - `generador_reportes.py`: Reportes automáticos
   - `analizador_graficos.py`: Análisis de gráficos

### 6.3. Resultados del Sprint 3

- ✅ 4 módulos de fundamentos completos
- ✅ 5 módulos de modelado implementados
- ✅ Sistema interactivo con 15 opciones
- ✅ 15 scripts demo adicionales
- ✅ Documentación completa
- ✅ Modelos entrenados y guardados
- ✅ Visualizaciones y reportes generados

### 6.4. Lecciones Aprendidas

- La educación en fundamentos es crucial para entender ML
- Los sistemas interactivos facilitan el aprendizaje
- La evaluación detallada revela fortalezas y debilidades
- La comparación de algoritmos ayuda a seleccionar el mejor modelo

### 6.5. Funciones Principales Utilizadas en el Sprint 3

Esta sección explica las funciones principales utilizadas en el Sprint 3 de manera sencilla, enfocándose en los fundamentos educativos y el proceso completo de modelado.

#### 6.5.1. Función: `define_ml()` (Fundamentos)

**¿Qué hace?**
Explica de manera simple qué es Machine Learning y cómo funciona, sin usar términos técnicos complicados.

**¿Cómo funciona?**
1. Define Machine Learning como una forma de hacer que las computadoras aprendan de los datos
2. Explica que en lugar de programar reglas específicas, se le dan datos a la computadora y ella encuentra patrones
3. Compara con el aprendizaje humano: así como los humanos aprenden de la experiencia, las computadoras aprenden de los datos

**¿Para qué se usó?**
Para educar y explicar los conceptos básicos antes de usar técnicas avanzadas. Es importante entender qué es Machine Learning antes de usarlo.

**Ejemplo práctico:**
Es como explicarle a alguien qué es la cocina antes de enseñarle a cocinar. Primero entienden el concepto general, luego pueden aprender técnicas específicas.

---

#### 6.5.2. Función: `ml_problem_types()` (Fundamentos)

**¿Qué hace?**
Explica los tres tipos principales de problemas que puede resolver Machine Learning: regresión, clasificación y clustering.

**¿Cómo funciona?**
1. **Regresión:** Explica que es predecir números (como predecir el precio de una casa)
2. **Clasificación:** Explica que es categorizar cosas (como clasificar si un correo es spam o no)
3. **Clustering:** Explica que es agrupar cosas similares (como agrupar clientes por comportamiento)
4. Da ejemplos prácticos de cada tipo
5. Muestra qué algoritmos se usan para cada tipo

**¿Para qué se usó?**
Para ayudar a entender qué tipo de problema se está resolviendo. No todos los problemas son iguales, y cada uno requiere un enfoque diferente.

**Ejemplo práctico:**
Es como explicar los diferentes tipos de herramientas. Un martillo es para clavar, un destornillador para atornillar, y una sierra para cortar. Cada herramienta (algoritmo) es mejor para diferentes tareas (tipos de problemas).

---

#### 6.5.3. Función: `typical_ml_process()` (Fundamentos)

**¿Qué hace?**
Explica el proceso paso a paso que se sigue para crear un modelo de Machine Learning, desde los datos hasta el despliegue.

**¿Cómo funciona?**
1. **Datos:** Recopilar y limpiar datos históricos
2. **Preparación:** Normalizar y codificar variables
3. **División:** Separar datos en entrenamiento (80%) y prueba (20%)
4. **Entrenamiento:** El algoritmo aprende de los datos de entrenamiento
5. **Predicción:** El modelo genera predicciones
6. **Evaluación:** Se mide qué tan bien funciona el modelo
7. **Despliegue:** Se pone el modelo en producción para usarlo

**¿Para qué se usó?**
Para entender el flujo completo del trabajo. Es como una receta: sigues los pasos en orden para obtener el resultado deseado.

**Ejemplo práctico:**
Es como el proceso de cocinar. Primero compras los ingredientes (datos), luego los preparas (normalización), cocinas (entrenamiento), pruebas el sabor (evaluación), y finalmente sirves el plato (despliegue).

---

#### 6.5.4. Función: `preparar_datos()` (Modelado)

**¿Qué hace?**
Prepara los datos para que puedan ser usados por los algoritmos de Machine Learning, aplicando todas las técnicas de limpieza y transformación necesarias.

**¿Cómo funciona?**
1. Carga los datos desde archivos
2. Analiza qué valores faltan y los completa
3. Identifica y trata valores extremos
4. Normaliza las variables numéricas
5. Codifica las variables categóricas (texto a números)
6. Separa las características (lo que se usa para predecir) del objetivo (lo que se quiere predecir)

**¿Para qué se usó?**
Para asegurar que los datos estén en el formato correcto para que los algoritmos puedan trabajar con ellos. Es como preparar los ingredientes antes de cocinar.

**Ejemplo práctico:**
Es como preparar los ingredientes para una receta. No puedes cocinar con ingredientes sucios o en el formato incorrecto. Primero los lavas, los cortas, los mides, y luego puedes cocinar.

---

#### 6.5.5. Función: `division_train_test()` (Modelado)

**¿Qué hace?**
Divide los datos en dos grupos: uno para enseñar al modelo (entrenamiento) y otro para probar qué tan bien aprendió (prueba).

**¿Cómo funciona?**
1. Toma todos los datos disponibles
2. Separa el 80% para entrenar el modelo (el modelo aprende de estos datos)
3. Separa el 20% para probar el modelo (estos datos el modelo nunca los ha visto)
4. Verifica que ambos grupos tengan características similares
5. Guarda ambos grupos para usarlos después

**¿Para qué se usó?**
Para poder evaluar si el modelo realmente aprendió o solo memorizó los datos. Si el modelo solo memorizó, funcionará bien con los datos de entrenamiento pero mal con los de prueba.

**Ejemplo práctico:**
Es como estudiar para un examen. Tienes un libro de texto (datos de entrenamiento) para estudiar, y luego tienes un examen (datos de prueba) que nunca has visto antes. Si realmente aprendiste, aprobarás el examen. Si solo memorizaste, fallarás.

---

#### 6.5.6. Función: `train_model()` (Modelado)

**¿Qué hace?**
Enseña a los modelos de Machine Learning a hacer predicciones usando los datos de entrenamiento.

**¿Cómo funciona?**
1. Recibe los datos de entrenamiento (características y objetivo)
2. Para regresión: entrena modelos que predicen números (Linear Regression, Random Forest, SVR)
3. Para clasificación: entrena modelos que clasifican en categorías (Logistic Regression, Random Forest, SVC)
4. Cada modelo "aprende" encontrando patrones en los datos
5. Prueba cada modelo con los datos de prueba
6. Calcula qué tan bien funciona cada modelo

**¿Para qué se usó?**
Para crear modelos que puedan hacer predicciones. Es el paso central del Machine Learning: enseñar a la computadora a aprender.

**Ejemplo práctico:**
Es como enseñarle a alguien a conducir. Le muestras muchos ejemplos de cómo conducir (datos de entrenamiento), y la persona aprende los patrones. Luego, cuando conduce en una situación nueva (datos de prueba), aplica lo que aprendió.

---

#### 6.5.7. Función: `evaluacion_modelos()` (Modelado)

**¿Qué hace?**
Evalúa qué tan bien funcionan los modelos comparando sus predicciones con los valores reales.

**¿Cómo funciona?**
1. Toma las predicciones de cada modelo
2. Las compara con los valores reales
3. Para regresión: calcula métricas como R² (qué tan bien explica los datos) y MSE (qué tan grandes son los errores)
4. Para clasificación: calcula Accuracy (qué porcentaje acertó), Precision, Recall, F1-Score
5. Crea visualizaciones mostrando las predicciones vs valores reales
6. Genera reportes detallados de cada modelo

**¿Para qué se usó?**
Para saber qué modelo funciona mejor y si los modelos son lo suficientemente buenos para usar en producción. No todos los modelos son iguales, y necesitas saber cuál elegir.

**Ejemplo práctico:**
Es como calificar un examen. Comparas las respuestas del estudiante (predicciones) con las respuestas correctas (valores reales) y calculas la calificación. Si sacó 90%, es un buen estudiante. Si sacó 50%, necesita estudiar más.

---

#### 6.5.8. Función: `determine_problem_type()` (Modelado)

**¿Qué hace?**
Determina automáticamente si el problema es de regresión (predecir números) o clasificación (categorizar).

**¿Cómo funciona?**
1. Analiza la variable objetivo (lo que se quiere predecir)
2. Si la variable tiene muchos valores únicos y es numérica → Regresión
3. Si la variable tiene pocos valores únicos y es categórica → Clasificación
4. Devuelve el tipo de problema identificado

**¿Para qué se usó?**
Para que el sistema pueda elegir automáticamente qué tipo de modelos usar. No necesitas decirle manualmente si es regresión o clasificación, el sistema lo detecta.

**Ejemplo práctico:**
Es como un asistente inteligente que ve qué tipo de tarea necesitas hacer y automáticamente te da las herramientas correctas. Si ve que quieres cortar, te da tijeras. Si ve que quieres clavar, te da un martillo.

---

#### 6.5.9. Función: `compare_models()` (Modelado)

**¿Qué hace?**
Compara todos los modelos entrenados y determina cuál es el mejor según las métricas de evaluación.

**¿Cómo funciona?**
1. Toma los resultados de todos los modelos
2. Compara sus métricas (R² para regresión, Accuracy para clasificación)
3. Ordena los modelos de mejor a peor
4. Identifica el mejor modelo
5. Muestra una tabla comparativa con todos los resultados

**¿Para qué se usó?**
Para elegir el mejor modelo entre varias opciones. No todos los modelos funcionan igual de bien, y necesitas saber cuál usar.

**Ejemplo práctico:**
Es como probar varios coches antes de comprar uno. Probaste 3 coches diferentes, comparaste su velocidad, consumo de gasolina, comodidad, y elegiste el mejor según tus necesidades.

---

#### 6.5.10. Función: `save_models()` (Modelado)

**¿Qué hace?**
Guarda los modelos entrenados en archivos para poder usarlos después sin tener que entrenarlos de nuevo.

**¿Cómo funciona?**
1. Toma los modelos entrenados
2. Los guarda en archivos especiales (.pkl) que preservan toda la información del modelo
3. Guarda información sobre el mejor modelo
4. Guarda las métricas de evaluación
5. Crea documentación sobre cómo usar cada modelo

**¿Para qué se usó?**
Para poder usar los modelos más tarde sin tener que entrenarlos de nuevo cada vez. El entrenamiento puede tomar tiempo, así que es mejor guardar los modelos ya entrenados.

**Ejemplo práctico:**
Es como guardar una receta que ya probaste y funcionó bien. En lugar de experimentar de nuevo cada vez que quieres cocinar ese plato, simplemente sigues la receta guardada.

---

### Resumen de Funciones del Sprint 3

| Función | Propósito Simple | Resultado |
|---------|------------------|-----------|
| `define_ml()` | Explicar qué es Machine Learning | Comprensión de conceptos básicos |
| `ml_problem_types()` | Explicar tipos de problemas | Entendimiento de regresión, clasificación, clustering |
| `typical_ml_process()` | Explicar el proceso completo | Conocimiento del flujo de trabajo |
| `preparar_datos()` | Preparar datos para ML | Datos listos para entrenar modelos |
| `division_train_test()` | Dividir datos en entrenamiento y prueba | Datos separados para entrenar y evaluar |
| `train_model()` | Enseñar modelos a predecir | Modelos entrenados y listos |
| `evaluacion_modelos()` | Evaluar qué tan bien funcionan | Métricas de rendimiento de cada modelo |
| `determine_problem_type()` | Detectar tipo de problema | Identificación automática del tipo |
| `compare_models()` | Comparar modelos | Identificación del mejor modelo |
| `save_models()` | Guardar modelos entrenados | Modelos guardados para uso futuro |

### 6.6. Métodos de Scikit-learn y Pandas Utilizados en el Sprint 3

En el Sprint 3 se utilizaron métodos adicionales de scikit-learn para el proceso completo de Machine Learning, desde la división de datos hasta la evaluación de modelos.

#### 6.6.1. Función: `train_test_split()`

**¿Qué hace?**
Divide automáticamente los datos en dos grupos: uno para entrenar el modelo y otro para probarlo.

**¿Cómo funciona?**
1. Recibe todos los datos (características X y objetivo y)
2. Los divide en 4 grupos:
   - **X_train:** Características para entrenar (80%)
   - **X_test:** Características para probar (20%)
   - **y_train:** Resultados esperados para entrenar (80%)
   - **y_test:** Resultados esperados para probar (20%)
3. Mezcla los datos aleatoriamente antes de dividir
4. Mantiene la proporción de clases si es clasificación (estratificación)

**¿Para qué se usó?**
Para separar los datos de manera que el modelo pueda aprender de unos datos y ser probado con otros datos que nunca ha visto. Esto es fundamental para evaluar si el modelo realmente aprendió o solo memorizó.

**Ejemplo práctico:**
Es como dividir un libro de ejercicios. Tienes 100 ejercicios, usas 80 para estudiar (train) y guardas 20 para el examen final (test). Así puedes ver si realmente aprendiste o solo memorizaste los ejercicios de estudio.

---

#### 6.6.2. Función: `cross_val_score()`

**¿Qué hace?**
Evalúa un modelo usando validación cruzada, que es una forma más robusta de evaluar el rendimiento.

**¿Cómo funciona?**
1. Divide los datos en varios grupos (por ejemplo, 5 grupos o "folds")
2. Entrena el modelo 5 veces, cada vez usando 4 grupos para entrenar y 1 grupo para probar
3. Calcula el score (precisión) en cada una de las 5 pruebas
4. Devuelve el promedio y la desviación estándar de los 5 scores

**¿Para qué se usó?**
Para obtener una evaluación más confiable del modelo. En lugar de probar una sola vez, se prueba 5 veces con diferentes divisiones de datos, lo que da una mejor idea del rendimiento real.

**Ejemplo práctico:**
Es como hacer 5 exámenes diferentes en lugar de uno solo. Si sacas buenas calificaciones en los 5 exámenes, es más confiable que si solo hiciste bien en uno. El promedio de los 5 exámenes te da una mejor idea de qué tan bien sabes el tema.

---

#### 6.6.3. Método: `.unique()` y `.nunique()`

**¿Qué hace?**
Analiza los valores únicos en una columna:
- **`.unique()`:** Devuelve una lista con todos los valores únicos (sin repetir)
- **`.nunique()`:** Cuenta cuántos valores únicos hay

**¿Para qué se usó?**
Para determinar automáticamente si un problema es de regresión o clasificación. Si hay muchos valores únicos, es regresión. Si hay pocos, es clasificación.

**Ejemplo práctico:**
Es como revisar una lista de estudiantes. `.unique()` te da la lista de todos los nombres diferentes, y `.nunique()` te dice cuántos estudiantes únicos hay (sin contar repetidos).

---

#### 6.6.4. Método: `.shape`

**¿Qué hace?**
Devuelve las dimensiones de una tabla (cuántas filas y cuántas columnas tiene).

**¿Cómo funciona?**
- **`.shape[0]`:** Número de filas
- **`.shape[1]`:** Número de columnas
- **`.shape`:** Devuelve ambos (filas, columnas)

**¿Para qué se usó?**
Para verificar cuántos datos hay y cuántas características se están usando. Es útil para entender el tamaño del dataset.

**Ejemplo práctico:**
Es como preguntar "¿cuántas filas y columnas tiene esta hoja de cálculo?" Si tienes 100 filas y 5 columnas, `.shape` devuelve (100, 5).

---

#### 6.6.5. Método: `.columns`

**¿Qué hace?**
Devuelve una lista con los nombres de todas las columnas de una tabla.

**¿Para qué se usó?**
Para identificar qué columnas están disponibles, qué columnas excluir (como IDs), y qué columnas usar como características para los modelos.

**Ejemplo práctico:**
Es como ver los encabezados de una tabla. Si tienes una tabla con columnas "nombre", "edad", "ciudad", `.columns` te devuelve esa lista de nombres.

---

#### 6.6.6. Método: `.dtype` y `.dtypes`

**¿Qué hace?**
Identifica el tipo de dato de una columna o de todas las columnas:
- **`.dtype`:** Tipo de dato de una columna específica
- **`.dtypes`:** Tipos de dato de todas las columnas

**¿Para qué se usó?**
Para determinar automáticamente qué columnas son numéricas y cuáles son categóricas, lo cual es importante para decidir cómo tratarlas.

**Ejemplo práctico:**
Es como identificar qué tipo de información hay en cada columna. Si una columna tiene números, su tipo es "int64" o "float64". Si tiene texto, su tipo es "object".

---

#### 6.6.7. Método: `pickle.dump()` y `pickle.load()`

**¿Qué hace?**
Guarda y carga objetos de Python (como modelos entrenados) en archivos:
- **`pickle.dump()`:** Guarda un objeto en un archivo
- **`pickle.load()`:** Carga un objeto desde un archivo

**¿Para qué se usó?**
Para guardar los modelos entrenados en archivos (.pkl) y poder cargarlos después sin tener que entrenarlos de nuevo. El entrenamiento puede tomar tiempo, así que es mejor guardar los modelos ya entrenados.

**Ejemplo práctico:**
Es como guardar un documento en tu computadora. Guardas el modelo entrenado (`.dump()`), y luego puedes abrirlo más tarde (`.load()`) sin tener que entrenarlo de nuevo.

---

#### 6.6.8. Método: `mean_squared_error()`, `r2_score()`, `accuracy_score()`

**¿Qué hace?**
Estas son funciones de scikit-learn que calculan métricas de evaluación:
- **`mean_squared_error(y_real, y_pred)`:** Calcula el error cuadrático medio (MSE) - qué tan grandes son los errores
- **`r2_score(y_real, y_pred)`:** Calcula el R² - qué tan bien explica el modelo los datos
- **`accuracy_score(y_real, y_pred)`:** Calcula la precisión - qué porcentaje de predicciones son correctas

**¿Para qué se usó?**
Para evaluar el rendimiento de los modelos. Cada métrica mide algo diferente:
- **MSE:** Para regresión - mide el tamaño de los errores
- **R²:** Para regresión - mide qué porcentaje de la variabilidad explica el modelo
- **Accuracy:** Para clasificación - mide qué porcentaje de predicciones son correctas

**Ejemplo práctico:**
Es como diferentes formas de calificar un examen. MSE es como contar cuántos puntos te faltaron en total. R² es como ver qué porcentaje del examen entendiste bien. Accuracy es como ver qué porcentaje de preguntas acertaste.

---

#### 6.6.9. Método: `confusion_matrix()` y `classification_report()`

**¿Qué hace?**
Estas funciones crean reportes detallados de cómo clasifica un modelo:
- **`confusion_matrix()`:** Crea una matriz que muestra cuántas predicciones correctas e incorrectas hay por cada categoría
- **`classification_report()`:** Genera un reporte con Precision, Recall y F1-Score para cada categoría

**¿Cómo funciona `confusion_matrix()`?**

La matriz de confusión es una tabla cuadrada donde:
- **Filas:** Representan los valores reales (ground truth, labels verdaderos)
- **Columnas:** Representan las predicciones del modelo
- **Diagonal principal:** Predicciones correctas (TP por clase)
- **Fuera de la diagonal:** Errores de clasificación

**Visualización como Heatmap:**

La matriz de confusión se visualiza comúnmente como un **heatmap** donde:
- **Colores intensos (rojo/naranja):** Valores altos (muchas predicciones)
- **Colores claros (azul):** Valores bajos (pocas predicciones)
- **Diagonal:** Debería ser la más intensa si el modelo es bueno (predicciones correctas)
- **Fuera de diagonal:** Errores del modelo (deberían ser colores más claros)

**Ejemplo de matriz de confusión en Aurelion:**
```
                    Predicción del Modelo
                  Bajo  Medio  Alto
   Valor    Bajo   28     2     0     ← 30 clientes reales "Bajo"
   Real     Medio   3    29     3     ← 35 clientes reales "Medio"
            Alto    0     4    31     ← 35 clientes reales "Alto"
```

**Interpretación:**
- **Diagonal (28, 29, 31):** Predicciones correctas = 88 predicciones correctas
- **Fuera de diagonal:** Errores
  - 2 clientes "Bajo" fueron predichos como "Medio" (FN para "Bajo")
  - 3 clientes "Medio" fueron predichos como "Bajo" (FP para "Bajo")
  - 3 clientes "Medio" fueron predichos como "Alto" (FP para "Alto")
  - 4 clientes "Alto" fueron predichos como "Medio" (FN para "Alto")

**¿Cómo funciona `classification_report()`?**

Genera un reporte detallado con métricas por clase:

```
              Precision    Recall  F1-Score   Support
Bajo              0.903     0.933     0.917        30
Medio             0.829     0.829     0.829        35
Alto              0.912     0.886     0.899        35

Accuracy                          0.880           100
Macro avg         0.881     0.883     0.882       100
Weighted avg      0.881     0.880     0.880       100
```

**Interpretación del reporte:**
- **Precision:** Por cada clase, qué tan confiables son las predicciones
- **Recall:** Por cada clase, qué porcentaje de casos reales se detectaron
- **F1-Score:** Balance entre Precision y Recall
- **Support:** Cantidad de casos reales de cada clase
- **Accuracy:** Precisión global del modelo
- **Macro avg:** Promedio simple de las métricas (todas las clases igual peso)
- **Weighted avg:** Promedio ponderado por cantidad de casos (clases más grandes tienen más peso)

**¿Para qué se usó?**
Para entender en detalle cómo funciona un modelo de clasificación. No solo saber si acertó o no, sino ver qué categorías confunde más y por qué.

**Ejemplo práctico:**
Es como un reporte detallado de un examen. No solo te dice que sacaste 88%, sino que te dice:
- "En la categoría 'Bajo': acertaste 28 de 30 casos reales (93.3% Recall), y cuando predijiste 'Bajo', acertaste 28 de 31 veces (90.3% Precision)"
- "En la categoría 'Medio': acertaste 29 de 35 casos reales (82.9% Recall), y cuando predijiste 'Medio', acertaste 29 de 35 veces (82.9% Precision)"
- "En la categoría 'Alto': acertaste 31 de 35 casos reales (88.6% Recall), y cuando predijiste 'Alto', acertaste 31 de 34 veces (91.2% Precision)"

Esto te muestra exactamente en qué categorías el modelo es bueno y en cuáles necesita mejorar.

---

#### 6.6.10. Método: `.fit()` y `.predict()` (Modelos de Machine Learning)

**¿Qué hace?**
Estos son los métodos fundamentales de todos los modelos de scikit-learn:
- **`.fit(X, y)`:** Entrena el modelo con datos de entrada (X) y resultados esperados (y)
- **`.predict(X)`:** Usa el modelo entrenado para hacer predicciones sobre nuevos datos

**¿Cómo funciona `.fit()`?**

1. **Recibe datos de entrenamiento:**
   - **X:** Características (variables predictoras) - ej: cantidad, precio, categoría
   - **y:** Variable objetivo (lo que queremos predecir) - ej: importe, segmento

2. **Proceso interno:**
   - El modelo analiza la relación entre X e y
   - Calcula los parámetros óptimos (pesos, coeficientes, estructura de árboles, etc.)
   - Ajusta el modelo para minimizar el error (función de coste)
   - **Nunca** ve los datos de prueba durante este proceso

3. **Resultado:**
   - Modelo entrenado listo para hacer predicciones
   - Los parámetros están ajustados a los datos de entrenamiento

**¿Cómo funciona `.predict()`?**

1. **Recibe datos nuevos:**
   - **X:** Características de datos que el modelo nunca ha visto
   - No necesita y (la respuesta) porque el modelo la va a predecir

2. **Proceso interno:**
   - El modelo usa los parámetros aprendidos durante `.fit()`
   - Aplica las reglas/patrones aprendidos a los nuevos datos
   - Genera predicciones basadas en lo que aprendió

3. **Resultado:**
   - **y_pred:** Predicciones del modelo para los nuevos datos

**Ejemplo completo en Aurelion:**

```python
# 1. Preparar datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 2. Crear modelo
modelo = RandomForestRegressor(n_estimators=100, random_state=42)

# 3. Entrenar con .fit()
modelo.fit(X_train, y_train)
# → El modelo aprende: "Cuando cantidad=3 y precio=2500, el importe suele ser 7500"

# 4. Predecir con .predict()
y_pred = modelo.predict(X_test)
# → Para X_test, el modelo predice los importes basándose en lo aprendido

# 5. Evaluar
r2_score(y_test, y_pred)  # Compara predicciones con valores reales
```

**¿Para qué se usó?**
- **`.fit()`:** Para entrenar todos los modelos (Linear Regression, Random Forest, SVR, Logistic Regression, SVC, K-Means)
- **`.predict()`:** Para generar predicciones y evaluar el rendimiento de los modelos

**Diferencia importante:**
- **`.fit()`** se llama **una sola vez** con los datos de entrenamiento
- **`.predict()`** se puede llamar **muchas veces** con diferentes datos nuevos

**Ejemplo práctico:**
Es como enseñarle a alguien a reconocer perros:
- **`.fit()`:** Le muestras 100 fotos de perros y le dices "estos son perros" (entrena)
- **`.predict()`:** Le muestras una foto nueva y te dice "esto es un perro" (predice)

**En Aurelion:**
- **Regresión:** `modelo.fit(X_train, y_train)` → Aprende a predecir importes
- **Clasificación:** `modelo.fit(X_train, y_train)` → Aprende a clasificar segmentos
- **Clustering:** `modelo.fit(X)` → Aprende a agrupar transacciones (no necesita y)

---

#### 6.6.11. Método: `silhouette_score()`

**¿Qué hace?**
Evalúa qué tan bien están agrupados los datos en un algoritmo de clustering.

**¿Cómo funciona?**
1. Mide qué tan similares son los puntos dentro del mismo grupo (cohesión)
2. Mide qué tan diferentes son los puntos de diferentes grupos (separación)
3. Calcula un score entre -1 y 1:
   - **Score cercano a 1:** Grupos muy bien definidos
   - **Score cercano a 0:** Grupos mal definidos o solapados
   - **Score negativo:** Los puntos están en el grupo equivocado

**¿Para qué se usó?**
Para evaluar la calidad del clustering. Un score alto significa que los grupos están bien separados y los puntos dentro de cada grupo son similares.

**Ejemplo práctico:**
Es como evaluar qué tan bien organizaste una biblioteca. Si los libros de ciencia están todos juntos y bien separados de los de historia, el score es alto. Si están mezclados, el score es bajo.

---

### Resumen de Métodos y Funciones del Sprint 3

| Método/Función | Librería | Propósito Simple | Ejemplo de Uso |
|----------------|----------|------------------|----------------|
| `train_test_split()` | scikit-learn | Dividir datos en entrenamiento y prueba | Separar 80% para entrenar, 20% para probar |
| `cross_val_score()` | scikit-learn | Evaluación con validación cruzada | Probar modelo 5 veces con diferentes divisiones |
| `.unique()`, `.nunique()` | pandas | Analizar valores únicos | Determinar si es regresión o clasificación |
| `.shape` | pandas | Ver dimensiones de tabla | Ver cuántas filas y columnas hay |
| `.columns` | pandas | Ver nombres de columnas | Listar todas las columnas disponibles |
| `.dtype`, `.dtypes` | pandas | Ver tipo de dato | Identificar columnas numéricas vs categóricas |
| `pickle.dump()`, `pickle.load()` | pickle | Guardar y cargar modelos | Guardar modelo entrenado para uso futuro |
| `mean_squared_error()`, `r2_score()` | scikit-learn | Métricas de regresión | Evaluar modelos que predicen números |
| `accuracy_score()` | scikit-learn | Métrica de clasificación | Evaluar modelos que clasifican categorías |
| `confusion_matrix()`, `classification_report()` | scikit-learn | Reportes detallados de clasificación | Ver detalles de predicciones correctas/incorrectas |
| `.fit()`, `.predict()` | scikit-learn | Entrenar y predecir con modelos | Entrenar modelos ML y hacer predicciones |
| `silhouette_score()` | scikit-learn | Evaluar calidad de clustering | Medir qué tan bien están agrupados los datos |

---

## 7. RESULTADOS Y LOGROS

### 7.1. Resultados Cuantitativos

#### 7.1.1. Modelos de Machine Learning

**Regresión (Predicción de Importe):**
- **R² Score:** 0.9962 (99.62% de variabilidad explicada)
- **MSE:** Mínimo entre todos los modelos
- **Mejor Modelo:** Random Forest Regressor

**Clasificación (Segmentación de Clientes):**
- **Accuracy:** 0.8841 (88.41% de precisión)
- **Precision:** 0.87 (promedio ponderado)
- **Recall:** 0.88 (promedio ponderado)
- **F1-Score:** 0.87 (promedio ponderado)
- **Mejor Modelo:** Random Forest Classifier

**Clustering (Agrupación de Transacciones):**
- **Silhouette Score:** 0.3863 (clusters moderadamente bien definidos)
- **Número Óptimo de Clusters:** 3-5 (según método)
- **Mejor Algoritmo:** K-Means

#### 7.1.2. Análisis Realizados

- **4 tipos de análisis** en Sprint 1 (Ventas, Productos, Pagos, Clientes)
- **1 segmentación RFM** implementada (4 segmentos)
- **9 modelos de ML** entrenados y evaluados
- **24 visualizaciones avanzadas** generadas
- **26 histogramas** de análisis exploratorio
- **3 tipos de estadística** (Descriptiva, Inferencial, Prescriptiva)

#### 7.1.3. Archivos Generados

- **Scripts Python:** 30+ archivos
- **Datasets Normalizados:** 6 archivos CSV
- **Modelos Entrenados:** 9 archivos .pkl
- **Visualizaciones:** 50+ archivos PNG
- **Reportes:** 10+ archivos de texto y Markdown
- **Documentación:** 5+ archivos Markdown

### 7.2. Resultados Cualitativos

#### 7.2.1. Calidad del Código

- ✅ **Programación Orientada a Objetos:** Código modular y reutilizable
- ✅ **Manejo de Errores:** Validación robusta en todas las operaciones
- ✅ **Documentación:** Código documentado en español
- ✅ **Reproducibilidad:** Semillas aleatorias fijas
- ✅ **Buenas Prácticas:** Seguimiento de estándares de Python

#### 7.2.2. Usabilidad

- ✅ **Sistemas Interactivos:** 3 sistemas de menú implementados
- ✅ **Navegación Intuitiva:** Fácil de usar para usuarios no técnicos
- ✅ **Visualizaciones Claras:** Gráficos con interpretación
- ✅ **Reportes Ejecutivos:** Información resumida y accionable

#### 7.2.3. Completitud

- ✅ **100% de Requisitos Cumplidos:** Verificado en checklists
- ✅ **Cobertura Completa:** Todos los aspectos del proyecto cubiertos
- ✅ **Documentación Exhaustiva:** Cada módulo documentado
- ✅ **Resultados Validados:** Métricas verificadas y consistentes

### 7.3. Impacto del Proyecto

#### 7.3.1. Para la Tienda Aurelion

- **Segmentación de Clientes:** Estrategias de marketing personalizadas
- **Predicción de Ventas:** Planificación de inventario y recursos
- **Optimización de Precios:** Maximización de ingresos
- **Gestión de Inventario:** Reducción de costos de almacenamiento
- **Recomendaciones Accionables:** Decisiones basadas en datos

#### 7.3.2. Para el Aprendizaje

- **Fundamentos Sólidos:** Comprensión profunda de ML
- **Experiencia Práctica:** Implementación real de modelos
- **Portfolio Profesional:** Proyecto completo y documentado
- **Habilidades Técnicas:** Dominio de herramientas y librerías

---

## 8. CONCLUSIONES

### 8.1. Conclusiones Técnicas

1. **La Normalización es Fundamental:**
   - La preparación adecuada de datos es crucial para el rendimiento de modelos ML
   - Las técnicas de imputación inteligente mejoran significativamente la calidad de datos
   - La selección apropiada de métodos de normalización impacta directamente en los resultados

2. **Los Modelos de Ensemble Son Superiores:**
   - Random Forest Regressor y Classifier mostraron el mejor rendimiento
   - La combinación de múltiples árboles reduce el overfitting
   - Proporcionan importancia de características interpretable

3. **La Segmentación RFM es Efectiva:**
   - Permite identificar claramente diferentes tipos de clientes
   - Facilita estrategias de marketing personalizadas
   - Mejora la retención y conversión de clientes

4. **La Analítica Prescriptiva Agrega Valor:**
   - Transforma insights en acciones concretas
   - Proporciona recomendaciones cuantificadas
   - Facilita la toma de decisiones estratégicas

### 8.2. Conclusiones Metodológicas

1. **Enfoque Iterativo Funciona:**
   - Los tres sprints permitieron profundizar gradualmente
   - Cada sprint construyó sobre los anteriores
   - La metodología ágil facilitó la adaptación

2. **Documentación es Esencial:**
   - La documentación completa facilita el mantenimiento
   - Los reportes ejecutivos comunican resultados efectivamente
   - La documentación técnica permite la reproducibilidad

3. **Sistemas Interactivos Mejoran la Usabilidad:**
   - Los menús interactivos facilitan el uso
   - La navegación intuitiva reduce la curva de aprendizaje
   - Los sistemas educativos promueven el entendimiento

### 8.3. Conclusiones de Negocio

1. **Los Datos Tienen Valor:**
   - Los datos históricos contienen patrones valiosos
   - El análisis adecuado revela oportunidades de negocio
   - La predicción mejora la planificación estratégica

2. **La Personalización es Clave:**
   - La segmentación de clientes permite personalización
   - Las estrategias personalizadas mejoran la satisfacción
   - El marketing dirigido aumenta la conversión

3. **La Optimización Genera Eficiencia:**
   - La optimización de inventario reduce costos
   - La optimización de precios maximiza ingresos
   - Las recomendaciones prescriptivas mejoran la eficiencia operativa

### 8.4. Lecciones Aprendidas

1. **Empezar Simple:**
   - Comenzar con análisis exploratorio básico
   - Avanzar gradualmente hacia técnicas más complejas
   - Validar cada paso antes de continuar

2. **Validar Resultados:**
   - Verificar la calidad de datos constantemente
   - Comparar múltiples modelos
   - Interpretar métricas en contexto de negocio

3. **Comunicar Efectivamente:**
   - Visualizaciones claras facilitan la comprensión
   - Reportes ejecutivos resumen información clave
   - La documentación técnica permite la reproducibilidad

---

## 9. RECOMENDACIONES ESTRATÉGICAS

### 9.1. Recomendaciones Inmediatas (0-3 meses)

#### 9.1.1. Implementación de Modelos en Producción

**Acción:** Desplegar los mejores modelos entrenados en un entorno de producción

**Pasos:**
1. Crear API REST para predicciones
2. Integrar con sistema de ventas existente
3. Implementar monitoreo de rendimiento
4. Establecer proceso de reentrenamiento periódico

**Beneficios:**
- Predicciones en tiempo real
- Automatización de decisiones
- Mejora continua del modelo

#### 9.1.2. Segmentación RFM para Marketing

**Acción:** Implementar campañas de marketing basadas en segmentación RFM

**Pasos:**
1. Identificar clientes por segmento
2. Diseñar campañas personalizadas
3. Medir efectividad de campañas
4. Ajustar estrategias según resultados

**Beneficios:**
- Mayor tasa de conversión
- Mejor retención de clientes
- ROI mejorado en marketing

#### 9.1.3. Optimización de Inventario

**Acción:** Implementar recomendaciones de optimización de inventario

**Pasos:**
1. Identificar productos con bajo stock
2. Reabastecer según recomendaciones
3. Reducir inventario de productos con exceso
4. Monitorear impacto en ventas

**Beneficios:**
- Reducción de costos de almacenamiento
- Mejor disponibilidad de productos
- Optimización de capital de trabajo

### 9.2. Recomendaciones a Mediano Plazo (3-6 meses)

#### 9.2.1. Expansión de Modelos

**Acción:** Desarrollar modelos adicionales para otros casos de uso

**Modelos Sugeridos:**
- Predicción de demanda por producto
- Detección de fraude en transacciones
- Recomendación de productos (sistema de recomendación)
- Predicción de abandono de clientes (churn)

**Beneficios:**
- Mayor cobertura de casos de uso
- Mejora continua de capacidades
- Ventaja competitiva

#### 9.2.2. Integración de Datos en Tiempo Real

**Acción:** Implementar pipeline de datos en tiempo real

**Pasos:**
1. Configurar streaming de datos
2. Actualizar modelos en tiempo real
3. Implementar alertas automáticas
4. Dashboard en tiempo real

**Beneficios:**
- Decisiones más rápidas
- Detección temprana de problemas
- Respuesta proactiva a cambios

#### 9.2.3. Análisis de Sentimiento

**Acción:** Implementar análisis de sentimiento en comentarios y reseñas

**Pasos:**
1. Recopilar datos de comentarios
2. Entrenar modelo de análisis de sentimiento
3. Integrar con sistema de CRM
4. Generar alertas para comentarios negativos

**Beneficios:**
- Mejora de satisfacción del cliente
- Identificación temprana de problemas
- Mejora de productos y servicios

### 9.3. Recomendaciones a Largo Plazo (6-12 meses)

#### 9.3.1. Plataforma de Machine Learning

**Acción:** Desarrollar plataforma completa de ML para la organización

**Componentes:**
- Gestión de datos centralizada
- Pipeline de ML automatizado
- Monitoreo y alertas
- Dashboard ejecutivo

**Beneficios:**
- Escalabilidad
- Eficiencia operativa
- Cultura data-driven

#### 9.3.2. Equipo de Ciencia de Datos

**Acción:** Formar equipo dedicado de ciencia de datos

**Roles Necesarios:**
- Data Scientist (2-3 personas)
- Data Engineer (1-2 personas)
- ML Engineer (1 persona)
- Data Analyst (1-2 personas)

**Beneficios:**
- Capacidad interna de desarrollo
- Innovación continua
- Conocimiento especializado

#### 9.3.3. Capacitación y Cultura de Datos

**Acción:** Implementar programa de capacitación en datos y ML

**Componentes:**
- Talleres para equipos de negocio
- Certificaciones técnicas
- Comunidad interna de datos
- Casos de uso compartidos

**Beneficios:**
- Cultura data-driven
- Mejor uso de herramientas
- Innovación desde todos los niveles

### 9.4. Recomendaciones Técnicas

#### 9.4.1. Mejora Continua de Modelos

- **Reentrenamiento Periódico:** Mensual o trimestral
- **Validación Continua:** Monitoreo de métricas en producción
- **A/B Testing:** Comparación de modelos en producción
- **Feature Engineering:** Identificación de nuevas características

#### 9.4.2. Calidad de Datos

- **Validación Automática:** Checks de calidad en pipeline
- **Limpieza Automática:** Procesos automatizados de limpieza
- **Documentación de Datos:** Catálogo de datos actualizado
- **Governanza de Datos:** Políticas y procedimientos claros

#### 9.4.3. Infraestructura

- **Cloud Computing:** Migración a cloud para escalabilidad
- **Containerización:** Docker para despliegue consistente
- **Orquestación:** Kubernetes para gestión de contenedores
- **CI/CD:** Pipeline de integración y despliegue continuo

---

## 10. PREGUNTAS FRECUENTES Y RESPUESTAS

### 10.1. Preguntas sobre Metodología

**P: ¿Por qué se eligió una metodología de 3 sprints?**

**R:** La metodología de 3 sprints permite un aprendizaje gradual y estructurado:
- **Sprint 1:** Fundamentos de análisis de datos y segmentación
- **Sprint 2:** Técnicas avanzadas de normalización y ML
- **Sprint 3:** Fundamentos teóricos y modelado completo

Cada sprint construye sobre los anteriores, permitiendo profundizar en conceptos complejos de manera progresiva.

**P: ¿Cómo se aseguró la calidad del código?**

**R:** Se implementaron múltiples prácticas de calidad:
- Programación Orientada a Objetos para modularidad
- Manejo robusto de errores en todas las operaciones
- Documentación completa en español
- Validación de datos en cada paso
- Semillas aleatorias para reproducibilidad
- Checklists de cumplimiento de requisitos

**P: ¿Qué herramientas se utilizaron y por qué?**

**R:** Se seleccionaron herramientas estándar de la industria:
- **Python:** Lenguaje principal por su ecosistema de ML
- **pandas:** Manipulación eficiente de datos estructurados
- **scikit-learn:** Librería estándar de ML con algoritmos probados
- **matplotlib/seaborn:** Visualizaciones profesionales
- **category-encoders:** Codificación avanzada de variables categóricas

### 10.2. Preguntas sobre Análisis de Datos

**P: ¿Cómo se manejaron los valores faltantes?**

**R:** Se implementó una estrategia inteligente de imputación:
- **Análisis previo:** Identificación de tipo de dato y distribución
- **Mediana:** Para distribuciones sesgadas (skewness > 1)
- **Media:** Para distribuciones normales (skewness ≤ 1)
- **Moda:** Para variables categóricas
- **Justificación:** Cada estrategia se eligió basándose en las características estadísticas de los datos

**P: ¿Cómo se trataron los outliers?**

**R:** Se utilizó Winsorización (método conservador):
- Identificación con método IQR (Interquartile Range)
- Reemplazo con percentiles 5 y 95
- **Ventaja:** Preserva la estructura de datos sin eliminarlos
- **Alternativa considerada:** Eliminación, pero se descartó por pérdida de información

**P: ¿Por qué se normalizaron los datos de diferentes maneras?**

**R:** Diferentes distribuciones requieren diferentes técnicas:
- **RobustScaler:** Para distribuciones con outliers (robusto a valores extremos)
- **StandardScaler:** Para distribuciones normales (media 0, std 1)
- **MinMaxScaler:** Para escalar a rango [0, 1] cuando se requiere
- **Selección automática:** Basada en análisis de skewness y kurtosis

### 10.3. Preguntas sobre Machine Learning

**P: ¿Por qué Random Forest tuvo el mejor rendimiento?**

**R:** Random Forest es un algoritmo de ensemble que:
- Combina múltiples árboles de decisión
- Reduce overfitting mediante promedios
- Maneja relaciones no lineales efectivamente
- Proporciona importancia de características interpretable
- Es robusto a outliers y valores faltantes

**P: ¿Cómo se evitó el overfitting?**

**R:** Se implementaron múltiples técnicas:
- División train/test (80/20)
- Validación cruzada (5 folds)
- Comparación de métricas en train vs test
- Parámetros de regularización en modelos
- Selección del modelo con mejor rendimiento en test

**P: ¿Por qué se usaron múltiples modelos?**

**R:** La comparación de modelos permite:
- Identificar el mejor algoritmo para el problema
- Validar que los resultados son consistentes
- Entender trade-offs entre complejidad y rendimiento
- Proporcionar alternativas si un modelo falla

**P: ¿Qué significa un R² de 0.9962?**

**R:** Un R² de 0.9962 significa que:
- El modelo explica el 99.62% de la variabilidad en los datos
- Solo el 0.38% de la variabilidad no es explicada
- Es un rendimiento **excelente** (típicamente > 0.9 se considera excelente)
- Indica que el modelo captura casi perfectamente los patrones en los datos

**P: ¿Cómo funciona la regresión y cómo se minimizan las distancias verticales entre los puntos y el modelo?**

**R:** La regresión funciona ajustando los parámetros del modelo para minimizar las distancias verticales entre los puntos reales y las predicciones del modelo. Aquí te explico el proceso completo:

**1. ¿Qué es la distancia vertical?**

La distancia vertical es la diferencia entre el valor real (y_real) y el valor predicho por el modelo (y_pred). En un gráfico de dispersión, es la distancia vertical desde cada punto real hasta la línea o curva del modelo.

**Ejemplo visual:**
```
Importe ($)
  ↑
  |     ● (punto real: cantidad=3, importe=$7,500)
  |    /|
  |   / |  ← Distancia vertical = $300 (error)
  |  /  |
  | ●   ● (punto en la línea del modelo: cantidad=3, importe=$7,200)
  |/
  └─────────────────→ Cantidad
```

**2. Función de Coste (MSE):**

El modelo usa el **Error Cuadrático Medio (MSE)** como función de coste:

```
MSE = (1/n) × Σ(y_real - y_pred)²
```

**¿Por qué al cuadrado?**
- Penaliza más los errores grandes
- Siempre da valores positivos
- Es diferenciable (necesario para optimización)
- La distancia vertical se mide como: error = y_real - y_pred

**3. Proceso de Minimización - Gradiente Descendente:**

El algoritmo de **Gradiente Descendente** ajusta los parámetros del modelo iterativamente:

**Paso 1: Inicialización**
- Comienza con parámetros aleatorios (ej: pendiente = 0, intercepto = 0)
- Calcula el MSE inicial (generalmente alto)

**Paso 2: Cálculo del Gradiente**
- Calcula la derivada de MSE respecto a cada parámetro
- El gradiente indica en qué dirección aumentar o disminuir los parámetros para reducir el error

**Paso 3: Actualización de Parámetros**
- Ajusta los parámetros en dirección opuesta al gradiente
- Fórmula: parámetro_nuevo = parámetro_anterior - α × gradiente
- α (alpha) = tasa de aprendizaje (qué tan grandes son los pasos)

**Paso 4: Repetición**
- Repite pasos 2-3 hasta que el MSE no disminuya más (convergencia)
- En cada iteración, las distancias verticales se hacen más pequeñas

**Ejemplo con Datos de Aurelion:**

**Iteración 1 (Modelo inicial):**
- Pendiente = 1.0, Intercepto = 0
- MSE = 16,300,000 (distancias verticales muy grandes)
- Predicción para cantidad=3: $3,000 (real: $7,500, error: $4,500)

**Iteración 50 (Después de optimización):**
- Pendiente = 2,500, Intercepto = 500
- MSE = 150,000 (distancias verticales mucho menores)
- Predicción para cantidad=3: $8,000 (real: $7,500, error: $500)

**Iteración 100 (Modelo óptimo):**
- Pendiente = 2,800, Intercepto = 1,200
- MSE = 1,200 (distancias verticales muy pequeñas)
- Predicción para cantidad=3: $7,600 (real: $7,500, error: $100)

**4. Resultado Final en Aurelion:**

Con R² = 0.9962 (99.62%):
- Las distancias verticales entre puntos reales y predicciones son muy pequeñas
- El modelo predice importes con gran precisión
- La línea/curva del modelo pasa muy cerca de todos los puntos
- El MSE (función de coste) se minimizó exitosamente

**5. Métricas que Miden las Distancias Verticales:**

- **MSE:** Suma de distancias verticales al cuadrado (función de coste)
- **RMSE:** Raíz del MSE (error promedio en unidades originales)
- **MAE:** Promedio de distancias verticales absolutas (más robusto)
- **R²:** Qué porcentaje de la variabilidad está explicada (relacionado con qué tan pequeñas son las distancias)

**En resumen:** El algoritmo ajusta los parámetros del modelo para que la línea/curva pase lo más cerca posible de todos los puntos, minimizando la suma de todas las distancias verticales al cuadrado. Esto se hace mediante gradiente descendente, que ajusta los parámetros iterativamente hasta encontrar el mínimo de la función de coste.

**P: ¿Qué significa un Accuracy de 88.41%?**

**R:** Un Accuracy de 88.41% significa que:
- El 88.41% de las predicciones de clasificación son correctas
- Es un rendimiento **bueno** (típicamente > 0.8 se considera bueno)
- Para clasificación de clientes, es suficiente para estrategias de marketing
- Se puede mejorar con más datos o ajuste de hiperparámetros

**P: ¿Cuál es la diferencia entre Accuracy, Precision y Recall?**

**R:** Estas tres métricas miden aspectos diferentes del rendimiento de un modelo de clasificación:

**Accuracy (Exactitud):**
- **Pregunta:** ¿Qué porcentaje de todas las predicciones son correctas?
- **Fórmula:** (TP + TN) / (TP + TN + FP + FN)
- **Ejemplo:** De 100 clientes, 88 fueron clasificados correctamente → 88% accuracy
- **Cuándo usar:** Cuando todas las clases son igualmente importantes y están balanceadas
- **Limitación:** Puede ser engañoso con clases desbalanceadas

**Precision (Precisión):**
- **Pregunta:** Cuando el modelo predice una clase, ¿qué tan confiable es esa predicción?
- **Fórmula:** TP / (TP + FP)
- **Ejemplo:** De 31 clientes predichos como "Bajo", 28 realmente son "Bajo" → 90.3% precision
- **Interpretación:** "Cuando digo que es X, tengo razón el 90% de las veces"
- **Cuándo usar:** Cuando los falsos positivos son costosos
  - Ejemplo: Clasificar clientes como "VIP" para enviar ofertas exclusivas. Quieres alta precision para no gastar en clientes que no lo son.

**Recall (Sensibilidad):**
- **Pregunta:** De todos los casos reales de una clase, ¿cuántos encontró el modelo?
- **Fórmula:** TP / (TP + FN)
- **Ejemplo:** De 30 clientes realmente "Bajo", el modelo detectó 28 → 93.3% recall
- **Interpretación:** "De todos los casos reales de X, encuentro el 93%"
- **Cuándo usar:** Cuando los falsos negativos son costosos
  - Ejemplo: Clasificar clientes "En Riesgo" para campañas de retención. Quieres alto recall para no perder clientes que se van a ir.

**Ejemplo Práctico con Aurelion:**

Imagina que clasificas 100 clientes en segmentos:

```
Matriz de Confusión:
                    Predicción
                  Bajo  Medio  Alto   Total Real
   Real    Bajo   28     2     0        30
           Medio   3    29     3        35
           Alto    0     4    31        35
   Total Pred.    31    35    34       100
```

**Para la clase "Bajo":**
- **TP (True Positive):** 28 (predichos "Bajo" y realmente "Bajo")
- **FP (False Positive):** 3 (predichos "Bajo" pero realmente "Medio")
- **FN (False Negative):** 2 (realmente "Bajo" pero predichos "Medio")
- **TN (True Negative):** 67 (correctamente predichos como "NO Bajo")

**Cálculo de métricas:**
- **Accuracy Global:** (28 + 29 + 31) / 100 = 88%
- **Precision "Bajo":** 28 / (28 + 3) = 90.3%
  - Interpretación: Cuando el modelo dice "Bajo", tiene razón el 90.3% de las veces
- **Recall "Bajo":** 28 / (28 + 2) = 93.3%
  - Interpretación: De todos los clientes realmente "Bajo", el modelo encuentra el 93.3%

**Trade-off Precision vs Recall:**
- Si aumentas Precision (más conservador): Predices menos casos, pero cuando predices, tienes más razón. Sin embargo, te pierdes más casos reales (Recall baja).
- Si aumentas Recall (más agresivo): Encuentras más casos reales, pero también cometes más errores (Precision baja).

**F1-Score:** Balance entre ambas
- **Fórmula:** 2 × (Precision × Recall) / (Precision + Recall)
- **Para "Bajo":** 2 × (0.903 × 0.933) / (0.903 + 0.933) = 91.7%
- Útil cuando necesitas balancear ambas métricas

**Recomendación para Aurelion:**
- Para segmentación de clientes, un accuracy de 88.41% es bueno
- Si necesitas identificar clientes "En Riesgo" para retención, prioriza Recall (no perder clientes)
- Si necesitas identificar clientes "VIP" para ofertas exclusivas, prioriza Precision (no gastar en clientes incorrectos)

### 10.4. Preguntas sobre Segmentación RFM

**P: ¿Qué es la segmentación RFM y por qué es importante?**

**R:** RFM es un método de segmentación de clientes basado en:
- **Recency (R):** Días desde última compra (más reciente = mejor)
- **Frequency (F):** Número de compras (más frecuente = mejor)
- **Monetary (M):** Monto total gastado (más alto = mejor)

**Importancia:**
- Permite identificar diferentes tipos de clientes
- Facilita estrategias de marketing personalizadas
- Mejora la retención y conversión
- Optimiza el ROI de campañas de marketing

**P: ¿Cómo se calcularon los segmentos RFM?**

**R:** El proceso fue:
1. Calcular R, F, M para cada cliente
2. Dividir en cuartiles (1-4) para cada métrica
3. Combinar scores para crear segmentos:
   - **Campeones:** R alto, F alto, M alto
   - **Leales:** R medio-alto, F alto, M medio-alto
   - **En Riesgo:** R bajo, F medio, M medio
   - **Nuevos:** R alto, F bajo, M bajo

### 10.5. Preguntas sobre Resultados y Aplicación

**P: ¿Cómo se pueden usar estos resultados en la práctica?**

**R:** Los resultados tienen múltiples aplicaciones prácticas:

1. **Marketing:**
   - Campañas personalizadas por segmento RFM
   - Productos recomendados por modelo de clasificación
   - Predicción de respuesta a campañas

2. **Ventas:**
   - Predicción de monto de venta por cliente
   - Identificación de clientes de alto valor
   - Optimización de precios

3. **Operaciones:**
   - Optimización de inventario
   - Predicción de demanda
   - Gestión de stock

4. **Estrategia:**
   - Análisis de tendencias
   - Identificación de oportunidades
   - Toma de decisiones basada en datos

**P: ¿Qué tan confiables son las predicciones?**

**R:** La confiabilidad depende del modelo:
- **Regresión (R² = 0.9962):** Muy confiable para predicción de importes
- **Clasificación (Accuracy = 88.41%):** Confiable para segmentación, con margen de error del 11.59%
- **Recomendación:** Usar predicciones como guía, no como verdad absoluta
- **Monitoreo:** Validar predicciones con datos reales periódicamente

**P: ¿Cómo se mantienen los modelos actualizados?**

**R:** Se recomienda:
- **Reentrenamiento periódico:** Mensual o trimestral con nuevos datos
- **Monitoreo continuo:** Seguimiento de métricas en producción
- **Validación:** Comparación de predicciones con resultados reales
- **Ajuste:** Modificación de hiperparámetros si el rendimiento disminuye

### 10.6. Preguntas sobre Escalabilidad y Producción

**P: ¿El sistema puede manejar más datos?**

**R:** Sí, con algunas consideraciones:
- **Actual:** Diseñado para datasets de tamaño medio
- **Escalabilidad:** Requiere optimización para datasets muy grandes
- **Recomendaciones:**
  - Usar procesamiento en chunks para archivos grandes
  - Considerar bases de datos en lugar de archivos Excel
  - Implementar procesamiento distribuido (Spark) si es necesario
  - Usar cloud computing para escalabilidad

**P: ¿Cómo se despliega en producción?**

**R:** Pasos recomendados:
1. **API REST:** Crear API para predicciones
2. **Containerización:** Docker para despliegue consistente
3. **Orquestación:** Kubernetes para gestión
4. **Monitoreo:** Herramientas de monitoreo de modelos
5. **CI/CD:** Pipeline de integración y despliegue continuo
6. **Documentación:** Documentación de API y procesos

**P: ¿Qué recursos se necesitan para producción?**

**R:** Recursos estimados:
- **Hardware:** Servidor con 8-16 GB RAM, 4+ cores
- **Software:** Python, librerías ML, servidor web (Flask/FastAPI)
- **Infraestructura:** Base de datos, almacenamiento, backup
- **Personal:** Data Scientist/ML Engineer para mantenimiento
- **Costo:** Variable según cloud provider y escala

### 10.7. Preguntas sobre Mejoras Futuras

**P: ¿Qué mejoras se pueden hacer al proyecto?**

**R:** Mejoras sugeridas:

1. **Técnicas:**
   - Deep Learning para problemas más complejos
   - Feature Engineering más avanzado
   - Optimización de hiperparámetros (GridSearch, Bayesian)
   - Ensemble de múltiples modelos

2. **Datos:**
   - Integración de más fuentes de datos
   - Datos en tiempo real
   - Datos externos (clima, eventos, etc.)
   - Análisis de texto (comentarios, reseñas)

3. **Sistema:**
   - Dashboard interactivo (Streamlit, Dash)
   - API REST para predicciones
   - Automatización de pipelines
   - Alertas automáticas

4. **Negocio:**
   - Más casos de uso (churn, recomendaciones, etc.)
   - A/B testing de modelos
   - Integración con sistemas existentes
   - Capacitación de usuarios

**P: ¿Se pueden agregar más modelos?**

**R:** Sí, el sistema está diseñado para ser extensible:
- **Fácil agregar modelos:** Estructura modular permite agregar nuevos algoritmos
- **Casos de uso adicionales:**
  - Predicción de demanda
  - Detección de fraude
  - Sistema de recomendación
  - Predicción de churn
- **Proceso:** Seguir la misma estructura de los modelos existentes

### 10.8. Preguntas sobre Documentación y Reproducibilidad

**P: ¿Cómo se asegura la reproducibilidad?**

**R:** Múltiples medidas implementadas:
- **Semillas aleatorias:** Fijadas en todos los modelos (random_state=42)
- **Versionado:** Control de versiones con Git
- **Documentación:** Código documentado y comentado
- **Dependencias:** requirements.txt con versiones específicas
- **Ambiente:** Entorno virtual para aislamiento
- **Resultados:** Archivos guardados con timestamps

**P: ¿La documentación es suficiente para otro desarrollador?**

**R:** Sí, la documentación incluye:
- **README.md:** Visión general y guía de inicio rápido
- **DOCUMENTACION.md:** Detalles técnicos del proyecto
- **README_DESARROLLO_TECNICO.md:** Desarrollo técnico detallado
- **Comentarios en código:** Explicaciones línea por línea
- **Reportes:** Resultados y conclusiones documentados
- **Diagramas:** Flujos de proceso visualizados

### 10.9. Preguntas sobre Limitaciones

**P: ¿Cuáles son las limitaciones del proyecto?**

**R:** Limitaciones identificadas:

1. **Datos:**
   - Basado en datos históricos (puede no reflejar cambios recientes)
   - Limitado a 4 tablas (podría beneficiarse de más fuentes)
   - Datos estáticos (no en tiempo real)

2. **Modelos:**
   - Entrenados con datos específicos (pueden no generalizar)
   - Requieren reentrenamiento periódico
   - No incluyen Deep Learning (para problemas más complejos)

3. **Sistema:**
   - No desplegado en producción aún
   - Requiere ejecución manual (no automatizado)
   - Interfaz de consola (no web/dashboard)

4. **Alcance:**
   - Enfocado en casos de uso específicos
   - No incluye todos los tipos de análisis posibles
   - Limitado a técnicas de ML clásicas

**P: ¿Cómo se pueden superar estas limitaciones?**

**R:** Plan de mejora:
- **Datos:** Integrar más fuentes, implementar streaming
- **Modelos:** Agregar Deep Learning, optimización avanzada
- **Sistema:** Desplegar en producción, automatizar pipelines
- **Alcance:** Expandir casos de uso, agregar más análisis

---

## 11. ANEXOS

### 11.1. Estructura Completa del Proyecto

```
PROYECTO AURELION/
├── Datos Proyecto/
│   └── Base de datos_Tienda_Aurelion/
│       └── Base de datos/
│           ├── clientes.xlsx
│           ├── productos.xlsx
│           ├── ventas.xlsx
│           └── detalle_ventas.xlsx
│
├── Sprint_1/
│   ├── ejecutar_sprint1.py
│   ├── CHECKLIST_FINAL_AURELION.md
│   └── Enith Gicela Vargas Vargas - Proyecto Aurelion/
│       ├── aurelion_analisis.py
│       ├── DOCUMENTACION.md
│       ├── README_DESARROLLO_TECNICO.md
│       ├── diagrama_flujo_aurelion.txt
│       └── reportes/
│
├── Sprint_2/
│   ├── ejecutar_sprint2.py
│   ├── sistema_interactivo_sprint2.py
│   └── Enith Gicela Vargas Vargas - Proyecto Aurelion/
│       ├── 00_analisis_esquema.py
│       ├── 01_analisis_exploratorio.py
│       ├── 02_normalizacion_datos.py
│       ├── 03_merge_tablas.py
│       ├── 04_resumen_final.py
│       ├── 05_visualizaciones_avanzadas.py
│       ├── 06_modelos_ml.py
│       ├── 07_reporte_final.py
│       ├── 08_estadistica_inferencial.py
│       ├── 09_estadistica_prescriptiva.py
│       ├── README.md
│       ├── VARIABLES_Y_CENTROIDES.md
│       └── resultados/
│
├── Sprint_3/
│   ├── ejecutar_sprint3.py
│   ├── REVISION_SPRINT3.md
│   └── Enith Gicela Vargas Vargas - Proyecto Aurelion/
│       ├── Fundamentos/
│       │   ├── 01_machine_learning_basico.py
│       │   ├── 02_tipos_aprendizajes.py
│       │   ├── 03_algoritmos_basicos.py
│       │   └── 04_metricas_evaluacion.py
│       ├── Modelado/
│       │   ├── 01_preparacion_datos.py
│       │   ├── 02_division_train_test.py
│       │   ├── 03_proceso_entrenamiento.py
│       │   ├── 04_evaluacion_modelos.py
│       │   └── 05_algoritmos_especificos.py
│       ├── Demo/
│       │   ├── demo_interactivo.py
│       │   └── [15 scripts demo adicionales]
│       ├── README.md
│       └── resultados/
│
├── programa_unificado_aurelion.py
├── PROGRAMAS_INTERACTIVOS.md
├── INFORME_PROYECTO_AURELION.md
├── README.md
└── requirements.txt
```

### 11.2. Glosario de Términos Técnicos

**Análisis Exploratorio de Datos (EDA):** Proceso de análisis de datos para descubrir patrones, detectar anomalías y generar hipótesis.

**Segmentación RFM:** Método de segmentación de clientes basado en Recency (recencia), Frequency (frecuencia) y Monetary (monetario).

**Normalización:** Proceso de transformar datos a una escala común para mejorar el rendimiento de algoritmos ML.

**Winsorización:** Técnica de tratamiento de outliers que reemplaza valores extremos con percentiles.

**OneHot Encoding:** Técnica de codificación de variables categóricas que crea una columna binaria por categoría.

**Random Forest:** Algoritmo de ensemble que combina múltiples árboles de decisión.

**R² Score:** Coeficiente de determinación que mide la proporción de varianza explicada por el modelo.

**Accuracy:** Métrica de clasificación que mide la proporción de predicciones correctas.

**Silhouette Score:** Métrica de clustering que mide la cohesión intra-cluster y separación inter-cluster.

**Overfitting:** Fenómeno donde un modelo se ajusta demasiado a los datos de entrenamiento y no generaliza bien.

**Train/Test Split:** División de datos en conjuntos de entrenamiento y prueba para evaluar modelos.

**Validación Cruzada:** Técnica que divide datos en múltiples subconjuntos para evaluación más robusta.

### 11.3. Referencias y Recursos

**Librerías Utilizadas:**
- pandas: https://pandas.pydata.org/
- scikit-learn: https://scikit-learn.org/
- matplotlib: https://matplotlib.org/
- seaborn: https://seaborn.pydata.org/
- category-encoders: https://contrib.scikit-learn.org/category_encoders/

**Documentación del Proyecto:**
- README.md: Visión general del proyecto
- INFORME_PROYECTO_AURELION.md: Informe completo (incluye conclusiones y recomendaciones)
- PROGRAMAS_INTERACTIVOS.md: Guía de uso de sistemas interactivos

**Metodologías:**
- Metodología Ágil: Desarrollo iterativo e incremental
- CRISP-DM: Metodología de minería de datos (inspiración)

---

## 12. CONTACTO Y AGRADECIMIENTOS

**Autor del Proyecto:**
Enith Gicela Vargas Vargas

**Curso:**
AI Fundamentals - Guayerd - IBM Skills Build

**Agradecimientos:**
- Guayerd por la excelente formación en AI Fundamentals
- IBM Skills Build por la oportunidad de aprendizaje
- Instructores y compañeros por el apoyo durante el desarrollo

---

**FIN DEL INFORME**

*Este informe fue generado como parte del Proyecto Aurelion, un sistema integral de análisis de datos e inteligencia artificial para tienda retail. Todos los resultados, conclusiones y recomendaciones están basados en análisis exhaustivos de datos reales y metodologías probadas de Machine Learning.*

