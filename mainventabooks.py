import funciones as fu

while True:
    fu.limpiarpantalla
    fu.printv("SISTEMA VENTABOOKS")
    fu.printv("******************")
    print("1) Guardar")
    print("2) Búsqueda")
    print("3) Certificados")
    print("0) Salir")
    opcion = int(input("Seleccione: "))

    if opcion==0:
        fu.printv("Adiós")
        break
    elif opcion==1:
        fu.printv("GUARDAR")
    elif opcion==2:
        fu.printv("BÚSQUEDA")
    elif opcion==3:
        fu.printv("CERTIFICADOS")
        print("1) Criticas")
        print("2) Detalles")
        cert = int(input("Seleccione: "))

        if cert==1:
            fu.printv("Certificado Criticas")
        elif cert==2:
            fu.printv("Certificado Detalle")
        else:
            fu.printr("Opción Inválida")
    else:
        fu.printr("Opción No Válida")