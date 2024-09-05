def encriptar(cadena):
    '''Encripta una cadena convirtiendo cada carácter a su representación binaria separada por guiones.'''
    cadena = str(cadena)
    cadena_script = ''  # Cadena a guardar
    for caracter in cadena:
        codigo_asci = ord(caracter)
        binario = bin(codigo_asci)[2:]  # Convertir a binario y quitar el prefijo '0b'
        cadena_script += binario + '-'  # Cadena encriptada
    return cadena_script.rstrip('-')  # Elimina el último guion

def encriptar_dic(dic):
    '''Encripta los valores de un diccionario, manejando diccionarios anidados.'''
    for clave, valor in dic.items():
        if isinstance(valor, dict):  # Comprobar si es un diccionario
            dic[clave] = encriptar_dic(valor)  # Encriptar el diccionario anidado
        else:
            dic[clave] = encriptar(valor)  # Encriptar el valor
    return dic
