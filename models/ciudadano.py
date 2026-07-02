class Ciudadano:
    
    def __init__(self, id, nombre, a_paterno, a_materno, calle, no_exterior, barrio, id_descuento):
        self.id = id
        self.nombre = nombre
        self.a_paterno = a_paterno
        self.a_materno = a_materno
        self.calle = calle
        self.no_exterior = no_exterior
        self.barrio = barrio
        self.descuento = id_descuento 
        
    def mostrar_info(self):
        num_ext = f"No. {self.no_exterior}" if self.no_exterior else "S/N"
        return f"ID: {self.id}, Nombre: {self.nombre}, Apellido paterno: {self.a_paterno}, Apellido materno: {self.a_materno}, Calle: {self.calle}, Num. Exterior: {num_ext}, Barrio: {self.barrio}, Descuento: {self.descuento}"
        