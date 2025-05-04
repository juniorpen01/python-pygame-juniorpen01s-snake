from typing import Callable, Generic, Protocol, TypeVar

import pygame
from pygame import Surface, event
from pygame.typing import IntPoint


class Data(Protocol):
    title: str
    dimensions_screen: IntPoint


T = TypeVar("T", bound=Data)


class Game(Generic[T]):
    def __init__(self, data: T) -> None:
        self._data = data
        self.running = True
        pygame.init()
        pygame.display.set_caption(data.title)
        self.screen = pygame.display.set_mode(data.dimensions_screen)

    def on_initialize(self, callback: Callable[[Surface, T], None]):
        self._callback_initialize = callback
        return self

    def on_update(self, callback: Callable[[Surface, T], None]):
        self._callback_update = callback
        return self

    def run(self):
        self._callback_initialize(self.screen, self._data)
        while self.running:
            for ev in event.get():
                if ev.type == pygame.QUIT:
                    self.running = False
            self._callback_update(self.screen, self._data)
            pygame.display.update()
        pygame.quit()
