from dao.ciudadano_dao import CiudadanoDAO
from models.ciudadano import Ciudadano

def ver_ciudadanos():  
    try:
        ciudadano_dao = CiudadanoDAO()  
        lista = ciudadano_dao.obtener_todo()

        if len(lista) == 0:
            print("No hay ciudadanos registrados.")
        else:
            for ciudadano in lista:

                print(ciudadano.mostrar_info())
            print("\nConexión exitosa con la base de datos.")
    except Exception as e:
        print("Error al visualizar los ciudadanos.")
        print(e)

def insertar_ciudadano():
    print("\n--- INSERTAR UN NUEVO CIUDADANO ---")
    nombre = input("Escribe el nombre del ciudadano: ")
    a_paterno = input("Escribe el apellido paterno: ")
    a_materno = input("Escribe el apellido materno: ")
    calle = input("Escribe el nombre de la calle: ")
    no_ext_input = input("Escribe el número exterior (deja vacío si no tiene): ")
    

    if no_ext_input.strip() == "":
        no_exterior = None  
    else:
        no_exterior = int(no_ext_input)
        
    barrio = int(input("Escribe el ID del barrio: "))
    id_descuento = int(input("Escribe el ID del descuento: "))

    try:
        ciudadano_dao = CiudadanoDAO()
        ultimo_id = ciudadano_dao.obtener_ultimo_id() + 1
        ciudadano = Ciudadano(ultimo_id, nombre, a_paterno, a_materno, calle, no_exterior, barrio, id_descuento)
        ciudadano_dao.insertar(ciudadano)
        print("Inserción del nuevo ciudadano ha sido exitosa.")
    except Exception as e:
        print("Error al insertar el ciudadano...")
        print(e)

def actualizar_ciudadano():
    try:
        ciudadano_dao = CiudadanoDAO()
        print("\nLista de ciudadanos disponibles:")
        
        lista = ciudadano_dao.obtener_todo()
        for c in lista:
            print(c.mostrar_info()) 
            
        id = int(input("\nSeleccione el id del ciudadano a actualizar: "))
        nombre = input("Escribe el nombre del usuario: ")
        a_paterno = input("Escribe el apellido paterno: ")
        a_materno = input("Escribe el apellido materno: ")
        calle = input("Escribe el nombre de la calle: ")
        no_ext_input = input("Escribe el número exterior (deja vacío si no tiene): ")
        
        if no_ext_input.strip() == "":
            no_exterior = None
        else:
            no_exterior = int(no_ext_input)
            
        barrio = int(input("Escribe el nuevo ID del barrio: "))
        id_descuento = int(input("Escribe el nuevo ID del descuento: "))
        
        ciudadano = Ciudadano(id, nombre, a_paterno, a_materno, calle, no_exterior, barrio, id_descuento)
        ciudadano_dao.actualizar(ciudadano)
        print("El ciudadano ha sido actualizado correctamente.")
        
    except Exception as e:
        print("Error al actualizar al ciudadano.")
        print(e)

def eliminar_ciudadano():
    try:
        ciudadano_dao = CiudadanoDAO()
        print("\nLista de ciudadanos disponibles:")
        
        lista = ciudadano_dao.obtener_todo()
        for c in lista:
            print(c.mostrar_info())
            
        id = int(input("\nEscribe el ID del ciudadano a eliminar: "))
        ciudadano_dao.eliminar(id)
        print(f"El ciudadano con ID {id} ha sido eliminado exitosamente.")
    except Exception as e:
        print("Error al eliminar el ciudadano.")
        print(e)

def menu_ciudadanos():
    print("\n1. Ver todos los ciudadanos")
    print("2. Insertar un nuevo ciudadano")
    print("3. Actualizar un ciudadano existente")
    print("4. Eliminar un ciudadano existente")
    opcion = int(input("Selecciona una opción (1-4): "))

    match opcion:
        case 1:
            ver_ciudadanos()  
        case 2:
            insertar_ciudadano()
        case 3:
            actualizar_ciudadano()
        case 4:  
            eliminar_ciudadano() 
    
def main():
    print("== SISTEMA GESTOR DE CIUDADANOS ==")
    print("Menú de opciones:")
    print("1-. Ciudadanos")
    opcion = int(input("Escribe tu opción: "))
    match opcion:
        case 1: 
            menu_ciudadanos()

if __name__ == "__main__":
    main()
