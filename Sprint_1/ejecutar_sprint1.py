#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SCRIPT DE EJECUCIÓN INDEPENDIENTE - SPRINT_1
============================================

**Autor:** Enith Gicela Vargas Vargas  
**Fecha:** 2025-10-27  
**Curso:** AI Fundamentals - Guayerd - IBM Skills Build  
**Sprint:** 1 - Análisis de Datos Básico  

Este script permite ejecutar el Sprint_1 de forma independiente.
"""

import os
import sys

# Obtener la ruta del directorio donde está este script
ruta_script = os.path.dirname(os.path.abspath(__file__))
ruta_sprint1 = os.path.join(ruta_script, "Enith Gicela Vargas Vargas - Proyecto Aurelion", "aurelion_analisis.py")

# Verificar que el archivo existe
if os.path.exists(ruta_sprint1):
    # Cambiar al directorio del Sprint_1
    directorio_sprint1 = os.path.dirname(ruta_sprint1)
    os.chdir(directorio_sprint1)
    
    # Ejecutar el programa
    print("🚀 Ejecutando Sprint_1 - Análisis de Datos Básico")
    print("=" * 60)
    print()
    
    try:
        exec(open(ruta_sprint1, encoding='utf-8').read())
    except Exception as e:
        print(f"❌ Error al ejecutar: {e}")
        sys.exit(1)
else:
    print(f"❌ No se encontró el archivo: {ruta_sprint1}")
    sys.exit(1)

