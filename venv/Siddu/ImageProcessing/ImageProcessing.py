import cv2
import os

img = cv2.imread("Kohli.jpg")
# cv2.imshow("box",img)
g_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

x_face = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
face = x_face.detectMultiScale(img, scaleFactor=1.05, minNeighbors=5)

for x,y,w,h in face:
    box_Image = cv2.rectangle(img, (x,y),(x+w,y+h),(255,0,0),3)

# img = cv2.resize(box_Image,(int(box_Image.shape[1]/2),int(box_Image.shape[0]/2)))
print(face)

cv2.imshow("box",img)

cv2.waitKey(0)

#-----------------------------------------------------------------

# faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# imgFormat = ".jpeg"
# fullimgpath = "..\ImageProcessing"
# faceimgpath = "face_image/"
# imfilelist = ["Siddu.jpg","Kohli.jpg"]#[os.path.join(fullimgpath, f) for f in os.listdir(fullimgpath) if f.endswith(imgFormat)]
#
# for el in imfilelist:
#     print (el)
#     imagen = cv2.imread(el)
#     gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
#     faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
#     for (x, y, w, h) in faces:
#         cv2.rectangle(imagen, (x, y), (x + w, y + h), (0, 255, 0), 2)
#         roi_color = imagen[y:y + h, x:x + w]
#
#     cv2.imshow('Imagen', imagen)
#     cv2.waitKey(1000)
