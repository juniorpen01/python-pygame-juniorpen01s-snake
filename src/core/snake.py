from typing import Optional

from pygame import Vector2
from pygame.typing import IntPoint

from .direction import Direction


class Snake:
    def __init__(
        self,
        position_initial: IntPoint,
        length_initial: int,
        direction_head: Direction,
    ) -> None:
        if length_initial < 1:
            raise ValueError("length_initial is zero")

        self.body: list[Vector2] = []
        self._direction: Optional[Direction] = direction_head

        self.body += [
            (position_initial - direction_head.into_vector2() * i)
            for i in range(length_initial)
        ]

        self.position_grow = self.body[-1] - direction_head.into_vector2()

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, direction: Direction):
        if self.direction != -direction:
            self._direction = direction

    def move(self):
        if self.direction:
            self.body.pop()
            self.body.insert(0, self.body[0] + self.direction.into_vector2())

    def grow(self):
        foo = self.position_grow - self.body[-1]
        self.body.append(self.position_grow.copy())
        self.position_grow += foo
