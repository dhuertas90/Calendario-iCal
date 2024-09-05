# -*- coding: utf-8 -*-

def desencriptar(cadena):
    '''Función que recibe una cadena de binarios separados por un carácter especial,
    separa la cadena en una lista y retorna la cadena desencriptada.'''
    
    dato_desencriptado = ''
    lista_script = cadena.split('-')  # Separa la cadena en una lista de códigos binarios
    for caracter in lista_script:  # Recorre cada elemento de la lista
        if caracter:  # Asegura que el carácter no esté vacío
            codigo_ascii = int(caracter, 2)  # Convierte el binario a código ASCII
            dato_desencriptado += chr(codigo_ascii)  # Convierte el código ASCII a carácter
    return dato_desencriptado
