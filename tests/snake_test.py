from unittest import TestCase

from pygame import Vector2

from core.direction import Direction
from core.snake import Snake


class TestSnake(TestCase):
    def setUp(self) -> None:
        self.snake = Snake(Vector2(3, 17), 6, Direction.DOWN)

    def test_snake_init(self):
        self.assertEqual(self.snake.body, [Vector2(3, 17 - i) for i in range(6)])

    def test_snake_position_grow(self):
        self.assertEqual(self.snake.position_grow, Vector2(3, 11))

    def test_snake_move(self):
        self.snake.direction = Direction.RIGHT
        self.snake.move()
        self.assertEqual(
            self.snake.body,
            [Vector2(3, 17) + Direction.RIGHT.into_vector2()]
            + [Vector2(3, 17 - i) for i in range(5)],
        )

    def test_snake_move_into_self(self):
        self.snake.direction = Direction.UP
        self.snake.move()
        self.assertEqual(self.snake.body, [Vector2(3, 18 - i) for i in range(6)])

    def test_snake_grow(self):
        self.snake.grow()
        self.assertEqual(self.snake.body, [Vector2(3, 17 - i) for i in range(7)])

    def test_snake_grow_multiple(self):
        for _ in range(8):
            self.snake.grow()
        self.assertEqual(self.snake.body, [Vector2(3, 17 - i) for i in range(14)])
