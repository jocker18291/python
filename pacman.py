import pygame
from board import boards
from math import pi

pygame.init()

width = 900
height = 950
screen = pygame.display.set_mode([width, height])
timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font('freesansbold.ttf', 20)
level = boards
player_images = []
for i in range(1, 5):
    player_images.append(pygame.transform.scale(pygame.image.load(f'player_images/{i}.png'), (45, 45)))

def draw_board(level):
    num1 = ((height - 50) // 32)
    num2 = (width // 30)
    for i in range(len(level)):
        for j in range(len(level[i])):
            if level[i][j] == 1:
                pygame.draw.circle(screen, 'white', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 4)
            if level[i][j] == 2:
                pygame.draw.circle(screen, 'white', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 10)
            if level[i][j] == 3:
                pygame.draw.line(screen, 'blue', (j * num2 + (0.5 * num2), i * num1), (j * num2 + (0.5 * num2), (i + 1) * num1), 3)
            if level[i][j] == 4:
                pygame.draw.line(screen, 'blue', (j * num2, i * num1 + (0.5 * num1)), ((j + 1) * num2, i * num1 + (0.5 * num1)), 3)
            if level[i][j] == 5:
                pygame.draw.arc(screen, 'blue', pygame.Rect(j * num2 - (num2 * 0.5), i * num1 + (0.5 * num1), num2, num1), 0, 0.5 * pi, 3)
            if level[i][j] == 6:
                pygame.draw.arc(screen, 'blue', pygame.Rect(j * num2 + (num2 * 0.5), i * num1 + (0.5 * num1), num2, num1), 0.5 * pi, pi, 3)
            if level[i][j] == 7:
                pygame.draw.arc(screen, 'blue', pygame.Rect(j * num2 + (num2 * 0.5), i * num1 - (0.5 * num1), num2, num1), pi, 1.5 * pi, 3)
            if level[i][j] == 8:
                pygame.draw.arc(screen, 'blue', pygame.Rect(j * num2 - (num2 * 0.5), i * num1 - (0.5 * num1), num2, num1), 1.5 * pi, 0, 3)
            if level[i][j] == 9:
                pygame.draw.line(screen, 'white', (j * num2, i * num1 + (0.5 * num1)), ((j + 1) * num2, i * num1 + (0.5 * num1)), 3)

def draw_player():
    pass 

run = True
while run:
    timer.tick(fps)
    screen.fill('black')
    draw_board(level)
    draw_player()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.flip()
pygame.quit()