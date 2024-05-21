from kivy.app import App
from kivy.metrics import dp
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout


class MyStack(StackLayout): # Used to Add multiple buttons
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(1, 101):
            b = Button(text=f"{i}", size_hint=(None, None), size=(dp(50), dp(50)))
            self.add_widget(b)


class MyKivy(App):
    pass


MyKivy().run()
