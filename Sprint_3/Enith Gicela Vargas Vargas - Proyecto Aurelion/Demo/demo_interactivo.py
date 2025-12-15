#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
<!--
# DEMO INTERACTIVO ML - SPRINT_3
**Autor:** Enith Gicela Vargas Vargas  
**Camada:** 1  
**Grupo:** 11  
**Fecha:** 2025-11-11  
**Curso:** AI Fundamentals - Guayerd - IBM Skills Build  
**Sprint:** 3 - Machine Learning Fundamentals  
**Módulo:** Demo - Sistema Interactivo  
-->

DEMO INTERACTIVO DE MACHINE LEARNING - PROYECTO AURELION SPRINT_3
=================================================================

Demo interactiva principal para explorar Machine Learning, incluyendo:
- Menú de opciones
- Explorar tipos de aprendizajes
- Probar algoritmos
- Ver métricas
- Ver predicciones
"""

import sys               # Módulo para interactuar con el sistema
import os               # Módulo del sistema operativo
import subprocess       # Módulo para ejecutar subprocesos
from pathlib import Path  # Módulo para manejo de rutas
from visualizador_automatico import VisualizadorAutomatico  # Módulo para visualización automática
from visualizador_predicciones import VisualizadorPredicciones  # Módulo para predicciones reales
from comparador_modelos import ComparadorModelos  # Módulo para comparación detallada
from generador_reportes import GeneradorReportes  # Módulo para reportes automáticos
from analizador_graficos import AnalizadorGraficos  # Módulo para análisis de gráficos

class InteractiveMLDemo:
    """
    Clase para demo interactiva de Machine Learning del Sprint_3.
    
    Sistema interactivo que permite explorar los fundamentos y aplicaciones
    de Machine Learning con datos del proyecto Aurelion.
    
    Funcionalidades:
    - Menú interactivo con 15 opciones
    - Navegación entre módulos de fundamentos y modelado
    - Visualizaciones de predicciones y modelos
    - Comparación de modelos entrenados
    - Generación automática de reportes
    - Análisis detallado de gráficos
    """
    
    def __init__(self):
        """
        Inicializar la demo interactiva de Machine Learning.
        
        Configura las rutas base y inicializa los módulos auxiliares para
        visualización, predicciones, comparación de modelos, reportes y análisis.
        
        Atributos:
            ruta_base (str): Ruta absoluta del directorio Demo
            visualizador (VisualizadorAutomatico): Módulo para visualización automática
            predicciones (VisualizadorPredicciones): Módulo para predicciones reales
            comparador (ComparadorModelos): Módulo para comparación detallada
            reportes (GeneradorReportes): Módulo para reportes automáticos
            analizador (AnalizadorGraficos): Módulo para análisis de gráficos
        """
        print("DEMO INTERACTIVA DE MACHINE LEARNING")
        print("Grupo 11 - Camada 1 | Enith Gicela Vargas Vargas")
        print("=" * 60)
        # Obtener la ruta base del directorio Demo
        # Manejar el caso cuando se ejecuta con exec() donde __file__ no está definido
        try:
            self.ruta_base = os.path.dirname(os.path.abspath(__file__))
        except NameError:
            # Si __file__ no está definido, buscar el directorio Demo
            # Primero verificar si hay una variable global establecida por ejecutar_sprint3.py
            import builtins
            # Intentar acceder directamente a __DEMO_DIR__
            try:
                demo_dir = getattr(builtins, '__DEMO_DIR__', None)
                if demo_dir:
                    self.ruta_base = os.path.abspath(demo_dir)
                else:
                    raise AttributeError
            except (AttributeError, TypeError):
                # Si no hay variable global, usar el directorio actual
                # ejecutar_sprint3.py hace os.chdir(directorio_demo) antes de ejecutar
                # pero con exec() puede que no funcione, así que construimos la ruta manualmente
                cwd = os.path.abspath(os.getcwd())
                # Verificar si estamos en el directorio Demo (debe tener demo_fundamentos.py)
                if os.path.exists(os.path.join(cwd, "demo_fundamentos.py")):
                    self.ruta_base = cwd
                else:
                    # Si no estamos en Demo, buscar desde Sprint_3
                    if os.path.basename(cwd) == "Sprint_3":
                        # Buscar la carpeta del proyecto dentro de Sprint_3
                        for item in os.listdir(cwd):
                            item_path = os.path.join(cwd, item)
                            if os.path.isdir(item_path) and "Enith" in item:
                                demo_path = os.path.join(item_path, "Demo")
                                if os.path.exists(demo_path) and os.path.exists(os.path.join(demo_path, "demo_fundamentos.py")):
                                    self.ruta_base = os.path.abspath(demo_path)
                                    break
                        else:
                            # Si no se encontró, usar cwd como fallback
                            self.ruta_base = cwd
                    else:
                        # Si no estamos en Sprint_3, usar cwd
                        self.ruta_base = cwd
        self.visualizador = VisualizadorAutomatico()  # Inicializar visualizador automático
        self.predicciones = VisualizadorPredicciones()  # Inicializar visualizador de predicciones
        self.comparador = ComparadorModelos()  # Inicializar comparador de modelos
        self.reportes = GeneradorReportes()  # Inicializar generador de reportes
        self.analizador = AnalizadorGraficos()  # Inicializar analizador de gráficos
        
    def display_menu(self):
        """
        Mostrar menú principal de la demo interactiva.
        
        Despliega todas las opciones disponibles organizadas en secciones:
        - Fundamentos: Conceptos básicos de ML
        - Modelado: Procesos prácticos con datos
        - Visualización y Resultados: Análisis de outputs
        
        Returns:
            None: Solo muestra el menú en consola
        """
        print("\nMENÚ PRINCIPAL")
        print("=" * 60)
        print("FUNDAMENTOS:")
        print("1. Fundamentos de Machine Learning")
        print("2. Tipos de Aprendizajes")
        print("3. Algoritmos Básicos")
        print("4. Métricas de Evaluación")
        print("\nMODELADO:")
        print("5. Preparar Datos para ML")
        print("6. Entrenar Modelos")
        print("7. Evaluar Modelos")
        print("8. Ver Predicciones")
        print("9. Comparar Modelos")
        print("\nVISUALIZACIÓN Y RESULTADOS:")
        print("10. Ver Gráficos Generados")
        print("11. Ver Reportes de Evaluación")
        print("12. Ver Archivos de Datos")
        print("13. Inspeccionar Modelos (.pkl)")
        print("14. Analizar Gráficos Detalladamente")
        print("\n15. Salir")
        print("-" * 60)
    
    def execute_option(self, numero):
        """
        Ejecutar el módulo correspondiente a la opción seleccionada.
        
        Procesa la opción del usuario y ejecuta la función correspondiente.
        Si la opción no es válida, muestra un mensaje de error.
        
        Args:
            numero (str): Número de opción seleccionada ('1' a '14')
        
        Returns:
            None: Ejecuta la función correspondiente o muestra error
        """
        modulos = {
            '1': self.execute_fundamentos,
            '2': self.execute_tipos_aprendizajes,
            '3': self.execute_algoritmos,
            '4': self.execute_metricas,
            '5': self.execute_preparacion,
            '6': self.execute_entrenamiento,
            '7': self.execute_evaluacion,
            '8': self.ver_predicciones,
            '9': self.comparar_modelos,
            '10': self.ver_graficos,
            '11': self.ver_reportes,
            '12': self.ver_archivos_datos,
            '13': self.inspeccionar_modelos,
            '14': self.analizar_graficos
        }
        
        modulo = modulos.get(numero)
        if modulo:
            modulo()
        else:
            print("\n[ERROR] Opción inválida")
    
    def _ejecutar_demo(self, nombre_archivo):
        """
        Método auxiliar para ejecutar demos usando rutas absolutas.
        
        Ejecuta un script demo específico del Sprint_3, asegurando que se ejecute
        desde el directorio correcto y restaurando el directorio original después.
        Esto garantiza que los scripts encuentren sus dependencias y archivos de datos.
        
        Args:
            nombre_archivo (str): Nombre del archivo demo a ejecutar (ej: 'demo_fundamentos.py')
        
        Returns:
            None: Ejecuta el script o muestra mensaje de error
        """
        ruta_demo = os.path.join(self.ruta_base, nombre_archivo)
        if os.path.exists(ruta_demo):
            try:
                # Guardar directorio actual
                directorio_original = os.getcwd()
                try:
                    # Cambiar al directorio Demo
                    os.chdir(self.ruta_base)
                    # Ejecutar usando subprocess
                    subprocess.run([sys.executable, ruta_demo], check=True)
                finally:
                    # Restaurar directorio original
                    os.chdir(directorio_original)
            except subprocess.CalledProcessError as e:
                print(f"Error al ejecutar {nombre_archivo}: {e}")
        else:
            print(f"❌ No se encontró el archivo: {nombre_archivo}")
            print(f"   Ruta buscada: {ruta_demo}")
    
    def execute_fundamentos(self):
        """Ejecutar módulo de fundamentos."""
        print("\nEJECUTANDO MÓDULO: FUNDAMENTOS DE ML")
        print("=" * 50)
        self._ejecutar_demo("demo_fundamentos.py")
    
    def execute_tipos_aprendizajes(self):
        """Ejecutar módulo de tipos de aprendizajes."""
        print("\nEJECUTANDO MÓDULO: TIPOS DE APRENDIZAJES")
        print("=" * 50)
        self._ejecutar_demo("demo_aprendizajes.py")
    
    def execute_algoritmos(self):
        """Ejecutar módulo de algoritmos."""
        print("\nEJECUTANDO MÓDULO: ALGORITMOS BÁSICOS")
        print("=" * 50)
        self._ejecutar_demo("demo_algoritmos.py")
    
    def execute_metricas(self):
        """Ejecutar módulo de métricas."""
        print("\nEJECUTANDO MÓDULO: MÉTRICAS DE EVALUACIÓN")
        print("=" * 50)
        self._ejecutar_demo("demo_metricas.py")
    
    def execute_preparacion(self):
        """Ejecutar módulo de preparación."""
        print("\nEJECUTANDO MÓDULO: PREPARACIÓN DE DATOS")
        print("=" * 50)
        self._ejecutar_demo("demo_preparacion.py")
    
    def execute_entrenamiento(self):
        """Ejecutar módulo de entrenamiento."""
        print("\nEJECUTANDO MÓDULO: ENTRENAMIENTO DE MODELOS")
        print("=" * 50)
        self._ejecutar_demo("demo_entrenamiento.py")
    
    def execute_evaluacion(self):
        """Ejecutar módulo de evaluación."""
        print("\nEJECUTANDO MÓDULO: EVALUACIÓN DE MODELOS")
        print("=" * 50)
        self._ejecutar_demo("demo_evaluacion.py")
    
    def ver_predicciones(self):
        """Mostrar predicciones reales de modelos entrenados."""
        self.predicciones.mostrar_predicciones()
    
    def comparar_modelos(self):
        """Realizar comparación detallada de modelos entrenados."""
        self.comparador.comparar_modelos()
    
    def analizar_graficos(self):
        """Analizar gráficos detalladamente."""
        self.analizador.analizar_graficos()
    
    def ver_graficos(self):
        """Ver gráficos generados con visualización automática."""
        self.visualizador.mostrar_graficos()
    
    def ver_reportes(self):
        """Ver reportes con generación automática."""
        self.reportes.mostrar_reportes()
    
    def ver_archivos_datos(self):
        """Ver archivos de datos con visualización automática."""
        self.visualizador.mostrar_datos()
    
    def inspeccionar_modelos(self):
        """Inspeccionar modelos guardados (.pkl)."""
        print("\nINSPECCIÓN DE MODELOS (.PKL)")
        print("=" * 50)
        
        # Verificar si existe el inspector (ruta relativa al directorio Demo)
        ruta_sprint3 = os.path.dirname(self.ruta_base)
        inspector_path = os.path.join(ruta_sprint3, "inspector_pkl.py")
        
        if os.path.exists(inspector_path):
            print("Ejecutando inspector de modelos...")
            print("-" * 40)
            try:
                # Guardar directorio actual
                directorio_original = os.getcwd()
                try:
                    # Cambiar al directorio del Sprint_3
                    os.chdir(ruta_sprint3)
                    # Ejecutar usando subprocess
                    subprocess.run([sys.executable, inspector_path], check=True)
                finally:
                    # Restaurar directorio original
                    os.chdir(directorio_original)
            except subprocess.CalledProcessError as e:
                print(f"Error al ejecutar inspector: {e}")
        else:
            print("Inspector de modelos no encontrado.")
            print("Ubicación esperada:", os.path.abspath(inspector_path))
            
            # Mostrar información básica de los modelos
            modelos_dir = os.path.join(ruta_sprint3, "resultados", "modelos")
            if os.path.exists(modelos_dir):
                print("\nModelos disponibles:")
                archivos = os.listdir(modelos_dir)
                modelos = [f for f in archivos if f.endswith('.pkl')]
                
                for i, modelo in enumerate(modelos, 1):
                    ruta_modelo = os.path.join(modelos_dir, modelo)
                    tamaño = os.path.getsize(ruta_modelo)
                    print(f"{i}. {modelo} ({tamaño} bytes)")
                
                print(f"\nUbicación: {os.path.abspath(modelos_dir)}")
                print("\nLos archivos .pkl contienen modelos entrenados.")
                print("Para usarlos, carga con pickle.load() en Python.")
    
    def execute(self):
        """
        Ejecutar el bucle principal de la demo interactiva.
        
        Mantiene el programa en ejecución mostrando el menú y procesando las
        opciones del usuario hasta que se seleccione salir (opción 15).
        
        Maneja:
        - Captura de interrupciones del teclado (Ctrl+C)
        - Manejo de errores inesperados
        - Navegación entre diferentes módulos
        
        Returns:
            None: El programa se ejecuta hasta que el usuario selecciona salir
        """
        while True:
            self.display_menu()
            
            try:
                opcion = input("\nSeleccione una opción (1-15): ").strip()
                
                if opcion == '15':
                    print("\n¡Gracias por usar la Demo de ML!")
                    break
                else:
                    self.execute_option(opcion)
                    input("\nPresione Enter para continuar...")
                    
            except KeyboardInterrupt:
                print("\n\n¡Gracias por usar la Demo de ML!")
                break
            except Exception as e:
                print(f"\n[ERROR] Error: {e}")
                input("Presione Enter para continuar...")

def main():
    """Función principal del demo."""
    demo = InteractiveMLDemo()
    demo.execute()

if __name__ == "__main__":
    main()
