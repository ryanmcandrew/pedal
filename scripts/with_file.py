import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

# don't need to specifically assign the builder talks to kivy to load the files
# kvfile2 = Builder.load_file("templates/basic.kv")
Builder.load_file("templates/files.kv")
# Builder.load_file("templates/basic.kv")

# create the layout class
class Filechooser(BoxLayout):
    def select(self, *args):
        try: self.label.text = args[1][0]
        except: pass

class kvfileApp(App):
    def build(self):
        # return kvfile2
        return Filechooser()
 
kv = kvfileApp()
kv.run()