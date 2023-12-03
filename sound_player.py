from PyQt6.QtMultimedia import QSoundEffect
from PyQt6.QtCore import QUrl

class SoundEffect(QSoundEffect):
    def __init__(self, type):
        super().__init__()
        self.setSource(QUrl.fromLocalFile('sound/' + type + '.wav'))

class SoundPlayer():
    def __init__(self):
        super().__init__()

        self.drum_sounds = {
            'snare': SoundEffect("snare"),
            'high-hat-closed': SoundEffect("high-hat-closed"),
            'kick': SoundEffect("kick"),
        }

    """
    drum_type should be the file name
    volume should be a value between 0 and 1 
    """
    def hit_drum(self, type, volume):
        sound = self.drum_sounds[type]
        sound.setVolume(volume)
        sound.play()
