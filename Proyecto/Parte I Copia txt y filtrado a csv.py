"""
Script Python que copia desde carpeta SAP archivos:
1_purch.txt
2_archivo de prueba.txt
3_archivo de prueba.txt
4_admitted.txt
5_archivo de prueba.txt
6_archivo de prueba.txt
7_archivo de prueba.txt
8_archivo de prueba.txt
9_archivo de prueba.txt
10_archivo de prueba.txt
11_archivo de prueba.txt
12_archivo de prueba.txt
13_archivo de prueba.txt

Para luego extraer lineas de interes.
"""

import shutil
import os
import csv
import codecs

#----------
# #Definiendo variables.
# #Carpeta ubicacion txt originales

# Crear carpeta Taller Pyday2022 y guardar ahi descarga reeposiutorio, completar xxx con ubicacion local
carpeta_referencia = r"X:\xxxx\xxxxx\Desktop\Taller Pyday2022\Ubicacion original"


# Crear carpeta Taller Pyday2022 y guardar ahi descarga reeposiutorio, completar xxx con ubicacion local
carpeta_bases_jobs = r"X:\xxxx\xxxxx\Desktop\Taller Pyday2022\Proyecto\bases_jobs_sap"

# Crear carpeta Taller Pyday2022 y guardar ahi descarga reeposiutorio, completar xxx con ubicacion local
carpeta_bases_csv = r"X:\xxxx\xxxxx\Desktop\Taller Pyday2022\Proyecto\bases_csv_automaticas"

#-----
#Archivos iniciales.
TXT_ORIGINALES = ['1_purch.txt', '2_archivo de prueba.txt', '3_archivo de prueba.txt', '4_admitted.txt', 
                  '5_archivo de prueba.txt', '6_archivo de prueba.txt', '7_archivo de prueba.txt', '8_archivo de prueba.txt', '9_archivo de prueba.txt', '10_archivo de prueba.txt', 
                  '11_archivo de prueba.txt', '12_archivo de prueba.txt', '13_archivo de prueba.txt']

TXT_COPIA_LOCAL = ['1_purch_copia.txt', '2_archivo de prueba_copia.txt', '3_archivo de prueba_copia.txt', '4_admitted_copia.txt', 
                  '5_archivo de prueba_copia.txt', '6_archivo de prueba_copia.txt', '7_archivo de prueba_copia.txt', '8_archivo de prueba_copia.txt', '9_archivo de prueba_copia.txt', '10_archivo de prueba_copia.txt', 
                  '11_archivo de prueba_copia.txt', '12_archivo de prueba_copia.txt', '13_archivo de prueba_copia.txt']

CSV_AUTOMATICOS_LOCAL = ['1_purch.csv', '2_archivo de prueba.csv', '3_archivo de prueba.csv', '4_admitted.csv', 
                  '5_archivo de prueba.csv', '6_archivo de prueba.csv', '7_archivo de prueba.csv', '8_archivo de prueba.csv', '9_archivo de prueba.csv', '10_archivo de prueba.csv', 
                  '11_archivo de prueba.csv', '12_archivo de prueba.csv', '13_archivo de prueba.csv']



CL01, CL07, CL82 = 'CL01', 'CL07', 'CL82'
AL02, AL04, AL05, AL22, AL23, AL38, AL03, AL06, AL21 = 'AL02', 'AL04', 'AL05', 'AL22', 'AL23', 'AL38', 'AL03', 'AL06', 'AL21'

types_of_encoding = ["utf8", "cp1252"]
ALMACENES = [AL02, AL04, AL05, AL22, AL23, AL38, AL03, AL06, AL21]
CENTROS = [CL01, CL07, CL82]


def lista_rutas_validas(carpeta, lista_nombre_archivos):
    """
    Lista que toma como parametros ubicacion de carpeta y lista de nombres de archivos a copia  y
    retorna lista con ubicaciones validas
    """
    lista_rutas_validas = list()
    for nombre_valido in lista_nombre_archivos:
        nombre_valido = os.path.join(carpeta, nombre_valido)
        lista_rutas_validas.append(nombre_valido)
    return lista_rutas_validas



def copiar_archivos(ruta_inicio, ruta_final):
    """
    Funcion que toma como paremetros dos listas con ubicaciones
    de archivos (originales y copia) y luego realiza
    la copia de los archivos seleccionados.
    """
    count = 0
    for archivo_original, archivo_copia in zip(ruta_inicio, ruta_final):
        shutil.copy(archivo_original, archivo_copia)
        count = count + 1
        print('!Archivo' + ' ' + str(count) + ' ' + 'copiado!')



#Extraemos cabecera de documento:
def lector_stock_diferenciado(txt_file, encoding ='ascii'):# 'cp850' funciona encoding ='utf-8'
    """
    Funcion que toma como parametro txt 'local_stock_diario.txt' y reordena
    documento en una lista de lista de lista.
    """
    with open(txt_file) as stock_diario:
        tabla = list()
        # Identificamos cabecera o primera linea y la guardamos en tabla resultante.
        cabecera = stock_diario.readline().rstrip()
        tabla.append(cabecera.split(';'))
        counter = 0
        for linea in stock_diario:
            linea = linea.rstrip()
            linea = linea.split(';')
            # Guardamos lienas interesantes que cumplen con los criteriarios IF anidados.
            if linea[1] in CENTROS:
                if linea[2] in ALMACENES:
                    tabla.append(linea)    
        return tabla



def lector_texto_diferenciado(txt_file, separator):
    """
    Funcion texto que toma centros Coquimbo y AP. txMB25
    """
    for encoding_type in types_of_encoding:
        with codecs.open(txt_file, encoding = encoding_type, errors ='replace') as file:
            tabla = list()
            # Identificamos cabecera o primera linea y la guardamos en tabla resultante.
            cabecera = file.readline().rstrip()
            tabla.append(cabecera.split(separator))
            counter = 0
            for linea in file:
                linea = linea.rstrip()
                linea = linea.split(separator)
                # Guardamos lienas interesantes que cumplen con los criteriarios IF anidados.
                # Guardamos lienas interesantes que cumplen con los criteriarios IF anidados.
#                 if CL01 in linea or CL07 in linea or CL82 in linea:
#                     if linea[1] == AL02 or linea[1] == AL04 or linea[1] == AL05:
                tabla.append(linea)   
        return tabla



def lector_texto(txt_file, separator):
    for encoding_type in types_of_encoding:
        with codecs.open(txt_file, encoding = encoding_type, errors ='replace') as file:
            tabla = list()
            # Identificamos cabecera o primera linea y la guardamos en tabla resultante.
            cabecera = file.readline().rstrip()
            tabla.append(cabecera.split(separator))
            counter = 0
            for linea in file:
                linea = linea.rstrip()
                linea = linea.split(separator)
                # Guardamos lienas interesantes que cumplen con los criteriarios IF anidados.
#                 if CL01 in linea or CL07 in linea or CL82 in linea:
                tabla.append(linea)
        return tabla
                

def ecritor_csv(tabla, nombre_csv):
    """
    Funcion que recibe como parametro una lista de listas y nombre de archivo a guarar.
    retorna archivo csv con el nombre elegido
    """
    for encoding_type in types_of_encoding:
        with open(nombre_csv, 'w', newline='', encoding = encoding_type, errors ='replace') as file:
            writer = csv.writer(file, delimiter=';', quotechar='"',
                                       quoting=csv.QUOTE_NONNUMERIC)
            for linea in tabla:
                writer.writerow(linea)
    

    



# #Creando listas ubicaciones:
# #Creamos nuevas listas que concatenan direccion y nombre de archivo a copiar o crear, estas se crean usando funcion "lista rutas validas"
lista_ubicaciones_originales = lista_rutas_validas(carpeta_referencia, TXT_ORIGINALES)
lista_ubicaciones_copia = lista_rutas_validas(carpeta_bases_jobs, TXT_COPIA_LOCAL)

#Creando listas ubicaciones:
lista_ubicaciones_txt_a_copiar = lista_rutas_validas(carpeta_bases_jobs, TXT_COPIA_LOCAL)
lista_ubicaciones_csv_a_grabar = lista_rutas_validas(carpeta_bases_csv, CSV_AUTOMATICOS_LOCAL)

# Corriendo funciones:
#Copiando Arcivos
copiar_archivos(lista_ubicaciones_originales, lista_ubicaciones_copia)

# #Compras
tabla = lector_texto(lista_ubicaciones_txt_a_copiar[0], ';')
ecritor_csv(tabla, lista_ubicaciones_csv_a_grabar[0])

# #Compras Hes Has 
tabla = lector_texto(lista_ubicaciones_txt_a_copiar[1], ';')
ecritor_csv(tabla, lista_ubicaciones_csv_a_grabar[1])
#
# #Compras Control de entregas 
tabla = lector_texto(lista_ubicaciones_txt_a_copiar[2], ';')
ecritor_csv(tabla, lista_ubicaciones_csv_a_grabar[2])

# #Documento Compra
tabla = lector_texto(lista_ubicaciones_txt_a_copiar[3], ';')
ecritor_csv(tabla, lista_ubicaciones_csv_a_grabar[3])

# #Factura
tabla = lector_texto(lista_ubicaciones_txt_a_copiar[4], ';')
ecritor_csv(tabla, lista_ubicaciones_csv_a_grabar[4])

# #MB25 (Reservas)
tabla = lector_texto(lista_ubicaciones_txt_a_copiar[5], ';')
ecritor_csv(tabla, lista_ubicaciones_csv_a_grabar[5])

# #MB51 (Historial)
tabla = lector_texto(lista_ubicaciones_txt_a_copiar[6], ';')
ecritor_csv(tabla, lista_ubicaciones_csv_a_grabar[6])

# # #MM60 (Historial)
tabla = lector_texto(lista_ubicaciones_txt_a_copiar[7], ';')#7
ecritor_csv(tabla, lista_ubicaciones_csv_a_grabar[7])

# #Solped
tabla = lector_texto(lista_ubicaciones_txt_a_copiar[8], ';')#8
ecritor_csv(tabla, lista_ubicaciones_csv_a_grabar[8])

# #Stock Diario
# FUNCION DIFERENCIADA.
tabla = lector_stock_diferenciado(lista_ubicaciones_txt_a_copiar[9])#9
ecritor_csv(tabla, lista_ubicaciones_csv_a_grabar[9])

# #ZMM_COMPRAS_CL
tabla = lector_texto(lista_ubicaciones_txt_a_copiar[10], ';')#10
ecritor_csv(tabla, lista_ubicaciones_csv_a_grabar[10])

# #Contratos Marco
tabla = lector_texto(lista_ubicaciones_txt_a_copiar[11], ';')#11
ecritor_csv(tabla, lista_ubicaciones_csv_a_grabar[11])

# #Reservas
# FUNCION DIFERENCIADA.
tabla = lector_texto_diferenciado(lista_ubicaciones_txt_a_copiar[12], ';')#12
ecritor_csv(tabla, lista_ubicaciones_csv_a_grabar[12])
