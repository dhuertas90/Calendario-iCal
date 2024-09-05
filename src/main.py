# -*- encoding: utf-8 -*-
from  src import cargar, buscar, borrar, importar_calendario, archivar, desarchivar


def main():
    ''' Módulo que imprime en pantalla un Menu Principal con opciones para interactuar con un Calendario '''

    try:
        lista = desarchivar('lista_dic.txt')
    except IOError:
        with open('lista_dic.txt', 'wb') as f:
            lista = []

    print('*' * 50)  # separador de menues
    txt = '\nCalendario de Cumpleaños \n\n'  # Creación del Menu Principal
    txt += 'Opciones: \n'
    txt += '1: Buscar cumpleaños por fecha o por nombre\n'
    txt += '2: Cargar un nuevo cumpleaños\n'
    txt += '3: Borrar un cumpleaños\n'
    txt += '4: Importar Calendario en formato iCal\n'
    txt += '0: Salir'
    print(txt)  # Impresión del Menu Principal

    opc = input('\n\nIngrese la opción deseada: ')

    while opc != '0':  # opción elegida del 0 al 4
        if opc == '1':
            buscar(lista)
        elif opc == '2':
            cargar(lista)
        elif opc == '3':
            borrar(lista)
        elif opc == '4':
            importar_calendario(lista)
        elif not opc.isdigit() or int(opc) not in range(1, 5):
            print('Error. ¡Ingrese opción válida!')
        archivar(lista, 'lista_dic.txt')
        print('*' * 50)
        print(txt)
        opc = input('\nIngrese la opción deseada: ')
        
    print('\n¡Adiós!')

if __name__ == "__main__":
    main()