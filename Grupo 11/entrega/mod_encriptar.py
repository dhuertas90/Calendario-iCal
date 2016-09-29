

def encriptar(cadena):
    cadena = str(cadena)
    cadena_script = '' #cadena a guardar
    for caracter in cadena:
        codigo_asci = ord(caracter)
        binario = bin(codigo_asci)[2:]
        cadena_script += binario + '-' #cadena encriptada
    return cadena_script[:-1]


def encriptar_dic(dic):
        valores = dic.values()
        claves = dic.keys()
        for indice in range(0,len(dic)):
            if type(valores[indice]) == dict:
                dic_aux = valores[indice]
                dic[claves[indice]] = encriptar_dic(dic_aux)
            else:
                aux = encriptar(valores[indice])
                dic[claves[indice]] = aux
        return dic

