import mod_cargar
import mod_desencriptar
import mod_encriptar
import time
import os

def buscarNombre(lista, nom):
    '''Función que recibe un nombre e imprime los datos de un cumpleaños con el mismo nombre de persona'''
    
    resultados = []  # Lista para acumular los resultados de búsqueda
    
    # Limpiar la pantalla (compatible con Windows y Unix)
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Espere por favor...")

    # Esperar 3 segundos
    time.sleep(3)

    for dic in lista:  # Recorrer lista de cumpleaños
        if mod_desencriptar.desencriptar(dic['nombre'].lower()) == nom.lower():  # Encuentra igualdad de nombre
            fecha = mod_desencriptar.desencriptar(dic['fecha'])  # MmDd
            txt = '\nFecha: ' + fecha[2:] + '-' + fecha[0:2]
            txt += ' | Nombre: ' + nom.capitalize()
            txt += ' | ' + mod_desencriptar.desencriptar(dic['contacto']['tipo'])
            txt += ': ' + mod_desencriptar.desencriptar(dic['contacto']['dato'])
            resultados.append(txt)  # Añade el resultado a la lista
    
    if resultados:
        print('Resultado de búsqueda:\n')
        for resultado in resultados:  # Imprime cada resultado
            print(resultado)
    else:
        print('¡No se encontraron resultados!')
        # Esperar 3 segundos
        time.sleep(3)

def buscarFecha(lista, fecha):
    '''Función que recibe fecha de cumpleaños y busca la coincidencia con los cumpleaños almacenados'''
    
    resultados = []  # Lista para acumular los resultados de búsqueda
    
    # Limpiar la pantalla (compatible con Windows y Unix)
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Espere por favor...")

    # Esperar 3 segundos
    time.sleep(3)

    for dic in lista:  # Recorre lista de cumpleaños
        if dic['fecha'] == fecha:  # Encuentra igualdad de fecha
            txt = '\nFecha: ' + mod_desencriptar.desencriptar(dic['fecha'])[2:] + '-' + mod_desencriptar.desencriptar(dic['fecha'])[:2]
            txt += ' | Nombre: ' + mod_desencriptar.desencriptar(dic['nombre']).capitalize()
            txt += ' | ' + mod_desencriptar.desencriptar(dic['contacto']['tipo'])
            txt += ': ' + mod_desencriptar.desencriptar(dic['contacto']['dato'])
            resultados.append(txt)  # Añade el resultado a la lista
    
    if resultados:
        print('Resultado de búsqueda:\n')
        for resultado in resultados:  # Imprime cada resultado
            print(resultado)
    else:
        print('¡No se encontraron resultados!')
        # Esperar 3 segundos
        time.sleep(3)


def buscar(lista):
    '''Función que realiza búsqueda de cumpleaños por nombre o por fecha'''
    
    print('*' * 50)  # Separador de menús
    print('\n\nBuscar cumpleaños:\n')

    print('1 - Buscar por Nombre')
    print('2 - Buscar por Fecha')
    print('0 - Salir\n')

    opc = input('INGRESE OPCIÓN: ')
    print('\n')

    while opc != '0':
        if opc == '1':  # Búsqueda por nombre
            nom = input('Ingrese el Nombre: ').strip()
            print('\n')
            buscarNombre(lista, nom)  # Realizar búsqueda en la lista
        elif opc == '2':  # Búsqueda por fecha
            print('Ingrese fecha\n(Con dos dígitos para el día y el mes)\n')
            try:
                dia = int(input('Día: ').strip())
                mes = input('Mes (en formato MM): ').strip()
                valido = mod_cargar.validar_fecha(dia, mes)  # Valida fecha ingresada
                if valido:  # Fecha válida
                    fecha = mes.zfill(2) + str(dia).zfill(2)  # Formato de búsqueda de fecha
                    fecha_encriptada = mod_encriptar.encriptar(fecha)
                    buscarFecha(lista, fecha_encriptada)  # Realiza búsqueda en la lista
                else:  # Fecha inválida
                    print('¡Fecha incorrecta!')
            except ValueError:
                print('¡Entrada inválida! El día debe ser un número entero.')
                # Esperar 3 segundos
                time.sleep(3)
        else:
            print('¡Opción inválida, intente nuevamente!')
            # Esperar 3 segundos
            time.sleep(3)
        
        # Limpiar la pantalla (compatible con Windows y Unix)
        os.system('cls' if os.name == 'nt' else 'clear')

        print('*' * 50)  # Separador de menús
        print('\n\nBuscar cumpleaños:\n')

        print('1 - Buscar por Nombre')
        print('2 - Buscar por Fecha')
        print('0 - Salir\n')
        opc = input('INGRESE OPCIÓN: ').strip()
        print('\n')
