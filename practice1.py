import pygame

pygame.init()

screen = pygame.display.set_mode((640, 640))

img = pygame.image.load('.png')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()