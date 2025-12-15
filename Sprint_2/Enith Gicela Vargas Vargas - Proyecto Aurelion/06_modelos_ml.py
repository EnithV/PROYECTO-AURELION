#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MODELOS DE MACHINE LEARNING - PROYECTO AURELION SPRINT_2
=========================================================

**Autor:** Enith Gicela Vargas Vargas  
**Camada:** 1  
**Grupo:** 11  
**Fecha:** 2025-10-27  
**Curso:** AI Fundamentals - Guayerd - IBM Skills Build  
**Sprint:** 2 - Machine Learning y Normalización  
**Módulo:** Modelos de Machine Learning  

Script para implementar modelos de Machine Learning en el dataset normalizado,
incluyendo:
- Regresion: Prediccion de importe y cantidad
- Clasificacion: Segmentacion de clientes
- Clustering: Agrupacion de productos/ventas
- Evaluacion de modelos con metricas apropiadas
"""

import pandas as pd          # Manipulación y análisis de datos estructurados
import numpy as np           # Operaciones numéricas y matemáticas con arrays
import matplotlib.pyplot as plt  # Creación de visualizaciones y gráficos
import seaborn as sns       # Visualizaciones estadísticas avanzadas
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV  # Módulo para dividir datos y validación
from sklearn.pipeline import Pipeline  # Pipeline para combinar transformaciones y modelos
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier  # Modelos de conjunto
from sklearn.linear_model import LinearRegression, LogisticRegression  # Modelos lineales
from sklearn.svm import SVR, SVC  # Support Vector Machines
from sklearn.cluster import KMeans, DBSCAN  # Algoritmos de clustering
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, classification_report, confusion_matrix  # Métricas de evaluación
from sklearn.preprocessing import StandardScaler  # Preprocesamiento de datos
import warnings             # Módulo para controlar avisos del sistema
warnings.filterwarnings('ignore')

class ModelosML:
    """
    Clase para implementar modelos de Machine Learning.
    
    Funcionalidades:
    - Regresion para prediccion de valores
    - Clasificacion para segmentacion
    - Clustering para agrupacion
    - Evaluacion y comparacion de modelos
    """
    
    def __init__(self):
        """Inicializar el modelo ML."""
        self.dataset = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.modelos = {}
        self.resultados = {}
        
    def cargar_dataset(self):
        """Cargar dataset final normalizado."""
        print("CARGANDO DATASET PARA MACHINE LEARNING")
        print("=" * 50)
        
        try:
            self.dataset = pd.read_csv("resultados/datasets_normalizados/dataset_final_completo.csv")
            print(f"Dataset cargado: {self.dataset.shape[0]} registros x {self.dataset.shape[1]} columnas")
            return True
        except Exception as e:
            print(f"Error al cargar dataset: {e}")
            return False
    
    def preparar_datos_regresion(self, variable_objetivo):
        """Preparar datos para regresion."""
        print(f"\nPREPARANDO DATOS PARA REGRESION: {variable_objetivo}")
        print("-" * 50)
        
        # Seleccionar solo variables numericas
        columnas_numericas = self.dataset.select_dtypes(include=[np.number]).columns.tolist()
        
        # Excluir IDs y variable objetivo
        columnas_excluir = ['id_venta', 'id_cliente', 'id_producto', variable_objetivo]
        columnas_predictoras = [col for col in columnas_numericas if col not in columnas_excluir]
        
        X = self.dataset[columnas_predictoras]
        y = self.dataset[variable_objetivo]
        
        # IMPORTANTE: Dividir PRIMERO en entrenamiento y prueba
        X_train_raw, X_test_raw, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        # IMPORTANTE: Normalizar DESPUÉS de dividir (evita data leakage)
        # fit_transform en training, transform en test
        scaler = StandardScaler()
        self.X_train = scaler.fit_transform(X_train_raw)  # Aprende SOLO de training
        self.X_test = scaler.transform(X_test_raw)        # Aplica parámetros de training
        self.y_train = y_train
        self.y_test = y_test
        
        # Guardar scaler para uso posterior
        self.scaler_regresion = scaler
        self.columnas_predictoras = columnas_predictoras
        
        # Convertir a DataFrame para mantener nombres de columnas
        self.X_train = pd.DataFrame(self.X_train, columns=columnas_predictoras, index=X_train_raw.index)
        self.X_test = pd.DataFrame(self.X_test, columns=columnas_predictoras, index=X_test_raw.index)
        
        print(f"   Variables predictoras: {X.shape[1]}")
        print(f"   Conjunto entrenamiento: {self.X_train.shape[0]} registros")
        print(f"   Conjunto prueba: {self.X_test.shape[0]} registros")
        print(f"   ✅ Normalización aplicada: fit_transform en training, transform en test")
        
        return X, y
    
    def entrenar_modelos_regresion(self, variable_objetivo):
        """Entrenar modelos de regresion."""
        print(f"\nENTRENANDO MODELOS DE REGRESION: {variable_objetivo}")
        print("-" * 50)
        
        # Preparar datos
        X, y = self.preparar_datos_regresion(variable_objetivo)
        
        # Definir modelos
        modelos = {
            'LinearRegression': LinearRegression(),
            'RandomForest': RandomForestRegressor(n_estimators=100, random_state=42),
            'SVR': SVR(kernel='rbf')
        }
        
        resultados = {}
        
        for nombre, modelo in modelos.items():
            print(f"   Entrenando {nombre}...")
            
            # Entrenar modelo
            modelo.fit(self.X_train, self.y_train)
            
            # Predicciones
            y_pred_train = modelo.predict(self.X_train)
            y_pred_test = modelo.predict(self.X_test)
            
            # Metricas
            mse_train = mean_squared_error(self.y_train, y_pred_train)
            mse_test = mean_squared_error(self.y_test, y_pred_test)
            r2_train = r2_score(self.y_train, y_pred_train)
            r2_test = r2_score(self.y_test, y_pred_test)
            
            # Cross-validation (usar datos normalizados correctamente)
            # Crear pipeline con normalización y modelo para CV
            # Esto asegura que cada fold normalice solo con sus datos de training
            pipeline = Pipeline([
                ('scaler', StandardScaler()),
                ('model', modelo)
            ])
            cv_scores = cross_val_score(pipeline, X, y, cv=5, scoring='r2')
            
            resultados[nombre] = {
                'modelo': modelo,
                'mse_train': mse_train,
                'mse_test': mse_test,
                'r2_train': r2_train,
                'r2_test': r2_test,
                'cv_mean': cv_scores.mean(),
                'cv_std': cv_scores.std(),
                'y_pred_test': y_pred_test
            }
            
            print(f"     R² entrenamiento: {r2_train:.4f}")
            print(f"     R² prueba: {r2_test:.4f}")
            print(f"     CV R²: {cv_scores.mean():.4f} (+/- {cv_scores.std()*2:.4f})")
        
        self.resultados[variable_objetivo] = resultados
        return resultados
    
    def entrenar_modelos_clasificacion(self, variable_objetivo):
        """Entrenar modelos de clasificacion."""
        print(f"\nENTRENANDO MODELOS DE CLASIFICACION: {variable_objetivo}")
        print("-" * 50)
        
        # Crear variable objetivo categórica basada en importe
        if variable_objetivo == 'segmento_cliente':
            # Crear segmentos basados en importe promedio
            importe_promedio = self.dataset.groupby('id_cliente')['importe'].mean()
            segmentos_cut = pd.cut(importe_promedio, bins=3, labels=['Bajo', 'Medio', 'Alto'])
            self.dataset['segmento_cliente'] = segmentos_cut.reindex(self.dataset['id_cliente']).values
            self.dataset['segmento_cliente'] = self.dataset['segmento_cliente'].fillna('Medio')
            
            # Guardar rangos específicos de importe para cada segmento
            self.rangos_segmentos = {}
            for segmento in ['Bajo', 'Medio', 'Alto']:
                clientes_segmento = importe_promedio[segmentos_cut == segmento]
                if len(clientes_segmento) > 0:
                    self.rangos_segmentos[segmento] = {
                        'min': clientes_segmento.min(),
                        'max': clientes_segmento.max(),
                        'promedio': clientes_segmento.mean(),
                        'mediana': clientes_segmento.median(),
                        'cantidad_clientes': len(clientes_segmento)
                    }
        
        # Preparar datos - solo variables numericas
        columnas_numericas = self.dataset.select_dtypes(include=[np.number]).columns.tolist()
        columnas_excluir = ['id_venta', 'id_cliente', 'id_producto', variable_objetivo, 'importe']
        columnas_predictoras = [col for col in columnas_numericas if col not in columnas_excluir]
        
        X = self.dataset[columnas_predictoras]
        y = self.dataset[variable_objetivo]
        
        # Verificar si se puede usar estratificación
        # La estratificación requiere que cada clase tenga al menos 2 miembros
        # y que haya suficientes clases para estratificar
        usar_stratify = False
        if len(y.unique()) <= 10:
            # Verificar que todas las clases tengan al menos 2 miembros
            conteo_clases = y.value_counts()
            if len(conteo_clases) > 0 and conteo_clases.min() >= 2:
                usar_stratify = True
                print(f"   ✅ Estratificación activada: {len(conteo_clases)} clases con distribución balanceada")
            else:
                print(f"   ⚠️  Estratificación desactivada: alguna clase tiene menos de 2 miembros")
                print(f"      Distribución de clases: {dict(conteo_clases)}")
        else:
            print(f"   ⚠️  Estratificación desactivada: demasiadas clases ({len(y.unique())})")
        
        # IMPORTANTE: Dividir PRIMERO en entrenamiento y prueba
        if usar_stratify:
            X_train_raw, X_test_raw, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42, stratify=y
            )
        else:
            X_train_raw, X_test_raw, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42
            )
        
        # IMPORTANTE: Normalizar DESPUÉS de dividir (evita data leakage)
        # fit_transform en training, transform en test
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train_raw)  # Aprende SOLO de training
        X_test = scaler.transform(X_test_raw)        # Aplica parámetros de training
        
        # Convertir a DataFrame para mantener nombres de columnas
        X_train = pd.DataFrame(X_train, columns=columnas_predictoras, index=X_train_raw.index)
        X_test = pd.DataFrame(X_test, columns=columnas_predictoras, index=X_test_raw.index)
        
        # Guardar scaler para uso posterior
        self.scaler_clasificacion = scaler
        
        # Definir modelos
        modelos = {
            'LogisticRegression': LogisticRegression(random_state=42, max_iter=1000),
            'RandomForest': RandomForestClassifier(n_estimators=100, random_state=42),
            'SVC': SVC(random_state=42)
        }
        
        resultados = {}
        
        for nombre, modelo in modelos.items():
            print(f"   Entrenando {nombre}...")
            
            # Entrenar modelo
            modelo.fit(X_train, y_train)
            
            # Predicciones
            y_pred_train = modelo.predict(X_train)
            y_pred_test = modelo.predict(X_test)
            
            # Metricas
            accuracy_train = accuracy_score(y_train, y_pred_train)
            accuracy_test = accuracy_score(y_test, y_pred_test)
            
            # Matriz de confusión
            cm = confusion_matrix(y_test, y_pred_test)
            
            # Classification report
            report = classification_report(y_test, y_pred_test, output_dict=True)
            
            # Cross-validation (usar datos normalizados correctamente)
            # Crear pipeline con normalización y modelo para CV
            # Esto asegura que cada fold normalice solo con sus datos de training
            pipeline = Pipeline([
                ('scaler', StandardScaler()),
                ('model', modelo)
            ])
            cv_scores = cross_val_score(pipeline, X, y, cv=5, scoring='accuracy')
            
            resultados[nombre] = {
                'modelo': modelo,
                'accuracy_train': accuracy_train,
                'accuracy_test': accuracy_test,
                'cv_mean': cv_scores.mean(),
                'cv_std': cv_scores.std(),
                'y_pred_test': y_pred_test,
                'y_test': y_test,
                'confusion_matrix': cm,
                'classification_report': report,
                'X_test': X_test,
                'y_test': y_test
            }
            
            print(f"     Accuracy entrenamiento: {accuracy_train:.4f}")
            print(f"     Accuracy prueba: {accuracy_test:.4f}")
            print(f"     CV Accuracy: {cv_scores.mean():.4f} (+/- {cv_scores.std()*2:.4f})")
            
            # Mostrar matriz de confusión en consola
            print(f"\n     Matriz de Confusión:")
            print(f"     {cm}")
        
        self.resultados[variable_objetivo] = resultados
        return resultados
    
    def entrenar_clustering(self):
        """Entrenar modelos de clustering."""
        print(f"\nENTRENANDO MODELOS DE CLUSTERING")
        print("-" * 40)
        
        # Seleccionar variables para clustering
        variables_clustering = ['cantidad', 'precio_unitario_detalle', 'importe']
        variables_disponibles = [v for v in variables_clustering if v in self.dataset.columns]
        
        if not variables_disponibles:
            print("   No hay variables numericas disponibles para clustering")
            return None
        
        X = self.dataset[variables_disponibles]
        
        # Normalizar datos
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        
        # K-Means
        print("   Entrenando K-Means...")
        kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
        clusters_kmeans = kmeans.fit_predict(X_scaled)
        
        # DBSCAN
        print("   Entrenando DBSCAN...")
        dbscan = DBSCAN(eps=0.5, min_samples=5)
        clusters_dbscan = dbscan.fit_predict(X_scaled)
        
        # Agregar clusters al dataset
        self.dataset['cluster_kmeans'] = clusters_kmeans
        self.dataset['cluster_dbscan'] = clusters_dbscan
        
        # Metricas de clustering
        from sklearn.metrics import silhouette_score
        
        silhouette_kmeans = silhouette_score(X_scaled, clusters_kmeans)
        n_clusters_dbscan = len(set(clusters_dbscan)) - (1 if -1 in clusters_dbscan else 0)
        
        print(f"     K-Means - Silhouette Score: {silhouette_kmeans:.4f}")
        print(f"     DBSCAN - Clusters encontrados: {n_clusters_dbscan}")
        
        # Guardar resultados para acceso posterior (incluyendo centroides)
        self.resultados_clustering = {
            'kmeans': kmeans,
            'dbscan': dbscan,
            'silhouette_kmeans': silhouette_kmeans,
            'n_clusters_dbscan': n_clusters_dbscan,
            'scaler': scaler,  # Guardar scaler para desnormalizar centroides
            'variables_clustering': variables_disponibles
        }
        
        # Mostrar información de centroides
        print(f"\n     Centroides K-Means (valores normalizados):")
        for i, centroide in enumerate(kmeans.cluster_centers_):
            print(f"       Cluster {i}: {centroide}")
        
        return self.resultados_clustering
    
    def crear_visualizaciones_modelos(self):
        """Crear visualizaciones de los modelos."""
        print(f"\nCREANDO VISUALIZACIONES DE MODELOS")
        print("-" * 45)
        
        # Grafico de comparacion de modelos de regresion
        if 'importe' in self.resultados:
            self.crear_grafico_comparacion_regresion()
        
        # Grafico de clustering
        self.crear_grafico_clustering()
        
        # Grafico de importancia de variables
        if 'importe' in self.resultados:
            self.crear_grafico_importancia_variables()
        
        # Matrices de confusión para modelos de clasificación
        if 'segmento_cliente' in self.resultados:
            self.crear_matrices_confusion()
    
    def crear_grafico_comparacion_regresion(self):
        """Crear grafico de comparacion de modelos de regresion."""
        if 'importe' not in self.resultados:
            return
        
        resultados = self.resultados['importe']
        
        # Crear grafico de comparacion
        fig, axes = plt.subplots(1, 2, figsize=(15, 6))
        
        # Grafico de valores reales vs predichos
        for i, (nombre, resultado) in enumerate(resultados.items()):
            y_pred = resultado['y_pred_test']
            axes[0].scatter(self.y_test, y_pred, alpha=0.6, label=nombre)
        
        axes[0].plot([self.y_test.min(), self.y_test.max()], 
                    [self.y_test.min(), self.y_test.max()], 'r--', lw=2)
        axes[0].set_xlabel('Valores Reales')
        axes[0].set_ylabel('Valores Predichos')
        axes[0].set_title('Valores Reales vs Predichos')
        axes[0].legend()
        axes[0].grid(True, alpha=0.3)
        
        # Grafico de metricas
        modelos = list(resultados.keys())
        r2_scores = [resultados[modelo]['r2_test'] for modelo in modelos]
        
        axes[1].bar(modelos, r2_scores, color=['skyblue', 'lightcoral', 'lightgreen'])
        axes[1].set_ylabel('R² Score')
        axes[1].set_title('Comparacion de Modelos (R²)')
        axes[1].set_ylim(0, 1)
        
        for i, v in enumerate(r2_scores):
            axes[1].text(i, v + 0.01, f'{v:.3f}', ha='center', va='bottom')
        
        plt.suptitle('COMPARACION DE MODELOS DE REGRESION', fontsize=14, fontweight='bold')
        
        # Calcular estadísticas para interpretación
        mejor_modelo = max(resultados.items(), key=lambda x: x[1]['r2_test'])
        peor_modelo = min(resultados.items(), key=lambda x: x[1]['r2_test'])
        
        # Crear interpretación específica
        interpretacion_lineas = ["INTERPRETACIÓN ESPECÍFICA:"]
        interpretacion_lineas.append(f"• Total de modelos comparados: {len(resultados)}")
        interpretacion_lineas.append(f"\nRENDIMIENTO POR MODELO:")
        for nombre, resultado in sorted(resultados.items(), key=lambda x: x[1]['r2_test'], reverse=True):
            calidad = "EXCELENTE" if resultado['r2_test'] > 0.9 else "BUENO" if resultado['r2_test'] > 0.7 else "REGULAR"
            interpretacion_lineas.append(f"  • {nombre}: R² = {resultado['r2_test']:.4f} ({calidad})")
        
        interpretacion_lineas.append(f"\nMEJOR MODELO: {mejor_modelo[0]}")
        interpretacion_lineas.append(f"  R² = {mejor_modelo[1]['r2_test']:.4f} (explica {mejor_modelo[1]['r2_test']*100:.1f}% de la variabilidad)")
        interpretacion_lineas.append(f"  MSE = {mejor_modelo[1]['mse_test']:.2f}")
        
        interpretacion_lineas.append(f"\nPEOR MODELO: {peor_modelo[0]}")
        interpretacion_lineas.append(f"  R² = {peor_modelo[1]['r2_test']:.4f} (explica {peor_modelo[1]['r2_test']*100:.1f}% de la variabilidad)")
        
        diferencia = mejor_modelo[1]['r2_test'] - peor_modelo[1]['r2_test']
        interpretacion_lineas.append(f"\nCONCLUSIÓN: {mejor_modelo[0]} es {diferencia*100:.1f} puntos porcentuales mejor que {peor_modelo[0]}")
        interpretacion_lineas.append(f"  Se recomienda usar {mejor_modelo[0]} para predicciones de importe.")
        
        interpretacion = "\n".join(interpretacion_lineas)
        fig.text(0.5, 0.01, interpretacion, ha='center', fontsize=7,
                bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.8),
                wrap=True)
        
        plt.tight_layout()
        plt.subplots_adjust(bottom=0.18)
        
        # Guardar grafico
        archivo = "resultados/histogramas/comparacion_modelos_regresion.png"
        plt.savefig(archivo, dpi=300, bbox_inches='tight')
        print(f"   Grafico de regresion guardado: {archivo}")
        plt.close()
    
    def crear_grafico_clustering(self):
        """Crear grafico de clustering."""
        if 'cluster_kmeans' not in self.dataset.columns:
            return
        
        # Variables para clustering
        variables_clustering = ['cantidad', 'precio_unitario_detalle', 'importe']
        variables_disponibles = [v for v in variables_clustering if v in self.dataset.columns]
        
        if len(variables_disponibles) < 2:
            return
        
        fig, axes = plt.subplots(1, 2, figsize=(15, 6))
        
        # K-Means con centroides
        scatter = axes[0].scatter(self.dataset[variables_disponibles[0]], 
                                 self.dataset[variables_disponibles[1]], 
                                 c=self.dataset['cluster_kmeans'], 
                                 cmap='viridis', alpha=0.6, s=50)
        axes[0].set_xlabel(variables_disponibles[0])
        axes[0].set_ylabel(variables_disponibles[1])
        axes[0].set_title('K-Means Clustering\n(con Centroides)')
        axes[0].grid(True, alpha=0.3)
        
        # Agregar centroides si están disponibles
        try:
            # Obtener el modelo K-Means del resultado de clustering
            if hasattr(self, 'resultados_clustering') and 'kmeans' in self.resultados_clustering:
                kmeans_model = self.resultados_clustering['kmeans']
                scaler = self.resultados_clustering.get('scaler')
                centroides_normalizados = kmeans_model.cluster_centers_
                
                # Calcular centroides en espacio original (promedio de puntos del cluster)
                # Esto es más interpretable que desnormalizar
                for i in range(len(centroides_normalizados)):
                    cluster_points = self.dataset[self.dataset['cluster_kmeans'] == i]
                    if len(cluster_points) > 0:
                        centroide_x = cluster_points[variables_disponibles[0]].mean()
                        centroide_y = cluster_points[variables_disponibles[1]].mean()
                        axes[0].scatter(centroide_x, centroide_y, 
                                       marker='X', s=400, c='red', 
                                       edgecolors='black', linewidths=3,
                                       label='Centroides' if i == 0 else '',
                                       zorder=10)  # zorder para que aparezcan encima
                if len(centroides_normalizados) > 0:
                    axes[0].legend(loc='best', fontsize=9, framealpha=0.9)
        except Exception as e:
            # Si no hay centroides disponibles, calcular directamente del dataset
            try:
                for i in range(3):  # 3 clusters
                    cluster_points = self.dataset[self.dataset['cluster_kmeans'] == i]
                    if len(cluster_points) > 0:
                        centroide_x = cluster_points[variables_disponibles[0]].mean()
                        centroide_y = cluster_points[variables_disponibles[1]].mean()
                        axes[0].scatter(centroide_x, centroide_y, 
                                       marker='X', s=400, c='red', 
                                       edgecolors='black', linewidths=3,
                                       label='Centroides' if i == 0 else '',
                                       zorder=10)
                axes[0].legend(loc='best', fontsize=9, framealpha=0.9)
            except:
                pass  # Si no se pueden calcular, continuar sin ellos
        
        # DBSCAN
        scatter = axes[1].scatter(self.dataset[variables_disponibles[0]], 
                                 self.dataset[variables_disponibles[1]], 
                                 c=self.dataset['cluster_dbscan'], 
                                 cmap='viridis', alpha=0.6)
        axes[1].set_xlabel(variables_disponibles[0])
        axes[1].set_ylabel(variables_disponibles[1])
        axes[1].set_title('DBSCAN Clustering')
        axes[1].grid(True, alpha=0.3)
        
        plt.suptitle('ANALISIS DE CLUSTERING', fontsize=14, fontweight='bold')
        
        # Calcular estadísticas de clustering para interpretación
        n_clusters_kmeans = len(set(self.dataset['cluster_kmeans']))
        n_clusters_dbscan = len(set(self.dataset['cluster_dbscan'])) - (1 if -1 in self.dataset['cluster_dbscan'].values else 0)
        puntos_ruido_dbscan = (self.dataset['cluster_dbscan'] == -1).sum()
        
        # Tamaño de cada cluster K-Means
        tamanos_kmeans = self.dataset['cluster_kmeans'].value_counts().sort_index()
        
        # Calcular información de centroides
        info_centroides = []
        try:
            if hasattr(self, 'resultados_clustering') and 'kmeans' in self.resultados_clustering:
                kmeans_model = self.resultados_clustering['kmeans']
                variables_clustering = self.resultados_clustering.get('variables_clustering', variables_disponibles)
                
                info_centroides.append(f"\nCENTROIDES (marcados con X roja):")
                for i in range(len(kmeans_model.cluster_centers_)):
                    cluster_points = self.dataset[self.dataset['cluster_kmeans'] == i]
                    if len(cluster_points) > 0:
                        # Calcular centroide en espacio original (promedio de puntos del cluster)
                        centroide_original = {}
                        for var in variables_clustering:
                            if var in cluster_points.columns:
                                centroide_original[var] = cluster_points[var].mean()
                        
                        info_centroides.append(f"  • Cluster {i}:")
                        for var, valor in centroide_original.items():
                            info_centroides.append(f"    - {var}: {valor:.2f}")
        except:
            pass
        
        # Crear interpretación específica
        interpretacion_lineas = ["INTERPRETACIÓN ESPECÍFICA:"]
        interpretacion_lineas.append(f"\nK-MEANS (IZQUIERDA):")
        interpretacion_lineas.append(f"  • Número de clusters: {n_clusters_kmeans}")
        interpretacion_lineas.append(f"  • Distribución de puntos por cluster:")
        for cluster, tamano in tamanos_kmeans.items():
            porcentaje = (tamano / len(self.dataset) * 100)
            interpretacion_lineas.append(f"    - Cluster {cluster}: {tamano} puntos ({porcentaje:.1f}%)")
        
        # Agregar información de centroides
        if info_centroides:
            interpretacion_lineas.extend(info_centroides)
        
        interpretacion_lineas.append(f"\nDBSCAN (DERECHA):")
        interpretacion_lineas.append(f"  • Número de clusters encontrados: {n_clusters_dbscan}")
        interpretacion_lineas.append(f"  • Puntos de ruido (sin cluster): {puntos_ruido_dbscan} ({(puntos_ruido_dbscan/len(self.dataset)*100):.1f}%)")
        
        cluster_mas_grande_kmeans = tamanos_kmeans.idxmax()
        interpretacion_lineas.append(f"\nCONCLUSIÓN:")
        interpretacion_lineas.append(f"  • K-Means creó {n_clusters_kmeans} grupos balanceados")
        interpretacion_lineas.append(f"  • El cluster más grande es el {cluster_mas_grande_kmeans} con {tamanos_kmeans.max()} puntos")
        interpretacion_lineas.append(f"  • DBSCAN identificó {n_clusters_dbscan} grupos naturales")
        interpretacion_lineas.append(f"  • Los centroides (marcados con X roja) representan el 'centro' de cada cluster")
        
        interpretacion = "\n".join(interpretacion_lineas)
        fig.text(0.5, 0.01, interpretacion, ha='center', fontsize=7,
                bbox=dict(boxstyle='round', facecolor='lavender', alpha=0.8),
                wrap=True)
        
        plt.tight_layout()
        plt.subplots_adjust(bottom=0.18)
        
        # Guardar grafico
        archivo = "resultados/histogramas/analisis_clustering.png"
        plt.savefig(archivo, dpi=300, bbox_inches='tight')
        print(f"   Grafico de clustering guardado: {archivo}")
        plt.close()
    
    def crear_grafico_importancia_variables(self):
        """Crear grafico de importancia de variables."""
        if 'importe' not in self.resultados:
            return
        
        # Obtener importancia de variables del Random Forest
        rf_resultado = self.resultados['importe'].get('RandomForest')
        if rf_resultado is None:
            return
        
        modelo_rf = rf_resultado['modelo']
        
        # Obtener importancia de variables
        importancia = modelo_rf.feature_importances_
        nombres_variables = self.X_train.columns
        
        # Crear DataFrame de importancia
        df_importancia = pd.DataFrame({
            'variable': nombres_variables,
            'importancia': importancia
        }).sort_values('importancia', ascending=False)
        
        # Grafico de importancia
        plt.figure(figsize=(12, 8))
        top_variables = df_importancia.head(10)
        
        plt.barh(range(len(top_variables)), top_variables['importancia'], 
                color='lightblue', alpha=0.8)
        plt.yticks(range(len(top_variables)), top_variables['variable'])
        plt.xlabel('Importancia')
        plt.title('Importancia de Variables - Random Forest', fontweight='bold')
        plt.grid(axis='x', alpha=0.3)
        
        # Agregar valores en las barras
        for i, v in enumerate(top_variables['importancia']):
            plt.text(v + 0.001, i, f'{v:.3f}', va='center')
        
        # Crear interpretación específica con valores reales
        interpretacion_lineas = ["INTERPRETACIÓN ESPECÍFICA:"]
        interpretacion_lineas.append(f"• Total de variables analizadas: {len(df_importancia)}")
        interpretacion_lineas.append(f"• Top 10 variables más importantes:\n")
        
        for idx, row in top_variables.iterrows():
            porcentaje = (row['importancia'] / df_importancia['importancia'].sum() * 100)
            interpretacion_lineas.append(f"  {idx+1}. {row['variable']}: {row['importancia']:.4f} ({porcentaje:.1f}% del total)")
        
        variable_mas_importante = top_variables.iloc[0]
        variable_segunda = top_variables.iloc[1] if len(top_variables) > 1 else None
        
        interpretacion_lineas.append(f"\nCONCLUSIÓN:")
        interpretacion_lineas.append(f"  • VARIABLE MÁS IMPORTANTE: {variable_mas_importante['variable']}")
        interpretacion_lineas.append(f"    Importancia: {variable_mas_importante['importancia']:.4f} ({(variable_mas_importante['importancia']/df_importancia['importancia'].sum()*100):.1f}% del total)")
        if variable_segunda is not None:
            ratio = variable_mas_importante['importancia'] / variable_segunda['importancia']
            interpretacion_lineas.append(f"  • Es {ratio:.1f}x más importante que {variable_segunda['variable']}")
        interpretacion_lineas.append(f"  • Las top 3 variables explican {(top_variables.head(3)['importancia'].sum()/df_importancia['importancia'].sum()*100):.1f}% de la importancia total")
        
        interpretacion = "\n".join(interpretacion_lineas)
        plt.figtext(0.5, 0.01, interpretacion, ha='center', fontsize=7,
                   bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8),
                   wrap=True)
        
        plt.tight_layout()
        plt.subplots_adjust(bottom=0.15)
        
        # Guardar grafico
        archivo = "resultados/histogramas/importancia_variables.png"
        plt.savefig(archivo, dpi=300, bbox_inches='tight')
        print(f"   Grafico de importancia guardado: {archivo}")
        plt.close()
    
    def crear_matrices_confusion(self):
        """
        Crear visualizaciones de matrices de confusión para todos los modelos de clasificación.
        
        Genera gráficos de matrices de confusión con interpretaciones detalladas para cada
        modelo de clasificación entrenado, mostrando verdaderos positivos, falsos positivos,
        verdaderos negativos y falsos negativos.
        """
        if 'segmento_cliente' not in self.resultados:
            return
        
        print("\n   Creando matrices de confusión...")
        resultados = self.resultados['segmento_cliente']
        
        # Determinar número de modelos
        n_modelos = len(resultados)
        fig = plt.figure(figsize=(6*n_modelos, 8))
        gs = fig.add_gridspec(2, n_modelos, height_ratios=[3, 1], hspace=0.3)
        
        # Obtener clases únicas del primer resultado
        primer_resultado = list(resultados.values())[0]
        y_test = primer_resultado['y_test']
        if hasattr(y_test, 'unique'):
            clases = sorted(y_test.unique())
        elif hasattr(y_test, 'cat'):
            clases = sorted(y_test.cat.categories)
        else:
            clases = sorted(set(y_test))
        
        # Crear matrices de confusión
        for idx, (nombre_modelo, resultado) in enumerate(resultados.items()):
            cm = resultado['confusion_matrix']
            
            # Subplot para la matriz
            ax = fig.add_subplot(gs[0, idx])
            
            # Crear heatmap de matriz de confusión
            sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                       xticklabels=clases, yticklabels=clases,
                       ax=ax, cbar_kws={'label': 'Cantidad'})
            
            ax.set_xlabel('Predicción', fontsize=11, fontweight='bold')
            ax.set_ylabel('Valor Real', fontsize=11, fontweight='bold')
            ax.set_title(f'{nombre_modelo}\nMatriz de Confusión', 
                               fontsize=12, fontweight='bold', pad=10)
            
            # Calcular métricas adicionales
            total = cm.sum()
            correctos = cm.trace()  # Suma de la diagonal
            accuracy = correctos / total if total > 0 else 0
            
            # Agregar texto con métricas
            texto_metricas = f'Accuracy: {accuracy:.2%}\nTotal: {total}'
            ax.text(0.5, -0.15, texto_metricas, 
                          transform=ax.transAxes,
                          ha='center', fontsize=9,
                          bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
        
        # Agregar interpretación específica con rangos de importe
        ax_interpretacion = fig.add_subplot(gs[1, :])
        ax_interpretacion.axis('off')
        
        # Generar interpretación con datos específicos
        interpretacion = self._generar_interpretacion_matrices_confusion(resultados, clases)
        
        ax_interpretacion.text(0.05, 0.95, interpretacion, transform=ax_interpretacion.transAxes,
                              fontsize=8, verticalalignment='top', family='monospace',
                              bbox=dict(boxstyle='round', facecolor='lavender', alpha=0.9))
        
        plt.suptitle('MATRICES DE CONFUSIÓN - MODELOS DE CLASIFICACIÓN', 
                    fontsize=14, fontweight='bold', y=0.98)
        
        # Guardar gráfico
        archivo = "resultados/histogramas/matrices_confusion.png"
        plt.savefig(archivo, dpi=300, bbox_inches='tight')
        plt.close()
        print(f"   Matrices de confusión guardadas: {archivo}")
        
        # Crear gráfico individual más detallado para el mejor modelo
        mejor_modelo = max(resultados.items(), 
                          key=lambda x: x[1]['accuracy_test'])
        self._crear_matriz_confusion_detallada(mejor_modelo[0], mejor_modelo[1], clases)
    
    def _crear_matriz_confusion_detallada(self, nombre_modelo, resultado, clases):
        """
        Crear matriz de confusión detallada con interpretación completa.
        
        Args:
            nombre_modelo (str): Nombre del modelo
            resultado (dict): Resultados del modelo
            clases (list): Lista de clases
        """
        cm = resultado['confusion_matrix']
        report = resultado['classification_report']
        
        # Crear figura con dos subplots
        fig = plt.figure(figsize=(16, 8))
        gs = fig.add_gridspec(2, 2, hspace=0.3, wspace=0.3)
        
        # Subplot 1: Matriz de confusión con valores absolutos
        ax1 = fig.add_subplot(gs[0, 0])
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                   xticklabels=clases, yticklabels=clases,
                   ax=ax1, cbar_kws={'label': 'Cantidad'})
        ax1.set_xlabel('Predicción', fontsize=11, fontweight='bold')
        ax1.set_ylabel('Valor Real', fontsize=11, fontweight='bold')
        ax1.set_title(f'{nombre_modelo} - Matriz de Confusión\n(Valores Absolutos)', 
                     fontsize=12, fontweight='bold', pad=10)
        
        # Subplot 2: Matriz de confusión normalizada (porcentajes)
        ax2 = fig.add_subplot(gs[0, 1])
        cm_percent = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis] * 100
        sns.heatmap(cm_percent, annot=True, fmt='.1f', cmap='Oranges', 
                   xticklabels=clases, yticklabels=clases,
                   ax=ax2, cbar_kws={'label': 'Porcentaje (%)'})
        ax2.set_xlabel('Predicción', fontsize=11, fontweight='bold')
        ax2.set_ylabel('Valor Real', fontsize=11, fontweight='bold')
        ax2.set_title(f'{nombre_modelo} - Matriz de Confusión\n(Valores Normalizados %)', 
                     fontsize=12, fontweight='bold', pad=10)
        
        # Subplot 3: Métricas por clase
        ax3 = fig.add_subplot(gs[1, :])
        ax3.axis('off')
        
        # Crear interpretación detallada
        interpretacion = self._generar_interpretacion_confusion(cm, clases, report, resultado)
        
        ax3.text(0.05, 0.95, interpretacion, transform=ax3.transAxes,
                fontsize=9, verticalalignment='top', family='monospace',
                bbox=dict(boxstyle='round', facecolor='lavender', alpha=0.9))
        
        plt.suptitle(f'ANÁLISIS DETALLADO DE MATRIZ DE CONFUSIÓN - {nombre_modelo.upper()}', 
                    fontsize=14, fontweight='bold', y=0.98)
        
        # Guardar gráfico detallado
        archivo_detallado = f"resultados/histogramas/matriz_confusion_{nombre_modelo.lower()}_detallada.png"
        plt.savefig(archivo_detallado, dpi=300, bbox_inches='tight')
        plt.close()
        print(f"   Matriz de confusión detallada guardada: {archivo_detallado}")
    
    def _generar_interpretacion_matrices_confusion(self, resultados, clases):
        """
        Generar interpretación específica para las matrices de confusión con datos del proyecto.
        
        Args:
            resultados: Diccionario con resultados de todos los modelos
            clases: Lista de clases (segmentos)
        
        Returns:
            str: Texto de interpretación con datos específicos
        """
        lineas = ["INTERPRETACIÓN ESPECÍFICA - PROYECTO AURELION"]
        lineas.append("=" * 70)
        
        # Agregar información de segmentos con rangos específicos
        if hasattr(self, 'rangos_segmentos') and self.rangos_segmentos:
            lineas.append("\nDEFINICIÓN DE SEGMENTOS (basados en importe promedio por cliente):")
            for segmento in clases:
                if segmento in self.rangos_segmentos:
                    rango = self.rangos_segmentos[segmento]
                    lineas.append(f"\n  • SEGMENTO {segmento.upper()}:")
                    lineas.append(f"    - Rango de importe promedio: ${rango['min']:,.2f} - ${rango['max']:,.2f}")
                    lineas.append(f"    - Importe promedio: ${rango['promedio']:,.2f}")
                    lineas.append(f"    - Importe mediano: ${rango['mediana']:,.2f}")
                    lineas.append(f"    - Cantidad de clientes: {rango['cantidad_clientes']}")
        else:
            lineas.append("\nDEFINICIÓN DE SEGMENTOS:")
            lineas.append("  • BAJO: Clientes con importe promedio en el tercio inferior")
            lineas.append("  • MEDIO: Clientes con importe promedio en el tercio medio")
            lineas.append("  • ALTO: Clientes con importe promedio en el tercio superior")
        
        # Agregar resultados por modelo
        lineas.append("\n" + "=" * 70)
        lineas.append("RESULTADOS POR MODELO:")
        
        for nombre_modelo, resultado in resultados.items():
            cm = resultado['confusion_matrix']
            total = cm.sum()
            correctos = cm.trace()
            accuracy = correctos / total if total > 0 else 0
            
            lineas.append(f"\n  {nombre_modelo}:")
            lineas.append(f"    • Accuracy: {accuracy:.2%} ({correctos}/{total} predicciones correctas)")
            
            # Desglose por clase
            for i, clase in enumerate(clases):
                tp = cm[i, i] if i < len(clases) else 0
                total_clase = cm[i, :].sum() if i < len(clases) else 0
                if total_clase > 0:
                    porcentaje = (tp / total_clase) * 100
                    lineas.append(f"    • {clase}: {tp}/{total_clase} correctas ({porcentaje:.1f}%)")
        
        # Mejor modelo
        mejor_modelo = max(resultados.items(), key=lambda x: x[1]['accuracy_test'])
        mejor_accuracy = mejor_modelo[1]['accuracy_test']
        lineas.append(f"\n  MEJOR MODELO: {mejor_modelo[0]} con {mejor_accuracy:.2%} de accuracy")
        
        return "\n".join(lineas)
    
    def _generar_interpretacion_confusion(self, cm, clases, report, resultado):
        """
        Generar interpretación detallada de la matriz de confusión.
        
        Args:
            cm: Matriz de confusión
            clases: Lista de clases
            report: Classification report
            resultado: Resultados del modelo
        
        Returns:
            str: Texto de interpretación
        """
        total = cm.sum()
        correctos = cm.trace()
        accuracy = correctos / total if total > 0 else 0
        
        lineas = ["INTERPRETACIÓN ESPECÍFICA DE LA MATRIZ DE CONFUSIÓN - PROYECTO AURELION"]
        lineas.append("=" * 70)
        
        # Agregar información de segmentos con rangos específicos
        if hasattr(self, 'rangos_segmentos') and self.rangos_segmentos:
            lineas.append("\nDEFINICIÓN DE SEGMENTOS (basados en importe promedio por cliente):")
            for segmento in clases:
                if segmento in self.rangos_segmentos:
                    rango = self.rangos_segmentos[segmento]
                    lineas.append(f"\n  • SEGMENTO {segmento.upper()}:")
                    lineas.append(f"    - Rango de importe promedio: ${rango['min']:,.2f} - ${rango['max']:,.2f}")
                    lineas.append(f"    - Importe promedio: ${rango['promedio']:,.2f}")
                    lineas.append(f"    - Importe mediano: ${rango['mediana']:,.2f}")
                    lineas.append(f"    - Cantidad de clientes: {rango['cantidad_clientes']}")
        
        lineas.append("\n" + "=" * 70)
        lineas.append(f"MÉTRICAS GENERALES:")
        lineas.append(f"  • Accuracy (Precisión Global): {accuracy:.2%}")
        lineas.append(f"  • Total de predicciones: {total}")
        lineas.append(f"  • Predicciones correctas: {correctos}")
        lineas.append(f"  • Predicciones incorrectas: {total - correctos}")
        
        lineas.append(f"\nDESGLOSE POR CLASE:")
        for i, clase in enumerate(clases):
            tp = cm[i, i]  # Verdaderos positivos
            fn = cm[i, :].sum() - tp  # Falsos negativos
            fp = cm[:, i].sum() - tp  # Falsos positivos
            tn = total - tp - fn - fp  # Verdaderos negativos
            
            precision = tp / (tp + fp) if (tp + fp) > 0 else 0
            recall = tp / (tp + fn) if (tp + fn) > 0 else 0
            f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
            
            lineas.append(f"\n  Clase '{clase}':")
            lineas.append(f"    • Verdaderos Positivos (TP): {tp}")
            lineas.append(f"    • Falsos Positivos (FP): {fp}")
            lineas.append(f"    • Falsos Negativos (FN): {fn}")
            lineas.append(f"    • Verdaderos Negativos (TN): {tn}")
            lineas.append(f"    • Precision: {precision:.2%}")
            lineas.append(f"    • Recall (Sensibilidad): {recall:.2%}")
            lineas.append(f"    • F1-Score: {f1:.2%}")
        
        lineas.append(f"\n¿QUÉ SIGNIFICA ESTO?")
        lineas.append(f"  • Verdaderos Positivos: Predicciones correctas de la clase")
        lineas.append(f"  • Falsos Positivos: Predicciones incorrectas (dijo que era la clase pero no lo era)")
        lineas.append(f"  • Falsos Negativos: No predijo la clase cuando debería haberlo hecho")
        lineas.append(f"  • Accuracy: Porcentaje total de predicciones correctas")
        
        if accuracy > 0.85:
            lineas.append(f"\n✅ El modelo tiene un rendimiento EXCELENTE (accuracy > 85%)")
        elif accuracy > 0.70:
            lineas.append(f"\n✅ El modelo tiene un rendimiento BUENO (accuracy > 70%)")
        else:
            lineas.append(f"\n⚠️  El modelo puede necesitar mejoras (accuracy < 70%)")
        
        return "\n".join(lineas)
    
    def guardar_resultados_ml(self):
        """Guardar resultados de ML."""
        print(f"\nGUARDANDO RESULTADOS DE ML")
        print("-" * 35)
        
        try:
            archivo = "resultados/estadisticas/resultados_ml.txt"
            with open(archivo, 'w', encoding='utf-8') as f:
                f.write("RESULTADOS DE MACHINE LEARNING - PROYECTO AURELION\n")
                f.write("Proyecto desarrollado como parte del curso AI Fundamentals - Guayerd - IBM Skills Build\n")
                f.write("=" * 80 + "\n\n")
                
                # Resultados de regresion
                if 'importe' in self.resultados:
                    f.write("MODELOS DE REGRESION - PREDICCION DE IMPORTE:\n")
                    f.write("-" * 50 + "\n")
                    for nombre, resultado in self.resultados['importe'].items():
                        f.write(f"{nombre}:\n")
                        f.write(f"  R² Entrenamiento: {resultado['r2_train']:.4f}\n")
                        f.write(f"  R² Prueba: {resultado['r2_test']:.4f}\n")
                        f.write(f"  CV R²: {resultado['cv_mean']:.4f} (+/- {resultado['cv_std']*2:.4f})\n")
                        f.write(f"  MSE Prueba: {resultado['mse_test']:.4f}\n\n")
                
                # Resultados de clustering
                if 'cluster_kmeans' in self.dataset.columns:
                    f.write("MODELOS DE CLUSTERING:\n")
                    f.write("-" * 30 + "\n")
                    f.write(f"K-Means: {len(set(self.dataset['cluster_kmeans']))} clusters\n")
                    f.write(f"DBSCAN: {len(set(self.dataset['cluster_dbscan']))} clusters\n")
            
            print(f"   Resultados guardados: {archivo}")
            
        except Exception as e:
            print(f"   Error al guardar resultados: {e}")
    
    def ejecutar_ml_completo(self):
        """Ejecutar pipeline completo de ML."""
        print("MODELOS DE MACHINE LEARNING - PROYECTO AURELION")
        print("Proyecto desarrollado como parte del curso AI Fundamentals - Guayerd - IBM Skills Build")
        print("=" * 80)
        
        # Cargar dataset
        if not self.cargar_dataset():
            return False
        
        # Entrenar modelos de regresion
        self.entrenar_modelos_regresion('importe')
        
        # Entrenar modelos de clasificacion
        self.entrenar_modelos_clasificacion('segmento_cliente')
        
        # Entrenar modelos de clustering
        self.entrenar_clustering()
        
        # Crear visualizaciones
        self.crear_visualizaciones_modelos()
        
        # Guardar resultados
        self.guardar_resultados_ml()
        
        print(f"\n[OK] Modelos de ML implementados exitosamente!")
        print(f"[INFO] Resultados guardados en: resultados/estadisticas/")
        print(f"[INFO] Graficos guardados en: resultados/histogramas/")
        
        # Generar automáticamente VARIABLES_Y_CENTROIDES.md
        print(f"\n📝 Generando VARIABLES_Y_CENTROIDES.md automáticamente...")
        try:
            import sys
            import os
            ruta_script = os.path.join(os.path.dirname(__file__), '11_generar_variables_centroides.py')
            if os.path.exists(ruta_script):
                import subprocess
                subprocess.run([sys.executable, ruta_script], check=False)
            else:
                print(f"   ⚠️ Script 11_generar_variables_centroides.py no encontrado")
        except Exception as e:
            print(f"   ⚠️ No se pudo generar VARIABLES_Y_CENTROIDES.md automáticamente: {e}")
            print(f"   💡 Puedes ejecutarlo manualmente: python 11_generar_variables_centroides.py")
        
        return True

def main():
    """Funcion principal de ML."""
    ml = ModelosML()
    ml.ejecutar_ml_completo()

if __name__ == "__main__":
    main()
