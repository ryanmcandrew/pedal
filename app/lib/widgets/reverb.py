from kivy.uix.boxlayout import BoxLayout
import lib.functions as functions

from pedalboard import Reverb

class ReverbWidget(BoxLayout):
    def __init__(self):
        super().__init__()
        self.room_size = None
        self.damping = None
        self.wet_level = None
        self.dry_level = None 
        self.reverb_width = None
        self.freeze_mode = None

        self.reverb_obj = Reverb()
        pass

    def update_reverb(self, room_size, damping, wet_level, dry_level, width, freeze_mode):
        self.room_size = room_size
        self.damping = damping
        self.wet_level = wet_level
        self.dry_level = dry_level 
        self.reverb_width = width
        self.freeze_mode = freeze_mode
        functions.update_reverb(room_size, damping, wet_level, dry_level, width, freeze_mode)
    
    def update(self, touch):
        if self.room_size_slider.collide_point(*touch.pos):
            self.reverb_obj.room_size = self.room_size_slider.value
            self.room_size_slider_label.text = "room_size - " + str(self.room_size_slider_slider.value)
            print('updated delay seconds with ' + str(self.delay_obj.room_size))
        elif self.damping_slider.collide_point(*touch.pos):
            self.reverb_obj.damping = self.damping_slider.value
            self.damping_slider_label.text = "damping - " + str(self.damping_slider.value)
            print('updated damping with ' + str(self.delay_obj.feedback))
        elif self.wet_level_slider.collide_point(*touch.pos):
            self.reverb_obj.mix = self.mix_slider.value
            self.wet_level_slider_label.text = "mix - " + str(self.wet_level_slider.value)
            print('updated mix value with ' + str(self.reverb_obj.wet_level))
        elif self.dry_level_slider.collide_point(*touch.pos):
            pass
        elif self.reverb_width_slider.collide_point(*touch.pos):
            pass
        elif self.freeze_mode_slider.collide_point(*touch.pos):
            pass

    def audio_devices(self):
        functions.audio_devices()