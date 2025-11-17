import pygame

from .entity import entity

image = pygame.image.load("Assets/Player/player.png")

class player(entity):
    def __init__(self, *groups, image: pygame.image = image, pos: tuple = (0, 0)):
        super().__init__(*groups, image=pygame.transform.scale(image, (image.get_width() * 6, image.get_height() * 6)), pos=pos)
        
    def update(self):

        return super().update()