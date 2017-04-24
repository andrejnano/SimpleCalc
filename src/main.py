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
# Peter Marko
# Stanislav Mechl
# 

## @package main
#  Documentation for main.
#

# python modules
import platform
import mat_module
import sys

##
# app requires utf-8 encoding to properly display some symbols
reload(sys)
sys.setdefaultencoding('utf8')

##
# app uses kivy 1.9.0 as a GUI framework
# https://kivy.org/
import kivy
kivy.require('1.9.0')

# kivy configs
from kivy.config import Config
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'borderless', 0)

##
# condition for macbook retina display
# macOS doubles the app window resolution, which causes bugged gui
# not important for other platforms
if platform.system() == "Darwin":
    Config.set('graphics', 'height', 225)
    Config.set('graphics', 'width', 225)
else:
    Config.set('graphics', 'height', 475)
    Config.set('graphics', 'width', 450)

##
# updates kivy configuration file
Config.write()

# kivy modules import
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.button import Button

##
# custom kivy GUI layout class
# @class CalcGridLayout
class CalcGridLayout(GridLayout):

##
# Creator method to setup Calculator instance
# @desc overrides the class init method and sets input rules with boolean flags,
# @param self, kwargs
    def __init__(self, **kwargs):
        super(CalcGridLayout, self).__init__(**kwargs)
        self.op_allowed = False
        self.dot_allowed = True
        self.trig_allowed = True
        self.plus_allowed = True
        self.minus_allowed = True
##
# Method to check if dot printing is allowed 
# @param self
# @pre input of dot is allowed (flag is true)
# @return prints dot if the condition was true, otherwise nothing
    def dotpress(self):
        if self.dot_allowed:
            self.display.text += "."
            self.dot_allowed = False
            self.op_allowed = False
            self.plus_allowed = False
            self.minus_allowed = False
            self.trig_allowed = False
        else: pass

##
# Method to adjust flags when a number was pressed
# @param self, num
# @return updates the display.text with the new number
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

##
# Method to adjust flags when a sign was pressed
# @param self, sign
# @desc updates the display.text with the new sign symbol
    def signpress(self, sign):
        if sign == "+" and self.plus_allowed:
            self.display.text += sign
            self.dot_allowed = True
            self.op_allowed = False
            self.trig_allowed = True
        elif sign == "-" and self.minus_allowed:
            self.display.text += sign
            self.dot_allowed = True
            self.op_allowed = False
            self.trig_allowed = True
        else: pass

##
# Method to adjust flags when an operation was pressed
# @param self, op
# @desc updates the display.text with the new operation symbol
    def oppress(self, op):
        if self.op_allowed:
            self.display.text += str(op)
            self.op_allowed = False
            self.dot_allowed = True
            self.trig_allowed = True
        else: pass

##
# Method to adjust flags when a trigonometric function was pressed
# @param self, op
# @desc updates the display.text with the new trig. op symbol
    def trigpress(self, op):
        if self.trig_allowed:
            self.display.text += str(op)
            self.trig_allowed = False
        else: pass

##
# Result calculation method, uses 'mat_module' module
# @param self, calculation
# @desc passes string from display.text to mat_module to calculate the equation
# @pre mat_module evaluation returns no exception
    def calculate(self,calculation):
        try:
            self.display.text = mat_module.evaluate(str(calculation))
        except Exception:
            self.display.text = 'ERROR'
##
# Character deleting method.
# @param self
# @desc deletes the last character in display.text
# @pre display.text is already empty -> resets flags
# @pre to be deleted character is an operation -> adjusts flags
    def delete(self):
        if self.display.text == "":
            self.op_allowed = False
            self.dot_allowed = True
            self.trig_allowed = True
            self.plus_allowed = True
            self.minus_allowed = True
            return
        if self.display.text[-1] == "/" or self.display.text[-1] == "*" or self.display.text[-1] == "\xe2\x88\x9a" or self.display.text[-1] == "^":
            self.op_allowed = True

        self.display.text = self.display.text[:-1]

##
# All clean method.
# @desc deletes the whole string in display.text and resets flags
# @param self
    def ac(self):
        self.display.text = ""
        self.op_allowed = False
        self.dot_allowed = True
        self.trig_allowed = True
        self.plus_allowed = True
        self.minus_allowed = True



##
# main application instance class
# @class CalculatorApp
class CalculatorApp(App):

##
# Kivy method to build the GUI
# @param self
# @brief defines apps layout, title and icon
# @return gui layout
    def build(self):
        self.grid = CalcGridLayout()
        self.title = "SimpleCalc"
        self.icon = "assets/favicon2.ico"
        return self.grid

##
# Method to generate help popup
# @param self, args (not used)
# @desc adds a new widget, a help popup, to the kivy layout
    def dochelp(self, *args):
        box = BoxLayout()
        popup = Popup(title='Informacie k pouzivaniu', content=box, size_hint=(None, None), size=(400, 350), background_normal='', background_color=(0, 0, 0, 0.5))
        label1 = (Label(text="SimpleCalc v1.0 - IVS 2016/17 projekt c. 2\n\n Kalkulacku lze ovladat pomoci tlacitek,\n nebo textoveho vstupu.\n\nPriklady zadani vyrazu:\nx^y  -  x na y\ny\xe2\x88\x9ax  -  y odmocnina z x\nx!  -  x faktorial\nsin(x)  -  sinus x\nsinx  -  ekvivalentni s predchozim radkem",
                        size=(400, 150), pos_hint={'top': 1.15}, halign='left'))
        button1 = Button(text="X", size_hint_x=None, size_hint_y=None,
                         size=(45, 45), background_normal='', background_color=(0.204,0.596,0.859,1))
        box.add_widget(label1)
        box.add_widget(button1)
        button1.bind(on_press=popup.dismiss)
        popup.open()

##
# creates Calculator instance
calc_inst = CalculatorApp()

##
# automatic
if __name__ == "__main__":
    calc_inst.run()

