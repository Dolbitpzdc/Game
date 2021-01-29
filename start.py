import pygame
import sys
import random
import os
from pers3 import *
import time
from pers import *
from pers2 import *
# from Class import*

pygame.init()
def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)
# display
display_width = 800
display_height = 600
bg = pygame.image.load(resource_path(os.path.join('pigs','bg.png')))
display = pygame.display.set_mode((display_width, display_height))
# pygame.display.set_caption("My game")
# player_counter: int = 0
clock = pygame.time.Clock()

class Button:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.inactive_color = (13, 162, 58)
        self.active_color = (23, 204, 58)

    def draw(self, x, y, message, action=None, font_size=30):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] + self.width and y < mouse[1] < y + self.height:
            pygame.draw.rect(display, self.active_color, (x, y, self.width, self.height))

            if click[0] == 1:
                pygame.mixer.Sound.play(button_sound)
                pygame.time.delay(300)
                if action is not None:
                    action()

        else:
            pygame.draw.rect(display, self.inactive_color, (x, y, self.width, self.height))

        print_text(message, x + 10, y + 10, font_size=font_size)





def show_menu():
    menu_background = pygame.image.load('./pigs/menu.jpg')


    btn1 = Button(180, 70)
    btn2 = Button(180, 70)
    btn3 = Button(180, 70)
    quit_btn = Button(180, 70)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            sys.exit(1)



    show = True
    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit(1)

        display.blit(menu_background, (0, 0))
        btn1.draw(290, 290, "Lvl 1", startgame, 50)
        btn2.draw(290, 290, "Lvl 2", startgame1, 50)
        btn3.draw(290, 290, "Lvl 3", startgame2, 50)
        quit_btn.draw(290, 390, "Quit", quit, 50)

        pygame.display.update()
        clock.tick(80)
