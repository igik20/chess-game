import pygame
from square import Square

class PARAMS():
    screen_size = 1000
    square_size = screen_size // 8

#initialization
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode( (PARAMS.screen_size, PARAMS.screen_size) )

screen.fill( (255, 255, 255) )

running = True

grid = []
for y in range(0, PARAMS.screen_size, PARAMS.square_size):
    for x in range(0, PARAMS.screen_size, PARAMS.square_size):
        file = chr(x // PARAMS.square_size + 97)
        row = chr(- y // PARAMS.square_size + 56)
        grid.append(Square(x, y, file, row))

font = pygame.font.SysFont(None, 24)

for s in grid:
    pygame.draw.rect(screen, s.color, pygame.Rect(s.x, s.y, PARAMS.square_size, PARAMS.square_size))
    img = font.render(s.coord(), True, (0,0,0))
    screen.blit(img, (s.x, s.y))

pygame.display.flip()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(30)

pygame.quit()

