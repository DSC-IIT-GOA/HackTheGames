import cv2
from cvzone.HandTrackingModule import HandDetector
import time
import pyautogui                  
    
detector = HandDetector(detectionCon=0.8, maxHands=1)

time.sleep(2.0)

video = cv2.VideoCapture(0)

prev_key = "nothing"

while True:
    ret, frame = video.read()
    video.set(cv2.CAP_PROP_FRAME_WIDTH, 1000)
    video.set(cv2.CAP_PROP_FRAME_HEIGHT, 2000)
    hands, img = detector.findHands(frame)
    cv2.rectangle(img, (0, 480), (300, 425), (50, 50, 255), -2)
    cv2.rectangle(img, (640, 480), (400, 425), (50, 50, 255), -2)
    if hands:
        lmList = hands[0]
        fingerUp = detector.fingersUp(lmList)
        
        if fingerUp == [1, 1, 1, 1, 1]:
            cv2.putText(frame, 'Right Direction', (20, 460),
            cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
            cv2.LINE_AA)
            cv2.putText(frame, 'Accelerator', (420, 460),
            cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
            cv2.LINE_AA)
            
            if(prev_key == "left"):
                pyautogui.keyUp('left')
                prev_key = "right"
                
            pyautogui.keyDown('right')
            prev_key = "right"
        
        if fingerUp == [0, 0, 0, 0, 0]:
            cv2.putText(frame, 'Left Direction', (20, 460),
            cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
            cv2.LINE_AA)
            cv2.putText(frame, 'Reverse', (420, 460),
            cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
            cv2.LINE_AA)
            
            if(prev_key == "right"):
                pyautogui.keyUp('right')
                prev_key = "left"
                
            pyautogui.keyDown('left')
            prev_key = "left"
            
        if(0 < sum(fingerUp) < 5):
            cv2.putText(frame, 'Nothing', (20, 460),
            cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
            cv2.LINE_AA)
            cv2.putText(frame, 'No action', (420, 460),
            cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
            cv2.LINE_AA)
            
            if(prev_key == "right"):
                pyautogui.keyUp('right')
                prev_key = "nothing"
                
            if(prev_key == "left"):
                pyautogui.keyUp('left')
                prev_key = "nothing"
    
    cv2.imshow("frame", frame)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
