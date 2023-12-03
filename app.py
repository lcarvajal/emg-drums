import sys
from sound_player import SoundPlayer

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EMG Drum Kit")
        self.setMinimumSize(QSize(400, 300))

        self.sound_player = SoundPlayer()

        self.firstDrumButton = QPushButton("Hit Snare")
        self.firstDrumButton.clicked.connect(self.first_drum_hit)

        self.secondDrumButton = QPushButton("Hit Kick")
        self.secondDrumButton.clicked.connect(self.second_drum_hit)

        self.thirdDrumButton = QPushButton("Hit High Hat")
        self.thirdDrumButton.clicked.connect(self.third_drum_hit)

        layout = QVBoxLayout(self)
        layout.addWidget(self.firstDrumButton)
        layout.addWidget(self.secondDrumButton)
        layout.addWidget(self.thirdDrumButton)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def first_drum_hit(self, didChange):
        self.sound_player.hit_drum("snare", 0.7)
    
    def second_drum_hit(self, didChange):
        self.sound_player.hit_drum("kick", 0.7)

    def third_drum_hit(self, didChange):
        self.sound_player.hit_drum("high-hat-closed", 0.7)

app = QApplication([])

# Create a Qt widget, which will be our window.
window = MainWindow()
window.show()

# Start the event loop.
app.exec()