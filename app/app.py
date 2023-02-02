import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import lib.widgets.chorus

Builder.load_file("templates/chorus.kv")

class kvfileApp(App):
    def build(self):
        # return kvfile2
        return lib.widgets.chorus.ChorusWidget()
 
if __name__ == '__main__':
    kv = kvfileApp()
    kv.run()