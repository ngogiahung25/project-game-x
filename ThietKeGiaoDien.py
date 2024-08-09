import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QVBoxLayout, QWidget 

class ProjectGameX(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pushbutton widgets (Yes or No)?")
        self.setGeometry(100, 100, 400, 200) 
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        start_button = QPushButton("Bắt đầu game")
        exit_button = QPushButton("Thoát game")
        
        start_button.clicked.connect(self.show_start_message) 
        exit_button.clicked.connect(self.exit_application)
        
        layout = QVBoxLayout() 
        layout.addWidget(start_button) 
        layout.addWidget(exit_button)
        
        central_widget.setLayout(layout)
        
    def show_start_message(self):
        QMessageBox.information(self, "Choice", "Chương trình đã bắt đầu.")
    
    def exit_application(self):
        reply = QMessageBox.information(self, "Choice", "Bạn đã thoát game.", QMessageBox.Ok)
        if reply == QMessageBox.Ok:
            QApplication.quit()

def main():
    app = QApplication(sys.argv) 
    window = ProjectGameX()
    window.show()
    sys.exit(app.exec_())
        
if __name__ == "__main__":
    main()