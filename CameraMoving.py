import time
import cv2
import serial
import math

arduinoSerial = serial.Serial('COM3', 115200, timeout=2)
print(arduinoSerial.readline())

previousX = 240
previousY = 320

minXX = 0
minYY = 0

def detect_faces(cascade, test_image, scaleFactor=1.5):
    global previousX, previousY, minXX, minYY

    image_copy = test_image.copy()

    # convert the test image to gray scale as opencv face detector expects gray images
    gray_image = cv2.cvtColor(image_copy, cv2.COLOR_BGR2GRAY)

    # Applying the haar classifier to detect faces
    facesDetected = cascade.detectMultiScale(gray_image, scaleFactor, minNeighbors=5)

    minimumdistance = 800

    if len(facesDetected) != 0:
        print(facesDetected)
        for (x, y, w, h) in facesDetected:

            cv2.rectangle(image_copy, (x, y), (x + w, y + h), (0, 255, 100), 5)

            # Center of the rectangle
            cv2.line(image_copy, (x + int(1 / 2 * w), y + int(1 / 2 * h)), (x + int(1 / 2 * w), y + int(1 / 2 * h)),
                     (0, 0, 255), 7)

            xx = x + int(1 / 2 * w)
            yy = y + int(1 / 2 * h)
            """
            print(xx, yy, previousX, previousY)
            if xx - 20 > previousX and yy - 20 > previousY:
                print('break')
                break
            distance = math.sqrt(((xx - previousX) ** 2) + ((previousY - yy) ** 2))

            if distance < minimumdistance:
                minXX = xx
                minYY = yy
                minimumdistance = distance

            minimumdistance = min(minimumdistance, distance)
            previousX = xx
            previousY = yy
            """
        serialOutput = "X{0:d}Y{1:d}".format(xx, yy)
        arduinoSerial.write(str.encode(serialOutput))
    else:
        arduinoSerial.write(str.encode('L'))
        print("nothing detected")
    return image_copy


def main():
    userInput = input("Do you want to use potentiometer or intelligent camera; "
                      "Type I for intelligent camera; Type P for potentiometer")

    if userInput == 'I' or userInput == 'i':

        cv2.namedWindow("videoWindow")
        cv2.moveWindow("videoWindow", 0, 0)
        videoCapture = cv2.VideoCapture(1)

        frameWidth = int(videoCapture.get(3))
        frameHeight = int(videoCapture.get(4))
        print(frameHeight, 'x', frameWidth)

        haar_cascade_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        # Read until video is completed
        while (videoCapture.isOpened()):
            time.sleep(0.01)
            # Capture frame-by-frame
            ret, frame = videoCapture.read()
            if ret == True:

                # Display the resulting frame
                frameFaceDetect = detect_faces(haar_cascade_face, frame)

                cv2.imshow('videoWindow', frameFaceDetect)

                # Press Q on keyboard to  exit
                if cv2.waitKey(33) & 0xFF == ord('q'):
                    arduinoSerial.write(str.encode('q'))
                    break

            # Break the loop
            else:
                break

        # When everything done, release the video video capture object and the output
        videoCapture.release()

        # Closes all the frames
        cv2.destroyAllWindows()

    elif userInput == 'P' or userInput == 'p':
        while True:
            arduinoSerial.write(str.encode('P'))


# Calling the main function
main()
