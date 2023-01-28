import pathlib
import cv2

cascade_path = pathlib.Path(__file__).parent / "./haarcascade_frontalface_default.xml"

clf = cv2.CascadeClassifier(str(cascade_path))

camera = cv2.VideoCapture(0)

while True:
        _, frame = camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = clf.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE
        )

        
        face_found = False   #---Initially set the flag to be False
        for (x, y, w, h) in faces:                #--- Set the flag True if w>0 (i.e, if face is detected)
                face_found = True
                
                cv2.rectangle(frame, (x, y), (x + w, y + h), (36,255,12), 1)
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame, 'Person', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1)

        cv2.imshow("Face Detection | Press q to quit", frame)
        cv2.addText
        if cv2.waitKey(1) == ord('q'):
                break



camera.release()
cv2.destroyAllWindows()