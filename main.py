from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QVBoxLayout, QWidget
from PySide6.QtGui import QIcon, QFont
import sys


class Login(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Inicio de Sesión")
        self.setFixedSize(300, 200)
        self.setWindowIcon(QIcon("icon.png"))

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.username_label = QLabel("Nombre de Usuario")
        self.layout.addWidget(self.username_label)

        self.username_input = QLineEdit()
        self.layout.addWidget(self.username_input)

        self.password_label = QLabel("Contraseña")
        self.layout.addWidget(self.password_label)

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.layout.addWidget(self.password_input)

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

        self.username_label = QLabel("Nombre de Usuario")
        self.layout.addWidget(self.username_label)

        self.username_input = QLineEdit()
        self.layout.addWidget(self.username_input)

        self.password_label = QLabel("Contraseña")
        self.layout.addWidget(self.password_label)

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.layout.addWidget(self.password_input)

        self.confirm_password_label = QLabel("Confirmar Contraseña")
        self.layout.addWidget(self.confirm_password_label)

        self.confirm_password_input = QLineEdit()
        self.confirm_password_input.setEchoMode(QLineEdit.Password)
        self.layout.addWidget(self.confirm_password_input)

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
    
    
print("hola")