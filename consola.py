


def menuPrincipal():
    print("========================== MENU PRINCIPAL===================================")
    print("1- LISTADO DE ALBUN POR ARTISTA ")
    print("2- LISTADO DE GENERO MUSICAL ")
    print("3- CREACION DE ALBUN  ")
    print("4- ELIMINACION DE ALBUM ")
    print("5- LISTADO DE ALBUN POR ARTISTA ")
    print("6- BUAQUEDA POR NOMBRE DE ALBUM ")
    print("7- SALIR ")
    print("============================================================================")
    opcion = int(input("seleccione una opcion: "))

    if opcion < 1 or opcion > 5:
        print("Opcion incorrecta, Ingrese Nuevamente...")

    elif opcion == 7:
        continuar = False
        print("Gracias por Usar Nuestro Sistema!")
    else:
        ejecutarOpcion(opcion)

def ejecutarOpcion(opcion):
    conectar = Conectar()

    if opcion == 1:
        try:
            albumes = 
            if len(albumes) > 0:
                pass

            else:
                print("No se encontraron Albumes...")

        except:
            print("Ocurrio un error...")

    elif opcion == 2:
        pass
    elif opcion == 3:
        pass
    elif opcion == 4:
        pass
    elif opcion == 5:
        pass
    elif opcion == 6:
        pass
    elif opcion == 7:
        pass
    else:
        print("Opcion mo Valida")
        

menuPrincipal()