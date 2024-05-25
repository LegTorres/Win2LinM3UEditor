import sys

# Creando un metodo para cambiar la ruta de las canciones.
def changePath(nombreArchivoOrigen, nuevaRuta, nombreArchivoDestino):

    print(f'Editando lista de reproduccion:\n {nombreArchivoOrigen}\n\n')

    # Abriendo el archivo de origen y guardando su contenido en la variable contenido.
    archivoOrigen = open(nombreArchivoOrigen, "r", encoding='utf-8')
    contenido = archivoOrigen.read()

    # Crendo en nuevo archivo en modo agregar.
    nuevoArchivo = open(nombreArchivoDestino, 'a', encoding='utf-8')

    # Dividiendo el contenido del archivo origen en sus diferentes lineas
    lineas=contenido.split(sep='\n')

    # Agregando la primera linea del archivo
    print('#EXTM3U')
    nuevoArchivo.write('#EXTM3U\n')

    # Creando un bucle que recorra cada una de las lineas del archivo origen.
    for numeroDeLinea in range(len(lineas) -1):

        # Creando una variable string que almacene el contendo de una sola linea (La correspondiente a cada iteracion del ciclo).
        linea = str(lineas[numeroDeLinea])

        if linea[0] != '#':
            # Creando una lista con los diferentes niveles de directorios de Windows (Separandolos por las barras inclinadas hacia la izq.)
            carpetas = linea.split(sep="\\")
            # Reemplazando el directorio de la unidad Windows por la de Linux.
            carpetas[0] = nuevaRuta

            # Creando una cadena para ir concatenando los diferentes sub-directorios y archivos deseados en la misma linea.
            nuevaLinea = ""
            # Creando un bucle para ir agregando los sub-directorios y archivos a la nueva ruta de la unidad e ir
            # modificando el signo de barra invertida izq por der.
            for nivelDirectorio in range(len(carpetas)):
                nuevaLinea = nuevaLinea + "/" + str(carpetas[nivelDirectorio])

           # linea = nuevaLinea

            print(nuevaLinea)
            nuevoArchivo.write(nuevaLinea + '\n')

    archivoOrigen.close()
    nuevoArchivo.close()
    print(f' \n\nCompletado! Creada lista de reproduccion: {nombreArchivoDestino}.\n\n {str(len(lineas))} lineas procesadas\n\n')

def removeFirstSlash(ruta):

    if ruta[0] == '/':
        ruta = ruta[1:]
        return ruta

def main():

    origen = sys.argv[1]
    #ruta =  removeFirstSlash(sys.argv[2])
    #destino = sys.argv[3]

    ruta = "media/Datos"
    destino = "Linux_PL_" + origen
    changePath(origen, ruta, destino)



if __name__ == '__main__':
    main()


