import funciones as fn

trabajadores = []

while True:
    print("Bienvenidos al super de pago de sueldos")
    print("1. Registro trabajador")
    print("2. Listar los trabajadores")
    print("3. Imprimir planilla de sueldos")
    print("4. Salir")
    opcion = int(input("Ingrese opcion: "))

    if opcion == 1:
        fn.registrar_trabajador(trabajadores)

    elif opcion == 2:
        fn.listar_trabajadores(trabajadores)

    elif opcion == 3:
        fn.imprimir_plantilla(trabajadores)

    elif opcion == 4:
        print()
        break
    else:
        print("Opcion no válida, seleccione nuevamente")


