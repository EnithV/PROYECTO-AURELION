#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PROGRAMA UNIFICADO AURELION - INTERACCIÓN CON LOS 3 SPRINTS
===========================================================

**Autor:** Enith Gicela Vargas Vargas  
**Camada:** 1  
**Grupo:** 11  
**Fecha:** 2025-10-27  
**Curso:** AI Fundamentals - Guayerd - IBM Skills Build  
**Proyecto:** Aurelion - Sistema Unificado  
**Módulo:** Programa Principal Interactivo  

Sistema unificado que permite al usuario interactuar con los 3 sprints del proyecto:
- Sprint_1: Análisis de Datos Básico
- Sprint_2: Machine Learning y Normalización  
- Sprint_3: Machine Learning Fundamentals

Funcionalidades:
- Menú principal para seleccionar sprint
- Navegación entre diferentes módulos
- Acceso a todas las funcionalidades de cada sprint
- Sistema de ayuda y documentación
"""

import os
import sys
import subprocess
from datetime import datetime

class ProgramaUnificadoAurelion:
    """
    Clase principal del sistema unificado de Aurelion.
    
    Permite al usuario navegar entre los 3 sprints y acceder a todas
    las funcionalidades interactivas disponibles.
    """
    
    def __init__(self):
        """
        Inicializar el sistema unificado de Aurelion.
        
        Configura las rutas a los programas principales de cada sprint y verifica
        que los archivos existan antes de permitir su ejecución.
        
        Atributos:
            fecha_actual (str): Fecha y hora actual en formato DD/MM/YYYY HH:MM:SS
            ruta_proyecto (str): Ruta absoluta del directorio raíz del proyecto
            rutas_sprints (dict): Diccionario con las rutas a los programas principales
                                 de cada sprint (claves: '1', '2', '3')
        """
        self.fecha_actual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.ruta_proyecto = os.path.dirname(os.path.abspath(__file__))
        
        # Rutas a los programas de cada sprint
        self.rutas_sprints = {
            '1': os.path.join(self.ruta_proyecto, 'Sprint_1', 'Enith Gicela Vargas Vargas - Proyecto Aurelion', 'aurelion_analisis.py'),
            '2': os.path.join(self.ruta_proyecto, 'Sprint_2', 'sistema_interactivo_sprint2.py'),
            '3': os.path.join(self.ruta_proyecto, 'Sprint_3', 'Enith Gicela Vargas Vargas - Proyecto Aurelion', 'Demo', 'demo_interactivo.py')
        }
        
        # Verificar que los archivos existen
        self.verificar_archivos()
        
    def verificar_archivos(self):
        """
        Verificar que los archivos principales de cada sprint existen.
        
        Comprueba la existencia de los archivos Python principales de cada sprint
        y muestra una advertencia si alguno no se encuentra. Esto ayuda a detectar
        problemas de configuración antes de intentar ejecutar los programas.
        
        Returns:
            None: Solo muestra advertencias en consola si hay archivos faltantes
        """
        archivos_faltantes = []
        
        for sprint, ruta in self.rutas_sprints.items():
            if not os.path.exists(ruta):
                archivos_faltantes.append(f"Sprint_{sprint}: {ruta}")
        
        if archivos_faltantes:
            print("⚠️  ADVERTENCIA: Los siguientes archivos no se encontraron:")
            for archivo in archivos_faltantes:
                print(f"   - {archivo}")
            print()
    
    def mostrar_banner(self):
        """Mostrar banner principal del sistema."""
        print("=" * 80)
        print("🏪 PROGRAMA UNIFICADO AURELION - SISTEMA DE ANÁLISIS DE DATOS E IA")
        print("=" * 80)
        print(f"👤 Autor: Enith Gicela Vargas Vargas")
        print(f"📅 Fecha: {self.fecha_actual}")
        print(f"🎓 Curso: AI Fundamentals - Guayerd - IBM Skills Build")
        print(f"🏢 Proyecto: Tienda Aurelion - Análisis Completo")
        print("=" * 80)
        print()
    
    def mostrar_menu_principal(self):
        """Mostrar menú principal del sistema unificado."""
        print("📋 MENÚ PRINCIPAL - SELECCIÓN DE SPRINT")
        print("=" * 50)
        print()
        print("🎯 OPCIONES DISPONIBLES:")
        print()
        print("1️⃣  [1] SPRINT_1 - ANÁLISIS DE DATOS BÁSICO")
        print("    📊 Análisis exploratorio de ventas, productos, clientes")
        print("    📈 Segmentación RFM de clientes")
        print("    📋 Reportes ejecutivos")
        print("    🔧 Sistema interactivo completo")
        print()
        print("2️⃣  [2] SPRINT_2 - MACHINE LEARNING Y NORMALIZACIÓN")
        print("    🔄 Normalización avanzada de datos")
        print("    🤖 Modelos de Machine Learning (regresión, clasificación, clustering)")
        print("    📊 Visualizaciones avanzadas (24 gráficos)")
        print("    📉 Análisis de curtosis (pesadez de colas)")
        print("    💳 Análisis estadístico detallado de medios de pago")
        print("    📈 Pairplots y scatter plots para variables continuas normalizadas")
        print("    📉 Boxplots para detección de outliers")
        print("    📈 Análisis de correlaciones y clustering")
        print("    🔬 Estadística inferencial avanzada (tests de hipótesis, ANOVA, chi-cuadrado)")
        print("    📋 Matrices de confusión para modelos de clasificación")
        print("    🎯 Estadística prescriptiva (optimización de inventario, precios, recomendaciones)")
        print()
        print("3️⃣  [3] SPRINT_3 - MACHINE LEARNING FUNDAMENTALS")
        print("    🧠 Fundamentos de Machine Learning")
        print("    🔬 Tipos de aprendizajes")
        print("    ⚙️  Algoritmos básicos")
        print("    📏 Métricas de evaluación")
        print("    🎯 Predicciones y comparación de modelos")
        print()
        print("4️⃣  [4] INFORMACIÓN DEL PROYECTO")
        print("    📖 Documentación completa")
        print("    📊 Resumen de resultados")
        print("    🔍 Estado de cada sprint")
        print()
        print("5️⃣  [5] SALIR")
        print()
        print("-" * 50)
    
    def ejecutar_sprint_1(self):
        """
        Ejecutar el programa interactivo del Sprint_1.
        
        Inicia el sistema de análisis de datos básico del Sprint_1, que incluye:
        - Análisis exploratorio de ventas, productos, clientes y pagos
        - Segmentación RFM de clientes
        - Generación de reportes ejecutivos
        - Consulta de documentación
        
        El método guarda y restaura el directorio de trabajo actual para asegurar
        que el programa se ejecute en el contexto correcto sin afectar el directorio
        del usuario.
        
        Returns:
            None: La función no retorna valores, solo ejecuta el programa
        """
        print("🚀 INICIANDO SPRINT_1 - ANÁLISIS DE DATOS BÁSICO")
        print("=" * 60)
        print()
        
        ruta_sprint1 = self.rutas_sprints['1']
        
        if os.path.exists(ruta_sprint1):
            try:
                print("📂 Ejecutando: aurelion_analisis.py")
                print("💡 Este programa te permitirá:")
                print("   - Analizar ventas, productos, clientes y pagos")
                print("   - Realizar segmentación RFM de clientes")
                print("   - Generar reportes ejecutivos")
                print("   - Consultar documentación")
                print()
                
                # Guardar el directorio actual
                directorio_original = os.getcwd()
                
                try:
                    # Cambiar al directorio del Sprint_1
                    directorio_sprint1 = os.path.dirname(ruta_sprint1)
                    os.chdir(directorio_sprint1)
                    
                    # Ejecutar el programa usando la ruta absoluta
                    subprocess.run([sys.executable, ruta_sprint1], check=True)
                finally:
                    # Restaurar el directorio original
                    os.chdir(directorio_original)
                
            except subprocess.CalledProcessError as e:
                print(f"❌ Error al ejecutar Sprint_1: {e}")
            except FileNotFoundError:
                print("❌ No se encontró el archivo aurelion_analisis.py")
        else:
            print("❌ El archivo del Sprint_1 no existe en la ruta esperada")
            print(f"   Ruta buscada: {ruta_sprint1}")
        
        input("\n⏸️  Presiona Enter para continuar...")
    
    def ejecutar_sprint_2(self):
        """
        Ejecutar el programa interactivo del Sprint_2.
        
        Inicia el sistema de Machine Learning y Normalización del Sprint_2, que incluye:
        - Análisis de esquema de base de datos
        - Análisis exploratorio de datos (EDA)
        - Normalización avanzada de datos
        - Merge de tablas
        - Generación de visualizaciones avanzadas (19 gráficos)
        - Entrenamiento y evaluación de modelos de ML
        - Visualización de resultados y reportes
        
        El método guarda y restaura el directorio de trabajo actual para asegurar
        que el programa se ejecute en el contexto correcto.
        
        Returns:
            None: La función no retorna valores, solo ejecuta el programa
        """
        print("🚀 INICIANDO SPRINT_2 - MACHINE LEARNING Y NORMALIZACIÓN")
        print("=" * 60)
        print()
        
        ruta_sprint2 = self.rutas_sprints['2']
        
        if os.path.exists(ruta_sprint2):
            try:
                print("📂 Ejecutando: sistema_interactivo_sprint2.py")
                print("💡 Este programa te permitirá:")
                print("   - Ejecutar análisis de esquema")
                print("   - Realizar análisis exploratorio (EDA)")
                print("   - Normalizar datos")
                print("   - Hacer merge de tablas")
                print("   - Generar visualizaciones")
                print("   - Entrenar modelos de ML")
                print("   - Ver resultados y reportes")
                print()
                
                # Guardar el directorio actual
                directorio_original = os.getcwd()
                
                try:
                    # Cambiar al directorio del Sprint_2
                    directorio_sprint2 = os.path.dirname(ruta_sprint2)
                    os.chdir(directorio_sprint2)
                    
                    # Ejecutar el programa usando la ruta absoluta
                    subprocess.run([sys.executable, ruta_sprint2], check=True)
                finally:
                    # Restaurar el directorio original
                    os.chdir(directorio_original)
                
            except subprocess.CalledProcessError as e:
                print(f"❌ Error al ejecutar Sprint_2: {e}")
            except FileNotFoundError:
                print("❌ No se encontró el archivo sistema_interactivo_sprint2.py")
        else:
            print("❌ El archivo del Sprint_2 no existe en la ruta esperada")
            print(f"   Ruta buscada: {ruta_sprint2}")
        
        input("\n⏸️  Presiona Enter para continuar...")
    
    def ejecutar_sprint_3(self):
        """
        Ejecutar el programa interactivo del Sprint_3.
        
        Inicia el sistema de Machine Learning Fundamentals del Sprint_3, que incluye:
        - Fundamentos de Machine Learning
        - Tipos de aprendizajes (Supervisado, No Supervisado, Refuerzo)
        - Algoritmos básicos con explicación de función costo
        - Métricas de evaluación
        - Preparación de datos para ML
        - Entrenamiento y evaluación de modelos
        - Visualización de predicciones y comparación de modelos
        
        El método guarda y restaura el directorio de trabajo actual para asegurar
        que el programa se ejecute en el contexto correcto.
        
        Returns:
            None: La función no retorna valores, solo ejecuta el programa
        """
        print("🚀 INICIANDO SPRINT_3 - MACHINE LEARNING FUNDAMENTALS")
        print("=" * 60)
        print()
        
        ruta_sprint3 = self.rutas_sprints['3']
        
        if os.path.exists(ruta_sprint3):
            try:
                print("📂 Ejecutando: demo_interactivo.py")
                print("💡 Este programa te permitirá:")
                print("   - Explorar fundamentos de Machine Learning")
                print("   - Conocer tipos de aprendizajes")
                print("   - Probar algoritmos básicos")
                print("   - Ver métricas de evaluación")
                print("   - Analizar predicciones y modelos")
                print()
                
                # Guardar el directorio actual
                directorio_original = os.getcwd()
                
                try:
                    # Cambiar al directorio del Sprint_3
                    directorio_sprint3 = os.path.dirname(ruta_sprint3)
                    os.chdir(directorio_sprint3)
                    
                    # Ejecutar el programa usando la ruta absoluta
                    subprocess.run([sys.executable, ruta_sprint3], check=True)
                finally:
                    # Restaurar el directorio original
                    os.chdir(directorio_original)
                
            except subprocess.CalledProcessError as e:
                print(f"❌ Error al ejecutar Sprint_3: {e}")
            except FileNotFoundError:
                print("❌ No se encontró el archivo demo_interactivo.py")
        else:
            print("❌ El archivo del Sprint_3 no existe en la ruta esperada")
            print(f"   Ruta buscada: {ruta_sprint3}")
        
        input("\n⏸️  Presiona Enter para continuar...")
    
    def mostrar_informacion_proyecto(self):
        """Mostrar información detallada del proyecto con datos específicos."""
        print("📖 INFORMACIÓN DEL PROYECTO AURELION")
        print("=" * 60)
        print()
        
        # Intentar cargar datos para mostrar información específica
        datos_especificos = self._obtener_datos_especificos_proyecto()
        
        print("🎯 OBJETIVO DEL PROYECTO:")
        print("   Desarrollar un sistema completo de análisis de datos e IA")
        print("   para optimizar las operaciones de la Tienda Aurelion.")
        print()
        
        if datos_especificos:
            print("📊 DATOS ESPECÍFICOS DEL PROYECTO:")
            print(datos_especificos)
            print()
        
        print("📊 ESTRUCTURA DEL PROYECTO:")
        print("   📁 Sprint_1: Análisis de Datos Básico")
        print("      - Sistema interactivo de análisis")
        print("      - Segmentación RFM de clientes")
        print("      - Reportes ejecutivos")
        print()
        print("   📁 Sprint_2: Machine Learning y Normalización")
        print("      - Normalización avanzada de datos")
        print("      - Modelos de ML (Regresión, Clasificación, Clustering)")
        print("      - Visualizaciones avanzadas (24 gráficos)")
        print("      - Análisis de curtosis (pesadez de colas)")
        print("      - Análisis estadístico detallado de medios de pago")
        print("      - Pairplots y scatter plots para variables continuas normalizadas")
        print("      - Boxplots para detección de outliers")
        print("      - Estadística inferencial avanzada (tests de hipótesis, ANOVA, chi-cuadrado)")
        print("      - Matrices de confusión para modelos de clasificación")
        print("      - Estadística prescriptiva (optimización y recomendaciones)")
        print("      - Generación automática de documentación (ANALISIS_GRAFICOS.md, VARIABLES_Y_CENTROIDES.md)")
        print()
        print("   📁 Sprint_3: Machine Learning Fundamentals")
        print("      - Fundamentos teóricos de ML")
        print("      - Algoritmos básicos")
        print("      - Métricas de evaluación")
        print()
        
        print("📈 RESULTADOS OBTENIDOS:")
        print("   ✅ Sprint_1: Sistema interactivo completo")
        print("   ✅ Sprint_2: 11 scripts + 40+ archivos generados (incluye generación automática de documentación)")
        print("   ✅ Sprint_3: Demo interactiva con 15 opciones")
        print()
        
        print("🔧 TECNOLOGÍAS UTILIZADAS:")
        print("   - Python 3.x")
        print("   - Pandas (manipulación de datos)")
        print("   - NumPy (cálculos numéricos)")
        print("   - Matplotlib/Seaborn (visualizaciones)")
        print("   - Scikit-learn (Machine Learning)")
        print("   - Excel (datos de entrada)")
        print()
        
        print("📚 DOCUMENTACIÓN DISPONIBLE:")
        print("   - README.md (instrucciones generales)")
        print("   - Documentación técnica de cada sprint")
        print("   - Reportes de verificación")
        print("   - Diagramas de flujo")
        print()
        
        input("\n⏸️  Presiona Enter para continuar...")
    
    def _obtener_datos_especificos_proyecto(self):
        """Obtener datos específicos del proyecto para mostrar en la información."""
        try:
            import pandas as pd
            from pathlib import Path
            
            # Intentar encontrar la ruta de los datos
            ruta_base = Path(__file__).parent
            ruta_datos = ruta_base / "Datos Proyecto" / "Base de datos_Tienda_Aurelion" / "Base de datos"
            
            if not ruta_datos.exists():
                return ""
            
            # Cargar datos
            df_clientes = pd.read_excel(ruta_datos / "clientes.xlsx")
            df_productos = pd.read_excel(ruta_datos / "productos.xlsx")
            df_ventas = pd.read_excel(ruta_datos / "ventas.xlsx")
            df_detalle = pd.read_excel(ruta_datos / "detalle_ventas.xlsx")
            
            # Calcular estadísticas
            num_clientes = len(df_clientes)
            num_productos = len(df_productos)
            num_ventas = len(df_ventas)
            num_detalle = len(df_detalle)
            
            if 'importe' in df_detalle.columns:
                total_ventas = df_detalle['importe'].sum()
                promedio_venta = df_detalle.groupby('id_venta')['importe'].sum().mean()
            else:
                total_ventas = 0
                promedio_venta = 0
            
            if 'precio_unitario' in df_productos.columns:
                precio_min = df_productos['precio_unitario'].min()
                precio_max = df_productos['precio_unitario'].max()
            else:
                precio_min = precio_max = 0
            
            return f"""   • Clientes: {num_clientes:,} clientes únicos
   • Productos: {num_productos:,} productos en catálogo
   • Ventas: {num_ventas:,} transacciones
   • Líneas de detalle: {num_detalle:,} líneas
   • Monto total de ventas: ${total_ventas:,.2f} pesos argentinos
   • Ticket promedio: ${promedio_venta:,.2f} pesos por venta
   • Rango de precios: ${precio_min:,.2f} - ${precio_max:,.2f} pesos"""
        except Exception as e:
            return ""
    
    def ejecutar_opcion(self, opcion):
        """
        Ejecutar la opción seleccionada por el usuario.
        
        Procesa la opción ingresada por el usuario y ejecuta la función correspondiente.
        Si la opción no es válida, muestra un mensaje de error con las opciones disponibles.
        
        Args:
            opcion (str): Número de opción seleccionada por el usuario ('1' a '5')
        
        Returns:
            None: Ejecuta la función correspondiente o muestra mensaje de error
        """
        opciones = {
            '1': self.ejecutar_sprint_1,
            '2': self.ejecutar_sprint_2,
            '3': self.ejecutar_sprint_3,
            '4': self.mostrar_informacion_proyecto,
            '5': self.salir
        }
        
        funcion = opciones.get(opcion)
        if funcion:
            funcion()
        else:
            print("❌ OPCIÓN INVÁLIDA")
            print("=" * 30)
            print("💡 Opciones válidas:")
            print("   • 1 - Sprint_1 (Análisis de Datos Básico)")
            print("   • 2 - Sprint_2 (Machine Learning y Normalización)")
            print("   • 3 - Sprint_3 (Machine Learning Fundamentals)")
            print("   • 4 - Información del Proyecto")
            print("   • 5 - Salir")
            print()
            print(f"⚠️  Has ingresado: '{opcion}'")
            print("   Por favor, ingresa un número del 1 al 5.")
            input("\n⏸️  Presiona Enter para continuar...")
    
    def salir(self):
        """Salir del programa."""
        print("👋 ¡Gracias por usar el Programa Unificado Aurelion!")
        print("🎓 Proyecto desarrollado para AI Fundamentals - Guayerd - IBM Skills Build")
        print("👤 Autor: Enith Gicela Vargas Vargas")
        print("=" * 60)
        sys.exit(0)
    
    def ejecutar(self):
        """
        Ejecutar el programa principal del sistema unificado.
        
        Bucle principal que mantiene el programa en ejecución, mostrando el menú
        y procesando las opciones del usuario hasta que se seleccione salir.
        
        Maneja:
        - Limpieza de pantalla antes de mostrar el menú
        - Captura de interrupciones del teclado (Ctrl+C)
        - Manejo de errores inesperados
        - Navegación entre diferentes sprints
        
        Returns:
            None: El programa se ejecuta hasta que el usuario selecciona salir
        """
        while True:
            try:
                # Limpiar pantalla (funciona en Windows y Unix)
                os.system('cls' if os.name == 'nt' else 'clear')
                
                # Mostrar banner y menú
                self.mostrar_banner()
                self.mostrar_menu_principal()
                
                # Solicitar opción al usuario
                print("💡 INSTRUCCIONES:")
                print("   • Escribe el número de la opción que deseas ejecutar")
                print("   • Ejemplo: escribe '1' para acceder al Sprint_1")
                print("   • Ejemplo: escribe '4' para ver información del proyecto")
                print()
                opcion = input("🔢 Ingresa tu opción (1-5): ").strip()
                
                # Ejecutar opción seleccionada
                self.ejecutar_opcion(opcion)
                
            except KeyboardInterrupt:
                print("\n\n⚠️  Programa interrumpido por el usuario.")
                self.salir()
            except Exception as e:
                print(f"\n❌ Error inesperado: {e}")
                input("\n⏸️  Presiona Enter para continuar...")

def main():
    """Función principal del programa."""
    programa = ProgramaUnificadoAurelion()
    programa.ejecutar()

if __name__ == "__main__":
    main()
