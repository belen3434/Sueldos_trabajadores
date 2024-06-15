CARGOS = ["ceo","desarrollador","analista de datos"]

def registrar_trabajador(trabajadores):
    nombre = input("Ingrese nombre y apellido del trabajador: ")
    cargo = input("Ingrese cargo del trabajador (CEO/Desarrollador/Analista de datos)").lower()
    
    while cargo not in CARGOS:
        print("Cargo no existe, intente nuevamente")
        cargo = input("Ingrese cargo del trabajador (CEO/Desarrollador/Analista de datos)").lower()
    sueldoBruto = int(input("Inrese sueldo bruto del trabajador: "))

    #calcular los descuentos
    descuentoSalud = sueldoBruto*0.7
    descuentoAfp = sueldoBruto*0.12
    liquidoPagar = sueldoBruto-descuentoSalud-descuentoAfp

    trabajadores.append({
        "Nombre":nombre,
        "Cargo": cargo,
        "SueldoBruto":sueldoBruto,
        "descuentoSalud": descuentoSalud,
        "DescAfp": descuentoAfp,
        "LiquidoPagar": liquidoPagar
    })

def listar_trabajadores(trabajadores):
    print("Lista de trabajadores")
    for trabajador in trabajadores:
        print(trabajador)
        #print(trabajador["Nombre"]) si quisiera mostrar los nombres de los trabajadores 

def imprimir_plantilla(trabajadores):
    cargoSeleccionado = input("Ingrese cargo para imprimir planilla o bien presione ENTER para seleccionar todos: ").lower()
    if cargoSeleccionado == "":
        trabajadores_a_imprimir = trabajadores
        nombreArchivo = "planilla_todos.txt"
    elif cargoSeleccionado in CARGOS:
        trabajadores_a_imprimir = []
        for trabajador in trabajadores:
            if trabajador["Cargo"] == cargoSeleccionado:
                trabajadores_a_imprimir.append(trabajador)
        nombreArchivo = f"planilla_{cargoSeleccionado}.txt"
    else:
        print("Cargo no valido")
        return
    
    with open(nombreArchivo,"w") as archivo:
        for trabajador in trabajadores_a_imprimir:
            archivo.write(f"Nombre y apellido: {trabajador["Nombre"]}\n")
            archivo.write(f"Cargo: {trabajador["Cargo"]}\n")
            archivo.write(f"Sueldo bruto: {trabajador["SueldoBruto"]}\n")
            archivo.write(f"Descuento de salud: {trabajador["descuentoSalud"]}\n")
            archivo.write(f"Descuento de afp: {trabajador["DescAfp"]}\n")
            archivo.write(f"Liquido a pagar: {trabajador["LiquidoPagar"]}\n\n")
            
    


