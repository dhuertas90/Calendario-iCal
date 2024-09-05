import mod_encriptar

def validar_fecha(dia, mes):
    '''Función que recibe día y mes y los valida'''
    meses31 = {'01', '03', '05', '07', '08', '10', '12'}
    meses30 = {'04', '06', '09', '11'}
    mes_str = mes.zfill(2)  # Asegura que el mes tenga dos dígitos
    
    if mes_str in meses31:
        if 1 <= dia <= 31:
            return True
        else:
            return False
    elif mes_str in meses30:
        if 1 <= dia <= 30:
            return True
        else:
            return False
    elif mes_str == '02':
        if 1 <= dia <= 28:  # Febrero simplificado, para año bisiesto podrías agregar más lógica
            return True
        else:
            return False
    else:
        return False

def cargar(lista):
    '''Función que carga los datos de un cumpleaños'''
    
    cont = {'tipo': '', 'dato': ''}  # Diccionario que contiene el tipo y dato del contacto
    dic = {'fecha': '', 'nombre': '', 'contacto': cont}  # Diccionario que contiene fecha, nombre y contacto de un cumpleaños

    print('*' * 50)  # Separador de menús
    print('\nIngrese los datos del cumpleaños:\n')

    try:
        dia = int(input('Día: '))
        mes = input('Mes (en formato MM): ')
        
        if not (1 <= dia <= 31):
            raise ValueError('Día fuera del rango permitido.')
        
        fecha_valida = validar_fecha(dia, mes)
        
        if fecha_valida:  # Fecha válida y comienza la carga de datos
            dic['fecha'] = mes.zfill(2) + str(dia).zfill(2)  # Formato de fecha en : mmdd
            dic['nombre'] = input('Nombre:  ').lower()
            print('\nSeleccione tipo de contacto\n')  # Menú de contacto
            print('\t1 - Email')
            print('\t2 - Teléfono')
            print('\t3 - Celular')
            print('\t4 - Dirección')
            num = int(input('\nOpción número: '))
    
            if num in range(1, 5):  # Opción válida
                tipo_contacto = {1: 'mail', 2: 'telefono', 3: 'celular', 4: 'direccion'}
                cont['tipo'] = tipo_contacto[num]
                cont['dato'] = input('\nIngrese dato: ')
                dic['contacto'] = cont  # Agrega el diccionario 'cont' en clave 'contacto' del diccionario principal
                dic_encript = mod_encriptar.encriptar_dic(dic)  # Encripta el diccionario principal, es decir, el cumpleaños       
                lista.append(dic_encript)  # Agrega un cumpleaños a la lista
                print('\n\t¡EL CUMPLEAÑOS SE CARGÓ EXITOSAMENTE!\n')
            else:  # Opción no válida
                print('¡OPCIÓN INVÁLIDA, INTÉNTELO NUEVAMENTE!')
        else:  # Fecha inválida
            print('\n\t¡FECHA INVÁLIDA, INTÉNTELO NUEVAMENTE!')
    except ValueError as ve:
        print(f'Error: {ve}')
    except Exception as e:
        print(f'Ocurrió un error inesperado: {e}')
