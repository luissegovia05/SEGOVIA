def crear_persona(personas):
    nombre = input("Ingrese el nombre de la persona: ")
    personas.append(nombre)
    print("Lista de personas:", personas)

def eliminar_persona(personas):
    if not personas:
        print("La lista está vacía no se puede eliminar ningún elemento.")
        return
    
    print("Lista de personas:")
    for idx, persona in enumerate(personas):
        print(f"{idx}. {persona}")
    
    try:
        indice = int(input("Ingrese el índice de la persona a eliminar: "))
        if 0 <= indice < len(personas):
            removed_person = personas.pop(indice)
            print(f"Se ha eliminado a {removed_person}.")
        else:
            print("Índice fuera de rango")
    except ValueError:
        print("Por favor ingrese un número entero válido")
    
    print("Lista actualizada de personas:", personas)

def listar_personas(personas):
    if not personas:
        print("La lista está vacía")
    else:
        print("Lista de personas:")
        for idx, persona in enumerate(personas):
            print(f"{idx}. {persona}")

def buscar_persona(personas):
    nombre = input("Ingrese el nombre de la persona a buscar: ")
    if nombre in personas:
        print(f"La persona '{nombre}' fue encontrada")
    else:
        print(f"La persona '{nombre}' no fue encontrada")

def menu():
    personas = []

    print("\n1 Crear persona")
    crear_persona(personas)

  
    print("\n2 Eliminar persona")
    eliminar_persona(personas)

   
    print("\n3 Listar personas")
    listar_personas(personas)
    
    print("\n4 Buscar persona")
    buscar_persona(personas)

if __name__ == "__main__":
    menu()