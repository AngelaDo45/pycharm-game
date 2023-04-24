# project: picture charades game
# creator: Angela Do Angela.Do45@gmail.com
# source code 1: https://www.techwithtim.net/tutorials/python-online-game-tutorial/client/
# source code 2: https://www.thepythoncode.com/article/make-a-drawing-program-with-python
# last update" 4/23/2023

import pygame

width = 1000
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

cyan = 0, 255, 255

# Initial color
drawColor = [0, 0, 0]

# Initial brush size
brushSize = 30
brushSizeSteps = 3

# Drawing Area Size
canvasSize = [800, 800]
# Canvas
canvas = pygame.Surface(canvasSize)
canvas.fill((255, 255, 0))

clientNumber = 0


class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.vel = 3

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.rect = (self.x, self.y, self.width, self.height)


def redrawWindow(win, player):
    win.fill((255, 255, 255))
    player.draw(win)
    pygame.display.update()


def main():
    run = True
    p = Player(50, 50, 100, 100, (0, 255, 0))
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move()
        redrawWindow(win, p)
        # Drawing with the mouse
        if pygame.mouse.get_pressed()[0]:
            p.color = (0, 255, 255)

        if event.type == pygame.MOUSEBUTTONDOWN:
            # mouse position
            click = pygame.mouse.get_pos()
            click_x = click[0]
            click_y = click[1]
            # if click height is within range
            # if click width is within range

            if p.rect[0] <= click_x <= (p.rect[0] + p.rect[2]) and p.rect[1] <= click_y <= (p.rect[1] + p.rect[3]):
                p.color = (255, 255, 0)
            else:
                print(click)
                print(p.rect)


main()
