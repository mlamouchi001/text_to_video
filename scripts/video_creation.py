from moviepy.editor import ImageClip, concatenate_videoclips, AudioFileClip


def create_video(image_paths, audio_path, video_output_path):
    clips = []

    for image_path in image_paths:
        # Créer une vidéo clip pour chaque image
        img_clip = ImageClip(image_path).set_duration(5)  # 5 secondes par image
        clips.append(img_clip)

    # Combiner tous les clips en une seule vidéo
    video = concatenate_videoclips(clips, method="compose")

    # Ajouter l'audio
    audio = AudioFileClip(audio_path)
    video = video.set_audio(audio)

    # Exporter la vidéo finale
    video.write_videofile(video_output_path, fps=24)
