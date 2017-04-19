#!/bin/python

# + ----------------------- +
# |   SimpleCalc            |
# |   2. projekt IVS / 2017 |
# |   @ FIT VUT, BRNO       |
# |                         |
# |   Peter Marko           |
# |   Stanislav Mechl       |
# |   Andrej Nano           |
# + ----------------------- +   

import mathFunc
import kivy
from kivy.config import Config
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window


# kivy configs
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'height', 900)
Config.set('graphics', 'width', 600)
Config.set('graphics', 'borderless', 0)
Config.write()

class CalcGridLayout(GridLayout):
    def calculate(self,calculation):
        try:
            self.display.text = str(eval(calculation))
        except Exception:
            self.display.text = 'Error'

class CalculatorApp(App):
    def build(self):
        return CalcGridLayout()

if __name__ == "__main__":
    CalculatorApp().run()

