from .db import get_connection

mydb = get_connection()

class Sale:

    def __init__(self, fecha, total, id_producto, id_usuario, unidades_vendidas, id_venta=None):
        self.id_venta = id_venta
        self.fecha = fecha
        self.total = total
        self.id_producto = id_producto
        self.id_usuario = id_usuario
        self.unidades_vendidas = unidades_vendidas
        
    def save(self):
        # Create a New Object in DB
        if self.id_venta is None:
            with mydb.cursor() as cursor:
                sql = "INSERT INTO sale(fecha, total, id_producto, id_usuario, unidades_vendidas ) VALUES(%s,%s,%s,%s,%s)"
                val = (self.fecha, self.total, self.id_producto, self.id_usuario, self.unidades_vendidas)
                cursor.execute(sql, val)
                mydb.commit()
                self.id_venta = cursor.lastrowid
                return self.id_venta
        # Update an Object
        else:
            with mydb.cursor() as cursor:
                sql = "UPDATE sale SET fecha = %s, total = %s, id_producto = %s, id_usuario = %s, unidades_vendidas = %s WHERE id_venta = %s"
                val = (self.fecha, self.total, self.id_producto, self.id_usuario, self.unidades_vendidas, self.id_venta)
                cursor.execute(sql, val)
                mydb.commit()
                return self.id_venta
            
    @staticmethod
    def get(id_venta):
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT fecha, total, id_producto, id_usuario, unidades_vendidas  FROM sale WHERE id_venta = { id_venta }"
            cursor.execute(sql)
            result = cursor.fetchone()
            print(result)
            fecha = Sale(result["fecha"], result["total"], result["id_producto"], result["id_usuario"], result["unidades_vendidas"], id_venta)
            return fecha
        
    @staticmethod
    def get_all():
        sale = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT id_venta, fecha, total, Producto, Usuario, unidades_vendidas FROM ventas_view"
            cursor.execute(sql)
            result = cursor.fetchall()
            for item in result:
                sale.append(Sale(item["fecha"], item["total"], item["Producto"],item["Usuario"], item["unidades_vendidas"], item["id_venta"]))
            return sale
        

    @staticmethod
    def get_by_product(id_producto):
        products = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT * FROM sale WHERE id_producto = { id_producto }"
            cursor.execute(sql)
            result = cursor.fetchall()
            for product in result:
                products.append(Sale(fecha=product["fecha"],
                                     total=product["total"],
                                     id_producto=product["id_producto"],
                                     id_usuario=product["id_usuario"],
                                     unidades_vendidas=product["unidades_vendidas"],
                                     id_venta=product["id_venta"]))
    
    @staticmethod
    def count_all():
        with mydb.cursor() as cursor:
            sql = f"SELECT COUNT(id_venta) FROM sale"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result[0]
        
    def __str__(self):
        return f"{ self.id_venta } - { self.fecha } - { self.total } - { self.id_producto } - { self.id_usuario } - { self.unidades_vendidas }  "