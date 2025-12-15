#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
<!--
# PREPARACION DATOS ML - SPRINT_3
**Autor:** Enith Gicela Vargas Vargas  
**Camada:** 1  
**Grupo:** 11  
**Fecha:** 2025-11-11  
**Curso:** AI Fundamentals - Guayerd - IBM Skills Build  
**Sprint:** 3 - Machine Learning Fundamentals  
**Módulo:** Modelado - Preparación de Datos  
-->

PREPARACION DE DATOS PARA ML - PROYECTO AURELION SPRINT_3
==========================================================

Script para preparar datos para Machine Learning, incluyendo:
- Carga de datos
- Limpieza y tratamiento de valores faltantes
- Tratamiento de outliers
- Normalización y codificación
- División de características y target
"""

import pandas as pd          # Librería para manipulación de datos
import numpy as np           # Librería para cálculos numéricos
import matplotlib.pyplot as plt  # Librería para visualizaciones
import seaborn as sns       # Librería para gráficos estadísticos
import category_encoders as ce  # Librería para encoding avanzado de categóricas
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler  # Escaladores
from sklearn.preprocessing import LabelEncoder, OneHotEncoder  # Codificadores
from sklearn.impute import SimpleImputer  # Imputador de valores faltantes
import warnings             # Módulo para controlar avisos
warnings.filterwarnings('ignore')

class DataPreparation:
    """
    Clase para preparar datos para Machine Learning.
    
    Funcionalidades:
    - Carga de datos
    - Limpieza y tratamiento de valores faltantes
    - Tratamiento de outliers
    - Normalización y codificación
    - División de características y target
    """
    
    def __init__(self):
        """Inicializar el preparador de datos."""
        print("PREPARACION DE DATOS PARA MACHINE LEARNING")
        print("Grupo 11 - Camada 1 | Enith Gicela Vargas Vargas")
        print("=" * 60)
        
    def load_dataset(self):
        """Cargar dataset de Aurelion."""
        print("\nCARGANDO DATASET DE AURELION")
        print("-" * 50)
        
        try:
            # Cargar datos desde la carpeta de datos del proyecto
            # Buscar la ruta correcta de Datos Proyecto
            from pathlib import Path
            import os
            
            # Intentar diferentes rutas posibles
            try:
                file_base = Path(__file__).parent.parent.parent.parent
            except NameError:
                file_base = Path(os.getcwd()).parent.parent.parent
            
            rutas_posibles = [
                Path("../../../Datos Proyecto/Base de datos_Tienda_Aurelion/Base de datos"),
                Path("../../../../Datos Proyecto/Base de datos_Tienda_Aurelion/Base de datos"),
                file_base / "Datos Proyecto" / "Base de datos_Tienda_Aurelion" / "Base de datos",
            ]
            
            data_path = None
            for ruta in rutas_posibles:
                ruta_abs = Path(ruta).resolve() if isinstance(ruta, Path) else Path(os.path.abspath(ruta))
                if ruta_abs.exists() and (ruta_abs / "clientes.xlsx").exists():
                    data_path = str(ruta_abs) + os.sep
                    break
            
            if data_path is None:
                # Fallback a ruta relativa
                data_path = "../../../Datos Proyecto/Base de datos_Tienda_Aurelion/Base de datos/"
            
            # Cargar archivos principales
            clientes = pd.read_excel(data_path + "clientes.xlsx")
            productos = pd.read_excel(data_path + "productos.xlsx")
            ventas = pd.read_excel(data_path + "ventas.xlsx")
            detalle_ventas = pd.read_excel(data_path + "detalle_ventas.xlsx")
            
            print(f"[OK] Clientes cargados: {clientes.shape}")
            print(f"[OK] Productos cargados: {productos.shape}")
            print(f"[OK] Ventas cargadas: {ventas.shape}")
            print(f"[OK] Detalle ventas cargado: {detalle_ventas.shape}")
            
            # Crear dataset combinado para ML
            dataset_ml = self._create_ml_dataset(clientes, productos, ventas, detalle_ventas)
            
            return dataset_ml
            
        except Exception as e:
            print(f"[ERROR] Error al cargar datos: {e}")
            # Crear dataset sintético para demostración
            return self._create_synthetic_dataset()
    
    def _create_ml_dataset(self, clientes, productos, ventas, detalle_ventas):
        """Crear dataset combinado para ML."""
        print("\nCREANDO DATASET COMBINADO PARA ML")
        print("-" * 50)
        
        # Combinar ventas con detalle de ventas
        ventas_completas = ventas.merge(detalle_ventas, on='id_venta', how='inner')
        
        # Agregar información de clientes
        ventas_completas = ventas_completas.merge(clientes, on='id_cliente', how='left')
        
        # Agregar información de productos
        ventas_completas = ventas_completas.merge(productos, on='id_producto', how='left')
        
        # Seleccionar características relevantes para ML
        features_ml = [
            'cantidad', 'precio_unitario', 'importe',
            'edad', 'genero', 'ciudad',
            'categoria', 'precio', 'stock'
        ]
        
        # Filtrar columnas que existen
        available_features = [col for col in features_ml if col in ventas_completas.columns]
        dataset_ml = ventas_completas[available_features].copy()
        
        print(f"[OK] Dataset ML creado: {dataset_ml.shape}")
        print(f"[OK] Características seleccionadas: {available_features}")
        
        return dataset_ml
    
    def _create_synthetic_dataset(self):
        """Crear dataset sintético para demostración."""
        print("\nCREANDO DATASET SINTETICO PARA DEMOSTRACION")
        print("-" * 50)
        
        np.random.seed(42)
        n_samples = 1000
        
        # Crear datos sintéticos
        data = {
            'edad': np.random.randint(18, 80, n_samples),
            'genero': np.random.choice(['M', 'F'], n_samples),
            'ciudad': np.random.choice(['Bogota', 'Medellin', 'Cali', 'Barranquilla'], n_samples),
            'cantidad': np.random.randint(1, 10, n_samples),
            'precio_unitario': np.random.uniform(1000, 50000, n_samples),
            'categoria': np.random.choice(['Electronica', 'Ropa', 'Hogar', 'Deportes'], n_samples),
            'stock': np.random.randint(0, 100, n_samples)
        }
        
        # Calcular importe
        data['importe'] = data['cantidad'] * data['precio_unitario']
        
        dataset_ml = pd.DataFrame(data)
        print(f"[OK] Dataset sintético creado: {dataset_ml.shape}")
        
        return dataset_ml
    
    def analyze_missing_values(self, df):
        """Analizar valores faltantes con detalles avanzados."""
        print("\nANALISIS AVANZADO DE VALORES FALTANTES")
        print("-" * 50)
        
        missing_data = df.isnull().sum()
        missing_percent = (missing_data / len(df)) * 100
        
        missing_info = pd.DataFrame({
            'Valores_Faltantes': missing_data,
            'Porcentaje': missing_percent,
            'Tipo_Dato': df.dtypes,
            'Estrategia_Recomendada': ''
        })
        
        # Determinar estrategia recomendada por tipo de dato
        for idx, row in missing_info.iterrows():
            if row['Valores_Faltantes'] > 0:
                if row['Tipo_Dato'] in ['int64', 'float64']:
                    # Analizar distribución para elegir estrategia
                    skewness = abs(df[idx].skew())
                    if skewness > 1:
                        missing_info.loc[idx, 'Estrategia_Recomendada'] = 'Mediana'
                    else:
                        missing_info.loc[idx, 'Estrategia_Recomendada'] = 'Media'
                elif row['Tipo_Dato'] in ['object', 'category']:
                    missing_info.loc[idx, 'Estrategia_Recomendada'] = 'Moda'
                elif row['Tipo_Dato'] == 'bool':
                    missing_info.loc[idx, 'Estrategia_Recomendada'] = 'Moda'
        
        missing_info = missing_info[missing_info['Valores_Faltantes'] > 0]
        
        if len(missing_info) > 0:
            print("Valores faltantes encontrados:")
            print(missing_info[['Valores_Faltantes', 'Porcentaje', 'Estrategia_Recomendada']])
        else:
            print("[OK] No se encontraron valores faltantes")
        
        return missing_info
    
    def impute_missing_values_intelligent(self, df):
        """Imputar valores faltantes usando estrategias inteligentes."""
        print("\nIMPUTACION INTELIGENTE DE VALORES FALTANTES")
        print("-" * 50)
        
        df_imputado = df.copy()
        imputaciones_info = {}
        
        for col in df.columns:
            if df[col].isnull().sum() > 0:  # Solo si hay valores faltantes
                nulos = df[col].isnull().sum()
                porcentaje = (nulos / len(df)) * 100
                
                print(f"Imputando {col}: {nulos} valores faltantes ({porcentaje:.1f}%)")
                
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
                    print(f"  -> Estrategia: {estrategia} (skewness: {skewness:.3f})")
                    
                elif df[col].dtype in ['object', 'category']:  # Variables categóricas
                    valor_imputado = df[col].mode().iloc[0] if not df[col].mode().empty else "Desconocido"
                    df_imputado[col].fillna(valor_imputado, inplace=True)
                    estrategia = "Moda"
                    print(f"  -> Estrategia: {estrategia} (valor: {valor_imputado})")
                    
                elif df[col].dtype == 'bool':  # Variables booleanas
                    valor_imputado = df[col].mode().iloc[0] if not df[col].mode().empty else False
                    df_imputado[col].fillna(valor_imputado, inplace=True)
                    estrategia = "Moda"
                    print(f"  -> Estrategia: {estrategia} (valor: {valor_imputado})")
                
                imputaciones_info[col] = {
                    'valores_faltantes': nulos,
                    'porcentaje': porcentaje,
                    'estrategia': estrategia,
                    'valor_imputado': valor_imputado
                }
            else:
                imputaciones_info[col] = {
                    'valores_faltantes': 0,
                    'porcentaje': 0,
                    'estrategia': 'Ninguna',
                    'valor_imputado': None
                }
        
        return df_imputado, imputaciones_info
    
    def handle_outliers(self, df, method='iqr'):
        """Tratar outliers usando diferentes métodos."""
        print(f"\nTRATAMIENTO DE OUTLIERS - METODO: {method.upper()}")
        print("-" * 50)
        
        numeric_columns = df.select_dtypes(include=[np.number]).columns
        df_cleaned = df.copy()
        
        outliers_info = {}
        
        for col in numeric_columns:
            if method == 'iqr':
                Q1 = df[col].quantile(0.25)
                Q3 = df[col].quantile(0.75)
                IQR = Q3 - Q1
                lower_bound = Q1 - 1.5 * IQR
                upper_bound = Q3 + 1.5 * IQR
                
                outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
                outliers_count = len(outliers)
                
                if outliers_count > 0:
                    # Winsorización: reemplazar outliers con percentiles
                    df_cleaned[col] = np.where(df_cleaned[col] < lower_bound, 
                                              df[col].quantile(0.05), df_cleaned[col])
                    df_cleaned[col] = np.where(df_cleaned[col] > upper_bound, 
                                              df[col].quantile(0.95), df_cleaned[col])
                
                outliers_info[col] = {
                    'outliers_count': outliers_count,
                    'outliers_percent': (outliers_count / len(df)) * 100,
                    'lower_bound': lower_bound,
                    'upper_bound': upper_bound
                }
        
        # Mostrar resumen
        print("Resumen de outliers tratados:")
        for col, info in outliers_info.items():
            if info['outliers_count'] > 0:
                print(f"  {col}: {info['outliers_count']} outliers ({info['outliers_percent']:.1f}%)")
        
        return df_cleaned, outliers_info
    
    def encode_categorical(self, df):
        """Codificar variables categóricas usando category_encoders."""
        print("\nCODIFICACION AVANZADA DE VARIABLES CATEGORICAS")
        print("-" * 50)
        
        df_encoded = df.copy()
        categorical_columns = df.select_dtypes(include=['object', 'category']).columns
        encoding_info = {}
        
        for col in categorical_columns:
            unique_values = df[col].nunique()
            print(f"Codificando {col}: {unique_values} valores únicos")
            
            # Elegir estrategia según número de categorías
            if unique_values <= 5:  # Pocas categorías -> OneHot
                encoder = ce.OneHotEncoder(cols=[col], use_cat_names=True)
                method = "OneHot"
                print(f"  -> Método: OneHot Encoding")
                
            elif unique_values <= 20:  # Categorías moderadas -> Binary
                encoder = ce.BinaryEncoder(cols=[col])
                method = "Binary"
                print(f"  -> Método: Binary Encoding")
                
            else:  # Muchas categorías -> Target Encoding
                encoder = ce.TargetEncoder(cols=[col], smoothing=1.0)
                method = "Target"
                print(f"  -> Método: Target Encoding")
            
            # Aplicar transformación usando fit_transform
            try:
                df_encoded = encoder.fit_transform(df_encoded, df_encoded.get('importe', None))
                print(f"  -> Transformación exitosa")
                
            except Exception as e:
                print(f"  -> Error en transformación: {e}")
                # Fallback a Label Encoding
                encoder = LabelEncoder()
                df_encoded[col] = encoder.fit_transform(df[col])
                method = "Label (fallback)"
                print(f"  -> Fallback: Label Encoding")
            
            encoding_info[col] = {
                'method': method,
                'unique_values': unique_values,
                'encoder': encoder
            }
        
        print(f"[OK] Variables categóricas codificadas: {len(categorical_columns)}")
        return df_encoded, encoding_info
    
    def define_features_target(self, df, target_column='importe'):
        """Definir características y variable objetivo."""
        print(f"\nDEFINICION DE FEATURES Y TARGET")
        print("-" * 50)
        
        if target_column in df.columns:
            X = df.drop(target_column, axis=1)
            y = df[target_column]
            print(f"[OK] Target definido: {target_column}")
        else:
            # Si no existe la columna target, usar la última columna numérica
            numeric_cols = df.select_dtypes(include=[np.number]).columns
            target_column = numeric_cols[-1]
            X = df.drop(target_column, axis=1)
            y = df[target_column]
            print(f"[OK] Target automático: {target_column}")
        
        print(f"[OK] Features: {X.shape[1]} columnas")
        print(f"[OK] Target: {y.shape[0]} muestras")
        print(f"[OK] Features seleccionadas: {list(X.columns)}")
        
        return X, y, target_column
    
    def normalize_data(self, X, method='standard'):
        """Normalizar datos usando diferentes métodos."""
        print(f"\nNORMALIZACION DE DATOS - METODO: {method.upper()}")
        print("-" * 50)
        
        numeric_columns = X.select_dtypes(include=[np.number]).columns
        X_normalized = X.copy()
        
        if method == 'standard':
            scaler = StandardScaler()
        elif method == 'minmax':
            scaler = MinMaxScaler()
        elif method == 'robust':
            scaler = RobustScaler()
        else:
            print(f"[ERROR] Método {method} no reconocido")
            return X
        
        X_normalized[numeric_columns] = scaler.fit_transform(X[numeric_columns])
        
        print(f"[OK] Datos normalizados usando {method}")
        print(f"[OK] Columnas normalizadas: {len(numeric_columns)}")
        
        return X_normalized, scaler
    
    def save_prepared_dataset(self, X, y, target_column, scaler=None):
        """Guardar dataset preparado."""
        print(f"\nGUARDANDO DATASET PREPARADO")
        print("-" * 50)
        
        # Crear directorio de resultados si no existe
        import os
        os.makedirs("../resultados", exist_ok=True)
        
        # Guardar características y target
        X.to_csv("../resultados/dataset_ml_preparado.csv", index=False)
        y.to_csv("../resultados/target_ml.csv", index=False)
        
        # Guardar información de columnas
        with open("../resultados/columnas_features.txt", "w") as f:
            f.write("\n".join(X.columns))
        
        with open("../resultados/columnas_target.txt", "w") as f:
            f.write(target_column)
        
        # Guardar scaler si existe
        if scaler is not None:
            import pickle
            with open("../resultados/scaler.pkl", "wb") as f:
                pickle.dump(scaler, f)
        
        print(f"[OK] Dataset guardado en ../resultados/")
        print(f"[OK] Archivos creados:")
        print(f"  - dataset_ml_preparado.csv")
        print(f"  - target_ml.csv")
        print(f"  - columnas_features.txt")
        print(f"  - columnas_target.txt")
        if scaler:
            print(f"  - scaler.pkl")
    
    def generate_summary(self, df_original, df_cleaned, outliers_info, encoding_info, imputaciones_info):
        """Generar resumen del proceso de preparación."""
        print(f"\nRESUMEN DEL PROCESO DE PREPARACION")
        print("=" * 60)
        
        print(f"DATOS ORIGINALES:")
        print(f"  - Forma: {df_original.shape}")
        print(f"  - Columnas: {df_original.shape[1]}")
        print(f"  - Muestras: {df_original.shape[0]}")
        
        print(f"\nDATOS LIMPIOS:")
        print(f"  - Forma: {df_cleaned.shape}")
        print(f"  - Columnas: {df_cleaned.shape[1]}")
        print(f"  - Muestras: {df_cleaned.shape[0]}")
        
        if outliers_info:
            print(f"\nOUTLIERS TRATADOS:")
            for col, info in outliers_info.items():
                if info['outliers_count'] > 0:
                    print(f"  - {col}: {info['outliers_count']} outliers")
        
        if encoding_info:
            print(f"\nCODIFICACION REALIZADA:")
            for col, method in encoding_info.items():
                print(f"  - {col}: {method}")
        
        print(f"\n[OK] Preparacion de datos completada!")
    
    def execute(self):
        """Ejecutar proceso completo de preparación de datos."""
        # 1. Cargar datos
        df = self.load_dataset()
        
        # 2. Analizar valores faltantes
        missing_info = self.analyze_missing_values(df)
        
        # 3. Imputar valores faltantes inteligentemente
        df_imputado, imputaciones_info = self.impute_missing_values_intelligent(df)
        
        # 4. Tratar outliers
        df_cleaned, outliers_info = self.handle_outliers(df_imputado)
        
        # 5. Codificar variables categóricas
        df_encoded, encoding_info = self.encode_categorical(df_cleaned)
        
        # 6. Definir features y target
        X, y, target_column = self.define_features_target(df_encoded)
        
        # 7. IMPORTANTE: NO normalizar aquí - se normalizará DESPUÉS de dividir en train/test
        # La normalización debe hacerse en 02_division_train_test.py después de train_test_split
        # para evitar data leakage (fit_transform en training, transform en test)
        print(f"\n[INFO] Datos preparados sin normalizar")
        print(f"[INFO] La normalización se aplicará DESPUÉS de dividir en train/test")
        print(f"[INFO] Esto evita data leakage (el scaler aprende solo de datos de training)")
        
        # 8. Guardar dataset preparado (SIN normalizar)
        self.save_prepared_dataset(X, y, target_column, scaler=None)
        
        # 9. Generar resumen
        self.generate_summary(df, df_encoded, outliers_info, encoding_info, imputaciones_info)

def main():
    """Función principal del módulo."""
    preparador = DataPreparation()
    preparador.execute()

if __name__ == "__main__":
    main()
