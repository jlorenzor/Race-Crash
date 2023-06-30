import cv2

# configuraciones adicionales
# link de referencia: https://docs.opencv.org/3.4/d8/dfe/classcv_1_1VideoCapture.html#a8c6d8c2d37505b5ca61ffd4bb54e9a7c
# cam.set(3, 30)  # largo
# cam.set(2, 20)  # alto
# cam.set(10, 150)  # 500) # brillo / luminosidad

class Camera:
    def __init__(self,width,height,luminosity):
        self.camera = cv2.VideoCapture(0)
        self.width = width
        self.height = height
        self.luminosity = luminosity

    def setCamera(self):
        self.camera.set(3,self.width)
        self.camera.set(3,self.height)
        self.camera.set(10,self.luminosity)

    def getFrame(self):
        check, img = self.camera.read()
        img = cv2.resize(img, (1000, 720))
        # cv2.imshow('Webcam', img)
        if cv2.waitKey(1) & 0xFF == ord('Q'):  # Se necesita poner este if para que la ventana de la camara salga.
            exit()
        return img