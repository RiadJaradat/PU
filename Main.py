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
    player_instance = Player.player(camera, image=Player.image)

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