#!/bin/python3

'''
SimpleCalc
2. projekt IVS / 2017
@ FIT VUT, BRNO

Peter Marko
Stanislav Mechl
Andrej Nano
''' 
    
import kivy

from kivy.app import App

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
class CalcGridLayout(GridLayout):
        # self.display.text = 
    def calculate(self,calculation):
        try:
            self.display.text = str(eval(calculation))
        except Exception:
            self.display.text = 'Error'


class CalculatorApp(App):

    def build(self):
        
        return CalcGridLayout()

calcApp = CalculatorApp()
calcApp.run()
