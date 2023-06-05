from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
import logging
from core.audio import AudioStream
import core.audio
import pedalboard

class ChorusLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.chorus = pedalboard.Chorus()

    def do_layout(self, *largs):
        # This method is called when we need to recalculate the layout
        super().do_layout(largs)

    def add_widget(self, widget, index=0, canvas=None):
        # This method is called when we add a new widget to the layout
        super().add_widget(widget, index=index, canvas=canvas)

    def remove_widget(self, widget):
        # This method is called when we remove a widget from the layout
        super().remove_widget(widget)

    def clear_widgets(self, children_only=False):
        # This method is called when we clear all widgets from the layout
        super().clear_widgets(children_only=children_only)

    def update(self, type_to_update, value ):
        if type_to_update == 'rate':
            self.chorus.rate_hz = value
        elif type_to_update == 'depth':
            self.chorus.depth = value
        elif type_to_update == 'centre delay':
            self.chorus.centre_delay_ms = value
        elif type_to_update == 'feedback':
            self.chorus.feedback = value
        elif type_to_update == 'mix':
            self.chorus.mix = value