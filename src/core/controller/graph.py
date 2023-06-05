from kivy.uix.boxlayout import BoxLayout
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivy.uix.floatlayout import FloatLayout
import matplotlib.pyplot as plt
import librosa
import core.audio

class GraphLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.graph = self.ids.graph

        # x = [1,2,3]
        # y = [5,6,7]
        # plt.plot(x,y)
        # self.dev_canvas = FigureCanvasKivyAgg( plt.gcf() )
        # self.graph.add_widget(self.dev_canvas)
        self.build_graph()

    def build_graph(self):
        
        fig, ax = plt.subplots(1,1)
        plt.ylabel = 'Amplitude'
        y, samplingRate = librosa.load(core.audio.WAV_FILE_READ, sr=22050)
        librosa.display.waveshow(y, sr=samplingRate, ax=ax, x_axis='time')
        self.dev_canvas = FigureCanvasKivyAgg( fig )

        self.graph.add_widget(self.dev_canvas)