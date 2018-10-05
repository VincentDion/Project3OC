# -*- coding: Utf-8 -*

"""Classes for the game MacGyver escapes !"""

import pygame
from pygame.locals import * 
from constants import *

class Level:
    """
    Creation of level class
    """

    def __init__(self, file):
        """
        Initialization of the Level class
        """
        self.file = file
        self.structure = 0

    def generate(self):
        """
        Method to generate a level based on a file.
        Creation of a global list, with a list for each line in the file within
        """	
        with open(self.file, "r") as file:
            #Main list
            level_structure = []
            for line in file:
                #"Line list", one for each line
                level_line = []
                for sprite in line:
                    if sprite != '\n':
                        level_line.append(sprite)
                level_structure.append(level_line)
            self.structure = level_structure

    def show_game(self, window):
        """
        Method to display the game according to the list in generate() 
        Only walls, a tile for start and stairs for finish are displayed
        No graphic clue for the Test tile
        """
        wall = pygame.image.load(IMAGE_WALL).convert_alpha()
        stairs = pygame.image.load(IMAGE_STAIRS).convert_alpha()
        start = pygame.image.load(IMAGE_START).convert()

        num_line = 0
        for line in self.structure:
            num_case = 0
            for sprite in line:
                #Conversion of the case position in pixels
                x = num_case * SIZE_SPRITE
                y = num_line * SIZE_SPRITE
                if sprite == 'W':		   
                    window.blit(wall, (x,y))
                elif sprite == 'S':		   
                    window.blit(start, (x,y))
                elif sprite == 'F':		   
                    window.blit(stairs, (x,y))
                num_case += 1
            num_line += 1


class Characters:
    """
    Creation of the Characters class, 
    corresponding to the characters controlled by the user,
    and the badguy at the end.
    """
    def __init__(self, sprite, level, case_x, case_y):
        """
        Initialization of Hero class, attributes concern its sprite,
        position in pixel and case and the level is in
        """
        self.sprite = pygame.image.load(sprite).convert_alpha()
        self.case_x = case_x
        self.case_y = case_y
        self.x = case_x * SIZE_SPRITE
        self.y = case_y * SIZE_SPRITE
        #in case there are more than one level in near future
        self.level = level


    def move(self, direction):
        """
        Method for the movement of the hero, use of the directional keys
        """
        if direction == 'right':
            #In order to avoid going out of the screen, right and bottom only
            if self.case_x < (NUMBER_SPRITE_SIDE - 1):
                #Forbid the user to move in a wall
                if self.level.structure[self.case_y][self.case_x+1] != 'W':
                    #Move of one case and its conversion in pixels
                    self.case_x += 1
                    self.x = self.case_x * SIZE_SPRITE
            self.direction = self.sprite

        if direction == 'left':
            if self.case_x > 0:
                if self.level.structure[self.case_y][self.case_x-1] != 'W':
                    self.case_x -= 1
                    self.x = self.case_x * SIZE_SPRITE
            self.direction = self.sprite

        if direction == 'up':
            if self.case_y > 0:
                if self.level.structure[self.case_y-1][self.case_x] != 'W':
                    self.case_y -= 1
                    self.y = self.case_y * SIZE_SPRITE
            self.direction = self.sprite

        if direction == 'down':
            if self.case_y < (NUMBER_SPRITE_SIDE - 1):
                if self.level.structure[self.case_y+1][self.case_x] != 'W':
                    self.case_y += 1
                    self.y = self.case_y * SIZE_SPRITE
            self.direction = self.sprite

    def sleep(self, sprite, level, case_x, case_y):
        """
        Simple method to change the sprite of the agent,
        This method concerns the enemies of the hero
        """
        self.sprite = pygame.image.load(sprite).convert_alpha()

        self.case_x = case_x
        self.case_y = case_y
        self.x = case_x * SIZE_SPRITE
        self.y = case_y * SIZE_SPRITE
        self.level = level



class QuestObjects:
    """
    Creation of the class for the objects needed to finish the level.
    Item are randomly placed but in the main code : mge_game.py
    When the user grab an item, it is displaced to the inventory bar
    """
    def __init__(self, sprite, level, case_x, case_y):
        """
        Initialization of QuestObjects class, with attributes of position,
        in case and pixels, and level they are in
        """
        self.sprite = pygame.image.load(sprite).convert_alpha()
        self.level = level
        self.case_x = case_x
        self.case_y = case_y
        self.x = case_x * SIZE_SPRITE
        self.y = case_y * SIZE_SPRITE

    def move_inventory(self, pos_x, pos_y):
        """
        Method for moving the grabbed item in the inventory
        For now the new position are given in the main code.
        Must be changed soon to be implemented directly in this method
        """
        self.x = pos_x
        self.y = pos_y
