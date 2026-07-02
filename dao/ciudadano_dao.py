from database.conexion import Conexion
from models.ciudadano import Ciudadano

class CiudadanoDAO:
    # SELECT * FROM ciudadano
    def obtener_todo(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        
        cursor.execute("SELECT * FROM ver_ciudadanos")
        registros = cursor.fetchall()
        
        ciudadanos = []
        for registro in registros:
            ciudadano = Ciudadano(
                id = registro[0],
                nombre = registro[1],
                a_paterno = registro[2],
                a_materno = registro[3],
                calle = registro[4],
                no_exterior = registro[5],
                barrio = registro[6],
                id_descuento = registro[7]
            )
            ciudadanos.append(ciudadano) 
            
        return ciudadanos 

    # INSERT
    def insertar(self, ciudadano):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """ 
        INSERT INTO ciudadano(id, nombre, a_paterno, a_materno, calle, no_exterior, barrio, id_descuento) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""


        cursor.execute(sql, (
            ciudadano.id,
            ciudadano.nombre,
            ciudadano.a_paterno,   
            ciudadano.a_materno,   
            ciudadano.calle,
            ciudadano.no_exterior,
            ciudadano.barrio,
            ciudadano.descuento   
        ))

        conexion.commit()
        cursor.close()
        conexion.close()

    # UPDATE
    def actualizar(self, ciudadano):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        UPDATE ciudadano
            SET nombre = %s, a_paterno = %s, a_materno = %s, calle = %s, no_exterior = %s, barrio = %s, id_descuento = %s
        WHERE id = %s
        """
        cursor.execute(sql, (
            ciudadano.nombre,
            ciudadano.a_paterno,   
            ciudadano.a_materno,   
            ciudadano.calle,
            ciudadano.no_exterior,
            ciudadano.barrio,
            ciudadano.descuento,  
            ciudadano.id          
        ))
        
        conexion.commit()
        cursor.close()
        conexion.close()

    # DELETE
    def eliminar(self, id):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("DELETE FROM ciudadano WHERE id = %s", (id,))

        conexion.commit()
        cursor.close()
        conexion.close()

    def obtener_ultimo_id(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        # Cambiamos MAX por COUNT para saber el total real de registros en la tabla base
        cursor.execute("SELECT COUNT(*) FROM ciudadano")
        resultado = cursor.fetchone()

        cursor.close()
        conexion.close()

        if resultado[0] is None:
            return 0
        return resultado[0]


