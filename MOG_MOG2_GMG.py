# importation de bibliothèques
import cv2
from matplotlib import pyplot as plt

# capturer des images à partir d'une caméra ou d'une vidéo
#cap = cv2.VideoCapture('vedio.mp4')
cap = cv2.VideoCapture(0)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))

# création des objets
fgbg_MOG = cv2.bgsegm.createBackgroundSubtractorMOG()
fgbg_GMG = cv2.bgsegm.createBackgroundSubtractorGMG()
fgbg_MOG2 = cv2.createBackgroundSubtractorMOG2(detectShadows=True)

# Définissez le codec et créez des objets VideoWriter
#fourcc = cv2.VideoWriter_fourcc(*'FMP4')
#out_MOG = cv2.VideoWriter('./video/out_MOG_v1.mp4', fourcc, 20.0, (1920,1080))
#out_original = cv2.VideoWriter('./video/out_original_v1.mp4', fourcc, 20.0, (1920,1080))
#out_MOG2 = cv2.VideoWriter('./video/out_MOG2_v1.mp4', fourcc, 20.0, (1920,1080))
#out_GMG = cv2.VideoWriter('./video/out_GMG_v1.mp4', fourcc, 20.0, (1920,1080))

while True:
    ret, frame = cap.read()
    
    if frame is None:
        break
    # appliquer mask pour la soustraction d'arrière-plan
    fgmask_MOG = fgbg_MOG.apply(frame)
    fgmask_GMG = fgbg_GMG.apply(frame)
    fgmask_MOG2 = fgbg_MOG2.apply(frame)
    
    fgmask_MOG2 = cv2.morphologyEx(fgmask_MOG2, cv2.MORPH_OPEN, kernel)
   
    #Écriture dans les fichiers de sortie
#    out_original.write(frame)
#    out_MOG.write(fgmask_MOG)
#    out_GMG.write(fgmask_GMG)
#    out_MOG2.write(fgmask_MOG2)
    
    # l'affichage sur console
#    plt.subplot(221),plt.imshow(frame),plt.title('Original')
#    plt.subplot(222),plt.imshow(fgmask_MOG),plt.title('fgmask_MOG')
#    plt.subplot(223),plt.imshow(fgmask_GMG),plt.title('fgmask_GMG')
#    plt.subplot(224),plt.imshow(fgmask_MOG2),plt.title('fgmask_MOG2')
#    plt.show()
    
    frame = cv2.resize(frame, dsize=None, fx=0.5, fy=0.5)
    cv2.moveWindow('Frame',10,0)
    
    fgmask_MOG = cv2.resize(fgmask_MOG, dsize=None, fx=0.5, fy=0.5)
    cv2.moveWindow('fgmask_MOG',690,0)
    
    fgmask_GMG = cv2.resize(fgmask_GMG, dsize=None, fx=0.5, fy=0.5)
    cv2.moveWindow('fgmask_GMG',10,350)
    
    fgmask_MOG2 = cv2.resize(fgmask_MOG2, dsize=None, fx=0.5, fy=0.5)
    cv2.moveWindow('fgmask_MOG2',700,350)
    
    #affichage
    cv2.imshow('Frame', frame)
    cv2.imshow('fgmask_MOG', fgmask_MOG)
    cv2.imshow('fgmask_GMG', fgmask_GMG)
    cv2.imshow('fgmask_MOG2', fgmask_MOG2)

    keyboard = cv2.waitKey(1)
    #Quitter lorsque Q est enfoncé
    if keyboard == 'q' or keyboard == 27:
        break
cap.release()
cv2.destroyAllWindows()