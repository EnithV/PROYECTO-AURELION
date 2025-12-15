#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
<!--
# EVALUACION MODELOS ML - SPRINT_3
**Autor:** Enith Gicela Vargas Vargas  
**Camada:** 1  
**Grupo:** 11  
**Fecha:** 2025-11-11  
**Curso:** AI Fundamentals - Guayerd - IBM Skills Build  
**Sprint:** 3 - Machine Learning Fundamentals  
**Módulo:** Modelado - Evaluación de Modelos  
-->

EVALUACION DE MODELOS ML - PROYECTO AURELION SPRINT_3
======================================================

Script para evaluar modelos de Machine Learning, incluyendo:
- Carga de modelos entrenados
- Evaluación detallada
- Visualización de resultados
- Reporte de rendimiento
"""

import pandas as pd          # Librería para manipulación de datos
import numpy as np           # Librería para cálculos numéricos
import matplotlib.pyplot as plt  # Librería para visualizaciones
import seaborn as sns       # Librería para gráficos estadísticos
from sklearn.metrics import (  # Métricas de evaluación
    mean_squared_error, r2_score, mean_absolute_error,
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report
)
import pickle               # Para cargar modelos
import os                   # Para manejo de archivos
import warnings             # Módulo para controlar avisos
warnings.filterwarnings('ignore')

class ModelEvaluation:
    """
    Clase para evaluar modelos de Machine Learning.
    
    Funcionalidades:
    - Carga de modelos entrenados
    - Evaluación detallada
    - Visualización de resultados
    - Reporte de rendimiento
    """
    
    def __init__(self):
        """Inicializar el evaluador de modelos."""
        print("EVALUACION DE MODELOS DE MACHINE LEARNING")
        print("Grupo 11 - Camada 1 | Enith Gicela Vargas Vargas")
        print("=" * 60)
        
    def load_data(self):
        """Cargar datos de prueba."""
        print("\nCARGANDO DATOS DE PRUEBA")
        print("-" * 50)
        
        try:
            X_test = pd.read_csv("../resultados/X_test.csv")
            y_test = pd.read_csv("../resultados/y_test.csv")
            
            # Convertir y a series si es necesario
            if y_test.shape[1] == 1:
                y_test = y_test.iloc[:, 0]
            
            print(f"✓ Datos de prueba: {X_test.shape}")
            print(f"✓ Target de prueba: {y_test.shape}")
            
            return X_test, y_test
            
        except FileNotFoundError as e:
            print(f"[ERROR] Archivos no encontrados: {e}")
            return None, None
        except Exception as e:
            print(f"[ERROR] Error al cargar datos: {e}")
            return None, None
    
    def load_models(self):
        """Cargar modelos entrenados."""
        print("\nCARGANDO MODELOS ENTRENADOS")
        print("-" * 50)
        
        models = {}
        model_dir = "../resultados/modelos"
        
        if not os.path.exists(model_dir):
            print("[ERROR] Directorio de modelos no encontrado")
            return None
        
        # Listar archivos de modelos
        model_files = [f for f in os.listdir(model_dir) if f.endswith('.pkl') and f != 'mejor_modelo.pkl']
        
        if not model_files:
            print("[ERROR] No se encontraron modelos entrenados")
            return None
        
        # Cargar cada modelo
        for model_file in model_files:
            model_name = model_file.replace('.pkl', '').replace('_', ' ').title()
            model_path = os.path.join(model_dir, model_file)
            
            try:
                with open(model_path, 'rb') as f:
                    models[model_name] = pickle.load(f)
                print(f"✓ {model_name} cargado")
            except Exception as e:
                print(f"[ERROR] Error al cargar {model_name}: {e}")
        
        print(f"✓ Total de modelos cargados: {len(models)}")
        return models
    
    def evaluate_regression(self, models, X_test, y_test):
        """Evaluar modelos de regresión."""
        print("\nEVALUACION DE MODELOS DE REGRESION")
        print("-" * 50)
        
        results = {}
        
        for name, model in models.items():
            print(f"\nEvaluando {name}...")
            
            # Predicciones
            y_pred = model.predict(X_test)
            
            # Métricas de regresión
            mse = mean_squared_error(y_test, y_pred)
            rmse = np.sqrt(mse)
            mae = mean_absolute_error(y_test, y_pred)
            r2 = r2_score(y_test, y_pred)
            
            # Métricas adicionales
            mape = np.mean(np.abs((y_test - y_pred) / y_test)) * 100
            
            results[name] = {
                'MSE': mse,
                'RMSE': rmse,
                'MAE': mae,
                'R2': r2,
                'MAPE': mape,
                'predictions': y_pred
            }
            
            print(f"  ✓ MSE: {mse:.4f}")
            print(f"  ✓ RMSE: {rmse:.4f}")
            print(f"  ✓ MAE: {mae:.4f}")
            print(f"  ✓ R²: {r2:.4f}")
            print(f"  ✓ MAPE: {mape:.2f}%")
        
        return results
    
    def evaluate_classification(self, models, X_test, y_test):
        """Evaluar modelos de clasificación."""
        print("\nEVALUACION DE MODELOS DE CLASIFICACION")
        print("-" * 50)
        
        results = {}
        
        for name, model in models.items():
            print(f"\nEvaluando {name}...")
            
            # Predicciones
            y_pred = model.predict(X_test)
            
            # Métricas de clasificación
            accuracy = accuracy_score(y_test, y_pred)
            precision = precision_score(y_test, y_pred, average='weighted')
            recall = recall_score(y_test, y_pred, average='weighted')
            f1 = f1_score(y_test, y_pred, average='weighted')
            
            results[name] = {
                'Accuracy': accuracy,
                'Precision': precision,
                'Recall': recall,
                'F1-Score': f1,
                'predictions': y_pred
            }
            
            print(f"  ✓ Accuracy: {accuracy:.4f}")
            print(f"  ✓ Precision: {precision:.4f}")
            print(f"  ✓ Recall: {recall:.4f}")
            print(f"  ✓ F1-Score: {f1:.4f}")
        
        return results
    
    def create_comparison_table(self, results, problem_type):
        """Crear tabla de comparación de modelos."""
        print(f"\nTABLA DE COMPARACION DE MODELOS")
        print("-" * 50)
        
        # Crear DataFrame de resultados
        comparison_data = []
        for name, metrics in results.items():
            row = {'Modelo': name}
            row.update({k: v for k, v in metrics.items() if k != 'predictions'})
            comparison_data.append(row)
        
        comparison_df = pd.DataFrame(comparison_data)
        
        # Ordenar por métrica principal
        if problem_type == 'regression':
            comparison_df = comparison_df.sort_values('R2', ascending=False)
            print("Ranking por R² Score:")
        else:
            comparison_df = comparison_df.sort_values('Accuracy', ascending=False)
            print("Ranking por Accuracy:")
        
        print(comparison_df.round(4))
        
        # Mejor modelo
        best_model = comparison_df.iloc[0]['Modelo']
        print(f"\n✓ Mejor modelo: {best_model}")
        
        return comparison_df, best_model
    
    def visualize_results(self, results, y_test, problem_type):
        """Visualizar resultados de evaluación."""
        print(f"\nVISUALIZACION DE RESULTADOS")
        print("-" * 50)
        
        # Crear directorio de resultados si no existe
        os.makedirs("../resultados/metricas", exist_ok=True)
        
        if problem_type == 'regression':
            # Gráfico de predicciones vs valores reales
            fig, axes = plt.subplots(2, 2, figsize=(15, 12))
            axes = axes.ravel()
            
            for i, (name, metrics) in enumerate(results.items()):
                if i >= 4:  # Máximo 4 modelos
                    break
                
                y_pred = metrics['predictions']
                
                # Scatter plot
                axes[i].scatter(y_test, y_pred, alpha=0.6)
                axes[i].plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
                axes[i].set_xlabel('Valores Reales')
                axes[i].set_ylabel('Predicciones')
                axes[i].set_title(f'{name}\nR² = {metrics["R2"]:.4f}')
                axes[i].grid(True, alpha=0.3)
            
            # Calcular estadísticas para interpretación específica
            mejor_modelo = max(results.items(), key=lambda x: x[1]['R2'])
            peor_modelo = min(results.items(), key=lambda x: x[1]['R2'])
            
            # Calcular distancias promedio de los puntos a la línea perfecta
            distancias_por_modelo = {}
            for name, metrics in results.items():
                y_pred = metrics['predictions']
                # Calcular distancia promedio a la línea perfecta
                distancias = np.abs(y_test - y_pred)
                distancias_por_modelo[name] = {
                    'distancia_promedio': distancias.mean(),
                    'distancia_max': distancias.max(),
                    'r2': metrics['R2'],
                    'mse': metrics['MSE']
                }
            
            # Crear interpretación específica con valores reales
            interpretacion_lineas = ["INTERPRETACIÓN ESPECÍFICA:"]
            interpretacion_lineas.append(f"• Total de modelos evaluados: {len(results)}")
            interpretacion_lineas.append(f"\nRENDIMIENTO POR MODELO:")
            for name, dist_info in sorted(distancias_por_modelo.items(), key=lambda x: x[1]['r2'], reverse=True):
                calidad = "EXCELENTE" if dist_info['r2'] > 0.9 else "BUENO" if dist_info['r2'] > 0.7 else "REGULAR" if dist_info['r2'] > 0.5 else "POBRE"
                interpretacion_lineas.append(f"  • {name}:")
                interpretacion_lineas.append(f"    - R² = {dist_info['r2']:.4f} ({calidad}) - Explica {dist_info['r2']*100:.1f}% de la variabilidad")
                interpretacion_lineas.append(f"    - Error promedio: {dist_info['distancia_promedio']:.2f} unidades")
                interpretacion_lineas.append(f"    - Error máximo: {dist_info['distancia_max']:.2f} unidades")
            
            interpretacion_lineas.append(f"\nMEJOR MODELO: {mejor_modelo[0]}")
            interpretacion_lineas.append(f"  R² = {mejor_modelo[1]['R2']:.4f} (explica {mejor_modelo[1]['R2']*100:.1f}% de la variabilidad)")
            interpretacion_lineas.append(f"  MSE = {mejor_modelo[1]['MSE']:.2f}")
            interpretacion_lineas.append(f"  Distancia promedio a línea perfecta: {distancias_por_modelo[mejor_modelo[0]]['distancia_promedio']:.2f}")
            
            interpretacion_lineas.append(f"\nPEOR MODELO: {peor_modelo[0]}")
            interpretacion_lineas.append(f"  R² = {peor_modelo[1]['R2']:.4f} (explica {peor_modelo[1]['R2']*100:.1f}% de la variabilidad)")
            
            diferencia = mejor_modelo[1]['R2'] - peor_modelo[1]['R2']
            interpretacion_lineas.append(f"\nCONCLUSIÓN: {mejor_modelo[0]} es {diferencia*100:.1f} puntos porcentuales mejor que {peor_modelo[0]}")
            interpretacion_lineas.append(f"  Se recomienda usar {mejor_modelo[0]} para predicciones de importe.")
            
            interpretacion = "\n".join(interpretacion_lineas)
            fig.text(0.5, 0.01, interpretacion, ha='center', fontsize=7,
                    bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8),
                    wrap=True)
            
            plt.tight_layout()
            plt.subplots_adjust(bottom=0.25)
            plt.savefig("../resultados/metricas/predicciones_vs_reales.png", dpi=300, bbox_inches='tight')
            plt.close()
            
            print("✓ Gráfico de predicciones vs valores reales guardado")
        
        else:  # classification
            # Matriz de confusión para el mejor modelo
            best_model_name = max(results.keys(), key=lambda x: results[x]['Accuracy'])
            y_pred = results[best_model_name]['predictions']
            
            cm = confusion_matrix(y_test, y_pred)
            
            plt.figure(figsize=(8, 6))
            sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
            plt.title(f'Matriz de Confusión - {best_model_name}')
            plt.xlabel('Predicciones')
            plt.ylabel('Valores Reales')
            
            # Calcular estadísticas para interpretación específica
            total_casos = cm.sum()
            predicciones_correctas = np.trace(cm)
            predicciones_incorrectas = total_casos - predicciones_correctas
            precision = predicciones_correctas / total_casos * 100
            
            # Encontrar la clase con más aciertos y más errores
            aciertos_por_clase = np.diag(cm)
            clase_mejor = np.argmax(aciertos_por_clase)
            clase_peor = np.argmin(aciertos_por_clase)
            
            # Calcular errores por clase
            errores_por_clase = cm.sum(axis=1) - aciertos_por_clase
            
            # Crear interpretación específica con valores reales
            interpretacion_lineas = ["INTERPRETACIÓN ESPECÍFICA:"]
            interpretacion_lineas.append(f"• Modelo evaluado: {best_model_name}")
            interpretacion_lineas.append(f"• Total de casos analizados: {total_casos}")
            interpretacion_lineas.append(f"• PREDICCIONES CORRECTAS: {predicciones_correctas} ({precision:.1f}% del total)")
            interpretacion_lineas.append(f"• PREDICCIONES INCORRECTAS: {predicciones_incorrectas} ({100-precision:.1f}% del total)")
            interpretacion_lineas.append(f"\nDETALLE POR CLASE:")
            for i in range(len(cm)):
                aciertos = aciertos_por_clase[i]
                errores = errores_por_clase[i]
                total_clase = aciertos + errores
                precision_clase = (aciertos / total_clase * 100) if total_clase > 0 else 0
                interpretacion_lineas.append(f"  • Clase {i}: {aciertos} correctas, {errores} incorrectas ({precision_clase:.1f}% precisión)")
            
            interpretacion_lineas.append(f"\nMEJOR CLASE: Clase {clase_mejor} con {aciertos_por_clase[clase_mejor]} aciertos")
            interpretacion_lineas.append(f"PEOR CLASE: Clase {clase_peor} con {aciertos_por_clase[clase_peor]} aciertos")
            
            calidad = "EXCELENTE" if precision > 90 else "BUENO" if precision > 80 else "REGULAR" if precision > 70 else "MEJORABLE"
            interpretacion_lineas.append(f"\nCONCLUSIÓN: El modelo tiene un rendimiento {calidad} ({precision:.1f}% de precisión)")
            if precision < 80:
                interpretacion_lineas.append(f"  Se recomienda mejorar el modelo, especialmente para la Clase {clase_peor}")
            
            interpretacion = "\n".join(interpretacion_lineas)
            plt.figtext(0.5, 0.01, interpretacion, ha='center', fontsize=7,
                       bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.8),
                       wrap=True)
            
            plt.tight_layout()
            plt.subplots_adjust(bottom=0.25)
            plt.savefig("../resultados/metricas/matriz_confusion.png", dpi=300, bbox_inches='tight')
            plt.close()
            
            print(f"✓ Matriz de confusión de {best_model_name} guardada")
    
    def generate_report(self, comparison_df, best_model, problem_type):
        """Generar reporte de evaluación."""
        print(f"\nGENERANDO REPORTE DE EVALUACION")
        print("-" * 50)
        
        report_path = "../resultados/metricas/reporte_evaluacion.txt"
        
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write("REPORTE DE EVALUACION DE MODELOS ML\n")
            f.write("=" * 50 + "\n")
            f.write(f"Fecha: {pd.Timestamp.now()}\n")
            f.write(f"Tipo de problema: {problem_type.upper()}\n")
            f.write(f"Mejor modelo: {best_model}\n\n")
            
            f.write("RESULTADOS DETALLADOS:\n")
            f.write("-" * 30 + "\n")
            f.write(comparison_df.to_string(index=False))
            f.write("\n\n")
            
            f.write("INTERPRETACION:\n")
            f.write("-" * 15 + "\n")
            
            if problem_type == 'regression':
                best_r2 = comparison_df.iloc[0]['R2']
                f.write(f"- R² Score del mejor modelo: {best_r2:.4f}\n")
                if best_r2 > 0.8:
                    f.write("- Excelente capacidad predictiva\n")
                elif best_r2 > 0.6:
                    f.write("- Buena capacidad predictiva\n")
                else:
                    f.write("- Capacidad predictiva limitada\n")
            else:
                best_acc = comparison_df.iloc[0]['Accuracy']
                f.write(f"- Accuracy del mejor modelo: {best_acc:.4f}\n")
                if best_acc > 0.9:
                    f.write("- Excelente rendimiento\n")
                elif best_acc > 0.8:
                    f.write("- Buen rendimiento\n")
                else:
                    f.write("- Rendimiento mejorable\n")
        
        print(f"✓ Reporte guardado en {report_path}")
    
    def execute(self):
        """Ejecutar proceso completo de evaluación."""
        # 1. Cargar datos de prueba
        X_test, y_test = self.load_data()
        
        if X_test is None:
            print("[ERROR] No se pudieron cargar los datos")
            return
        
        # 2. Cargar modelos
        models = self.load_models()
        
        if models is None:
            print("[ERROR] No se pudieron cargar los modelos")
            return
        
        # 3. Determinar tipo de problema
        unique_values = len(np.unique(y_test))
        problem_type = 'classification' if unique_values <= 10 else 'regression'
        
        print(f"\nTipo de problema detectado: {problem_type.upper()}")
        
        # 4. Evaluar modelos
        if problem_type == 'regression':
            results = self.evaluate_regression(models, X_test, y_test)
        else:
            results = self.evaluate_classification(models, X_test, y_test)
        
        # 5. Crear tabla de comparación
        comparison_df, best_model = self.create_comparison_table(results, problem_type)
        
        # 6. Visualizar resultados
        self.visualize_results(results, y_test, problem_type)
        
        # 7. Generar reporte
        self.generate_report(comparison_df, best_model, problem_type)
        
        print(f"\n[OK] Evaluación de modelos completada!")
        print(f"✓ Mejor modelo: {best_model}")

def main():
    """Función principal del módulo."""
    evaluador = ModelEvaluation()
    evaluador.execute()

if __name__ == "__main__":
    main()
