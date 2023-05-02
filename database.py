import mysql.connector
import hashlib

class Database:
    #datos de conexion listos
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="admin",
            database="fulladmin")

    #desconectarse de la db
    def disconnect(self):
        self.connection.close()

    #registrar un usuario
    def registroDeUsuario(self, rut, correo, nombre, apPat, apMat, contrasena, contrasenaConfirm, root):
        if contrasena != contrasenaConfirm:
            print("Las contraseñas no coinciden")
            return False
        else:
            cursor = self.connection.cursor()
            encrypt = hashlib.sha256(contrasena.encode())
            contrasena = encrypt.hexdigest()
            cursor.execute("INSERT INTO usuarios (rut, correo, nombre, apPat, apMat, contrasena, root) VALUES (%s, %s, %s, %s, %s, %s, %s)", (rut, correo, nombre, apPat, apMat, contrasena, root))
            self.connection.commit()
    
    def login(self, rut, correo, contrasena):
        encrypt = hashlib.sha256(contrasena.encode())
        contrasena = encrypt.hexdigest()
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE rut = %s AND correo = %s", (rut, correo))
        user = cursor.fetchone()

        if user is None:
            print("Usuario no encontrado")
            return False
        elif user[5] != contrasena:
            print("Contraseña incorrecta")
            return False
        else:
            print("Inicio de sesión exitoso")
            return True
    
    
    def listaUsuarios(self):
        c = self.connection.cursor()
        c.execute("SELECT * FROM usuarios")
        usuarios = c.fetchall()
        return usuarios
