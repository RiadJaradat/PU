import pygame

from .entity import entity

image = pygame.image.load("Assets/Player/player.png")

class player(entity):
    def __init__(self, *groups, image: pygame.image = image, pos: tuple = (0, 0)):
        super().__init__(*groups, image=image, pos=pos)
        
    def update(self):

        return super().update()