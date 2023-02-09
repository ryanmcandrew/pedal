from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from kivy.uix.slider import Slider
from kivy.uix.label import Label

import lib.functions as functions

from pedalboard import Delay

class DelayWidget(BoxLayout):

    def __init__(self) -> None:
        
        super().__init__()
        self.delay_obj = Delay()
        self.delay_obj.delay_seconds = 0.5
        self.delay_obj.feedback = 0.3
        self.delay_obj.mix = 0.5

        self.widget_name_label = Label()
        self.widget_name_label.text = "Delay - " 
        self.add_widget(self.widget_name_label)
        
        self.delay_seconds_slider = Slider()
        self.delay_seconds_slider.min = 0
        self.delay_seconds_slider.max = 30
        self.delay_seconds_slider.orientation = "vertical" 
        self.delay_seconds_slider_label = Label()
        self.delay_seconds_slider_label.text = "delay_seconds"
        self.add_widget(self.delay_seconds_slider)
        self.add_widget(self.delay_seconds_slider_label)
        
        self.feedback_slider = Slider()
        self.feedback_slider.min = 0
        self.feedback_slider.max = 1
        self.feedback_slider.step = 0.01
        self.feedback_slider_label = Label()
        self.feedback_slider_label.text = "feedback"
        self.feedback_slider.orientation = "vertical" 
        self.add_widget(self.feedback_slider)
        self.add_widget(self.feedback_slider_label)
        
        self.mix_slider = Slider()
        self.mix_slider.min = 0
        self.mix_slider.max = 1
        self.mix_slider.step = 0.01
        self.mix_slider.value = 0.6
        self.mix_slider_label = Label()
        self.mix_slider_label.text = "mix - " + str(self.mix_slider.value)
        self.mix_slider.orientation = "vertical" 
        self.add_widget(self.mix_slider)
        self.add_widget(self.mix_slider_label)

    
    def update_delay(self, delay_seconds, feedback, mix):
        # self.delay_seconds = delay_seconds
        # self.feedback = feedback
        # self.mix = mix
        # self.delay_obj.delay_seconds = delay_seconds
        # self.delay_obj.feedback = feedback
        # self.delay_obj.mix = mix
        functions.update_delay(delay_seconds, feedback, mix)

    def on_touch_move(self, touch):
        if self.delay_seconds_slider.collide_point(*touch.pos):
            self.delay_obj.delay_seconds = self.delay_seconds_slider.value
            self.delay_seconds_slider_label.text = "delay_seconds - " + str(self.delay_seconds_slider.value)
            print('updated delay seconds with ' + str(self.delay_obj.delay_seconds))
        elif self.feedback_slider.collide_point(*touch.pos):
            self.delay_obj.feedback = self.feedback_slider.value
            self.feedback_slider_label.text = "feedback - " + str(self.feedback_slider.value)
            print('updated feedback with ' + str(self.delay_obj.feedback))
        elif self.mix_slider.collide_point(*touch.pos):
            self.delay_obj.mix = self.mix_slider.value
            self.mix_slider_label.text = "mix - " + str(self.mix_slider.value)
            print('updated mix value with ' + str(self.delay_obj.mix))
        
