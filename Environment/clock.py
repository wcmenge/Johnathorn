
from typing import Dict, List
from threading import Event, Thread
import pygame
from pygame.time import Clock


class GameClock():
    threads: Dict = {}
    gameClock: Clock = pygame.time.Clock()
    
    def __init__(self) -> None:
        pass

    def tickClock(self, tick: int) -> None:
        self.gameClock.tick(tick)

    def createSubProcess(self, name: str, event, handler) -> Thread:
        thread = Thread(target=handler, args=(event,), name=name)
        self.threads[name] = { "event": event, "handler": handler, "thread": thread }
        return thread

    def startSubProcess(self, name: str) -> Thread:
        self.threads[name].thread.start()
        return self.threads[name].thread.start()

    def endSubProcess(self, name: str) -> None:
        self.threads[name].thread.join()
        del self.threads[name]

    pass

