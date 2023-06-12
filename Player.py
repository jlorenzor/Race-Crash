import pygame

class Player:
    def __init__(self, pos, player_img, collision_img):
        self.pos = pos
        self.player_img = player_img
        self.collision_img = collision_img

    def move_left(self, step):
        self.pos[0] -= step

    def move_right(self, step):
        self.pos[0] += step

    def draw(self, screen, collided):
        if collided:
            screen.blit(self.collision_img, self.pos)
        else:
            screen.blit(self.player_img, self.pos)

    def get_rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.player_img.get_width(), self.player_img.get_height())
