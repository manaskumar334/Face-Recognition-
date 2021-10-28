import cv2
import mediapipe as mp
import face_recognition_models as fc
import  time

cap = cv2.VideoCapture(0)
mpface = mp.solutions.face_detection
face = mpface.FaceDetection()
mpDraw = mp.solutions.drawing_utils
cTime

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    cv2.imshow("Video", img)
    cv2.waitKey(1)
