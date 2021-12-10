from kivy.core.audio import SoundLoader
from kivy.app import App
from kivy.properties import NumericProperty
from kivy.uix.widget import Widget
from kivy.core.window import Window

from random import randint




class Cow(Widget):
    pass




class FindTheInvisibleCow(App):
    Window.size = (1280, 720)
    cow_size = int(((Window.height)+(Window.width))/21)
    cow_pos_x = randint(0+cow_size,(Window.width)-cow_size)
    cow_pos_y = randint(0+cow_size,(Window.height)-cow_size)

    def build(self):
        sound = SoundLoader.load("resources\\audio\Cow.mp3")
        if sound:
            sound.play()
        return Cow()


FindTheInvisibleCow().run()
