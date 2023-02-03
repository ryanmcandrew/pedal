from kivy.uix.boxlayout import BoxLayout
import lib.functions as functions

class ChorusWidget(BoxLayout):
    def play_wav(self):
        functions.play_wav()
    def stop_wav(self):
        functions.stop_wav()
    def seek_wav(self, value):
        functions.seek_wav(value)
    def reload_wav(self):
        functions.reload_wav()
    def update_chorus(self, rate, depth, delay, feedback, mix):
        functions.update_chorus(rate, depth, delay, feedback, mix)
    def audio_devices(self):
        functions.audio_devices()