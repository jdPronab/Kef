from kivy.app import App
from kivy.clock import Clock
from kivy.vector import Vector
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty, ObjectProperty, ReferenceListProperty, ListProperty
from kivy.core.window import Window

import random



class Emoji(Image):
	root = ObjectProperty(None)
	velocity_x = NumericProperty(0)
	velocity_y = NumericProperty(0)
	velocity = ReferenceListProperty(velocity_x, velocity_y)

	def __init__(self, recognition, *args, **kwargs):
		super().__init__(**kwargs)
		self.recognition = recognition

	def spawn(self):
		'''TODO:// spawn mode ['eruption', 'circle']'''
        #self.pos = Vector(*self.kefmain.center)
		self.pos =  Vector(*self.parent.center)

	def move(self):
		try:
			self.pos = Vector(*self.velocity) + self.pos
		except Exception as e:
			print(e)
			print(self.pos)
			print(self.velocity)

class KefMain(FloatLayout):
    eggplant = ObjectProperty(None)
    middle_finger = ObjectProperty(None)
    kscore = NumericProperty(0)
    fscore = NumericProperty(0)

    def kspawn(self):
        ep  = Emoji(
			'eggplant',
            #velocity_x = random.choice(self.direction), #randint(-180, 180),
            #velocity_y = random.choice(self.direction), #randint(-180, 180),
            velocity_x = random.randint(-10, 10) * random.random(),
            velocity_y = random.randint(-10, 10) * random.random(),
            source="./img/eggplant-w.png"
            )
        self.add_widget(ep)

    def fspawn(self):
        mf = Emoji(
			'middle-finger',
            #velocity_x = random.choice(self.direction), #randint(-180, 180),
            #velocity_y = random.choice(self.direction), #randint(-180, 180),
            velocity_x = random.randint(-10, 10) * random.random(),
            velocity_y = random.randint(-10, 10) * random.random(),
            source="./img/middle-finger.png"
            )
        self.add_widget(mf)

    def update(self, dt):
        if len(self.children) > 4:
            half_window_width = Window.width / 2     # GET HALF OF WINDOWS's WIDTH
            half_window_height = Window.height / 2 # GET HALF OF WINDOWS's WIDTH
            for child in self.children[:-4]:
                if child.y > Window.height - half_window_height or child.y < 0 - half_window_height or child.x > Window.width - half_window_width or  child.x < 0 - half_window_width:
                    if child.recognition == 'eggplant':
                        self.kscore += 1
                    else:
                        self.fscore += 1
                    self.remove_widget(child)
                child.x += child.velocity_x
                child.y += child.velocity_y
                child.move()

class KefApp(App):
    def build(self):
        game = KefMain()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game


if __name__ == '__main__':
    KefApp().run()
