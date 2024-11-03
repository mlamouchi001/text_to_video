import os
import cv2
from scenedetect import VideoManager, SceneManager
from scenedetect.detectors import ContentDetector
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

# Dossier de sortie pour les scènes
OUTPUT_DIR = 'scenes/'

# Vérifie si le dossier de sortie existe, sinon le crée
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# Fonction pour détecter les scènes dans une vidéo
def detect_scenes(video_path):
    # Crée un gestionnaire vidéo
    video_manager = VideoManager([video_path])
    scene_manager = SceneManager()

    # Utilise un détecteur basé sur le contenu pour détecter les scènes
    scene_manager.add_detector(ContentDetector(threshold=40.0))

    # Ouvre la vidéo
    video_manager.start()

    # Détecte les scènes
    scene_manager.detect_scenes(video_manager)
    scene_list = scene_manager.get_scene_list()

    print(f"Nombre de scènes détectées : {len(scene_list)}")
    return scene_list

# Fonction pour générer une vidéo pour chaque scène détectée
def generate_scene_videos(video_path, scene_list):
    for i, scene in enumerate(scene_list):
        start_time = scene[0].get_seconds()
        end_time = scene[1].get_seconds()

        output_file = os.path.join(OUTPUT_DIR, f"scene_{i+1}.mp4")
        ffmpeg_extract_subclip(video_path, start_time, end_time, targetname=output_file)
        print(f"Scène {i+1} exportée : {output_file}")

# Le chemin de la vidéo à traiter
video_path = 'inputes/video.mp4'

# Détecte les scènes
scenes = detect_scenes(video_path)

# Génère une vidéo pour chaque scène détectée
generate_scene_videos(video_path, scenes)
