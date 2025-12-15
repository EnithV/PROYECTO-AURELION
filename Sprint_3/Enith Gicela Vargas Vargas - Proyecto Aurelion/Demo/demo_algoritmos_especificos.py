#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
<!--
# DEMO ALGORITMOS ESPECIFICOS - SPRINT_3
**Autor:** Enith Gicela Vargas Vargas  
**Camada:** 1  
**Grupo:** 11  
**Fecha:** 2025-11-11  
**Curso:** AI Fundamentals - Guayerd - IBM Skills Build  
**Sprint:** 3 - Machine Learning Fundamentals  
**Módulo:** Demo - Algoritmos Específicos  
-->

DEMO DE ALGORITMOS ESPECIFICOS - PROYECTO AURELION SPRINT_3
===========================================================

Demo para ejecutar el módulo de algoritmos específicos ML.
"""

import sys               # Módulo para interactuar con el sistema
import os               # Módulo del sistema operativo
import importlib.util   # Módulo para importación dinámica
from pathlib import Path  # Módulo para manejo de rutas

def main():
    """Función principal del demo."""
    print("DEMO DE ALGORITMOS ESPECIFICOS ML")
    print("Grupo 11 - Camada 1 | Enith Gicela Vargas Vargas")
    print("=" * 60)
    
    try:
        # Cargar el módulo de algoritmos específicos
        # Manejar el caso cuando se ejecuta con exec() donde __file__ no está definido
        try:
            base_path = Path(__file__).parent
        except NameError:
            base_path = Path(os.getcwd())
            if not (base_path / "demo_algoritmos_especificos.py").exists():
                posibles = [
                    base_path / "Demo",
                    base_path.parent / "Demo",
                    base_path.parent.parent / "Enith Gicela Vargas Vargas - Proyecto Aurelion" / "Demo",
                ]
                for p in posibles:
                    if p.exists() and (p / "demo_algoritmos_especificos.py").exists():
                        base_path = p
                        break
        
        module_path = base_path.parent / "Modelado" / "05_algoritmos_especificos.py"
        
        spec = importlib.util.spec_from_file_location("algoritmos_especificos", module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        # Obtener la clase SpecificAlgorithms
        SpecificAlgorithms = getattr(module, 'SpecificAlgorithms')
        
        # Crear instancia y ejecutar
        demo = SpecificAlgorithms()
        demo.execute()
        
    except Exception as e:
        print(f"[ERROR] Error al ejecutar demo: {e}")
        print("Ejecutando módulo directamente...")
        os.system("python ../Modelado/05_algoritmos_especificos.py")

if __name__ == "__main__":
    main()
