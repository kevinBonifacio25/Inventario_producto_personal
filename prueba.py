import crud


def registrar_clientes(lista_clientes):
   
    while True:
        try:
            cant_clientes = int(input("escriba la cantidad de clientes a ingresar: "))
            
            if cant_clientes<=0:
                print("ingrese un numero positivo")
                continue
            break
            
        except ValueError:
            print("solo se admiten numeros")

       
    for cliente in range(cant_clientes):
        print(f"\nRegistro del cliente {cliente+1}")
          
        clientes = {

                "id": int(input("Ingrese el ID del cliente: ")),
                "nombre": input("Ingrese el nombre del cliente: "),
                "edad": int(input("Ingrese la edad del cliente: ")),
                "membresia": input("Ingrese el tipo de membresia del cliente: "),
                "estado": input("Ingrese el estado del cliente: ")
                }
        
        lista_clientes.append(clientes)
        crud.guardar_datos(lista_clientes)
        
    print(f"Esta es la informacion de los clientes, {lista_clientes}")


def listar_clientes(lista_clientes):

    for i,  cliente in enumerate(lista_clientes, start=1):
        print(f"El cliente numero {i} es: Su nombre es {cliente["nombre"]}, el id es {cliente["id"]} ,la edad es {cliente["edad"]}, su tipo de membresia es {cliente["membresia"]}, y su estado es: {cliente["estado"]}.")


def buscar_clientes_por_id(lista):
    """Ingresar el numero de ID del cliente que necesita buscar"""
    try:
        id_cliente_buscar = int(input("Ingrese el ID del cliente a buscar: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return 

    for cliente in lista:
        if cliente.get("id") == id_cliente_buscar:
            print(f"El cliente con ID {id_cliente_buscar} es: {cliente}")
            return cliente
        
    print(f"No se encontró ningún cliente con ID {id_cliente_buscar}.")
    return 


def actualizar_info_clientes (lista_clientes):

    try:
        id_cliente_actualizar = int(input("Ingrese el ID del cliente para actualizar informacion: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return 
    
    encontrado = False
    for cliente in lista_clientes:
        if cliente.get("id") == id_cliente_actualizar:          
            cliente["membresia"] = input("Ingrese la nueva membresia del cliente: ")  # Actualiza el valor directamente
            print(f"El cliente con ID {id_cliente_actualizar} cambio de membresia a tipo: {cliente['membresia']}")
            crud.guardar_datos(lista_clientes)
            encontrado = True
            break
    if not encontrado:
        print("Cliente no encontrado.")

        
    return


def eliminar_cliente (lista_clientes):   

    try:
        id_cliente_para_eliminar = int(input("Ingrese el ID del cliente para actualizar informacion: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return 
    
   
    for cliente in lista_clientes:
        #te elimina el objeto cliente
        if cliente.get("id") == id_cliente_para_eliminar: 
            lista_clientes.remove(cliente) #elimino el cliente por medio del id
            print(f"Cliente con ID {id_cliente_para_eliminar} eliminado.")
            print(f"La lista de clientes actualizada es: {lista_clientes}")
            crud.guardar_datos(lista_clientes)
            break
        else:
            print("No se encontró ningún cliente con ese ID.")


    return 

