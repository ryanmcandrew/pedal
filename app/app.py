import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

import lib.widgets.chorus
import lib.widgets.reverb
import lib.widgets.delay
import lib.widgets.toolbar

class PedalsApp(BoxLayout, App):
    def build(self):
        global delay_widget
        
        grid = GridLayout(rows=4)
        grid.add_widget(toolbar_widget)
        # grid.add_widget(lib.widgets.chorus.ChorusWidget())
        grid.add_widget(chorus_widget)
        grid.add_widget(reverb_widget)
        grid.add_widget(delay_widget)
        # self.add_widget(lib.widgets.chorus.ChorusWidget())
        # self.add_widget(lib.widgets.reverb.ReverbWidget())
        # # self.add_widget(lib.widgets.delay.DelayWidget())
        return grid
        pass

delay_widget = lib.widgets.delay.DelayWidget()
# delay_widget = None
 
if __name__ == '__main__':

    Builder.load_file("templates/chorus.kv")
    Builder.load_file("templates/reverb.kv")
    Builder.load_file("templates/toolbar.kv")
    
    toolbar_widget = lib.widgets.toolbar.ToolbarWidget()
    reverb_widget = lib.widgets.reverb.ReverbWidget()
    chorus_widget = lib.widgets.chorus.ChorusWidget()

    # Builder.load_file("templates/delay.kv")
    kv = PedalsApp()
    kv.run()