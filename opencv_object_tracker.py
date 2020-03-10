import cv2
from time import sleep


class FaceDetectionSystem:

    def __init__(self, filePath, faceDetectionFile, camera, frame1, face ):
        self.File = filePath
        self.faceDetect = faceDetectionFile
        self.cam = camera
        self.fr = frame
        self.fc = face


    #pathing required file

    def filePathing(self, requiredFile = '"haarcascade_frontalface_default.xml"'):
        self.__File = requiredFile

    #assigning required file

    def faceDetectionFileAssigning(self, faceDetect):
        self.__File = faceDetect

    def cameraTurnOn(self, cameraTurningOn = cv2.VideoCapture(1)):
        self.__cam = cameraTurningOn

    def cameraReading(self, something, something2 = ret, frame):
        self.__cam = something2.

    def frameSetUp(self, framing):
        self.__fr = framing

def main():
    startProgram = FaceDetectionSystem()

while True:
    if not CameraTurnOn.isOpened():
        print('No camera is loaded up')
        sleep(5)
        pass

    # Capture frame-by-frame
    ret, frame = CameraTurnOn.read()

    faces = FaceDetectionSys.detectMultiScale(
        frame,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(20, 30)
    )

    # Draw a rectangle around the faces
    for (top, bottom, left, right) in faces:
        cv2.rectangle(frame, (top, bottom), (top+left, bottom+right), (255, 255, 255), 2)


    # Display the resulting frame
    cv2.imshow('Video', frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Display the resulting frame
    cv2.imshow('Video', frame)

# When everything is done, release the capture
CameraTurnOn.release()
cv2.destroyAllWindows()