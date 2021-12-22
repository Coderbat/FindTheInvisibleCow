from kivy.core.audio import SoundLoader
from kivy.app import App
from kivy.properties import NumericProperty
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.clock import Clock
from kivy import*
from random import randint

class Background(Image):
    pass




class FindTheInvisibleCow(App):
    Window.size = (1280, 720)
    Window_width = (Window.width)
    Window_height = (Window.height)
    cow_size = int(((Window.height) + (Window.width)) / 21)
    cow_pos_x = randint(0 + cow_size, (Window.width) - cow_size)
    cow_pos_y = randint(0 + cow_size, (Window.height) - cow_size)
    cow_spos_x = ((cow_pos_x) / (Window_width))
    cow_spos_y = (cow_pos_y) / (Window_height)

    def touched(self,instance,touch):
        touch_x = touch.spos[0]
        touch_y = touch.spos[1]
        intensity_x = abs(self.cow_spos_x-touch_x)
        intensity_y = abs(self.cow_spos_y-touch_y)
        total_intensity = (intensity_x+intensity_x)*2
    def on_start(self):
        self.Cow_Sound = SoundLoader.load('resources\\audio\Cow.mp3')
        if self.Cow_Sound:
            self.Cow_Sound.loop = True
            self.Cow_Sound.play()

    def touched(self, instance, touch):
        touch_x = touch.spos[0]
        touch_y = touch.spos[1]
        intensity_x = abs(self.cow_spos_x - touch_x)
        intensity_y = abs(self.cow_spos_y - touch_y)
        self.Cow_Sound.volume = 2-(intensity_x + intensity_y)
        total_intensity = (intensity_x + intensity_x) * 2


if __name__ == '__main__':
    FindTheInvisibleCow().run()
