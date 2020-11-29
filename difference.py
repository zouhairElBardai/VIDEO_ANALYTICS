import cv2
#Lecture d’une vidéo capture avec le camera de laptop
video = cv2.VideoCapture(0)
# Lecture d’une vidéo enregistrer sur le disque dur
#video = cv2.VideoCapture('video.mp4')
#lecture l'image d'arrière-plan 
_,background = video.read()
background = cv2.cvtColor(background, cv2.COLOR_BGR2GRAY)

while video.isOpened():
    # lire le video image par image 
    ret, img = video.read()
    if img is None:
        break
    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
# la différence prise de l'image actuelle et de l'image précédente
    mask = cv2.absdiff(img, background)
    
    # faire le seuillage globale
    ret,mask = cv2.threshold(mask,25,255,cv2.THRESH_BINARY) 
    
    backgroud=img
    
    img = cv2.resize(img, dsize=None, fx=0.5, fy=0.5)  
    mask = cv2.resize(mask, dsize=None, fx=0.5, fy=0.5)
    #l'afichage des videos
    cv2.imshow("image",img)
    cv2.imshow("Différentes d'images", mask)
    
    key = cv2.waitKey(40) 
    if key == 'q': 
        break
        
video.release()
cv2.destroyAllWindows()