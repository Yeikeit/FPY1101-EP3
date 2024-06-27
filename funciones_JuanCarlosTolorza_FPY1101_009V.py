import time
import os
listaDeLibros = []
infoFecha = time.localtime()
fechaActual = f"{infoFecha.tm_mday}-{infoFecha.tm_mon}-{infoFecha.tm_year}"
direccionArchivo = os.getcwd()

def registrar():
    try:
        print("Ingrese los datos para registrar su libro:")
        titulo = input("Título: ")
        autor = input("Autor: ")
        añoDePublicacion = int(input("Año de Publicación: "))
        print("Formato SKU: 6 primeras letras del título del libro-las 3 primeras letras del autor-año de publicación")
        print("Ejemplo: LOSMON-PED-1998")
        sku = input("SKU: ")
        if titulo == "" or autor == "" or añoDePublicacion <= 0 or sku == "":
            print("La informacion provista está incompleta")
            return
        else:
            nuevoLibro = {
               "titulo":titulo,
                "autor": autor,
                "añoDePublicacion": añoDePublicacion,
                "sku": sku,
                # Disponible por defecto
                "estado": "disponible",
                # Sin usuario poseedor por defecto
                "usuarioPoseedor": "",
                # Sin fecha de prestamo por defecto
                "fechaPrestamo":""
            }
            listaDeLibros.append(nuevoLibro)
            print("Libro agregado exitosamente")
    except ValueError:
        print("No se logró agregar el libro")
def prestar():
        print("Ingrese la información del libro que desea solicitar")
        nombreUsuario = input("Ingrese su nombre de usuario:\n")
        skuLibro = input("Ingrese el SKU del libro:\n")
        if nombreUsuario == "" or skuLibro == "":
            print("La informacion provista está incompleta")
            return
        else:
            for libro in listaDeLibros:
                if libro["sku"] == skuLibro and libro["estado"] == "disponible":
                    print("Libro encontrado y disponible para ser prestado.")
                    print("Registrando prestamo.")
                    libro["estado"] = "prestado"
                    libro["usuarioPoseedor"] = nombreUsuario
                    libro["fechaPrestamo"] = fechaActual
                    print("Libro registrado como prestado.")
                elif libro["sku"] != skuLibro:
                    print("No registramos libros con el SKU ingresado")
                    return
                elif libro["estado"] != "disponible":
                    print("El libro está en lista, mas no está disponible de momento.")
                    return
def listar():
    print("TÍTULO\t\tAUTOR\t\tAÑO DE PUBLICACIÓN\t\tSKU")
    for libro in listaDeLibros:
        print(f"{libro["titulo"]}\t\t{libro["autor"]}\t\t{libro["añoDePublicacion"]}\t\t{libro["sku"]}")

def imprmir():
    with open("lista_libros.txt","w") as archivo:
        archivo.write("USUARIO\t\tTITULO\t\tFECHA DEL PRESATAMO\n")
        for libro in listaDeLibros:
            archivo.write(f"{libro["usuarioPoseedor"]}\t\t{libro["titulo"]}\t\t{libro["fechaPrestamo"]}\n")
    print(f"Archivo con la lista de libros generado exitosamente en: {direccionArchivo}" )
    
def menu():
    while True:
        try:
            print("***** Menú *****")
            print("1. Registrar libro\n2. Prestar libro\n3. Listar todos los libros\n4. Imprimir reporte de préstamos\n5. Salir del Programa")
            op = int(input("Ingrese una opción (1-5): "))
            if op == 1:
                registrar()
            elif op == 2:
                prestar()
            elif op == 3:
                listar()
            elif op == 4:
                imprmir()
            elif op == 5:
                print("Saliendo del programa")
                os.system("cls")
                print("Programa finalizado...")
                print("Desarrollado por Juan Carlos Tolorza")
                print("19.859.484-9")
                break
            else:
                print("Opcion invalida, pruebe nuevamente")
        except ValueError:
            print("Opcion ingresada no valida, no cumple con el formato numerico")