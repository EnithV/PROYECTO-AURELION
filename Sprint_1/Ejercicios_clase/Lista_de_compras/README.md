<!--
# README.md
===========
Lista de compras interactiva - Sprint_1

Autor: Enith Gicela Vargas Vargas
Grupo: 11 - Camada 1
Curso: AI Fundamentals - Guayerd - IBM Skills Build
Fecha: 2025-10-27
Sprint: Sprint_1 - Análisis de Datos de Tienda
-->

# Lista de Compras - Programa Interactivo

Este proyecto implementa un sistema de lista de compras que cumple con los requisitos de la Task 2.

## Requisitos Cumplidos

✅ **Pedir al usuario el nombre y precio de 3 productos**  
✅ **Guardar los datos en una estructura que permita acceder tanto al nombre como al precio**  
✅ **Calcular el total a pagar**  
✅ **Mostrar la lista de productos y el total**

## Archivos del Proyecto

### 1. `lista_compras.py` - Programa Interactivo
- **Uso**: `python lista_compras.py`
- **Descripción**: Programa interactivo que pide al usuario ingresar 3 productos manualmente
- **Características**:
  - Validación de entrada (nombres no vacíos, precios válidos)
  - Manejo de errores
  - Interfaz amigable con mensajes claros

### 2. `demo_lista_compras.py` - Demostración
- **Uso**: `python demo_lista_compras.py`
- **Descripción**: Versión de demostración que muestra el funcionamiento con datos predefinidos
- **Características**:
  - Simula la entrada del usuario
  - Muestra el flujo completo del programa
  - Ideal para verificar el funcionamiento

## Estructura de Datos

El programa utiliza una **clase `Producto`** para almacenar cada producto:

```python
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
```

Y una **clase `ListaCompras`** para manejar la colección de productos:

```python
class ListaCompras:
    def __init__(self):
        self.productos = []  # Lista de objetos Producto
```

## Funcionalidades Implementadas

### 1. Entrada de Datos
- Solicita nombre y precio de 3 productos
- Valida que el nombre no esté vacío
- Valida que el precio sea un número válido y no negativo
- Maneja interrupciones del usuario (Ctrl+C)

### 2. Almacenamiento
- Utiliza una lista de objetos `Producto`
- Cada producto contiene nombre y precio
- Fácil acceso a ambos atributos

### 3. Cálculo
- Suma automática de todos los precios
- Formato de moneda con 2 decimales

### 4. Visualización
- Lista numerada de productos con precios
- Total destacado al final
- Formato profesional y claro

## Ejemplo de Salida

```
BIENVENIDO AL SISTEMA DE LISTA DE COMPRAS
==================================================
Vamos a registrar 3 productos para tu lista de compras.

--- PRODUCTO 1 ---
Ingrese el nombre del producto: Manzanas
Ingrese el precio del producto: $2.50
[OK] Producto 'Manzanas' agregado con precio $2.50

--- PRODUCTO 2 ---
Ingrese el nombre del producto: Leche
Ingrese el precio del producto: $3.20
[OK] Producto 'Leche' agregado con precio $3.20

--- PRODUCTO 3 ---
Ingrese el nombre del producto: Pan
Ingrese el precio del producto: $1.80
[OK] Producto 'Pan' agregado con precio $1.80

==================================================
           LISTA DE COMPRAS
==================================================

PRODUCTOS:
------------------------------
1. Manzanas: $2.50
2. Leche: $3.20
3. Pan: $1.80
------------------------------
TOTAL A PAGAR: $7.50
==================================================

¡Gracias por usar el sistema de lista de compras!
```

## Cómo Ejecutar

1. **Versión Interactiva** (entrada manual):
   ```bash
   python lista_compras.py
   ```

2. **Versión Demo** (datos predefinidos):
   ```bash
   python demo_lista_compras.py
   ```

## Tecnologías Utilizadas

- **Python 3.x**
- **Programación Orientada a Objetos**
- **Manejo de excepciones**
- **Validación de entrada**
- **Formateo de salida**

