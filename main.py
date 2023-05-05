from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QVBoxLayout, QWidget,QMessageBox
from PySide6.QtGui import QIcon, QFont
from register import Register
from database import Database
import hashlib
import sys


class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db = Database()

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
        

        self.register_label = QLabel("¿No tienes una cuenta?")
        self.layout.addWidget(self.register_label)

        self.register_button = QPushButton("Registrarse")
        self.register_button.setStyleSheet("background-color: #bd93f9;")
        self.register_button.setFont(QFont("Arial", 10))
        self.layout.addWidget(self.register_button)

        self.login_button.clicked.connect(self.fLogin)
        self.register_button.clicked.connect(self.fRegister)

        self.show()


    # funcion que abre la ventana de registro    
    def fRegister(self):
        self.ventana = Register()
        self.ventana.show()        


    #funcion que ejecuta la logica para ingresar los datos de inicio de sesion
    def fLogin(self):
        rut = self.rutInput.text()
        correo = self.correoInput.text()
        contrasena = self.contrasenaInput.text()
        print(rut,  correo, contrasena)
        self.db.login(rut, correo, contrasena)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Login()
    ventana.show()
    sys.exit(app.exec())