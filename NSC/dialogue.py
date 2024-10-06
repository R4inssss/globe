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
        self.A2text = [{'A': 'Industrial factory emissions', 'B': 'Burning of Fossil Fuels',
                        'C': 'Transportation emissions', 'D': 'Agricultural practices'}]

    def WaterDialogue(self):
        self.B1text = [{'A': '0°C to 5°C'}, {'B': '10°C to 18°C'}, {'C': '18°C to 22°C'}, {'D': '22°C to 28°C'}]
        self.B2text = [{'A': 'Does not impact salmon populations'}, {'B': 'Increases salmon reproduction rates'},
                       {'C': 'Decreases oxygen levels, impacting fish survival'}, {'D': 'Decreases salmon population'}]

    def CarbonDialogue(self):
        self.C1text = [{'A': 'Non-veg diet including beef/pork'}, {'B': 'A plant-based diet'},
                       {'C': 'Vegetarian diet'}, {'D': 'Non-veg diet including only chicken'}]
        self.C2text = [{'A': 'Operating a gasoline-powered car'}, {'B': 'Using energy-efficient home appliances'},
                       {'C': 'Conserving water usage'}, {'D': 'Flying frequently'}]

    def SurfaceDialogue(self):
        self.E1text = [{'A': ''}, {'B': ''}, {'C': ''}, {'D': ''}]
        self.E2text = [{'A': ''}, {'B': ''}, {'C': ''}, {'D': ''}]

