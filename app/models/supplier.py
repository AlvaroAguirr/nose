from .db import get_connection

mydb = get_connection()

class Supplier:

    def __init__(self, nombre, localidad, telefono, direccion, id_proveedor=None):
        self.id_proveedor = id_proveedor
        self.nombre = nombre
        self.localidad = localidad
        self.telefono = telefono
        self.direccion = direccion
        
    def save(self):
        # Create a New Object in DB
        if self.id_proveedor is None:
            with mydb.cursor() as cursor:
                sql = "INSERT INTO supplier(nombre, localidad, telefono, direccion) VALUES(%s, %s, %s, %s)"
                val = (self.nombre, self.localidad, self.telefono, self.direccion)
                cursor.execute(sql, val)
                mydb.commit()
                self.id_proveedor = cursor.lastrowid
                return self.id_proveedor
        # Update an Object
        else:
            with mydb.cursor() as cursor:
                sql = "UPDATE supplier SET nombre = %s, localidad = %s, telefono = %s, direccion = %s WHERE id_proveedor = %s"
                val = (self.nombre, self.localidad, self.telefono, self.direccion, self.id_proveedor)
                cursor.execute(sql, val)
                mydb.commit()
                return self.id_proveedor
            
    def delete(self):
        with mydb.cursor() as cursor:
            sql = f"DELETE FROM supplier WHERE id_proveedor = { self.id_proveedor }"
            cursor.execute(sql)
            mydb.commit()
            return self.id_proveedor
            
    @staticmethod
    def get(id_proveedor):
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT * FROM supplier WHERE id_proveedor = { id_proveedor }"
            cursor.execute(sql)
            result = cursor.fetchone()
            print(result)
            nombre = Supplier(result["nombre"], result["localidad"], result["telefono"], result["direccion"], id_proveedor)
            return nombre
        
    @staticmethod
    def get_all():
        supplier = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT id_proveedor, nombre, localidad, telefono, direccion FROM supplier"
            cursor.execute(sql)
            result = cursor.fetchall()
            for item in result:
                supplier.append(Supplier(item["nombre"], item["localidad"], item["telefono"], item["direccion"], item["id_proveedor"]))
            return supplier
    
    @staticmethod
    def count_all():
        with mydb.cursor() as cursor:
            sql = f"SELECT COUNT(id_proveedor) FROM supplier"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result[0]
        
    def __str__(self):
        return f"{ self.id_proveedor } - { self.nombre } - { self.localidad } - { self.telefono } - { self.direccion }"