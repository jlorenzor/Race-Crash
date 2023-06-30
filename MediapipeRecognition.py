import mediapipe as mp
import cv2
import math
import time
from Player import Player
from Config import *

class Recognition:

    def __init__(self, player, img):
        self.img = img
        self.player = player
        self.mpFaceMesh = mp.solutions.face_mesh
        self.faceMesh = self.mpFaceMesh.FaceMesh()
        self.mpDraw = mp.solutions.drawing_utils
        self.estado = 'X'
        self.inicio = 0
        self.estado_actual = ''

    def secondSet(self):
        results = self.faceMesh.process(self.img)
        h, w, _ = self.img.shape

        if results:
            if not results.multi_face_landmarks:
                 return 0
            for face in results.multi_face_landmarks:
                #print(face)
                self.mpDraw.draw_landmarks(self.img, face, self.mpFaceMesh.FACEMESH_FACE_OVAL)
                d1x, d1y = int((face.landmark[159].x)*w), int((face.landmark[159].y)*h)
                d2x, d2y = int((face.landmark[145].x) * w), int((face.landmark[145].y) * h)
                i1x, i1y = int((face.landmark[386].x) * w), int((face.landmark[386].y) * h)
                i2x, i2y = int((face.landmark[374].x) * w), int((face.landmark[374].y) * h)

                distD = math.hypot(d1x - d2x, d1y - d2y)
                distI = math.hypot(i1x - i2x, i1y - i2y)


                # print(f'distD: {distD}, distI: {distI}')
                if distI <= 15 and distD <= 15: #Default 15
                    print('ojos cerrados')

                    self.player.move_left(STEP_BLIP / 25)
                    
                    cv2.rectangle(self.img, (100, 30), (390, 80), (0,0,255), -1)
                    cv2.putText(self.img, 'OJOS CERRADOS', (105,65), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255, 255), 3)
                    self.estado = 'Dormido'
                    if self.estado != self.estado_actual:
                        self.inicio = time.time()
                else:
                    print('ojos abiertos')

                    self.player.move_right(STEP_BLIP / 25)
                    cv2.rectangle(self.img, (100, 30), (390, 80), (255, 0, 0), -1)
                    cv2.putText(self.img, 'OJOS ABIERTOS', (105, 65), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)
                    self.estado = 'Despierto'
                    self.inicio = time.time()
                    tiempo = int(time.time() - self.inicio)

                if self.estado == 'Dormido':
                    tiempo = int(time.time() - self.inicio)

                if tiempo >= 2:
                    cv2.rectangle(self.img, (300, 150), (850, 220), (0,0,255), -1)
                    cv2.putText(self.img, f'DORMIDO: {tiempo} SEG', (310, 200), cv2.FONT_HERSHEY_SIMPLEX, 1.7, (255, 255, 255), 5)
                self.estado_actual = self.estado