import pygame
import sys
import random
import cv2

import mediapipe as mp
import math
import time

from Player import Player
from Obstacle import Obstacle
from Utils import load_images, select_obstacle_image, get_obstacle_random_position, collision_check, show_message
from Config import *
from Camera import *
from MediaPipeRecognition import *

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

# cam = cv2.VideoCapture('/dev/video0')
# cam = cv2.VideoCapture(0)
#
# # configuraciones adicionales
# # link de referencia: https://docs.opencv.org/3.4/d8/dfe/classcv_1_1VideoCapture.html#a8c6d8c2d37505b5ca61ffd4bb54e9a7c
# cam.set(3, 30)  # largo
# cam.set(2, 20)  # alto
# cam.set(10, 150)  # 500) # brillo / luminosidad
newCamera = Camera(30,20,150)
newCamera.setCamera()

######################Semana14#########################
# mpFaceMesh = mp.solutions.face_mesh
# faceMesh = mpFaceMesh.FaceMesh()
# mpDraw = mp.solutions.drawing_utils
# estado = 'X'
# inicio = 0
# estado_actual = ''
mpRecog = MediaPipeRecognition('X',0,'')
# faceMesh = mpRecog.getFaceMesh()
# mpDraw = mpRecog.getDraw()

######################Semana14#########################


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

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_LEFT]:
    #     player.move_left(STEP_BLIP / 25)
    # if keys[pygame.K_RIGHT]:
    #     player.move_right(STEP_BLIP / 25)

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
        sys.exit()

    player.draw(screen, collided)
    obstacle.draw(screen)

    # Dibujar el puntaje
    score_text = font.render("Puntajes: " + str(score), 1, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Dibujar las vidas
    lives_text = font.render("Vidas: " + str(lives), 1, (255, 255, 255))
    screen.blit(lives_text, (10, 50))

    # check, img = cam.read()
    # img = cv2.resize(img, (1000, 720))
    # # cv2.imshow('Webcam', img)
    # if cv2.waitKey(1) & 0xFF == ord('Q'):  # Se necesita poner este if para que la ventana de la camara salga.
    #     break
    img = newCamera.getFrame()

    #############Semana14##################
    h, w, _ = img.shape

    # results = faceMesh.process(img)
    #
    # if results:
    #     if not results.multi_face_landmarks:
    #         continue
    #     for face in results.multi_face_landmarks:
    #         # print(face)
    #         mpDraw.draw_landmarks(img, face, mpFaceMesh.FACEMESH_FACE_OVAL)
    #         d1x, d1y = int((face.landmark[159].x) * w), int((face.landmark[159].y) * h)
    #         d2x, d2y = int((face.landmark[145].x) * w), int((face.landmark[145].y) * h)
    #         i1x, i1y = int((face.landmark[386].x) * w), int((face.landmark[386].y) * h)
    #         i2x, i2y = int((face.landmark[374].x) * w), int((face.landmark[374].y) * h)
    #
    #         distD = math.hypot(d1x - d2x, d1y - d2y)
    #         distI = math.hypot(i1x - i2x, i1y - i2y)
    #
    #         # print(f'distD: {distD}, distI: {distI}')
    #         if distI <= 15 and distD <= 15:  # Default 15
    #             print('ojos cerrados')
    #
    #             player.move_left(STEP_BLIP / 25)
    #
    #             cv2.rectangle(img, (100, 30), (390, 80), (0, 0, 255), -1)
    #             cv2.putText(img, 'OJOS CERRADOS', (105, 65), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)
    #             estado = 'Dormido'
    #             if estado != estado_actual:
    #                 inicio = time.time()
    #         else:
    #             print('ojos abiertos')
    #
    #             player.move_right(STEP_BLIP / 25)
    #             cv2.rectangle(img, (100, 30), (390, 80), (255, 0, 0), -1)
    #             cv2.putText(img, 'OJOS ABIERTOS', (105, 65), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)
    #             estado = 'Despierto'
    #             inicio = time.time()
    #             tiempo = int(time.time() - inicio)
    #
    #         if estado == 'Dormido':
    #             tiempo = int(time.time() - inicio)
    #
    #         if tiempo >= 2:
    #             cv2.rectangle(img, (300, 150), (850, 220), (0, 0, 255), -1)
    #             cv2.putText(img, f'DORMIDO: {tiempo} SEG', (310, 200), cv2.FONT_HERSHEY_SIMPLEX, 1.7, (255, 255, 255),
    #                         5)
    #         estado_actual = estado
    imagen = mpRecog.noseAun(img,h,w,player)
    cv2.imshow('Detector', imagen)
    cv2.waitKey(10)
    #############Semana14##################
    pygame.display.update()