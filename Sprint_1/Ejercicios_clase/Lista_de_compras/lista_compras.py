#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LISTA DE COMPRAS - PROYECTO AURELION SPRINT_1
=============================================

**Autor:** Enith Gicela Vargas Vargas  
**Fecha:** 2025-10-27  
**Curso:** AI Fundamentals - Guayerd - IBM Skills Build  
**Sprint:** 1 - Análisis de Datos Básico  
**Módulo:** Lista de Compras  

Programa interactivo que permite al usuario registrar productos y calcular 
información de la compra.

Funcionalidades:
1. Pedir al usuario el nombre y precio de 3 productos
2. Guardar los datos en una estructura que permita acceder tanto al nombre como al precio
3. Calcular el total a pagar
4. Mostrar la lista de productos y el total
5. Análisis de productos más caros y baratos
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

def pedir_datos_producto(numero_producto):
    """Pide al usuario los datos de un producto"""
    print(f"\n--- PRODUCTO {numero_producto} ---")
    
    while True:
        try:
            nombre = input("Ingrese el nombre del producto: ").strip()
            if not nombre:
                print("[ERROR] El nombre no puede estar vacío. Intente nuevamente.")
                continue
            break
        except KeyboardInterrupt:
            print("\n\nPrograma interrumpido por el usuario.")
            exit()
    
    while True:
        try:
            precio = float(input("Ingrese el precio del producto: $"))
            if precio < 0:
                print("[ERROR] El precio no puede ser negativo. Intente nuevamente.")
                continue
            break
        except ValueError:
            print("[ERROR] Por favor, ingrese un precio válido (número).")
        except KeyboardInterrupt:
            print("\n\nPrograma interrumpido por el usuario.")
            exit()
    
    return nombre, precio

def main():
    """Función principal del programa"""
    print("BIENVENIDO AL SISTEMA DE LISTA DE COMPRAS")
    print("=" * 50)
    print("Vamos a registrar 3 productos para tu lista de compras.")
    
    # Crear instancia de la lista de compras
    lista = ListaCompras()
    
    # Pedir datos de 3 productos
    for i in range(1, 4):
        try:
            nombre, precio = pedir_datos_producto(i)
            lista.agregar_producto(nombre, precio)
        except KeyboardInterrupt:
            print("\n\nPrograma interrumpido por el usuario.")
            exit()
    
    # Mostrar la lista completa y el total
    lista.mostrar_lista()
    
    print("\n¡Gracias por usar el sistema de lista de compras!")

if __name__ == "__main__":
    main()
