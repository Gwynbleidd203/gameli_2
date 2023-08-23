import pygame
from scripts.scene import Scene
from scripts.menu import Menu
from scripts.gameover import GameOver
from scripts.game import Game
from scripts.settings import SETTINGS

class StartGame:

    def __init__(self):

        pygame.init()
        pygame.mixer.init()
        pygame.font.init()

        self.display = pygame.display.set_mode([SETTINGS["width"], SETTINGS["height"]])

        self.current_scene = Scene()
        self.scene = "menu"
        self.current_scene = Menu()

    
    def run(self):

        while True:

            if self.scene == "menu" and self.current_scene.active == False:

                self.scene = "game"
                self.current_scene = Game()

            elif self.scene == "game" and self.current_scene.active == False:

                self.scene = "gameover"
                self.current_scene = GameOver()

            elif self.scene == "gameover" and self.current_scene.active == False:

                self.scene = "menu"
                self.current_scene = Menu()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    pygame.quit()

                self.current_scene.events(event)

            self.display.fill("#000000")
            self.current_scene.draw()
            self.current_scene.update()
            pygame.display.flip()