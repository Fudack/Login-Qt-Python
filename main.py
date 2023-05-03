from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QVBoxLayout, QWidget
from PySide6.QtGui import QIcon, QFont
from database import Database
import hashlib
import sys



class Fbotones:
    def __init__(self):
        self.db = Database()
        self.L= Login()
        
    #Funcion del boton de register
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
    
    
    
    #funcion del boton de inicio de sesion 
    



class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db = Database()
        self.mostrarRegistro = Register()

        self.setWindowTitle("Inicio de Sesión")
        self.setFixedSize(300, 200)
        self.setWindowIcon(QIcon("icon.png"))

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.rutLabel = QLabel("Rut de Usuario")
        self.layout.addWidget(self.rutLabel)

        self.rutInput = QLineEdit()
        self.layout.addWidget(self.rutInput)
        
        self.correoLabel = QLabel("Correo de Usuario")
        self.layout.addWidget(self.correoLabel)

        self.correoInput = QLineEdit()
        self.layout.addWidget(self.correoInput)

        self.contrasenaLabel = QLabel("Contraseña")
        self.layout.addWidget(self.contrasenaLabel)

        self.contrasenaInput = QLineEdit()
        self.contrasenaInput.setEchoMode(QLineEdit.Password)
        self.layout.addWidget(self.contrasenaInput)

        self.login_button = QPushButton("Iniciar Sesión")
        self.login_button.setStyleSheet("background-color: #bd93f9;")
        self.login_button.setFont(QFont("Arial", 12, QFont.Bold))
        self.layout.addWidget(self.login_button)
        
        def fLogin(self):
            rut = self.rutInput.text()
            correo = self.correoInput.text()
            contrasena = self.contrasenaInput.text()
            print(rut,  correo, contrasena)
            self.db.login(rut, correo, contrasena)

        self.register_label = QLabel("¿No tienes una cuenta?")
        self.layout.addWidget(self.register_label)

        self.register_button = QPushButton("Registrarse")
        self.register_button.setStyleSheet("background-color: #bd93f9;")
        self.register_button.setFont(QFont("Arial", 10))
        self.layout.addWidget(self.register_button)
        
        self.login_button.clicked.connect(lambda: fLogin(self))
        self.register_button.clicked.connect(self.mostrarRegistro.show)
        
        self.show()


class Register(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Registro")
        self.setFixedSize(300, 200)
        self.setWindowIcon(QIcon("icon.png"))

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.rutLabel = QLabel("Nombre de Usuario")
        self.layout.addWidget(self.rutLabel)

        self.rutInput = QLineEdit()
        self.layout.addWidget(self.rutInput)

        self.contrasenaLabel = QLabel("Contraseña")
        self.layout.addWidget(self.contrasenaLabel)

        self.contrasenaInput = QLineEdit()
        self.contrasenaInput.setEchoMode(QLineEdit.Password)
        self.layout.addWidget(self.contrasenaInput)

        self.confirm_contrasenaLabel = QLabel("Confirmar Contraseña")
        self.layout.addWidget(self.confirm_contrasenaLabel)

        self.confirm_contrasenaInput = QLineEdit()
        self.confirm_contrasenaInput.setEchoMode(QLineEdit.Password)
        self.layout.addWidget(self.confirm_contrasenaInput)

        self.register_button = QPushButton("Registrarse")
        self.register_button.setStyleSheet("background-color: #bd93f9;")
        self.register_button.setFont(QFont("Arial", 12, QFont.Bold))
        self.layout.addWidget(self.register_button)

        self.login_label = QLabel("¿Ya tienes una cuenta?")
        self.layout.addWidget(self.login_label)

        self.login_button = QPushButton("Iniciar Sesión")
        self.login_button.setStyleSheet("background-color: #bd93f9;")
        self.login_button.setFont(QFont("Arial", 10))
        self.layout.addWidget(self.login_button)

        self.show()


class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyDracula Inicio de Sesión y Registro")
        self.setFixedSize(300, 200)
        self.setWindowIcon(QIcon("icon.png"))

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.login_button = QPushButton("Iniciar Sesión")
        self.login_button.setStyleSheet("background-color: #bd93f9;")
        self.login_button.setFont



    
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Login()
    ventana.show()
    sys.exit(app.exec())