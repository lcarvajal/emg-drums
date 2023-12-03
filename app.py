import sys
from sound_player import SoundPlayer

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QGridLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EMG Drum Kit")
        self.setMinimumSize(QSize(400, 300))

        self.sound_player = SoundPlayer()

        self.image = QPixmap("image/classic-drums.png")
        self.label = QLabel()
        self.label.setPixmap(self.image)
        self.label.adjustSize()
        self.resize(self.image.size())

        self.firstDrumButton = QPushButton("Hit Snare")
        self.firstDrumButton.clicked.connect(self.first_drum_hit)

        self.secondDrumButton = QPushButton("Hit Kick")
        self.secondDrumButton.clicked.connect(self.second_drum_hit)

        self.thirdDrumButton = QPushButton("Hit High Hat")
        self.thirdDrumButton.clicked.connect(self.third_drum_hit)

        layout = QGridLayout()
        layout.addWidget(self.label, 0, 0, 1, 3, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.firstDrumButton, 1, 0, 1, 1)
        layout.addWidget(self.secondDrumButton, 1, 1, 1, 1)
        layout.addWidget(self.thirdDrumButton, 1, 2, 1, 1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def first_drum_hit(self, didChange):
        drum_type = "snare"
        self.sound_player.hit_drum(drum_type, 0.7)
        self.update_image(drum_type)
    
    def second_drum_hit(self, didChange):
        drum_type = "kick"
        self.sound_player.hit_drum(drum_type, 0.7)
        self.update_image(drum_type)

    def third_drum_hit(self, didChange):
        drum_type = "high-hat"
        self.sound_player.hit_drum(drum_type, 0.7)
        self.update_image(drum_type)

    def update_image(self, drum_type):
        self.image = QPixmap("image/" + drum_type + ".png")
        if not self.image.isNull():
            self.label.setPixmap(self.image)
            self.label.adjustSize()
            self.resize(self.image.size())

app = QApplication([])

# Create a Qt widget, which will be our window.
window = MainWindow()
window.show()

# Start the event loop.
app.exec()