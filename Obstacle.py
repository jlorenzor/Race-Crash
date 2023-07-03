import pygame
import random
from Config import *


class Obstacle:
    def __init__(self, image=None):
        self.pos = [random.randint(FRONTIER, WIDTH - OBSTACLE_SIZE - FRONTIER), 0]
        self.size = OBSTACLE_SIZE
        self.speed = OBSTACLE_SPEED
        self.image = image
        self.moves = []

    def move(self):
        if len(self.moves) > 0:
            pos_x = self.moves.pop(0)
        else:
            pos_x = self.get_pos_x()
        pos_y = self.get_pos_y()
        self.set_pos([pos_x, pos_y + self.speed])

    def draw(self, screen):
        screen.blit(self.image, self.pos)

    def get_rect(self):
        pos_x = self.get_pos_x()
        pos_y = self.get_pos_y()
        return pygame.Rect(pos_x, pos_y, self.size, self.size)

    def get_pos_x(self):
        return self.pos[0]

    def get_pos_y(self):
        return self.pos[1]

    def get_pos(self):
        return self.pos

    def set_pos(self, pos):
        self.pos = pos

    def get_image(self):
        return self.image

    def set_image(self, image):
        self.image = image

    def has_collided(self, another_object):
        return self.get_rect().colliderect(another_object.get_rect())

    def save_moves(self, moves):
        self.moves = moves

    def get_moves(self):
        return self.moves

    def generate_random_position(self):
        print(f"Anterior obstáculo estuvo en {self.pos}")
        if len(self.moves) > 0:
            print(f"Los movimientos son {self.moves}")
            max_pos_x = self.moves.pop(0)
        else:
            max_pos_x = random.randint(FRONTIER, WIDTH - FRONTIER - OBSTACLE_SIZE)
        new_pos = [max_pos_x, 0]
        print(f"Nuevo obstáculo en {new_pos}")
        self.pos = new_pos
