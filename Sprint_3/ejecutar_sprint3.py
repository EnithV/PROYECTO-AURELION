#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SCRIPT DE EJECUCIÓN INDEPENDIENTE - SPRINT_3
============================================

**Autor:** Enith Gicela Vargas Vargas  
**Fecha:** 2025-11-11  
**Curso:** AI Fundamentals - Guayerd - IBM Skills Build  
**Sprint:** 3 - Machine Learning Fundamentals  

Este script permite ejecutar el Sprint_3 de forma independiente.
"""

import os
import sys
import subprocess

# Obtener la ruta del directorio donde está este script
ruta_script = os.path.dirname(os.path.abspath(__file__))
ruta_sprint3 = os.path.join(ruta_script, "Enith Gicela Vargas Vargas - Proyecto Aurelion", "Demo", "demo_interactivo.py")

# Verificar que el archivo existe
if os.path.exists(ruta_sprint3):
    # Guardar el directorio actual
    directorio_original = os.getcwd()
    
    try:
        # Cambiar al directorio del Demo (igual que programa_unificado_aurelion.py)
        directorio_demo = os.path.dirname(ruta_sprint3)
        directorio_demo = os.path.abspath(directorio_demo)  # Asegurar ruta absoluta
        os.chdir(directorio_demo)
        
        # Ejecutar el programa usando subprocess.run() (igual que programa_unificado_aurelion.py)
        # Esto asegura que __file__ esté definido correctamente
        print("🚀 Ejecutando Sprint_3 - Machine Learning Fundamentals")
        print("=" * 60)
        print()
        
        subprocess.run([sys.executable, ruta_sprint3], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Error al ejecutar Sprint_3: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print("❌ No se encontró el archivo demo_interactivo.py")
        sys.exit(1)
    finally:
        # Restaurar el directorio original
        os.chdir(directorio_original)
else:
    print(f"❌ No se encontró el archivo: {ruta_sprint3}")
    sys.exit(1)

