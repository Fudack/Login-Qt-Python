from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QVBoxLayout, QWidget,QMessageBox, QCheckBox
from PySide6.QtGui import QIcon, QFont
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
        self.close()
        self.ventana = Register()
        self.ventana.show()        


    #funcion que ejecuta la logica para ingresar los datos de inicio de sesion
    def fLogin(self):
        rut = self.rutInput.text()
        correo = self.correoInput.text()
        contrasena = self.contrasenaInput.text()
        print(rut,  correo, contrasena)
        self.db.login(rut, correo, contrasena)


class Register(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db = Database()

        self.setWindowTitle("Registro")
        self.setFixedSize(300, 400)
        self.setWindowIcon(QIcon("icon.png"))

        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        self.layout = QVBoxLayout()
        self.centralWidget.setLayout(self.layout)

        self.rutLabel = QLabel("Rut de Usuario")
        self.layout.addWidget(self.rutLabel)

        self.rutInput = QLineEdit()
        self.layout.addWidget(self.rutInput)

        self.correoLabel = QLabel("Correo Electrónico")
        self.layout.addWidget(self.correoLabel)

        self.correoInput = QLineEdit()
        self.layout.addWidget(self.correoInput)

        self.nombreLabel = QLabel("Nombre")
        self.layout.addWidget(self.nombreLabel)

        self.nombreInput = QLineEdit()
        self.layout.addWidget(self.nombreInput)

        self.apPatLabel = QLabel("Apellido Paterno")
        self.layout.addWidget(self.apPatLabel)

        self.apPatInput = QLineEdit()
        self.layout.addWidget(self.apPatInput)

        self.apMatLabel = QLabel("Apellido Materno")
        self.layout.addWidget(self.apMatLabel)

        self.apMatInput = QLineEdit()
        self.layout.addWidget(self.apMatInput)

        self.contrasenaLabel = QLabel("Contraseña")
        self.layout.addWidget(self.contrasenaLabel)

        self.contrasenaInput = QLineEdit()
        self.contrasenaInput.setEchoMode(QLineEdit.Password)
        self.layout.addWidget(self.contrasenaInput)

        self.confirmcontrasenaLabel = QLabel("Confirmar Contraseña")
        self.layout.addWidget(self.confirmcontrasenaLabel)

        self.confirmcontrasenaInput = QLineEdit()
        self.confirmcontrasenaInput.setEchoMode(QLineEdit.Password)
        self.layout.addWidget(self.confirmcontrasenaInput)

        self.rootLabel = QLabel("¿Es root?")
        self.layout.addWidget(self.rootLabel)

        self.rootCheckBox = QCheckBox()
        self.layout.addWidget(self.rootCheckBox)

        self.registerButton = QPushButton("Registrarse")
        self.registerButton.setStyleSheet("background-color: #bd93f9;")
        self.registerButton.setFont(QFont("Arial", 12, QFont.Bold))
        self.layout.addWidget(self.registerButton)

        self.loginLabel = QLabel("¿Ya tienes una cuenta?")
        self.layout.addWidget(self.loginLabel)

        self.loginButton = QPushButton("Iniciar Sesión")
        self.loginButton.setStyleSheet("background-color: #bd93f9;")
        self.loginButton.setFont(QFont("Arial", 10))
        self.layout.addWidget(self.loginButton)

        self.registerButton.clicked.connect(self.onRegisterClicked)
        self.loginButton.clicked.connect(self.fLogin)

        self.show()

    def fLogin(self):
        self.close()
        self.ventana = Login()
        self.ventana.show() 

    def onRegisterClicked(self):
        rut = self.rutInput.text()
        correo = self.correoInput.text()
        nombre = self.nombreInput.text()
        apPat = self.apPatInput.text() 
        apMat = self.apMatInput.text()
        contrasena = self.contrasenaInput.text()
        contrasenaConfirm = self.confirmcontrasenaInput.text()
        root = self.rootCheckBox.isChecked()

        if contrasena != contrasenaConfirm:
            QMessageBox.warning(self, "Error", "Las contraseñas no coinciden.")
            return

        # Aquí es donde puedes guardar la información del usuario en tu base de datos o archivo.
        # También puedes mostrar el mensaje de bienvenida aquí.
        print(rut, correo, nombre, apPat, apMat, contrasena, contrasenaConfirm, root)
        self.db.registroDeUsuario(rut, correo, nombre, apPat, apMat, contrasena, contrasenaConfirm, root)






if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Login()
    ventana.show()
    sys.exit(app.exec())