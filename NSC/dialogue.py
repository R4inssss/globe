import pygame
from config import *
from main import *
from protocols import *
from score import *
from sprites import *



class DialogueProgram():
    def __init__(self):
        self = self
        pass


class MainText():
    def __init__(self):
        self = self


    def AirDialogue(self):
        Atext = [[{'A':'Gas-powered transportation'},{'B':'Electric Transportation'},{'C':'Human Powered Transportation'},{'D':'Water Transportation'}],
                 [{'A':'','B':'', 'C':'', 'D':''}]]

    def CarbonDialogue(self):
        Btext = [[{},{},{},{}],
                 [{},{},{},{}]]

    def SurfaceDialogue(self):
        Ctext = [[{},{},{},{}],
                 [{},{},{},{}]]
    
    def WaterTemp(self):
        Dtext = [[{},{},{},{}],
                 [{},{},{},{}]]

