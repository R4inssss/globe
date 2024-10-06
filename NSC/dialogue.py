import pygame
from config import *
from main import *
from protocols import *
from score import *
from sprites import *


class DialogueProgram():
    def __init__(self):
        pass


class MainText():
    def __init__(self):
        self.Atext = None
        self.Btest = None
        self.Ctext = None
        self.Etext = None

    def AirDialogue(self):
        self.Atext = [[{'A': 'Gas-powered transportation'}, {'B': 'Electric Transportation'},
                  {'C': 'Human Powered Transportation'}, {'D': 'Water Transportation'}],
                 [{'A': '', 'B': '', 'C': '', 'D': ''}]]

    def CarbonDialogue(self):
        self.Btext = [[{}, {}, {}, {}],
                 [{}, {}, {}, {}]]

    def SurfaceDialogue(self):
        self.Ctext = [[{}, {}, {}, {}],
                 [{}, {}, {}, {}]]

    def WaterDialogue(self):
        self.Etext = [[{}, {}, {}, {}],
                 [{}, {}, {}, {}]]

