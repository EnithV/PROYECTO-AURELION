#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Helper function para manejar rutas cuando __file__ no está definido.
"""

import os
from pathlib import Path

def get_demo_base_path(archivo_actual="demo_interactivo.py"):
    """
    Obtener la ruta base del directorio Demo.
    
    Maneja el caso cuando se ejecuta con exec() donde __file__ no está definido.
    
    Args:
        archivo_actual (str): Nombre del archivo actual para verificar
        
    Returns:
        Path: Ruta del directorio Demo
    """
    try:
        base_path = Path(__file__).parent
    except NameError:
        # Si __file__ no está definido, usar el directorio actual
        base_path = Path(os.getcwd())
        # Si no estamos en Demo, buscar el directorio correcto
        if not (base_path / archivo_actual).exists():
            # Buscar el directorio Demo
            posibles = [
                base_path / "Demo",
                base_path.parent / "Demo",
                base_path.parent.parent / "Enith Gicela Vargas Vargas - Proyecto Aurelion" / "Demo",
            ]
            for p in posibles:
                if p.exists() and (p / archivo_actual).exists():
                    base_path = p
                    break
    
    return base_path

