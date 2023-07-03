import pygame
import sys
import random
import cv2
from Camera import Camera
from MediapipeRecognition import Recognition

from Player import Player
from Obstacle import Obstacle
from Utils import load_images, select_obstacle_image, get_obstacle_random_position, collision_check, show_message
from Config import *

# Inicializar Pygame
pygame.init()

# Configurar la ventana del juego
screen = pygame.display.set_mode((WIDTH, HEIGHT))
road = pygame.image.load(ROAD_IMAGE_PATH)

# color variable
# Its a rgb value of white color
white = (255, 255, 255)
# first make variables of position of road
roadx = 0
roady = 0

#############Camara#############
Camera1 = Camera()
Camera1.cameraSetting()
#############Camara#############

# # configuraciones adicionales
# # link de referencia: https://docs.opencv.org/3.4/d8/dfe/classcv_1_1VideoCapture.html#a8c6d8c2d37505b5ca61ffd4bb54e9a7c

# Configurar el personaje
player_size = (WIDTH // 8, HEIGHT // 5)
player_pos = [WIDTH // 2, HEIGHT - player_size[1] - 20]

# Configurar los obstáculos
OBSTACLE_SIZE = 80
obstacle_pos = [random.randint(FRONTIER, WIDTH - OBSTACLE_SIZE - FRONTIER), 0]
OBSTACLE_SPEED = 1.5 * VELOCITY

# Configurar las vidas y el puntaje
lives = 3
score = 0

# Cargar las imágenes
player_img, collision_img, obstacle_images = load_images(player_size)

current_select_obstacle_image = select_obstacle_image(obstacle_images)

# Configurar la fuente para el puntaje
font = pygame.font.Font(None, 36)

# Crear instancia de la clase Player
player = Player(player_pos, player_img, collision_img)

# Crear instancia de la clase Obstacle
obstacle = Obstacle(obstacle_pos, OBSTACLE_SIZE, OBSTACLE_SPEED, current_select_obstacle_image)

check = True

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Ahora agregamos VELOCITY a la posición de la carretera
    roady += VELOCITY
    # Esto agrega el valor VELOCITY a la posición y de la carretera, lo que hace que parezca que se está moviendo

    # Ahora creamos una condición if
    if roady == STEP_BLIP:
        roady = 0
    # Esto establece la posición de roady nuevamente en su posición original
    # Ahora tenemos que dibujar la carretera en la pantalla
    # Tenemos dos argumentos, el nombre de la imagen y la posición de la imagen en x e y
    # Vamos a dibujar otra carretera
    # Pero no en la posición de la carretera inicial, sino detrás de la imagen de la carretera inicial, es decir, roady - STEP_BLIP
    screen.blit(road, (roadx, roady - STEP_BLIP))
    screen.blit(road, (roadx, roady))

    # Mover el obstáculo hacia el personaje
    obstacle.move()
    if obstacle.pos[1] > HEIGHT:
        obstacle.pos = get_obstacle_random_position(FRONTIER, WIDTH - FRONTIER - OBSTACLE_SIZE)
        obstacle.image = select_obstacle_image(obstacle_images)
        score += 1  # Incrementar el puntaje cuando el personaje esquiva un obstáculo

    collided = collision_check(player.get_rect(), obstacle.get_rect())
    if collided:
        lives -= 1
        player.draw(screen, collided)
        if lives == 0:
            show_message(screen, font, "You Lose!")
            pygame.quit()
            sys.exit()
        else:
            obstacle.pos = get_obstacle_random_position(FRONTIER, WIDTH - FRONTIER - OBSTACLE_SIZE)

    # Verificar si el jugador ha ganado
    # Asume que TARGET_SCORE es el puntaje que el jugador necesita para ganar
    if score == TARGET_SCORE:
        show_message(screen, font, "You Win!")
        pygame.quit()
        exit(0)


    player.draw(screen, collided)
    obstacle.draw(screen)

    # Dibujar el puntaje
    score_text = font.render("Puntajes: " + str(score), 1, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Dibujar las vidas
    lives_text = font.render("Vidas: " + str(lives), 1, (255, 255, 255))
    screen.blit(lives_text, (10, 50))

    #####Camara#####
    img = Camera1.readCamera()
    #####Camara#####

    #############MediaPipe##################

    Recognition1 = Recognition(player, img)
    print("Recognition object: ", Recognition1)

    l = Recognition1.secondSet()
    print("l: ", l)

    if l != None and l != 0 and check == True:
        inicio = l
        check = False
    if l != None and l != 0 and check == False:
        print("final e inicio: ", l - inicio)
        if l - inicio > 15:
            exit(0)
    #############Mediapipe##################

    cv2.imshow('Detector', img)
    cv2.waitKey(10)

    pygame.display.update()
