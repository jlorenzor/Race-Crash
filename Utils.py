import pygame
import random
from Config import *

def load_images(player_size):
    player_img = pygame.image.load(PLAYER_IMAGE_PATH)
    player_img = pygame.transform.scale(player_img, player_size)

    collision_img = pygame.image.load(COLLISION_IMAGE_PATH)
    collision_img = pygame.transform.scale(collision_img, player_size)

    obstacle_images = []
    for i in range(1, 7):
        obstacle_img = pygame.image.load(f'{OBSTACLE_IMAGE_PREFIX}{i}.png')
        obstacle_img = pygame.transform.scale(obstacle_img, player_size)
        obstacle_img = pygame.transform.rotate(obstacle_img, -180)
        obstacle_images.append(obstacle_img)

    return player_img, collision_img, obstacle_images

def select_obstacle_image(obstacle_images):
    return random.choice(obstacle_images)

def get_obstacle_random_position(frontier, max_pos):
    return [random.randint(frontier, max_pos), 0]

def collision_check(player_rect, obstacle_rect):
    return player_rect.colliderect(obstacle_rect)

def show_message(screen, font, message):
    text = font.render(message, 1, (255, 255, 255))
    screen.blit(text, (screen.get_width() / 2 - text.get_width() / 2, screen.get_height() / 2 - text.get_height() / 2))
    pygame.display.update()
    pygame.time.wait(2000)
