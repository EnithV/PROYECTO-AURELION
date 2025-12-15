#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ANÁLISIS DE ESQUEMA - PROYECTO AURELION SPRINT_2
=================================================

**Autor:** Enith Gicela Vargas Vargas  
**Camada:** 1  
**Grupo:** 11  
**Fecha:** 2025-10-27  
**Curso:** AI Fundamentals - Guayerd - IBM Skills Build  
**Sprint:** 2 - Machine Learning y Normalización  
**Módulo:** Análisis de Esquema  

Script para analizar la estructura de la base de datos Aurelion,
identificar Primary Keys (PK) y Foreign Keys (FK), y definir
el esquema de relaciones para la normalización de datos.
"""

import pandas as pd          # Librería para manipulación y análisis de datos estructurados
import numpy as np           # Librería para cálculos numéricos y operaciones matemáticas
import os                    # Módulo para interactuar con el sistema operativo
import sys                   # Módulo para interactuar con el intérprete de Python
from pathlib import Path     # Módulo para manipulación de rutas de archivos

class AnalisisEsquema:
    """
    Clase para analizar el esquema de la base de datos Aurelion.
    
    Funcionalidades:
    - Cargar y examinar cada tabla
    - Identificar PK y FK
    - Mapear relaciones entre tablas
    - Documentar esquema final
    """
    
    def __init__(self):
        """Inicializar el analizador de esquema."""
        self.base_path = "../../Datos Proyecto/Base de datos_Tienda_Aurelion/Base de datos"
        self.tablas = {}
        self.esquema = {}
        self.relaciones = {}
        
    def cargar_tablas(self):
        """Cargar todas las tablas de la base de datos."""
        print("CARGANDO TABLAS DE LA BASE DE DATOS AURELION")
        print("=" * 60)
        
        try:
            # Cargar tabla CLIENTES
            print("📊 Cargando clientes.xlsx...")
            self.tablas['clientes'] = pd.read_excel(f"{self.base_path}/clientes.xlsx")
            print(f"   ✅ Clientes: {len(self.tablas['clientes'])} registros")
            
            # Cargar tabla PRODUCTOS
            print("📊 Cargando productos.xlsx...")
            self.tablas['productos'] = pd.read_excel(f"{self.base_path}/productos.xlsx")
            print(f"   ✅ Productos: {len(self.tablas['productos'])} registros")
            
            # Cargar tabla VENTAS
            print("📊 Cargando ventas.xlsx...")
            self.tablas['ventas'] = pd.read_excel(f"{self.base_path}/ventas.xlsx")
            print(f"   ✅ Ventas: {len(self.tablas['ventas'])} registros")
            
            # Cargar tabla DETALLE_VENTAS
            print("📊 Cargando detalle_ventas.xlsx...")
            self.tablas['detalle_ventas'] = pd.read_excel(f"{self.base_path}/detalle_ventas.xlsx")
            print(f"   ✅ Detalle Ventas: {len(self.tablas['detalle_ventas'])} registros")
            
            print(f"\n✅ Todas las tablas cargadas exitosamente!")
            return True
            
        except Exception as e:
            print(f"❌ Error al cargar tablas: {e}")
            return False
    
    def analizar_estructura_tabla(self, nombre_tabla, df):
        """Analizar la estructura de una tabla específica."""
        print(f"\n📋 ANÁLISIS DE ESTRUCTURA: {nombre_tabla.upper()}")
        print("-" * 50)
        
        # Información básica
        print(f"📊 Dimensiones: {df.shape[0]} filas × {df.shape[1]} columnas")
        print(f"📊 Memoria: {df.memory_usage(deep=True).sum() / 1024:.1f} KB")
        
        # Información de columnas
        print(f"\n📝 COLUMNAS:")
        for i, col in enumerate(df.columns, 1):
            tipo = df[col].dtype
            nulos = df[col].isnull().sum()
            unicos = df[col].nunique()
            print(f"   {i:2d}. {col:<20} | Tipo: {str(tipo):<10} | Nulos: {nulos:3d} | Únicos: {unicos:4d}")
        
        # Valores únicos por columna
        print(f"\n🔍 ANÁLISIS DE UNICIDAD:")
        for col in df.columns:
            unicos = df[col].nunique()
            total = len(df)
            porcentaje = (unicos / total) * 100
            print(f"   {col:<20}: {unicos:4d} únicos ({porcentaje:5.1f}%)")
        
        return {
            'dimensiones': df.shape,
            'columnas': list(df.columns),
            'tipos': df.dtypes.to_dict(),
            'unicidad': {col: df[col].nunique() for col in df.columns},
            'nulos': df.isnull().sum().to_dict()
        }
    
    def identificar_primary_keys(self):
        """Identificar las Primary Keys de cada tabla."""
        print(f"\n🔑 IDENTIFICACIÓN DE PRIMARY KEYS")
        print("=" * 50)
        
        pk_candidatas = {}
        
        for nombre, df in self.tablas.items():
            print(f"\n📊 Tabla: {nombre.upper()}")
            
            # Buscar columnas candidatas a PK
            candidatas = []
            for col in df.columns:
                # Verificar si es única y no nula
                es_unica = df[col].nunique() == len(df)
                es_no_nula = df[col].notna().all()
                
                if es_unica and es_no_nula:
                    candidatas.append(col)
                    print(f"   ✅ {col}: ÚNICA y NO NULA → Candidata a PK")
                elif es_unica:
                    print(f"   ⚠️  {col}: ÚNICA pero tiene nulos")
                elif es_no_nula:
                    print(f"   ⚠️  {col}: NO NULA pero no es única")
                else:
                    print(f"   ❌ {col}: No es candidata")
            
            # Seleccionar PK (preferir columnas con 'id')
            pk_seleccionada = None
            for candidata in candidatas:
                if 'id' in candidata.lower():
                    pk_seleccionada = candidata
                    break
            
            if not pk_seleccionada and candidatas:
                pk_seleccionada = candidatas[0]
            
            pk_candidatas[nombre] = pk_seleccionada
            print(f"   🎯 PK seleccionada: {pk_seleccionada}")
        
        return pk_candidatas
    
    def identificar_foreign_keys(self, pk_candidatas):
        """Identificar las Foreign Keys entre tablas."""
        print(f"\n🔗 IDENTIFICACIÓN DE FOREIGN KEYS")
        print("=" * 50)
        
        fk_relaciones = {}
        
        # Mapear PKs para búsqueda
        pk_map = {tabla: pk for tabla, pk in pk_candidatas.items()}
        
        for tabla_origen, df_origen in self.tablas.items():
            print(f"\n📊 Analizando FK en tabla: {tabla_origen.upper()}")
            fk_encontradas = []
            
            for col in df_origen.columns:
                # Buscar si esta columna es FK de otra tabla
                for tabla_destino, pk_destino in pk_map.items():
                    if tabla_destino != tabla_origen and col == pk_destino:
                        # Verificar integridad referencial
                        valores_fk = df_origen[col].dropna()
                        valores_pk = self.tablas[tabla_destino][pk_destino]
                        
                        # Verificar si todos los valores FK existen en PK
                        valores_validos = valores_fk.isin(valores_pk).all()
                        
                        if valores_validos:
                            fk_encontradas.append({
                                'columna': col,
                                'tabla_destino': tabla_destino,
                                'pk_destino': pk_destino,
                                'integridad': 'OK'
                            })
                            print(f"   ✅ {col} → {tabla_destino}.{pk_destino} (Integridad OK)")
                        else:
                            print(f"   ❌ {col} → {tabla_destino}.{pk_destino} (Integridad ROTA)")
            
            fk_relaciones[tabla_origen] = fk_encontradas
        
        return fk_relaciones
    
    def definir_esquema_final(self, pk_candidatas, fk_relaciones):
        """Definir el esquema final con nombres estandarizados."""
        print(f"\n📋 ESQUEMA FINAL DEFINIDO")
        print("=" * 50)
        
        esquema = {
            'clientes': {
                'pk': pk_candidatas.get('clientes'),
                'fk': [],
                'columnas': list(self.tablas['clientes'].columns),
                'descripcion': 'Información de clientes'
            },
            'productos': {
                'pk': pk_candidatas.get('productos'),
                'fk': [],
                'columnas': list(self.tablas['productos'].columns),
                'descripcion': 'Catálogo de productos'
            },
            'ventas': {
                'pk': pk_candidatas.get('ventas'),
                'fk': [fk['columna'] for fk in fk_relaciones.get('ventas', [])],
                'columnas': list(self.tablas['ventas'].columns),
                'descripcion': 'Transacciones de ventas'
            },
            'detalle_ventas': {
                'pk': 'compuesta',  # (id_venta, id_producto)
                'fk': [fk['columna'] for fk in fk_relaciones.get('detalle_ventas', [])],
                'columnas': list(self.tablas['detalle_ventas'].columns),
                'descripcion': 'Detalle de productos por venta'
            }
        }
        
        # Mostrar esquema
        for tabla, info in esquema.items():
            print(f"\n📊 {tabla.upper()}:")
            print(f"   PK: {info['pk']}")
            print(f"   FK: {info['fk']}")
            print(f"   Columnas: {info['columnas']}")
            print(f"   Descripción: {info['descripcion']}")
        
        return esquema
    
    def generar_reporte_esquema(self):
        """Generar reporte completo del análisis de esquema."""
        print(f"\n📋 REPORTE COMPLETO DE ESQUEMA")
        print("=" * 60)
        
        # Cargar tablas
        if not self.cargar_tablas():
            return False
        
        # Analizar estructura de cada tabla
        for nombre, df in self.tablas.items():
            self.analizar_estructura_tabla(nombre, df)
        
        # Identificar PKs
        pk_candidatas = self.identificar_primary_keys()
        
        # Identificar FKs
        fk_relaciones = self.identificar_foreign_keys(pk_candidatas)
        
        # Definir esquema final
        esquema_final = self.definir_esquema_final(pk_candidatas, fk_relaciones)
        
        # Guardar esquema
        self.guardar_esquema(esquema_final)
        
        print(f"\n✅ Análisis de esquema completado exitosamente!")
        return True
    
    def guardar_esquema(self, esquema):
        """Guardar el esquema en un archivo."""
        try:
            with open('resultados/esquema_base_datos.txt', 'w', encoding='utf-8') as f:
                f.write("ESQUEMA DE BASE DE DATOS AURELION\n")
                f.write("=" * 50 + "\n\n")
                
                for tabla, info in esquema.items():
                    f.write(f"TABLA: {tabla.upper()}\n")
                    f.write(f"PK: {info['pk']}\n")
                    f.write(f"FK: {info['fk']}\n")
                    f.write(f"Columnas: {', '.join(info['columnas'])}\n")
                    f.write(f"Descripción: {info['descripcion']}\n")
                    f.write("-" * 30 + "\n\n")
            
            print("💾 Esquema guardado en: resultados/esquema_base_datos.txt")
            
        except Exception as e:
            print(f"❌ Error al guardar esquema: {e}")

def main():
    """Función principal del análisis de esquema."""
    print("🔍 ANÁLISIS DE ESQUEMA - PROYECTO AURELION")
    print("Grupo 11 - Camada 1 | Enith Gicela Vargas Vargas")
    print("=" * 60)
    
    # Crear instancia del analizador
    analizador = AnalisisEsquema()
    
    # Ejecutar análisis completo
    analizador.generar_reporte_esquema()

if __name__ == "__main__":
    main()
