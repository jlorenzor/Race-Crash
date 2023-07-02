import cv2


class Camera:
    # cam = cv2.VideoCapture('/dev/video0')

    def __init__(self):
        self.cam = cv2.VideoCapture('/dev/video0')
        self.cameraSetting()

    def cameraSetting(self):
        # configuraciones adicionales
        # link de referencia: https://docs.opencv.org/3.4/d8/dfe/classcv_1_1VideoCapture.html#a8c6d8c2d37505b5ca61ffd4bb54e9a7c
        self.cam.set(3, 30)  # largo
        self.cam.set(2, 20)  # alto
        self.cam.set(10, 150)  # 500) # brillo / luminosidad

    def readCamera(self):
        check, img = self.cam.read()
        img = cv2.resize(img, (1000, 720))

        return img