import pygame
import random

class Obstacle:
    def __init__(self, pos, size, speed, image):
        self.pos = pos
        self.size = size
        self.speed = speed
        self.image = image

    def move(self):
        self.pos[1] += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.pos)

    def get_rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size, self.size)
