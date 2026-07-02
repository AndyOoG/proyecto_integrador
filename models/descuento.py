class Descuento:

    def __init__(self,id,nombre_descuento):
        self.nombre = nombre_descuento

    def mostrar_info(self):
        return f"ID: {self.id}, Nombre: {self.nombre}"
    
        