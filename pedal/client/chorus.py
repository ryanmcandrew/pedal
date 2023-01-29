import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import lib.functions
import os

app_abs = os.path.join(os.path.dirname(__file__))

# don't need to specifically assign the builder talks to kivy to load the files
# kvfile2 = Builder.load_file("templates/basic.kv")
Builder.load_file("templates/chorus.kv")
# Builder.load_file("templates/basic.kv")

# create the layout class
class ChorusWidget(BoxLayout):
    def check_status(self, btn):
        print('something')

    def select(self, *args):
        try: self.label.text = args[1][0]
        except: pass

    def play_wav(self):
        lib.functions.play_wav()

    def stop_wav(self):
        lib.functions.stop_wav()
    
    def seek_wav(self, value):
        lib.functions.seek_wav(value)

    def chorus(self):
        lib.functions.test_one()

    def reload_wav(self):
        lib.functions.reload_wav()

    def update_chorus(self,rate, depth, delay, feedback, mix):
        lib.functions.update_chorus(rate, depth, delay, feedback, mix)

    def audio_devices(self):
        return lib.functions.audio_devices()
        pass

    def update_active_audio_device(self):
        lib.functions.update_active_audio_device()
        pass
    
    # def on_touch_down(self, touch):
    #     # self.bind(on_click=lambda x:print(x))
    #     print('something')
        # return super().on_touch_down(touch)

class kvfileApp(App):
    def build(self):
        # return kvfile2
        return ChorusWidget()
 
kv = kvfileApp()
kv.run()