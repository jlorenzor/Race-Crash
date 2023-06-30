import mediapipe as mp
import cv2
import math
import time
from Config import *
from Player import Player

class MediaPipeRecognition:
    def ___init__(self,estado,inicio,estado_actual):
        mpFaceMesh = mp.solutions.face_mesh
        self.faceMesh = mpFaceMesh.FaceMesh() # Obtengo puntos en cada frame
        self.mpDraw = mp.solutions.drawing_utils # Dibujar los puntos
        self.estado = estado
        self.inicio = inicio
        self.estado_actual = estado_actual
    # def ___init__(self):
    #     mpFaceMesh = mp.solutions.face_mesh
    #     self.faceMesh = mpFaceMesh.FaceMesh() # Obtengo puntos en cada frame
    #     self.mpDraw = mp.solutions.drawing_utils # Dibujar los puntos
    def getEstado(self):
        return self.estado
    def getInicio(self):
        return self.inicio
    def getEstadoActual(self):
        return self.estado_actual
    def getFaceMesh(self):
        return self.faceMesh

    def getDraw(self):
        return self.mpDraw

    def noseAun(self,img,h,w,player):
        estado = self.getEstado()
        estado_actual = self.getEstadoActual()
        inicio = self.getInicio()
        results = self.getFaceMesh().process(img)
        if results:
            if not results.multi_face_landmarks:
                return
            for face in results.multi_face_landmarks:
                # print(face)
                self.getDraw().draw_landmarks(img, face, self.getFaceMesh().FACEMESH_FACE_OVAL)
                d1x, d1y = int((face.landmark[159].x) * w), int((face.landmark[159].y) * h)
                d2x, d2y = int((face.landmark[145].x) * w), int((face.landmark[145].y) * h)
                i1x, i1y = int((face.landmark[386].x) * w), int((face.landmark[386].y) * h)
                i2x, i2y = int((face.landmark[374].x) * w), int((face.landmark[374].y) * h)

                distD = math.hypot(d1x - d2x, d1y - d2y)
                distI = math.hypot(i1x - i2x, i1y - i2y)

                # print(f'distD: {distD}, distI: {distI}')
                if distI <= 15 and distD <= 15:  # Default 15
                    print('ojos cerrados')

                    player.move_left(STEP_BLIP / 25)

                    cv2.rectangle(img, (100, 30), (390, 80), (0, 0, 255), -1)
                    cv2.putText(img, 'OJOS CERRADOS', (105, 65), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)
                    estado = 'Dormido'
                    if estado != estado_actual:
                        inicio = time.time()
                else:
                    print('ojos abiertos')

                    player.move_right(STEP_BLIP / 25)
                    cv2.rectangle(img, (100, 30), (390, 80), (255, 0, 0), -1)
                    cv2.putText(img, 'OJOS ABIERTOS', (105, 65), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)
                    estado = 'Despierto'
                    inicio = time.time()
                    tiempo = int(time.time() - inicio)

                if estado == 'Dormido':
                    tiempo = int(time.time() - inicio)

                if tiempo >= 2:
                    cv2.rectangle(img, (300, 150), (850, 220), (0, 0, 255), -1)
                    cv2.putText(img, f'DORMIDO: {tiempo} SEG', (310, 200), cv2.FONT_HERSHEY_SIMPLEX, 1.7, (255, 255, 255),
                                5)
                estado_actual = estado
        return img