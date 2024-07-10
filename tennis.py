from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from kivy.app import App

counter_a = 0
counter_b = 0


class MainBox(BoxLayout):
    pass


class MainGrid(GridLayout):
    counter_a = 0
    counter_b = 0

    # Whatever is inside the StringProperty will be displayed in our Labels (in the kv file)
    text_score_a = StringProperty(f"{counter_a}")
    text_score_b = StringProperty(f"{counter_b}")

    def add_points_a(self):
        if self.counter_a < 30:
            self.counter_a += 15

        elif self.counter_a == 30:
            self.counter_a += 10

        elif 40 <= self.counter_a < 45:
            self.counter_a += 1

        self.text_score_a = str(self.counter_a)

    def sub_points_a(self):
        if 0 != self.counter_a <= 30:
            self.counter_a -= 15

        elif 30 < self.counter_a <= 40:
            self.counter_a -= 10

        elif 40 <= self.counter_a < 45:
            self.counter_a -= 1

        self.text_score_a = str(self.counter_a)

    def add_points_b(self):
        if self.counter_b < 30:
            self.counter_b += 15

        elif self.counter_b == 30:
            self.counter_b += 10

        elif 40 <= self.counter_b < 45:
            self.counter_b += 1

        self.text_score_b = str(self.counter_b)

    def sub_points_b(self):
        if 0 != self.counter_b <= 30:
            self.counter_b -= 15

        elif 30 < self.counter_b <= 40:
            self.counter_b -= 10

        elif 40 <= self.counter_b < 45:
            self.counter_b -= 1

        self.text_score_b = str(self.counter_b)

    def reset_counters(self):
        self.text_score_a = str(self.counter_a)
        self.text_score_b = str(self.counter_b)


class Tennis(App):
    pass


Tennis().run()
