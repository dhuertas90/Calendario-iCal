# -*- encoding: utf-8 -*-

import mod_desencriptar
import mod_encriptar
import os
import time

# def borrar_dic(lista, nombre, tipo, contacto):
#     '''Función que borra cumpleaños del diccionario'''

#     encontrado = False
#     i = 0
#     while not encontrado and i < len(lista):  # Buscar persona en el diccionario
#         dic = lista[i]
#         if dic['nombre'] == nombre and dic['contacto']['tipo'] == tipo and dic['contacto']['dato'] == contacto:
#             del lista[i]  # Elimina cumpleaños
#             encontrado = True
#         else:
#             i += 1
#     return encontrado

def borrar(lista):
    '''Función que busca el cumpleaños a borrar'''

    # Limpiar la pantalla (compatible con Windows y Unix)
    os.system('cls' if os.name == 'nt' else 'clear')

    print('Ingrese los datos solicitados\n')  # Comienzo de ingreso de datos personales

    nombre = input('Nombre: ')
    nombre = mod_encriptar.encriptar(nombre)

    encontrado = False  # Variable para verificar si se encontró el cumpleaños

    # Limpiar la pantalla (compatible con Windows y Unix)
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Espere por favor...")

    # Esperar 3 segundos
    time.sleep(3)

    for i, dic in enumerate(lista):  # Busco el cumpleaños en la lista
        if nombre == dic['nombre']:
            txt = f'Desea borrar el cumpleaños de: {mod_desencriptar.desencriptar(nombre)} con {mod_desencriptar.desencriptar(dic["contacto"]["tipo"])} {mod_desencriptar.desencriptar(dic["contacto"]["dato"])}'
            print(txt)
            res = input('Ingrese:\n S -Para confirmar \n N -Para cancelar\n Opción: ')
            if res.lower() == 's':
                del lista[i]  # Elimina cumpleaños
                print('\n\tCumpleaños eliminado exitosamente!\n')
                encontrado = True
                break
            elif res.lower() == 'n':
                print('\n\tNo se pudo eliminar el cumpleaños.\n')
                encontrado = True
                break

    if not encontrado:
        print('\n\tNo se encontró ningún cumpleaños con el nombre ingresado.\n')
        # Esperar 3 segundos
        time.sleep(3)