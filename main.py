import sys
from PySide6.QtWidgets import (QApplication)
from window_ui import WindowUI

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WindowUI()
    window.show()
    sys.exit(app.exec())
