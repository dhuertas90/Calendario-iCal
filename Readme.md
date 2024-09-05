# Calendario de Cumpleaños

Este es un programa de consola hecho en Python que permite gestionar un calendario de cumpleaños. A través de un menú interactivo, los usuarios pueden buscar, agregar, borrar y cargar cumpleaños desde un archivo iCal.

## Características
- Buscar cumpleaños: Puedes buscar cumpleaños por nombre o fecha.
- Cargar cumpleaños: Permite añadir nuevos cumpleaños a la lista.
- Borrar cumpleaños: Elimina cumpleaños de la lista.
- Importar desde iCal: Puedes importar un calendario desde un archivo en formato iCal (.ics).
- Guardar y cargar datos: Los datos se guardan automáticamente en un archivo lista_dic.txt y se cargan al iniciar el programa.

## Requisitos
- Python 3.x
- Módulos locales:
  - cargar: Función para añadir cumpleaños a la lista.
  - buscar: Función para buscar cumpleaños.
  - borrar: Función para eliminar cumpleaños de la lista.
  - importar_calendario: Función para importar cumpleaños desde un archivo iCal.
  - archivar: Función para guardar los datos en un archivo.
  - desarchivar: Función para cargar los datos desde un archivo.

## Instalación
Clona este repositorio o descarga el código fuente.
Asegúrate de tener Python 3 instalado.
Coloca el archivo lista_dic.txt en la misma carpeta donde se encuentra el script, o el programa lo creará al iniciar.

## Uso
Ejecuta el programa principal main.py desde la terminal:
python main.py

A continuación, se mostrará un menú con las siguientes opciones:

- 1: Buscar cumpleaños por nombre o fecha.
- 2: Cargar un nuevo cumpleaños.
- 3: Borrar un cumpleaños.
- 4: Importar un calendario en formato iCal.
- 0: Salir del programa.

### Ejemplo de uso
1. Ejecuta el programa.
2. Selecciona la opción deseada ingresando el número correspondiente.
3. Sigue las instrucciones en pantalla para interactuar con el calendario.

## Archivos
- main.py: Archivo principal que ejecuta el programa.
- lista_dic.txt: Archivo donde se guardan los cumpleaños (se crea automáticamente si no existe).
- src/: Carpeta con los módulos auxiliares para cargar, buscar, borrar y archivar cumpleaños.

## Autor
David Huertas - Seminario de lenguaje de Python 2013 UNLP

