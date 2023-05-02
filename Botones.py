from database import Database
import hashlib

class Fbotones:
    def __init__(self):
        self.db = Database()
    
    def btnRegistro(self):
        rut = int(input("Ingrese rut: "))
        correo = input("Ingrese correo: ")
        nombre = input("Ingrese nombre: ")
        apPat = input("Ingrese apellido paterno: ")
        apMat = input("Ingrese apellido materno: ")
        contrasena = input("Ingrese contraseña: ")
        
        while True:
            contrasenaConfirm = input("Confirme contraseña: ")
            if contrasena == contrasenaConfirm:
                break
            else:
                print("Las contraseñas no coinciden")
    
        root = input("El usuario es root [si/no]: ")
    
        while True:
            if root == "si" or root == "no":
                break
            else:
                print("opcion no valida")
        
        if root == "si":
            root = True
        else:
            root = False
            
        self.db.registroDeUsuario(rut, correo, nombre, apPat, apMat, contrasena, contrasenaConfirm, root)

        usuarios = self.db.listaUsuarios()
        for usuario in usuarios:
            print(usuario)        
        
    def btnLogin(self):
        rut = int(input("Ingrese rut: "))
        correo = input("Ingrese correo: ")
        contrasena = input("Ingrese contraseña: ")
        self.db.login(rut, correo, contrasena)
