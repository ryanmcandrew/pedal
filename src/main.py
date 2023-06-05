from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

from core.controller.root import RootBoxLayout
from core.controller.chorus import ChorusLayout
from core.controller.delay import DelayLayout
from core.controller.reverb import ReverbLayout
from core.controller.graph import GraphLayout
from core.controller.audioManager import AudioManagerSettingsLayout

import logging

logging.basicConfig(level=logging.DEBUG)

class Pedal(App):
    
    templates = {
        'templates/root.kv', 
        'templates/graph.kv',
        'templates/chorus.kv',
        'templates/audioManager.kv',  
        'templates/reverb.kv', 
        'templates/delay.kv', 
    }
    
    def build(self):
        '''
            Adds all the widgets
        '''
        
        for i in self.templates:
            Builder.load_file(str(i))
    
        # grid = BoxLayout(orientation='horizontal')
        grid = GridLayout(rows=6)

        root = RootBoxLayout()
        chorus = ChorusLayout()
        delay = DelayLayout()
        reverb = ReverbLayout()
        graph = GraphLayout()
        audioManager = AudioManagerSettingsLayout()

        root.effect_chain.append(chorus.chorus)
        root.effect_chain.append(delay.delay)
        root.effect_chain.append(reverb.reverb)
        
        grid.add_widget(audioManager)
        grid.add_widget(root)
        grid.add_widget(graph)
        grid.add_widget(chorus)
        grid.add_widget(delay)
        grid.add_widget(reverb)

        return grid

    def on_start(self):
        # this method is called when the app starts
        pass

    def on_stop(self):
        # this method is called when the app stops
        pass

    def on_pause(self):
        # this method is called when the app is paused
        pass

    def on_resume(self):
        # this method is called when the app is resumed
        pass

    def on_size(self, *args):
        # this method is called when the app window size changes
        pass

def main():
    app = Pedal()
    app.run()

if __name__ == '__main__':
    main()