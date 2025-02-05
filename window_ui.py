from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLineEdit,
    QPushButton,
    QLabel,
    QComboBox,
    QTextEdit,
)
from PySide6.QtCore import (
    QTimer
)
from hash_generator import HashGenerator


class WindowUI(QWidget):
    hashTypes = (
        'md5',
        'sha1',
        'sha224',
        'sha256',
        'sha384',
        'sha512',
        'sha3_224',
        'sha3_256',
        'sha3_384',
        'sha3_512',
    )

    def __init__(self):
        super().__init__()

        self.initial_configuration()

        self.hash_generator = HashGenerator()
        self.hash_generated = ''
        self.timer = QTimer()
        self.timer.timeout.connect(self.restore_hash)

    def initial_configuration(self):
        self.setWindowTitle("Hash Generator")
        self.setup_ui()
        self.setFixedSize(400, 400)
        self.centerWindow()

    def centerWindow(self):
        self.setWindowOpacity(0.0)
        QTimer.singleShot(500, lambda: self.setWindowOpacity(1.0))

        qt_rectangle = self.frameGeometry()
        center_point = self.screen().availableGeometry().center()
        qt_rectangle.moveCenter(center_point)
        self.move(qt_rectangle.topLeft())

    def setup_ui(self):
        layout = QVBoxLayout()

        # Campo para a senha
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Digite sua senha")
        self.password_input.setStyleSheet("""
            QLineEdit {
                font-size: 16px;
                height: 20px;
                padding: 10px;
                margin: 5px;
                border: 2px solid #ccc;
                border-radius: 5px;
            }
        """)
        layout.addWidget(self.password_input)

        # Campo para o salt (opcional)
        self.salt_input = QLineEdit()
        self.salt_input.setPlaceholderText("Digite o salt (opcional)")
        self.salt_input.setStyleSheet("""
            QLineEdit {
                font-size: 16px;
                height: 20px;
                padding: 10px;
                margin: 5px;
                border: 2px solid #ccc;
                border-radius: 5px;
            }
        """)
        layout.addWidget(self.salt_input)

        # ComboBox para escolha do tipo de hash
        self.hashLabel = QLabel("Tipo de hash")
        layout.addWidget(self.hashLabel)

        self.selectHash = QComboBox()
        self.selectHash.addItems([hashs.upper() for hashs in self.hashTypes])
        layout.addWidget(self.selectHash)

        # Botão de geração
        self.generate_button = QPushButton("Gerar Hash")
        self.generate_button.clicked.connect(self.generate_hash)
        layout.addWidget(self.generate_button)

        # Exibição do hash
        self.result_label = QLabel("Hash Generated")
        layout.addWidget(self.result_label)

        self.hash_output = QTextEdit()
        self.hash_output.setReadOnly(True)
        self.hash_output.setFixedHeight(80)
        self.hash_output.setStyleSheet("""
            QLineEdit {
                font-size: 14px;
                padding: 10px;
                margin: 5px;
                border-radius: 5px;
                user-select: none;
            }
        """)
        layout.addWidget(self.hash_output)

        # Botão de copiar
        self.copy_button = QPushButton("Copiar Hash")
        self.copy_button.clicked.connect(self.copy_hash)
        layout.addWidget(self.copy_button)

        self.setLayout(layout)

    def generate_hash(self):
        self.hash_generated = self.hash_generator.generate_hash(
            password=self.password_input.text(),
            salt=self.salt_input.text(),
            hash_type=self.selectHash.currentText()
        )

        self.hash_output.setPlainText(self.hash_generated)

    def copy_hash(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.hash_generated)

        self.timer.start(1500)
        self.hash_output.setPlainText(self.hash_generator.copy_alert())

    def restore_hash(self):
        self.hash_output.setPlainText(self.hash_generated)
        self.timer.stop()
