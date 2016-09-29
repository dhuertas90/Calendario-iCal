# -*- coding: utf-8 -*-

def desencriptar(cadena):
    ''' Funcion que recibe una cadena de binarios separados por un caracter especial,
separa la cadena en una lista y retorna la cadena desencriptada'''

    dato_desencriptado = ''
    lista_script=cadena.split('-') #crea lista de codigos binarios
    for caracter in lista_script: #recorre cada elemento de la lista
        codigo_ascii = int(caracter, 2) #convierte a codigo ascii un elemento
        dato_desencriptado += chr(codigo_ascii) #convierte a string el codigo ascii
    return dato_desencriptado
