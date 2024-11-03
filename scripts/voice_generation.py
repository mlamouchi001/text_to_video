from gtts import gTTS

def generate_voice(text, audio_path):
    tts = gTTS(text, lang='en')
    tts.save(audio_path)
