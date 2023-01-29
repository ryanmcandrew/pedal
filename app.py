import pedalboard
import pyaudio
import tests.open_tests

# from PySide2.QtWidgets import QApplication, QLabel

import sys
import tkinter as tk
from PIL import Image,ImageTk

# import tests.draw_tests
# import PySide6
# from PySide6.QtCore import Qt
# from PySide6.QtWidgets import QApplication, QLabel

def run():

    # app = QApplication(sys.argv)
    # #label = QLabel("Hello World!")
    # label = QLabel("<font color=red size=40>Hello World!</font>")
    # label.show()
    # app.exec_()
                                                     
    # app = QApplication(sys.argv)
    # label = QLabel("Hello World", alignment=Qt.AlignCenter)
    # label.show()
    # sys.exit(app.exec_())

    win = tk.Tk()

    width = 50
    height = 50

    # playButtonImg = Image.open("static/play-button.png")
    # playButtonImg = playButtonImg.resize((width,height), Image.ANTIALIAS)
    # playButtonImg =  ImageTk.PhotoImage(playButtonImg)

    # recordButtonImg = Image.open("static/record-button.png")
    # recordButtonImg = recordButtonImg.resize((width,height), Image.ANTIALIAS)
    # recordButtonImg =  ImageTk.PhotoImage(recordButtonImg)

    # # playBtnImg = tk.PhotoImage(file="static/play-button.png")
    # playPBtnImg = tk.PhotoImage(playButtonImg)
    # recordPBtnImg = tk.PhotoImage(recordButtonImg)
    
    # # playBtn = tk.Button(win, text="play", image=playPBtnImg, width=50, height=50)
    # playBtn = tk.Button(win, text="play", image=playPBtnImg)
    # # recordBtn = tk.Button(win, text="record", image=recordPBtnImg, width=50, height=50)    
    # recordBtn = tk.Button(win, text="record", image=recordPBtnImg)    

    # recordBtn.pack()
    # playBtn.pack()

    tk.mainloop()
    tests.open_tests.run()
    tests.draw_tests.main()
    st = pyaudio.Stream()

    #draw window
    #  -- record button, play button, wav drawing
    #    -- stretch: add effects 

    #record

    #playback

    #plot

    pass


run()