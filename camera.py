import cv2

class Camera:

    def __init__(self, cameraNumber, path='haarcascade_frontalface_default.xml', window='videoWindow'):
        self.videoCapture = cv2.VideoCapture(cameraNumber)
        self.pathXML = path
        self.classfier = cv2.CascadeClassifier(self.pathXML)
        self.window = window
        cv2.namedWindow(self.window)
        cv2.moveWindow(self.window, 0, 0)

    def getCameraFrame(self):
        boolReturn, frame = self.videoCapture.read()
        return boolReturn, frame

    def showFrame(self, frame):
        cv2.imshow(self.window, frame)

    def cleanup(self):
        self.videoCapture.release()
        cv2.destroyAllWindows()

    def detectFaces(self, frame):
        # global previousX, previousY, minXX, minYY

        cascade = self.classfier
        imageCopy = frame.copy()

        # convert the test image to gray scale as opencv face detector expects gray images
        grayImage = cv2.cvtColor(imageCopy, cv2.COLOR_BGR2GRAY)

        # Applying the haar classifier to detect faces
        facesDetected = cascade.detectMultiScale(grayImage, scaleFactor = 1.5, minNeighbors = 5)

        centers = []

        if len(facesDetected) != 0:
            #print(facesDetected)
            for (x, y, w, h) in facesDetected:
                cv2.rectangle(imageCopy, (x, y), (x + w, y + h), (0, 255, 100), 5)

                # Center of the rectangle
                cv2.line(imageCopy, (x + int(1 / 2 * w), y + int(1 / 2 * h)), (x + int(1 / 2 * w), y + int(1 / 2 * h)),
                         (0, 0, 255), 7)

                xx = x + int(1 / 2 * w)
                yy = y + int(1 / 2 * h)
                centers.append((xx, yy))

        return imageCopy, centers

