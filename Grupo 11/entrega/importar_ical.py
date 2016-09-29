# -*- coding: utf-8 -*-

import mod_desencriptar
import mod_cargar


def fecha_dtend_ical(cadena):
    ''' Funcion que le suma un dia mas a la fecha de cumpleaños
    para colocarla en el texto del archivo .ical como fecha de fin del evento (zona horaria GM+3)'''

    mes = cadena[:2] #separo el mes de la cadena 
    dia = cadena[2:] #separo el dia de la cadena
    dia = int(dia) #convierto en entero el dia
    
    dia += 1 # sumo un dia mas a el dia del cumpleaños
    
    fecha = mod_cargar.validar_fecha(dia, mes) #valido la fecha con el dia sumado en 1 
    if fecha == False: # dia fuera del rango del mes
        dia = '01' #inicializo la fecha
        mes = int(mes) #convierto el mes en 'entero'
        if mes == 12:
            mes = '01' # el mes es 12, entonces inicializo a primer mes del año
        else:
            mes += 1 # el mes no es 12, entonces le sumo 1 al mes
            mes = str(mes) #convierto el mes a 'string'
        fecha = mes + dia #concateno la fecha (fin del evento)
    else: #dia dentro del rango del mes
        fecha = mes + str(dia) #concateno la fecha (fin del evento)
    return fecha # retorno fecha fin del evento


def importar_calendario(lista):
    ''' Función que importa los cumpleaños a un archivo .ics '''

    f = open('calendar.ics','w')
    linea = 'BEGIN:VCALENDAR\nVERSION:2.0\n'
    for dic in lista: # para cada cumpleaños en la lista
        linea += 'BEGIN:VEVENT\nCATEGORIES:MEETING\nSTATUS:TENTATIVE\n'
        linea += 'DTSTART:2013' + mod_desencriptar.desencriptar(dic['fecha']) + 'T030000Z\n'
        fecha_fin = fecha_dtend_ical(mod_desencriptar.desencriptar(dic['fecha']))
        linea += 'DTEND:2013' + fecha_fin + 'T025959Z\n'
        linea += 'SUMMARY:' + 'Cumpleaños de ' + mod_desencriptar.desencriptar(dic['nombre']) + '\n'
        linea += 'DESCRIPTION:Material de Gerardo Sosa y David Huertas\n'
        linea += 'END:VEVENT\n'
    linea += 'END:VCALENDAR'
    f.write(linea)
    f.close()
    print 'Se creo correctamente el archivo calendar.ics'




