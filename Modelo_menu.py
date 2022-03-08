def menu():
    while True: 
        print("""CONVERSOR DE SEGUNDOS\n\n
        1 - Ingresar Segundos\n
        2 - Salir\n
        """)
        try:
            opcion = int(input("Ingrese una opcion: "))
        except:
            print('Hay un error, debe ingresar 1 o 2!\n')
            menu() # VUELVO A MENU
        try:    
            if opcion == 1:
                seconds = int(input('Ingrese los segundos: '))
                format_duration(seconds) #para referir la variable 'seconds' a otra funcion
            elif opcion == 2:
                break
        except:
            print('Hay un error, debe ingresar un Numero entero!\n')
            seconds = int(input('Ingrese los segundos: ')) #VUELVO A PEDIR LOS SEGUNDOS
            format_duration(seconds) 
    
    return
    
menu()