import pygame
import json

import Classes.player as Player
import Classes.CameraGroup as CameraGroup

pygame.init()

screen = pygame.display.set_mode((1500, 1000))
clock = pygame.time.Clock()

isRunning = True

def load_settings():
    with open("Assets/Settings.json", "r") as f:
        settings = json.load(f)
    return settings

def main():
    settings = load_settings()

    pygame.display.set_caption(settings["TITLE"])

    camera = CameraGroup.Camera()
    player_instance = Player.player(image=Player.image_left, pos=(0,0))

    camera.add(player_instance)

    NPC1 = pygame.sprite.Sprite()
    NPC1.image = pygame.image.load("Assets/Player/npc1.png").convert_alpha()
    NPC1.image = pygame.transform.scale(pygame.image.load("Assets/Player/npc1.png").convert_alpha(), (NPC1.image.get_width() * 6, NPC1.image.get_height() * 6))
    NPC1.rect = NPC1.image.get_rect(topleft=(0, 0))
    camera.add(NPC1)

    isRunning = True
    while isRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False

        screen.fill((0, 0, 0))

        player_instance.update()
        camera.draw(player_instance)
        

        pygame.display.update()
        clock.tick(settings["FPS"])

    pygame.quit()

if __name__ == "__main__":
    main()