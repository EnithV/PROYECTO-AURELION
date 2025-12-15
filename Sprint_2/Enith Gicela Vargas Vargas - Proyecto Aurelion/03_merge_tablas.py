#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MERGE DE TABLAS NORMALIZADAS - PROYECTO AURELION SPRINT_2
=========================================================

**Autor:** Enith Gicela Vargas Vargas  
**Camada:** 1  
**Grupo:** 11  
**Fecha:** 2025-10-27  
**Curso:** AI Fundamentals - Guayerd - IBM Skills Build  
**Sprint:** 2 - Machine Learning y Normalización  
**Módulo:** Merge de Tablas  

Script para combinar todas las tablas normalizadas en un dataset
final para machine learning, manteniendo la integridad referencial
y las relaciones entre tablas.
"""

import pandas as pd          # Librería para manipulación y análisis de datos estructurados
import numpy as np           # Librería para operaciones numéricas y matemáticas
import os                    # Módulo del sistema operativo

class MergeTablas:
    """
    Clase para combinar tablas normalizadas.
    
    Funcionalidades:
    - Merge de tablas manteniendo integridad referencial
    - Validacion de relaciones
    - Creacion de dataset final para ML
    - Analisis de calidad del merge
    """
    
    def __init__(self):
        """Inicializar el mergeador."""
        self.base_path = "../../Datos Proyecto/Base de datos_Tienda_Aurelion/Base de datos"
        self.tablas_originales = {}
        self.tablas_normalizadas = {}
        self.dataset_final = None
        
    def cargar_tablas_originales(self):
        """Cargar tablas originales para referencia."""
        print("CARGANDO TABLAS ORIGINALES PARA REFERENCIA")
        print("=" * 60)
        
        try:
            self.tablas_originales['clientes'] = pd.read_excel(f"{self.base_path}/clientes.xlsx")
            self.tablas_originales['productos'] = pd.read_excel(f"{self.base_path}/productos.xlsx")
            self.tablas_originales['ventas'] = pd.read_excel(f"{self.base_path}/ventas.xlsx")
            self.tablas_originales['detalle_ventas'] = pd.read_excel(f"{self.base_path}/detalle_ventas.xlsx")
            
            print("Tablas originales cargadas exitosamente!")
            return True
            
        except Exception as e:
            print(f"Error al cargar tablas originales: {e}")
            return False
    
    def cargar_tablas_normalizadas(self):
        """Cargar tablas normalizadas."""
        print("\nCARGANDO TABLAS NORMALIZADAS")
        print("=" * 40)
        
        try:
            self.tablas_normalizadas['clientes'] = pd.read_csv("resultados/datasets_normalizados/clientes_normalizada.csv")
            self.tablas_normalizadas['productos'] = pd.read_csv("resultados/datasets_normalizados/productos_normalizada.csv")
            self.tablas_normalizadas['ventas'] = pd.read_csv("resultados/datasets_normalizados/ventas_normalizada.csv")
            self.tablas_normalizadas['detalle_ventas'] = pd.read_csv("resultados/datasets_normalizados/detalle_ventas_normalizada.csv")
            
            print("Tablas normalizadas cargadas exitosamente!")
            return True
            
        except Exception as e:
            print(f"Error al cargar tablas normalizadas: {e}")
            return False
    
    def merge_ventas_clientes(self):
        """Merge de ventas con clientes."""
        print("\nMERGE: VENTAS + CLIENTES")
        print("-" * 40)
        
        # Merge usando id_cliente
        ventas_clientes = self.tablas_normalizadas['ventas'].merge(
            self.tablas_normalizadas['clientes'],
            on='id_cliente',
            how='left',
            suffixes=('_venta', '_cliente')
        )
        
        print(f"   Registros antes del merge: {len(self.tablas_normalizadas['ventas'])}")
        print(f"   Registros despues del merge: {len(ventas_clientes)}")
        print(f"   Columnas resultantes: {len(ventas_clientes.columns)}")
        
        return ventas_clientes
    
    def merge_ventas_productos(self):
        """Merge de detalle_ventas con productos."""
        print("\nMERGE: DETALLE_VENTAS + PRODUCTOS")
        print("-" * 40)
        
        # Merge usando id_producto
        detalle_productos = self.tablas_normalizadas['detalle_ventas'].merge(
            self.tablas_normalizadas['productos'],
            on='id_producto',
            how='left',
            suffixes=('_detalle', '_producto')
        )
        
        print(f"   Registros antes del merge: {len(self.tablas_normalizadas['detalle_ventas'])}")
        print(f"   Registros despues del merge: {len(detalle_productos)}")
        print(f"   Columnas resultantes: {len(detalle_productos.columns)}")
        
        return detalle_productos
    
    def merge_final_completo(self):
        """Merge final de todas las tablas."""
        print("\nMERGE FINAL COMPLETO")
        print("=" * 50)
        
        # 1. Merge ventas + clientes
        ventas_clientes = self.merge_ventas_clientes()
        
        # 2. Merge detalle_ventas + productos
        detalle_productos = self.merge_ventas_productos()
        
        # 3. Merge final: (ventas + clientes) + (detalle_ventas + productos)
        dataset_final = detalle_productos.merge(
            ventas_clientes,
            on='id_venta',
            how='left',
            suffixes=('_detalle', '_venta')
        )
        
        print(f"\nDATASET FINAL CREADO:")
        print(f"   Registros: {len(dataset_final)}")
        print(f"   Columnas: {len(dataset_final.columns)}")
        print(f"   Memoria: {dataset_final.memory_usage(deep=True).sum() / 1024:.1f} KB")
        
        return dataset_final
    
    def validar_integridad_referencial(self, dataset_final):
        """Validar integridad referencial del dataset final."""
        print(f"\nVALIDACION DE INTEGRIDAD REFERENCIAL")
        print("-" * 50)
        
        # Verificar que no hay valores nulos en claves
        claves_importantes = ['id_venta', 'id_cliente', 'id_producto']
        problemas = []
        
        for clave in claves_importantes:
            if clave in dataset_final.columns:
                nulos = dataset_final[clave].isnull().sum()
                if nulos > 0:
                    problemas.append(f"{clave}: {nulos} valores nulos")
                else:
                    print(f"   {clave}: OK (sin valores nulos)")
        
        if problemas:
            print("   PROBLEMAS DETECTADOS:")
            for problema in problemas:
                print(f"     - {problema}")
        else:
            print("   [OK] Integridad referencial validada correctamente")
        
        return len(problemas) == 0
    
    def analizar_calidad_dataset(self, dataset_final):
        """Analizar calidad del dataset final."""
        print(f"\nANALISIS DE CALIDAD DEL DATASET")
        print("-" * 50)
        
        # Informacion basica
        print(f"   Dimensiones: {dataset_final.shape[0]} filas x {dataset_final.shape[1]} columnas")
        print(f"   Memoria utilizada: {dataset_final.memory_usage(deep=True).sum() / 1024:.1f} KB")
        
        # Analisis de valores nulos
        nulos_por_columna = dataset_final.isnull().sum()
        columnas_con_nulos = nulos_por_columna[nulos_por_columna > 0]
        
        if len(columnas_con_nulos) > 0:
            print(f"   Columnas con valores nulos: {len(columnas_con_nulos)}")
            for col, nulos in columnas_con_nulos.items():
                print(f"     - {col}: {nulos} nulos ({nulos/len(dataset_final)*100:.1f}%)")
        else:
            print("   [OK] Sin valores nulos en el dataset")
        
        # Analisis de tipos de datos
        tipos_datos = dataset_final.dtypes.value_counts()
        print(f"\n   TIPOS DE DATOS:")
        for tipo, cantidad in tipos_datos.items():
            print(f"     - {tipo}: {cantidad} columnas")
        
        # Analisis de columnas numericas
        columnas_numericas = dataset_final.select_dtypes(include=[np.number]).columns
        print(f"\n   COLUMNAS NUMERICAS: {len(columnas_numericas)}")
        
        # Analisis de columnas categoricas
        columnas_categoricas = dataset_final.select_dtypes(include=['object', 'category']).columns
        print(f"   COLUMNAS CATEGORICAS: {len(columnas_categoricas)}")
    
    def guardar_dataset_final(self, dataset_final):
        """Guardar dataset final."""
        print(f"\nGUARDANDO DATASET FINAL")
        print("-" * 30)
        
        try:
            # Guardar dataset completo
            archivo_completo = "resultados/datasets_normalizados/dataset_final_completo.csv"
            dataset_final.to_csv(archivo_completo, index=False, encoding='utf-8')
            print(f"   Dataset completo: {archivo_completo}")
            
            # Guardar muestra para inspeccion
            muestra = dataset_final.head(100)
            archivo_muestra = "resultados/datasets_normalizados/dataset_final_muestra.csv"
            muestra.to_csv(archivo_muestra, index=False, encoding='utf-8')
            print(f"   Muestra (100 registros): {archivo_muestra}")
            
            # Guardar informacion del dataset
            archivo_info = "resultados/estadisticas/dataset_final_info.txt"
            with open(archivo_info, 'w', encoding='utf-8') as f:
                f.write("DATASET FINAL - PROYECTO AURELION\n")
                f.write("=" * 50 + "\n\n")
                f.write(f"Dimensiones: {dataset_final.shape[0]} filas x {dataset_final.shape[1]} columnas\n")
                f.write(f"Memoria: {dataset_final.memory_usage(deep=True).sum() / 1024:.1f} KB\n\n")
                f.write("COLUMNAS:\n")
                for i, col in enumerate(dataset_final.columns, 1):
                    f.write(f"{i:2d}. {col}\n")
                f.write(f"\nTIPOS DE DATOS:\n")
                tipos = dataset_final.dtypes.value_counts()
                for tipo, cantidad in tipos.items():
                    f.write(f"  {tipo}: {cantidad} columnas\n")
            
            print(f"   Informacion del dataset: {archivo_info}")
            
        except Exception as e:
            print(f"   Error al guardar dataset: {e}")
    
    def ejecutar_merge_completo(self):
        """Ejecutar merge completo de todas las tablas."""
        print("MERGE DE TABLAS NORMALIZADAS - PROYECTO AURELION")
        print("Grupo 11 - Camada 1 | Enith Gicela Vargas Vargas")
        print("=" * 80)
        
        # Cargar tablas
        if not self.cargar_tablas_originales():
            return False
        
        if not self.cargar_tablas_normalizadas():
            return False
        
        # Realizar merge final
        dataset_final = self.merge_final_completo()
        
        # Validar integridad
        integridad_ok = self.validar_integridad_referencial(dataset_final)
        
        # Analizar calidad
        self.analizar_calidad_dataset(dataset_final)
        
        # Guardar dataset
        self.guardar_dataset_final(dataset_final)
        
        # Guardar referencia
        self.dataset_final = dataset_final
        
        print(f"\n[OK] Merge completado exitosamente!")
        print(f"[INFO] Dataset final listo para machine learning")
        print(f"[INFO] Archivos guardados en: resultados/datasets_normalizados/")
        
        return True

def main():
    """Funcion principal del merge."""
    mergeador = MergeTablas()
    mergeador.ejecutar_merge_completo()

if __name__ == "__main__":
    main()
