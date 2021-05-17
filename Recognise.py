import cv2
import numpy as np;
import xlwrite
import firebase_admin
import time
import sys

start = time.time()
period = 80
face_cas = cv2.CascadeClassifier(
    r'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0);
recognizer = cv2.face.LBPHFaceRecognizer_create();
recognizer.read(r'Recogniser\trainer.yml');
flag = 0;
id = 0;
filename = 'xlwrite.py';
dict = {
    'item1': 1
}

font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    ret, img = cap.read();
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
    faces = face_cas.detectMultiScale(gray, 1.3, 7);
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2);
        id, conf = recognizer.predict(roi_gray)
        if (id == 79):
                id = 'Kiran Kumar M K'
                if ((str(id)) not in dict):
                    filename = xlwrite.output('attendance', 'class1', 1, id, 'Present', "79");
                    dict[str(id)] = str(id);

        elif (id == 36):
                id = 'Charitra'
                if ((str(id)) not in dict):
                    filename = xlwrite.output('attendance', 'class1', 2, id, 'Present', "36");
                    dict[str(id)] = str(id);

        elif (id == 1):
                id = 'Hemalatha M K'
                if ((str(id)) not in dict):
                    filename = xlwrite.output('attendance', 'class1', 3, id, 'Present', "1");
                    dict[str(id)] = str(id)

        elif (id == 3):
                id = 'Manjulamma H R'
                if ((str(id)) not in dict):
                    filename = xlwrite.output('attendance', 'class1', 4, id, 'Present', "3");
                    dict[str(id)] = str(id)

        elif (id == 6):
                id = 'Karibasavaiah H M'
                if ((str(id)) not in dict):
                    filename = xlwrite.output('attendance', 'class1', 5, id, 'Present', "6");
                    dict[str(id)] = str(id)

        cv2.putText(img, str(id) + " " + str(conf), (x, y - 10), font, 0.55, (120, 255, 120), 1)
        # cv2.cv.PutText(cv2.cv.fromarray(img),str(id),(x,y+h),font,(0,0,255));
    cv2.imshow('frame', img);


    if time.time() > start + period:
        break;
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break;

print("[INFO]: The Attendnce is Taken!!")

cap.release();
cv2.destroyAllWindows();
