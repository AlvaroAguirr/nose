from .db import get_connection
from werkzeug.security import generate_password_hash, check_password_hash

mydb = get_connection()

class User:

    def __init__(self, 
                 nombre, 
                 ape_paterno, 
                 ape_materno,                 
                 nom_usuario, 
                 contrasenia, 
                 rol, 
                 id_usuario=None):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.ape_paterno = ape_paterno
        self.ape_materno = ape_materno
        self.nom_usuario = nom_usuario
        self.contrasenia = contrasenia
        self.rol = rol
        
    def save(self):
        # Create a New Object in DB
        if self.id_usuario is None:
            with mydb.cursor() as cursor:
                self.contrasenia = generate_password_hash(self.contrasenia)
                sql = "INSERT INTO user(nombre, ape_paterno, ape_materno, nom_usuario, contrasenia, rol) VALUES(%s,%s,%s,%s,%s,%s)"
                val = (self.nombre, self.ape_paterno, self.ape_materno, self.nom_usuario, self.contrasenia, self.rol)
                cursor.execute(sql, val)
                mydb.commit()
                self.id_usuario = cursor.lastrowid
                return self.id_usuario
        # Update an Object
        else:
            with mydb.cursor() as cursor:
                self.contrasenia = generate_password_hash(self.contrasenia)
                sql = "UPDATE user SET nombre = %s, ape_paterno = %s, ape_materno = %s, nom_usuario = %s, contrasenia = %s, rol=%s WHERE id_usuario = %s"
                val = (self.nombre, self.ape_paterno, self.ape_materno, self.nom_usuario, self.contrasenia, self.rol, self.id_usuario)
                cursor.execute(sql, val)
                mydb.commit()
                return self.id_usuario
            
    def delete(self):
        with mydb.cursor() as cursor:
            sql = f"DELETE FROM user WHERE id_usuario = { self.id_usuario }"
            cursor.execute(sql)
            mydb.commit()
            return self.id_usuario
            
    @staticmethod
    def __get__(id_usuario):
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT * FROM user WHERE id_usuario = { id_usuario }"
            cursor.execute(sql)

            user = cursor.fetchone()
            
            if user:
                user = User(nombre=user["nombre"], 
                            ape_paterno=user["ape_paterno"], 
                            ape_materno=user["ape_materno"], 
                            nom_usuario=user["nom_usuario"],
                            contrasenia=user["contrasenia"],
                            rol=user['rol'], 
                            id_usuario = id_usuario)
                return user
            return None
        
    @staticmethod
    def get_all():
        user = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT * FROM user"
            cursor.execute(sql)
            result = cursor.fetchall()
            for use in result:
                user.append(
                    User(nombre=use["nombre"], 
                         ape_paterno=use["ape_paterno"], 
                         ape_materno=use["ape_materno"],
                         nom_usuario=use["nom_usuario"],
                         contrasenia=use["contrasenia"], 
                         rol=use["rol"], 
                         id_usuario=use["id_usuario"])
                )
            return user
        
    @staticmethod
    def get_by_password(nom_usuario, contrasenia):
        with mydb.cursor(dictionary=True) as cursor:
            sql = "SELECT id_usuario, nom_usuario, contrasenia, rol FROM user WHERE nom_usuario = %s"
            val = (nom_usuario,)
            cursor.execute(sql, val)
            user = cursor.fetchone()
            print(user)
            if user != None:
                if check_password_hash(user["contrasenia"], contrasenia):
                    return User.__get__(user["id_usuario"])
            return None
    
    @staticmethod
    def count_all():
        with mydb.cursor() as cursor:
            sql = f"SELECT COUNT(id_usuario) FROM user"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result[0]
        
    def __str__(self):
        return f"{ self.id_usuario } - { self.nombre } - { self.ape_paterno } - { self.ape_materno } - { self.nom_usuario } - { self.contrasenia } - { self.rol }"