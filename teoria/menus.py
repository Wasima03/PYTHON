opcion=input("P para jugar, C para configurar o X para salir ")

match opcion:
    case "P" | "p" | "j" | "J":
        print("Has elegido Jugar")
    case "C":
        print("Has elegido Configurar")
    case "X":
        print("Has elegido Salir")
    case _:  #default
        print("Opción no válida")
print("Fin del menú")