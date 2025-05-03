import sys

import pygame
from pygame import Vector2, display, event, image, transform

from core.direction import Direction
from core.snake import Snake


def main() -> None:
    print("Hello from juniorpen01s-snake!")

    snake = Snake(Vector2(3, 17), 6, Direction.DOWN)
    snake.grow()

    print(snake.body)

    pygame.init()
    pygame.display.set_caption("juniorpen01's Snake")
    screen = display.set_mode((800, 800))

    cat_image = image.load("assets/cat.jpg")
    cat_image_scaled = transform.scale(cat_image, (800, 800))

    is_running = True
    while is_running:
        for ev in event.get():
            match ev.type:
                case pygame.QUIT:
                    is_running = False
                case _:
                    pass

        screen.blit(cat_image_scaled, (0, 0))

        pygame.display.update()

    pygame.quit()
    sys.exit()
