from kivy.uix.boxlayout import BoxLayout

from pedalboard import Pedalboard, Chorus, Reverb, Delay
import lib.functions as functions

class ChorusWidget(BoxLayout):
    def __init__(self) -> None:
        super().__init__()
        self.rate = 0.0
        self.depth = 0.0
        self.centre_delay = 0.0
        self.feedback = 0.0
        self.mix = 0.0

        # self.widget_name_label = Label()
        # self.widget_name_label.text = "Chorus - " 
        # self.add_widget(self.widget_name_label)
        
        # self.rate_slider = Slider()
        # self.rate_slider.min = 0
        # self.rate_slider.max = 30
        # self.rate_slider.value = self.chorus_obj.rate
        # self.rate_slider.orientation = "vertical" 
        # self.rate_slider_label = Label()
        # self.rate_slider_label.text = "rate - " + self.chorus_obj.rate
        # self.add_widget(self.delay_seconds_slider)
        # self.add_widget(self.delay_seconds_slider_label)

        self.chorus_obj = Chorus()

    def update_chorus(self, rate, depth, centre_delay, feedback, mix):
        self.rate = rate
        self.depth = depth
        self.centre_delay = centre_delay
        self.feedback = feedback
        self.mix = mix

        self.rate_slider = 0
        self.depth_slider = 0
        self.centre_delay_slider = 0
        self.feedback_slider = 0
        self.mix_slider = 0

        functions.update_chorus(rate, depth, centre_delay, feedback, mix)

    def update(self, touch):
        if self.rate_slider.collide_point(*touch.pos):
            pass
        elif self.depth_slider.collide_point(*touch.pos):
            pass
        elif self.centre_delay_slider.collide_point(*touch.pos):
            pass
        elif self.feedback_slider.collide_point(*touch.pos):
            pass
        elif self.mix_slider.collide_point(*touch.pos):
            pass

    def on_touch_move(self, touch):
        pass
        print('updating chorus')
        # print('chorus')
        # print("----------------------------------------------------------------")
        # print(touch.grab(self))
        # print('touch id: ' + str(touch.id))