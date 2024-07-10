from kivy.app import App
from kivy.graphics import Ellipse
from kivy.metrics import dp
from kivy.properties import Clock
from kivy.uix.widget import Widget
import random


class CanvasOne(Widget):
    pass


class BouncingBall(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Screen size x, y
        self.screen_x = None
        self.screen_y = None
        self.limit = 0

        # Ball´s position, size and velocity
        self.my_center_x = None
        self.my_center_y = None
        self.ball_size = dp(50)
        self.vx = dp(3)
        self.vy = dp(4)

        # This class method is used to permanently call a function within a time interval
        # In this case we use 1/60 as we are working at 60 frames per second (we can change it)
        Clock.schedule_interval(self.update, 1/60)

        # Canvas initialization (if you will)
        with self.canvas:
            self.ball = Ellipse(pos=(0, 0), size=(self.ball_size, self.ball_size))

    def on_size(self, *args):
        # Here we located the ball in the middle of the screen
        # we need to subtract half of the size cause the location of our ball
        # start on the down-left corner of an imaginary rectangle around the ball
        self.my_center_x = self.center_x - self.ball_size/2
        self.my_center_y = self.center_y - self.ball_size/2
        self.ball.pos = (self.my_center_x, self.my_center_y)

        # We storages the size of the screen, so we can use its values
        self.screen_x = self.width
        self.screen_y = self.height
        print(self.screen_x, self.screen_y)     # Just to check if its working

    # as the following function is called by the clock we must add a second parameter call
    # by convention delta time (dt)
    def update(self, dt):

        if (self.my_center_x + self.ball_size < self.screen_x and self.limit == 0
                or self.my_center_y + self.ball_size < self.screen_y and self.limit == 0):

            self.my_center_x += self.vx
            self.my_center_y += self.vy
            self.ball.pos = (self.my_center_x, self.my_center_y)

            if (self.my_center_x + self.ball_size >= self.screen_x
                    or self.my_center_y + self.ball_size >= self.screen_y):
                self.limit = 1

        elif (self.my_center_x > 0 and self.limit == 1
                or self.my_center_y < self.screen_y and self.limit == 1):
            self.my_center_x -= self.vx
            self.my_center_y -= self.vy
            self.ball.pos = (self.my_center_x, self.my_center_y)

            if self.my_center_x <= 0 or self.my_center_y <= 0:
                self.limit = 0


class Board(App):
    pass


Board().run()
