#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
<!--
# VISUALIZADOR AUTOMATICO - SPRINT_3
**Autor:** Enith Gicela Vargas Vargas  
**Camada:** 1  
**Grupo:** 11  
**Fecha:** 2025-11-11  
**Curso:** AI Fundamentals - Guayerd - IBM Skills Build  
**Sprint:** 3 - Machine Learning Fundamentals  
**Módulo:** Visualizador Automático  
-->

VISUALIZADOR AUTOMATICO - PROYECTO AURELION SPRINT_3
====================================================

Módulo para visualización automática de gráficos y datos.
"""

import os               # Módulo del sistema operativo
import pandas as pd     # Módulo para manipulación de datos
import matplotlib.pyplot as plt  # Módulo para gráficos
import subprocess       # Módulo para ejecutar comandos del sistema
from pathlib import Path  # Módulo para manejo de rutas

class VisualizadorAutomatico:
    """
    Clase para visualización automática de gráficos y datos.
    
    Funcionalidades:
    - Mostrar gráficos automáticamente
    - Mostrar tablas de datos
    - Sub-opciones para selección
    - Apertura automática de archivos
    """
    
    def __init__(self):
        """Inicializar el visualizador."""
        # Manejar el caso cuando se ejecuta con exec() donde __file__ no está definido
        try:
            base_path = Path(__file__).parent
        except NameError:
            base_path = Path(os.getcwd())
            if not (base_path / "visualizador_automatico.py").exists():
                posibles = [
                    base_path / "Demo",
                    base_path.parent / "Demo",
                    base_path.parent.parent / "Enith Gicela Vargas Vargas - Proyecto Aurelion" / "Demo",
                ]
                for p in posibles:
                    if p.exists() and (p / "visualizador_automatico.py").exists():
                        base_path = p
                        break
        
        self.resultados_dir = base_path.parent / "resultados"
        self.metricas_dir = self.resultados_dir / "metricas"
        
    def mostrar_graficos(self):
        """Mostrar gráficos con sub-opciones."""
        print("\nVISUALIZACION DE GRAFICOS")
        print("=" * 50)
        
        if not self.metricas_dir.exists():
            print("Directorio de métricas no encontrado.")
            print("Ejecuta primero la evaluación de modelos.")
            return
        
        # Buscar archivos de imagen
        archivos_imagen = []
        for ext in ['.png', '.jpg', '.jpeg', '.svg', '.pdf']:
            archivos_imagen.extend(list(self.metricas_dir.glob(f"*{ext}")))
        
        if not archivos_imagen:
            print("No se encontraron gráficos generados.")
            print("Ejecuta primero la evaluación de modelos.")
            return
        
        print(f"Gráficos disponibles ({len(archivos_imagen)}):")
        for i, archivo in enumerate(archivos_imagen, 1):
            tamaño = archivo.stat().st_size
            print(f"{i}. {archivo.name} ({tamaño} bytes)")
        
        print(f"\n{len(archivos_imagen) + 1}. Abrir carpeta de gráficos")
        print(f"{len(archivos_imagen) + 2}. Volver al menú principal")
        
        try:
            opcion = input(f"\nSelecciona un gráfico (1-{len(archivos_imagen) + 2}): ").strip()
            
            if opcion.isdigit():
                opcion_num = int(opcion)
                
                if 1 <= opcion_num <= len(archivos_imagen):
                    # Mostrar gráfico seleccionado
                    archivo_seleccionado = archivos_imagen[opcion_num - 1]
                    self._abrir_grafico(archivo_seleccionado)
                    
                elif opcion_num == len(archivos_imagen) + 1:
                    # Abrir carpeta
                    self._abrir_carpeta(self.metricas_dir)
                    
                elif opcion_num == len(archivos_imagen) + 2:
                    # Volver
                    return
                else:
                    print("Opción inválida.")
            else:
                print("Opción inválida.")
                
        except KeyboardInterrupt:
            print("\nOperación cancelada.")
        except Exception as e:
            print(f"Error: {e}")
    
    def mostrar_datos(self):
        """Mostrar datos con sub-opciones."""
        print("\nVISUALIZACION DE DATOS")
        print("=" * 50)
        
        if not self.resultados_dir.exists():
            print("Directorio de resultados no encontrado.")
            print("Ejecuta primero la preparación de datos.")
            return
        
        # Buscar archivos CSV
        archivos_csv = list(self.resultados_dir.glob("*.csv"))
        
        if not archivos_csv:
            print("No se encontraron archivos de datos.")
            print("Ejecuta primero la preparación de datos.")
            return
        
        print(f"Archivos de datos disponibles ({len(archivos_csv)}):")
        for i, archivo in enumerate(archivos_csv, 1):
            tamaño = archivo.stat().st_size
            print(f"{i}. {archivo.name} ({tamaño} bytes)")
        
        print(f"\n{len(archivos_csv) + 1}. Ver resumen de todos los archivos")
        print(f"{len(archivos_csv) + 2}. Abrir carpeta de datos")
        print(f"{len(archivos_csv) + 3}. Volver al menú principal")
        
        try:
            opcion = input(f"\nSelecciona una opción (1-{len(archivos_csv) + 3}): ").strip()
            
            if opcion.isdigit():
                opcion_num = int(opcion)
                
                if 1 <= opcion_num <= len(archivos_csv):
                    # Mostrar archivo seleccionado
                    archivo_seleccionado = archivos_csv[opcion_num - 1]
                    self._mostrar_tabla(archivo_seleccionado)
                    
                elif opcion_num == len(archivos_csv) + 1:
                    # Resumen de todos los archivos
                    self._mostrar_resumen_datos()
                    
                elif opcion_num == len(archivos_csv) + 2:
                    # Abrir carpeta
                    self._abrir_carpeta(self.resultados_dir)
                    
                elif opcion_num == len(archivos_csv) + 3:
                    # Volver
                    return
                else:
                    print("Opción inválida.")
            else:
                print("Opción inválida.")
                
        except KeyboardInterrupt:
            print("\nOperación cancelada.")
        except Exception as e:
            print(f"Error: {e}")
    
    def _abrir_grafico(self, archivo_grafico):
        """Abrir gráfico automáticamente y mostrar interpretación."""
        print(f"\n📊 GRÁFICO: {archivo_grafico.name}")
        print("=" * 60)
        
        # Mostrar interpretación específica basada en el nombre del archivo
        self._mostrar_interpretacion(archivo_grafico)
        
        print("\n" + "-" * 60)
        print("Opciones:")
        print("1. Abrir gráfico en visor de imágenes")
        print("2. Ver solo interpretación (sin abrir)")
        print("3. Volver")
        
        try:
            opcion = input("\nSelecciona una opción (1-3): ").strip()
            
            if opcion == '1':
                # Intentar abrir con el programa predeterminado del sistema
                if os.name == 'nt':  # Windows
                    os.startfile(str(archivo_grafico))
                    print(f"[OK] Gráfico abierto con programa predeterminado")
                else:  # Linux/Mac
                    subprocess.run(['xdg-open', str(archivo_grafico)])
                    print(f"[OK] Gráfico abierto con programa predeterminado")
            elif opcion == '2':
                print("\n[OK] Interpretación mostrada arriba")
            elif opcion == '3':
                return
            else:
                print("Opción inválida.")
                
        except Exception as e:
            print(f"[ERROR] No se pudo abrir automáticamente: {e}")
            print(f"Ubicación del archivo: {archivo_grafico.absolute()}")
            print("Abre manualmente el archivo desde el explorador.")
    
    def _mostrar_interpretacion(self, archivo_grafico):
        """Mostrar interpretación específica del gráfico."""
        nombre = archivo_grafico.name.lower()
        
        # Cargar datos si están disponibles para interpretaciones dinámicas
        try:
            # Intentar cargar datos de evaluación si existen
            reporte_path = self.metricas_dir / "reporte_evaluacion.txt"
            datos_disponibles = False
            
            if reporte_path.exists():
                with open(reporte_path, 'r', encoding='utf-8') as f:
                    contenido_reporte = f.read()
                    datos_disponibles = True
        except:
            datos_disponibles = False
            contenido_reporte = ""
        
        print("\n📋 INTERPRETACIÓN ESPECÍFICA:")
        print("-" * 60)
        
        if "predicciones_vs_reales" in nombre:
            print("""
¿QUÉ MUESTRA ESTE GRÁFICO?
──────────────────────────────────────────────────────────────────────────────
Este gráfico compara las predicciones de los modelos de Machine Learning con 
los valores reales del conjunto de prueba. Cada subgráfico corresponde a un 
modelo diferente.

ELEMENTOS VISUALES:
──────────────────────────────────────────────────────────────────────────────
• PUNTOS AZULES: Cada punto representa una predicción del modelo vs su valor real
• LÍNEA ROJA DIAGONAL: Línea perfecta donde predicción = realidad
• TÍTULO: Nombre del modelo y su R² Score

CÓMO LEERLO:
──────────────────────────────────────────────────────────────────────────────
1. Si los puntos están MUY CERCA de la línea roja:
   → El modelo es EXCELENTE (predice muy bien)

2. Si los puntos están DISPERSOS alrededor de la línea:
   → El modelo necesita mejorar

3. R² Score en el título:
   • R² > 0.9 = EXCELENTE (explica más del 90% de la variabilidad)
   • R² > 0.7 = BUENO (explica más del 70% de la variabilidad)
   • R² > 0.5 = REGULAR (explica más del 50% de la variabilidad)
   • R² < 0.5 = POBRE (explica menos del 50% de la variabilidad)
            """)
            
            # Agregar valores específicos si están disponibles
            if datos_disponibles and "R²" in contenido_reporte:
                print("\nVALORES ESPECÍFICOS DE ESTE GRÁFICO:")
                print("-" * 60)
                # Extraer información del reporte si es posible
                lineas = contenido_reporte.split('\n')
                for linea in lineas:
                    if 'R²' in linea or 'MSE' in linea or 'Mejor modelo' in linea:
                        print(f"  • {linea.strip()}")
            
        elif "matriz_confusion" in nombre or "confusion" in nombre:
            print("""
¿QUÉ MUESTRA ESTE GRÁFICO?
──────────────────────────────────────────────────────────────────────────────
Esta matriz muestra qué tan bien el modelo clasifica los datos en diferentes 
categorías. Es especialmente útil para problemas de clasificación.

ELEMENTOS VISUALES:
──────────────────────────────────────────────────────────────────────────────
• CUADRADOS CON NÚMEROS: Cada cuadrado muestra cuántos casos fueron clasificados
• DIAGONAL (arriba-izquierda a abajo-derecha): Predicciones CORRECTAS
• FUERA DE LA DIAGONAL: Predicciones INCORRECTAS
• COLORES MÁS OSCUROS: Más casos en esa categoría

CÓMO LEERLO:
──────────────────────────────────────────────────────────────────────────────
1. Números ALTOS en la diagonal:
   → El modelo clasifica BIEN esas categorías

2. Números ALTOS fuera de la diagonal:
   → El modelo confunde esas categorías (necesita mejorar)

3. Matriz perfecta:
   → Todos los números estarían en la diagonal (modelo perfecto)

EJEMPLO:
──────────────────────────────────────────────────────────────────────────────
Si ves:
  [100   5]  → 100 correctas de Clase 0, 5 incorrectas (confundidas con Clase 1)
  [  3  92]  → 92 correctas de Clase 1, 3 incorrectas (confundidas con Clase 0)
            """)
            
            # Agregar valores específicos si están disponibles
            if datos_disponibles:
                print("\nVALORES ESPECÍFICOS DE ESTE GRÁFICO:")
                print("-" * 60)
                if "Accuracy" in contenido_reporte:
                    for linea in contenido_reporte.split('\n'):
                        if 'Accuracy' in linea or 'Precision' in linea or 'Recall' in linea:
                            print(f"  • {linea.strip()}")
        else:
            print("""
¿QUÉ MUESTRA ESTE GRÁFICO?
──────────────────────────────────────────────────────────────────────────────
Este gráfico muestra resultados de evaluación de modelos de Machine Learning.

ELEMENTOS VISUALES:
──────────────────────────────────────────────────────────────────────────────
• Diferentes elementos visuales según el tipo de gráfico
• Colores y formas que representan diferentes métricas o modelos

CÓMO LEERLO:
──────────────────────────────────────────────────────────────────────────────
1. Revisa los títulos y etiquetas para entender qué representa cada elemento
2. Compara los valores mostrados entre diferentes modelos o métricas
3. Busca patrones o tendencias en los datos visualizados
            """)
        
        print("\n💡 RECOMENDACIONES:")
        print("-" * 60)
        if "predicciones_vs_reales" in nombre:
            print("• Si el R² es bajo, considera:")
            print("  → Ajustar hiperparámetros del modelo")
            print("  → Agregar más características (features)")
            print("  → Revisar la calidad de los datos")
            print("  → Probar otros algoritmos")
        elif "matriz_confusion" in nombre or "confusion" in nombre:
            print("• Si hay muchos errores fuera de la diagonal:")
            print("  → Revisar el balance de clases en los datos")
            print("  → Ajustar el umbral de clasificación")
            print("  → Probar técnicas de balanceo de datos")
            print("  → Considerar modelos de ensemble")
        
        print(f"\n📁 Ubicación: {archivo_grafico.absolute()}")
    
    def _mostrar_tabla(self, archivo_csv):
        """Mostrar tabla de datos."""
        print(f"\nMostrando datos: {archivo_csv.name}")
        print("-" * 40)
        
        try:
            # Cargar datos
            df = pd.read_csv(archivo_csv)
            
            print(f"Dimensiones: {df.shape[0]} filas x {df.shape[1]} columnas")
            print(f"Columnas: {list(df.columns)}")
            
            # Mostrar primeras filas
            print(f"\nPrimeras 10 filas:")
            print(df.head(10).to_string(index=True))
            
            # Mostrar estadísticas básicas si hay datos numéricos
            if df.select_dtypes(include=['number']).shape[1] > 0:
                print(f"\nEstadísticas básicas:")
                print(df.describe().to_string())
            
            # Opciones adicionales
            print(f"\nOpciones adicionales:")
            print("1. Ver más filas (20)")
            print("2. Ver estadísticas completas")
            print("3. Abrir archivo en Excel")
            print("4. Volver")
            
            opcion_extra = input("\nSelecciona una opción (1-4): ").strip()
            
            if opcion_extra == '1':
                print(f"\nPrimeras 20 filas:")
                print(df.head(20).to_string(index=True))
            elif opcion_extra == '2':
                print(f"\nEstadísticas completas:")
                print(df.describe(include='all').to_string())
            elif opcion_extra == '3':
                self._abrir_excel(archivo_csv)
            elif opcion_extra == '4':
                return
            else:
                print("Opción inválida.")
                
        except Exception as e:
            print(f"[ERROR] Error al cargar datos: {e}")
            print("El archivo puede estar corrupto o tener formato incorrecto.")
    
    def _mostrar_resumen_datos(self):
        """Mostrar resumen de todos los archivos de datos."""
        print(f"\nRESUMEN DE ARCHIVOS DE DATOS")
        print("-" * 40)
        
        archivos_csv = list(self.resultados_dir.glob("*.csv"))
        
        for archivo in archivos_csv:
            try:
                df = pd.read_csv(archivo)
                tamaño = archivo.stat().st_size
                print(f"\n{archivo.name}:")
                print(f"  - Dimensiones: {df.shape[0]} filas x {df.shape[1]} columnas")
                print(f"  - Tamaño: {tamaño} bytes")
                print(f"  - Columnas: {list(df.columns)}")
                
                # Mostrar tipos de datos
                tipos = df.dtypes.value_counts()
                print(f"  - Tipos de datos: {dict(tipos)}")
                
            except Exception as e:
                print(f"\n{archivo.name}: Error al leer - {e}")
    
    def _abrir_excel(self, archivo_csv):
        """Abrir archivo CSV en Excel."""
        print(f"\nAbriendo en Excel: {archivo_csv.name}")
        
        try:
            if os.name == 'nt':  # Windows
                # Intentar abrir con Excel
                subprocess.run(['excel', str(archivo_csv)], check=False)
                print(f"[OK] Archivo abierto en Excel")
            else:
                # En otros sistemas, abrir con programa predeterminado
                subprocess.run(['xdg-open', str(archivo_csv)])
                print(f"[OK] Archivo abierto con programa predeterminado")
                
        except Exception as e:
            print(f"[ERROR] No se pudo abrir en Excel: {e}")
            print(f"Ubicación del archivo: {archivo_csv.absolute()}")
            print("Abre manualmente el archivo desde el explorador.")
    
    def _abrir_carpeta(self, directorio):
        """Abrir carpeta en el explorador."""
        print(f"\nAbriendo carpeta: {directorio.name}")
        
        try:
            if os.name == 'nt':  # Windows
                os.startfile(str(directorio))
                print(f"[OK] Carpeta abierta en explorador")
            else:  # Linux/Mac
                subprocess.run(['xdg-open', str(directorio)])
                print(f"[OK] Carpeta abierta en explorador")
                
        except Exception as e:
            print(f"[ERROR] No se pudo abrir carpeta: {e}")
            print(f"Ubicación: {directorio.absolute()}")

def main():
    """Función principal para pruebas."""
    visualizador = VisualizadorAutomatico()
    
    print("VISUALIZADOR AUTOMATICO - PROYECTO AURELION")
    print("Grupo 11 - Camada 1 | Enith Gicela Vargas Vargas")
    print("=" * 60)
    
    while True:
        print("\nMENU DE VISUALIZACION:")
        print("1. Ver gráficos")
        print("2. Ver datos")
        print("3. Salir")
        
        opcion = input("\nSelecciona una opción (1-3): ").strip()
        
        if opcion == '1':
            visualizador.mostrar_graficos()
        elif opcion == '2':
            visualizador.mostrar_datos()
        elif opcion == '3':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()
