#!/usr/local/bin/python

'''

SimpleCalc
2. projekt IVS / 2017
@ FIT VUT, BRNO

Peter Marko
Stanislav Mechl
Andrej Nano

'''

from kivy.app import App
from kivy.uix.button import Button
message_var = "Click here"

class TestApp(App):
    def build(self):
        return Button(text=message_var)

TestApp().run()

#byl jsem tady! S
