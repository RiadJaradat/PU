import pygame

class entity(pygame.sprite.Sprite):
    def __init__(self, *groups, image: pygame.image, pos: tuple = (0, 0)):
        super().__init__(*groups)
        self.screen = pygame.display.get_surface()
        self.image: pygame.image = image
        self.rect = self.image.get_rect(topleft=pos)

    def draw(self):
        self.update()
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        pass