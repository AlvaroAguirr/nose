from .db import get_connection

mydb = get_connection()

class Category:

    def __init__(self, nombre, id_categoria=None):
        self.id_categoria = id_categoria
        self.nombre = nombre
        

    def save(self):
        # Create a New Object in DB
        if self.id_categoria is None:
            with mydb.cursor() as cursor:
                sql = "INSERT INTO category(nombre) VALUES(%s)"
                val = (self.nombre,)
                cursor.execute(sql, val)
                mydb.commit()
                self.id_categoria = cursor.lastrowid
                return self.id_categoria
        # Update an Object
        else:
            with mydb.cursor() as cursor:
                sql = "UPDATE category SET nombre = %s WHERE id_categoria = %s"
                val = (self.nombre, self.id_categoria)
                cursor.execute(sql, val)
                mydb.commit()
                return self.id_categoria
            
    def delete(self):
        with mydb.cursor() as cursor:
            sql = f"DELETE FROM category WHERE id_categoria = { self.id_categoria }"
            cursor.execute(sql)
            mydb.commit()
            return self.id_categoria
            
    @staticmethod
    def get(id_categoria):
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT nombre FROM category WHERE id_categoria = { id_categoria }"
            cursor.execute(sql)
            result = cursor.fetchone()
            print(result)
            nombre = Category(result["nombre"], id_categoria)
            return nombre
        
          
    @staticmethod
    def get_all(limit=10, page=1):
        offset = limit * page - limit 
        categoria = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT nombre,id_categoria FROM category limit { limit } offset { offset }"
            cursor.execute(sql)
            result = cursor.fetchall()
            for cats in result:
                categoria.append(Category(nombre=cats["nombre"],
                                           id_categoria=cats["id_categoria"]))
            return categoria
    
    @staticmethod
    def count_all():
        with mydb.cursor() as cursor:
            sql = f"SELECT COUNT(id_categoria) FROM category"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result[0]
        
    def __str__(self):
        return f"{ self.id_categoria } - { self.nombre }"
    

    @staticmethod
    def count():
        with mydb.cursor(dictionary=True) as cursor:
            sql= "select count(id_categoria) as total from category"
            cursor.execute(sql)
            result =cursor.fetchone()
            return result['total']