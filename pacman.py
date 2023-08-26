import pygame
from board import boards

pygame.init()

width = 900
height = 950
screen = pygame.display.set_mode([width, height])
timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font('freesansbold.ttf', 20)
level = boards

def draw_board(level):
    num1 = ((height - 50) // 32)
    num2 = (width // 30)
    for i in range(len(level)):
        for j in range(len(level[i])):


run = True
while run:
    timer.tick(fps)
    screen.fill('black')
    draw_board(level)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.flip()
pygame.quit()