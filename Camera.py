import cv2


class Camera:

    def __init__(self):
        # self.cam = cv2.VideoCapture('/dev/video0') # Arch Linux
        self.cam = cv2.VideoCapture(0) # Windows
        self.cameraSetting()

    def cameraSetting(self):
        self.cam.set(3, 30)  # largo
        self.cam.set(2, 20)  # alto
        self.cam.set(10, 150)  # brillo / luminosidad

    def readCamera(self):
        check, img = self.cam.read()
        img = cv2.resize(img, (320, 250))#400, 320))#1000, 720

        return img