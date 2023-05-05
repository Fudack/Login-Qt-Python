from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QVBoxLayout, QWidget,QMessageBox
from PySide6.QtGui import QIcon, QFont
from database import Database
import hashlib
import sys

class Register(QMainWindow):
    def __init__(self):
        super().__init__()

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

        self.show()

    def onRegisterClicked(self):
        rut = self.rutInput.text()
        contrasena = self.contrasenaInput.text()
        confirm_contrasena = self.confirmcontrasenaInput.text()

        if contrasena != confirm_contrasena:
            QMessageBox.warning(self, "Error", "Las contraseñas no coinciden.")
            return

        # Aquí es donde puedes guardar la información del usuario en tu base de datos o archivo.
        # También puedes mostrar el mensaje de bienvenida aquí.
        self.welcomeMessage.setText(f"Bienvenido(a), {rut}!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Register()
    ventana.show()
    sys.exit(app.exec())