from abc import ABC, abstractmethod


class Instrument(ABC):
    @abstractmethod
    def play(self):
        pass


def play_instrument(i: Instrument):
    return i.play()