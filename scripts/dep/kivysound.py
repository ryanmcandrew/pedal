class AppSoundLoader():

    def __init__(self):
        self.sound = SoundLoader.load(WAV_FILE_READ)

    def load(self):
        self.sound = SoundLoader.load(WAV_FILE_READ)

    def play_wav(self):
        
        print('test2')
        test_one()
        print('test3')
        if sound:
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
            # test_one()
            sound.play()

    def stop_wav(self):
        if sound:
            sound.stop()

    def seek_wav(self, value):
        if sound:
            sound.seek(value)