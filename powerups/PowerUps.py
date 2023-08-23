from typing import Literal, Callable

class PowerUp:

    def __init__(self, name:str, duration:float, target:Literal["self", "enemy"], cooldown:float, effect:Callable) -> None:
        self.name = name
        self.duration = duration
        self.target = target
        self.coolddown = cooldown
        self.effect = effect

    def apply_effect(self):

        self.effect()
