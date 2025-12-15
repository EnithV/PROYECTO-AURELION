#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SISTEMA DE DESPACHO INTELIGENTE - PROYECTO AURELION SPRINT_1
============================================================

**Autor:** Enith Gicela Vargas Vargas  
**Fecha:** 2025-10-27  
**Curso:** AI Fundamentals - Guayerd - IBM Skills Build  
**Sprint:** 1 - Análisis de Datos Básico  
**Módulo:** Despacho Inteligente  

Este programa calcula el recuento de pedidos por estado y método de envío
basándose en las reglas de negocio definidas.

Reglas de negocio:
1. Si Pago = Anulado → Estado = Anulado
2. Si Pago ≠ Aprobado → Estado = Pendiente
3. Si Pago = Aprobado y Stock = No → Estado = Enviado
4. Si Pago = Aprobado y Stock = Sí → Método de envío:
   - Moto si Destino = Capital y Peso ≤ 5
   - Correo si Destino = Interior y Peso ≤ 10
   - Expreso en cualquier otro caso
"""

class Pedido:
    """Clase para representar un pedido"""
    def __init__(self, id_pedido, pago, stock, destino, peso):
        self.id = id_pedido
        self.pago = pago
        self.stock = stock
        self.destino = destino
        self.peso = peso
        self.estado = None
        self.metodo_envio = None

class DespachoInteligente:
    """Clase principal del sistema de despacho inteligente"""
    
    def __init__(self):
        # Inicializar contadores
        self.contador_anulado = 0
        self.contador_pendiente = 0
        self.contador_enviado = 0
        self.contador_moto = 0
        self.contador_correo = 0
        self.contador_expreso = 0
        
    def procesar_pedido(self, pedido):
        """Procesa un pedido individual aplicando las reglas de negocio"""
        
        # Regla 1: Si Pago = Anulado → Estado = Anulado
        if pedido.pago == "Anulado":
            pedido.estado = "Anulado"
            self.contador_anulado += 1
            
        # Regla 2: Si Pago ≠ Aprobado → Estado = Pendiente
        elif pedido.pago != "Aprobado":
            pedido.estado = "Pendiente"
            self.contador_pendiente += 1
            
        # Regla 3: Si Pago = Aprobado y Stock = No → Estado = Enviado
        elif pedido.pago == "Aprobado" and pedido.stock == "No":
            pedido.estado = "Enviado"
            self.contador_enviado += 1
            
        # Regla 4: Si Pago = Aprobado y Stock = Sí → Determinar método de envío
        elif pedido.pago == "Aprobado" and pedido.stock == "Sí":
            # Determinar método de envío
            if pedido.destino == "Capital" and pedido.peso <= 5:
                pedido.metodo_envio = "Moto"
                self.contador_moto += 1
                
            elif pedido.destino == "Interior" and pedido.peso <= 10:
                pedido.metodo_envio = "Correo"
                self.contador_correo += 1
                
            else:
                pedido.metodo_envio = "Expreso"
                self.contador_expreso += 1
    
    def procesar_pedidos(self, lista_pedidos):
        """Procesa una lista de pedidos"""
        for pedido in lista_pedidos:
            self.procesar_pedido(pedido)
    
    def mostrar_resultados(self):
        """Muestra los resultados del procesamiento"""
        print("=" * 50)
        print("RESULTADOS DEL SISTEMA DE DESPACHO INTELIGENTE")
        print("=" * 50)
        print()
        
        print("RECUENTO DE PEDIDOS POR ESTADO:")
        print("-" * 35)
        print(f"Anulado: {self.contador_anulado}")
        print(f"Pendiente: {self.contador_pendiente}")
        print(f"Enviado: {self.contador_enviado}")
        print()
        
        print("RECUENTO DE PEDIDOS POR MÉTODO DE ENVÍO:")
        print("-" * 40)
        print(f"Moto: {self.contador_moto}")
        print(f"Correo: {self.contador_correo}")
        print(f"Expreso: {self.contador_expreso}")
        print()
        
        total_pedidos = (self.contador_anulado + self.contador_pendiente + 
                        self.contador_enviado + self.contador_moto + 
                        self.contador_correo + self.contador_expreso)
        print(f"TOTAL DE PEDIDOS PROCESADOS: {total_pedidos}")
    
    def mostrar_detalle_pedidos(self, lista_pedidos):
        """Muestra el detalle de cada pedido procesado"""
        print("=" * 80)
        print("DETALLE DE PEDIDOS PROCESADOS")
        print("=" * 80)
        print()
        
        print(f"{'ID':<8} | {'Pago':<10} | {'Stock':<5} | {'Destino':<8} | {'Peso':<4} | {'Estado':<10} | {'Método Envío':<12}")
        print("-" * 80)
        
        for pedido in lista_pedidos:
            estado = pedido.estado if pedido.estado else "-"
            metodo = pedido.metodo_envio if pedido.metodo_envio else "-"
            
            print(f"{pedido.id:<8} | {pedido.pago:<10} | {pedido.stock:<5} | {pedido.destino:<8} | {pedido.peso:<4} | {estado:<10} | {metodo:<12}")
        
        print()

def main():
    """Función principal del programa"""
    
    # Crear los pedidos de la tabla
    pedidos = [
        Pedido("0-702", "Pendiente", "Sí", "Interior", 7),
        Pedido("0-708", "Aprobado", "Sí", "Interior", 10),
        Pedido("0-705", "Aprobado", "No", "Capital", 2),
        Pedido("0-701", "Aprobado", "Sí", "Capital", 3),
        Pedido("0-703", "Aprobado", "Sí", "Interior", 8),
        Pedido("0-707", "Aprobado", "Sí", "Capital", 6),
        Pedido("0-704", "Aprobado", "Sí", "Interior", 12),
        Pedido("0-706", "Anulado", "Sí", "Capital", 1)
    ]
    
    # Crear instancia del sistema de despacho
    despacho = DespachoInteligente()
    
    # Mostrar detalle de pedidos antes del procesamiento
    despacho.mostrar_detalle_pedidos(pedidos)
    
    # Procesar todos los pedidos
    despacho.procesar_pedidos(pedidos)
    
    # Mostrar detalle de pedidos después del procesamiento
    despacho.mostrar_detalle_pedidos(pedidos)
    
    # Mostrar resultados finales
    despacho.mostrar_resultados()

if __name__ == "__main__":
    main()
