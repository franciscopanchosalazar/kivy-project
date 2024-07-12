from kivy.core.audio import SoundLoader

from kivy.app import App
from kivy.graphics import Ellipse, Color, Rectangle
from kivy.properties import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.metrics import dp

hit = SoundLoader.load('tennis hit.mp3')


class BallExercise(Widget):     # The following classes are working in a bouncing ball project
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # I use these variables to locate the ball in the centre of the screen
        self.x_center = None
        self.y_center = None
        self.ball_diameter = dp(50)

        # Ball velocity
        self.vx = 7
        self.vy = 8

        Clock.schedule_interval(self.update, 1/60)

        with self.canvas:
            self.my_bg = Rectangle(source='tennis court.jpg', pos=(0, 0), size=self.size)

            Color(1, 1, 1, 1)
            self.ball_shadow = Ellipse(pos=(0, 0), size=(self.ball_diameter + 5, self.ball_diameter + 5))

            Color(160/255, 201/255, 36/255, 1)
            self.ball = Ellipse(pos=(0, 0), size=(self.ball_diameter, self.ball_diameter))

    def on_size(self, *args):
        self.x_center = self.center_x - self.ball_diameter / 2
        self.y_center = self.center_y - self.ball_diameter / 2
        # Initially (init method), the ball is in the corner of the screen, so we
        # update the position immediately
        self.ball.pos = (self.x_center, self.y_center)
        self.my_bg.size = self.size     # update bg size

    def update(self, dt):
        x, y = self.ball.pos

        x += self.vx
        y += self.vy

        self.ball.pos = (x, y)
        self.ball_shadow.pos = (x - 2.5, y - 2.5)
        
        if y + self.ball_diameter > self.height:
            y = self.height - self.ball_diameter
            self.vy = self.vy * -1
            hit.play()

        if x + self.ball_diameter > self.width:
            x = self.width - self.ball_diameter
            self.vx = self.vx * -1
            hit.play()

        if y <= 0:
            y = 0
            self.vy = self.vy * -1
            hit.play()

        if x <= 0:
            x = 0
            self.vx = self.vx * -1
            hit.play()


class CoordinatesExample(BoxLayout):   # This is an exercise to draw different canvas in a layout
    pass


class Course(App):
    pass


Course().run()
