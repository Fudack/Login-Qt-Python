import mysql.connector
import hashlib

class Database:
    # datos de conexion listos
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host = "127.0.0.1",
                user = "root",
                password = "admin",
                database = "fulladmin")
            print("Conexión a la base de datos exitosa")
        except mysql.connector.Error as error:
            print(f"Error al conectarse a la base de datos: {error}")

    # desconectarse de la db
    def disconnect(self):
        self.connection.close()
        print("Desconexión de la base de datos exitosa")

    # registrar un usuario
    def registroDeUsuario(self, rut, correo, nombre, apPat, apMat, contrasena, contrasenaConfirm, root):
        if contrasena != contrasenaConfirm:
            print("Las contraseñas no coinciden")
            return False
        else:
            cursor = self.connection.cursor()
            encrypt = hashlib.sha256(contrasena.encode())
            contrasena = encrypt.hexdigest()
            try:
                cursor.execute("INSERT INTO usuarios (rut, correo, nombre, apPat, apMat, contrasena, root) VALUES (%s, %s, %s, %s, %s, %s, %s)", (rut, correo, nombre, apPat, apMat, contrasena, root))
                self.connection.commit()
                print(f"Registro de usuario exitoso. Rut: {rut}")
            except mysql.connector.Error as error:
                print(f"Error al registrar el usuario: {error}")
                self.connection.rollback()

    # login
    def login(self, rut, correo, contrasena):
        encrypt = hashlib.sha256(contrasena.encode())
        contrasena = encrypt.hexdigest()
        cursor = self.connection.cursor()
        try:
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
        except mysql.connector.Error as error:
            print(f"Error al iniciar sesión: {error}")
            return False

    # listado de usuarios
    def listaUsuarios(self):
        c = self.connection.cursor()
        try:
            c.execute("SELECT * FROM usuarios")
            usuarios = c.fetchall()
            return usuarios
        except mysql.connector.Error as error:
            print(f"Error al obtener la lista de usuarios: {error}")
            return None
