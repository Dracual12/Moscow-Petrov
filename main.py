import pygame, os, sys


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


if __name__ == '__main__':
    image = load_image("gameover.png")
    pygame.init()
    pygame.display.set_caption('Game over')
    size = width, height = 600, 300
    screen = pygame.display.set_mode(size)
    running = True
    pos = [-600, 0]
    v = 100
    clock = pygame.time.Clock()
    while running:
        screen.fill(pygame.Color('blue'))
        screen.blit(image, pos)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if pos[0] < 0:
            pos[0] += v * clock.tick() / 1000
        else:
            v = 0
        pygame.display.flip()
    pygame.quit()
