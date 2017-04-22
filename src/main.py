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

# python modules
import platform

import kivy
kivy.require('1.9.0')

# kivy configs
from kivy.config import Config
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'borderless', 0)

#podmienka kvoli retina displeju na macu
#automaticky sa zdvojnasobuje velkost okna.
#na win. a linux je to ok

if platform.system() == "Darwin":
    Config.set('graphics', 'height', 225)
    Config.set('graphics', 'width', 225)
else:
    Config.set('graphics', 'height', 450)
    Config.set('graphics', 'width', 450)

Config.write()

# kivy modules
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.core.window import Window


class CalcGridLayout(GridLayout):

    def __init__(self, **kwargs):
        super(CalcGridLayout, self).__init__(**kwargs)
        self.op_allowed = True

    def numpress(self, num):
        if not self.op_allowed:
            self.op_allowed = True
        self.display.text += num

    def oppress(self, op):
        if self.op_allowed:
            self.display.text += op
            self.op_allowed = False
        else: pass

    def calculate(self,calculation):
        try:
            self.display.text = str(eval(calculation))
        except Exception:
            self.display.text = 'Error'

    def delete(self):
        self.display.text = self.display.text[:-1]

    def ac(self):
        self.display.text = ""


class CalculatorApp(App):
   
    # vykreslenie
    def build(self):
        self.grid = CalcGridLayout()
        return self.grid
 
    # pomocne okno
    def dochelp(self, *args):
        box = BoxLayout();
        box.add_widget(Label(text="""Lorem ipsum dolor sit amet, \n consectetur
        \nVestibulum dictum \nvelit eu mattis bibendum.
        """, size=(600, 400), halign='center'))

        button1 = Button(text="Zatvorit okno", size_hint=(None, None),
                size=(700, 150))
        box.add_widget(button1)
        
        popup = Popup(title='Help', content=box, size_hint=(None, None),
                size=(750, 900), background_normal='', background_color=(0, 0, 0, 0.5))
        
        button1.bind(on_press=popup.dismiss)
        popup.open()


calc_inst = CalculatorApp()

## auto run 
if __name__ == "__main__":
    calc_inst.run()

