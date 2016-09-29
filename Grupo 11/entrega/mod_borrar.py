# -*- encoding: utf-8 -*-

import mod_desencriptar
import mod_encriptar
import archivo

def borrar_dic(lista,nombre,tipo,contacto):
    ''' Funcion que borra cumpleaños del diccionario '''
    
    i=0
    encontrado = False
    while encontrado == False: #Buscar persona en el diccionario
        dic = lista[i]
        if dic['nombre'] == nombre:
            if dic['contacto']['tipo'] == tipo:
                if dic['contacto']['dato'] == contacto:
                    del lista[i] #Elimina cumpleaños
                    encontrado = True
                    return encontrado
        else:
            i += 1
    

        
def borrar(lista):
    ''' Funcion que busca el cumpleaños a borrar '''
    
    print 'Ingrese datos\n' #Comienzo de ingreso de datos personales

    nombre = raw_input('Nombre: ')
    nombre = mod_encriptar.encriptar(nombre)

    i=0
    for dic in lista: #busco el cumpleaños en la lista
        if nombre == dic['nombre']:
            txt = 'Desea borrar el cumpeaños de: '
            txt += '' + mod_desencriptar.desencriptar(nombre)
            txt += ' con '+ mod_desencriptar.desencriptar(dic['contacto']['tipo'])
            txt +=' ' +  mod_desencriptar.desencriptar(dic['contacto']['dato'])
            print txt
            res = raw_input('Ingrese:\n S -Para confirmar \n N -Para cancelar\n Opcion: ')
            if res == 's' or res == 'S':
                del lista[i] #Elimina cumpleaños!
                print '\n\tCumpleaños eliminado exitosamente!\n'
                break
            elif res == 'n' or res == 'N':
                print '\n\tNo se pudo eliminar el cumpleaños.\n'
                break
        else:
            i += 1 #posicion siguiente cumpleaños en la lista
            
