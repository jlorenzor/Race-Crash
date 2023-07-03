import mediapipe as mp
import cv2
import math
import time
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
        self.final = 0

    def secondSet(self):
        results = self.faceMesh.process(self.img)
        h, w, _ = self.img.shape

        if results:
            if not results.multi_face_landmarks:
                return 0
            for face in results.multi_face_landmarks:
                self.mpDraw.draw_landmarks(self.img, face, self.mpFaceMesh.FACEMESH_FACE_OVAL)
                d1x, d1y = int((face.landmark[159].x) * w), int((face.landmark[159].y) * h)
                d2x, d2y = int((face.landmark[145].x) * w), int((face.landmark[145].y) * h)
                i1x, i1y = int((face.landmark[386].x) * w), int((face.landmark[386].y) * h)
                i2x, i2y = int((face.landmark[374].x) * w), int((face.landmark[374].y) * h)

                boca_top_x, boca_top_y = int((face.landmark[13].x) * w), int((face.landmark[13].y) * h)
                boca_bottom_x, boca_bottom_y = int((face.landmark[14].x) * w), int((face.landmark[14].y) * h)

                distD_boca = math.hypot(boca_top_x - boca_bottom_x, boca_top_y - boca_bottom_y)

                distD = math.hypot(d1x - d2x, d1y - d2y)
                distI = math.hypot(i1x - i2x, i1y - i2y)

                if distD_boca > 10:
                    print('mover derecha')

                    self.player.move_left(STEP_BLIP / 25)

                    cv2.rectangle(self.img, (100, 30), (370, 80), (0, 0, 255), -1)
                    cv2.putText(self.img, 'A LA DERECHA', (105, 65), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)

                else:
                    print('mover izquierda')

                    self.player.move_right(STEP_BLIP / 25)
                    cv2.rectangle(self.img, (100, 30), (370, 80), (255, 0, 0), -1)
                    cv2.putText(self.img, 'A LA IZQUIERDA', (105, 65), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)

                if distI <= 16 and distD <= 16:
                    print('ojos cerrados')

                    self.final = time.time()
                    print(self.final)

                    return self.final
