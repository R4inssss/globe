# implementation of protocols 
import pygame
import sys
from config import *
from main import Game
from main import *
import math


# Game.event functions 
# C


class GlobalWarming:
    def __init__(self):
        pass

# Updating current answering logic
    def answer_key(self, key1, key2):
        # TODO: Check if answer matches answer key, if answer key matches the answer then return bool value?
        if key1 == key2:
            return True
        return False

    def border123(self, correct, border_size_plus):
        if correct:
            border_size_plus += 10
        else:
            border_size_plus -= 100
        return border_size_plus
