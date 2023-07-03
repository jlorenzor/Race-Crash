import pygame
from Config import *


class Player:
    def __init__(self, pos, player_img, collision_img):
        self.pos = pos
        self.player_img = player_img
        self.collision_img = collision_img
        self.last_moves = []
        self.max_last_moves = PLAYER_MAX_MOVES

    def move_left(self, step):
        self.pos[0] -= step
        self.save_last_move(self.pos[0])

    def move_right(self, step):
        self.pos[0] += step
        self.save_last_move(self.pos[0])

    def draw(self, screen, collided):
        if collided:
            screen.blit(self.collision_img, self.pos)
        else:
            screen.blit(self.player_img, self.pos)

    def get_rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.player_img.get_width(), self.player_img.get_height())

    def has_collided(self, another_object):
        return self.get_rect().colliderect(another_object.get_rect())

    def save_last_move(self, move):
        # print(f"save_last_move: {move} - {self.last_moves}")
        if len(self.last_moves) < self.max_last_moves:
            self.last_moves.append(move)
        else:
            self.last_moves.pop(0)
            self.last_moves.append(move)

    def get_last_moves(self):
        print(f"get_last_moves: {self.last_moves}")
        if len(self.last_moves) >= self.max_last_moves:
            send_last_moves = self.last_moves[-self.max_last_moves:]
            self.last_moves = []
            return send_last_moves
        else:
            send_last_moves = self.last_moves[-self.max_last_moves:] + [WIDTH/2] * (self.max_last_moves - len(self.last_moves))
            self.last_moves = []
            return send_last_moves
