# -*- coding: utf-8 -*-

import mod_desencriptar
import mod_cargar

def fecha_dtend_ical(cadena):
    '''Función que le suma un día más a la fecha de cumpleaños
    para colocarla en el texto del archivo .ical como fecha de fin del evento (zona horaria GM+3)'''

    mes = cadena[:2]  # separo el mes de la cadena 
    dia = cadena[2:]  # separo el día de la cadena
    dia = int(dia)  # convierto en entero el día
    
    dia += 1  # sumo un día más al día del cumpleaños
    
    fecha = mod_cargar.validar_fecha(dia, mes)  # valido la fecha con el día sumado en 1 
    if not fecha:  # día fuera del rango del mes
        dia = '01'  # inicializo el día
        mes = int(mes)  # convierto el mes en 'entero'
        if mes == 12:
            mes = '01'  # si el mes es 12, inicializo al primer mes del año
        else:
            mes += 1  # si el mes no es 12, sumo 1 al mes
            mes = str(mes).zfill(2)  # convierto el mes a 'string' y le añado un cero a la izquierda si es necesario
        fecha = mes + dia  # concateno la fecha (fin del evento)
    else:  # día dentro del rango del mes
        fecha = mes + str(dia).zfill(2)  # concateno la fecha (fin del evento), asegurando que el día tenga dos dígitos
    return fecha  # retorno fecha fin del evento


def importar_calendario(lista):
    '''Función que importa los cumpleaños a un archivo .ics'''

    with open('calendar.ics', 'w') as f:
        linea = 'BEGIN:VCALENDAR\nVERSION:2.0\n'
        for dic in lista:  # para cada cumpleaños en la lista
            linea += 'BEGIN:VEVENT\nCATEGORIES:MEETING\nSTATUS:TENTATIVE\n'
            linea += 'DTSTART:2013' + mod_desencriptar.desencriptar(dic['fecha']) + 'T030000Z\n'
            fecha_fin = fecha_dtend_ical(mod_desencriptar.desencriptar(dic['fecha']))
            linea += 'DTEND:2013' + fecha_fin + 'T025959Z\n'
            linea += 'SUMMARY:Cumpleaños de ' + mod_desencriptar.desencriptar(dic['nombre']) + '\n'
            linea += 'DESCRIPTION:Material de Gerardo Sosa y David Huertas\n'
            linea += 'END:VEVENT\n'
        linea += 'END:VCALENDAR'
        f.write(linea)
    print('Se creó correctamente el archivo calendar.ics')
