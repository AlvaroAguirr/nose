from .db import get_connection

mydb = get_connection()

class Reports:

    def __init__(self, fecha, total, id_producto, id_usuario, unidades_vendidas, id_venta=None):
        self.id_venta = id_venta
        self.fecha = fecha
        self.total = total
        self.id_producto = id_producto
        self.id_usuario = id_usuario
        self.unidades_vendidas = unidades_vendidas
        
    @staticmethod
    def get(id_venta):
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT fecha, total, id_producto, id_usuario  FROM sale WHERE id_venta = { id_venta }"
            cursor.execute(sql)
            result = cursor.fetchone()
            print(result)
            fecha = Reports(result["fecha"], result["total"], result["id_producto"], result["id_usuario"], id_venta)
            return fecha
        
    @staticmethod
    def get_all():
        sale = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT id_venta, fecha, total, Producto, Usuario, unidades_vendidas FROM ventas_view"
            cursor.execute(sql)
            result = cursor.fetchall()
            for item in result:
                sale.append(Reports(item["fecha"], item["total"], item["Producto"],item["Usuario"], item["unidades_vendidas"], item["id_venta"]))
            return sale
    
    @staticmethod
    def count_all():
        with mydb.cursor() as cursor:
            sql = f"SELECT COUNT(id_venta) FROM sale"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result[0]
        
    def __str__(self):
        return f"{ self.id_venta } - { self.fecha } - { self.total } - { self.id_producto } - { self.id_usuario } "