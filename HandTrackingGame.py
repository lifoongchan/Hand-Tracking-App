import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm

pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)
detector = htm.handDetector()
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img)
    if len(lmList) != 0:
        userfind = int(input("Enter a point: "))
        print(lmList[userfind])

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
