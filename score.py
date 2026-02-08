import sys
import pygame
from logger import log_event
from asteroid import Asteroid


class stats:
    def __init__(self, health, score):
        self.health = health
        self.score = score

    def add_score(self, other):
        while self.health > 0:
            points = other.radius * 100
            self.score += points
            log_event("score_increased")

    def lose_health(self):
        self.health -= 1
        log_event("health_lost")
