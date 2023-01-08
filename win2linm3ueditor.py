import sys

def changePath(nombreArchivoOrigen, nuevaRuta, nombreArchivoDestino):

    print('CONVIRTIENDO LISTA DE REPRODUCCION')

    archivo = open(nombreArchivoOrigen, "r", encoding='utf-8')
    contenido = archivo.read()

    nuevoArchivo = open(nombreArchivoDestino, 'a', encoding='utf-8')
    
    lineas=contenido.split(sep='\n')

    for numeroDeLinea in range(len(lineas)):
        
        linea = str(lineas[numeroDeLinea])

        if linea[0] != '#':
            carpetas = linea.split(sep="\\")
            carpetas[0] = nuevaRuta

            nuevaLinea = ""
            for nivelDirectorio in range(len(carpetas)):
                nuevaLinea = nuevaLinea + "/" + str(carpetas[nivelDirectorio])

            linea = nuevaLinea
     
        print(linea)
        nuevoArchivo.write(linea + '\n')

    archivo.close()
    nuevoArchivo.close()


def removeFirstSlash(ruta):

    if ruta[0] == '/':
        ruta = ruta[1:]
        return ruta

def main():

    origen = sys.argv[1]
    ruta =  removeFirstSlash(sys.argv[2])
    destino = sys.argv[3]

    changePath(origen, ruta,destino)

    

if __name__ == '__main__':
    main()


