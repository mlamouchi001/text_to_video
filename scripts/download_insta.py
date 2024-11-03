import instaloader

def download_instagram_video(video_url, output_path, username, password):
    # Créer une instance d'Instaloader
    loader = instaloader.Instaloader()

    # Se connecter avec les identifiants Instagram
    try:
        loader.login(username, password)
    except instaloader.exceptions.BadCredentialsException:
        print("Erreur : Identifiants incorrects")
        return
    except instaloader.exceptions.TwoFactorAuthRequiredException:
        print("Erreur : Authentification à deux facteurs requise")
        return

    # Extraire le shortcode de l'URL de la vidéo
    shortcode = video_url.split('/')[-2]

    # Télécharger la vidéo
    try:
        post = instaloader.Post.from_shortcode(loader.context, shortcode)
        loader.download_post(post, target=output_path)
        print(f"Vidéo téléchargée avec succès : {output_path}")
    except Exception as e:
        print(f"Erreur lors du téléchargement de la vidéo : {e}")

# Exemple d'utilisation
video_url = 'https://www.instagram.com/reel/DBBgRWiIltE/?igsh=MTUzZWh2YWQ3eG55cw=='
output_path = 'output/instagram_video'
username = 'votre_nom_utilisateur'
password = 'votre_mot_de_passe'
download_instagram_video(video_url, output_path, username, password)