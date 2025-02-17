import sys
import os
from PyQt6.QtWidgets import QApplication, QWidget, QTextEdit, QPushButton, QVBoxLayout, QLineEdit, QListWidget
import subprocess

class PlaywrightGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Playwright GUI")
        self.setGeometry(100, 100, 600, 600)  # Am mărit fereastra

        # Editor de cod
        self.code_editor = QTextEdit(self)
        self.code_editor.setPlaceholderText("Introduceți codul Playwright aici...")

        # Câmp pentru numele fișierului
        self.file_name_input = QLineEdit(self)
        self.file_name_input.setPlaceholderText("Introduceți numele fișierului")

        # Buton pentru rulare
        self.run_button = QPushButton("Rulează", self)
        self.run_button.clicked.connect(self.run_playwright_script)

        # Buton pentru salvare
        self.save_button = QPushButton("Salvează", self)
        self.save_button.clicked.connect(self.save_code)

        # Output
        self.output_console = QTextEdit(self)
        self.output_console.setReadOnly(True)

        # Listă de fișiere salvate
        self.saved_files_list = QListWidget(self)
        self.saved_files_list.itemClicked.connect(self.load_code_from_file)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.code_editor)
        layout.addWidget(self.file_name_input)
        layout.addWidget(self.save_button)
        layout.addWidget(self.run_button)
        layout.addWidget(self.saved_files_list)
        layout.addWidget(self.output_console)
        self.setLayout(layout)

        # Încarcă fișierele salvate la pornirea aplicației
        self.load_saved_files()

    def run_playwright_script(self):
        code = self.code_editor.toPlainText()
        
        with open("playwright_runner.py", "w", encoding="utf-8") as f:
            f.write(code)

        try:
            result = subprocess.run(["python", "playwright_runner.py"], capture_output=True, text=True)
            self.output_console.setText(result.stdout if result.stdout else result.stderr)
        except Exception as e:
            self.output_console.setText(str(e))

    def save_code(self):
        file_name = self.file_name_input.text().strip()
        if not file_name:
            self.output_console.setText("Te rog să introduci un nume pentru fișier!")
            return
        
        # Adaugă prefixul "dacian_" la numele fișierului
        file_name = f"dacian_{file_name}"

        # Calea completă către fișierul salvat
        file_path = os.path.join(os.getcwd(), f"{file_name}.py")
        
        # Salvează codul în fișier
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(self.code_editor.toPlainText())

        # Adaugă fișierul în lista de fișiere salvate
        self.saved_files_list.addItem(file_name)

        self.output_console.setText(f"Codul a fost salvat ca {file_name}.py")

    def load_code_from_file(self, item):
        file_name = item.text()
        file_path = os.path.join(os.getcwd(), f"{file_name}.py")

        # Încarcă codul din fișier
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                code = f.read()
                self.code_editor.setText(code)
        except Exception as e:
            self.output_console.setText(f"Eroare la încărcarea fișierului: {str(e)}")

    def load_saved_files(self):
        # Încarcă fișierele salvate la pornirea aplicației
        files = [f for f in os.listdir(os.getcwd()) if f.endswith(".py") and f.startswith("dacian_")]
        for file in files:
            file_name = file[:-3]  # Îndepărtează extensia .py
            self.saved_files_list.addItem(file_name)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = PlaywrightGUI()
    gui.show()
    sys.exit(app.exec())
