import cv2
import numpy as np
#  Lecture d’une vidéo capture avec le camera de laptop
cap = cv2.VideoCapture(0)
# Lecture d’une vidéo enregistrer sur le disque dur
#cap = cv2.VideoCapture('video.mp4')

n = 50  # nomber d'image pris pour faire la moyenne
List = []

# l'apprentissage initiale
for _ in range(n):
    _,background = cap.read()
    background = cv2.cvtColor(background, cv2.COLOR_RGB2GRAY)
    background = cv2.GaussianBlur(background,(5,5),0)
    List.append(background)

while cap.isOpened():
    # lire le video image par image 
    ret, img = cap.read()
    if img is None:
        break
    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.GaussianBlur(img,(5,5),0)
    
    #convertir le tableau vers ArrayList
    arrayList = np.array(List)
    
    Background = arrayList.mean(0).astype('uint8')

    for i in range(n-1):    # Ecrasi l'img avec l'img suivant
        List[i] = List[i+1]
    List[n-1]=img # Ajouter la novel img a la fin du tableau
    
    frame_diff = cv2.absdiff(img,Background)
    # faire le seuillage globale
    _,frame_diff = cv2.threshold(frame_diff,20,255,cv2.THRESH_BINARY) 
        
    img = cv2.resize(img, dsize=None, fx=0.40, fy=0.40)
    Background = cv2.resize(Background, dsize=None, fx=0.40, fy=0.40)
    frame_diff = cv2.resize(frame_diff, dsize=None, fx=0.40, fy=0.40)
    cv2.moveWindow('Frame',1,100)
    cv2.moveWindow('Background Mean Filter',450,100)   
    cv2.moveWindow('Mean Filter',900,100)
    
#affichier les image dans des frames a chaque instance
    cv2.imshow("Frame", img)
    cv2.imshow("Background Mean Filter", Background)
    cv2.imshow("Mean Filter", frame_diff)
    
    
    key=cv2.waitKey(1)&0xFF
    if key==ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()