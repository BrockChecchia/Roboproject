import cv2 as cv

face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")

cap = cv.VideoCapture("Face-Cap-4.mp4")

while cap.isOpened():
    _, frame = cap.read()
    gray_img = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    face_detect = face_cascade.detectMultiScale(gray_img, 1.1, 4)

    for (x, y, w, h) in face_detect:
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), thickness=3)

        cv.imshow("Frame", frame)

    if cv.waitKey(1) & 0xFF == ord("e"):
        break

cap.release()
cv.destroyAllWindows()