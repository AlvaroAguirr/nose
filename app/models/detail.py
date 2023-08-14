from .db import get_connection

mydb = get_connection()

class Detail:

    def __init__(self, producto, cantidad, id_venta, id_detalle=None):
        self.id_detalle = id_detalle
        self.producto = producto
        self.cantidad = cantidad
        self.id_venta = id_venta
        
    def save(self):
        # Create a New Object in DB
        if self.id_detalle is None:
            with mydb.cursor() as cursor:
                sql = "INSERT INTO detail(producto, cantidad, id_venta) VALUES(%s,%s,%s)"
                val = (self.producto, self.cantidad, self.id_venta)
                cursor.execute(sql, val)
                mydb.commit()
                self.id_detalle = cursor.lastrowid
                return self.id_detalle
        # Update an Object
        else:
            with mydb.cursor() as cursor:
                sql = "UPDATE detail SET producto = %s, cantidad = %s, id_venta = %s WHERE id_detalle = %s"
                val = (self.producto, self.cantidad, self.id_venta, self.id_detalle)
                cursor.execute(sql, val)
                mydb.commit()
                return self.id_detalle
            
    def delete(self):
        with mydb.cursor() as cursor:
            sql = f"DELETE FROM detail WHERE id_detalle = { self.id_detalle }"
            cursor.execute(sql)
            mydb.commit()
            return self.id_detalle
            
    @staticmethod
    def get(id_detalle):
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT producto, cantidad, id_venta  FROM detail WHERE id_detalle = { id_detalle }"
            cursor.execute(sql)
            result = cursor.fetchone()
            print(result)
            producto = Detail(result["producto"], result["cantidad"], result["id_venta"], id_detalle)
            return producto
        
    @staticmethod
    def get_all():
        detail = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT id_detalle, producto, cantidad, id_venta FROM detail"
            cursor.execute(sql)
            result = cursor.fetchall()
            for item in result:
                detail.append(Detail(item["producto"], item["cantidad"], item["id_venta"],item["id_detalle"]))
            return detail
    
    @staticmethod
    def count_all():
        with mydb.cursor() as cursor:
            sql = f"SELECT COUNT(id_detalle) FROM detail"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result[0]
        
    def __str__(self):
        return f"{ self.id_detalle } - { self.producto } - { self.cantidad } - { self.id_venta } "