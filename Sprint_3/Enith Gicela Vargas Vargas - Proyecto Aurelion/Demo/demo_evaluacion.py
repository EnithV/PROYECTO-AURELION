#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
<!--
# DEMO EVALUACION MODELOS - SPRINT_3
**Autor:** Enith Gicela Vargas Vargas  
**Camada:** 1  
**Grupo:** 11  
**Fecha:** 2025-11-11  
**Curso:** AI Fundamentals - Guayerd - IBM Skills Build  
**Sprint:** 3 - Machine Learning Fundamentals  
**Módulo:** Demo - Evaluación de Modelos  
-->

DEMO DE EVALUACION DE MODELOS - PROYECTO AURELION SPRINT_3
===========================================================

Demo para ejecutar el módulo de evaluación de modelos ML.
"""

import sys               # Módulo para interactuar con el sistema
import os               # Módulo del sistema operativo
import importlib.util   # Módulo para importación dinámica
from pathlib import Path  # Módulo para manejo de rutas

def main():
    """Función principal del demo."""
    print("DEMO DE EVALUACION DE MODELOS ML")
    print("Grupo 11 - Camada 1 | Enith Gicela Vargas Vargas")
    print("=" * 60)
    
    try:
        # Cargar el módulo de evaluación
        # Manejar el caso cuando se ejecuta con exec() donde __file__ no está definido
        try:
            base_path = Path(__file__).parent
        except NameError:
            base_path = Path(os.getcwd())
            if not (base_path / "demo_evaluacion.py").exists():
                posibles = [
                    base_path / "Demo",
                    base_path.parent / "Demo",
                    base_path.parent.parent / "Enith Gicela Vargas Vargas - Proyecto Aurelion" / "Demo",
                ]
                for p in posibles:
                    if p.exists() and (p / "demo_evaluacion.py").exists():
                        base_path = p
                        break
        
        module_path = base_path.parent / "Modelado" / "04_evaluacion_modelos.py"
        
        spec = importlib.util.spec_from_file_location("evaluacion_modelos", module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        # Obtener la clase ModelEvaluation
        ModelEvaluation = getattr(module, 'ModelEvaluation')
        
        # Crear instancia y ejecutar
        demo = ModelEvaluation()
        demo.execute()
        
    except Exception as e:
        print(f"[ERROR] Error al ejecutar demo: {e}")
        print("Ejecutando módulo directamente...")
        os.system("python ../Modelado/04_evaluacion_modelos.py")

if __name__ == "__main__":
    main()
