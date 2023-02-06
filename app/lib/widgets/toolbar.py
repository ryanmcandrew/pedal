from kivy.uix.boxlayout import BoxLayout
import lib.functions as functions

class ToolbarWidget(BoxLayout):

    def __init__(self):
        super().__init__()
        pass

    def play_wav(self):
        functions.play_wav()
    def stop_wav(self):
        functions.stop_wav()
    def seek_wav(self, value):
        functions.seek_wav(value)
    def reload_wav(self):
        functions.reload_wav()
    def audio_devices(self):
        return functions.audio_devices()