# -*- encoding: utf-8 -*-
import mod_encriptar

def validar_fecha(dia,mes):
    ''' Funcion que recibe fecha de cumpleaños y la valida '''
    meses31=set(['01','03','05','07','08','10','12'])
    meses30=set(['04','06','09','11'])
    if dia in range(1,32) and mes in meses31: #valida dia en rango y mes en conjunto
        result=True
        return result
    elif dia in range(1,31) and mes in meses30:	#valida dia en rango y mes en conjunto
        result=True
        return result
    elif dia <= 28 and mes == '02': #valida dia y mes de Febrero
        result=True
        return result
    else: #fecha no existente
        result=False
        return result


            
def cargar(lista):
    ''' Funcion que carga los datos de un cumpleaños '''
    
    cont={'tipo' : '', 'dato' : '' } #diccionario que contiene el tipo y dato del contacto
    dic={'fecha' : '', 'nombre' : '', 'contacto' : cont} #diccionario que contiene fecha, nombre y contacto de un cumpleaños

    print '*'*50 #separador de menues
    print '\nIngrese los datos del cumpleaños:\n'

    dia = input('Dia: ')
    mes = raw_input('Mes: ')
    fecha = validar_fecha(dia, mes) #validar fecha ingresada    
    if fecha == True: #fecha valida y comienza la carga de datos
        dic['fecha'] = mes + str(dia) # formato de fecha en : mmdd
        dic['nombre'] = raw_input ('Nombre:  ')
        print '\nSeleccione tipo de contacto\n' #menu de contacto
        print '\t1 - Email'
        print '\t2 - Teléfono'
        print '\t3 - Celular'
        print '\t4 - Dirección'
        num = input('\nOpción número: ')
    
        if num in range(1,5): #opcion valida
            if num == 1:
                cont['tipo'] = 'mail'
            elif num == 2:
                cont['tipo'] = 'telefono'
            elif num == 3:
                cont['tipo'] = 'celular'
            elif num == 4:
                cont['tipo'] = 'direccion'
                
            cont['dato'] = raw_input('\nIngrese dato: ')
            dic['contacto'] = cont #agrega el diccionario 'cont' en clave 'contacto' del diccionario principal
            dic_encript = mod_encriptar.encriptar_dic(dic) #encripta el diccionario principal, es decir, el cumpleaños       
            lista.append(dic_encript) #agrega un cumpleaños a la lista
            print '\n\tEL CUMPLEAÑOS SE CARGO EXITOSAMENTE!\n'
        else: #opcion no valida
            print 'OPCION INVALIDA INTENTELO NUEVAMENTE!'
            
    else: #fecha invalida
        print '\n\tFECHA INVALIDA INTENTELO NUEVAMENTE!'
