import cv2
import numpy as np
#  Lecture d’une vidéo capture avec le camera de laptop
#cap = cv2.VideoCapture(0)
# Lecture d’une vidéo enregistrer sur le disque dur
cap = cv2.VideoCapture('video.mp4')

n = 10  # nomber d'image pris pour faire la moyenne
Img_List = []

_,im = cap.read()
width,height,_ = im.shape

for _ in range(n):
    _,background = cap.read()
    background = cv2.cvtColor(background, cv2.COLOR_RGB2GRAY)
    background = cv2.GaussianBlur(background,(5,5),0)
    Img_List.append(background)

while cap.isOpened():
    # lire le video image par image 
    ret, img = cap.read()
    if img is None:
        break
    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.GaussianBlur(img,(5,5),0)
    
    #convertir le tableau vers ArrayList
    matrix = np.array(Img_List)
    # Take the median over the first dim
    Background = np.median(matrix, axis=0).reshape(width, height).astype('uint8')
      
    for i in range(n-1):    # Ecrasi l'img avec l'img suivant
        Img_List[i]=Img_List[i+1]
    Img_List[n-1]=img # Ajouter la novel img a la fin du tableau
    
    # faire le seuiage globale
    frame_diff = cv2.absdiff(img,Background)
    _,frame_diff = cv2.threshold(frame_diff,25,255,cv2.THRESH_BINARY)
        
    img = cv2.resize(img, dsize=None, fx=0.35, fy=0.35)
    Background = cv2.resize(Background, dsize=None, fx=0.35, fy=0.35)
    frame_diff = cv2.resize(frame_diff, dsize=None, fx=0.35, fy=0.35)
    cv2.moveWindow('The Original Frame',1,100)
    cv2.moveWindow('Background Median Filter',450,100)  
    cv2.moveWindow('Median Filter',900,100)
    
#    affichier l'image dans une frame a chaque instance
    cv2.imshow("The Original Frame", img)
    cv2.imshow("Background Median Filter", Background)
    cv2.imshow("Median Filter", frame_diff)
    
#   key listener sur le clavier a chaq 20 mili segonde
    key = cv2.waitKey(20) 
    if key == 27: # hadi hiyya Esc
        cap.release()
        cv2.destroyAllWindows()
        break
cap.release()
cv2.destroyAllWindows()