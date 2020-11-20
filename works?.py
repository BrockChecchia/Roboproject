import cv2
from matplotlib import pyplot as plt

eye_cascade = cv2.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)
im2 = Image.open("/content/drive/My Drive/Colab Notebooks/eye2.png").convert('RGBA')
while cap.isOpened():
    _, frame = cap.read()
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    eye_detect = eye_cascade.detectMultiScale(gray_img)
    face_detect = face_cascade.detectMultiScale(gray_img,1.1,4)
    im2 = Image.open("/content/drive/My Drive/Colab Notebooks/eye2.png").convert('RGBA')
    ## Resize Image on Left Eye Size using width and height
    new_image = im2.resize((eyes[[0], [2]], eyes[[0], [3]]))
    ## Resize Image on Right Eye Size
    new_image2 = im2.resize((eyes[[1], [2]], eyes[[1], [3]]))
    ## Left Eye Pasted at x = eye 0,0 and y = eyes 0,1
    back_im.paste(new_image, (eyes[[0], [0]], eyes[[0], [1]]), mask=new_image)
    ## Right Eye Pasted
    back_im.paste(new_image2, (eyes[[1], [0]], eyes[[1], [1]]), mask=new_image2)
    cv2.imshow("Image", frame)

    if cv2.waitKey(1) & 0xFF == ord("e"):
        break

cap.release()
cv2.destroyAllWindows()
