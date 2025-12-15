#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PRIMERAS 10 VENTAS - PROYECTO AURELION SPRINT_1
===============================================

**Autor:** Enith Gicela Vargas Vargas  
**Fecha:** 2025-10-27  
**Curso:** AI Fundamentals - Guayerd - IBM Skills Build  
**Sprint:** 1 - Análisis de Datos Básico  
**Módulo:** Primeras Ventas  

Análisis de las primeras 10 ventas de una tienda recién abierta.
El usuario ingresa los montos de las primeras 10 ventas y el programa
analiza estos datos para entender el arranque del negocio.

Funcionalidades:
1. Solicitar primeras 10 ventas
2. Calcular promedio de ventas
3. Identificar ventas sobre promedio
4. Análisis estadístico básico
5. Recomendaciones de negocio
"""

def solicitar_primeras_10_ventas():
    """Solicitar al usuario el monto de las primeras 10 ventas"""
    print("🏪 ANÁLISIS DE LAS PRIMERAS 10 VENTAS")
    print("=" * 50)
    print("Acabas de abrir tu primera tienda y quieres analizar")
    print("tus primeras 10 ventas para entender el arranque del negocio.")
    print()
    
    ventas = []
    
    for i in range(1, 11):
        while True:
            try:
                monto = float(input(f"Ingresa el monto de la venta {i}: $"))
                if monto < 0:
                    print("❌ El monto no puede ser negativo. Intenta nuevamente.")
                    continue
                ventas.append(monto)
                break
            except ValueError:
                print("❌ Por favor, ingresa un monto válido (número).")
            except KeyboardInterrupt:
                print("\n\nPrograma interrumpido por el usuario.")
                exit()
    
    return ventas

def calcular_promedio(ventas):
    """Calcular el promedio de las ventas iniciales"""
    if not ventas:
        return 0
    return sum(ventas) / len(ventas)

def identificar_ventas_sobre_promedio(ventas, promedio):
    """Identificar cuáles ventas estuvieron por encima del promedio"""
    ventas_sobre_promedio = []
    for i, venta in enumerate(ventas, 1):
        if venta > promedio:
            ventas_sobre_promedio.append((i, venta))
    return ventas_sobre_promedio

def calcular_total_recaudado(ventas):
    """Calcular el total recaudado en estas primeras ventas"""
    return sum(ventas)

def determinar_mejor_peor_venta(ventas):
    """Determinar cuál fue la mejor y peor venta inicial"""
    if not ventas:
        return None, None
    
    mejor_venta = max(ventas)
    peor_venta = min(ventas)
    
    # Encontrar las posiciones
    mejor_posicion = ventas.index(mejor_venta) + 1
    peor_posicion = ventas.index(peor_venta) + 1
    
    return (mejor_posicion, mejor_venta), (peor_posicion, peor_venta)

def mostrar_analisis(ventas):
    """Mostrar el análisis completo de las primeras 10 ventas"""
    
    print("\n" + "=" * 60)
    print("📊 ANÁLISIS DE LAS PRIMERAS 10 VENTAS")
    print("=" * 60)
    
    # Mostrar las ventas ingresadas
    print("\n💰 VENTAS INGRESADAS:")
    print("-" * 30)
    for i, venta in enumerate(ventas, 1):
        print(f"   Venta {i:2d}: ${venta:>8,.2f}")
    
    # 2. Calcular el promedio
    promedio = calcular_promedio(ventas)
    print(f"\n📈 PROMEDIO DE VENTAS INICIALES:")
    print("-" * 40)
    print(f"   Promedio: ${promedio:,.2f}")
    
    # 3. Identificar ventas sobre el promedio
    ventas_sobre_promedio = identificar_ventas_sobre_promedio(ventas, promedio)
    print(f"\n⬆️ VENTAS POR ENCIMA DEL PROMEDIO:")
    print("-" * 40)
    if ventas_sobre_promedio:
        print(f"   Total de ventas sobre promedio: {len(ventas_sobre_promedio)}")
        for posicion, monto in ventas_sobre_promedio:
            diferencia = monto - promedio
            print(f"   Venta {posicion:2d}: ${monto:>8,.2f} (+${diferencia:>6,.2f})")
    else:
        print("   No hay ventas por encima del promedio")
    
    # 4. Calcular el total recaudado
    total = calcular_total_recaudado(ventas)
    print(f"\n💵 TOTAL RECAUDADO:")
    print("-" * 30)
    print(f"   Total: ${total:,.2f}")
    
    # 5. Determinar mejor y peor venta
    mejor, peor = determinar_mejor_peor_venta(ventas)
    print(f"\n🏆 MEJOR Y PEOR VENTA:")
    print("-" * 30)
    if mejor and peor:
        print(f"   Mejor venta: #{mejor[0]} con ${mejor[1]:,.2f}")
        print(f"   Peor venta:  #{peor[0]} con ${peor[1]:,.2f}")
        diferencia = mejor[1] - peor[1]
        print(f"   Diferencia:  ${diferencia:,.2f}")
    
    # Insights adicionales
    print(f"\n💡 INSIGHTS ADICIONALES:")
    print("-" * 30)
    
    # Consistencia de ventas
    if len(ventas) > 1:
        desviacion = (max(ventas) - min(ventas)) / promedio * 100 if promedio > 0 else 0
        print(f"   Variabilidad: {desviacion:.1f}% (diferencia entre mejor y peor venta)")
    
    # Porcentaje sobre promedio
    porcentaje_sobre_promedio = (len(ventas_sobre_promedio) / len(ventas)) * 100
    print(f"   Ventas sobre promedio: {porcentaje_sobre_promedio:.1f}% del total")
    
    # Tendencia
    if len(ventas) >= 3:
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

def main():
    """Función principal del programa"""
    try:
        # 1. Solicitar al usuario el monto de las primeras 10 ventas
        ventas = solicitar_primeras_10_ventas()
        
        # Mostrar análisis completo
        mostrar_analisis(ventas)
        
    except KeyboardInterrupt:
        print("\n\nPrograma interrumpido por el usuario.")
    except Exception as e:
        print(f"\n❌ Error inesperado: {str(e)}")

if __name__ == "__main__":
    main()
