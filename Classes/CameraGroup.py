import pygame

class Camera(pygame.sprite.Group):
    def __init__(self, *sprites):
        super().__init__(*sprites)
        self.screen = pygame.display.get_surface()
        self.ground_surface = pygame.Surface((1000, 1000)).convert_alpha()
        self.ground_surface.fill((0, 0, 0, 0))
        self.ground_rect = self.ground_surface.get_rect()
        self.offset = pygame.math.Vector2()
        self.half_w = self.screen.get_width() // 2
        self.half_h = self.screen.get_height() // 2

    def draw(self, player):

        self.offset.x = player.rect.centerx - self.half_w
        self.offset.y = player.rect.centery - self.half_h

        ground_offset = self.ground_rect.topleft -  self.offset
        self.screen.blit(self.ground_surface, ground_offset)

        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.screen.blit(sprite.image, offset_pos)
