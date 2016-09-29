# -*- encoding: utf-8 -*-
import mod_cargar
import mod_buscar
import mod_borrar
import archivo
import importar_ical

''' Módulo que imprime en pantalla un Menu Principal con opciones para interactuar con un Calendario '''

try:
   lista = archivo.desarchivar('lista_dic.txt')
except IOError:
   f = open('lista_dic.txt', 'wb')
   f.close()
   lista=[]

print '*'*50 #separador de menues 
txt = '\nCalendario de Cumpleaños \n\n' #Creacion del Menu Principal
txt += 'Opciones: \n'
txt += '1: Buscar cumpleaños por fecha o por nombre\n'
txt += '2: Cargar un nuevo cumpleaños\n'
txt += '3: Borrar un cumpleaños\n'
txt += '4: Importar Calendario en formato iCal\n'
txt += '0: Salir'
print txt #Impresion del Menu Principal

opc = raw_input('\n\nIngrese la opcion deseada: ')


while opc != '0': #opcion elegida del 0 al 4
    if opc == '1':
        mod_buscar.buscar(lista)
    elif opc == '2':
        mod_cargar.cargar(lista)
    elif opc == '3':
        mod_borrar.borrar(lista)
    elif opc == '4':
        importar_ical.importar_calendario(lista)
    elif type(opc)==str or opc not in range(1,4):
        print 'Error. Ingrese opcion válida!'
    archivo.archivar(lista,'lista_dic.txt')
    print '*'*50
    print txt
    opc = raw_input('ingrese la opcion deseada: ') 
print '\nAdiós!'
