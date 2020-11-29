# VIDEO_ANALYTICS
Détection des objets mobiles • Modélisation de l’arrière-plan • Soustraction de l’arrière-plan

En utilisant une vidéo enregistrée sur le disque dur ou capture à partir d’une web Cam.

simple.py : réaliser une segmentation avant-plan/arrière-plan par la méthode approches simples, on utilise la bibliothèque openCV.

difference.py : réaliser une segmentation avant-plan/arrière-plan par la méthode différence d’images, j'améliorerai le code de méthode approches simples et j'initialiserai la variable background « c’est l’arrière-plan à l’instant t: 𝑩(𝒙,𝒚,𝒕) =I(x, y, t−1) » par le premier frame de la vidéo et dans la boucle while j'ajouterai backgroud=img .

mean_Filter.py : dans le cas de filtre moyen, l’arrière-plan est la moyenne des anciennes n images (frames). Pour ça, j'initialiserai la liste List par n images pour calculer l’arrière-plan. J’utilisai arrayList.mean(0).astype('uint8') pour calculer la moyenne des images pixel par pixel et l’intervalle de chaque pixel entre 0 et 255 (uint8).

median_Filter.py : dans le cas de filtre médian, on le même code de filtre moyen je changerai la fonction arrayList.mean(0).astype('uint8') à np.median(matrix, axis=0).reshape(width, height).astype('uint8') pour calculer le Background.

MOG_MOG2_GMG.py : Réaliser une segmentation avantplan/arrièreplan en utilisant la méthode MOG, MOG2, GMG.

flot_optique_deux_frames.py : Extraire deux frames à l’instant t et t+1. Calculer le flot optique à base de ces deux frames.

flot_optique_video.py : le flot optique en temps réel en se basant sur des frames prises au bout des laps du temps.
