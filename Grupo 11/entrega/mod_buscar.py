# -*- encoding: utf-8 -*-
import mod_cargar
import mod_desencriptar
import mod_encriptar
import archivo



def buscarNombre(lista,nom):
    ''' Función que recibe un nombre e imprime los datos de un cumpleaños con el mismo nombre de persona'''

    ok = False
    for dic in lista: #recorrer lista de cumpleaños
        if dic['nombre']== nom: #encuentra igualdad de nombre
            fecha = mod_desencriptar.desencriptar(dic['fecha']) #MmDd
            txt = '\nFecha: ' + fecha[2:] + '-' + fecha[0:2]
            txt += ' | nombre: ' + mod_desencriptar.desencriptar(dic['nombre'])
            txt += ' | ' + mod_desencriptar.desencriptar(dic['contacto']['tipo'])
            txt += ': ' + mod_desencriptar.desencriptar(dic['contacto']['dato'])
            print txt #imprime los datos del cumpleaños
            ok = True
    if ok == False:
        print 'No se encontraron resultados!'
        

        
def buscarFecha(lista,fecha):
    ''' Funcion que recibe fecha de cumpleaños y busca la coincidencia con los cumpleaños almacenados'''
    ok = False
    for dic in lista: #recorre lista de cumpleaños
        if dic['fecha'] == fecha: #encuentra igualdad de fecha
            txt = '\nFecha: '+ mod_desencriptar.desencriptar(dic['fecha'])[2:] + '-' + mod_desencriptar.desencriptar(dic['fecha'])[:2]
            txt += ' ' + mod_desencriptar.desencriptar(dic['nombre'])
            txt += ' ' + mod_desencriptar.desencriptar(dic['contacto']['tipo'])
            txt += ' ' + mod_desencriptar.desencriptar(dic['contacto']['dato'])
            print txt #imprime los datos del cumpleaños
            ok = True
    if ok == False:
        print 'No se encrontraron resultados!'

        
            
def buscar(lista):
    " Función que realiza busqueda de cumpleaños por nombre o por fecha "

    print '*'*50 #separador de menues
    print '\n\nBuscar cumpleaños:\n'
    
    print '1-Buscar por Nombre'
    print '2-Buscar por Fecha'
    print '0-Salir\n'
    
    opc = raw_input('INGRESE OPCION: ')
    print '\n'
    
    while opc != '0':
        if opc == '1': #Busqueda por nombre
            nom = raw_input('Ingrese el Nombre: ')
            print '\n'
            nom = mod_encriptar.encriptar(nom) #encriptar nombre ingresado
            buscarNombre(lista, nom) #realizar busqueda en la lista
        elif opc == '2': #Busqueda por fecha 
            print 'Ingrese fecha\n(Con dos digitos para el dia y el mes\n'
            dia = input('Dia: ')
            mes = raw_input('Mes: ')
            valido = mod_cargar.validar_fecha(dia, mes) #valida fecha ingresada
            if valido == True: #fecha valida
                fecha = mes + str(dia) #formato de busqueda de fecha
                print fecha
                fecha = mod_encriptar.encriptar(fecha)
                buscarFecha(lista, fecha) #realiza busqueda en la lista
            else: #fecha invalida
                print 'Fecha incorrecta!'
        print '*'*50 #separador de menues
        print '\n\nBuscar cumpleaños:\n'
    
        print '1-Buscar por Nombre'
        print '2-Buscar por Fecha'
        print '0-Salir\n'
        opc = raw_input('\n\nINGRESE OPCION: ')
        print '\n'
