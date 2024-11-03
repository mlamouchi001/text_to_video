import cv2
import numpy as np


def interpolate_frames(image1_path, image2_path, output_path):
    img1 = cv2.imread(image1_path)
    img2 = cv2.imread(image2_path)

    # Création d'une série de frames interpolées entre img1 et img2
    alpha_values = np.linspace(0, 1, num=10)  # 10 frames d'interpolation
    frames = []

    for alpha in alpha_values:
        interpolated_frame = cv2.addWeighted(img1, 1 - alpha, img2, alpha, 0)
        frames.append(interpolated_frame)

    # Enregistrer les frames dans une vidéo
    height, width, layers = frames[0].shape
    video = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'DIVX'), 10, (width, height))

    for frame in frames:
        video.write(frame)

    video.release()
