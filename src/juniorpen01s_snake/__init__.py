from typing import Protocol

from pygame import Surface, image, transform
from pygame.typing import IntPoint

from core.direction import Direction
from core.game import Game
from core.snake import Snake


class SnakeData(Protocol):
    position_initial: IntPoint
    length_initial: int
    direction_initial: Direction


class Data:
    title: str = "juniorpen01's Snake"
    dimensions_screen: IntPoint = 800, 800
    snake = Snake((3, 17), 6, Direction.DOWN)
    cat_image = image.load("assets/cat.jpg")
    cat_image_scaled = transform.scale(cat_image, (800, 800))


def main() -> None:
    print("Hello from juniorpen01s-snake!")

    def on_initialize(screen: Surface, data: Data):
        data.snake.grow()

        print(data.snake.body)

    def on_update(screen: Surface, data: Data):
        screen.blit(data.cat_image_scaled, (0, 0))

    Game(Data()).on_initialize(on_initialize).on_update(on_update).run()
