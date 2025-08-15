import sys
from PySide6.QtWidgets import QApplication
from gui.main_window import MainWindow

def main():
    app = QApplication(sys.argv)

    app.setApplicationName("API definition") 

    main_window = MainWindow()
    main_window.setWindowTitle("API definition")

    main_window.show()

    sys.exit(app.exec())
    
if __name__ == "__main__":
    main()