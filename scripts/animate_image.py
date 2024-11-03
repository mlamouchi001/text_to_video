from moviepy.editor import ImageClip
from moviepy.video.fx.all import resize


def animate_image(image_path, output_path, duration=5):
    # Charger l'image en tant que clip
    clip = ImageClip(image_path)

    # Appliquer un effet de zoom progressif
    def zoom_in(get_frame, t):
        zoom_factor = 1 + 0.1 * t  # Zoom de 10% par seconde
        return resize(get_frame(t), zoom_factor)

    # Appliquer un déplacement latéral (panoramique)
    def move_right(get_frame, t):
        frame = get_frame(t)
        width, height = frame.shape[1], frame.shape[0]
        dx = int(50 * t)  # Déplacement de 50 pixels par seconde
        return frame[:, dx:min(dx + width, frame.shape[1]), :]

    # Durée de la vidéo en secondes
    animated_clip = clip.set_duration(duration)

    # Ajouter un zoom progressif à l'image
    animated_clip = animated_clip.fl(zoom_in)

    # Ajouter un mouvement panoramique vers la droite
    animated_clip = animated_clip.fl(move_right)

    # Exporter la vidéo en fichier mp4
    animated_clip.write_videofile(output_path, fps=24)


# Utiliser le script
image_path = 'images/scene_0.png'
output_path = 'output_animated_image.mp4'
animate_image(image_path, output_path)
