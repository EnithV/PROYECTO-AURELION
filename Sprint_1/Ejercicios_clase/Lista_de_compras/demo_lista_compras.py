#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DEMO - LISTA DE COMPRAS - PROGRAMA INTERACTIVO - PROYECTO AURELION SPRINT_1
===========================================================================

**Autor:** Enith Gicela Vargas Vargas  
**Fecha:** 2025-10-27  
**Curso:** AI Fundamentals - Guayerd - IBM Skills Build  
**Sprint:** 1 - Análisis de Datos Básico  
**Módulo:** Lista de Compras - Demo  

Esta es una versión de demostración que muestra cómo funciona el programa
con datos predefinidos para evitar la entrada interactiva.
"""

class Producto:
    """Clase para representar un producto con nombre y precio"""
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def __str__(self):
        return f"{self.nombre}: ${self.precio:.2f}"

class ListaCompras:
    """Clase principal para manejar la lista de compras"""
    
    def __init__(self):
        self.productos = []
    
    def agregar_producto(self, nombre, precio):
        """Agrega un producto a la lista"""
        producto = Producto(nombre, precio)
        self.productos.append(producto)
        print(f"[OK] Producto '{nombre}' agregado con precio ${precio:.2f}")
    
    def calcular_total(self):
        """Calcula el total a pagar"""
        total = sum(producto.precio for producto in self.productos)
        return total
    
    def mostrar_lista(self):
        """Muestra la lista de productos y el total"""
        print("\n" + "="*50)
        print("           LISTA DE COMPRAS")
        print("="*50)
        
        if not self.productos:
            print("No hay productos en la lista.")
            return
        
        print("\nPRODUCTOS:")
        print("-" * 30)
        for i, producto in enumerate(self.productos, 1):
            print(f"{i}. {producto}")
        
        total = self.calcular_total()
        print("-" * 30)
        print(f"TOTAL A PAGAR: ${total:.2f}")
        print("="*50)

def demo_interactivo():
    """Función de demostración que simula la entrada del usuario"""
    print("BIENVENIDO AL SISTEMA DE LISTA DE COMPRAS")
    print("=" * 50)
    print("Vamos a registrar 3 productos para tu lista de compras.")
    
    # Crear instancia de la lista de compras
    lista = ListaCompras()
    
    # Datos de demostración
    productos_demo = [
        ("Manzanas", 2.50),
        ("Leche", 3.20),
        ("Pan", 1.80)
    ]
    
    print("\n[DEMO] Simulando entrada de datos del usuario...")
    
    # Simular entrada de 3 productos
    for i, (nombre, precio) in enumerate(productos_demo, 1):
        print(f"\n--- PRODUCTO {i} ---")
        print(f"Usuario ingresa: {nombre}")
        print(f"Usuario ingresa: ${precio}")
        lista.agregar_producto(nombre, precio)
    
    # Mostrar la lista completa y el total
    lista.mostrar_lista()
    
    print("\n¡Gracias por usar el sistema de lista de compras!")

def demo_programa_original():
    """Demuestra el programa original con entrada real del usuario"""
    print("\n" + "="*60)
    print("VERSION INTERACTIVA DEL PROGRAMA")
    print("="*60)
    print("Para usar la versión interactiva, ejecute: python lista_compras.py")
    print("El programa pedirá al usuario ingresar 3 productos manualmente.")
    print("="*60)

if __name__ == "__main__":
    demo_interactivo()
    demo_programa_original()
