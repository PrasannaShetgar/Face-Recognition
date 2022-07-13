import cv2
import numpy as np

faceDetect = cv2.CascadeClassifier(r"D:/Face Regonizition/haarcascade_frontalface_default.xml")
cam = cv2.VideoCapture(0)

rec = cv2.face.LBPHFaceRecognizer_create()
rec.read(r"D:/Face Regonizition/recognizer/Trainingdata.yml")
id = 0

while True:
    ret, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray, 1.3, 5)

    for x,y,w,h in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h),(0,255,0),2)
        id, conf = rec.predict(gray[y:y+h,x:x+w])
        print(id, conf)
        if conf < 85:
            if id == 1:
                id = 'Prasanna {:.2f}'.format(conf)
            else:
                id = 'unknown'
                
        else:
            id = 'unknown'
        cv2.rectangle(frame,(x,y-20),(x+100,y),(0,255,0),cv2.FILLED)
        cv2.putText(frame,id,(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1)

    cv2.imshow("FACE",frame)
    if cv2.waitKey(1) == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
