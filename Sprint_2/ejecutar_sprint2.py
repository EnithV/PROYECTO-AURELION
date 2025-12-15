#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SCRIPT DE EJECUCIÓN INDEPENDIENTE - SPRINT_2
============================================

**Autor:** Enith Gicela Vargas Vargas  
**Fecha:** 2025-10-27  
**Curso:** AI Fundamentals - Guayerd - IBM Skills Build  
**Sprint:** 2 - Machine Learning y Normalización  

Este script permite ejecutar el Sprint_2 de forma independiente.
"""

import os
import sys

# Obtener la ruta del directorio donde está este script
ruta_script = os.path.dirname(os.path.abspath(__file__))
ruta_sprint2 = os.path.join(ruta_script, "sistema_interactivo_sprint2.py")

# Verificar que el archivo existe
if os.path.exists(ruta_sprint2):
    # Cambiar al directorio del Sprint_2
    os.chdir(ruta_script)
    
    # Ejecutar el programa
    print("🚀 Ejecutando Sprint_2 - Machine Learning y Normalización")
    print("=" * 60)
    print()
    
    try:
        exec(open(ruta_sprint2, encoding='utf-8').read())
    except Exception as e:
        print(f"❌ Error al ejecutar: {e}")
        sys.exit(1)
else:
    print(f"❌ No se encontró el archivo: {ruta_sprint2}")
    sys.exit(1)

