#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PROGRAMA INTERACTIVO SPRINT_2 - MACHINE LEARNING Y NORMALIZACIÓN
================================================================

**Autor:** Enith Gicela Vargas Vargas  
**Camada:** 1  
**Grupo:** 11  
**Fecha:** 2025-10-27  
**Curso:** AI Fundamentals - Guayerd - IBM Skills Build  
**Sprint:** 2 - Machine Learning y Normalización  
**Módulo:** Sistema Interactivo Principal  

Sistema interactivo para el Sprint_2 que permite al usuario:
- Ejecutar análisis de esquema
- Realizar análisis exploratorio (EDA)
- Normalizar datos
- Hacer merge de tablas
- Generar visualizaciones
- Entrenar modelos de ML
- Ver resultados y reportes
"""

import os
import sys
import subprocess
from datetime import datetime

class Sprint2Interactivo:
    """
    Clase para el sistema interactivo del Sprint_2.
    
    Permite al usuario ejecutar todos los scripts del Sprint_2
    de forma interactiva con un menú de opciones.
    """
    
    def __init__(self):
        """
        Inicializar el sistema interactivo del Sprint_2.
        
        Configura las rutas a los scripts del Sprint_2 y verifica que existan.
        Define la estructura de scripts disponibles con sus descripciones.
        
        Atributos:
            fecha_actual (str): Fecha y hora actual en formato DD/MM/YYYY HH:MM:SS
            ruta_sprint2 (str): Ruta absoluta al directorio de scripts del Sprint_2
            scripts (dict): Diccionario con información de los 8 scripts disponibles
            scripts_existentes (dict): Diccionario con solo los scripts que existen
        """
        self.fecha_actual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        # Ruta base donde está este archivo (Sprint_2/)
        ruta_base = os.path.dirname(os.path.abspath(__file__))
        # Ruta donde están los scripts (Sprint_2/Enith Gicela Vargas Vargas - Proyecto Aurelion/)
        self.ruta_sprint2 = os.path.join(ruta_base, 'Enith Gicela Vargas Vargas - Proyecto Aurelion')
        
        # Scripts disponibles en el Sprint_2
        self.scripts = {
            '1': {
                'archivo': '00_analisis_esquema.py',
                'descripcion': 'Análisis de Esquema de Base de Datos',
                'detalle': 'Analiza las claves primarias y foráneas de las tablas'
            },
            '2': {
                'archivo': '01_analisis_exploratorio.py',
                'descripcion': 'Análisis Exploratorio de Datos (EDA)',
                'detalle': 'Estadísticas descriptivas, análisis de distribuciones y análisis estadístico detallado de medios de pago'
            },
            '3': {
                'archivo': '02_normalizacion_datos.py',
                'descripcion': 'Normalización de Datos',
                'detalle': 'Normaliza y limpia los datos para ML'
            },
            '4': {
                'archivo': '03_merge_tablas.py',
                'descripcion': 'Merge de Tablas',
                'detalle': 'Combina todas las tablas en un dataset unificado'
            },
            '5': {
                'archivo': '04_resumen_final.py',
                'descripcion': 'Resumen Final',
                'detalle': 'Genera resumen estadístico del dataset final'
            },
            '6': {
                'archivo': '05_visualizaciones_avanzadas.py',
                'descripcion': 'Visualizaciones Avanzadas',
                'detalle': 'Genera 24 gráficos profesionales con interpretaciones específicas del proyecto (histogramas, correlaciones, outliers, curtosis, etc.)'
            },
            '7': {
                'archivo': '06_modelos_ml.py',
                'descripcion': 'Modelos de Machine Learning',
                'detalle': 'Entrena y evalúa modelos de ML (regresión, clasificación, clustering) con matrices de confusión que incluyen rangos específicos de importe por segmento'
            },
            '8': {
                'archivo': '08_estadistica_inferencial.py',
                'descripcion': 'Estadística Inferencial Avanzada',
                'detalle': 'Tests de hipótesis (t-test, chi-cuadrado, ANOVA), tests de normalidad, intervalos de confianza'
            },
            '9': {
                'archivo': '09_estadistica_prescriptiva.py',
                'descripcion': 'Estadística Prescriptiva',
                'detalle': 'Optimización de inventario, precios, recomendaciones de acciones basadas en datos'
            },
            '10': {
                'archivo': '07_reporte_final.py',
                'descripcion': 'Reporte Final',
                'detalle': 'Genera reporte completo del proyecto'
            },
            '11': {
                'archivo': '10_generar_analisis_graficos.py',
                'descripcion': 'Generar ANALISIS_GRAFICOS.md Automáticamente',
                'detalle': 'Genera automáticamente el archivo ANALISIS_GRAFICOS.md con datos reales del proyecto (se ejecuta automáticamente después de las visualizaciones)'
            },
            '12': {
                'archivo': '11_generar_variables_centroides.py',
                'descripcion': 'Generar VARIABLES_Y_CENTROIDES.md Automáticamente',
                'detalle': 'Genera automáticamente el archivo VARIABLES_Y_CENTROIDES.md con datos reales de modelos ML (se ejecuta automáticamente después de entrenar modelos)'
            }
        }
        
        # Verificar que los scripts existen
        self.verificar_scripts()
    
    def verificar_scripts(self):
        """Verificar que todos los scripts existen."""
        self.scripts_existentes = {}
        
        for numero, info in self.scripts.items():
            ruta_script = os.path.join(self.ruta_sprint2, info['archivo'])
            if os.path.exists(ruta_script):
                self.scripts_existentes[numero] = info
            else:
                print(f"⚠️  Script no encontrado: {info['archivo']}")
    
    def mostrar_banner(self):
        """Mostrar banner del Sprint_2."""
        print("=" * 80)
        print("🤖 SPRINT_2 - MACHINE LEARNING Y NORMALIZACIÓN")
        print("=" * 80)
        print(f"👤 Autor: Enith Gicela Vargas Vargas")
        print(f"📅 Fecha: {self.fecha_actual}")
        print(f"🎓 Curso: AI Fundamentals - Guayerd - IBM Skills Build")
        print(f"🏢 Proyecto: Tienda Aurelion - Sprint_2")
        print("=" * 80)
        print()
    
    def _numero_a_emoji(self, numero):
        """
        Convertir un número a su representación en emojis.
        
        Args:
            numero (str): Número como string (ej: '1', '10', '11')
        
        Returns:
            str: Representación del número en emojis (ej: '1️⃣', '1️⃣0️⃣', '1️⃣1️⃣')
        """
        emoji_map = {
            '0': '0️⃣', '1': '1️⃣', '2': '2️⃣', '3': '3️⃣', '4': '4️⃣',
            '5': '5️⃣', '6': '6️⃣', '7': '7️⃣', '8': '8️⃣', '9': '9️⃣'
        }
        
        # Si es un solo dígito, usar el emoji directamente
        if len(numero) == 1:
            return emoji_map.get(numero, numero)
        
        # Si es de dos dígitos, combinar los emojis
        return ''.join([emoji_map.get(digito, digito) for digito in numero])
    
    def mostrar_menu(self):
        """Mostrar menú principal del Sprint_2."""
        print("📋 MENÚ PRINCIPAL - SPRINT_2")
        print("=" * 50)
        print()
        print("🔧 SCRIPTS DISPONIBLES:")
        print()
        
        for numero, info in self.scripts_existentes.items():
            estado = "✅" if numero in self.scripts_existentes else "❌"
            numero_emoji = self._numero_a_emoji(numero)
            print(f"{numero_emoji}  {estado} {info['descripcion']}")
            print(f"    📝 {info['detalle']}")
            print()
        
        print("1️⃣3️⃣  📊 Ver Resultados Generados")
        print("    📁 Explorar archivos de resultados")
        print()
        print("1️⃣4️⃣  📈 Visualizar Gráficos con Interpretaciones")
        print("    🖼️  Ver gráficos específicos con análisis detallado")
        print()
        print("0️⃣  🚪 Salir")
        print()
        print("-" * 50)
    
    def ejecutar_script(self, numero):
        """
        Ejecutar un script específico del Sprint_2.
        
        Ejecuta el script correspondiente al número seleccionado, cambiando al
        directorio correcto y restaurando el directorio original después de la
        ejecución. Maneja errores y muestra mensajes informativos.
        
        Args:
            numero (str): Número del script a ejecutar ('1' a '8')
        
        Returns:
            None: Ejecuta el script o muestra mensaje de error
        """
        if numero not in self.scripts_existentes:
            print("❌ Script no disponible.")
            return
        
        info = self.scripts_existentes[numero]
        archivo = info['archivo']
        
        print(f"🚀 EJECUTANDO: {info['descripcion']}")
        print("=" * 60)
        print(f"📂 Archivo: {archivo}")
        print(f"📝 Descripción: {info['detalle']}")
        print()
        
        try:
            # Guardar directorio actual
            directorio_actual = os.getcwd()
            try:
                # Cambiar al directorio donde están los scripts
                os.chdir(self.ruta_sprint2)
                # Configurar entorno con codificación UTF-8 para Windows
                env = os.environ.copy()
                env['PYTHONIOENCODING'] = 'utf-8'
                # Ejecutar el script directamente sin capturar output
                # Esto permite que los emojis se muestren correctamente en la consola
                subprocess.run(
                    [sys.executable, archivo], 
                    check=True,
                    env=env
                )
            finally:
                # Restaurar directorio original
                os.chdir(directorio_actual)
            
            print()
            print("✅ Script ejecutado exitosamente!")
                
        except subprocess.CalledProcessError as e:
            print(f"❌ Error al ejecutar el script: {e}")
            print(f"   Código de salida: {e.returncode}")
        except FileNotFoundError:
            print("❌ No se encontró el archivo del script")
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
        
        input("\n⏸️  Presiona Enter para continuar...")
    
    def ver_resultados(self):
        """
        Mostrar la estructura de resultados generados por los scripts.
        
        Explora recursivamente el directorio de resultados y muestra la estructura
        de archivos y carpetas generados por los diferentes scripts del Sprint_2.
        Incluye información de tamaño de archivos.
        
        Returns:
            None: Solo muestra información en consola
        """
        print("📊 RESULTADOS GENERADOS - SPRINT_2")
        print("=" * 60)
        print()
        
        # Directorio de resultados
        directorio_resultados = os.path.join(self.ruta_sprint2, 'resultados')
        
        if not os.path.exists(directorio_resultados):
            print("❌ No se encontró el directorio de resultados.")
            print("   Ejecuta primero algunos scripts para generar resultados.")
            input("\n⏸️  Presiona Enter para continuar...")
            return
        
        print("📁 ESTRUCTURA DE RESULTADOS:")
        print()
        
        # Explorar directorio de resultados
        self.explorar_directorio(directorio_resultados, nivel=0)
        
        print()
        print("💡 Para ver archivos específicos, navega a las carpetas correspondientes.")
        
        input("\n⏸️  Presiona Enter para continuar...")
    
    def explorar_directorio(self, directorio, nivel=0):
        """Explorar recursivamente un directorio."""
        indentacion = "  " * nivel
        
        try:
            elementos = sorted(os.listdir(directorio))
            
            for elemento in elementos:
                ruta_elemento = os.path.join(directorio, elemento)
                
                if os.path.isdir(ruta_elemento):
                    print(f"{indentacion}📁 {elemento}/")
                    # Solo mostrar un nivel más para no saturar
                    if nivel < 1:
                        self.explorar_directorio(ruta_elemento, nivel + 1)
                else:
                    # Mostrar información del archivo
                    tamaño = os.path.getsize(ruta_elemento)
                    if tamaño > 1024 * 1024:  # > 1MB
                        tamaño_str = f"{tamaño / (1024 * 1024):.1f} MB"
                    elif tamaño > 1024:  # > 1KB
                        tamaño_str = f"{tamaño / 1024:.1f} KB"
                    else:
                        tamaño_str = f"{tamaño} bytes"
                    
                    print(f"{indentacion}📄 {elemento} ({tamaño_str})")
        
        except PermissionError:
            print(f"{indentacion}❌ Sin permisos para acceder")
        except Exception as e:
            print(f"{indentacion}❌ Error: {e}")
    
    def visualizar_graficos(self):
        """
        Abrir el visualizador de gráficos interactivo.
        
        Ejecuta el visualizador de gráficos que permite ver los 19 gráficos generados
        con sus interpretaciones detalladas. El visualizador incluye análisis específicos
        para cada gráfico adaptados para personas sin conocimiento estadístico.
        
        Returns:
            None: Ejecuta el visualizador o muestra mensaje de error
        """
        print("📈 VISUALIZADOR DE GRÁFICOS INTERACTIVO")
        print("=" * 60)
        print()
        
        # Importar y ejecutar el visualizador
        try:
            ruta_visualizador = os.path.join(self.ruta_sprint2, 'visualizador_graficos_interactivo.py')
            if os.path.exists(ruta_visualizador):
                # Cambiar al directorio correcto
                directorio_actual = os.getcwd()
                try:
                    os.chdir(self.ruta_sprint2)
                    # Ejecutar el visualizador
                    subprocess.run([sys.executable, 'visualizador_graficos_interactivo.py'], check=True)
                finally:
                    os.chdir(directorio_actual)
            else:
                print("❌ El visualizador de gráficos no está disponible.")
                print(f"   Archivo esperado: {ruta_visualizador}")
        except Exception as e:
            print(f"❌ Error al abrir el visualizador: {e}")
        
        input("\n⏸️  Presiona Enter para continuar...")
    
    def ejecutar_opcion(self, opcion):
        """Ejecutar la opción seleccionada."""
        if opcion in self.scripts_existentes:
            self.ejecutar_script(opcion)
        elif opcion == '13':
            self.ver_resultados()
        elif opcion == '14':
            self.visualizar_graficos()
        elif opcion == '0':
            self.salir()
        else:
            print("❌ Opción inválida. Por favor, selecciona una opción válida.")
            input("\n⏸️  Presiona Enter para continuar...")
    
    def salir(self):
        """Salir del programa."""
        print("👋 ¡Gracias por usar el Sistema Interactivo Sprint_2!")
        print("🎓 Proyecto desarrollado para AI Fundamentals - Guayerd - IBM Skills Build")
        print("👤 Autor: Enith Gicela Vargas Vargas")
        print("=" * 60)
        sys.exit(0)
    
    def ejecutar(self):
        """Ejecutar el programa principal."""
        while True:
            try:
                # Limpiar pantalla
                os.system('cls' if os.name == 'nt' else 'clear')
                
                # Mostrar banner y menú
                self.mostrar_banner()
                self.mostrar_menu()
                
                # Solicitar opción al usuario
                opcion = input("🔢 Selecciona una opción: ").strip()
                
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
    programa = Sprint2Interactivo()
    programa.ejecutar()

if __name__ == "__main__":
    main()
