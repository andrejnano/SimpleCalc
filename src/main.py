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

## \mainpage SimpleCalc documentation
# 
# \section intro_sec Introduction
#
# This is the introduction about our project.
#
# \section authors_sec Authors
#  
# Andrej Nano
#
# Peter Marko
#
# Stanislav Mechl
# 

## @package main
#  Documentation for main.
#
#  More details. 

# python modules
import platform
import mat_module
import sys

reload(sys)
sys.setdefaultencoding('utf8')

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

class CalcGridLayout(GridLayout):

    def __init__(self, **kwargs):
        super(CalcGridLayout, self).__init__(**kwargs)
        self.op_allowed = False
        self.dot_allowed = True
        self.trig_allowed = True
        self.plus_allowed = True
        self.minus_allowed = True

    def dotpress(self):
        if self.dot_allowed:
            self.display.text += "."
            self.dot_allowed = False
        else: pass

    def numpress(self, num):
        if not self.op_allowed:
            self.op_allowed = True
        if not self.trig_allowed:
            self.trig_allowed = True
        if not self.plus_allowed:
            self.plus_allowed = True
        if not self.minus_allowed:
            self.minus_allowed = True
        self.display.text += num

    def signpress(self, sign):
        if sign == "+" and self.plus_allowed:
            self.display.text += sign

        elif sign == "-" and self.minus_allowed:
            self.display.text += sign


    def oppress(self, op):
        if self.op_allowed:
            self.display.text += str(op)
            self.op_allowed = False
            self.dot_allowed = True
        else: pass

    def trigpress(self, op):
        if self.trig_allowed:
            self.display.text += str(op)
            self.trig_allowed = False
        else: pass

    def calculate(self,calculation):
        try:
            self.display.text = mat_module.evaluate(str(calculation))
        except Exception:
            self.display.text = 'ERROR'

    def delete(self):
        if self.display.text[-1] == "/" or self.display.text[-1] == "*" or self.display.text[-1] == "\xe2\x88\x9a" or self.display.text[-1] == "^":
            self.op_allowed = True

        self.display.text = self.display.text[:-1]
        if self.display.text == "":
            self.op_allowed = False
            self.dot_allowed = True
            self.trig_allowed = True
            self.plus_allowed = True
            self.minus_allowed = True

    def ac(self):
        self.display.text = ""
        self.op_allowed = False
        self.dot_allowed = True
        self.trig_allowed = True
        self.plus_allowed = True
        self.minus_allowed = True


class CalculatorApp(App):
   
    # vykreslenie
    def build(self):
        self.grid = CalcGridLayout()
        self.title = "SimpleCalc"
        self.icon = "assets/favicon2.ico"
        return self.grid
 
    # pomocne okno
    def dochelp(self, *args):
        box = BoxLayout()

        label1 = (Label(text="SimpleCalc v1.0\nIVS 2016/17 projekt c. 2\n\n Kalkulacku sa da ovladat pomocou tlacidiel,\n alebo textoveho vstupu.\nV pripade trigonometrickych funkcii,\n mozte vyraz zadat v tvare 'sinx' alebo 'sin(x)'.\nObidve moznosti su spravne",
                        size=(400, 150), pos_hint={'top': 1.15}, halign='left'))

        button1 = Button(text="X", size_hint_x=None, size_hint_y=None,
                         size=(45, 45), background_normal='', background_color=(0.204,0.596,0.859,1))

        box.add_widget(label1)
        box.add_widget(button1)

        popup = Popup(title='Informacie k pouzivaniu', content=box, size_hint=(None, None),
                size=(400, 350), background_normal='', background_color=(0, 0, 0, 0.5))
        
        button1.bind(on_press=popup.dismiss)
        popup.open()


calc_inst = CalculatorApp()

## auto run 
if __name__ == "__main__":
    calc_inst.run()

