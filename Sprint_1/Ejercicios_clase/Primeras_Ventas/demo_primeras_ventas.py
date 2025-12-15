#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DEMO: PRIMERAS 10 VENTAS - PROYECTO AURELION SPRINT_1
======================================================

**Autor:** Enith Gicela Vargas Vargas  
**Fecha:** 2025-10-27  
**Curso:** AI Fundamentals - Guayerd - IBM Skills Build  
**Sprint:** 1 - Análisis de Datos Básico  
**Módulo:** Primeras Ventas - Demo  

Versión de demostración que muestra cómo funciona el programa
con datos de ejemplo predefinidos.
"""

def demo_primeras_10_ventas():
    """
    Demostración del análisis de las primeras 10 ventas.
    
    Esta función muestra cómo funciona el análisis automáticamente
    usando datos de ejemplo predefinidos, evitando la entrada del usuario.
    """
    
    print("🏪 ANÁLISIS DE LAS PRIMERAS 10 VENTAS")
    print("=" * 50)
    print("Acabas de abrir tu primera tienda y quieres analizar")
    print("tus primeras 10 ventas para entender el arranque del negocio.")
    print()
    
    # Datos de ejemplo simulando las primeras 10 ventas de una tienda recién abierta
    # Estos valores representan montos de ventas en pesos argentinos
    ventas = [150.50, 200.00, 175.25, 300.00, 125.75, 250.00, 180.00, 220.50, 195.25, 160.00]
    
    print("💰 VENTAS DE EJEMPLO (simuladas):")
    print("-" * 30)
    for i, venta in enumerate(ventas, 1):
        print(f"   Venta {i:2d}: ${venta:>8,.2f}")
    
    # ===== ANÁLISIS ESTADÍSTICO DE LAS VENTAS =====
    print("\n" + "=" * 60)
    print("📊 ANÁLISIS DE LAS PRIMERAS 10 VENTAS")
    print("=" * 60)
    
    # 1. Calcular promedio: Suma total de ventas dividida entre número de ventas
    # Este promedio nos da una idea del rendimiento promedio del negocio
    promedio = sum(ventas) / len(ventas)
    print(f"\n📈 PROMEDIO DE VENTAS INICIALES:")
    print("-" * 40)
    print(f"   Promedio: ${promedio:,.2f}")
    
    # 2. Identificar ventas sobre el promedio
    ventas_sobre_promedio = []
    for i, venta in enumerate(ventas, 1):
        if venta > promedio:
            ventas_sobre_promedio.append((i, venta))
    
    print(f"\n⬆️ VENTAS POR ENCIMA DEL PROMEDIO:")
    print("-" * 40)
    if ventas_sobre_promedio:
        print(f"   Total de ventas sobre promedio: {len(ventas_sobre_promedio)}")
        for posicion, monto in ventas_sobre_promedio:
            diferencia = monto - promedio
            print(f"   Venta {posicion:2d}: ${monto:>8,.2f} (+${diferencia:>6,.2f})")
    else:
        print("   No hay ventas por encima del promedio")
    
    # 3. Calcular total recaudado
    total = sum(ventas)
    print(f"\n💵 TOTAL RECAUDADO:")
    print("-" * 30)
    print(f"   Total: ${total:,.2f}")
    
    # 4. Determinar mejor y peor venta
    mejor_venta = max(ventas)
    peor_venta = min(ventas)
    mejor_posicion = ventas.index(mejor_venta) + 1
    peor_posicion = ventas.index(peor_venta) + 1
    
    print(f"\n🏆 MEJOR Y PEOR VENTA:")
    print("-" * 30)
    print(f"   Mejor venta: #{mejor_posicion} con ${mejor_venta:,.2f}")
    print(f"   Peor venta:  #{peor_posicion} con ${peor_venta:,.2f}")
    diferencia = mejor_venta - peor_venta
    print(f"   Diferencia:  ${diferencia:,.2f}")
    
    # Insights adicionales
    print(f"\n💡 INSIGHTS ADICIONALES:")
    print("-" * 30)
    
    # Variabilidad
    variabilidad = ((mejor_venta - peor_venta) / promedio) * 100
    print(f"   Variabilidad: {variabilidad:.1f}% (diferencia entre mejor y peor venta)")
    
    # Porcentaje sobre promedio
    porcentaje_sobre_promedio = (len(ventas_sobre_promedio) / len(ventas)) * 100
    print(f"   Ventas sobre promedio: {porcentaje_sobre_promedio:.1f}% del total")
    
    # Tendencia
    primeras_3 = sum(ventas[:3]) / 3
    ultimas_3 = sum(ventas[-3:]) / 3
    if ultimas_3 > primeras_3:
        print(f"   Tendencia: 📈 Mejorando (últimas 3 vs primeras 3)")
    elif ultimas_3 < primeras_3:
        print(f"   Tendencia: 📉 Empeorando (últimas 3 vs primeras 3)")
    else:
        print(f"   Tendencia: ➡️ Estable (últimas 3 vs primeras 3)")
    
    print(f"\n✅ Análisis completado exitosamente")
    print("=" * 60)
    
    print(f"\n📝 NOTA:")
    print("Este es un ejemplo con datos simulados.")
    print("Para usar el programa interactivo, ejecuta: python primeras_ventas.py")
    print("El programa te pedirá ingresar tus propias 10 ventas.")

if __name__ == "__main__":
    demo_primeras_10_ventas()
