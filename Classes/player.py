import pygame

from .entity import entity

scale = 4

image_right = pygame.image.load("Assets/Player/player_right.png")
image_right = pygame.transform.scale(image_right, (image_right.get_width() * scale, image_right.get_height() * scale))
image_left = pygame.image.load("Assets/Player/player_left.png")
image_left = pygame.transform.scale(image_left, (image_left.get_width() * scale, image_left.get_height() * scale))

class player(entity):
    def __init__(self, *groups, image: pygame.image = image_left, pos: tuple = (0, 0)):
        super().__init__(*groups, image=image, pos=pos)
        self.direction = pygame.math.Vector2()
        self.old_pos = self.rect.topleft
        self.speed = 8
        self.mask = pygame.mask.from_surface(self.image)

    def inputs(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_a]:
            self.image = image_left
            self.direction.x = -1
        elif keys[pygame.K_d]:
            self.image = image_right
            self.direction.x = 1
        else:
            self.direction.x = 0
            

    def update(self):
        self.inputs()
        self.old_pos = (self.rect.x, self.rect.y)

        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        
        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed

        return super().update()