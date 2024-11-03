import cv2
import numpy as np
from moviepy.editor import VideoFileClip

def remove_text_from_video(input_video_path, output_video_path):
    # Ouvrir la vidéo d'entrée
    cap = cv2.VideoCapture(input_video_path)
    if not cap.isOpened():
        print("Erreur lors de l'ouverture de la vidéo")
        return

    # Obtenir les propriétés de la vidéo
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Créer un writer pour la vidéo de sortie
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Convertir l'image en niveaux de gris
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Appliquer un seuillage adaptatif pour détecter le texte
        thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

        # Trouver les contours du texte
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Remplir les contours détectés avec du blanc
        for contour in contours:
            cv2.drawContours(frame, [contour], -1, (255, 255, 255), thickness=cv2.FILLED)

        # Écrire la frame traitée dans la vidéo de sortie
        out.write(frame)

    # Libérer les ressources
    cap.release()
    out.release()
    cv2.destroyAllWindows()

    # Exemple d'utilisation
    input_video_path = 'inputes/LaFerrari.mp4'
    output_video_path = 'output/video_without_text.mp4'
    remove_text_from_video(input_video_path, output_video_path)


# Exemple d'utilisation
input_video_path = 'inputes/video.mp4'
output_video_path = 'output/video_without_text.mp4'
remove_text_from_video(input_video_path, output_video_path)