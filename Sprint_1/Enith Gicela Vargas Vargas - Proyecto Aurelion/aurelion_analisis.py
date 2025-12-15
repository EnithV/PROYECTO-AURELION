#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AURELION - SISTEMA DE ANÁLISIS DE DATOS - PROYECTO AURELION SPRINT_1
===================================================================

**Autor:** Enith Gicela Vargas Vargas  
**Camada:** 1  
**Grupo:** 11  
**Fecha:** 2025-10-27  
**Curso:** AI Fundamentals - Guayerd - IBM Skills Build  
**Sprint:** 1 - Análisis de Datos Básico  
**Módulo:** Sistema de Análisis Aurelion  

Sistema interactivo para analizar datos de ventas, clientes, productos 
y pagos de la Tienda Aurelion.

Funcionalidades:
1. Análisis de Ventas
2. Segmentación de Clientes (RFM)
3. Análisis de Productos
4. Análisis de Pagos
5. Reporte Completo
"""

# Importaciones necesarias para el funcionamiento del sistema
import pandas as pd          # Para manipulación y análisis de datos
import numpy as np           # Para cálculos numéricos
from datetime import datetime, timedelta  # Para manejo de fechas
import os                    # Para operaciones del sistema operativo
import sys                   # Para acceso a variables del sistema

class AurelionAnalisis:
    """
    Clase principal que implementa el sistema de análisis de datos de Aurelion.
    
    Esta clase encapsula toda la funcionalidad del sistema, incluyendo:
    - Carga y preparación de datos
    - Análisis de ventas, productos, pagos y clientes
    - Segmentación RFM de clientes
    - Interfaz de usuario interactiva
    - Consulta de documentación
    """
    def __init__(self):
        """
        Constructor de la clase AurelionAnalisis.
        
        Inicializa todas las variables de instancia que almacenarán los DataFrames
        de pandas con los datos de la base de datos de Aurelion.
        
        Variables de instancia:
        - df_clientes: DataFrame con información de clientes
        - df_productos: DataFrame con información de productos
        - df_ventas: DataFrame con información de ventas
        - df_detalle_ventas: DataFrame con detalle de cada venta
        - df_ventas_completo: DataFrame combinado para análisis complejos
        """
        # Obtener la ruta del directorio donde está este script
        # Esto permite que el script funcione desde cualquier ubicación
        self.ruta_base = os.path.dirname(os.path.abspath(__file__))
        
        # Inicializar todos los DataFrames como None
        self.df_clientes = None        # Datos de clientes
        self.df_productos = None       # Datos de productos
        self.df_ventas = None          # Datos de ventas principales
        self.df_detalle_ventas = None  # Detalle de cada venta
        self.df_ventas_completo = None # Datos combinados para análisis
        
    def cargar_datos(self):
        """
        Cargar datos desde archivos Excel de la base de datos de Aurelion.
        
        Esta función:
        1. Lee los 4 archivos Excel de la base de datos
        2. Los carga en DataFrames de pandas
        3. Prepara los datos para análisis
        4. Muestra estadísticas de carga
        
        Returns:
            bool: True si la carga fue exitosa, False en caso de error
        """
        try:
            print("CARGANDO DATOS DE AURELION...")
            print("=" * 50)
            
            # Definir ruta base donde están los archivos Excel
            # Usar ruta absoluta basada en la ubicación del script
            base_path = os.path.join(self.ruta_base, "Base de datos_Tienda_Aurelion", "Base de datos")
            
            # Verificar que el directorio existe
            if not os.path.exists(base_path):
                # Intentar ruta alternativa (desde el directorio raíz del proyecto)
                ruta_alternativa = os.path.join(self.ruta_base, "..", "..", "Datos Proyecto", "Base de datos_Tienda_Aurelion", "Base de datos")
                ruta_alternativa = os.path.abspath(ruta_alternativa)
                if os.path.exists(ruta_alternativa):
                    base_path = ruta_alternativa
                else:
                    raise FileNotFoundError(f"No se encontró el directorio de datos. Buscado en: {base_path}")
            
            # Cargar cada archivo Excel en su respectivo DataFrame
            print("Cargando clientes.xlsx...")
            ruta_clientes = os.path.join(base_path, "clientes.xlsx")
            self.df_clientes = pd.read_excel(ruta_clientes)
            
            print("Cargando productos.xlsx...")
            ruta_productos = os.path.join(base_path, "productos.xlsx")
            self.df_productos = pd.read_excel(ruta_productos)
            
            print("Cargando ventas.xlsx...")
            ruta_ventas = os.path.join(base_path, "ventas.xlsx")
            self.df_ventas = pd.read_excel(ruta_ventas)
            
            print("Cargando detalle_ventas.xlsx...")
            ruta_detalle = os.path.join(base_path, "detalle_ventas.xlsx")
            self.df_detalle_ventas = pd.read_excel(ruta_detalle)
            
            # Llamar a la función privada para preparar los datos
            print("Preparando datos para análisis...")
            self._preparar_datos()
            
            # Mostrar resumen de datos cargados
            print("\nDatos cargados exitosamente!")
            print(f"   • Clientes: {len(self.df_clientes)} registros")
            print(f"   • Productos: {len(self.df_productos)} registros")
            print(f"   • Ventas: {len(self.df_ventas)} registros")
            print(f"   • Detalle Ventas: {len(self.df_detalle_ventas)} registros")
            
            return True
            
        except Exception as e:
            # Capturar cualquier error durante la carga
            print(f"Error al cargar datos: {e}")
            return False
    
    def _preparar_datos(self):
        """
        Función privada para preparar y limpiar datos para análisis.
        
        Esta función realiza las siguientes operaciones:
        1. Convierte fechas al formato datetime de pandas
        2. Combina ventas con totales de detalle_ventas
        3. Agrega información de clientes a las ventas
        4. Agrega información de productos al detalle de ventas
        
        Nota: Esta es una función privada (prefijo _) que solo se usa internamente
        """
        # Convertir la columna de fechas al formato datetime para análisis temporal
        self.df_ventas['fecha'] = pd.to_datetime(self.df_ventas['fecha'])
        
        # Combinar ventas con totales calculados desde detalle_ventas
        # Agrupa por id_venta y suma los importes para obtener el total por venta
        self.df_ventas_completo = self.df_ventas.merge(
            self.df_detalle_ventas.groupby('id_venta')['importe'].sum().reset_index(),
            on='id_venta',
            how='left'
        )
        # Renombrar la columna 'importe' a 'total_venta' para mayor claridad
        self.df_ventas_completo.rename(columns={'importe': 'total_venta'}, inplace=True)
        
        # Agregar información de clientes a las ventas
        # Solo trae id_cliente y nombre_cliente para evitar duplicados
        self.df_ventas_completo = self.df_ventas_completo.merge(
            self.df_clientes[['id_cliente', 'nombre_cliente']],
            on='id_cliente',
            how='left',
            suffixes=('', '_cliente')  # Evita conflictos de nombres de columnas
        )
        
        # Agregar información de productos al detalle de ventas
        # Trae nombre_producto y precio_unitario para análisis de productos
        self.df_detalle_ventas = self.df_detalle_ventas.merge(
            self.df_productos[['id_producto', 'nombre_producto', 'precio_unitario']],
            on='id_producto',
            how='left',
            suffixes=('', '_prod')  # Evita conflictos de nombres de columnas
        )
    
    def mostrar_menu(self):
        """
        Mostrar el menú principal del sistema interactivo.
        
        Esta función despliega todas las opciones disponibles para el usuario,
        incluyendo los diferentes tipos de análisis y funciones del sistema.
        """
        print("\n" + "=" * 60)
        print("AURELION - SISTEMA DE ANÁLISIS DE DATOS")
        print("Grupo 11 - Camada 1 | Enith Gicela Vargas Vargas")
        print("=" * 60)
        print("\nSeleccione una opción:")
        print("1. Análisis de Ventas")           # Métricas básicas y tendencias de ventas
        print("2. Análisis de Productos")        # Productos más vendidos y rentables
        print("3. Análisis de Pagos")            # Distribución por método de pago
        print("4. Análisis de Clientes")         # Clientes más frecuentes y estadísticas
        print("5. Segmentación RFM de Clientes") # Clasificación avanzada de clientes
        print("6. Reporte Completo")             # Ejecuta todos los análisis
        print("7. Ver Reportes Guardados")       # Acceder a reportes guardados
        print("8. Consultar Documentación")      # Información del proyecto
        print("9. Salir")                        # Terminar el programa
        print("-" * 60)
    
    def analisis_ventas(self):
        """
        Realizar análisis completo de ventas.
        
        Esta función calcula y muestra:
        1. Métricas básicas de ventas (total, promedio, mejor/peor venta)
        2. Análisis temporal (ventas por mes)
        3. Top productos más vendidos
        4. Top clientes por frecuencia de compras
        """
        print("\nANÁLISIS DE VENTAS")
        print("=" * 50)
        
        # Calcular totales por venta agrupando detalle_ventas por id_venta
        # Esto nos da el monto total de cada venta individual
        totales_ventas = self.df_detalle_ventas.groupby('id_venta')['importe'].sum()
        
        # Calcular métricas básicas de ventas
        total_ventas = totales_ventas.sum()        # Suma total de todas las ventas
        promedio_venta = totales_ventas.mean()     # Promedio por venta
        mejor_venta = totales_ventas.max()         # Venta con mayor monto
        peor_venta = totales_ventas.min()          # Venta con menor monto
        num_ventas = len(totales_ventas)           # Número total de ventas
        
        print(f"MÉTRICAS BÁSICAS:")
        print(f"   • Total de ventas: ${total_ventas:,.2f}")
        print(f"   • Promedio por venta: ${promedio_venta:,.2f}")
        print(f"   • Mejor venta: ${mejor_venta:,.2f}")
        print(f"   • Peor venta: ${peor_venta:,.2f}")
        print(f"   • Número de ventas: {num_ventas}")
        
        # Análisis temporal: agrupar ventas por mes
        print(f"\nANÁLISIS TEMPORAL:")
        ventas_por_mes = self.df_ventas.groupby(self.df_ventas['fecha'].dt.to_period('M')).size()
        print("   Ventas por mes:")
        for periodo, cantidad in ventas_por_mes.items():
            print(f"   • {periodo}: {cantidad} ventas")
        
        # Top 5 productos más vendidos por cantidad
        print(f"\nTOP PRODUCTOS VENDIDOS:")
        top_productos = self.df_detalle_ventas.groupby('nombre_producto')['cantidad'].sum().nlargest(5)
        for i, (producto, cantidad) in enumerate(top_productos.items(), 1):
            print(f"   {i}. {producto}: {cantidad} unidades")
        
        # Top 5 clientes por número de compras
        print(f"\nTOP CLIENTES POR COMPRAS:")
        top_clientes = self.df_ventas_completo.groupby('nombre_cliente').size().nlargest(5)
        for i, (nombre, compras) in enumerate(top_clientes.items(), 1):
            print(f"   {i}. {nombre}: {compras} compras")
    
    def analisis_productos(self):
        """
        Realizar análisis completo de productos.
        
        Esta función calcula y muestra:
        1. Top 10 productos más vendidos con métricas detalladas
        2. Top 5 productos más rentables por ingresos totales
        3. Análisis de rentabilidad y performance de productos
        """
        print("\nANÁLISIS DE PRODUCTOS")
        print("=" * 50)
        
        # Agrupar productos y calcular métricas agregadas
        # Suma cantidades, promedia precios y suma importes por producto
        productos_analisis = self.df_detalle_ventas.groupby('nombre_producto').agg({
            'cantidad': 'sum',           # Total de unidades vendidas
            'precio_unitario': 'mean',   # Precio promedio del producto
            'importe': 'sum'             # Ingresos totales generados
        }).round(2)
        
        # Renombrar columnas para mayor claridad
        productos_analisis.columns = ['Unidades_Vendidas', 'Precio_Promedio', 'Ingresos_Totales']
        # Ordenar por unidades vendidas (descendente)
        productos_analisis = productos_analisis.sort_values('Unidades_Vendidas', ascending=False)
        
        # Mostrar top 10 productos más vendidos en formato tabla
        print("TOP 10 PRODUCTOS MÁS VENDIDOS:")
        print("   Producto | Unidades | Precio Prom | Ingresos")
        print("   " + "-" * 60)
        
        for i, (producto, datos) in enumerate(productos_analisis.head(10).iterrows(), 1):
            # Truncar nombre del producto a 30 caracteres para formato
            print(f"   {producto[:30]:<30} | {datos['Unidades_Vendidas']:>8.0f} | ${datos['Precio_Promedio']:>8.0f} | ${datos['Ingresos_Totales']:>8.0f}")
        
        # Mostrar top 5 productos más rentables por ingresos
        print(f"\nTOP 5 PRODUCTOS MÁS RENTABLES:")
        top_rentables = productos_analisis.nlargest(5, 'Ingresos_Totales')
        for i, (producto, datos) in enumerate(top_rentables.iterrows(), 1):
            print(f"   {i}. {producto}: ${datos['Ingresos_Totales']:,.2f} ingresos")
    
    def analisis_pagos(self):
        """
        Realizar análisis de métodos de pago.
        
        Esta función calcula y muestra:
        1. Distribución de ventas por método de pago
        2. Porcentajes de uso de cada método
        3. Análisis de preferencias de pago de los clientes
        """
        print("\nANÁLISIS DE PAGOS")
        print("=" * 50)
        
        # Agrupar ventas por método de pago y contar número de ventas
        pagos_analisis = self.df_ventas.groupby('medio_pago').agg({
            'id_venta': 'count'  # Contar número de ventas por método
        }).round(2)
        
        # Renombrar columna para mayor claridad
        pagos_analisis.columns = ['Numero_Ventas']
        # Ordenar por número de ventas (descendente)
        pagos_analisis = pagos_analisis.sort_values('Numero_Ventas', ascending=False)
        
        # Mostrar distribución absoluta por método de pago
        print("DISTRIBUCIÓN POR MÉTODO DE PAGO:")
        for metodo, datos in pagos_analisis.iterrows():
            print(f"   • {metodo}: {datos['Numero_Ventas']} ventas")
        
        # Calcular y mostrar porcentajes de uso
        print(f"\nPORCENTAJES:")
        total_ventas = pagos_analisis['Numero_Ventas'].sum()
        for metodo, datos in pagos_analisis.iterrows():
            porcentaje = (datos['Numero_Ventas'] / total_ventas) * 100
            print(f"   • {metodo}: {porcentaje:.1f}% de las ventas")
    
    def analisis_clientes(self):
        """
        Realizar análisis completo de clientes.
        
        Esta función calcula y muestra:
        1. Top 10 clientes más frecuentes por número de compras
        2. Estadísticas generales de comportamiento de clientes
        3. Métricas de engagement y actividad
        """
        print("\nANÁLISIS DE CLIENTES")
        print("=" * 50)
        
        # Calcular frecuencia de compras por cliente
        # Agrupa por nombre_cliente y cuenta el número de compras
        clientes_frecuencia = self.df_ventas_completo.groupby('nombre_cliente').size().nlargest(10)
        
        # Mostrar top 10 clientes más frecuentes
        print("TOP 10 CLIENTES MÁS FRECUENTES:")
        for i, (nombre, compras) in enumerate(clientes_frecuencia.items(), 1):
            print(f"   {i}. {nombre}: {compras} compras")
        
        # Calcular estadísticas generales de clientes
        total_clientes = len(self.df_clientes)                    # Total de clientes en la BD
        clientes_activos = len(self.df_ventas_completo['id_cliente'].unique())  # Clientes que han comprado
        promedio_compras = len(self.df_ventas) / clientes_activos # Promedio de compras por cliente activo
        max_compras = clientes_frecuencia.max()                   # Máximo número de compras de un cliente
        
        print(f"\nESTADÍSTICAS DE CLIENTES:")
        print(f"   • Total de clientes únicos: {clientes_activos}")
        print(f"   • Promedio de compras por cliente: {promedio_compras:.1f}")
        print(f"   • Cliente más activo: {max_compras} compras")
    
    def segmentacion_clientes_rfm(self):
        """
        Realizar segmentación RFM (Recency, Frequency, Monetary) de clientes.
        
        RFM es una técnica de análisis de clientes que evalúa:
        - Recency (R): Días desde la última compra (menos días = mejor)
        - Frequency (F): Número de compras realizadas (más compras = mejor)
        - Monetary (M): Valor total gastado (más dinero = mejor)
        
        Esta función:
        1. Calcula las métricas RFM para cada cliente
        2. Asigna puntuaciones del 1-5 para cada métrica
        3. Clasifica clientes en segmentos de comportamiento
        4. Muestra distribución y top clientes por segmento
        """
        print("\nSEGMENTACIÓN RFM DE CLIENTES")
        print("=" * 50)
        
        # Obtener la fecha más reciente para calcular Recency
        fecha_actual = self.df_ventas['fecha'].max()
        
        # Calcular Recency: días desde la última compra de cada cliente
        recency = self.df_ventas.groupby('id_cliente')['fecha'].max().apply(
            lambda x: (fecha_actual - x).days
        )
        
        # Calcular Frequency: número total de compras por cliente
        frequency = self.df_ventas.groupby('id_cliente').size()
        
        # Calcular Monetary: valor total gastado por cliente
        # Primero suma importes por venta, luego agrupa por cliente
        monetary = self.df_detalle_ventas.groupby('id_venta')['importe'].sum().groupby(
            self.df_ventas.set_index('id_venta')['id_cliente']
        ).sum()
        
        # Crear DataFrame con las tres métricas RFM
        rfm_df = pd.DataFrame({
            'Recency': recency,      # Días desde última compra
            'Frequency': frequency,  # Número de compras
            'Monetary': monetary     # Valor total gastado
        }).fillna(0)  # Llenar valores nulos con 0
        
        # Asignar puntuaciones del 1-5 para cada métrica RFM
        # Recency: 5 = muy reciente, 1 = muy antiguo
        rfm_df['R_Score'] = pd.cut(rfm_df['Recency'], bins=5, labels=[5,4,3,2,1])
        # Frequency: 5 = muy frecuente, 1 = poco frecuente
        rfm_df['F_Score'] = pd.cut(rfm_df['Frequency'], bins=5, labels=[1,2,3,4,5])
        # Monetary: 5 = muy alto gasto, 1 = bajo gasto
        rfm_df['M_Score'] = pd.cut(rfm_df['Monetary'], bins=5, labels=[1,2,3,4,5])
        
        # Crear código RFM combinando las tres puntuaciones
        rfm_df['RFM_Segment'] = rfm_df['R_Score'].astype(str) + rfm_df['F_Score'].astype(str) + rfm_df['M_Score'].astype(str)
        
        # Función para clasificar clientes en segmentos de comportamiento
        def segmentar_cliente(rfm_segment):
            """
            Clasificar cliente según su código RFM en segmentos de comportamiento.
            
            Segmentos:
            - Campeones: Clientes ideales (R alto, F alto, M alto)
            - Clientes Leales: Frecuentes y valiosos
            - Clientes Potenciales: Alto valor pero poca frecuencia
            - Clientes Nuevos: Recientes pero sin historial
            - Clientes Prometedores: En desarrollo
            - Clientes en Riesgo: Baja actividad reciente
            - Clientes Regulares: Comportamiento promedio
            """
            if rfm_segment in ['555', '554', '544', '545', '454', '455', '445']:
                return 'Campeones'  # R alto, F alto, M alto
            elif rfm_segment in ['543', '444', '435', '355', '354', '345', '344', '335']:
                return 'Clientes Leales'  # Frecuentes y valiosos
            elif rfm_segment in ['512', '511', '422', '421', '412', '411', '311']:
                return 'Clientes Potenciales'  # Alto valor, poca frecuencia
            elif rfm_segment in ['155', '154', '144', '214', '215', '115', '114']:
                return 'Clientes Nuevos'  # Recientes, sin historial
            elif rfm_segment in ['332', '342', '322', '231', '241', '251', '233']:
                return 'Clientes Prometedores'  # En desarrollo
            elif rfm_segment in ['111', '112', '121', '131', '141', '151']:
                return 'Clientes en Riesgo'  # Baja actividad
            else:
                return 'Clientes Regulares'  # Comportamiento promedio
        
        # Aplicar clasificación a todos los clientes
        rfm_df['Segmento'] = rfm_df['RFM_Segment'].apply(segmentar_cliente)
        
        # Mostrar distribución de segmentos
        print("DISTRIBUCIÓN DE SEGMENTOS:")
        segmentos = rfm_df['Segmento'].value_counts()
        for segmento, cantidad in segmentos.items():
            print(f"   • {segmento}: {cantidad} clientes")
        
        # Mostrar top clientes por segmento más importante
        print(f"\nTOP CLIENTES POR SEGMENTO:")
        for segmento in ['Campeones', 'Clientes Leales', 'Clientes Potenciales']:
            if segmento in segmentos.index:
                print(f"\n{segmento}:")
                # Obtener top 3 clientes del segmento por valor monetario
                top_clientes = rfm_df[rfm_df['Segmento'] == segmento].nlargest(3, 'Monetary')
                for i, (cliente_id, datos) in enumerate(top_clientes.iterrows(), 1):
                    # Buscar nombre del cliente en la tabla de clientes
                    cliente_info = self.df_clientes[self.df_clientes['id_cliente'] == cliente_id]
                    if not cliente_info.empty:
                        nombre = cliente_info.iloc[0]['nombre_cliente']
                        print(f"   {i}. {nombre}: ${datos['Monetary']:,.2f}")
    
    def reporte_completo(self):
        """
        Generar reporte completo ejecutando todos los análisis del sistema.
        
        Esta función:
        1. Ejecuta todos los análisis individuales (ventas, productos, pagos, clientes, RFM)
        2. Genera un resumen ejecutivo con métricas clave del negocio
        3. Proporciona una vista integral del rendimiento de la tienda
        4. Guarda el reporte completo en un archivo de texto
        """
        print("\nREPORTE COMPLETO - AURELION")
        print("=" * 60)
        
        # Capturar la salida del reporte para guardarla en archivo
        import io
        import sys
        from contextlib import redirect_stdout
        
        # Crear un buffer para capturar la salida
        output_buffer = io.StringIO()
        
        # Guardar stdout original
        stdout_original = sys.stdout
        
        # Crear un objeto que escriba tanto en el buffer como en la terminal
        class TeeOutput:
            def __init__(self, buffer, original):
                self.buffer = buffer
                self.original = original
            
            def write(self, text):
                self.buffer.write(text)
                self.original.write(text)
            
            def flush(self):
                self.buffer.flush()
                self.original.flush()
        
        # Usar TeeOutput para escribir en ambos lugares
        tee = TeeOutput(output_buffer, stdout_original)
        sys.stdout = tee
        
        try:
            # Ejecutar todos los análisis disponibles en secuencia
            self.analisis_ventas()              # Análisis de ventas y tendencias
            self.analisis_productos()           # Análisis de productos y rentabilidad
            self.analisis_pagos()               # Análisis de métodos de pago
            self.analisis_clientes()            # Análisis de comportamiento de clientes
            self.segmentacion_clientes_rfm()    # Segmentación avanzada RFM
            
            # Generar resumen ejecutivo con métricas clave
            print(f"\nRESUMEN EJECUTIVO")
            print("=" * 30)
            
            # Calcular métricas principales del negocio
            total_ventas = self.df_detalle_ventas['importe'].sum()  # Ingresos totales
            total_clientes = len(self.df_clientes)                  # Total de clientes registrados
            total_productos = len(self.df_productos)                # Total de productos en catálogo
            total_ventas_count = len(self.df_ventas)                # Número total de transacciones
            ticket_promedio = total_ventas / total_ventas_count     # Valor promedio por venta
            
            # Mostrar métricas clave del negocio
            print(f"• Total de ingresos: ${total_ventas:,.2f}")
            print(f"• Número de clientes: {total_clientes}")
            print(f"• Número de productos: {total_productos}")
            print(f"• Número de ventas: {total_ventas_count}")
            print(f"• Ticket promedio: ${ticket_promedio:,.2f}")
        finally:
            # Restaurar stdout original
            sys.stdout = stdout_original
        
        # Obtener el contenido del buffer
        contenido_reporte = output_buffer.getvalue()
        
        # Guardar el reporte en un archivo
        self._guardar_reporte(contenido_reporte)
    
    def _guardar_reporte(self, contenido):
        """
        Guardar el reporte completo en un archivo de texto.
        
        Args:
            contenido (str): Contenido del reporte a guardar
        """
        try:
            # Crear directorio de reportes si no existe
            directorio_reportes = os.path.join(self.ruta_base, "reportes")
            if not os.path.exists(directorio_reportes):
                os.makedirs(directorio_reportes)
            
            # Generar nombre de archivo con fecha y hora
            fecha_hora = datetime.now().strftime("%Y%m%d_%H%M%S")
            nombre_archivo = f"reporte_completo_{fecha_hora}.txt"
            ruta_archivo = os.path.join(directorio_reportes, nombre_archivo)
            
            # Agregar encabezado al reporte
            encabezado = f"""
{'='*60}
REPORTE COMPLETO - AURELION
{'='*60}
Fecha de generación: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}
Autor: Enith Gicela Vargas Vargas
Proyecto: AI Fundamentals - Guayerd - IBM Skills Build
{'='*60}

"""
            
            # Escribir el reporte en el archivo
            with open(ruta_archivo, 'w', encoding='utf-8') as f:
                f.write(encabezado)
                f.write(contenido)
            
            print(f"\n✅ Reporte guardado exitosamente:")
            print(f"   📄 {ruta_archivo}")
            
        except Exception as e:
            print(f"\n⚠️  Error al guardar el reporte: {e}")
    
    def ver_reportes_guardados(self):
        """
        Mostrar menú para acceder a reportes guardados.
        
        Permite al usuario:
        1. Ver lista de reportes disponibles
        2. Leer un reporte específico en la terminal
        3. Abrir la carpeta de reportes
        """
        print("\nREPORTES DE EVALUACIÓN")
        print("=" * 50)
        
        # Directorio de reportes
        directorio_reportes = os.path.join(self.ruta_base, "reportes")
        
        # Verificar si existe el directorio
        if not os.path.exists(directorio_reportes):
            print("⚠️  No se encontró el directorio de reportes.")
            print("   Los reportes se crearán cuando generes un reporte completo.")
            return
        
        # Obtener lista de archivos de reportes
        archivos_reportes = [f for f in os.listdir(directorio_reportes) 
                           if f.startswith("reporte_completo_") and f.endswith(".txt")]
        
        if not archivos_reportes:
            print("⚠️  No hay reportes guardados.")
            print("   Genera un reporte completo primero (opción 6).")
            return
        
        # Ordenar por fecha (más reciente primero)
        archivos_reportes.sort(reverse=True)
        
        # Bucle del sub-menú de reportes
        while True:
            print(f"\nReportes disponibles ({len(archivos_reportes)}):")
            for i, archivo in enumerate(archivos_reportes, 1):
                ruta_completa = os.path.join(directorio_reportes, archivo)
                tamaño = os.path.getsize(ruta_completa)
                print(f"{i}. {archivo} ({tamaño} bytes)")
            
            print(f"\n{len(archivos_reportes) + 1}. Generar reporte completo automático")
            print(f"{len(archivos_reportes) + 2}. Ver resumen ejecutivo")
            print(f"{len(archivos_reportes) + 3}. Abrir carpeta de reportes")
            print(f"{len(archivos_reportes) + 4}. Volver al menú principal")
            print("-" * 50)
            
            try:
                opcion = input(f"\nIngrese su opción (1-{len(archivos_reportes) + 4}): ").strip()
                
                # Ver reporte específico
                if opcion.isdigit() and 1 <= int(opcion) <= len(archivos_reportes):
                    indice = int(opcion) - 1
                    archivo_seleccionado = archivos_reportes[indice]
                    self._mostrar_reporte(os.path.join(directorio_reportes, archivo_seleccionado))
                
                # Generar nuevo reporte
                elif opcion == str(len(archivos_reportes) + 1):
                    self.reporte_completo()
                
                # Ver resumen ejecutivo
                elif opcion == str(len(archivos_reportes) + 2):
                    self._mostrar_resumen_ejecutivo()
                
                # Abrir carpeta
                elif opcion == str(len(archivos_reportes) + 3):
                    self._abrir_carpeta_reportes(directorio_reportes)
                
                # Volver al menú principal
                elif opcion == str(len(archivos_reportes) + 4):
                    break
                else:
                    print("\n❌ Opción inválida. Por favor, seleccione una opción válida.")
                
                if opcion != str(len(archivos_reportes) + 4):
                    input("\n⏸️  Presiona Enter para continuar...")
                    
            except KeyboardInterrupt:
                print("\n\nVolviendo al menú principal...")
                break
            except Exception as e:
                print(f"\n❌ Error: {e}")
                input("Presione Enter para continuar...")
    
    def _mostrar_reporte(self, ruta_archivo):
        """
        Mostrar el contenido de un reporte en la terminal.
        
        Args:
            ruta_archivo (str): Ruta completa al archivo de reporte
        """
        try:
            print("\n" + "=" * 60)
            print(f"REPORTE: {os.path.basename(ruta_archivo)}")
            print("=" * 60)
            
            with open(ruta_archivo, 'r', encoding='utf-8') as f:
                contenido = f.read()
                print(contenido)
            
            print("=" * 60)
            
        except FileNotFoundError:
            print(f"❌ No se encontró el archivo: {ruta_archivo}")
        except Exception as e:
            print(f"❌ Error al leer el archivo: {e}")
    
    def _mostrar_resumen_ejecutivo(self):
        """
        Mostrar un resumen ejecutivo rápido con métricas clave.
        """
        if self.df_detalle_ventas is None:
            print("\n⚠️  Primero debes cargar los datos.")
            return
        
        print("\n" + "=" * 60)
        print("RESUMEN EJECUTIVO - AURELION")
        print("=" * 60)
        
        # Calcular métricas principales
        total_ventas = self.df_detalle_ventas['importe'].sum()
        total_clientes = len(self.df_clientes)
        total_productos = len(self.df_productos)
        total_ventas_count = len(self.df_ventas)
        ticket_promedio = total_ventas / total_ventas_count if total_ventas_count > 0 else 0
        
        print(f"\n📊 MÉTRICAS CLAVE:")
        print(f"   • Total de ingresos: ${total_ventas:,.2f}")
        print(f"   • Número de clientes: {total_clientes}")
        print(f"   • Número de productos: {total_productos}")
        print(f"   • Número de ventas: {total_ventas_count}")
        print(f"   • Ticket promedio: ${ticket_promedio:,.2f}")
        print("\n💡 Para ver el reporte completo, selecciona un reporte guardado.")
        print("=" * 60)
    
    def _abrir_carpeta_reportes(self, directorio):
        """
        Abrir la carpeta de reportes en el explorador de archivos.
        
        Args:
            directorio (str): Ruta al directorio de reportes
        """
        try:
            import platform
            sistema = platform.system()
            
            if sistema == "Windows":
                os.startfile(directorio)
            elif sistema == "Darwin":  # macOS
                os.system(f"open '{directorio}'")
            else:  # Linux
                os.system(f"xdg-open '{directorio}'")
            
            print(f"\n✅ Carpeta abierta: {directorio}")
            
        except Exception as e:
            print(f"\n❌ Error al abrir la carpeta: {e}")
            print(f"   Ruta: {directorio}")
    
    def consultar_documentacion(self):
        """
        Consultar documentación del proyecto de manera interactiva.
        
        Esta función proporciona un sub-menú para acceder a diferentes secciones
        de documentación del proyecto, incluyendo información técnica, guías de uso
        y detalles de implementación.
        """
        print("\nCONSULTA DE DOCUMENTACIÓN - PROYECTO AURELION")
        print("=" * 60)
        
        # Bucle principal del sub-menú de documentación
        while True:
            print("\nSeleccione qué documentación desea consultar:")
            print("1. Información del Proyecto")        # Datos del estudiante y objetivos
            print("2. Estructura de la Base de Datos")   # Clasificación según clase 2
            print("3. Funcionalidades del Sistema")      # Descripción de cada análisis
            print("4. Guía de Uso")                      # Instrucciones de navegación
            print("5. Tecnologías Utilizadas")          # Librerías y herramientas
            print("6. Volver al Menú Principal")        # Regresar al menú principal
            print("-" * 50)
            
            try:
                # Obtener opción del usuario
                opcion = input("\nIngrese su opción (1-6): ").strip()
                
                # Ejecutar función correspondiente según la opción
                if opcion == '1':
                    self._mostrar_info_proyecto()      # Mostrar información del proyecto
                elif opcion == '2':
                    self._mostrar_estructura_bd()      # Mostrar estructura de BD
                elif opcion == '3':
                    self._mostrar_funcionalidades()    # Mostrar funcionalidades
                elif opcion == '4':
                    self._mostrar_guia_uso()           # Mostrar guía de uso
                elif opcion == '5':
                    self._mostrar_tecnologias()        # Mostrar tecnologías
                elif opcion == '6':
                    break  # Salir del sub-menú
                else:
                    print("\nOpción inválida. Por favor, seleccione una opción del 1 al 6.")
                
                # Pausa para que el usuario lea la información (excepto al salir)
                if opcion != '6':
                    input("\nPresione Enter para continuar...")
                    
            except KeyboardInterrupt:
                # Manejar interrupción del teclado (Ctrl+C)
                print("\n\nVolviendo al menú principal...")
                break
            except Exception as e:
                # Manejar cualquier otro error
                print(f"\nError: {e}")
                input("Presione Enter para continuar...")
    
    def _mostrar_info_proyecto(self):
        """
        Función auxiliar privada para mostrar información básica del proyecto.
        
        Muestra datos del estudiante, grupo, curso y objetivos del proyecto.
        """
        print("\n" + "=" * 50)
        print("INFORMACIÓN DEL PROYECTO")
        print("=" * 50)
        print("• Estudiante: Enith Gicela Vargas Vargas")
        print("• Grupo: 11 - Camada 1")
        print("• Proyecto: Análisis de Tienda Aurelion")
        print("• Curso: AI Fundamentals - Guayerd - IBM Skills Build")
        print("• Fecha: Octubre 2025")
        print("\nOBJETIVO:")
        print("Desarrollar un sistema de análisis de datos para optimizar")
        print("las operaciones comerciales de la Tienda Aurelion utilizando")
        print("técnicas de Inteligencia Artificial y análisis estadístico.")
    
    def _mostrar_estructura_bd(self):
        """
        Función auxiliar privada para mostrar estructura de la base de datos.
        
        Incluye clasificación según estructura, identificadores, tablas principales
        y clasificación según origen según los conceptos de la Clase 2.
        Muestra datos específicos calculados del proyecto.
        """
        print("\n" + "=" * 50)
        print("ESTRUCTURA DE LA BASE DE DATOS - PROYECTO AURELION")
        print("=" * 50)
        
        # Intentar cargar datos si no están cargados
        if self.df_clientes is None:
            self.cargar_datos()
        
        # Calcular datos específicos si los datos están cargados
        datos_especificos = ""
        if self.df_clientes is not None and self.df_productos is not None and \
           self.df_ventas is not None and self.df_detalle_ventas is not None:
            
            num_clientes = len(self.df_clientes)
            num_productos = len(self.df_productos)
            num_ventas = len(self.df_ventas)
            num_detalle = len(self.df_detalle_ventas)
            
            # Calcular estadísticas adicionales
            clientes_unicos = self.df_clientes['id_cliente'].nunique()
            productos_unicos = self.df_productos['id_producto'].nunique()
            ventas_unicas = self.df_ventas['id_venta'].nunique()
            
            # Calcular totales
            if 'importe' in self.df_detalle_ventas.columns:
                total_importe = self.df_detalle_ventas['importe'].sum()
                promedio_importe = self.df_detalle_ventas['importe'].mean()
            else:
                total_importe = 0
                promedio_importe = 0
            
            if 'precio_unitario' in self.df_productos.columns:
                precio_min = self.df_productos['precio_unitario'].min()
                precio_max = self.df_productos['precio_unitario'].max()
                precio_promedio = self.df_productos['precio_unitario'].mean()
            else:
                precio_min = precio_max = precio_promedio = 0
            
            # Período temporal
            if 'fecha_alta' in self.df_clientes.columns:
                fecha_min_clientes = self.df_clientes['fecha_alta'].min()
                fecha_max_clientes = self.df_clientes['fecha_alta'].max()
            else:
                fecha_min_clientes = fecha_max_clientes = None
            
            if 'fecha' in self.df_ventas.columns:
                fecha_min_ventas = self.df_ventas['fecha'].min()
                fecha_max_ventas = self.df_ventas['fecha'].max()
            else:
                fecha_min_ventas = fecha_max_ventas = None
            
            datos_especificos = f"""
DATOS ESPECÍFICOS DEL PROYECTO AURELION:
───────────────────────────────────────────────────────────────────────────────
• Total de registros en la base de datos: {num_clientes + num_productos + num_ventas + num_detalle:,} registros
• Clientes únicos: {clientes_unicos} clientes
• Productos únicos: {productos_unicos} productos
• Ventas únicas: {ventas_unicas} transacciones
• Líneas de detalle: {num_detalle:,} líneas
• Monto total de ventas: ${total_importe:,.2f} pesos argentinos
• Importe promedio por línea: ${promedio_importe:,.2f} pesos
• Rango de precios de productos: ${precio_min:,.2f} - ${precio_max:,.2f} pesos
• Precio promedio de productos: ${precio_promedio:,.2f} pesos
"""
            if fecha_min_clientes is not None:
                datos_especificos += f"• Período de clientes: {fecha_min_clientes.strftime('%Y-%m')} a {fecha_max_clientes.strftime('%Y-%m')}\n"
            if fecha_min_ventas is not None:
                datos_especificos += f"• Período de ventas: {fecha_min_ventas.strftime('%Y-%m')} a {fecha_max_ventas.strftime('%Y-%m')}\n"
        
        print("CLASIFICACIÓN SEGÚN ESTRUCTURA:")
        print("• Tipo: Estructurados (Tabulares)")
        print("• Formato: Excel (.xlsx)")
        print("• Características:")
        print("  - Campos (columnas): Características de entidades")
        print("  - Registros (filas): Instancias únicas")
        print("  - Tabla: Agrupación de registros")
        
        print("\nIDENTIFICADORES:")
        print("• Clave Primaria (PK): Garantiza unicidad")
        print("• Clave Foránea (FK): Establece relaciones")
        
        print("\nTABLAS PRINCIPALES:")
        
        if self.df_clientes is not None:
            num_clientes = len(self.df_clientes)
            print(f"\n1. CLIENTES ({num_clientes:,} registros)")
        else:
            print("\n1. CLIENTES (100 registros)")
        print("   • id_cliente: PK - Identificador único")
        print("   • nombre_cliente: Nombre completo")
        print("   • email: Correo electrónico")
        print("   • ciudad: Ciudad de residencia")
        print("   • fecha_alta: Fecha de registro")
        
        if self.df_productos is not None:
            num_productos = len(self.df_productos)
            print(f"\n2. PRODUCTOS ({num_productos:,} registros)")
        else:
            print("\n2. PRODUCTOS (100 registros)")
        print("   • id_producto: PK - Identificador único")
        print("   • nombre_producto: Nombre del producto")
        print("   • categoria: Categoría del producto")
        print("   • precio_unitario: Precio en pesos")
        
        if self.df_ventas is not None:
            num_ventas = len(self.df_ventas)
            print(f"\n3. VENTAS ({num_ventas:,} registros)")
        else:
            print("\n3. VENTAS (120 registros)")
        print("   • id_venta: PK - Identificador único")
        print("   • fecha: Fecha de la transacción")
        print("   • id_cliente: FK → clientes.id_cliente")
        print("   • medio_pago: Método de pago")
        
        if self.df_detalle_ventas is not None:
            num_detalle = len(self.df_detalle_ventas)
            print(f"\n4. DETALLE_VENTAS ({num_detalle:,} registros)")
        else:
            print("\n4. DETALLE_VENTAS (343 registros)")
        print("   • id_venta: FK → ventas.id_venta")
        print("   • id_producto: FK → productos.id_producto")
        print("   • cantidad: Cantidad vendida")
        print("   • importe: Importe total")
        
        print(datos_especificos)
        
        print("\nCLASIFICACIÓN SEGÚN ORIGEN:")
        print("• Tipo: Datos Secundarios")
        print("• Fuente: Base de datos del curso")
        print("• Características: Históricos, predefinidos, validados")
    
    def _mostrar_funcionalidades(self):
        """
        Función auxiliar privada para mostrar funcionalidades del sistema.
        
        Describe cada módulo de análisis disponible en el sistema.
        """
        print("\n" + "=" * 50)
        print("FUNCIONALIDADES DEL SISTEMA")
        print("=" * 50)
        print("1. ANÁLISIS DE VENTAS")
        print("   • Métricas básicas (total, promedio, mejor/peor venta)")
        print("   • Análisis temporal (ventas por mes)")
        print("   • Top productos y clientes")
        print("\n2. ANÁLISIS DE PRODUCTOS")
        print("   • Productos más vendidos")
        print("   • Análisis de rentabilidad")
        print("   • Categorización de productos")
        print("\n3. ANÁLISIS DE PAGOS")
        print("   • Distribución por método de pago")
        print("   • Análisis de porcentajes")
        print("   • Tendencias de pago")
        print("\n4. ANÁLISIS DE CLIENTES")
        print("   • Clientes más frecuentes")
        print("   • Estadísticas de comportamiento")
        print("   • Análisis de frecuencia")
        print("\n5. SEGMENTACIÓN RFM")
        print("   • Recency (días desde última compra)")
        print("   • Frequency (frecuencia de compras)")
        print("   • Monetary (valor total gastado)")
        print("   • Clasificación en segmentos")
    
    def _mostrar_guia_uso(self):
        """
        Función auxiliar privada para mostrar guía de uso del sistema.
        
        Proporciona instrucciones paso a paso para usar el sistema interactivo.
        """
        print("\n" + "=" * 50)
        print("GUÍA DE USO DEL SISTEMA")
        print("=" * 50)
        print("1. EJECUTAR EL SISTEMA:")
        print("   python aurelion_analisis.py")
        print("\n2. NAVEGACIÓN:")
        print("   • Seleccione una opción del menú (1-8)")
        print("   • Siga las instrucciones en pantalla")
        print("   • Use 'Enter' para continuar entre secciones")
        print("\n3. OPCIONES DISPONIBLES:")
        print("   • Opciones 1-6: Análisis específicos")
        print("   • Opción 7: Consultar documentación")
        print("   • Opción 8: Salir del sistema")
        print("\n4. INTERPRETACIÓN DE RESULTADOS:")
        print("   • Los resultados se muestran en formato legible")
        print("   • Los montos están en pesos argentinos")
        print("   • Las fechas siguen formato YYYY-MM-DD")
        print("\n5. DEMOSTRACIÓN COMPLETA:")
        print("   python demo_interactivo.py")
    
    def _mostrar_tecnologias(self):
        """
        Función auxiliar privada para mostrar tecnologías utilizadas.
        
        Lista las librerías, herramientas y estructura del código del proyecto.
        """
        print("\n" + "=" * 50)
        print("TECNOLOGÍAS UTILIZADAS")
        print("=" * 50)
        print("LENGUAJE DE PROGRAMACIÓN:")
        print("• Python 3.x - Lenguaje principal")
        print("\nLIBRERÍAS PRINCIPALES:")
        print("• pandas - Manipulación de datos")
        print("• numpy - Cálculos numéricos")
        print("• matplotlib - Visualizaciones")
        print("• seaborn - Gráficos estadísticos")
        print("• openpyxl - Lectura de archivos Excel")
        print("\nESTRUCTURA DEL CÓDIGO:")
        print("• Programación Orientada a Objetos")
        print("• Clases y métodos organizados")
        print("• Manejo de errores robusto")
        print("• Documentación completa")
        print("\nFORMATO DE DATOS:")
        print("• Archivos Excel (.xlsx)")
        print("• Codificación UTF-8")
        print("• Estructura relacional")
    
    def ejecutar(self):
        """
        Función principal que ejecuta el sistema interactivo completo.
        
        Esta función:
        1. Muestra el encabezado del sistema
        2. Carga los datos de la base de datos
        3. Ejecuta el bucle principal del menú interactivo
        4. Maneja la navegación entre opciones
        5. Gestiona errores y excepciones
        """
        print("AURELION - SISTEMA DE ANÁLISIS DE DATOS")
        print("Grupo 11 - Camada 1 | Enith Gicela Vargas Vargas")
        print("=" * 60)
        
        # Cargar datos de la base de datos
        if not self.cargar_datos():
            print("No se pudieron cargar los datos. Saliendo...")
            return
        
        # Bucle principal del sistema interactivo
        while True:
            self.mostrar_menu()  # Mostrar opciones del menú
            
            try:
                # Obtener opción del usuario
                opcion = input("\nIngrese su opción (1-9): ").strip()
                
                # Ejecutar función correspondiente según la opción seleccionada
                if opcion == '1':
                    self.analisis_ventas()              # Análisis de ventas
                elif opcion == '2':
                    self.analisis_productos()           # Análisis de productos
                elif opcion == '3':
                    self.analisis_pagos()               # Análisis de pagos
                elif opcion == '4':
                    self.analisis_clientes()            # Análisis de clientes
                elif opcion == '5':
                    self.segmentacion_clientes_rfm()    # Segmentación RFM
                elif opcion == '6':
                    self.reporte_completo()             # Reporte completo
                elif opcion == '7':
                    self.ver_reportes_guardados()       # Ver reportes guardados
                elif opcion == '8':
                    self.consultar_documentacion()      # Consultar documentación
                elif opcion == '9':
                    print("\n¡Gracias por usar el sistema Aurelion!")
                    break  # Salir del bucle principal
                else:
                    print("\nOpción inválida. Por favor, seleccione una opción del 1 al 9.")
                
                # Pausa para que el usuario lea los resultados (excepto documentación, reportes y salir)
                if opcion not in ['7', '8', '9']:
                    input("\nPresione Enter para continuar...")
                    
            except KeyboardInterrupt:
                # Manejar interrupción del teclado (Ctrl+C)
                print("\n\n¡Gracias por usar el sistema Aurelion!")
                break
            except Exception as e:
                # Manejar cualquier otro error durante la ejecución
                print(f"\nError: {e}")
                input("Presione Enter para continuar...")

# Bloque principal de ejecución del programa
if __name__ == "__main__":
    """
    Punto de entrada principal del programa.
    
    Este bloque se ejecuta solo cuando el archivo se ejecuta directamente
    (no cuando se importa como módulo). Crea una instancia de la clase
    AurelionAnalisis y ejecuta el sistema interactivo.
    """
    # Crear instancia del sistema de análisis
    sistema = AurelionAnalisis()
    
    # Ejecutar el sistema interactivo
    sistema.ejecutar()