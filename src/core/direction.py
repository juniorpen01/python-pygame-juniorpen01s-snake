from enum import Enum

from pygame import Vector2


class Direction(Enum):
    LEFT = 1
    DOWN = 2
    UP = 3
    RIGHT = 4

    def __neg__(self):
        match self:
            case Direction.LEFT:
                return Direction.RIGHT
            case Direction.DOWN:
                return Direction.UP
            case Direction.UP:
                return Direction.DOWN
            case Direction.RIGHT:
                return Direction.LEFT

    def into_vector2(self) -> Vector2:
        match self:
            case Direction.LEFT:
                return Vector2(-1, 0)
            case Direction.DOWN:
                return Vector2(0, 1)
            case Direction.UP:
                return Vector2(0, -1)
            case Direction.RIGHT:
                return Vector2(1, 0)
