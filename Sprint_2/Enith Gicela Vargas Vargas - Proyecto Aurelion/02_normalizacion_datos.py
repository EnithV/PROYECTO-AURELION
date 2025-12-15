#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NORMALIZACION DE DATOS - PROYECTO AURELION SPRINT_2
==================================================

**Autor:** Enith Gicela Vargas Vargas  
**Camada:** 1  
**Grupo:** 11  
**Fecha:** 2025-10-27  
**Curso:** AI Fundamentals - Guayerd - IBM Skills Build  
**Sprint:** 2 - Machine Learning y Normalización  
**Módulo:** Normalización de Datos  

Script para normalizar datos de cada tabla de la base de datos Aurelion,
incluyendo:
- Tratamiento de outliers
- Normalizacion de variables numericas
- Encoding de variables categoricas
- Validacion de transformaciones
"""

import pandas as pd          # Librería para manipulación de datos estructurados
import numpy as np           # Librería para operaciones numéricas
import category_encoders as ce  # Librería para encoding avanzado de categóricas
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler, LabelEncoder  # Módulo de scikit-learn para preprocesamiento de datos
from sklearn.impute import SimpleImputer  # Imputador de valores faltantes
import warnings             # Módulo para controlar avisos del sistema
warnings.filterwarnings('ignore')

class NormalizadorDatos:
    """
    Clase para normalizar datos de la base de datos Aurelion.
    
    Funcionalidades:
    - Tratamiento de outliers
    - Normalizacion de variables numericas
    - Encoding de variables categoricas
    - Validacion de transformaciones
    """
    
    def __init__(self):
        """Inicializar el normalizador."""
        self.base_path = "../../Datos Proyecto/Base de datos_Tienda_Aurelion/Base de datos"
        self.tablas_originales = {}
        self.tablas_normalizadas = {}
        self.transformadores = {}
        self.resultados = {}
        
    def cargar_tablas(self):
        """Cargar todas las tablas de la base de datos."""
        print("CARGANDO TABLAS PARA NORMALIZACION")
        print("=" * 60)
        
        try:
            # Cargar cada tabla
            self.tablas_originales['clientes'] = pd.read_excel(f"{self.base_path}/clientes.xlsx")
            self.tablas_originales['productos'] = pd.read_excel(f"{self.base_path}/productos.xlsx")
            self.tablas_originales['ventas'] = pd.read_excel(f"{self.base_path}/ventas.xlsx")
            self.tablas_originales['detalle_ventas'] = pd.read_excel(f"{self.base_path}/detalle_ventas.xlsx")
            
            print("Todas las tablas cargadas exitosamente!")
            return True
            
        except Exception as e:
            print(f"Error al cargar tablas: {e}")
            return False
    
    def tratar_outliers(self, df, nombre_tabla):
        """Tratar outliers en variables numericas."""
        print(f"\nTRATAMIENTO DE OUTLIERS: {nombre_tabla.upper()}")
        print("-" * 50)
        
        df_tratado = df.copy()
        columnas_numericas = df.select_dtypes(include=[np.number]).columns
        outliers_info = {}
        
        for col in columnas_numericas:
            if df[col].notna().sum() > 0:
                # Metodo IQR para detectar outliers
                Q1 = df[col].quantile(0.25)
                Q3 = df[col].quantile(0.75)
                IQR = Q3 - Q1
                limite_inferior = Q1 - 1.5 * IQR
                limite_superior = Q3 + 1.5 * IQR
                
                outliers = df[(df[col] < limite_inferior) | (df[col] > limite_superior)]
                num_outliers = len(outliers)
                
                if num_outliers > 0:
                    print(f"   {col}: {num_outliers} outliers detectados ({num_outliers/len(df)*100:.1f}%)")
                    
                    # Estrategia: Winsorization (limitar valores extremos)
                    df_tratado[col] = np.where(df_tratado[col] < limite_inferior, limite_inferior, df_tratado[col])
                    df_tratado[col] = np.where(df_tratado[col] > limite_superior, limite_superior, df_tratado[col])
                    
                    print(f"     -> Aplicada Winsorization")
                else:
                    print(f"   {col}: Sin outliers")
                
                outliers_info[col] = {
                    'outliers_detectados': num_outliers,
                    'porcentaje': num_outliers/len(df)*100,
                    'tratamiento': 'Winsorization' if num_outliers > 0 else 'Ninguno'
                }
        
        return df_tratado, outliers_info
    
    def normalizar_variables_numericas(self, df, nombre_tabla):
        """Normalizar variables numericas."""
        print(f"\nNORMALIZACION DE VARIABLES NUMERICAS: {nombre_tabla.upper()}")
        print("-" * 60)
        
        df_normalizado = df.copy()
        columnas_numericas = df.select_dtypes(include=[np.number]).columns
        normalizaciones = {}
        
        for col in columnas_numericas:
            if col not in ['id_cliente', 'id_producto', 'id_venta']:  # No normalizar IDs
                print(f"   Normalizando {col}...")
                
                # Analizar distribucion para elegir metodo
                skewness = df[col].skew()
                
                if abs(skewness) > 1:  # Distribucion muy sesgada
                    # Usar RobustScaler (resistente a outliers)
                    scaler = RobustScaler()
                    metodo = "RobustScaler"
                elif abs(skewness) > 0.5:  # Distribucion moderadamente sesgada
                    # Usar StandardScaler
                    scaler = StandardScaler()
                    metodo = "StandardScaler"
                else:  # Distribucion normal
                    # Usar MinMaxScaler
                    scaler = MinMaxScaler()
                    metodo = "MinMaxScaler"
                
                # Aplicar normalizacion
                valores_originales = df[col].values.reshape(-1, 1)
                valores_normalizados = scaler.fit_transform(valores_originales)
                df_normalizado[col] = valores_normalizados.flatten()
                
                print(f"     -> Metodo: {metodo}")
                print(f"     -> Skewness original: {skewness:.3f}")
                print(f"     -> Rango normalizado: [{valores_normalizados.min():.3f}, {valores_normalizados.max():.3f}]")
                
                normalizaciones[col] = {
                    'metodo': metodo,
                    'skewness_original': skewness,
                    'scaler': scaler,
                    'rango_original': [df[col].min(), df[col].max()],
                    'rango_normalizado': [valores_normalizados.min(), valores_normalizados.max()]
                }
        
        return df_normalizado, normalizaciones
    
    def imputar_valores_faltantes(self, df, nombre_tabla):
        """Imputar valores faltantes usando estrategias inteligentes."""
        print(f"\nIMPUTACION DE VALORES FALTANTES: {nombre_tabla.upper()}")
        print("-" * 50)
        
        df_imputado = df.copy()
        imputaciones_info = {}
        
        for col in df.columns:
            if df[col].isnull().sum() > 0:  # Solo si hay valores faltantes
                nulos = df[col].isnull().sum()
                porcentaje = (nulos / len(df)) * 100
                
                print(f"   Imputando {col}: {nulos} valores faltantes ({porcentaje:.1f}%)")
                
                if df[col].dtype in ['int64', 'float64']:  # Variables numéricas
                    # Analizar distribución para elegir estrategia
                    skewness = abs(df[col].skew())
                    
                    if skewness > 1:  # Distribución sesgada
                        valor_imputado = df[col].median()
                        estrategia = "Mediana"
                    else:  # Distribución normal
                        valor_imputado = df[col].mean()
                        estrategia = "Media"
                    
                    df_imputado[col].fillna(valor_imputado, inplace=True)
                    print(f"     -> Estrategia: {estrategia} (skewness: {skewness:.3f})")
                    
                elif df[col].dtype in ['object', 'category']:  # Variables categóricas
                    valor_imputado = df[col].mode().iloc[0] if not df[col].mode().empty else "Desconocido"
                    df_imputado[col].fillna(valor_imputado, inplace=True)
                    estrategia = "Moda"
                    print(f"     -> Estrategia: {estrategia} (valor: {valor_imputado})")
                    
                elif df[col].dtype == 'bool':  # Variables booleanas
                    valor_imputado = df[col].mode().iloc[0] if not df[col].mode().empty else False
                    df_imputado[col].fillna(valor_imputado, inplace=True)
                    estrategia = "Moda"
                    print(f"     -> Estrategia: {estrategia} (valor: {valor_imputado})")
                
                imputaciones_info[col] = {
                    'valores_faltantes': nulos,
                    'porcentaje': porcentaje,
                    'estrategia': estrategia,
                    'valor_imputado': valor_imputado
                }
            else:
                print(f"   {col}: Sin valores faltantes")
                imputaciones_info[col] = {
                    'valores_faltantes': 0,
                    'porcentaje': 0,
                    'estrategia': 'Ninguna',
                    'valor_imputado': None
                }
        
        return df_imputado, imputaciones_info

    def codificar_variables_categoricas(self, df, nombre_tabla):
        """Codificar variables categoricas con category_encoders."""
        print(f"\nCODIFICACION DE VARIABLES CATEGORICAS: {nombre_tabla.upper()}")
        print("-" * 60)
        
        df_codificado = df.copy()
        columnas_categoricas = df.select_dtypes(include=['object', 'category']).columns
        codificaciones = {}
        
        for col in columnas_categoricas:
            if col not in ['nombre_cliente', 'email', 'nombre_producto']:  # No codificar nombres
                print(f"   Codificando {col}...")
                
                valores_unicos = df[col].nunique()
                print(f"     -> Valores únicos: {valores_unicos}")
                
                # Elegir estrategia según número de categorías
                if valores_unicos <= 5:  # Pocas categorías -> OneHot
                    encoder = ce.OneHotEncoder(cols=[col], use_cat_names=True)
                    metodo = "OneHot"
                    print(f"     -> Método: OneHot Encoding")
                    
                elif valores_unicos <= 20:  # Categorías moderadas -> Binary
                    encoder = ce.BinaryEncoder(cols=[col])
                    metodo = "Binary"
                    print(f"     -> Método: Binary Encoding")
                    
                else:  # Muchas categorías -> Target Encoding
                    encoder = ce.TargetEncoder(cols=[col], smoothing=1.0)
                    metodo = "Target"
                    print(f"     -> Método: Target Encoding")
                
                # Aplicar transformación usando fit_transform
                try:
                    df_codificado = encoder.fit_transform(df_codificado, df_codificado.get('importe', None))
                    print(f"     -> Transformación exitosa")
                    
                except Exception as e:
                    print(f"     -> Error en transformación: {e}")
                    # Fallback a Label Encoding
                    le = LabelEncoder()
                    df_codificado[col] = le.fit_transform(df[col])
                    metodo = "Label (fallback)"
                    print(f"     -> Fallback: Label Encoding")
                
                codificaciones[col] = {
                    'metodo': metodo,
                    'categorias': valores_unicos,
                    'valores_unicos': df[col].unique().tolist()[:10]  # Solo primeros 10
                }
        
        return df_codificado, codificaciones
    
    def normalizar_tabla_completa(self, nombre_tabla, df):
        """Normalizar una tabla completa con técnicas avanzadas."""
        print(f"\n{'='*80}")
        print(f"NORMALIZACION COMPLETA AVANZADA: {nombre_tabla.upper()}")
        print(f"{'='*80}")
        
        # 1. Imputar valores faltantes
        df_imputado, imputaciones_info = self.imputar_valores_faltantes(df, nombre_tabla)
        
        # 2. Tratar outliers
        df_sin_outliers, outliers_info = self.tratar_outliers(df_imputado, nombre_tabla)
        
        # 3. Normalizar variables numericas
        df_normalizado, normalizaciones = self.normalizar_variables_numericas(df_sin_outliers, nombre_tabla)
        
        # 4. Codificar variables categoricas
        df_final, codificaciones = self.codificar_variables_categoricas(df_normalizado, nombre_tabla)
        
        # Guardar resultados
        self.guardar_tabla_normalizada(nombre_tabla, df_final)
        self.guardar_resultados_normalizacion(nombre_tabla, {
            'imputaciones': imputaciones_info,
            'outliers': outliers_info,
            'normalizaciones': normalizaciones,
            'codificaciones': codificaciones
        })
        
        return df_final, {
            'imputaciones': imputaciones_info,
            'outliers': outliers_info,
            'normalizaciones': normalizaciones,
            'codificaciones': codificaciones
        }
    
    def guardar_tabla_normalizada(self, nombre_tabla, df):
        """Guardar tabla normalizada."""
        try:
            archivo = f"resultados/datasets_normalizados/{nombre_tabla}_normalizada.csv"
            df.to_csv(archivo, index=False, encoding='utf-8')
            print(f"   Tabla normalizada guardada: {archivo}")
        except Exception as e:
            print(f"   Error al guardar tabla: {e}")
    
    def guardar_resultados_normalizacion(self, nombre_tabla, resultados):
        """Guardar resultados de normalizacion."""
        try:
            archivo = f"resultados/estadisticas/normalizacion_{nombre_tabla}.txt"
            with open(archivo, 'w', encoding='utf-8') as f:
                f.write(f"NORMALIZACION AVANZADA - {nombre_tabla.upper()}\n")
                f.write("=" * 60 + "\n\n")
                
                # Imputaciones
                f.write("IMPUTACIONES DE VALORES FALTANTES:\n")
                imputaciones_realizadas = False
                for col, info in resultados['imputaciones'].items():
                    if info['valores_faltantes'] > 0:
                        f.write(f"  {col}: {info['valores_faltantes']} valores ({info['porcentaje']:.1f}%)\n")
                        f.write(f"    Estrategia: {info['estrategia']}\n")
                        f.write(f"    Valor imputado: {info['valor_imputado']}\n\n")
                        imputaciones_realizadas = True
                if not imputaciones_realizadas:
                    f.write("  No hay valores faltantes en esta tabla\n")
                
                # Outliers
                f.write("TRATAMIENTO DE OUTLIERS:\n")
                for col, info in resultados['outliers'].items():
                    f.write(f"  {col}: {info['outliers_detectados']} outliers ({info['porcentaje']:.1f}%)\n")
                    f.write(f"    Tratamiento: {info['tratamiento']}\n\n")
                
                # Normalizaciones
                f.write("NORMALIZACIONES NUMERICAS:\n")
                for col, info in resultados['normalizaciones'].items():
                    f.write(f"  {col}: {info['metodo']}\n")
                    f.write(f"    Skewness original: {info['skewness_original']:.3f}\n")
                    f.write(f"    Rango original: {info['rango_original']}\n")
                    f.write(f"    Rango normalizado: {info['rango_normalizado']}\n\n")
                
                # Codificaciones
                f.write("CODIFICACIONES CATEGORICAS AVANZADAS:\n")
                if resultados['codificaciones']:
                    for col, info in resultados['codificaciones'].items():
                        f.write(f"  {col}: {info['metodo']} ({info['categorias']} categorias)\n")
                        f.write(f"    Valores únicos: {info['valores_unicos']}\n\n")
                else:
                    f.write("  No hay variables categoricas para codificar (todas excluidas o no existen)\n")
            
            print(f"   Resultados guardados: {archivo}")
            
        except Exception as e:
            print(f"   Error al guardar resultados: {e}")
    
    def ejecutar_normalizacion_completa(self):
        """Ejecutar normalizacion completa de todas las tablas."""
        print("NORMALIZACION DE DATOS - PROYECTO AURELION")
        print("Grupo 11 - Camada 1 | Enith Gicela Vargas Vargas")
        print("=" * 80)
        
        # Cargar tablas
        if not self.cargar_tablas():
            return False
        
        # Normalizar cada tabla
        for nombre_tabla, df in self.tablas_originales.items():
            df_normalizado, resultados = self.normalizar_tabla_completa(nombre_tabla, df)
            self.tablas_normalizadas[nombre_tabla] = df_normalizado
            self.resultados[nombre_tabla] = resultados
        
        print(f"\nNormalizacion completada exitosamente!")
        print(f"Tablas normalizadas guardadas en: resultados/datasets_normalizados/")
        return True

def main():
    """Funcion principal de normalizacion."""
    normalizador = NormalizadorDatos()
    normalizador.ejecutar_normalizacion_completa()

if __name__ == "__main__":
    main()
