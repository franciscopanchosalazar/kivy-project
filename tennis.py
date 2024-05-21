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

    text_score_a = StringProperty(f"{counter_a}")
    text_score_b = StringProperty(f"{counter_b}")

    def add_points_a(self):
        #self.text_score_a = str(self.counter_a)

        if self.counter_a == 45:
            self.counter_a = 40

        else:
            self.counter_a += 15

        self.text_score_a = str(self.counter_a)

    def sub_points_a(self):
        self.counter_a -= 15
        self.text_score_a = str(self.counter_a)

    def add_points_b(self):
        self.counter_b += 15
        self.text_score_b = str(self.counter_b)

    def sub_points_b(self):
        self.counter_b -= 15
        self.text_score_b = str(self.counter_b)

    def reset_counters(self):
        self.text_score_a = str(self.counter_a)
        self.text_score_b = str(self.counter_b)


class Tennis(App):
    pass


Tennis().run()
