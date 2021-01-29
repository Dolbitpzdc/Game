import pygame
import sys
import random
import os
# from options import *
import time
# from functions import *
# from questions import *
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


# user
x = 50
y = 376
width = 128
height = 128
player1_img = [pygame.image.load(resource_path(os.path.join('pigs', 'personage_1_right.png'))),
              pygame.image.load(resource_path(os.path.join('pigs', 'personage_1.2_right.png'))), pygame.image.load(resource_path(os.path.join('pigs', 'personage_1.3_right.png'))),
              pygame.image.load(resource_path(os.path.join('pigs', 'personage_1.2_right.png'))), pygame.image.load(resource_path(os.path.join('pigs', 'personage_1_right.png'))),
              pygame.image.load(resource_path(os.path.join('pigs', 'personage_1_right.png'))), pygame.image.load(resource_path(os.path.join('pigs', 'personage_1.2_right.png'))),
              pygame.image.load(resource_path(os.path.join('pigs', 'personage_1.3_right.png'))), pygame.image.load(resource_path(os.path.join('pigs', 'personage_1.2_right.png'))),
              pygame.image.load(resource_path(os.path.join('pigs', 'personage_1_right.png')))]

# Jump
isJump = False
jumpCount = 11

left = False
right = False
animCount = 0
lastMove = "right"
# sound_jump = pygame.mixer.Sound('./sound/jump.mp3')

# Barriers
# pc_width = 20
pc_height = 70
pc_x = display_width - 50
pc_y = display_height - pc_height - 100
pc_img = [pygame.image.load(resource_path('./pigs/pc.png')), pygame.image.load(resource_path('./pigs/tf.png'))]
pc_options = [32, 449, 20, 469]

scores = 0
max_scores = 0
max_above = 0


button_sound = pygame.mixer.Sound(resource_path(os.path.join('sound', 'button.wav')))

display = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption("My game")
pygame.display.set_caption("My game")


button_sound = pygame.mixer.Sound(resource_path(os.path.join('sound', 'button.wav')))

sound_game = pygame.mixer.Sound(resource_path(os.path.join('sound', 'game_sound2.wav')))
death_sound = pygame.mixer.Sound(resource_path(os.path.join('sound', 'death.wav')))



player_counter: int = 0

clock = pygame.time.Clock()

paused_game = False


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


class Cactus:
    def __init__(self, x, y, width, image, speed):
        self.x = x
        self.y = y
        self.width = width
        self.image = image
        self.speed = speed

    def move(self):
        if self.x >= -self.width:
            display.blit(self.image, (self.x, self.y))
            # pygame.draw.rect(display, (224, 121, 31), (self.x, self.y, self.width, self.height))
            self.x -= self.speed
            return True

        else:
            self.x = display_width + 100 + random.randrange(-80, 60)
            return False

    def return_self(self, radius, y, width, image):
        self.x = radius
        self.y = y
        self.width = width
        self.image = image
        display.blit(self.image, (self.x, self.y))


def draw_player():
    global player_counter

    if player_counter == 20:
        player_counter = 0

    display.blit(player1_img[player_counter // 10], (x, y))
    player_counter += 1


def print_text(message, x, y, font_color=(0, 0, 0), font_type='./pigs/20050.ttf', font_size=30):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    display.blit(text, (x, y))


def pause():
    global paused_game
    paused = True
    counter = 0
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        print_text('Paused! Press Enter to play agein, Esc to exit', 50, 300)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            paused = False

        if keys[pygame.K_ESCAPE]:
            if counter >= 10:
                if paused_game == True:
                    paused_game = False
                    paused = False
                    show_menu()

        pygame.display.update()
        clock.tick(15)
        counter = counter + 1


def create_cactus_arr(array):
    choice = random.randrange(0, 2)
    img = pc_img[choice]
    width = pc_options[choice * 2]
    height = pc_options[choice * 2 + 1]
    array.append(Cactus(display_width + 20, height, width, img, 13))

    choice = random.randrange(0, 2)
    img = pc_img[choice]
    width = pc_options[choice * 2]
    height = pc_options[choice * 2 + 1]
    array.append(Cactus(display_width + 300, height, width, img, 13))

    choice = random.randrange(0, 2)
    img = pc_img[choice]
    width = pc_options[choice * 2]
    height = pc_options[choice * 2 + 1]
    array.append(Cactus(display_width + 700, height, width, img, 13))


def find_radius(array):
    maximum = max(array[0].x, array[1].x)

    if maximum < display_width:
        radius = display_width
        if radius - maximum < 50:
            radius += 280
    else:
        radius = maximum

    choice = random.randrange(0, 5)
    if choice == 0:
        radius += random.randrange(50, 150)
    else:
        radius += random.randrange(250, 400)

    return radius


def draw_array(array):
    for cactus in array:
        check = cactus.move()
        if not check:
            radius = find_radius(array)

            choice = random.randrange(0, 2)
            image = pc_img[choice]
            width = pc_options[choice * 2]
            height = pc_options[choice * 2 + 1]

            cactus.return_self(radius, height, width, image)


def check_collision(barrier):
    for Cactus in barrier:
        if y + width >= Cactus.y:
            if Cactus.x - 70 <= x <= Cactus.x + Cactus.width:
                game_over()
            elif Cactus.x <= x + width <= Cactus.x + Cactus.width:
                return False


def count_scores(barriers):
    global scores, max_above
    above_pc = 0

    if -10 <= jumpCount < 7:
        for Cactus in barriers:
            if y + height - 5 <= Cactus.y:
                if Cactus.x <= x <= Cactus.x + Cactus.width:
                    above_pc += 1
                elif Cactus.x <= x + width <= Cactus.x + Cactus.width:
                    above_pc += 1

        max_above = max(max_above, above_pc)

    else:
        if jumpCount == -11:
            scores += max_above
            max_above = 0





def game_over():
    global scores, max_scores
    if scores > max_scores:
        max_scores = scores

    stopped = True
    display.blit(bg, (0, 0))
    pygame.mixer.Sound.stop(death_sound)
    pygame.mixer.Sound.stop(sound_game)
    pygame.mixer.Sound.play(death_sound)
    while stopped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        print_text('Game OVER! Press Enter to play agein, Esc to exit', 50, 300)
        print_text('Max scores: ' + str(max_scores), 300, 350)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            pygame.mixer.Sound.stop(death_sound)
            pygame.mixer.Sound.stop(sound_game)
            startgame()

        if keys[pygame.K_ESCAPE]:
            pygame.mixer.Sound.stop(death_sound)
            pygame.mixer.Sound.stop(sound_game)
            show_menu()

        pygame.display.update()
        clock.tick(15)


def waitThree():
    counter = 0
    display.blit(bg, (0, 0))
    while True:
        print_text('3', 400, 300, (255, 255, 255), font_size=50)

        if counter > 500 and counter < 1000:
            display.blit(bg, (0, 0))
            print_text('2', 400, 300, (255, 255, 255), font_size=50)

        elif counter > 1500 and counter < 2000:
            display.blit(bg, (0, 0))
            print_text('1', 400, 300, (255, 255, 255), font_size=50)

        elif counter > 2500 and counter < 3000:
            break
        counter = counter + 10

        pygame.display.update()


def question_1():
    global scores
    if scores == 5 and 6:

        print_text('СТОП! Ты не побежишь дальше, пока не ответишь на вопрос!', 20, 50,  (255, 255, 255))
        print_text('В чем чаще всего измеряется кол-во информации?', 50, 90,  (255, 255, 255))
        print_text('A. Литры', 50, 130, (255, 255, 255))
        print_text('B. Байты', 50, 170,  (255, 255, 255))
        print_text('C. Метры', 50, 210,  (255, 255, 255))

        stopped_game = True
        while stopped_game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_b]:
                waitThree()
                scores += 1
                stopped_game = False
            elif keys[pygame.K_a]:
                game_over()
            elif keys[pygame.K_c]:
                game_over()

            pygame.display.update()


def question_2():
    global scores
    if scores == 10:
        print_text("Стоп еще один вопрос!", 50, 50, (255, 255, 255))
        print_text("Сколько мегабайт в одном гигобайте?", 50, 90,  (255, 255, 255))
        print_text('A. 100', 50, 130,  (255, 255, 255))
        print_text('B.10000', 50, 170,  (255, 255, 255))
        print_text('C. 1000', 50, 210,  (255, 255, 255))

        stopped_game = True
        while stopped_game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_c]:
                waitThree()
                scores += 1
                stopped_game = False
            elif keys[pygame.K_a]:
                game_over()
            elif keys[pygame.K_b]:
                game_over()

            pygame.display.update()


def question_3():
    global scores

    if scores == 15:
        print_text("Стоп еще один вопрос!", 50, 50, (255, 255, 255))
        print_text("Посоянная память - это?", 50, 90,  (255, 255, 255))
        print_text('A. BIOS', 50, 130,  (255, 255, 255))
        print_text('B. SSD', 50, 170,  (255, 255, 255))
        print_text('C. HDD', 50, 210,  (255, 255, 255))

        stopped_game = True
        while stopped_game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                waitThree()
                scores += 1
                stopped_game = False
            elif keys[pygame.K_b]:
                game_over()
            elif keys[pygame.K_c]:
                game_over()

            pygame.display.update()



def startgame():
    global run, isJump, x, jumpCount, y, button_sound, button_sound, display, player_counter, \
        animCount, paused_game, scores, above_pc, game, max_above, sound_jump, sound_game

    game = True
    cactus_arr = []
    create_cactus_arr(cactus_arr)
    scores = 0
    speed = 13


    pygame.mixer.Sound.play(sound_game)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()

        keys = pygame.key.get_pressed()

        if not isJump:
            if keys[pygame.K_SPACE]:

                # pygame.time.delay(50)
                isJump = True

        else:
            if jumpCount >= -11:
                if jumpCount < 0:
                    y += (jumpCount ** 2) / 2
                else:
                    y -= (jumpCount ** 2) / 2
                jumpCount -= 1
            else:
                isJump = False
                jumpCount = 11

        if keys[pygame.K_ESCAPE]:
            paused_game = True
            pause()

        drawWindow()



        check_collision(cactus_arr)

        draw_array(cactus_arr)

        count_scores(cactus_arr)

        if scores % 10 == 0:
            if scores != 0:
                speed = speed + 0.05
                for cactus in cactus_arr:
                    cactus.speed = round(speed, 1)

        print_text('Scores: ' + str(scores), 600, 20, (255, 255, 255))

        if check_collision(cactus_arr):
            game = False

        question_1()
        question_2()
        question_3()

        pygame.display.update()
        clock.tick(30)

    return game_over()


def show_menu():
    menu_background = pygame.image.load('./pigs/menu.jpg')


    start_btn = Button(180, 70)
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
        start_btn.draw(290, 290, "323232", startgame, 50)
        quit_btn.draw(290, 390, "Quit", quit, 50)

        pygame.display.update()
        clock.tick(80)



def drawWindow():
    global animCount
    display.blit(bg, (0, 0))

    if animCount + 1 >= 30:
        animCount = 0

    draw_player()

    pygame.display.update()


run = True
bullets = []

show_menu()

pygame.quit()
quit()
