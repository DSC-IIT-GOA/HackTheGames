import cv2
from cvzone.HandTrackingModule import HandDetector
import time

detector = HandDetector(detectionCon=0.8, maxHands=1)
time.sleep(2.0)
video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    video.set(cv2.CAP_PROP_FRAME_WIDTH, 1000)
    video.set(cv2.CAP_PROP_FRAME_HEIGHT, 3000)
    cv2.rectangle(img, (0, 480), (300, 425), (50, 50, 255), -2)
    cv2.rectangle(img, (640, 480), (400, 425), (50, 50, 255), -2)
    cv2.imshow("frame", frame)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
