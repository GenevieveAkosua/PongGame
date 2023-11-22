# Pong game using Pygame
# 22 November 2023

import pygame
pygame.init()

# Initial constants
WIDTH, HEIGHT = 700, 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Pong Game")

FPS = 60  # Sets a limit for how fast it can run

# Colour constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Paddle:



def draw(window):
    window.fill(BLACK)

    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        draw(WINDOW)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

    pygame.quit()


if __name__ == '__main__':
    main()
