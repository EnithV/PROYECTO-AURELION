#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DEMO CAFÉ DEL BARRIO - ANÁLISIS DE DATOS - PROYECTO AURELION SPRINT_1
=====================================================================

**Autor:** Enith Gicela Vargas Vargas  
**Fecha:** 2025-10-27  
**Curso:** AI Fundamentals - Guayerd - IBM Skills Build  
**Sprint:** 1 - Análisis de Datos Básico  
**Módulo:** Café del Barrio - Demo  

Script de demostración que ejecuta todas las tareas automáticamente
sin requerir interacción del usuario.
"""

# Importar la clase CafeDelBarrio del módulo cafe_del_barrio
# Esta clase contiene toda la lógica de análisis del café del barrio
from cafe_del_barrio import CafeDelBarrio

def main():
    """
    Ejecuta la demostración completa del análisis del café del barrio.
    
    Esta función crea una instancia del sistema y ejecuta todas las tareas
    de forma automática sin requerir interacción del usuario.
    """
    print("☕ DEMO - CAFÉ DEL BARRIO - ANÁLISIS DE DATOS")
    print("=" * 60)
    print("Ejecutando todas las tareas automáticamente...")
    print()
    
    # Crear instancia del sistema de análisis del café del barrio
    cafe = CafeDelBarrio()
    
    # Ejecutar reporte completo con todos los análisis automáticos
    cafe.generar_reporte_completo()

if __name__ == "__main__":
    main()
