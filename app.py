import sys

from check_trigno import run_checks
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button_is_checked = True

        self.setWindowTitle("EMG Drum Kit")
        self.setMinimumSize(QSize(400, 300))

        self.button = QPushButton("Test EMG Connections")
        self.button.clicked.connect(self.test_connection_button_clicked)

        self.setCentralWidget(self.button)

    def test_connection_button_clicked(self):
        self.button.setText("Testing connection...")
        self.button.setEnabled(False)
        run_checks()

    def drum_one_hit():
        print('Drum one hit')

app = QApplication([])

# Create a Qt widget, which will be our window.
window = MainWindow()
window.show()

# Start the event loop.
app.exec()