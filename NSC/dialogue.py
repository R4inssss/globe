import pygame
from config import *
from main import *
from protocols import *
from score import *
from sprites import *


class DialogueProgram:
    def __init__(self):
        pass


class MainText:
    def __init__(self):
        self.A1text = None
        self.B1text = None
        self.C1text = None
        self.E1text = None
        self.A2text = None
        self.B2text = None
        self.C2text = None
        self.E2text = None

    def AirDialogue(self):
        self.A1text = [{'A': 'Gas-powered transportation'}, {'B': 'Electric Transportation'},
                  {'C': 'Human Powered Transportation'}, {'D': 'Water Transportation'}]
        self.A2text = [{'A': '', 'B': '', 'C': '', 'D': ''}]

    def CarbonDialogue(self):
        self.B1text = [{}, {}, {}, {}]
        self.B2text = [{}, {}, {}, {}]

    def SurfaceDialogue(self):
        self.C1text = [{}, {}, {}, {}]
        self.C2text[{}, {}, {}, {}]


    def WaterDialogue(self):
        self.E1text = [{}, {}, {}, {}]
        self.E2text = [{}, {}, {}, {}]

